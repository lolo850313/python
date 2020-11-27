def wiring_frame(effectARJ,dmCode,wireInfo,phInfo):
    from lxml import etree
    from lxml.builder import ElementMaker    

    E = ElementMaker()

    #************************初始化相关E工厂对象，形成基本树（即不管arj项目如何构成，都需要的基本子元素）
    wiringData_XML = E.wiringData
    wireGroup_XML = E.wireGroup
    wireAlts_XML = E.wireAlts
    wire_XML = E.wire
    wireIdent_XML = E.wireIdent
    wireNumber_XML = E.wireNumber
    wireConnection_XML = E.wireConnection
    fromEquip_XML = E.fromEquip
    contactInfo_XML = E.contactInfo
    wireConnectionCode_XML = E.wireConnectionCode
    contact_XML = E.contact
    specialConnection_XML = E.specialConnection
    toEquip_XML = E.toEquip
    wireInfo_XML = E.wireInfo
    wireCode_XML = E.wireCode
    wireType_XML = E.wireType
    wireGauge_XML = E.wireGauge
    partNumber_XML = E.partNumber
    harnessIdent_XML = E.harnessIdent
    length_XML = E.length
    wireColor_XML = E.wireColor
    wireRoute_XML = E.wireRoute
    functionalDescrRef_XML = E.functionalDescrRef
    refs_XML = E.refs
    dmRef_XML = E.dmRef
    dmRefIdent_XML = E.dmRefIdent
    electricalEquipGroup_XML = E.electricalEquipGroup
    electricalEquip_XML = E.electricalEquip
    equipName_XML = E.equipName
    dmCode_XML = E.dmCode
   
    wiringData_element = wiringData_XML(
            wireGroup_XML(
                wireAlts_XML(
                    wire_XML(
                        wireIdent_XML
                            (wireNumber_XML(wireInfo["导线号"])),
                        wireConnection_XML
                            (fromEquip_XML
                                (contactInfo_XML
                                    (contact_XML(contactIdent = wireInfo["从端孔号"],contactPartNumber = phInfo["接触件件号"]),
                                    wireConnectionCode_XML(specialConnection_XML(wireInfo["从端端接代号"]))
                                    )
                                ),
                            toEquip_XML
                                (contactInfo_XML
                                    (contact_XML(contactIdent = wireInfo["到端孔号"],contactPartNumber = phInfo["接触件件号"]),
                                    wireConnectionCode_XML(specialConnection_XML(wireInfo["到端端接代号"]))
                                    )
                                )
                            ),
                        wireInfo_XML
                            (wireCode_XML
                                (
                                    wireType_XML(wireInfo["导线材料"]),
                                    wireGauge_XML(wireInfo["AWG"])
                                ),
                            partNumber_XML(phInfo["导线零件号"]),
                            harnessIdent_XML(wireInfo["线束号"]),
                            length_XML(wireInfo["导线长度"]),
                            wireColor_XML(phInfo["导线颜色"]),
                            wireRoute_XML(wireInfo["敷设字母"]),
                            functionalDescrRef_XML
                                (refs_XML
                                    (dmRef_XML
                                        (dmRefIdent_XML
                                            (dmCode_XML
                                                (assyCode = dmCode["assyCode"],
                                                disassyCode = dmCode["disassyCode"],
                                                disassyCodeVariant = dmCode["disassyCodeVariant"],
                                                infoCode = dmCode["infoCode"],
                                                infoCodeVariant = dmCode["infoCodeVariant"],
                                                itemLocationCode = dmCode["itemLocationCode"],
                                                modelIdentCode = dmCode["modelIdentCode"],
                                                subSubSystemCode = dmCode["subSubSystemCode"],
                                                subSystemCode = dmCode["subSystemCode"],
                                                systemCode = dmCode["systemCode"],
                                                systemDiffCode = dmCode["systemDiffCode"]
                                                )
                                            )
                                        )
                                    )
                                )
                            ),
                        applicRefId = effectARJ
                    )
                )
            )      
        )

    return wiringData_element






