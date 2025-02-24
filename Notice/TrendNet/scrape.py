import requests
import lxml.html as lh
import time

dirtyList = """TI_G642i1.0R
TEG_284WS1.5R
TL2_E2841.0R
TEG_2248WSC1.0R
TEW_716BRG1.0R
TEW_634GRU1.0R
TEW_410APBPlusA
TEW_753DAP1.0R
TEW_432BRPD1.2R
TS_U200
TI_PG541i1.0R
TEW_722BRM1.0R
TEW_714TRU1.0R_EU
TEG_204WS1.0R
TPE_5048WS1.0R
TEW_435BRMD1.0R
TW100_BRM504A1
TEW_652BRU1.0R
THA_1011.0R
TPE_2840WS2.5R
TEW_692GR1.0R
TI_PG1284i1.0R
TPL_430AP1.0R
TL2_G2441.0R
TEW_734APO1.0R
TPL_410AP2.0R
TEG_401281.0R
TEW_820DRU1.0R
TEW_718BRM1.0R
TEW_640MB1.0R
TDM_C5001.0R
TEG_082WS2.5R
TEW_755AP1.0R
TEW_816DRM1.0R
TV_IP110WN2.0R
TEW_812DRU2.xR
TEW_818DRU1.0R
TEW_687GA1.0R
TI_PG1284i2.0R
TEG_448WSC1.0R
TI_G160i1.0R
TEG_30102WS1.0R
TN_2001.0R
TI_G102i1.0R
TEW_737HRE1.1R
TPE_1020WS1.0R
TV_IP551WI1.1R
TPE_3018LS1.0R
TEW_WLC100P1.0R
TL2_G2442.0R
TEW_690AP1.0R
TEW_713RE1.0R
TPE_204US1.0R
TPE_1620WS2.5R
TWG_431BR1.0R
TS_U100
TPE_5240WS1.0R
TEW_638APB3.0R
TEW_230APB
TEW_430APBC1.0R
TEW_647GA2.xR
TEW_411BRPPlusA
TEW_813DRU1.0R
TPE_224WSC1.0R
TEW_658BRM1.0R
TL2_PG2841.0R
TEW_639GR1.0R
TV_IP751WC1.0R
TEG_160WSD1
TEW_637AP3.0R
TV_IP651W1.0R
TEW_825DAP1.5R
TEW_656BRG1.0R
TEW_824DRU1.0R
TEW_638APB2.0R
TEW_655BR3G1.0R
TEW_730APO1.0R
TI_RP262i1.0R
TW100_BRM504C1.0R
TEW_637APB1.0R
TEW_657BRM1.0R
TEW_714TRU1.0R
TI_PG102i1.0R
TPE_5028WS1.0R
TL2_G4481.0R
TEW651BR
TEW_751DR1.0R
TV_IP551WI1.0R
TEW691GR
TEW_815DAP1.0R
TEW_811DRU1.0R
TV_IP301W1.0R
TEW_737HRE1.0R
TEW_691GR1.0R
TEW_638APB1.0R
TEW_639GR3.0R
TV_IP322WI1.0R
TEW_637APB2.0R
TV_IP320PI__TV_IP320PI2K__TV_IP321PI__TV_IP322WI_TV_IP340PI__TV_IP341PI
TEG_524WS1.0R
TEW_739APBO1.0R
TEW_828DRU1.0R
TV_IP320PI1.0R
TEW_636APB1.0R
TPE_2840WS2.0R
TEW_659BRV1.0R
TEW_652BRP3.0R
TEW_635BRM1.0R
TEW_740APBO2K3.0R
TEW_632BRPA1.1
TEW_821DAP1.0R
TEW_827DRU2.0R
TEG_302841.0R
TEW_822DRE1.0R
TPL_310AP1.0R
TEW_812DRU1.0R
TEG_082WS1.0R
TEW_820AP1.0R
TEW_752DRU1.0R
TEW_740APBO2K2.0R
TL_PG4841.0R
THA_103AC1.0R
TEW_652BRP2.0R
TEG_284WS1.0R
TEW_WLC1001.0R
TEW_712BR1.0R
TE100_MFP11.0R
TEG_204WS1.5R
TEW_800MB1.0R
TPE_5048WS1.5R
TPE_2840WS1.0R
TEW_810DR1.0R
TEW_821DAP2.0R
TEW_635BRM2.0R
TEW_MFP11.0R
TV_M71.0R
TV_IP551W1.0R
TEW_652BRP1.0R
TV_IP201P1.0R
TEW_673GRU1.0R
TEG_240D1.0R
TEW_814DAP1.0R
TEG_082WS2.0R
TEW_732BR1.0R
TS_I300W1.0R
TS_S4021.0R
TEG_424WS2.0R
TDM_C5041.0R
TI_G160WS1.0R
TV_IP651WI1.0R
TEW_435BRMB1
TW100_BRV2141.0R
TEW_680MB1.0R
TEW_736RE1.0R
TEW_740APBO1.0R
TPE_5240WS1.5R
TEW_817DTR1.0R
TEW_436BRM1.0R
TEW639GR
TEW_651BR1.0R
TPE_1620WS2.0R
TPE_204US1.5R
TEW_714TRU1.0R_A
TEW_731BR1.0R
TPE_4840WS1.0R
TEW_711BR2.0R
FW_TV_IP851WIC_V1_1.03
TV_IP201__TV_IP201W1.0R
TEW_738APBO1.0R
TPE_1620WSF1.0R
TEW_672GR1.0R
TV_NVR4081.0R
TEW_823DRU1.0R
TV_IP302PI1.0R
TV_IP851WC1.0R
TFC_1600MMC1.0R
TEW_740APBO2.0R
TEW_733GR1.0R
TEW_638PAP1.0R
TEW_650AP1.0R
TEW_651BR2.0R
TPE_1620WS1.0R
TV_IP851WIC1.0R
TEW_434APBA1.0R
TV_IP751WIC1.0R
TEW_740APBO3.0R
TEW_721BRM1.0R
TEW_810DR1.1R
TPE_5028WS1.5R
TV_IP121WN2.0R
TEW_676APBO1.0R
TEW_750DAP1.0R
TI_PG1284I2.0R
TEW_654TR1.0R
TEW_731BR2.0R
TEW_711BR1.0R
TPE_3012LS1.0R
TEW_647GA1.0R"""

dirtyList = dirtyList.split("\n")

reqCounter = 0
for router in dirtyList:
  original = router

  if len(router.split('_')) > 2:
    router = router.split('_')[0] + "-" + router.split('_')[1]

  if len(router.split('.')) > 1:
    router = router.split('.')[0][:-1]
  
  if reqCounter == 5:
    time.sleep(30)
    reqCounter = 0
  else:
    reqCounter += 1
  url = f"https://www.trendnet.com/support/discontinued-products.asp?search={router}&todo=search"
  res = requests.get(url)

  doc = lh.fromstring(res.content)
  tr_elements = doc.xpath('//tr')

  if len(tr_elements) == 0:
    print(f"{original} ({router}) not found")
    date = '-'
  else:
    cells = tr_elements[0]
    date = cells.xpath('//td')[3].text_content()
  
  print(f'{original},{router},{date}')
