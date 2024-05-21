import scrapy
from unidecode import unidecode
from datetime import date, timedelta, datetime

class ShuttleSpider(scrapy.Spider):
    name = "shuttle"
    allowed_domains = ["vexere.com"]
    start_urls = ["https://vexere.com/vi-VN"]



    def start_requests(self):
        f = open("./codeCity.txt", "r",  encoding="utf8")
        lstCityStart  = f.readlines()
        f = open("./codeCity1.txt", "r",  encoding="utf8")
        lstCityEnd    = f.readlines()

        for i in lstCityStart:
            cityStart , codeStart   = i.split(',')
            cityStartName = cityStart
            cityStart = unidecode(cityStart.strip()).lower().replace(' ', '-')
        for j in lstCityEnd:
            cityEnd , codeEnd = j.split(',')
            cityEndName = cityEnd
            cityEnd = unidecode(cityEnd.strip()).lower().replace(' ', '-')
            if cityEnd != cityStart:
                ## today ---> 30 date 
                datePlan = datetime.now() + timedelta(days=7)
                datePlan = datePlan.strftime("%d-%m-%Y")
                url =   f'https://vexere.com/vi-VN/ve-xe-khach-tu-{cityStart}-di-{cityEnd}-{codeStart}t{codeEnd}1.html?date={datePlan}&sort=fare%3Aasc&v=5'
                yield scrapy.Request(url= url , callback=self.parse_detail , cb_kwargs={ "cityStartName": cityStartName , "cityEndName": cityEndName , "datePlan" : datePlan  })

    def parse_detail(self, response,  cityStartName ,  cityEndName ,  datePlan):
        priceLowest = ''
        nameBus = ''
        durationBus = ''
        try:
            priceLowest = response.css('div.fare-sale')
            priceLowest = priceLowest.css('div::text').get()
            if priceLowest == None:
                priceLowest = response.css('div.fare')
                priceLowest = priceLowest.css('div::text').get()
            nameBus   = response.css('div.bus-name::text').get()
            durationBus = response.css('div.duration::text').get()

        except:
            pass

        yield {
            "cityStartName": cityStartName ,
            "cityEndName": cityEndName ,
            "priceLowest" : priceLowest,
            "nameBus" : nameBus,
            "durationBus" : durationBus
        }


