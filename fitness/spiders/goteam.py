from urllib import response
from fsspec import Callback
import scrapy
from ..items import FitnessItem


class ExampleSpider(scrapy.Spider):
    name = "goteam"
    page_range = (10 ** 5, 10 ** 9)
    base_url = f"https://goteamup.com"
    # allowed_domains = ['example.com']
    start_urls = [
        "https://goteamup.com/p/1003249-ruth-partington-pilates/",
        "https://goteamup.com/p/1007856-m-squared-fitness-ltd/",
        "https://goteamup.com/p/1008791-crossfit-ludwigsburg/",
        "https://goteamup.com/p/1010842-365motivate/",
        "https://goteamup.com/p/1011481-club-deportivo-smonker-te/",
        "https://goteamup.com/p/1011962-talbot-fitness/",
        "https://goteamup.com/p/1013494-the-strength-circuit/",
        "https://goteamup.com/p/1014787-kugb/",
        "https://goteamup.com/p/1016639-entrenatt/",
        "https://goteamup.com/p/1018077-crossfit-weinstrasse-cros/",
        "https://goteamup.com/p/1020157-spin-city-exeter/",
        "https://goteamup.com/p/1020493-zumba-nxg/",
        "https://goteamup.com/p/1020390-just-fit/",
        "https://goteamup.com/p/1021156-function1fitness/",
        "https://goteamup.com/p/1022151-imagine-technologies/",
        "https://goteamup.com/p/1022670-supercharged-club/",
        "https://goteamup.com/p/1024717-aspentuck1/",
        "https://goteamup.com/p/1026051-jolly-llama-yoga/",
        "https://goteamup.com/p/1027649-shin-ghi-tai/",
        "https://goteamup.com/p/1028488-rene-ferguson-strength-pe/",
        "https://goteamup.com/p/1028265-crossfit-buxton/",
        "https://goteamup.com/p/1028382-studio-boutique/",
        "https://goteamup.com/p/1030940-fortitude-health-and-perf/",
        "https://goteamup.com/p/1031579-box-callero-crossfit-tima/",
        "https://goteamup.com/p/1032743-swift-fitness-hilly-field/",
        "https://goteamup.com/p/1033510-fitness-lab-birkdale/",
        "https://goteamup.com/p/1033620-farnham-pilates/",
        "https://goteamup.com/p/1034342-triswim/",
        "https://goteamup.com/p/1034444-hotpod-yoga-derby-and-bur/",
        "https://goteamup.com/p/1034650-kikipilates/",
        "https://goteamup.com/p/1034086-body-up/",
        "https://goteamup.com/p/1035384-parkour-austria/",
        "https://goteamup.com/p/1035247-courageous-impact/",
        "https://goteamup.com/p/1035903-triple-x-personal-trainin/",
        "https://goteamup.com/p/1035587-swift-fitness-highbury/",
        "https://goteamup.com/p/1036641-hotpod-yoga-newcastle/",
        "https://goteamup.com/p/1038492-active-body-collective-lo/",
        "https://goteamup.com/p/1038681-team-aubin-lacrosse/",
        "https://goteamup.com/p/1039833-fettle/",
        "https://goteamup.com/p/1040216-cube-north-east-olympic-w/",
        "https://goteamup.com/p/1041355-leesa-vain-dance-academy/",
        "https://goteamup.com/p/1041838-hurley-fitness/",
        "https://goteamup.com/p/1042194-didi-rugby-uk-twickenham/",
        "https://goteamup.com/p/1042372-girls-allowed-gyms/",
        "https://goteamup.com/p/1042582-jersey-crossfit/",
        "https://goteamup.com/p/1043745-flow-performance-and-well/",
        "https://goteamup.com/p/1046897-the-fitness-link/",
        "https://goteamup.com/p/1046927-fit-fusion/",
        "https://goteamup.com/p/1047377-wave-brazilian-jiu-jitsu-/",
        "https://goteamup.com/p/1047616-hotpod-yoga-dummy/",
        "https://goteamup.com/p/1048543-coventry-pilates-studio/",
        "https://goteamup.com/p/1048736-demo/",
        "https://goteamup.com/p/1049642-ldn-fitness/",
        "https://goteamup.com/p/1052212-runpainfree/",
        "https://goteamup.com/p/1053071-shoheb/",
        "https://goteamup.com/p/1055308-crossfit-antipolis/",
        "https://goteamup.com/p/1058933-pilatesbody4u/",
        "https://goteamup.com/p/1059755-eskrimamadrid/",
        "https://goteamup.com/p/1060089-mycore-pilates/",
        "https://goteamup.com/p/1060105-lifestyle-and-more/",
        "https://goteamup.com/p/1062132-crossfit-ballincollig/",
        "https://goteamup.com/p/1062800-lifestyle-fitness-plus/",
        "https://goteamup.com/p/1064274-vertigo-climbing/",
        "https://goteamup.com/p/1064377-putton-mill-fitness-centr/",
        "https://goteamup.com/p/1065615-vip-fitness/",
        "https://goteamup.com/p/1067414-ss-training/",
        "https://goteamup.com/p/1068062-elite-conditioning/",
        "https://goteamup.com/p/1070117-male/",
        "https://goteamup.com/p/1070420-forever-strong-fitness-bu/",
        "https://goteamup.com/p/1070588-defence-lab-bangkok/",
        "https://goteamup.com/p/1070388-thrive-training-club/",
        "https://goteamup.com/p/1070889-the-fitness-hub/",
        "https://goteamup.com/p/1070857-ctc-fitness/",
        "https://goteamup.com/p/1071034-phalanx/",
        "https://goteamup.com/p/1071083-right-balance-fitness/",
        "https://goteamup.com/p/1072205-the-yoga-lighthouse/",
        "https://goteamup.com/p/1072180-seans-fitness-studio/",
        "https://goteamup.com/p/1073549-fitnessflex-farnborough/",
        "https://goteamup.com/p/1073693-cssh/",
        "https://goteamup.com/p/1073936-mama-wellness/",
        "https://goteamup.com/p/1074422-heyl-crossfit/",
        "https://goteamup.com/p/1075107-champion-london-limited/",
        "https://goteamup.com/p/1076801-westend-workouts/",
        "https://goteamup.com/p/1078105-lakshmi-yoga/",
        "https://goteamup.com/p/1079191-fitprohqcom/",
        "https://goteamup.com/p/1079494-taurus/",
        "https://goteamup.com/p/1080026-shadowparkour/",
        "https://goteamup.com/p/1080566-sm9-fitness/",
        "https://goteamup.com/p/1081613-mama-wellness/",
        "https://goteamup.com/p/1081567-stretch2health/",
        "https://goteamup.com/p/1082608-dante-languages/",
        "https://goteamup.com/p/1083475-brancoeda/",
        "https://goteamup.com/p/1085378-boogie-bounce-dublin-24/",
        "https://goteamup.com/p/1086863-boogie-bounce-with-lucy/",
        "https://goteamup.com/p/1086866-boogie-bounce-with-norma-/",
        "https://goteamup.com/p/1087525-crossfit-hartlepool/",
        "https://goteamup.com/p/1092057-fitness-company/",
        "https://goteamup.com/p/1091929-mathouse-bjj-reading/",
        "https://goteamup.com/p/1092656-tfd-lifestyle-pt/",
    ]

    # def start_requests(self):
    #     # urls = [
    #     # https://goteamup.com/p/3715633
    #     # ]
    #     for number in range(self.page_range[0], self.page_range[1]):
    #         url = f"{self.base_url}/p/{number}"
    #         yield scrapy.Request(url=url, callback=self.parse)
    #         # if str(num) in existing_numbers:
    #         #     print("repeated link")
    #         #     # pass

    def parse_contact(self, response):
        contact_info = FitnessItem()
        contact_info["url"] = response.url
        contact_info["email"] = response.xpath("//p/a/text()").get()

        contact_info["phone"] = "".join(
            response.xpath(
                '//p[preceding-sibling::h2["Phone"] and following-sibling::h2["Address"]]/text()'
            ).getall()
        ).strip()

        contact_info["address"] = "".join(
            response.xpath("//p[3]/text()").getall()
        ).strip()

        yield contact_info
        # yield {"url": url, "email": email, "phone": phone, "address": address}

    def parse(self, response):

        try:
            check_page = response.css("h1::text").extract()[0]
        except:
            check_page = "found page"

        if check_page != "Page Not Found":
            contact_sub_url = response.css("a::attr(href)").re(".*contact.*")[0]
            contact_url = f"{self.base_url}{contact_sub_url}"
            yield response.follow(contact_url, callback=self.parse_contact)

