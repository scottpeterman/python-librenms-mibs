# SNMP MIB module (TROPIC-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TROPIC-GLOBAL-REG
# Produced by pysmi-1.6.2 at Thu Oct  2 12:12:02 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

tropicGlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tropicGlobalRegModule.setRevisions(
        ("2022-11-18 12:00",
         "2022-07-15 12:00",
         "2022-04-29 12:00",
         "2022-03-25 12:00",
         "2022-03-04 12:00",
         "2021-12-24 12:00",
         "2021-12-17 12:00",
         "2021-12-03 12:00",
         "2021-10-22 12:00",
         "2021-06-04 12:00",
         "2021-05-14 12:00",
         "2021-05-07 12:00",
         "2021-04-30 12:00",
         "2021-03-05 12:00",
         "2020-12-18 12:00",
         "2020-10-02 12:00",
         "2020-09-18 12:00",
         "2020-08-21 12:00",
         "2020-08-07 12:00",
         "2020-04-03 12:00",
         "2020-03-20 12:00",
         "2020-02-28 12:00",
         "2020-01-10 12:00",
         "2019-11-15 12:00",
         "2019-11-01 12:00",
         "2019-10-04 12:00",
         "2019-09-27 12:00",
         "2019-08-02 12:00",
         "2019-07-19 12:00",
         "2019-05-31 12:00",
         "2019-04-12 12:00",
         "2019-03-08 12:00",
         "2019-02-22 12:00",
         "2019-02-08 12:00",
         "2019-01-25 12:00",
         "2019-01-18 12:00",
         "2018-12-28 12:00",
         "2018-10-26 12:00",
         "2018-10-19 12:00",
         "2018-09-28 12:00",
         "2018-08-10 12:00",
         "2018-07-06 12:00",
         "2018-06-29 12:00",
         "2018-06-15 12:00",
         "2018-06-08 12:00",
         "2018-05-25 12:00",
         "2018-03-23 12:00",
         "2018-03-09 12:00",
         "2018-02-23 12:00",
         "2018-01-26 12:00",
         "2018-01-12 12:00",
         "2017-11-10 12:00",
         "2017-11-03 12:00",
         "2017-10-27 12:00",
         "2017-10-13 12:00",
         "2017-09-22 12:00",
         "2017-09-15 12:00",
         "2017-09-01 12:00",
         "2017-08-18 12:00",
         "2017-07-14 12:00",
         "2017-07-07 12:00",
         "2017-06-30 12:00",
         "2017-06-23 12:00",
         "2017-06-09 12:00",
         "2017-05-26 12:00",
         "2017-04-07 12:00",
         "2017-03-24 12:00",
         "2017-03-10 12:00",
         "2017-02-24 12:00",
         "2017-01-27 12:00",
         "2017-01-20 12:00",
         "2016-12-21 12:00",
         "2016-12-19 12:00",
         "2016-12-09 12:00",
         "2016-11-18 12:00",
         "2016-11-16 12:00",
         "2016-11-11 12:00",
         "2016-11-01 12:00",
         "2016-10-25 12:00",
         "2016-09-13 12:00",
         "2016-08-30 12:00",
         "2016-08-29 12:00",
         "2016-08-22 12:00",
         "2016-08-11 12:00",
         "2016-07-27 12:00",
         "2016-06-01 12:00",
         "2016-05-25 12:00",
         "2016-05-20 12:00",
         "2016-05-10 12:00",
         "2016-05-04 12:00",
         "2016-04-13 12:00",
         "2016-04-07 12:00",
         "2016-03-18 12:00",
         "2015-12-24 12:00",
         "2015-12-07 12:00",
         "2015-10-28 12:00",
         "2015-10-05 12:00",
         "2015-08-06 12:00",
         "2015-06-22 12:00",
         "2015-06-12 12:00",
         "2015-02-20 12:00",
         "2015-01-16 12:00",
         "2014-09-25 12:00",
         "2014-09-18 12:00",
         "2014-08-08 12:00",
         "2014-07-07 12:00",
         "2014-06-20 12:00",
         "2014-05-18 12:00",
         "2014-05-09 12:00",
         "2014-05-06 12:00",
         "2014-04-08 12:00",
         "2014-02-19 12:00",
         "2014-01-22 12:00",
         "2013-12-17 12:00",
         "2013-11-25 12:00",
         "2013-10-10 12:00",
         "2013-10-07 12:00",
         "2013-09-04 12:00",
         "2013-08-12 12:00",
         "2013-06-27 12:00",
         "2013-06-24 12:00",
         "2013-05-24 12:00",
         "2013-05-15 12:00",
         "2013-04-19 12:00",
         "2013-04-11 12:00",
         "2013-03-16 12:00",
         "2013-03-07 12:00",
         "2013-01-24 12:00",
         "2012-11-06 12:00",
         "2012-10-12 12:00",
         "2012-08-28 12:00",
         "2012-07-24 12:00",
         "2012-06-18 12:00",
         "2012-05-01 12:00",
         "2012-04-27 12:00",
         "2012-04-24 12:00",
         "2012-04-06 12:00",
         "2012-03-29 12:00",
         "2012-03-18 12:00",
         "2012-03-15 12:00",
         "2012-02-16 12:00",
         "2012-01-19 12:00",
         "2012-01-18 12:00",
         "2012-01-10 12:00",
         "2011-11-21 12:00",
         "2011-11-14 12:00",
         "2011-09-16 12:00",
         "2011-09-06 12:00",
         "2011-08-31 12:00",
         "2011-07-19 12:00",
         "2011-07-07 12:00",
         "2011-06-30 12:00",
         "2011-06-13 12:00",
         "2011-06-07 12:00",
         "2011-05-17 12:00",
         "2011-05-04 12:00",
         "2010-11-22 12:00",
         "2010-11-14 12:00",
         "2010-11-10 12:00",
         "2010-10-19 12:00",
         "2010-10-17 12:00",
         "2010-10-12 12:00",
         "2010-09-28 12:00",
         "2010-09-24 12:00",
         "2010-09-20 12:00",
         "2010-09-10 12:00",
         "2010-08-02 12:00",
         "2010-07-20 12:00",
         "2010-06-28 12:00",
         "2010-06-23 12:00",
         "2010-06-04 12:00",
         "2010-05-11 12:00",
         "2010-05-10 12:00",
         "2010-05-07 12:00",
         "2010-02-17 12:00",
         "2010-01-24 12:00",
         "2010-01-04 12:00",
         "2009-12-29 12:00",
         "2009-12-10 12:00",
         "2009-11-01 12:00",
         "2009-09-25 12:00",
         "2009-05-14 12:00",
         "2009-04-23 12:00",
         "2009-03-31 12:00",
         "2009-03-18 12:00",
         "2009-03-15 12:00",
         "2009-03-02 12:00",
         "2009-02-13 12:00",
         "2008-07-24 12:00",
         "2008-05-29 12:00",
         "2008-03-20 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tropic_ObjectIdentity = ObjectIdentity
tropic = _Tropic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483)
)
if mibBuilder.loadTexts:
    tropic.setStatus("current")
_TropicRegistry_ObjectIdentity = ObjectIdentity
tropicRegistry = _TropicRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1)
)
if mibBuilder.loadTexts:
    tropicRegistry.setStatus("current")
_TropicModules_ObjectIdentity = ObjectIdentity
tropicModules = _TropicModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1)
)
if mibBuilder.loadTexts:
    tropicModules.setStatus("current")
_TnGenericModules_ObjectIdentity = ObjectIdentity
tnGenericModules = _TnGenericModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnGenericModules.setStatus("current")
_TnSystemModules_ObjectIdentity = ObjectIdentity
tnSystemModules = _TnSystemModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnSystemModules.setStatus("current")
_TnEquipmentModules_ObjectIdentity = ObjectIdentity
tnEquipmentModules = _TnEquipmentModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnEquipmentModules.setStatus("current")
_TnShelfModules_ObjectIdentity = ObjectIdentity
tnShelfModules = _TnShelfModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnShelfModules.setStatus("current")
_TnSlotModules_ObjectIdentity = ObjectIdentity
tnSlotModules = _TnSlotModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tnSlotModules.setStatus("current")
_TnCardModules_ObjectIdentity = ObjectIdentity
tnCardModules = _TnCardModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    tnCardModules.setStatus("current")
_TnPortModules_ObjectIdentity = ObjectIdentity
tnPortModules = _TnPortModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tnPortModules.setStatus("current")
_TnMiscModules_ObjectIdentity = ObjectIdentity
tnMiscModules = _TnMiscModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    tnMiscModules.setStatus("current")
_TnVwmMsModules_ObjectIdentity = ObjectIdentity
tnVwmMsModules = _TnVwmMsModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    tnVwmMsModules.setStatus("current")
_TnPsdModules_ObjectIdentity = ObjectIdentity
tnPsdModules = _TnPsdModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    tnPsdModules.setStatus("current")
_TnServiceModules_ObjectIdentity = ObjectIdentity
tnServiceModules = _TnServiceModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tnServiceModules.setStatus("current")
_TnProtocolModules_ObjectIdentity = ObjectIdentity
tnProtocolModules = _TnProtocolModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    tnProtocolModules.setStatus("current")
_TropicExprModules_ObjectIdentity = ObjectIdentity
tropicExprModules = _TropicExprModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tropicExprModules.setStatus("current")
_TnGmplsMIBModules_ObjectIdentity = ObjectIdentity
tnGmplsMIBModules = _TnGmplsMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    tnGmplsMIBModules.setStatus("current")
_TnAbsNodeMIBModules_ObjectIdentity = ObjectIdentity
tnAbsNodeMIBModules = _TnAbsNodeMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    tnAbsNodeMIBModules.setStatus("current")
_TnDhpMIBModules_ObjectIdentity = ObjectIdentity
tnDhpMIBModules = _TnDhpMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    tnDhpMIBModules.setStatus("current")
_TnTypeDefinitionModules_ObjectIdentity = ObjectIdentity
tnTypeDefinitionModules = _TnTypeDefinitionModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnTypeDefinitionModules.setStatus("current")
_TropicMetroReg_ObjectIdentity = ObjectIdentity
tropicMetroReg = _TropicMetroReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3)
)
if mibBuilder.loadTexts:
    tropicMetroReg.setStatus("current")
_TropicMetroNodeReg_ObjectIdentity = ObjectIdentity
tropicMetroNodeReg = _TropicMetroNodeReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tropicMetroNodeReg.setStatus("current")
_TropicTRX24000_ObjectIdentity = ObjectIdentity
tropicTRX24000 = _TropicTRX24000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tropicTRX24000.setStatus("current")
_AluWdm1830PSS32_ObjectIdentity = ObjectIdentity
aluWdm1830PSS32 = _AluWdm1830PSS32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    aluWdm1830PSS32.setStatus("current")
_AluWdm1830PSS1_ObjectIdentity = ObjectIdentity
aluWdm1830PSS1 = _AluWdm1830PSS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    aluWdm1830PSS1.setStatus("current")
_AluWdm1830PSS1MD4H_ObjectIdentity = ObjectIdentity
aluWdm1830PSS1MD4H = _AluWdm1830PSS1MD4H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    aluWdm1830PSS1MD4H.setStatus("current")
_AluWdm1830PSS1GBEH_ObjectIdentity = ObjectIdentity
aluWdm1830PSS1GBEH = _AluWdm1830PSS1GBEH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    aluWdm1830PSS1GBEH.setStatus("current")
_AluWdm1830PSS_ObjectIdentity = ObjectIdentity
aluWdm1830PSS = _AluWdm1830PSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    aluWdm1830PSS.setStatus("current")
_AluWdm1830PSS4_ObjectIdentity = ObjectIdentity
aluWdm1830PSS4 = _AluWdm1830PSS4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 8)
)
if mibBuilder.loadTexts:
    aluWdm1830PSS4.setStatus("current")
_AluWdm1830PSS1MSAH_ObjectIdentity = ObjectIdentity
aluWdm1830PSS1MSAH = _AluWdm1830PSS1MSAH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 9)
)
if mibBuilder.loadTexts:
    aluWdm1830PSS1MSAH.setStatus("current")
_Nokia1830VwmMs_ObjectIdentity = ObjectIdentity
nokia1830VwmMs = _Nokia1830VwmMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 11)
)
if mibBuilder.loadTexts:
    nokia1830VwmMs.setStatus("current")
_Nokia1830Psd_ObjectIdentity = ObjectIdentity
nokia1830Psd = _Nokia1830Psd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 12)
)
if mibBuilder.loadTexts:
    nokia1830Psd.setStatus("current")
_AluWdm1830PSI_ObjectIdentity = ObjectIdentity
aluWdm1830PSI = _AluWdm1830PSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 13)
)
if mibBuilder.loadTexts:
    aluWdm1830PSI.setStatus("current")
_AluWdm1830PSIM_ObjectIdentity = ObjectIdentity
aluWdm1830PSIM = _AluWdm1830PSIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 14)
)
if mibBuilder.loadTexts:
    aluWdm1830PSIM.setStatus("current")
_AluWdm1830OLS_ObjectIdentity = ObjectIdentity
aluWdm1830OLS = _AluWdm1830OLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 15)
)
if mibBuilder.loadTexts:
    aluWdm1830OLS.setStatus("current")
_Nokia1830TPS_ObjectIdentity = ObjectIdentity
nokia1830TPS = _Nokia1830TPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 16)
)
if mibBuilder.loadTexts:
    nokia1830TPS.setStatus("current")
_Nokia1830SAS_ObjectIdentity = ObjectIdentity
nokia1830SAS = _Nokia1830SAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 3, 1, 17)
)
if mibBuilder.loadTexts:
    nokia1830SAS.setStatus("current")
_TropicShelfReg_ObjectIdentity = ObjectIdentity
tropicShelfReg = _TropicShelfReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4)
)
if mibBuilder.loadTexts:
    tropicShelfReg.setStatus("current")
_TropicEmptyShelf_ObjectIdentity = ObjectIdentity
tropicEmptyShelf = _TropicEmptyShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tropicEmptyShelf.setStatus("current")
_TropicUnknownShelf_ObjectIdentity = ObjectIdentity
tropicUnknownShelf = _TropicUnknownShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tropicUnknownShelf.setStatus("current")
_AluWdmSfd44Shelf_ObjectIdentity = ObjectIdentity
aluWdmSfd44Shelf = _AluWdmSfd44Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 7)
)
if mibBuilder.loadTexts:
    aluWdmSfd44Shelf.setStatus("current")
_AluWdmDcmShelf_ObjectIdentity = ObjectIdentity
aluWdmDcmShelf = _AluWdmDcmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 8)
)
if mibBuilder.loadTexts:
    aluWdmDcmShelf.setStatus("current")
_AluWdmUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmUniversalShelf = _AluWdmUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 9)
)
if mibBuilder.loadTexts:
    aluWdmUniversalShelf.setStatus("current")
_AluWdmSfd44bShelf_ObjectIdentity = ObjectIdentity
aluWdmSfd44bShelf = _AluWdmSfd44bShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 10)
)
if mibBuilder.loadTexts:
    aluWdmSfd44bShelf.setStatus("current")
_AluWdmItlbShelf_ObjectIdentity = ObjectIdentity
aluWdmItlbShelf = _AluWdmItlbShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 11)
)
if mibBuilder.loadTexts:
    aluWdmItlbShelf.setStatus("current")
_AluWdmPSS32UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS32UniversalShelf = _AluWdmPSS32UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 12)
)
if mibBuilder.loadTexts:
    aluWdmPSS32UniversalShelf.setStatus("current")
_AluWdmPSS16UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS16UniversalShelf = _AluWdmPSS16UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 13)
)
if mibBuilder.loadTexts:
    aluWdmPSS16UniversalShelf.setStatus("current")
_AluWdmSfd40Shelf_ObjectIdentity = ObjectIdentity
aluWdmSfd40Shelf = _AluWdmSfd40Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 14)
)
if mibBuilder.loadTexts:
    aluWdmSfd40Shelf.setStatus("current")
_AluWdmSfd40bShelf_ObjectIdentity = ObjectIdentity
aluWdmSfd40bShelf = _AluWdmSfd40bShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 15)
)
if mibBuilder.loadTexts:
    aluWdmSfd40bShelf.setStatus("current")
_AluWdmPSS4UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS4UniversalShelf = _AluWdmPSS4UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 16)
)
if mibBuilder.loadTexts:
    aluWdmPSS4UniversalShelf.setStatus("current")
_AluWdmPSS36UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS36UniversalShelf = _AluWdmPSS36UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 18)
)
if mibBuilder.loadTexts:
    aluWdmPSS36UniversalShelf.setStatus("current")
_AluWdmPSS64UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS64UniversalShelf = _AluWdmPSS64UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 23)
)
if mibBuilder.loadTexts:
    aluWdmPSS64UniversalShelf.setStatus("current")
_AluWdmItluShelf_ObjectIdentity = ObjectIdentity
aluWdmItluShelf = _AluWdmItluShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 24)
)
if mibBuilder.loadTexts:
    aluWdmItluShelf.setStatus("current")
_AluWdmPSS32SwitchUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS32SwitchUniversalShelf = _AluWdmPSS32SwitchUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 25)
)
if mibBuilder.loadTexts:
    aluWdmPSS32SwitchUniversalShelf.setStatus("current")
_AluWdmPSS32Switch1P2TUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS32Switch1P2TUniversalShelf = _AluWdmPSS32Switch1P2TUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 26)
)
if mibBuilder.loadTexts:
    aluWdmPSS32Switch1P2TUniversalShelf.setStatus("current")
_AluWdmPsc1x6Shelf_ObjectIdentity = ObjectIdentity
aluWdmPsc1x6Shelf = _AluWdmPsc1x6Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 27)
)
if mibBuilder.loadTexts:
    aluWdmPsc1x6Shelf.setStatus("current")
_AluWdmPSS8UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS8UniversalShelf = _AluWdmPSS8UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 28)
)
if mibBuilder.loadTexts:
    aluWdmPSS8UniversalShelf.setStatus("current")
_AluWdmPSS16IIUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS16IIUniversalShelf = _AluWdmPSS16IIUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 29)
)
if mibBuilder.loadTexts:
    aluWdmPSS16IIUniversalShelf.setStatus("current")
_AluWdmPSS48UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS48UniversalShelf = _AluWdmPSS48UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 30)
)
if mibBuilder.loadTexts:
    aluWdmPSS48UniversalShelf.setStatus("current")
_AluWdmPSS96UniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS96UniversalShelf = _AluWdmPSS96UniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 31)
)
if mibBuilder.loadTexts:
    aluWdmPSS96UniversalShelf.setStatus("current")
_AluWdmMsh8fsmShelf_ObjectIdentity = ObjectIdentity
aluWdmMsh8fsmShelf = _AluWdmMsh8fsmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 32)
)
if mibBuilder.loadTexts:
    aluWdmMsh8fsmShelf.setStatus("current")
_AluWdmVwmCwUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmVwmCwUniversalShelf = _AluWdmVwmCwUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 33)
)
if mibBuilder.loadTexts:
    aluWdmVwmCwUniversalShelf.setStatus("current")
_AluWdmVwmDwUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmVwmDwUniversalShelf = _AluWdmVwmDwUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 34)
)
if mibBuilder.loadTexts:
    aluWdmVwmDwUniversalShelf.setStatus("current")
_NokiaVwmMsOsu20Shelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsOsu20Shelf = _NokiaVwmMsOsu20Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 37)
)
if mibBuilder.loadTexts:
    nokiaVwmMsOsu20Shelf.setStatus("current")
_NokiaVwmMsTlu9Shelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsTlu9Shelf = _NokiaVwmMsTlu9Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 38)
)
if mibBuilder.loadTexts:
    nokiaVwmMsTlu9Shelf.setStatus("current")
_NokiaVwmMsPmu9UcShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmu9UcShelf = _NokiaVwmMsPmu9UcShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 39)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmu9UcShelf.setStatus("current")
_NokiaVwmMsPmu9LcShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmu9LcShelf = _NokiaVwmMsPmu9LcShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 40)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmu9LcShelf.setStatus("current")
_NokiaVwmMsPmu9UcmShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmu9UcmShelf = _NokiaVwmMsPmu9UcmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 41)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmu9UcmShelf.setStatus("current")
_NokiaVwmMsPmu9LcmShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmu9LcmShelf = _NokiaVwmMsPmu9LcmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 42)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmu9LcmShelf.setStatus("current")
_NokiaVwmMsItp4UcaShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsItp4UcaShelf = _NokiaVwmMsItp4UcaShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 43)
)
if mibBuilder.loadTexts:
    nokiaVwmMsItp4UcaShelf.setStatus("current")
_NokiaVwmMsItp4UcbShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsItp4UcbShelf = _NokiaVwmMsItp4UcbShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 44)
)
if mibBuilder.loadTexts:
    nokiaVwmMsItp4UcbShelf.setStatus("current")
_NokiaVwmMsItp4LcaShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsItp4LcaShelf = _NokiaVwmMsItp4LcaShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 45)
)
if mibBuilder.loadTexts:
    nokiaVwmMsItp4LcaShelf.setStatus("current")
_NokiaVwmMsItp4LcbShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsItp4LcbShelf = _NokiaVwmMsItp4LcbShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 46)
)
if mibBuilder.loadTexts:
    nokiaVwmMsItp4LcbShelf.setStatus("current")
_NokiaVwmMsSmmAoShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsSmmAoShelf = _NokiaVwmMsSmmAoShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 47)
)
if mibBuilder.loadTexts:
    nokiaVwmMsSmmAoShelf.setStatus("current")
_NokiaVwmMsSmmAiShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsSmmAiShelf = _NokiaVwmMsSmmAiShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 48)
)
if mibBuilder.loadTexts:
    nokiaVwmMsSmmAiShelf.setStatus("current")
_NokiaVwmMsOpsShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsOpsShelf = _NokiaVwmMsOpsShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 49)
)
if mibBuilder.loadTexts:
    nokiaVwmMsOpsShelf.setStatus("current")
_AluWdmPSS8xUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS8xUniversalShelf = _AluWdmPSS8xUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 50)
)
if mibBuilder.loadTexts:
    aluWdmPSS8xUniversalShelf.setStatus("current")
_NokiaPsdShelf_ObjectIdentity = ObjectIdentity
nokiaPsdShelf = _NokiaPsdShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 51)
)
if mibBuilder.loadTexts:
    nokiaPsdShelf.setStatus("current")
_NokiaVwmMsTlu9mShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsTlu9mShelf = _NokiaVwmMsTlu9mShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 52)
)
if mibBuilder.loadTexts:
    nokiaVwmMsTlu9mShelf.setStatus("current")
_AluWdmPSI1TUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSI1TUniversalShelf = _AluWdmPSI1TUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 53)
)
if mibBuilder.loadTexts:
    aluWdmPSI1TUniversalShelf.setStatus("current")
_AluWdmPSI2TUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSI2TUniversalShelf = _AluWdmPSI2TUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 54)
)
if mibBuilder.loadTexts:
    aluWdmPSI2TUniversalShelf.setStatus("current")
_AluWdmPSI2TLUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSI2TLUniversalShelf = _AluWdmPSI2TLUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 55)
)
if mibBuilder.loadTexts:
    aluWdmPSI2TLUniversalShelf.setStatus("current")
_AluWdmPSIMUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSIMUniversalShelf = _AluWdmPSIMUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 56)
)
if mibBuilder.loadTexts:
    aluWdmPSIMUniversalShelf.setStatus("current")
_AluWdmPSS12xUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSS12xUniversalShelf = _AluWdmPSS12xUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 57)
)
if mibBuilder.loadTexts:
    aluWdmPSS12xUniversalShelf.setStatus("current")
_NokiaVwmMsPmuD21AShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmuD21AShelf = _NokiaVwmMsPmuD21AShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 58)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmuD21AShelf.setStatus("current")
_NokiaVwmMsPmuD21BShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmuD21BShelf = _NokiaVwmMsPmuD21BShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 59)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmuD21BShelf.setStatus("current")
_NokiaVwmMsPmuD21CShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmuD21CShelf = _NokiaVwmMsPmuD21CShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 60)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmuD21CShelf.setStatus("current")
_NokiaVwmMsPmuD21DShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmuD21DShelf = _NokiaVwmMsPmuD21DShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 61)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmuD21DShelf.setStatus("current")
_AluWdmSfd96Shelf_ObjectIdentity = ObjectIdentity
aluWdmSfd96Shelf = _AluWdmSfd96Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 62)
)
if mibBuilder.loadTexts:
    aluWdmSfd96Shelf.setStatus("current")
_AluWdmBmuPShelf_ObjectIdentity = ObjectIdentity
aluWdmBmuPShelf = _AluWdmBmuPShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 63)
)
if mibBuilder.loadTexts:
    aluWdmBmuPShelf.setStatus("current")
_AluWdmSplit2Shelf_ObjectIdentity = ObjectIdentity
aluWdmSplit2Shelf = _AluWdmSplit2Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 64)
)
if mibBuilder.loadTexts:
    aluWdmSplit2Shelf.setStatus("current")
_AluWdmOscCplrShelf_ObjectIdentity = ObjectIdentity
aluWdmOscCplrShelf = _AluWdmOscCplrShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 65)
)
if mibBuilder.loadTexts:
    aluWdmOscCplrShelf.setStatus("current")
_AluWdmOAUnidirShelf_ObjectIdentity = ObjectIdentity
aluWdmOAUnidirShelf = _AluWdmOAUnidirShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 66)
)
if mibBuilder.loadTexts:
    aluWdmOAUnidirShelf.setStatus("current")
_AluWdmMsh4fsbShelf_ObjectIdentity = ObjectIdentity
aluWdmMsh4fsbShelf = _AluWdmMsh4fsbShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 67)
)
if mibBuilder.loadTexts:
    aluWdmMsh4fsbShelf.setStatus("current")
_NokiaVwmMsTlu200Shelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsTlu200Shelf = _NokiaVwmMsTlu200Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 68)
)
if mibBuilder.loadTexts:
    nokiaVwmMsTlu200Shelf.setStatus("current")
_NokiaVwmMsADVGIShelf_ObjectIdentity = ObjectIdentity
nokiaVwmMsADVGIShelf = _NokiaVwmMsADVGIShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 69)
)
if mibBuilder.loadTexts:
    nokiaVwmMsADVGIShelf.setStatus("current")
_AluWdmPSIL3uUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSIL3uUniversalShelf = _AluWdmPSIL3uUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 70)
)
if mibBuilder.loadTexts:
    aluWdmPSIL3uUniversalShelf.setStatus("current")
_AluWdmPSIL5uUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSIL5uUniversalShelf = _AluWdmPSIL5uUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 71)
)
if mibBuilder.loadTexts:
    aluWdmPSIL5uUniversalShelf.setStatus("current")
_NokiaSfd10ALmShelf_ObjectIdentity = ObjectIdentity
nokiaSfd10ALmShelf = _NokiaSfd10ALmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 72)
)
if mibBuilder.loadTexts:
    nokiaSfd10ALmShelf.setStatus("current")
_NokiaSfd10BLmShelf_ObjectIdentity = ObjectIdentity
nokiaSfd10BLmShelf = _NokiaSfd10BLmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 73)
)
if mibBuilder.loadTexts:
    nokiaSfd10BLmShelf.setStatus("current")
_NokiaSfd10CLmShelf_ObjectIdentity = ObjectIdentity
nokiaSfd10CLmShelf = _NokiaSfd10CLmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 74)
)
if mibBuilder.loadTexts:
    nokiaSfd10CLmShelf.setStatus("current")
_NokiaSfd10DLmShelf_ObjectIdentity = ObjectIdentity
nokiaSfd10DLmShelf = _NokiaSfd10DLmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 75)
)
if mibBuilder.loadTexts:
    nokiaSfd10DLmShelf.setStatus("current")
_NokiaSfd2AShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2AShelf = _NokiaSfd2AShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 76)
)
if mibBuilder.loadTexts:
    nokiaSfd2AShelf.setStatus("current")
_NokiaSfd2BShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2BShelf = _NokiaSfd2BShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 77)
)
if mibBuilder.loadTexts:
    nokiaSfd2BShelf.setStatus("current")
_NokiaSfd2CShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2CShelf = _NokiaSfd2CShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 78)
)
if mibBuilder.loadTexts:
    nokiaSfd2CShelf.setStatus("current")
_NokiaSfd2DShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2DShelf = _NokiaSfd2DShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 79)
)
if mibBuilder.loadTexts:
    nokiaSfd2DShelf.setStatus("current")
_NokiaSfd2EShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2EShelf = _NokiaSfd2EShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 80)
)
if mibBuilder.loadTexts:
    nokiaSfd2EShelf.setStatus("current")
_NokiaSfd2FShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2FShelf = _NokiaSfd2FShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 81)
)
if mibBuilder.loadTexts:
    nokiaSfd2FShelf.setStatus("current")
_NokiaSfd2GShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2GShelf = _NokiaSfd2GShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 82)
)
if mibBuilder.loadTexts:
    nokiaSfd2GShelf.setStatus("current")
_NokiaSfd2HShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2HShelf = _NokiaSfd2HShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 83)
)
if mibBuilder.loadTexts:
    nokiaSfd2HShelf.setStatus("current")
_NokiaSfd2IShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2IShelf = _NokiaSfd2IShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 84)
)
if mibBuilder.loadTexts:
    nokiaSfd2IShelf.setStatus("current")
_NokiaSfd2LShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2LShelf = _NokiaSfd2LShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 85)
)
if mibBuilder.loadTexts:
    nokiaSfd2LShelf.setStatus("current")
_NokiaSfd2MShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2MShelf = _NokiaSfd2MShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 86)
)
if mibBuilder.loadTexts:
    nokiaSfd2MShelf.setStatus("current")
_NokiaSfd2NShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2NShelf = _NokiaSfd2NShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 87)
)
if mibBuilder.loadTexts:
    nokiaSfd2NShelf.setStatus("current")
_NokiaSfd2OShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2OShelf = _NokiaSfd2OShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 88)
)
if mibBuilder.loadTexts:
    nokiaSfd2OShelf.setStatus("current")
_NokiaSfd2PShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2PShelf = _NokiaSfd2PShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 89)
)
if mibBuilder.loadTexts:
    nokiaSfd2PShelf.setStatus("current")
_NokiaSfd2QShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2QShelf = _NokiaSfd2QShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 90)
)
if mibBuilder.loadTexts:
    nokiaSfd2QShelf.setStatus("current")
_NokiaSfd2RShelf_ObjectIdentity = ObjectIdentity
nokiaSfd2RShelf = _NokiaSfd2RShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 91)
)
if mibBuilder.loadTexts:
    nokiaSfd2RShelf.setStatus("current")
_NokiaSfd4AShelf_ObjectIdentity = ObjectIdentity
nokiaSfd4AShelf = _NokiaSfd4AShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 92)
)
if mibBuilder.loadTexts:
    nokiaSfd4AShelf.setStatus("current")
_NokiaSfd4BShelf_ObjectIdentity = ObjectIdentity
nokiaSfd4BShelf = _NokiaSfd4BShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 93)
)
if mibBuilder.loadTexts:
    nokiaSfd4BShelf.setStatus("current")
_NokiaSfd4CShelf_ObjectIdentity = ObjectIdentity
nokiaSfd4CShelf = _NokiaSfd4CShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 94)
)
if mibBuilder.loadTexts:
    nokiaSfd4CShelf.setStatus("current")
_NokiaSfd4DShelf_ObjectIdentity = ObjectIdentity
nokiaSfd4DShelf = _NokiaSfd4DShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 95)
)
if mibBuilder.loadTexts:
    nokiaSfd4DShelf.setStatus("current")
_NokiaSfd4EShelf_ObjectIdentity = ObjectIdentity
nokiaSfd4EShelf = _NokiaSfd4EShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 96)
)
if mibBuilder.loadTexts:
    nokiaSfd4EShelf.setStatus("current")
_NokiaSfd4FShelf_ObjectIdentity = ObjectIdentity
nokiaSfd4FShelf = _NokiaSfd4FShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 97)
)
if mibBuilder.loadTexts:
    nokiaSfd4FShelf.setStatus("current")
_NokiaSfd4GShelf_ObjectIdentity = ObjectIdentity
nokiaSfd4GShelf = _NokiaSfd4GShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 98)
)
if mibBuilder.loadTexts:
    nokiaSfd4GShelf.setStatus("current")
_NokiaSfd4HShelf_ObjectIdentity = ObjectIdentity
nokiaSfd4HShelf = _NokiaSfd4HShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 99)
)
if mibBuilder.loadTexts:
    nokiaSfd4HShelf.setStatus("current")
_NokiaSfd8AShelf_ObjectIdentity = ObjectIdentity
nokiaSfd8AShelf = _NokiaSfd8AShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 100)
)
if mibBuilder.loadTexts:
    nokiaSfd8AShelf.setStatus("current")
_NokiaSfd8BShelf_ObjectIdentity = ObjectIdentity
nokiaSfd8BShelf = _NokiaSfd8BShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 101)
)
if mibBuilder.loadTexts:
    nokiaSfd8BShelf.setStatus("current")
_NokiaSfd8CShelf_ObjectIdentity = ObjectIdentity
nokiaSfd8CShelf = _NokiaSfd8CShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 102)
)
if mibBuilder.loadTexts:
    nokiaSfd8CShelf.setStatus("current")
_NokiaSfd8DShelf_ObjectIdentity = ObjectIdentity
nokiaSfd8DShelf = _NokiaSfd8DShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 103)
)
if mibBuilder.loadTexts:
    nokiaSfd8DShelf.setStatus("current")
_NokiaSfc1AShelf_ObjectIdentity = ObjectIdentity
nokiaSfc1AShelf = _NokiaSfc1AShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 104)
)
if mibBuilder.loadTexts:
    nokiaSfc1AShelf.setStatus("current")
_NokiaSfc1BShelf_ObjectIdentity = ObjectIdentity
nokiaSfc1BShelf = _NokiaSfc1BShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 105)
)
if mibBuilder.loadTexts:
    nokiaSfc1BShelf.setStatus("current")
_NokiaSfc1CShelf_ObjectIdentity = ObjectIdentity
nokiaSfc1CShelf = _NokiaSfc1CShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 106)
)
if mibBuilder.loadTexts:
    nokiaSfc1CShelf.setStatus("current")
_NokiaSfc1DShelf_ObjectIdentity = ObjectIdentity
nokiaSfc1DShelf = _NokiaSfc1DShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 107)
)
if mibBuilder.loadTexts:
    nokiaSfc1DShelf.setStatus("current")
_NokiaSfc1EShelf_ObjectIdentity = ObjectIdentity
nokiaSfc1EShelf = _NokiaSfc1EShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 108)
)
if mibBuilder.loadTexts:
    nokiaSfc1EShelf.setStatus("current")
_NokiaSfc1FShelf_ObjectIdentity = ObjectIdentity
nokiaSfc1FShelf = _NokiaSfc1FShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 109)
)
if mibBuilder.loadTexts:
    nokiaSfc1FShelf.setStatus("current")
_NokiaSfc1GShelf_ObjectIdentity = ObjectIdentity
nokiaSfc1GShelf = _NokiaSfc1GShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 110)
)
if mibBuilder.loadTexts:
    nokiaSfc1GShelf.setStatus("current")
_NokiaSfc1HShelf_ObjectIdentity = ObjectIdentity
nokiaSfc1HShelf = _NokiaSfc1HShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 111)
)
if mibBuilder.loadTexts:
    nokiaSfc1HShelf.setStatus("current")
_NokiaSfc2ABShelf_ObjectIdentity = ObjectIdentity
nokiaSfc2ABShelf = _NokiaSfc2ABShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 112)
)
if mibBuilder.loadTexts:
    nokiaSfc2ABShelf.setStatus("current")
_NokiaSfc2CDShelf_ObjectIdentity = ObjectIdentity
nokiaSfc2CDShelf = _NokiaSfc2CDShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 113)
)
if mibBuilder.loadTexts:
    nokiaSfc2CDShelf.setStatus("current")
_NokiaSfc2EFShelf_ObjectIdentity = ObjectIdentity
nokiaSfc2EFShelf = _NokiaSfc2EFShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 114)
)
if mibBuilder.loadTexts:
    nokiaSfc2EFShelf.setStatus("current")
_NokiaSfc2GHShelf_ObjectIdentity = ObjectIdentity
nokiaSfc2GHShelf = _NokiaSfc2GHShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 115)
)
if mibBuilder.loadTexts:
    nokiaSfc2GHShelf.setStatus("current")
_NokiaSfc4ADShelf_ObjectIdentity = ObjectIdentity
nokiaSfc4ADShelf = _NokiaSfc4ADShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 116)
)
if mibBuilder.loadTexts:
    nokiaSfc4ADShelf.setStatus("current")
_NokiaSfc4EHShelf_ObjectIdentity = ObjectIdentity
nokiaSfc4EHShelf = _NokiaSfc4EHShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 117)
)
if mibBuilder.loadTexts:
    nokiaSfc4EHShelf.setStatus("current")
_NokiaSfc8UShelf_ObjectIdentity = ObjectIdentity
nokiaSfc8UShelf = _NokiaSfc8UShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 118)
)
if mibBuilder.loadTexts:
    nokiaSfc8UShelf.setStatus("current")
_NokiaSfc8LShelf_ObjectIdentity = ObjectIdentity
nokiaSfc8LShelf = _NokiaSfc8LShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 119)
)
if mibBuilder.loadTexts:
    nokiaSfc8LShelf.setStatus("current")
_NokiaSARO2AShelf_ObjectIdentity = ObjectIdentity
nokiaSARO2AShelf = _NokiaSARO2AShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 120)
)
if mibBuilder.loadTexts:
    nokiaSARO2AShelf.setStatus("current")
_NokiaSARO2BShelf_ObjectIdentity = ObjectIdentity
nokiaSARO2BShelf = _NokiaSARO2BShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 121)
)
if mibBuilder.loadTexts:
    nokiaSARO2BShelf.setStatus("current")
_NokiaSARO2CShelf_ObjectIdentity = ObjectIdentity
nokiaSARO2CShelf = _NokiaSARO2CShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 122)
)
if mibBuilder.loadTexts:
    nokiaSARO2CShelf.setStatus("current")
_NokiaSARO2DShelf_ObjectIdentity = ObjectIdentity
nokiaSARO2DShelf = _NokiaSARO2DShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 123)
)
if mibBuilder.loadTexts:
    nokiaSARO2DShelf.setStatus("current")
_NokiaSARO2EShelf_ObjectIdentity = ObjectIdentity
nokiaSARO2EShelf = _NokiaSARO2EShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 124)
)
if mibBuilder.loadTexts:
    nokiaSARO2EShelf.setStatus("current")
_NokiaSARO2FShelf_ObjectIdentity = ObjectIdentity
nokiaSARO2FShelf = _NokiaSARO2FShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 125)
)
if mibBuilder.loadTexts:
    nokiaSARO2FShelf.setStatus("current")
_NokiaSARO2GShelf_ObjectIdentity = ObjectIdentity
nokiaSARO2GShelf = _NokiaSARO2GShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 126)
)
if mibBuilder.loadTexts:
    nokiaSARO2GShelf.setStatus("current")
_NokiaSARO2HShelf_ObjectIdentity = ObjectIdentity
nokiaSARO2HShelf = _NokiaSARO2HShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 127)
)
if mibBuilder.loadTexts:
    nokiaSARO2HShelf.setStatus("current")
_NokiaSARO4AShelf_ObjectIdentity = ObjectIdentity
nokiaSARO4AShelf = _NokiaSARO4AShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 128)
)
if mibBuilder.loadTexts:
    nokiaSARO4AShelf.setStatus("current")
_NokiaSARO4BShelf_ObjectIdentity = ObjectIdentity
nokiaSARO4BShelf = _NokiaSARO4BShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 129)
)
if mibBuilder.loadTexts:
    nokiaSARO4BShelf.setStatus("current")
_NokiaSARO4CShelf_ObjectIdentity = ObjectIdentity
nokiaSARO4CShelf = _NokiaSARO4CShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 130)
)
if mibBuilder.loadTexts:
    nokiaSARO4CShelf.setStatus("current")
_NokiaSARO4DShelf_ObjectIdentity = ObjectIdentity
nokiaSARO4DShelf = _NokiaSARO4DShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 131)
)
if mibBuilder.loadTexts:
    nokiaSARO4DShelf.setStatus("current")
_NokiaSARO8AShelf_ObjectIdentity = ObjectIdentity
nokiaSARO8AShelf = _NokiaSARO8AShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 132)
)
if mibBuilder.loadTexts:
    nokiaSARO8AShelf.setStatus("current")
_NokiaSARO8BShelf_ObjectIdentity = ObjectIdentity
nokiaSARO8BShelf = _NokiaSARO8BShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 133)
)
if mibBuilder.loadTexts:
    nokiaSARO8BShelf.setStatus("current")
_NokiaLR4BOCShelf_ObjectIdentity = ObjectIdentity
nokiaLR4BOCShelf = _NokiaLR4BOCShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 134)
)
if mibBuilder.loadTexts:
    nokiaLR4BOCShelf.setStatus("current")
_NokiaTPS24Shelf_ObjectIdentity = ObjectIdentity
nokiaTPS24Shelf = _NokiaTPS24Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 135)
)
if mibBuilder.loadTexts:
    nokiaTPS24Shelf.setStatus("current")
_NokiaTPS12Shelf_ObjectIdentity = ObjectIdentity
nokiaTPS12Shelf = _NokiaTPS12Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 136)
)
if mibBuilder.loadTexts:
    nokiaTPS12Shelf.setStatus("current")
_NokiaDmCt05LmShelf_ObjectIdentity = ObjectIdentity
nokiaDmCt05LmShelf = _NokiaDmCt05LmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 137)
)
if mibBuilder.loadTexts:
    nokiaDmCt05LmShelf.setStatus("current")
_NokiaDmCt10LmShelf_ObjectIdentity = ObjectIdentity
nokiaDmCt10LmShelf = _NokiaDmCt10LmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 138)
)
if mibBuilder.loadTexts:
    nokiaDmCt10LmShelf.setStatus("current")
_NokiaDmIt05LmShelf_ObjectIdentity = ObjectIdentity
nokiaDmIt05LmShelf = _NokiaDmIt05LmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 139)
)
if mibBuilder.loadTexts:
    nokiaDmIt05LmShelf.setStatus("current")
_NokiaDmIt10LmShelf_ObjectIdentity = ObjectIdentity
nokiaDmIt10LmShelf = _NokiaDmIt10LmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 140)
)
if mibBuilder.loadTexts:
    nokiaDmIt10LmShelf.setStatus("current")
_AluWdmPSIMXUniversalShelf_ObjectIdentity = ObjectIdentity
aluWdmPSIMXUniversalShelf = _AluWdmPSIMXUniversalShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 141)
)
if mibBuilder.loadTexts:
    aluWdmPSIMXUniversalShelf.setStatus("current")
_AluWdmMlfsbShelf_ObjectIdentity = ObjectIdentity
aluWdmMlfsbShelf = _AluWdmMlfsbShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 142)
)
if mibBuilder.loadTexts:
    aluWdmMlfsbShelf.setStatus("current")
_NokiaSfd5AShelf_ObjectIdentity = ObjectIdentity
nokiaSfd5AShelf = _NokiaSfd5AShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 143)
)
if mibBuilder.loadTexts:
    nokiaSfd5AShelf.setStatus("current")
_NokiaSfd5BShelf_ObjectIdentity = ObjectIdentity
nokiaSfd5BShelf = _NokiaSfd5BShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 144)
)
if mibBuilder.loadTexts:
    nokiaSfd5BShelf.setStatus("current")
_NokiaSfd5CShelf_ObjectIdentity = ObjectIdentity
nokiaSfd5CShelf = _NokiaSfd5CShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 145)
)
if mibBuilder.loadTexts:
    nokiaSfd5CShelf.setStatus("current")
_NokiaSfd5DShelf_ObjectIdentity = ObjectIdentity
nokiaSfd5DShelf = _NokiaSfd5DShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 146)
)
if mibBuilder.loadTexts:
    nokiaSfd5DShelf.setStatus("current")
_NokiaSfd5ADShelf_ObjectIdentity = ObjectIdentity
nokiaSfd5ADShelf = _NokiaSfd5ADShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 147)
)
if mibBuilder.loadTexts:
    nokiaSfd5ADShelf.setStatus("current")
_NokiaSfd5BDShelf_ObjectIdentity = ObjectIdentity
nokiaSfd5BDShelf = _NokiaSfd5BDShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 148)
)
if mibBuilder.loadTexts:
    nokiaSfd5BDShelf.setStatus("current")
_NokiaSfd5CDShelf_ObjectIdentity = ObjectIdentity
nokiaSfd5CDShelf = _NokiaSfd5CDShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 149)
)
if mibBuilder.loadTexts:
    nokiaSfd5CDShelf.setStatus("current")
_NokiaSfd5DDShelf_ObjectIdentity = ObjectIdentity
nokiaSfd5DDShelf = _NokiaSfd5DDShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 150)
)
if mibBuilder.loadTexts:
    nokiaSfd5DDShelf.setStatus("current")
_NokiaSfd5AUShelf_ObjectIdentity = ObjectIdentity
nokiaSfd5AUShelf = _NokiaSfd5AUShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 151)
)
if mibBuilder.loadTexts:
    nokiaSfd5AUShelf.setStatus("current")
_NokiaSfd5BUShelf_ObjectIdentity = ObjectIdentity
nokiaSfd5BUShelf = _NokiaSfd5BUShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 152)
)
if mibBuilder.loadTexts:
    nokiaSfd5BUShelf.setStatus("current")
_NokiaSfd5CUShelf_ObjectIdentity = ObjectIdentity
nokiaSfd5CUShelf = _NokiaSfd5CUShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 153)
)
if mibBuilder.loadTexts:
    nokiaSfd5CUShelf.setStatus("current")
_NokiaSfd5DUShelf_ObjectIdentity = ObjectIdentity
nokiaSfd5DUShelf = _NokiaSfd5DUShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 154)
)
if mibBuilder.loadTexts:
    nokiaSfd5DUShelf.setStatus("current")
_NokiaDcm2pShelf_ObjectIdentity = ObjectIdentity
nokiaDcm2pShelf = _NokiaDcm2pShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 155)
)
if mibBuilder.loadTexts:
    nokiaDcm2pShelf.setStatus("current")
_NokiaSAS24Shelf_ObjectIdentity = ObjectIdentity
nokiaSAS24Shelf = _NokiaSAS24Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 156)
)
if mibBuilder.loadTexts:
    nokiaSAS24Shelf.setStatus("current")
_NokiaMsh8aShelf_ObjectIdentity = ObjectIdentity
nokiaMsh8aShelf = _NokiaMsh8aShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 157)
)
if mibBuilder.loadTexts:
    nokiaMsh8aShelf.setStatus("current")
_NokiaSfd48Shelf_ObjectIdentity = ObjectIdentity
nokiaSfd48Shelf = _NokiaSfd48Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 158)
)
if mibBuilder.loadTexts:
    nokiaSfd48Shelf.setStatus("current")
_NokiaSfd64Shelf_ObjectIdentity = ObjectIdentity
nokiaSfd64Shelf = _NokiaSfd64Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 4, 159)
)
if mibBuilder.loadTexts:
    nokiaSfd64Shelf.setStatus("current")
_TropicCardReg_ObjectIdentity = ObjectIdentity
tropicCardReg = _TropicCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5)
)
if mibBuilder.loadTexts:
    tropicCardReg.setStatus("current")
_TropicMiscCardReg_ObjectIdentity = ObjectIdentity
tropicMiscCardReg = _TropicMiscCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tropicMiscCardReg.setStatus("current")
_TropicEmptyCard_ObjectIdentity = ObjectIdentity
tropicEmptyCard = _TropicEmptyCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tropicEmptyCard.setStatus("current")
_TropicUnknownCard_ObjectIdentity = ObjectIdentity
tropicUnknownCard = _TropicUnknownCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    tropicUnknownCard.setStatus("current")
_TropicInvalidCard_ObjectIdentity = ObjectIdentity
tropicInvalidCard = _TropicInvalidCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    tropicInvalidCard.setStatus("current")
_TropicReservedCard_ObjectIdentity = ObjectIdentity
tropicReservedCard = _TropicReservedCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    tropicReservedCard.setStatus("current")
_TropicHalfHeightCarrierCard_ObjectIdentity = ObjectIdentity
tropicHalfHeightCarrierCard = _TropicHalfHeightCarrierCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 5)
)
if mibBuilder.loadTexts:
    tropicHalfHeightCarrierCard.setStatus("current")
_AluWdmVirtualCard_ObjectIdentity = ObjectIdentity
aluWdmVirtualCard = _AluWdmVirtualCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 6)
)
if mibBuilder.loadTexts:
    aluWdmVirtualCard.setStatus("current")
_AluWdmGmreCard_ObjectIdentity = ObjectIdentity
aluWdmGmreCard = _AluWdmGmreCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 7)
)
if mibBuilder.loadTexts:
    aluWdmGmreCard.setStatus("current")
_AluWdmMsh8fsmCard_ObjectIdentity = ObjectIdentity
aluWdmMsh8fsmCard = _AluWdmMsh8fsmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 8)
)
if mibBuilder.loadTexts:
    aluWdmMsh8fsmCard.setStatus("current")
_AluWdmIroadmvCard_ObjectIdentity = ObjectIdentity
aluWdmIroadmvCard = _AluWdmIroadmvCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 9)
)
if mibBuilder.loadTexts:
    aluWdmIroadmvCard.setStatus("current")
_AluWdmIroadmfCard_ObjectIdentity = ObjectIdentity
aluWdmIroadmfCard = _AluWdmIroadmfCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 10)
)
if mibBuilder.loadTexts:
    aluWdmIroadmfCard.setStatus("current")
_AluWdmIroadm9mCard_ObjectIdentity = ObjectIdentity
aluWdmIroadm9mCard = _AluWdmIroadm9mCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 11)
)
if mibBuilder.loadTexts:
    aluWdmIroadm9mCard.setStatus("current")
_AluWdmIroadm9rCard_ObjectIdentity = ObjectIdentity
aluWdmIroadm9rCard = _AluWdmIroadm9rCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 12)
)
if mibBuilder.loadTexts:
    aluWdmIroadm9rCard.setStatus("current")
_AluWdmIroadm20Card_ObjectIdentity = ObjectIdentity
aluWdmIroadm20Card = _AluWdmIroadm20Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 13)
)
if mibBuilder.loadTexts:
    aluWdmIroadm20Card.setStatus("current")
_AluWdmSplit2Card_ObjectIdentity = ObjectIdentity
aluWdmSplit2Card = _AluWdmSplit2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 14)
)
if mibBuilder.loadTexts:
    aluWdmSplit2Card.setStatus("current")
_AluWdmOscCplrCard_ObjectIdentity = ObjectIdentity
aluWdmOscCplrCard = _AluWdmOscCplrCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 15)
)
if mibBuilder.loadTexts:
    aluWdmOscCplrCard.setStatus("current")
_AluWdmMsh4fsbCard_ObjectIdentity = ObjectIdentity
aluWdmMsh4fsbCard = _AluWdmMsh4fsbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 16)
)
if mibBuilder.loadTexts:
    aluWdmMsh4fsbCard.setStatus("current")
_AluWdmIpreampCard_ObjectIdentity = ObjectIdentity
aluWdmIpreampCard = _AluWdmIpreampCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 17)
)
if mibBuilder.loadTexts:
    aluWdmIpreampCard.setStatus("current")
_NokiaSfd2ACard_ObjectIdentity = ObjectIdentity
nokiaSfd2ACard = _NokiaSfd2ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 18)
)
if mibBuilder.loadTexts:
    nokiaSfd2ACard.setStatus("current")
_NokiaSfd2BCard_ObjectIdentity = ObjectIdentity
nokiaSfd2BCard = _NokiaSfd2BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 19)
)
if mibBuilder.loadTexts:
    nokiaSfd2BCard.setStatus("current")
_NokiaSfd2CCard_ObjectIdentity = ObjectIdentity
nokiaSfd2CCard = _NokiaSfd2CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 20)
)
if mibBuilder.loadTexts:
    nokiaSfd2CCard.setStatus("current")
_NokiaSfd2DCard_ObjectIdentity = ObjectIdentity
nokiaSfd2DCard = _NokiaSfd2DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 21)
)
if mibBuilder.loadTexts:
    nokiaSfd2DCard.setStatus("current")
_NokiaSfd2ECard_ObjectIdentity = ObjectIdentity
nokiaSfd2ECard = _NokiaSfd2ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 22)
)
if mibBuilder.loadTexts:
    nokiaSfd2ECard.setStatus("current")
_NokiaSfd2FCard_ObjectIdentity = ObjectIdentity
nokiaSfd2FCard = _NokiaSfd2FCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 23)
)
if mibBuilder.loadTexts:
    nokiaSfd2FCard.setStatus("current")
_NokiaSfd2GCard_ObjectIdentity = ObjectIdentity
nokiaSfd2GCard = _NokiaSfd2GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 24)
)
if mibBuilder.loadTexts:
    nokiaSfd2GCard.setStatus("current")
_NokiaSfd2HCard_ObjectIdentity = ObjectIdentity
nokiaSfd2HCard = _NokiaSfd2HCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 25)
)
if mibBuilder.loadTexts:
    nokiaSfd2HCard.setStatus("current")
_NokiaSfd2ICard_ObjectIdentity = ObjectIdentity
nokiaSfd2ICard = _NokiaSfd2ICard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 26)
)
if mibBuilder.loadTexts:
    nokiaSfd2ICard.setStatus("current")
_NokiaSfd2LCard_ObjectIdentity = ObjectIdentity
nokiaSfd2LCard = _NokiaSfd2LCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 27)
)
if mibBuilder.loadTexts:
    nokiaSfd2LCard.setStatus("current")
_NokiaSfd2MCard_ObjectIdentity = ObjectIdentity
nokiaSfd2MCard = _NokiaSfd2MCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 28)
)
if mibBuilder.loadTexts:
    nokiaSfd2MCard.setStatus("current")
_NokiaSfd2NCard_ObjectIdentity = ObjectIdentity
nokiaSfd2NCard = _NokiaSfd2NCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 29)
)
if mibBuilder.loadTexts:
    nokiaSfd2NCard.setStatus("current")
_NokiaSfd2OCard_ObjectIdentity = ObjectIdentity
nokiaSfd2OCard = _NokiaSfd2OCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 30)
)
if mibBuilder.loadTexts:
    nokiaSfd2OCard.setStatus("current")
_NokiaSfd2PCard_ObjectIdentity = ObjectIdentity
nokiaSfd2PCard = _NokiaSfd2PCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 31)
)
if mibBuilder.loadTexts:
    nokiaSfd2PCard.setStatus("current")
_NokiaSfd2QCard_ObjectIdentity = ObjectIdentity
nokiaSfd2QCard = _NokiaSfd2QCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 32)
)
if mibBuilder.loadTexts:
    nokiaSfd2QCard.setStatus("current")
_NokiaSfd2RCard_ObjectIdentity = ObjectIdentity
nokiaSfd2RCard = _NokiaSfd2RCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 33)
)
if mibBuilder.loadTexts:
    nokiaSfd2RCard.setStatus("current")
_NokiaSfd4ACard_ObjectIdentity = ObjectIdentity
nokiaSfd4ACard = _NokiaSfd4ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 34)
)
if mibBuilder.loadTexts:
    nokiaSfd4ACard.setStatus("current")
_NokiaSfd4BCard_ObjectIdentity = ObjectIdentity
nokiaSfd4BCard = _NokiaSfd4BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 35)
)
if mibBuilder.loadTexts:
    nokiaSfd4BCard.setStatus("current")
_NokiaSfd4CCard_ObjectIdentity = ObjectIdentity
nokiaSfd4CCard = _NokiaSfd4CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 36)
)
if mibBuilder.loadTexts:
    nokiaSfd4CCard.setStatus("current")
_NokiaSfd4DCard_ObjectIdentity = ObjectIdentity
nokiaSfd4DCard = _NokiaSfd4DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 37)
)
if mibBuilder.loadTexts:
    nokiaSfd4DCard.setStatus("current")
_NokiaSfd4ECard_ObjectIdentity = ObjectIdentity
nokiaSfd4ECard = _NokiaSfd4ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 38)
)
if mibBuilder.loadTexts:
    nokiaSfd4ECard.setStatus("current")
_NokiaSfd4FCard_ObjectIdentity = ObjectIdentity
nokiaSfd4FCard = _NokiaSfd4FCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 39)
)
if mibBuilder.loadTexts:
    nokiaSfd4FCard.setStatus("current")
_NokiaSfd4GCard_ObjectIdentity = ObjectIdentity
nokiaSfd4GCard = _NokiaSfd4GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 40)
)
if mibBuilder.loadTexts:
    nokiaSfd4GCard.setStatus("current")
_NokiaSfd4HCard_ObjectIdentity = ObjectIdentity
nokiaSfd4HCard = _NokiaSfd4HCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 41)
)
if mibBuilder.loadTexts:
    nokiaSfd4HCard.setStatus("current")
_NokiaSfd8ACard_ObjectIdentity = ObjectIdentity
nokiaSfd8ACard = _NokiaSfd8ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 42)
)
if mibBuilder.loadTexts:
    nokiaSfd8ACard.setStatus("current")
_NokiaSfd8BCard_ObjectIdentity = ObjectIdentity
nokiaSfd8BCard = _NokiaSfd8BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 43)
)
if mibBuilder.loadTexts:
    nokiaSfd8BCard.setStatus("current")
_NokiaSfd8CCard_ObjectIdentity = ObjectIdentity
nokiaSfd8CCard = _NokiaSfd8CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 44)
)
if mibBuilder.loadTexts:
    nokiaSfd8CCard.setStatus("current")
_NokiaSfd8DCard_ObjectIdentity = ObjectIdentity
nokiaSfd8DCard = _NokiaSfd8DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 45)
)
if mibBuilder.loadTexts:
    nokiaSfd8DCard.setStatus("current")
_NokiaSfc1ACard_ObjectIdentity = ObjectIdentity
nokiaSfc1ACard = _NokiaSfc1ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 46)
)
if mibBuilder.loadTexts:
    nokiaSfc1ACard.setStatus("current")
_NokiaSfc1BCard_ObjectIdentity = ObjectIdentity
nokiaSfc1BCard = _NokiaSfc1BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 47)
)
if mibBuilder.loadTexts:
    nokiaSfc1BCard.setStatus("current")
_NokiaSfc1CCard_ObjectIdentity = ObjectIdentity
nokiaSfc1CCard = _NokiaSfc1CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 48)
)
if mibBuilder.loadTexts:
    nokiaSfc1CCard.setStatus("current")
_NokiaSfc1DCard_ObjectIdentity = ObjectIdentity
nokiaSfc1DCard = _NokiaSfc1DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 49)
)
if mibBuilder.loadTexts:
    nokiaSfc1DCard.setStatus("current")
_NokiaSfc1ECard_ObjectIdentity = ObjectIdentity
nokiaSfc1ECard = _NokiaSfc1ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 50)
)
if mibBuilder.loadTexts:
    nokiaSfc1ECard.setStatus("current")
_NokiaSfc1FCard_ObjectIdentity = ObjectIdentity
nokiaSfc1FCard = _NokiaSfc1FCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 51)
)
if mibBuilder.loadTexts:
    nokiaSfc1FCard.setStatus("current")
_NokiaSfc1GCard_ObjectIdentity = ObjectIdentity
nokiaSfc1GCard = _NokiaSfc1GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 52)
)
if mibBuilder.loadTexts:
    nokiaSfc1GCard.setStatus("current")
_NokiaSfc1HCard_ObjectIdentity = ObjectIdentity
nokiaSfc1HCard = _NokiaSfc1HCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 53)
)
if mibBuilder.loadTexts:
    nokiaSfc1HCard.setStatus("current")
_NokiaSfc2ABCard_ObjectIdentity = ObjectIdentity
nokiaSfc2ABCard = _NokiaSfc2ABCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 54)
)
if mibBuilder.loadTexts:
    nokiaSfc2ABCard.setStatus("current")
_NokiaSfc2CDCard_ObjectIdentity = ObjectIdentity
nokiaSfc2CDCard = _NokiaSfc2CDCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 55)
)
if mibBuilder.loadTexts:
    nokiaSfc2CDCard.setStatus("current")
_NokiaSfc2EFCard_ObjectIdentity = ObjectIdentity
nokiaSfc2EFCard = _NokiaSfc2EFCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 56)
)
if mibBuilder.loadTexts:
    nokiaSfc2EFCard.setStatus("current")
_NokiaSfc2GHCard_ObjectIdentity = ObjectIdentity
nokiaSfc2GHCard = _NokiaSfc2GHCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 57)
)
if mibBuilder.loadTexts:
    nokiaSfc2GHCard.setStatus("current")
_NokiaSfc4ADCard_ObjectIdentity = ObjectIdentity
nokiaSfc4ADCard = _NokiaSfc4ADCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 58)
)
if mibBuilder.loadTexts:
    nokiaSfc4ADCard.setStatus("current")
_NokiaSfc4EHCard_ObjectIdentity = ObjectIdentity
nokiaSfc4EHCard = _NokiaSfc4EHCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 59)
)
if mibBuilder.loadTexts:
    nokiaSfc4EHCard.setStatus("current")
_NokiaSfc8UCard_ObjectIdentity = ObjectIdentity
nokiaSfc8UCard = _NokiaSfc8UCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 60)
)
if mibBuilder.loadTexts:
    nokiaSfc8UCard.setStatus("current")
_NokiaSfc8LCard_ObjectIdentity = ObjectIdentity
nokiaSfc8LCard = _NokiaSfc8LCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 61)
)
if mibBuilder.loadTexts:
    nokiaSfc8LCard.setStatus("current")
_NokiaSARO2ACard_ObjectIdentity = ObjectIdentity
nokiaSARO2ACard = _NokiaSARO2ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 62)
)
if mibBuilder.loadTexts:
    nokiaSARO2ACard.setStatus("current")
_NokiaSARO2BCard_ObjectIdentity = ObjectIdentity
nokiaSARO2BCard = _NokiaSARO2BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 63)
)
if mibBuilder.loadTexts:
    nokiaSARO2BCard.setStatus("current")
_NokiaSARO2CCard_ObjectIdentity = ObjectIdentity
nokiaSARO2CCard = _NokiaSARO2CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 64)
)
if mibBuilder.loadTexts:
    nokiaSARO2CCard.setStatus("current")
_NokiaSARO2DCard_ObjectIdentity = ObjectIdentity
nokiaSARO2DCard = _NokiaSARO2DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 65)
)
if mibBuilder.loadTexts:
    nokiaSARO2DCard.setStatus("current")
_NokiaSARO2ECard_ObjectIdentity = ObjectIdentity
nokiaSARO2ECard = _NokiaSARO2ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 66)
)
if mibBuilder.loadTexts:
    nokiaSARO2ECard.setStatus("current")
_NokiaSARO2FCard_ObjectIdentity = ObjectIdentity
nokiaSARO2FCard = _NokiaSARO2FCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 67)
)
if mibBuilder.loadTexts:
    nokiaSARO2FCard.setStatus("current")
_NokiaSARO2GCard_ObjectIdentity = ObjectIdentity
nokiaSARO2GCard = _NokiaSARO2GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 68)
)
if mibBuilder.loadTexts:
    nokiaSARO2GCard.setStatus("current")
_NokiaSARO2HCard_ObjectIdentity = ObjectIdentity
nokiaSARO2HCard = _NokiaSARO2HCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 69)
)
if mibBuilder.loadTexts:
    nokiaSARO2HCard.setStatus("current")
_NokiaSARO4ACard_ObjectIdentity = ObjectIdentity
nokiaSARO4ACard = _NokiaSARO4ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 70)
)
if mibBuilder.loadTexts:
    nokiaSARO4ACard.setStatus("current")
_NokiaSARO4BCard_ObjectIdentity = ObjectIdentity
nokiaSARO4BCard = _NokiaSARO4BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 71)
)
if mibBuilder.loadTexts:
    nokiaSARO4BCard.setStatus("current")
_NokiaSARO4CCard_ObjectIdentity = ObjectIdentity
nokiaSARO4CCard = _NokiaSARO4CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 72)
)
if mibBuilder.loadTexts:
    nokiaSARO4CCard.setStatus("current")
_NokiaSARO4DCard_ObjectIdentity = ObjectIdentity
nokiaSARO4DCard = _NokiaSARO4DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 73)
)
if mibBuilder.loadTexts:
    nokiaSARO4DCard.setStatus("current")
_NokiaSARO8ACard_ObjectIdentity = ObjectIdentity
nokiaSARO8ACard = _NokiaSARO8ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 74)
)
if mibBuilder.loadTexts:
    nokiaSARO8ACard.setStatus("current")
_NokiaSARO8BCard_ObjectIdentity = ObjectIdentity
nokiaSARO8BCard = _NokiaSARO8BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 75)
)
if mibBuilder.loadTexts:
    nokiaSARO8BCard.setStatus("current")
_NokiaLR4BOCCard_ObjectIdentity = ObjectIdentity
nokiaLR4BOCCard = _NokiaLR4BOCCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 76)
)
if mibBuilder.loadTexts:
    nokiaLR4BOCCard.setStatus("current")
_AluWdmIrdm32Card_ObjectIdentity = ObjectIdentity
aluWdmIrdm32Card = _AluWdmIrdm32Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 77)
)
if mibBuilder.loadTexts:
    aluWdmIrdm32Card.setStatus("current")
_AluWdmOpenIrdm32Card_ObjectIdentity = ObjectIdentity
aluWdmOpenIrdm32Card = _AluWdmOpenIrdm32Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 78)
)
if mibBuilder.loadTexts:
    aluWdmOpenIrdm32Card.setStatus("current")
_AluWdmIrdm32lCard_ObjectIdentity = ObjectIdentity
aluWdmIrdm32lCard = _AluWdmIrdm32lCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 79)
)
if mibBuilder.loadTexts:
    aluWdmIrdm32lCard.setStatus("current")
_AluWdmOpenIrdm32LCard_ObjectIdentity = ObjectIdentity
aluWdmOpenIrdm32LCard = _AluWdmOpenIrdm32LCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 80)
)
if mibBuilder.loadTexts:
    aluWdmOpenIrdm32LCard.setStatus("current")
_AluWdmOpenEilaCard_ObjectIdentity = ObjectIdentity
aluWdmOpenEilaCard = _AluWdmOpenEilaCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 81)
)
if mibBuilder.loadTexts:
    aluWdmOpenEilaCard.setStatus("current")
_AluWdmEsreCard_ObjectIdentity = ObjectIdentity
aluWdmEsreCard = _AluWdmEsreCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 82)
)
if mibBuilder.loadTexts:
    aluWdmEsreCard.setStatus("current")
_AluWdmOmdclCard_ObjectIdentity = ObjectIdentity
aluWdmOmdclCard = _AluWdmOmdclCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 83)
)
if mibBuilder.loadTexts:
    aluWdmOmdclCard.setStatus("current")
_AluWdmOpenOmdclCard_ObjectIdentity = ObjectIdentity
aluWdmOpenOmdclCard = _AluWdmOpenOmdclCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 84)
)
if mibBuilder.loadTexts:
    aluWdmOpenOmdclCard.setStatus("current")
_AluWdmEilaLCard_ObjectIdentity = ObjectIdentity
aluWdmEilaLCard = _AluWdmEilaLCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 85)
)
if mibBuilder.loadTexts:
    aluWdmEilaLCard.setStatus("current")
_AluWdmOpenEilaLCard_ObjectIdentity = ObjectIdentity
aluWdmOpenEilaLCard = _AluWdmOpenEilaLCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 86)
)
if mibBuilder.loadTexts:
    aluWdmOpenEilaLCard.setStatus("current")
_AluWdmMlfsbCard_ObjectIdentity = ObjectIdentity
aluWdmMlfsbCard = _AluWdmMlfsbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 88)
)
if mibBuilder.loadTexts:
    aluWdmMlfsbCard.setStatus("current")
_NokiaIr9Card_ObjectIdentity = ObjectIdentity
nokiaIr9Card = _NokiaIr9Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 89)
)
if mibBuilder.loadTexts:
    nokiaIr9Card.setStatus("current")
_NokiaTic48TCard_ObjectIdentity = ObjectIdentity
nokiaTic48TCard = _NokiaTic48TCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 90)
)
if mibBuilder.loadTexts:
    nokiaTic48TCard.setStatus("current")
_NokiaMsh8aCard_ObjectIdentity = ObjectIdentity
nokiaMsh8aCard = _NokiaMsh8aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 91)
)
if mibBuilder.loadTexts:
    nokiaMsh8aCard.setStatus("current")
_NokiaIr4Card_ObjectIdentity = ObjectIdentity
nokiaIr4Card = _NokiaIr4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 92)
)
if mibBuilder.loadTexts:
    nokiaIr4Card.setStatus("current")
_NokiaIr32AWCard_ObjectIdentity = ObjectIdentity
nokiaIr32AWCard = _NokiaIr32AWCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 93)
)
if mibBuilder.loadTexts:
    nokiaIr32AWCard.setStatus("current")
_NokiaOpenIr32AWCard_ObjectIdentity = ObjectIdentity
nokiaOpenIr32AWCard = _NokiaOpenIr32AWCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 94)
)
if mibBuilder.loadTexts:
    nokiaOpenIr32AWCard.setStatus("current")
_NokiaEilaAWCard_ObjectIdentity = ObjectIdentity
nokiaEilaAWCard = _NokiaEilaAWCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 95)
)
if mibBuilder.loadTexts:
    nokiaEilaAWCard.setStatus("current")
_NokiaOpenEilaAWCard_ObjectIdentity = ObjectIdentity
nokiaOpenEilaAWCard = _NokiaOpenEilaAWCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 96)
)
if mibBuilder.loadTexts:
    nokiaOpenEilaAWCard.setStatus("current")
_TropicControlCardReg_ObjectIdentity = ObjectIdentity
tropicControlCardReg = _TropicControlCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tropicControlCardReg.setStatus("current")
_TropicMasterControlCard_ObjectIdentity = ObjectIdentity
tropicMasterControlCard = _TropicMasterControlCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    tropicMasterControlCard.setStatus("current")
_AluWdmEquipmentControllerCard_ObjectIdentity = ObjectIdentity
aluWdmEquipmentControllerCard = _AluWdmEquipmentControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    aluWdmEquipmentControllerCard.setStatus("current")
_AluWdmFirstLevelControllerCard_ObjectIdentity = ObjectIdentity
aluWdmFirstLevelControllerCard = _AluWdmFirstLevelControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    aluWdmFirstLevelControllerCard.setStatus("current")
_AluWdmMatrix3T8Card_ObjectIdentity = ObjectIdentity
aluWdmMatrix3T8Card = _AluWdmMatrix3T8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    aluWdmMatrix3T8Card.setStatus("current")
_AluWdmMatrix1T9Card_ObjectIdentity = ObjectIdentity
aluWdmMatrix1T9Card = _AluWdmMatrix1T9Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 7)
)
if mibBuilder.loadTexts:
    aluWdmMatrix1T9Card.setStatus("current")
_AluWdmPSS4EquipmentControllerCard_ObjectIdentity = ObjectIdentity
aluWdmPSS4EquipmentControllerCard = _AluWdmPSS4EquipmentControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 8)
)
if mibBuilder.loadTexts:
    aluWdmPSS4EquipmentControllerCard.setStatus("current")
_AluWdmMatrix0CompactCard_ObjectIdentity = ObjectIdentity
aluWdmMatrix0CompactCard = _AluWdmMatrix0CompactCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 9)
)
if mibBuilder.loadTexts:
    aluWdmMatrix0CompactCard.setStatus("current")
_AluWdmUniversalMatrixFirstLevelControllerCard_ObjectIdentity = ObjectIdentity
aluWdmUniversalMatrixFirstLevelControllerCard = _AluWdmUniversalMatrixFirstLevelControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 10)
)
if mibBuilder.loadTexts:
    aluWdmUniversalMatrixFirstLevelControllerCard.setStatus("current")
_AluWdmEndOfShelfMiddleCard_ObjectIdentity = ObjectIdentity
aluWdmEndOfShelfMiddleCard = _AluWdmEndOfShelfMiddleCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 12)
)
if mibBuilder.loadTexts:
    aluWdmEndOfShelfMiddleCard.setStatus("current")
_AluWdmUniversalMatrixFirstLevelController1p2TCard_ObjectIdentity = ObjectIdentity
aluWdmUniversalMatrixFirstLevelController1p2TCard = _AluWdmUniversalMatrixFirstLevelController1p2TCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 14)
)
if mibBuilder.loadTexts:
    aluWdmUniversalMatrixFirstLevelController1p2TCard.setStatus("current")
_AluWdmPSS8EquipmentController2Card_ObjectIdentity = ObjectIdentity
aluWdmPSS8EquipmentController2Card = _AluWdmPSS8EquipmentController2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 15)
)
if mibBuilder.loadTexts:
    aluWdmPSS8EquipmentController2Card.setStatus("current")
_AluWdmPSS32EquipmentController2Card_ObjectIdentity = ObjectIdentity
aluWdmPSS32EquipmentController2Card = _AluWdmPSS32EquipmentController2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 17)
)
if mibBuilder.loadTexts:
    aluWdmPSS32EquipmentController2Card.setStatus("current")
_AluWdmClockControllerCard96Card_ObjectIdentity = ObjectIdentity
aluWdmClockControllerCard96Card = _AluWdmClockControllerCard96Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 18)
)
if mibBuilder.loadTexts:
    aluWdmClockControllerCard96Card.setStatus("current")
_AluWdmVwmCwEquipmentControllerCard_ObjectIdentity = ObjectIdentity
aluWdmVwmCwEquipmentControllerCard = _AluWdmVwmCwEquipmentControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 19)
)
if mibBuilder.loadTexts:
    aluWdmVwmCwEquipmentControllerCard.setStatus("current")
_AluWdmVwmDwEquipmentControllerCard_ObjectIdentity = ObjectIdentity
aluWdmVwmDwEquipmentControllerCard = _AluWdmVwmDwEquipmentControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 20)
)
if mibBuilder.loadTexts:
    aluWdmVwmDwEquipmentControllerCard.setStatus("current")
_AluWdmPSS8EquipmentController2EncryptionCard_ObjectIdentity = ObjectIdentity
aluWdmPSS8EquipmentController2EncryptionCard = _AluWdmPSS8EquipmentController2EncryptionCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 21)
)
if mibBuilder.loadTexts:
    aluWdmPSS8EquipmentController2EncryptionCard.setStatus("current")
_AluWdmPSS32EquipmentController2EncryptionCard_ObjectIdentity = ObjectIdentity
aluWdmPSS32EquipmentController2EncryptionCard = _AluWdmPSS32EquipmentController2EncryptionCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 22)
)
if mibBuilder.loadTexts:
    aluWdmPSS32EquipmentController2EncryptionCard.setStatus("current")
_AluWdmPSIEquipmentController2Card_ObjectIdentity = ObjectIdentity
aluWdmPSIEquipmentController2Card = _AluWdmPSIEquipmentController2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 23)
)
if mibBuilder.loadTexts:
    aluWdmPSIEquipmentController2Card.setStatus("current")
_AluWdmPSS8xClockEquipmentController2Card_ObjectIdentity = ObjectIdentity
aluWdmPSS8xClockEquipmentController2Card = _AluWdmPSS8xClockEquipmentController2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 24)
)
if mibBuilder.loadTexts:
    aluWdmPSS8xClockEquipmentController2Card.setStatus("current")
_NokiaVwmMsOsu20Card_ObjectIdentity = ObjectIdentity
nokiaVwmMsOsu20Card = _NokiaVwmMsOsu20Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 25)
)
if mibBuilder.loadTexts:
    nokiaVwmMsOsu20Card.setStatus("current")
_NokiaVwmMsTlu9Card_ObjectIdentity = ObjectIdentity
nokiaVwmMsTlu9Card = _NokiaVwmMsTlu9Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 26)
)
if mibBuilder.loadTexts:
    nokiaVwmMsTlu9Card.setStatus("current")
_NokiaVwmMsPmu9UcCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmu9UcCard = _NokiaVwmMsPmu9UcCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 27)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmu9UcCard.setStatus("current")
_NokiaVwmMsPmu9LcCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmu9LcCard = _NokiaVwmMsPmu9LcCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 28)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmu9LcCard.setStatus("current")
_NokiaVwmMsPmu9UcmCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmu9UcmCard = _NokiaVwmMsPmu9UcmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 29)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmu9UcmCard.setStatus("current")
_NokiaVwmMsPmu9LcmCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmu9LcmCard = _NokiaVwmMsPmu9LcmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 30)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmu9LcmCard.setStatus("current")
_NokiaVwmMsItp4UcaCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsItp4UcaCard = _NokiaVwmMsItp4UcaCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 31)
)
if mibBuilder.loadTexts:
    nokiaVwmMsItp4UcaCard.setStatus("current")
_NokiaVwmMsItp4UcbCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsItp4UcbCard = _NokiaVwmMsItp4UcbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 32)
)
if mibBuilder.loadTexts:
    nokiaVwmMsItp4UcbCard.setStatus("current")
_NokiaVwmMsItp4LcaCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsItp4LcaCard = _NokiaVwmMsItp4LcaCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 33)
)
if mibBuilder.loadTexts:
    nokiaVwmMsItp4LcaCard.setStatus("current")
_NokiaVwmMsItp4LcbCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsItp4LcbCard = _NokiaVwmMsItp4LcbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 34)
)
if mibBuilder.loadTexts:
    nokiaVwmMsItp4LcbCard.setStatus("current")
_NokiaVwmMsSmmAoCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsSmmAoCard = _NokiaVwmMsSmmAoCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 35)
)
if mibBuilder.loadTexts:
    nokiaVwmMsSmmAoCard.setStatus("current")
_NokiaVwmMsSmmAiCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsSmmAiCard = _NokiaVwmMsSmmAiCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 36)
)
if mibBuilder.loadTexts:
    nokiaVwmMsSmmAiCard.setStatus("current")
_NokiaVwmMsOpsEmuCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsOpsEmuCard = _NokiaVwmMsOpsEmuCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 37)
)
if mibBuilder.loadTexts:
    nokiaVwmMsOpsEmuCard.setStatus("current")
_NokiaPsdCard_ObjectIdentity = ObjectIdentity
nokiaPsdCard = _NokiaPsdCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 38)
)
if mibBuilder.loadTexts:
    nokiaPsdCard.setStatus("current")
_NokiaVwmMsTlu9mCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsTlu9mCard = _NokiaVwmMsTlu9mCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 39)
)
if mibBuilder.loadTexts:
    nokiaVwmMsTlu9mCard.setStatus("current")
_AluWdmMiniEquipmentController2Card_ObjectIdentity = ObjectIdentity
aluWdmMiniEquipmentController2Card = _AluWdmMiniEquipmentController2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 40)
)
if mibBuilder.loadTexts:
    aluWdmMiniEquipmentController2Card.setStatus("current")
_AluWdmPSS12xClockEquipmentController2Card_ObjectIdentity = ObjectIdentity
aluWdmPSS12xClockEquipmentController2Card = _AluWdmPSS12xClockEquipmentController2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 41)
)
if mibBuilder.loadTexts:
    aluWdmPSS12xClockEquipmentController2Card.setStatus("current")
_NokiaVwmMsPmuD21ACard_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmuD21ACard = _NokiaVwmMsPmuD21ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 42)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmuD21ACard.setStatus("current")
_NokiaVwmMsPmuD21BCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmuD21BCard = _NokiaVwmMsPmuD21BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 43)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmuD21BCard.setStatus("current")
_NokiaVwmMsPmuD21CCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmuD21CCard = _NokiaVwmMsPmuD21CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 44)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmuD21CCard.setStatus("current")
_NokiaVwmMsPmuD21DCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsPmuD21DCard = _NokiaVwmMsPmuD21DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 45)
)
if mibBuilder.loadTexts:
    nokiaVwmMsPmuD21DCard.setStatus("current")
_NokiaVwmMsTlu200Card_ObjectIdentity = ObjectIdentity
nokiaVwmMsTlu200Card = _NokiaVwmMsTlu200Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 46)
)
if mibBuilder.loadTexts:
    nokiaVwmMsTlu200Card.setStatus("current")
_NokiaVwmMsADVGICard_ObjectIdentity = ObjectIdentity
nokiaVwmMsADVGICard = _NokiaVwmMsADVGICard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 47)
)
if mibBuilder.loadTexts:
    nokiaVwmMsADVGICard.setStatus("current")
_AluWdmMini32GEquipmentController2Card_ObjectIdentity = ObjectIdentity
aluWdmMini32GEquipmentController2Card = _AluWdmMini32GEquipmentController2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 48)
)
if mibBuilder.loadTexts:
    aluWdmMini32GEquipmentController2Card.setStatus("current")
_NokiaTPS24EquipmentControllerCard_ObjectIdentity = ObjectIdentity
nokiaTPS24EquipmentControllerCard = _NokiaTPS24EquipmentControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 50)
)
if mibBuilder.loadTexts:
    nokiaTPS24EquipmentControllerCard.setStatus("current")
_NokiaTPS12EquipmentControllerCard_ObjectIdentity = ObjectIdentity
nokiaTPS12EquipmentControllerCard = _NokiaTPS12EquipmentControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 51)
)
if mibBuilder.loadTexts:
    nokiaTPS12EquipmentControllerCard.setStatus("current")
_NokiaSAS24EquipmentControllerCard_ObjectIdentity = ObjectIdentity
nokiaSAS24EquipmentControllerCard = _NokiaSAS24EquipmentControllerCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 52)
)
if mibBuilder.loadTexts:
    nokiaSAS24EquipmentControllerCard.setStatus("current")
_NokiaEquipmentController3Card_ObjectIdentity = ObjectIdentity
nokiaEquipmentController3Card = _NokiaEquipmentController3Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 2, 53)
)
if mibBuilder.loadTexts:
    nokiaEquipmentController3Card.setStatus("current")
_TropicOpticalSwitchCardReg_ObjectIdentity = ObjectIdentity
tropicOpticalSwitchCardReg = _TropicOpticalSwitchCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3)
)
if mibBuilder.loadTexts:
    tropicOpticalSwitchCardReg.setStatus("current")
_TropicPhotonicProtectionSwitchCard_ObjectIdentity = ObjectIdentity
tropicPhotonicProtectionSwitchCard = _TropicPhotonicProtectionSwitchCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    tropicPhotonicProtectionSwitchCard.setStatus("current")
_AluWdmOpsaCard_ObjectIdentity = ObjectIdentity
aluWdmOpsaCard = _AluWdmOpsaCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    aluWdmOpsaCard.setStatus("current")
_AluWdmOpsbCard_ObjectIdentity = ObjectIdentity
aluWdmOpsbCard = _AluWdmOpsbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    aluWdmOpsbCard.setStatus("current")
_AluWdmMcs8x16Card_ObjectIdentity = ObjectIdentity
aluWdmMcs8x16Card = _AluWdmMcs8x16Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 4)
)
if mibBuilder.loadTexts:
    aluWdmMcs8x16Card.setStatus("current")
_AluWdmSwitchingCard_ObjectIdentity = ObjectIdentity
aluWdmSwitchingCard = _AluWdmSwitchingCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 5)
)
if mibBuilder.loadTexts:
    aluWdmSwitchingCard.setStatus("current")
_AluWdm12p120Card_ObjectIdentity = ObjectIdentity
aluWdm12p120Card = _AluWdm12p120Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 6)
)
if mibBuilder.loadTexts:
    aluWdm12p120Card.setStatus("current")
_AluWdm20p200Card_ObjectIdentity = ObjectIdentity
aluWdm20p200Card = _AluWdm20p200Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 7)
)
if mibBuilder.loadTexts:
    aluWdm20p200Card.setStatus("current")
_AluWdm1ud200Card_ObjectIdentity = ObjectIdentity
aluWdm1ud200Card = _AluWdm1ud200Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 8)
)
if mibBuilder.loadTexts:
    aluWdm1ud200Card.setStatus("current")
_AluWdmSwitching1T6Card_ObjectIdentity = ObjectIdentity
aluWdmSwitching1T6Card = _AluWdmSwitching1T6Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 9)
)
if mibBuilder.loadTexts:
    aluWdmSwitching1T6Card.setStatus("current")
_AluWdmMcs8x16lCard_ObjectIdentity = ObjectIdentity
aluWdmMcs8x16lCard = _AluWdmMcs8x16lCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 10)
)
if mibBuilder.loadTexts:
    aluWdmMcs8x16lCard.setStatus("current")
_NokiaVwmMsOpsOsmCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsOpsOsmCard = _NokiaVwmMsOpsOsmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 11)
)
if mibBuilder.loadTexts:
    nokiaVwmMsOpsOsmCard.setStatus("current")
_AluWdmSwitching4T8Card_ObjectIdentity = ObjectIdentity
aluWdmSwitching4T8Card = _AluWdmSwitching4T8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 12)
)
if mibBuilder.loadTexts:
    aluWdmSwitching4T8Card.setStatus("current")
_AluWdmOpsflexCard_ObjectIdentity = ObjectIdentity
aluWdmOpsflexCard = _AluWdmOpsflexCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 13)
)
if mibBuilder.loadTexts:
    aluWdmOpsflexCard.setStatus("current")
_AluWdmSwitchingXST4T8Card_ObjectIdentity = ObjectIdentity
aluWdmSwitchingXST4T8Card = _AluWdmSwitchingXST4T8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 14)
)
if mibBuilder.loadTexts:
    aluWdmSwitchingXST4T8Card.setStatus("current")
_NokiaVwmMsOpsOsmDsvCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsOpsOsmDsvCard = _NokiaVwmMsOpsOsmDsvCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 15)
)
if mibBuilder.loadTexts:
    nokiaVwmMsOpsOsmDsvCard.setStatus("current")
_AluWdmOpsb5Card_ObjectIdentity = ObjectIdentity
aluWdmOpsb5Card = _AluWdmOpsb5Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 16)
)
if mibBuilder.loadTexts:
    aluWdmOpsb5Card.setStatus("current")
_AluWdmMcs16x15Card_ObjectIdentity = ObjectIdentity
aluWdmMcs16x15Card = _AluWdmMcs16x15Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 18)
)
if mibBuilder.loadTexts:
    aluWdmMcs16x15Card.setStatus("current")
_AluWdmSwitching24TCard_ObjectIdentity = ObjectIdentity
aluWdmSwitching24TCard = _AluWdmSwitching24TCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 19)
)
if mibBuilder.loadTexts:
    aluWdmSwitching24TCard.setStatus("current")
_AluWdmMcs16x15LCard_ObjectIdentity = ObjectIdentity
aluWdmMcs16x15LCard = _AluWdmMcs16x15LCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 20)
)
if mibBuilder.loadTexts:
    aluWdmMcs16x15LCard.setStatus("current")
_AluWdm12p120sCard_ObjectIdentity = ObjectIdentity
aluWdm12p120sCard = _AluWdm12p120sCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 21)
)
if mibBuilder.loadTexts:
    aluWdm12p120sCard.setStatus("current")
_Nokia16p200Card_ObjectIdentity = ObjectIdentity
nokia16p200Card = _Nokia16p200Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 22)
)
if mibBuilder.loadTexts:
    nokia16p200Card.setStatus("current")
_NokiaSwitchingXST4TCard_ObjectIdentity = ObjectIdentity
nokiaSwitchingXST4TCard = _NokiaSwitchingXST4TCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 23)
)
if mibBuilder.loadTexts:
    nokiaSwitchingXST4TCard.setStatus("current")
_NokiaSwitchingXST12TCard_ObjectIdentity = ObjectIdentity
nokiaSwitchingXST12TCard = _NokiaSwitchingXST12TCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 24)
)
if mibBuilder.loadTexts:
    nokiaSwitchingXST12TCard.setStatus("current")
_NokiaMxn824Card_ObjectIdentity = ObjectIdentity
nokiaMxn824Card = _NokiaMxn824Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 25)
)
if mibBuilder.loadTexts:
    nokiaMxn824Card.setStatus("current")
_NokiaSwitching48TCard_ObjectIdentity = ObjectIdentity
nokiaSwitching48TCard = _NokiaSwitching48TCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 26)
)
if mibBuilder.loadTexts:
    nokiaSwitching48TCard.setStatus("current")
_NokiaOpsumCard_ObjectIdentity = ObjectIdentity
nokiaOpsumCard = _NokiaOpsumCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 27)
)
if mibBuilder.loadTexts:
    nokiaOpsumCard.setStatus("current")
_NokiaMxn1624Card_ObjectIdentity = ObjectIdentity
nokiaMxn1624Card = _NokiaMxn1624Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 28)
)
if mibBuilder.loadTexts:
    nokiaMxn1624Card.setStatus("current")
_NokiaOpsumlCard_ObjectIdentity = ObjectIdentity
nokiaOpsumlCard = _NokiaOpsumlCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 3, 29)
)
if mibBuilder.loadTexts:
    nokiaOpsumlCard.setStatus("current")
_TropicDWDMFilterCardReg_ObjectIdentity = ObjectIdentity
tropicDWDMFilterCardReg = _TropicDWDMFilterCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6)
)
if mibBuilder.loadTexts:
    tropicDWDMFilterCardReg.setStatus("current")
_AluWdmCwr8Card_ObjectIdentity = ObjectIdentity
aluWdmCwr8Card = _AluWdmCwr8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 9)
)
if mibBuilder.loadTexts:
    aluWdmCwr8Card.setStatus("current")
_AluWdmSfd44Card_ObjectIdentity = ObjectIdentity
aluWdmSfd44Card = _AluWdmSfd44Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 10)
)
if mibBuilder.loadTexts:
    aluWdmSfd44Card.setStatus("current")
_AluWdmSVACCard_ObjectIdentity = ObjectIdentity
aluWdmSVACCard = _AluWdmSVACCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 11)
)
if mibBuilder.loadTexts:
    aluWdmSVACCard.setStatus("current")
_AluWdmCwr8c88Card_ObjectIdentity = ObjectIdentity
aluWdmCwr8c88Card = _AluWdmCwr8c88Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 12)
)
if mibBuilder.loadTexts:
    aluWdmCwr8c88Card.setStatus("current")
_AluWdmSfd44bCard_ObjectIdentity = ObjectIdentity
aluWdmSfd44bCard = _AluWdmSfd44bCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 13)
)
if mibBuilder.loadTexts:
    aluWdmSfd44bCard.setStatus("current")
_AluWdmItlbCard_ObjectIdentity = ObjectIdentity
aluWdmItlbCard = _AluWdmItlbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 14)
)
if mibBuilder.loadTexts:
    aluWdmItlbCard.setStatus("current")
_AluWdmSfd40Card_ObjectIdentity = ObjectIdentity
aluWdmSfd40Card = _AluWdmSfd40Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 19)
)
if mibBuilder.loadTexts:
    aluWdmSfd40Card.setStatus("current")
_AluWdmSfd40bCard_ObjectIdentity = ObjectIdentity
aluWdmSfd40bCard = _AluWdmSfd40bCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 20)
)
if mibBuilder.loadTexts:
    aluWdmSfd40bCard.setStatus("current")
_AluWdmWr2c88Card_ObjectIdentity = ObjectIdentity
aluWdmWr2c88Card = _AluWdmWr2c88Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 21)
)
if mibBuilder.loadTexts:
    aluWdmWr2c88Card.setStatus("current")
_AluWdmMVACCard_ObjectIdentity = ObjectIdentity
aluWdmMVACCard = _AluWdmMVACCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 22)
)
if mibBuilder.loadTexts:
    aluWdmMVACCard.setStatus("current")
_AluWdmItluCard_ObjectIdentity = ObjectIdentity
aluWdmItluCard = _AluWdmItluCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 23)
)
if mibBuilder.loadTexts:
    aluWdmItluCard.setStatus("current")
_AluWdmWr8c88aCard_ObjectIdentity = ObjectIdentity
aluWdmWr8c88aCard = _AluWdmWr8c88aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 24)
)
if mibBuilder.loadTexts:
    aluWdmWr8c88aCard.setStatus("current")
_AluWdmMesh4Card_ObjectIdentity = ObjectIdentity
aluWdmMesh4Card = _AluWdmMesh4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 25)
)
if mibBuilder.loadTexts:
    aluWdmMesh4Card.setStatus("current")
_AluWdmMVAC8BCard_ObjectIdentity = ObjectIdentity
aluWdmMVAC8BCard = _AluWdmMVAC8BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 26)
)
if mibBuilder.loadTexts:
    aluWdmMVAC8BCard.setStatus("current")
_AluWdmWr8c88afCard_ObjectIdentity = ObjectIdentity
aluWdmWr8c88afCard = _AluWdmWr8c88afCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 27)
)
if mibBuilder.loadTexts:
    aluWdmWr8c88afCard.setStatus("current")
_AluWdmPsc1x6Card_ObjectIdentity = ObjectIdentity
aluWdmPsc1x6Card = _AluWdmPsc1x6Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 28)
)
if mibBuilder.loadTexts:
    aluWdmPsc1x6Card.setStatus("current")
_AluWdmWr20tfCard_ObjectIdentity = ObjectIdentity
aluWdmWr20tfCard = _AluWdmWr20tfCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 29)
)
if mibBuilder.loadTexts:
    aluWdmWr20tfCard.setStatus("current")
_AluWdmWr20tfmCard_ObjectIdentity = ObjectIdentity
aluWdmWr20tfmCard = _AluWdmWr20tfmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 30)
)
if mibBuilder.loadTexts:
    aluWdmWr20tfmCard.setStatus("current")
_AluWdmWr20tfmlCard_ObjectIdentity = ObjectIdentity
aluWdmWr20tfmlCard = _AluWdmWr20tfmlCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 31)
)
if mibBuilder.loadTexts:
    aluWdmWr20tfmlCard.setStatus("current")
_AluWdmSfd96Card_ObjectIdentity = ObjectIdentity
aluWdmSfd96Card = _AluWdmSfd96Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 32)
)
if mibBuilder.loadTexts:
    aluWdmSfd96Card.setStatus("current")
_NokiaSfd10ALmCard_ObjectIdentity = ObjectIdentity
nokiaSfd10ALmCard = _NokiaSfd10ALmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 33)
)
if mibBuilder.loadTexts:
    nokiaSfd10ALmCard.setStatus("current")
_NokiaSfd10BLmCard_ObjectIdentity = ObjectIdentity
nokiaSfd10BLmCard = _NokiaSfd10BLmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 34)
)
if mibBuilder.loadTexts:
    nokiaSfd10BLmCard.setStatus("current")
_NokiaSfd10CLmCard_ObjectIdentity = ObjectIdentity
nokiaSfd10CLmCard = _NokiaSfd10CLmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 35)
)
if mibBuilder.loadTexts:
    nokiaSfd10CLmCard.setStatus("current")
_NokiaSfd10DLmCard_ObjectIdentity = ObjectIdentity
nokiaSfd10DLmCard = _NokiaSfd10DLmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 36)
)
if mibBuilder.loadTexts:
    nokiaSfd10DLmCard.setStatus("current")
_NokiaSfd48Card_ObjectIdentity = ObjectIdentity
nokiaSfd48Card = _NokiaSfd48Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 37)
)
if mibBuilder.loadTexts:
    nokiaSfd48Card.setStatus("current")
_NokiaSfd64Card_ObjectIdentity = ObjectIdentity
nokiaSfd64Card = _NokiaSfd64Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 6, 38)
)
if mibBuilder.loadTexts:
    nokiaSfd64Card.setStatus("current")
_TropicAmplifierCardReg_ObjectIdentity = ObjectIdentity
tropicAmplifierCardReg = _TropicAmplifierCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7)
)
if mibBuilder.loadTexts:
    tropicAmplifierCardReg.setStatus("current")
_AluWdmAhphgCard_ObjectIdentity = ObjectIdentity
aluWdmAhphgCard = _AluWdmAhphgCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 4)
)
if mibBuilder.loadTexts:
    aluWdmAhphgCard.setStatus("current")
_AluWdmAlphgCard_ObjectIdentity = ObjectIdentity
aluWdmAlphgCard = _AluWdmAlphgCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 5)
)
if mibBuilder.loadTexts:
    aluWdmAlphgCard.setStatus("current")
_AluWdmAhplgCard_ObjectIdentity = ObjectIdentity
aluWdmAhplgCard = _AluWdmAhplgCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 6)
)
if mibBuilder.loadTexts:
    aluWdmAhplgCard.setStatus("current")
_AluWdmAlpfgkCard_ObjectIdentity = ObjectIdentity
aluWdmAlpfgkCard = _AluWdmAlpfgkCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 7)
)
if mibBuilder.loadTexts:
    aluWdmAlpfgkCard.setStatus("current")
_AluWdmOscCard_ObjectIdentity = ObjectIdentity
aluWdmOscCard = _AluWdmOscCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 8)
)
if mibBuilder.loadTexts:
    aluWdmOscCard.setStatus("current")
_AluWdmA2325aCard_ObjectIdentity = ObjectIdentity
aluWdmA2325aCard = _AluWdmA2325aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 10)
)
if mibBuilder.loadTexts:
    aluWdmA2325aCard.setStatus("current")
_AluWdmAlpfgtCard_ObjectIdentity = ObjectIdentity
aluWdmAlpfgtCard = _AluWdmAlpfgtCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 11)
)
if mibBuilder.loadTexts:
    aluWdmAlpfgtCard.setStatus("current")
_AluWdmOsctCard_ObjectIdentity = ObjectIdentity
aluWdmOsctCard = _AluWdmOsctCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 12)
)
if mibBuilder.loadTexts:
    aluWdmOsctCard.setStatus("current")
_AluWdmWtocmCard_ObjectIdentity = ObjectIdentity
aluWdmWtocmCard = _AluWdmWtocmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 13)
)
if mibBuilder.loadTexts:
    aluWdmWtocmCard.setStatus("current")
_AluWdmAm2017bCard_ObjectIdentity = ObjectIdentity
aluWdmAm2017bCard = _AluWdmAm2017bCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 14)
)
if mibBuilder.loadTexts:
    aluWdmAm2017bCard.setStatus("current")
_AluWdmAm2325bCard_ObjectIdentity = ObjectIdentity
aluWdmAm2325bCard = _AluWdmAm2325bCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 15)
)
if mibBuilder.loadTexts:
    aluWdmAm2325bCard.setStatus("current")
_AluWdmRa2pCard_ObjectIdentity = ObjectIdentity
aluWdmRa2pCard = _AluWdmRa2pCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 16)
)
if mibBuilder.loadTexts:
    aluWdmRa2pCard.setStatus("current")
_AluWdmAm2318aCard_ObjectIdentity = ObjectIdentity
aluWdmAm2318aCard = _AluWdmAm2318aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 17)
)
if mibBuilder.loadTexts:
    aluWdmAm2318aCard.setStatus("current")
_AluWdmAm2125aCard_ObjectIdentity = ObjectIdentity
aluWdmAm2125aCard = _AluWdmAm2125aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 18)
)
if mibBuilder.loadTexts:
    aluWdmAm2125aCard.setStatus("current")
_AluWdmAm2125bCard_ObjectIdentity = ObjectIdentity
aluWdmAm2125bCard = _AluWdmAm2125bCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 19)
)
if mibBuilder.loadTexts:
    aluWdmAm2125bCard.setStatus("current")
_AluWdmWtocmaCard_ObjectIdentity = ObjectIdentity
aluWdmWtocmaCard = _AluWdmWtocmaCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 20)
)
if mibBuilder.loadTexts:
    aluWdmWtocmaCard.setStatus("current")
_AluWdmA2p2125Card_ObjectIdentity = ObjectIdentity
aluWdmA2p2125Card = _AluWdmA2p2125Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 21)
)
if mibBuilder.loadTexts:
    aluWdmA2p2125Card.setStatus("current")
_AluWdmAm2625aCard_ObjectIdentity = ObjectIdentity
aluWdmAm2625aCard = _AluWdmAm2625aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 22)
)
if mibBuilder.loadTexts:
    aluWdmAm2625aCard.setStatus("current")
_AluWdmAm2032aCard_ObjectIdentity = ObjectIdentity
aluWdmAm2032aCard = _AluWdmAm2032aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 23)
)
if mibBuilder.loadTexts:
    aluWdmAm2032aCard.setStatus("current")
_AluWdmAa2donwCard_ObjectIdentity = ObjectIdentity
aluWdmAa2donwCard = _AluWdmAa2donwCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 24)
)
if mibBuilder.loadTexts:
    aluWdmAa2donwCard.setStatus("current")
_AluWdmWtocmfCard_ObjectIdentity = ObjectIdentity
aluWdmWtocmfCard = _AluWdmWtocmfCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 25)
)
if mibBuilder.loadTexts:
    aluWdmWtocmfCard.setStatus("current")
_AluWdmAswgCard_ObjectIdentity = ObjectIdentity
aluWdmAswgCard = _AluWdmAswgCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 26)
)
if mibBuilder.loadTexts:
    aluWdmAswgCard.setStatus("current")
_AluWdmA4pswgCard_ObjectIdentity = ObjectIdentity
aluWdmA4pswgCard = _AluWdmA4pswgCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 27)
)
if mibBuilder.loadTexts:
    aluWdmA4pswgCard.setStatus("current")
_AluWdmOtdrCard_ObjectIdentity = ObjectIdentity
aluWdmOtdrCard = _AluWdmOtdrCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 28)
)
if mibBuilder.loadTexts:
    aluWdmOtdrCard.setStatus("current")
_AluWdmAar8aCard_ObjectIdentity = ObjectIdentity
aluWdmAar8aCard = _AluWdmAar8aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 29)
)
if mibBuilder.loadTexts:
    aluWdmAar8aCard.setStatus("current")
_AluWdmMonOtdrCard_ObjectIdentity = ObjectIdentity
aluWdmMonOtdrCard = _AluWdmMonOtdrCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 30)
)
if mibBuilder.loadTexts:
    aluWdmMonOtdrCard.setStatus("current")
_AluWdmAwbegrCard_ObjectIdentity = ObjectIdentity
aluWdmAwbegrCard = _AluWdmAwbegrCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 31)
)
if mibBuilder.loadTexts:
    aluWdmAwbegrCard.setStatus("current")
_AluWdmAwbingCard_ObjectIdentity = ObjectIdentity
aluWdmAwbingCard = _AluWdmAwbingCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 32)
)
if mibBuilder.loadTexts:
    aluWdmAwbingCard.setStatus("current")
_AluWdmAwbilaCard_ObjectIdentity = ObjectIdentity
aluWdmAwbilaCard = _AluWdmAwbilaCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 33)
)
if mibBuilder.loadTexts:
    aluWdmAwbilaCard.setStatus("current")
_AluWdmRa5pCard_ObjectIdentity = ObjectIdentity
aluWdmRa5pCard = _AluWdmRa5pCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 34)
)
if mibBuilder.loadTexts:
    aluWdmRa5pCard.setStatus("current")
_AluWdmAa2donwBCard_ObjectIdentity = ObjectIdentity
aluWdmAa2donwBCard = _AluWdmAa2donwBCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 35)
)
if mibBuilder.loadTexts:
    aluWdmAa2donwBCard.setStatus("current")
_AluWdmOsctaprCard_ObjectIdentity = ObjectIdentity
aluWdmOsctaprCard = _AluWdmOsctaprCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 36)
)
if mibBuilder.loadTexts:
    aluWdmOsctaprCard.setStatus("current")
_AluWdmAar2x8aCard_ObjectIdentity = ObjectIdentity
aluWdmAar2x8aCard = _AluWdmAar2x8aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 37)
)
if mibBuilder.loadTexts:
    aluWdmAar2x8aCard.setStatus("current")
_AluWdmAar2x8alCard_ObjectIdentity = ObjectIdentity
aluWdmAar2x8alCard = _AluWdmAar2x8alCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 38)
)
if mibBuilder.loadTexts:
    aluWdmAar2x8alCard.setStatus("current")
_AluWdmWtocmflCard_ObjectIdentity = ObjectIdentity
aluWdmWtocmflCard = _AluWdmWtocmflCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 39)
)
if mibBuilder.loadTexts:
    aluWdmWtocmflCard.setStatus("current")
_AluWdmOtdrwbCard_ObjectIdentity = ObjectIdentity
aluWdmOtdrwbCard = _AluWdmOtdrwbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 40)
)
if mibBuilder.loadTexts:
    aluWdmOtdrwbCard.setStatus("current")
_AluWdmRa2p96Card_ObjectIdentity = ObjectIdentity
aluWdmRa2p96Card = _AluWdmRa2p96Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 41)
)
if mibBuilder.loadTexts:
    aluWdmRa2p96Card.setStatus("current")
_AluWdmOtdrmCard_ObjectIdentity = ObjectIdentity
aluWdmOtdrmCard = _AluWdmOtdrmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 42)
)
if mibBuilder.loadTexts:
    aluWdmOtdrmCard.setStatus("current")
_AluWdmOAUnidirCard_ObjectIdentity = ObjectIdentity
aluWdmOAUnidirCard = _AluWdmOAUnidirCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 43)
)
if mibBuilder.loadTexts:
    aluWdmOAUnidirCard.setStatus("current")
_AluWdmAswglCard_ObjectIdentity = ObjectIdentity
aluWdmAswglCard = _AluWdmAswglCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 44)
)
if mibBuilder.loadTexts:
    aluWdmAswglCard.setStatus("current")
_AluWdmRa4pCard_ObjectIdentity = ObjectIdentity
aluWdmRa4pCard = _AluWdmRa4pCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 45)
)
if mibBuilder.loadTexts:
    aluWdmRa4pCard.setStatus("current")
_AluWdmEilaCard_ObjectIdentity = ObjectIdentity
aluWdmEilaCard = _AluWdmEilaCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 46)
)
if mibBuilder.loadTexts:
    aluWdmEilaCard.setStatus("current")
_AluWdmRa5pbCard_ObjectIdentity = ObjectIdentity
aluWdmRa5pbCard = _AluWdmRa5pbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 47)
)
if mibBuilder.loadTexts:
    aluWdmRa5pbCard.setStatus("current")
_AluWdmAsgCard_ObjectIdentity = ObjectIdentity
aluWdmAsgCard = _AluWdmAsgCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 48)
)
if mibBuilder.loadTexts:
    aluWdmAsgCard.setStatus("current")
_NokiaAsc4Card_ObjectIdentity = ObjectIdentity
nokiaAsc4Card = _NokiaAsc4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 49)
)
if mibBuilder.loadTexts:
    nokiaAsc4Card.setStatus("current")
_NokiaAsc2Card_ObjectIdentity = ObjectIdentity
nokiaAsc2Card = _NokiaAsc2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 7, 50)
)
if mibBuilder.loadTexts:
    nokiaAsc2Card.setStatus("current")
_TropicDispersionCompCardReg_ObjectIdentity = ObjectIdentity
tropicDispersionCompCardReg = _TropicDispersionCompCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 8)
)
if mibBuilder.loadTexts:
    tropicDispersionCompCardReg.setStatus("current")
_AluWdmDcmCard_ObjectIdentity = ObjectIdentity
aluWdmDcmCard = _AluWdmDcmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 8, 3)
)
if mibBuilder.loadTexts:
    aluWdmDcmCard.setStatus("current")
_NokiaDmCt05LmCard_ObjectIdentity = ObjectIdentity
nokiaDmCt05LmCard = _NokiaDmCt05LmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 8, 4)
)
if mibBuilder.loadTexts:
    nokiaDmCt05LmCard.setStatus("current")
_NokiaDmCt10LmCard_ObjectIdentity = ObjectIdentity
nokiaDmCt10LmCard = _NokiaDmCt10LmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 8, 5)
)
if mibBuilder.loadTexts:
    nokiaDmCt10LmCard.setStatus("current")
_NokiaDmIt05LmCard_ObjectIdentity = ObjectIdentity
nokiaDmIt05LmCard = _NokiaDmIt05LmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 8, 6)
)
if mibBuilder.loadTexts:
    nokiaDmIt05LmCard.setStatus("current")
_NokiaDmIt10LmCard_ObjectIdentity = ObjectIdentity
nokiaDmIt10LmCard = _NokiaDmIt10LmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 8, 7)
)
if mibBuilder.loadTexts:
    nokiaDmIt10LmCard.setStatus("current")
_AluWdmOpticalTransponderCardReg_ObjectIdentity = ObjectIdentity
aluWdmOpticalTransponderCardReg = _AluWdmOpticalTransponderCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11)
)
if mibBuilder.loadTexts:
    aluWdmOpticalTransponderCardReg.setStatus("current")
_AluWdm11star1Card_ObjectIdentity = ObjectIdentity
aluWdm11star1Card = _AluWdm11star1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 1)
)
if mibBuilder.loadTexts:
    aluWdm11star1Card.setStatus("current")
_AluWdm11stge12Card_ObjectIdentity = ObjectIdentity
aluWdm11stge12Card = _AluWdm11stge12Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 2)
)
if mibBuilder.loadTexts:
    aluWdm11stge12Card.setStatus("current")
_AluWdm11dpge12Card_ObjectIdentity = ObjectIdentity
aluWdm11dpge12Card = _AluWdm11dpge12Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 3)
)
if mibBuilder.loadTexts:
    aluWdm11dpge12Card.setStatus("current")
_AluWdm11stmm10Card_ObjectIdentity = ObjectIdentity
aluWdm11stmm10Card = _AluWdm11stmm10Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 4)
)
if mibBuilder.loadTexts:
    aluWdm11stmm10Card.setStatus("current")
_AluWdm4dpa4Card_ObjectIdentity = ObjectIdentity
aluWdm4dpa4Card = _AluWdm4dpa4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 5)
)
if mibBuilder.loadTexts:
    aluWdm4dpa4Card.setStatus("current")
_AluWdm43stx4Card_ObjectIdentity = ObjectIdentity
aluWdm43stx4Card = _AluWdm43stx4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 6)
)
if mibBuilder.loadTexts:
    aluWdm43stx4Card.setStatus("current")
_AluWdm4dpa2Card_ObjectIdentity = ObjectIdentity
aluWdm4dpa2Card = _AluWdm4dpa2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 7)
)
if mibBuilder.loadTexts:
    aluWdm4dpa2Card.setStatus("current")
_AluWdm43sta1pCard_ObjectIdentity = ObjectIdentity
aluWdm43sta1pCard = _AluWdm43sta1pCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 8)
)
if mibBuilder.loadTexts:
    aluWdm43sta1pCard.setStatus("current")
_AluWdm43stx4pCard_ObjectIdentity = ObjectIdentity
aluWdm43stx4pCard = _AluWdm43stx4pCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 9)
)
if mibBuilder.loadTexts:
    aluWdm43stx4pCard.setStatus("current")
_AluWdm11qpa4Card_ObjectIdentity = ObjectIdentity
aluWdm11qpa4Card = _AluWdm11qpa4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 12)
)
if mibBuilder.loadTexts:
    aluWdm11qpa4Card.setStatus("current")
_AluWdm112scx10Card_ObjectIdentity = ObjectIdentity
aluWdm112scx10Card = _AluWdm112scx10Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 13)
)
if mibBuilder.loadTexts:
    aluWdm112scx10Card.setStatus("current")
_AluWdm112sca1Card_ObjectIdentity = ObjectIdentity
aluWdm112sca1Card = _AluWdm112sca1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 14)
)
if mibBuilder.loadTexts:
    aluWdm112sca1Card.setStatus("current")
_AluWdm1dpp21Card_ObjectIdentity = ObjectIdentity
aluWdm1dpp21Card = _AluWdm1dpp21Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 15)
)
if mibBuilder.loadTexts:
    aluWdm1dpp21Card.setStatus("current")
_AluWdm43scx4Card_ObjectIdentity = ObjectIdentity
aluWdm43scx4Card = _AluWdm43scx4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 16)
)
if mibBuilder.loadTexts:
    aluWdm43scx4Card.setStatus("current")
_AluWdm11dpe12eCard_ObjectIdentity = ObjectIdentity
aluWdm11dpe12eCard = _AluWdm11dpe12eCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 17)
)
if mibBuilder.loadTexts:
    aluWdm11dpe12eCard.setStatus("current")
_AluWdm112sx10lCard_ObjectIdentity = ObjectIdentity
aluWdm112sx10lCard = _AluWdm112sx10lCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 18)
)
if mibBuilder.loadTexts:
    aluWdm112sx10lCard.setStatus("current")
_AluWdm112sa1lCard_ObjectIdentity = ObjectIdentity
aluWdm112sa1lCard = _AluWdm112sa1lCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 19)
)
if mibBuilder.loadTexts:
    aluWdm112sa1lCard.setStatus("current")
_AluWdm11dpm12Card_ObjectIdentity = ObjectIdentity
aluWdm11dpm12Card = _AluWdm11dpm12Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 20)
)
if mibBuilder.loadTexts:
    aluWdm11dpm12Card.setStatus("current")
_AluWdm43sca1Card_ObjectIdentity = ObjectIdentity
aluWdm43sca1Card = _AluWdm43sca1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 21)
)
if mibBuilder.loadTexts:
    aluWdm43sca1Card.setStatus("current")
_AluWdm43scx4lCard_ObjectIdentity = ObjectIdentity
aluWdm43scx4lCard = _AluWdm43scx4lCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 22)
)
if mibBuilder.loadTexts:
    aluWdm43scx4lCard.setStatus("current")
_AluWdm112snx10Card_ObjectIdentity = ObjectIdentity
aluWdm112snx10Card = _AluWdm112snx10Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 23)
)
if mibBuilder.loadTexts:
    aluWdm112snx10Card.setStatus("current")
_AluWdm112sna1Card_ObjectIdentity = ObjectIdentity
aluWdm112sna1Card = _AluWdm112sna1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 24)
)
if mibBuilder.loadTexts:
    aluWdm112sna1Card.setStatus("current")
_AluWdm1dpp24mCard_ObjectIdentity = ObjectIdentity
aluWdm1dpp24mCard = _AluWdm1dpp24mCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 26)
)
if mibBuilder.loadTexts:
    aluWdm1dpp24mCard.setStatus("current")
_AluWdmul43scupCard_ObjectIdentity = ObjectIdentity
aluWdmul43scupCard = _AluWdmul43scupCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 27)
)
if mibBuilder.loadTexts:
    aluWdmul43scupCard.setStatus("current")
_AluWdmul11qcupCard_ObjectIdentity = ObjectIdentity
aluWdmul11qcupCard = _AluWdmul11qcupCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 28)
)
if mibBuilder.loadTexts:
    aluWdmul11qcupCard.setStatus("current")
_AluWdm11qpen4Card_ObjectIdentity = ObjectIdentity
aluWdm11qpen4Card = _AluWdm11qpen4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 29)
)
if mibBuilder.loadTexts:
    aluWdm11qpen4Card.setStatus("current")
_AluWdm43scx4eCard_ObjectIdentity = ObjectIdentity
aluWdm43scx4eCard = _AluWdm43scx4eCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 30)
)
if mibBuilder.loadTexts:
    aluWdm43scx4eCard.setStatus("current")
_AluWdm43scge1Card_ObjectIdentity = ObjectIdentity
aluWdm43scge1Card = _AluWdm43scge1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 31)
)
if mibBuilder.loadTexts:
    aluWdm43scge1Card.setStatus("current")
_AluWdm11qpe24Card_ObjectIdentity = ObjectIdentity
aluWdm11qpe24Card = _AluWdm11qpe24Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 32)
)
if mibBuilder.loadTexts:
    aluWdm11qpe24Card.setStatus("current")
_AluWdm11star1aCard_ObjectIdentity = ObjectIdentity
aluWdm11star1aCard = _AluWdm11star1aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 33)
)
if mibBuilder.loadTexts:
    aluWdm11star1aCard.setStatus("current")
_AluWdmcl10an10gCard_ObjectIdentity = ObjectIdentity
aluWdmcl10an10gCard = _AluWdmcl10an10gCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 34)
)
if mibBuilder.loadTexts:
    aluWdmcl10an10gCard.setStatus("current")
_AluWdmcl24anmCard_ObjectIdentity = ObjectIdentity
aluWdmcl24anmCard = _AluWdmcl24anmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 35)
)
if mibBuilder.loadTexts:
    aluWdmcl24anmCard.setStatus("current")
_AluWdm11dpe12aCard_ObjectIdentity = ObjectIdentity
aluWdm11dpe12aCard = _AluWdm11dpe12aCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 36)
)
if mibBuilder.loadTexts:
    aluWdm11dpe12aCard.setStatus("current")
_AluWdmul130scupCard_ObjectIdentity = ObjectIdentity
aluWdmul130scupCard = _AluWdmul130scupCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 37)
)
if mibBuilder.loadTexts:
    aluWdmul130scupCard.setStatus("current")
_AluWdm130scx10Card_ObjectIdentity = ObjectIdentity
aluWdm130scx10Card = _AluWdm130scx10Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 38)
)
if mibBuilder.loadTexts:
    aluWdm130scx10Card.setStatus("current")
_AluWdm4qpa8Card_ObjectIdentity = ObjectIdentity
aluWdm4qpa8Card = _AluWdm4qpa8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 39)
)
if mibBuilder.loadTexts:
    aluWdm4qpa8Card.setStatus("current")
_AluWdmOt112pdm11Card_ObjectIdentity = ObjectIdentity
aluWdmOt112pdm11Card = _AluWdmOt112pdm11Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 40)
)
if mibBuilder.loadTexts:
    aluWdmOt112pdm11Card.setStatus("current")
_AluWdmPtpctlCard_ObjectIdentity = ObjectIdentity
aluWdmPtpctlCard = _AluWdmPtpctlCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 41)
)
if mibBuilder.loadTexts:
    aluWdmPtpctlCard.setStatus("current")
_AluWdmPtpioCard_ObjectIdentity = ObjectIdentity
aluWdmPtpioCard = _AluWdmPtpioCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 42)
)
if mibBuilder.loadTexts:
    aluWdmPtpioCard.setStatus("current")
_AluWdmIo24et1gbCard_ObjectIdentity = ObjectIdentity
aluWdmIo24et1gbCard = _AluWdmIo24et1gbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 43)
)
if mibBuilder.loadTexts:
    aluWdmIo24et1gbCard.setStatus("current")
_AluWdmIo4an10gCard_ObjectIdentity = ObjectIdentity
aluWdmIo4an10gCard = _AluWdmIo4an10gCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 44)
)
if mibBuilder.loadTexts:
    aluWdmIo4an10gCard.setStatus("current")
_AluWdmIo8et1gbCard_ObjectIdentity = ObjectIdentity
aluWdmIo8et1gbCard = _AluWdmIo8et1gbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 45)
)
if mibBuilder.loadTexts:
    aluWdmIo8et1gbCard.setStatus("current")
_AluWdmIo10et10gCard_ObjectIdentity = ObjectIdentity
aluWdmIo10et10gCard = _AluWdmIo10et10gCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 46)
)
if mibBuilder.loadTexts:
    aluWdmIo10et10gCard.setStatus("current")
_AluWdmUl11qcupcCard_ObjectIdentity = ObjectIdentity
aluWdmUl11qcupcCard = _AluWdmUl11qcupcCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 47)
)
if mibBuilder.loadTexts:
    aluWdmUl11qcupcCard.setStatus("current")
_AluWdmOt520scx4Card_ObjectIdentity = ObjectIdentity
aluWdmOt520scx4Card = _AluWdmOt520scx4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 48)
)
if mibBuilder.loadTexts:
    aluWdmOt520scx4Card.setStatus("current")
_AluWdm11ope8Card_ObjectIdentity = ObjectIdentity
aluWdm11ope8Card = _AluWdm11ope8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 49)
)
if mibBuilder.loadTexts:
    aluWdm11ope8Card.setStatus("current")
_AluWdm11qce12xCard_ObjectIdentity = ObjectIdentity
aluWdm11qce12xCard = _AluWdm11qce12xCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 50)
)
if mibBuilder.loadTexts:
    aluWdm11qce12xCard.setStatus("current")
_AluWdmOt260scx2Card_ObjectIdentity = ObjectIdentity
aluWdmOt260scx2Card = _AluWdmOt260scx2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 51)
)
if mibBuilder.loadTexts:
    aluWdmOt260scx2Card.setStatus("current")
_AluWdmOt130snx10Card_ObjectIdentity = ObjectIdentity
aluWdmOt130snx10Card = _AluWdmOt130snx10Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 52)
)
if mibBuilder.loadTexts:
    aluWdmOt130snx10Card.setStatus("current")
_AluWdmIo24anmbCard_ObjectIdentity = ObjectIdentity
aluWdmIo24anmbCard = _AluWdmIo24anmbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 53)
)
if mibBuilder.loadTexts:
    aluWdmIo24anmbCard.setStatus("current")
_AluWdmOt11dpm8Card_ObjectIdentity = ObjectIdentity
aluWdmOt11dpm8Card = _AluWdmOt11dpm8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 54)
)
if mibBuilder.loadTexts:
    aluWdmOt11dpm8Card.setStatus("current")
_AluWdmOt11dpm4mCard_ObjectIdentity = ObjectIdentity
aluWdmOt11dpm4mCard = _AluWdmOt11dpm4mCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 55)
)
if mibBuilder.loadTexts:
    aluWdmOt11dpm4mCard.setStatus("current")
_AluWdmOt11dpm4eCard_ObjectIdentity = ObjectIdentity
aluWdmOt11dpm4eCard = _AluWdmOt11dpm4eCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 56)
)
if mibBuilder.loadTexts:
    aluWdmOt11dpm4eCard.setStatus("current")
_AluWdmUl130scupbCard_ObjectIdentity = ObjectIdentity
aluWdmUl130scupbCard = _AluWdmUl130scupbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 57)
)
if mibBuilder.loadTexts:
    aluWdmUl130scupbCard.setStatus("current")
_AluWdmOt112sdx11Card_ObjectIdentity = ObjectIdentity
aluWdmOt112sdx11Card = _AluWdmOt112sdx11Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 58)
)
if mibBuilder.loadTexts:
    aluWdmOt112sdx11Card.setStatus("current")
_AluWdmOt130sca1Card_ObjectIdentity = ObjectIdentity
aluWdmOt130sca1Card = _AluWdmOt130sca1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 59)
)
if mibBuilder.loadTexts:
    aluWdmOt130sca1Card.setStatus("current")
_AluWdmIo10an10gbCard_ObjectIdentity = ObjectIdentity
aluWdmIo10an10gbCard = _AluWdmIo10an10gbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 60)
)
if mibBuilder.loadTexts:
    aluWdmIo10an10gbCard.setStatus("current")
_AluWdmIo10et10gbCard_ObjectIdentity = ObjectIdentity
aluWdmIo10et10gbCard = _AluWdmIo10et10gbCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 61)
)
if mibBuilder.loadTexts:
    aluWdmIo10et10gbCard.setStatus("current")
_AluWdmIo4an100gCard_ObjectIdentity = ObjectIdentity
aluWdmIo4an100gCard = _AluWdmIo4an100gCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 62)
)
if mibBuilder.loadTexts:
    aluWdmIo4an100gCard.setStatus("current")
_AluWdmIo30an10gCard_ObjectIdentity = ObjectIdentity
aluWdmIo30an10gCard = _AluWdmIo30an10gCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 63)
)
if mibBuilder.loadTexts:
    aluWdmIo30an10gCard.setStatus("current")
_AluWdmIo30an300Card_ObjectIdentity = ObjectIdentity
aluWdmIo30an300Card = _AluWdmIo30an300Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 64)
)
if mibBuilder.loadTexts:
    aluWdmIo30an300Card.setStatus("current")
_AluWdmIo4an400Card_ObjectIdentity = ObjectIdentity
aluWdmIo4an400Card = _AluWdmIo4an400Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 65)
)
if mibBuilder.loadTexts:
    aluWdmIo4an400Card.setStatus("current")
_AluWdmOt130snq10Card_ObjectIdentity = ObjectIdentity
aluWdmOt130snq10Card = _AluWdmOt130snq10Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 66)
)
if mibBuilder.loadTexts:
    aluWdmOt130snq10Card.setStatus("current")
_AluWdmUl2uc400Card_ObjectIdentity = ObjectIdentity
aluWdmUl2uc400Card = _AluWdmUl2uc400Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 67)
)
if mibBuilder.loadTexts:
    aluWdmUl2uc400Card.setStatus("current")
_AluWdmUl4uc400Card_ObjectIdentity = ObjectIdentity
aluWdmUl4uc400Card = _AluWdmUl4uc400Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 68)
)
if mibBuilder.loadTexts:
    aluWdmUl4uc400Card.setStatus("current")
_AluWdmUl20uc200Card_ObjectIdentity = ObjectIdentity
aluWdmUl20uc200Card = _AluWdmUl20uc200Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 69)
)
if mibBuilder.loadTexts:
    aluWdmUl20uc200Card.setStatus("current")
_AluWdmD5x500Card_ObjectIdentity = ObjectIdentity
aluWdmD5x500Card = _AluWdmD5x500Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 70)
)
if mibBuilder.loadTexts:
    aluWdmD5x500Card.setStatus("current")
_AluWdmOtS11M100Card_ObjectIdentity = ObjectIdentity
aluWdmOtS11M100Card = _AluWdmOtS11M100Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 71)
)
if mibBuilder.loadTexts:
    aluWdmOtS11M100Card.setStatus("current")
_AluWdm12ce120Card_ObjectIdentity = ObjectIdentity
aluWdm12ce120Card = _AluWdm12ce120Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 72)
)
if mibBuilder.loadTexts:
    aluWdm12ce120Card.setStatus("current")
_AluWdm1ce100Card_ObjectIdentity = ObjectIdentity
aluWdm1ce100Card = _AluWdm1ce100Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 73)
)
if mibBuilder.loadTexts:
    aluWdm1ce100Card.setStatus("current")
_AluWdmLcI1000Card_ObjectIdentity = ObjectIdentity
aluWdmLcI1000Card = _AluWdmLcI1000Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 74)
)
if mibBuilder.loadTexts:
    aluWdmLcI1000Card.setStatus("current")
_AluWdmS13x100Card_ObjectIdentity = ObjectIdentity
aluWdmS13x100Card = _AluWdmS13x100Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 75)
)
if mibBuilder.loadTexts:
    aluWdmS13x100Card.setStatus("current")
_AluWdm12ce121Card_ObjectIdentity = ObjectIdentity
aluWdm12ce121Card = _AluWdm12ce121Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 76)
)
if mibBuilder.loadTexts:
    aluWdm12ce121Card.setStatus("current")
_AluWdmPtpioctlCard_ObjectIdentity = ObjectIdentity
aluWdmPtpioctlCard = _AluWdmPtpioctlCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 77)
)
if mibBuilder.loadTexts:
    aluWdmPtpioctlCard.setStatus("current")
_AluWdm11qpa4BCard_ObjectIdentity = ObjectIdentity
aluWdm11qpa4BCard = _AluWdm11qpa4BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 78)
)
if mibBuilder.loadTexts:
    aluWdm11qpa4BCard.setStatus("current")
_AluWdm1ux100Card_ObjectIdentity = ObjectIdentity
aluWdm1ux100Card = _AluWdm1ux100Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 79)
)
if mibBuilder.loadTexts:
    aluWdm1ux100Card.setStatus("current")
_AluWdm20ax200Card_ObjectIdentity = ObjectIdentity
aluWdm20ax200Card = _AluWdm20ax200Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 80)
)
if mibBuilder.loadTexts:
    aluWdm20ax200Card.setStatus("current")
_AluWdm20mx80Card_ObjectIdentity = ObjectIdentity
aluWdm20mx80Card = _AluWdm20mx80Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 81)
)
if mibBuilder.loadTexts:
    aluWdm20mx80Card.setStatus("current")
_AluWdmS13x100eCard_ObjectIdentity = ObjectIdentity
aluWdmS13x100eCard = _AluWdmS13x100eCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 82)
)
if mibBuilder.loadTexts:
    aluWdmS13x100eCard.setStatus("current")
_AluWdmLcI2000Card_ObjectIdentity = ObjectIdentity
aluWdmLcI2000Card = _AluWdmLcI2000Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 83)
)
if mibBuilder.loadTexts:
    aluWdmLcI2000Card.setStatus("current")
_AluWdm30se300Card_ObjectIdentity = ObjectIdentity
aluWdm30se300Card = _AluWdm30se300Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 84)
)
if mibBuilder.loadTexts:
    aluWdm30se300Card.setStatus("current")
_AluWdm6se300Card_ObjectIdentity = ObjectIdentity
aluWdm6se300Card = _AluWdm6se300Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 85)
)
if mibBuilder.loadTexts:
    aluWdm6se300Card.setStatus("current")
_AluWdmD5x500lCard_ObjectIdentity = ObjectIdentity
aluWdmD5x500lCard = _AluWdmD5x500lCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 86)
)
if mibBuilder.loadTexts:
    aluWdmD5x500lCard.setStatus("current")
_AluWdmLcI2000lCard_ObjectIdentity = ObjectIdentity
aluWdmLcI2000lCard = _AluWdmLcI2000lCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 87)
)
if mibBuilder.loadTexts:
    aluWdmLcI2000lCard.setStatus("current")
_AluWdm20an80Card_ObjectIdentity = ObjectIdentity
aluWdm20an80Card = _AluWdm20an80Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 88)
)
if mibBuilder.loadTexts:
    aluWdm20an80Card.setStatus("current")
_AluWdm10an400Card_ObjectIdentity = ObjectIdentity
aluWdm10an400Card = _AluWdm10an400Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 89)
)
if mibBuilder.loadTexts:
    aluWdm10an400Card.setStatus("current")
_AluWdm8p20Card_ObjectIdentity = ObjectIdentity
aluWdm8p20Card = _AluWdm8p20Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 90)
)
if mibBuilder.loadTexts:
    aluWdm8p20Card.setStatus("current")
_AluWdmD5x500qCard_ObjectIdentity = ObjectIdentity
aluWdmD5x500qCard = _AluWdmD5x500qCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 91)
)
if mibBuilder.loadTexts:
    aluWdmD5x500qCard.setStatus("current")
_AluWdm18p40Card_ObjectIdentity = ObjectIdentity
aluWdm18p40Card = _AluWdm18p40Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 92)
)
if mibBuilder.loadTexts:
    aluWdm18p40Card.setStatus("current")
_AluWdmDa2c4Card_ObjectIdentity = ObjectIdentity
aluWdmDa2c4Card = _AluWdmDa2c4Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 93)
)
if mibBuilder.loadTexts:
    aluWdmDa2c4Card.setStatus("current")
_AluWdm130sla1Card_ObjectIdentity = ObjectIdentity
aluWdm130sla1Card = _AluWdm130sla1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 94)
)
if mibBuilder.loadTexts:
    aluWdm130sla1Card.setStatus("current")
_AluWdm130slx10Card_ObjectIdentity = ObjectIdentity
aluWdm130slx10Card = _AluWdm130slx10Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 95)
)
if mibBuilder.loadTexts:
    aluWdm130slx10Card.setStatus("current")
_AluWdmBmuPCard_ObjectIdentity = ObjectIdentity
aluWdmBmuPCard = _AluWdmBmuPCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 96)
)
if mibBuilder.loadTexts:
    aluWdmBmuPCard.setStatus("current")
_AluWdmS2ad200Card_ObjectIdentity = ObjectIdentity
aluWdmS2ad200Card = _AluWdmS2ad200Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 97)
)
if mibBuilder.loadTexts:
    aluWdmS2ad200Card.setStatus("current")
_AluWdm2ux200Card_ObjectIdentity = ObjectIdentity
aluWdm2ux200Card = _AluWdm2ux200Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 98)
)
if mibBuilder.loadTexts:
    aluWdm2ux200Card.setStatus("current")
_AluWdm4mx200Card_ObjectIdentity = ObjectIdentity
aluWdm4mx200Card = _AluWdm4mx200Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 99)
)
if mibBuilder.loadTexts:
    aluWdm4mx200Card.setStatus("current")
_AluWdm10an1tCard_ObjectIdentity = ObjectIdentity
aluWdm10an1tCard = _AluWdm10an1tCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 103)
)
if mibBuilder.loadTexts:
    aluWdm10an1tCard.setStatus("current")
_AluWdm8uc1tCard_ObjectIdentity = ObjectIdentity
aluWdm8uc1tCard = _AluWdm8uc1tCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 104)
)
if mibBuilder.loadTexts:
    aluWdm8uc1tCard.setStatus("current")
_AluWdmDfc12Card_ObjectIdentity = ObjectIdentity
aluWdmDfc12Card = _AluWdmDfc12Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 105)
)
if mibBuilder.loadTexts:
    aluWdmDfc12Card.setStatus("current")
_NokiaT24PS1Card_ObjectIdentity = ObjectIdentity
nokiaT24PS1Card = _NokiaT24PS1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 106)
)
if mibBuilder.loadTexts:
    nokiaT24PS1Card.setStatus("current")
_NokiaT12PSCard_ObjectIdentity = ObjectIdentity
nokiaT12PSCard = _NokiaT12PSCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 107)
)
if mibBuilder.loadTexts:
    nokiaT12PSCard.setStatus("current")
_AluWdmS4x400Card_ObjectIdentity = ObjectIdentity
aluWdmS4x400Card = _AluWdmS4x400Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 108)
)
if mibBuilder.loadTexts:
    aluWdmS4x400Card.setStatus("current")
_NokiaT24PS2Card_ObjectIdentity = ObjectIdentity
nokiaT24PS2Card = _NokiaT24PS2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 109)
)
if mibBuilder.loadTexts:
    nokiaT24PS2Card.setStatus("current")
_AluWdmGenericOtCard_ObjectIdentity = ObjectIdentity
aluWdmGenericOtCard = _AluWdmGenericOtCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 110)
)
if mibBuilder.loadTexts:
    aluWdmGenericOtCard.setStatus("current")
_AluWdm1ety100Card_ObjectIdentity = ObjectIdentity
aluWdm1ety100Card = _AluWdm1ety100Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 111)
)
if mibBuilder.loadTexts:
    aluWdm1ety100Card.setStatus("current")
_AluWdm18P400Card_ObjectIdentity = ObjectIdentity
aluWdm18P400Card = _AluWdm18P400Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 113)
)
if mibBuilder.loadTexts:
    aluWdm18P400Card.setStatus("current")
_AluWdm4uc1tCard_ObjectIdentity = ObjectIdentity
aluWdm4uc1tCard = _AluWdm4uc1tCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 114)
)
if mibBuilder.loadTexts:
    aluWdm4uc1tCard.setStatus("current")
_Nokia5mx500Card_ObjectIdentity = ObjectIdentity
nokia5mx500Card = _Nokia5mx500Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 115)
)
if mibBuilder.loadTexts:
    nokia5mx500Card.setStatus("current")
_Nokia2ux500Card_ObjectIdentity = ObjectIdentity
nokia2ux500Card = _Nokia2ux500Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 116)
)
if mibBuilder.loadTexts:
    nokia2ux500Card.setStatus("current")
_NokiaS24PS1Card_ObjectIdentity = ObjectIdentity
nokiaS24PS1Card = _NokiaS24PS1Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 117)
)
if mibBuilder.loadTexts:
    nokiaS24PS1Card.setStatus("current")
_NokiaS24PS2Card_ObjectIdentity = ObjectIdentity
nokiaS24PS2Card = _NokiaS24PS2Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 118)
)
if mibBuilder.loadTexts:
    nokiaS24PS2Card.setStatus("current")
_Nokia18ce300Card_ObjectIdentity = ObjectIdentity
nokia18ce300Card = _Nokia18ce300Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 11, 119)
)
if mibBuilder.loadTexts:
    nokia18ce300Card.setStatus("current")
_AluWdmStaticFilterCardReg_ObjectIdentity = ObjectIdentity
aluWdmStaticFilterCardReg = _AluWdmStaticFilterCardReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12)
)
if mibBuilder.loadTexts:
    aluWdmStaticFilterCardReg.setStatus("current")
_AluWdmSFD5ACard_ObjectIdentity = ObjectIdentity
aluWdmSFD5ACard = _AluWdmSFD5ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 1)
)
if mibBuilder.loadTexts:
    aluWdmSFD5ACard.setStatus("current")
_AluWdmSFD5BCard_ObjectIdentity = ObjectIdentity
aluWdmSFD5BCard = _AluWdmSFD5BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 2)
)
if mibBuilder.loadTexts:
    aluWdmSFD5BCard.setStatus("current")
_AluWdmSFD5CCard_ObjectIdentity = ObjectIdentity
aluWdmSFD5CCard = _AluWdmSFD5CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 3)
)
if mibBuilder.loadTexts:
    aluWdmSFD5CCard.setStatus("current")
_AluWdmSFD5DCard_ObjectIdentity = ObjectIdentity
aluWdmSFD5DCard = _AluWdmSFD5DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 4)
)
if mibBuilder.loadTexts:
    aluWdmSFD5DCard.setStatus("current")
_AluWdmSFD5ECard_ObjectIdentity = ObjectIdentity
aluWdmSFD5ECard = _AluWdmSFD5ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 5)
)
if mibBuilder.loadTexts:
    aluWdmSFD5ECard.setStatus("current")
_AluWdmSFD5FCard_ObjectIdentity = ObjectIdentity
aluWdmSFD5FCard = _AluWdmSFD5FCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 6)
)
if mibBuilder.loadTexts:
    aluWdmSFD5FCard.setStatus("current")
_AluWdmSFD5GCard_ObjectIdentity = ObjectIdentity
aluWdmSFD5GCard = _AluWdmSFD5GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 7)
)
if mibBuilder.loadTexts:
    aluWdmSFD5GCard.setStatus("current")
_AluWdmSFD5HCard_ObjectIdentity = ObjectIdentity
aluWdmSFD5HCard = _AluWdmSFD5HCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 8)
)
if mibBuilder.loadTexts:
    aluWdmSFD5HCard.setStatus("current")
_AluWdmSFD10ACard_ObjectIdentity = ObjectIdentity
aluWdmSFD10ACard = _AluWdmSFD10ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 9)
)
if mibBuilder.loadTexts:
    aluWdmSFD10ACard.setStatus("current")
_AluWdmSFD10BCard_ObjectIdentity = ObjectIdentity
aluWdmSFD10BCard = _AluWdmSFD10BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 10)
)
if mibBuilder.loadTexts:
    aluWdmSFD10BCard.setStatus("current")
_AluWdmSFD10CCard_ObjectIdentity = ObjectIdentity
aluWdmSFD10CCard = _AluWdmSFD10CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 11)
)
if mibBuilder.loadTexts:
    aluWdmSFD10CCard.setStatus("current")
_AluWdmSFD10DCard_ObjectIdentity = ObjectIdentity
aluWdmSFD10DCard = _AluWdmSFD10DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 12)
)
if mibBuilder.loadTexts:
    aluWdmSFD10DCard.setStatus("current")
_AluWdmSFC2ACard_ObjectIdentity = ObjectIdentity
aluWdmSFC2ACard = _AluWdmSFC2ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 13)
)
if mibBuilder.loadTexts:
    aluWdmSFC2ACard.setStatus("current")
_AluWdmSFC2BCard_ObjectIdentity = ObjectIdentity
aluWdmSFC2BCard = _AluWdmSFC2BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 14)
)
if mibBuilder.loadTexts:
    aluWdmSFC2BCard.setStatus("current")
_AluWdmSFC2CCard_ObjectIdentity = ObjectIdentity
aluWdmSFC2CCard = _AluWdmSFC2CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 15)
)
if mibBuilder.loadTexts:
    aluWdmSFC2CCard.setStatus("current")
_AluWdmSFC2DCard_ObjectIdentity = ObjectIdentity
aluWdmSFC2DCard = _AluWdmSFC2DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 16)
)
if mibBuilder.loadTexts:
    aluWdmSFC2DCard.setStatus("current")
_AluWdmSFC4ACard_ObjectIdentity = ObjectIdentity
aluWdmSFC4ACard = _AluWdmSFC4ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 17)
)
if mibBuilder.loadTexts:
    aluWdmSFC4ACard.setStatus("current")
_AluWdmSFC4BCard_ObjectIdentity = ObjectIdentity
aluWdmSFC4BCard = _AluWdmSFC4BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 18)
)
if mibBuilder.loadTexts:
    aluWdmSFC4BCard.setStatus("current")
_AluWdmSFC8Card_ObjectIdentity = ObjectIdentity
aluWdmSFC8Card = _AluWdmSFC8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 19)
)
if mibBuilder.loadTexts:
    aluWdmSFC8Card.setStatus("current")
_AluWdmSFC1ACard_ObjectIdentity = ObjectIdentity
aluWdmSFC1ACard = _AluWdmSFC1ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 20)
)
if mibBuilder.loadTexts:
    aluWdmSFC1ACard.setStatus("current")
_AluWdmSFC1BCard_ObjectIdentity = ObjectIdentity
aluWdmSFC1BCard = _AluWdmSFC1BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 21)
)
if mibBuilder.loadTexts:
    aluWdmSFC1BCard.setStatus("current")
_AluWdmSFC1CCard_ObjectIdentity = ObjectIdentity
aluWdmSFC1CCard = _AluWdmSFC1CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 22)
)
if mibBuilder.loadTexts:
    aluWdmSFC1CCard.setStatus("current")
_AluWdmSFC1DCard_ObjectIdentity = ObjectIdentity
aluWdmSFC1DCard = _AluWdmSFC1DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 23)
)
if mibBuilder.loadTexts:
    aluWdmSFC1DCard.setStatus("current")
_AluWdmSFC1ECard_ObjectIdentity = ObjectIdentity
aluWdmSFC1ECard = _AluWdmSFC1ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 24)
)
if mibBuilder.loadTexts:
    aluWdmSFC1ECard.setStatus("current")
_AluWdmSFC1FCard_ObjectIdentity = ObjectIdentity
aluWdmSFC1FCard = _AluWdmSFC1FCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 25)
)
if mibBuilder.loadTexts:
    aluWdmSFC1FCard.setStatus("current")
_AluWdmSFC1GCard_ObjectIdentity = ObjectIdentity
aluWdmSFC1GCard = _AluWdmSFC1GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 26)
)
if mibBuilder.loadTexts:
    aluWdmSFC1GCard.setStatus("current")
_AluWdmSFC1HCard_ObjectIdentity = ObjectIdentity
aluWdmSFC1HCard = _AluWdmSFC1HCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 27)
)
if mibBuilder.loadTexts:
    aluWdmSFC1HCard.setStatus("current")
_AluWdmSFD8ACard_ObjectIdentity = ObjectIdentity
aluWdmSFD8ACard = _AluWdmSFD8ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 28)
)
if mibBuilder.loadTexts:
    aluWdmSFD8ACard.setStatus("current")
_AluWdmSFD8BCard_ObjectIdentity = ObjectIdentity
aluWdmSFD8BCard = _AluWdmSFD8BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 29)
)
if mibBuilder.loadTexts:
    aluWdmSFD8BCard.setStatus("current")
_AluWdmSFD8CCard_ObjectIdentity = ObjectIdentity
aluWdmSFD8CCard = _AluWdmSFD8CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 30)
)
if mibBuilder.loadTexts:
    aluWdmSFD8CCard.setStatus("current")
_AluWdmSFD8DCard_ObjectIdentity = ObjectIdentity
aluWdmSFD8DCard = _AluWdmSFD8DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 31)
)
if mibBuilder.loadTexts:
    aluWdmSFD8DCard.setStatus("current")
_AluWdmSFD4ACard_ObjectIdentity = ObjectIdentity
aluWdmSFD4ACard = _AluWdmSFD4ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 32)
)
if mibBuilder.loadTexts:
    aluWdmSFD4ACard.setStatus("current")
_AluWdmSFD4BCard_ObjectIdentity = ObjectIdentity
aluWdmSFD4BCard = _AluWdmSFD4BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 33)
)
if mibBuilder.loadTexts:
    aluWdmSFD4BCard.setStatus("current")
_AluWdmSFD4CCard_ObjectIdentity = ObjectIdentity
aluWdmSFD4CCard = _AluWdmSFD4CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 34)
)
if mibBuilder.loadTexts:
    aluWdmSFD4CCard.setStatus("current")
_AluWdmSFD4DCard_ObjectIdentity = ObjectIdentity
aluWdmSFD4DCard = _AluWdmSFD4DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 35)
)
if mibBuilder.loadTexts:
    aluWdmSFD4DCard.setStatus("current")
_AluWdmSFD4ECard_ObjectIdentity = ObjectIdentity
aluWdmSFD4ECard = _AluWdmSFD4ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 36)
)
if mibBuilder.loadTexts:
    aluWdmSFD4ECard.setStatus("current")
_AluWdmSFD4FCard_ObjectIdentity = ObjectIdentity
aluWdmSFD4FCard = _AluWdmSFD4FCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 37)
)
if mibBuilder.loadTexts:
    aluWdmSFD4FCard.setStatus("current")
_AluWdmSFD4GCard_ObjectIdentity = ObjectIdentity
aluWdmSFD4GCard = _AluWdmSFD4GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 38)
)
if mibBuilder.loadTexts:
    aluWdmSFD4GCard.setStatus("current")
_AluWdmSFD4HCard_ObjectIdentity = ObjectIdentity
aluWdmSFD4HCard = _AluWdmSFD4HCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 39)
)
if mibBuilder.loadTexts:
    aluWdmSFD4HCard.setStatus("current")
_AluWdmSFD2ACard_ObjectIdentity = ObjectIdentity
aluWdmSFD2ACard = _AluWdmSFD2ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 40)
)
if mibBuilder.loadTexts:
    aluWdmSFD2ACard.setStatus("current")
_AluWdmSFD2BCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2BCard = _AluWdmSFD2BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 41)
)
if mibBuilder.loadTexts:
    aluWdmSFD2BCard.setStatus("current")
_AluWdmSFD2CCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2CCard = _AluWdmSFD2CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 42)
)
if mibBuilder.loadTexts:
    aluWdmSFD2CCard.setStatus("current")
_AluWdmSFD2DCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2DCard = _AluWdmSFD2DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 43)
)
if mibBuilder.loadTexts:
    aluWdmSFD2DCard.setStatus("current")
_AluWdmSFD2ECard_ObjectIdentity = ObjectIdentity
aluWdmSFD2ECard = _AluWdmSFD2ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 44)
)
if mibBuilder.loadTexts:
    aluWdmSFD2ECard.setStatus("current")
_AluWdmSFD2FCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2FCard = _AluWdmSFD2FCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 45)
)
if mibBuilder.loadTexts:
    aluWdmSFD2FCard.setStatus("current")
_AluWdmSFD2GCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2GCard = _AluWdmSFD2GCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 46)
)
if mibBuilder.loadTexts:
    aluWdmSFD2GCard.setStatus("current")
_AluWdmSFD2HCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2HCard = _AluWdmSFD2HCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 47)
)
if mibBuilder.loadTexts:
    aluWdmSFD2HCard.setStatus("current")
_AluWdmSFD2ICard_ObjectIdentity = ObjectIdentity
aluWdmSFD2ICard = _AluWdmSFD2ICard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 48)
)
if mibBuilder.loadTexts:
    aluWdmSFD2ICard.setStatus("current")
_AluWdmSFD2LCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2LCard = _AluWdmSFD2LCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 49)
)
if mibBuilder.loadTexts:
    aluWdmSFD2LCard.setStatus("current")
_AluWdmSFD2MCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2MCard = _AluWdmSFD2MCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 50)
)
if mibBuilder.loadTexts:
    aluWdmSFD2MCard.setStatus("current")
_AluWdmSFD2NCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2NCard = _AluWdmSFD2NCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 51)
)
if mibBuilder.loadTexts:
    aluWdmSFD2NCard.setStatus("current")
_AluWdmSFD2OCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2OCard = _AluWdmSFD2OCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 52)
)
if mibBuilder.loadTexts:
    aluWdmSFD2OCard.setStatus("current")
_AluWdmSFD2PCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2PCard = _AluWdmSFD2PCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 53)
)
if mibBuilder.loadTexts:
    aluWdmSFD2PCard.setStatus("current")
_AluWdmSFD2QCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2QCard = _AluWdmSFD2QCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 54)
)
if mibBuilder.loadTexts:
    aluWdmSFD2QCard.setStatus("current")
_AluWdmSFD2RCard_ObjectIdentity = ObjectIdentity
aluWdmSFD2RCard = _AluWdmSFD2RCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 55)
)
if mibBuilder.loadTexts:
    aluWdmSFD2RCard.setStatus("current")
_AluWdmVwmSFD8ACard_ObjectIdentity = ObjectIdentity
aluWdmVwmSFD8ACard = _AluWdmVwmSFD8ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 56)
)
if mibBuilder.loadTexts:
    aluWdmVwmSFD8ACard.setStatus("current")
_AluWdmVwmSFD8BCard_ObjectIdentity = ObjectIdentity
aluWdmVwmSFD8BCard = _AluWdmVwmSFD8BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 57)
)
if mibBuilder.loadTexts:
    aluWdmVwmSFD8BCard.setStatus("current")
_AluWdmVwmSFD8CCard_ObjectIdentity = ObjectIdentity
aluWdmVwmSFD8CCard = _AluWdmVwmSFD8CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 58)
)
if mibBuilder.loadTexts:
    aluWdmVwmSFD8CCard.setStatus("current")
_AluWdmVwmSFD8DCard_ObjectIdentity = ObjectIdentity
aluWdmVwmSFD8DCard = _AluWdmVwmSFD8DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 59)
)
if mibBuilder.loadTexts:
    aluWdmVwmSFD8DCard.setStatus("current")
_AluWdmVwmSFC8Card_ObjectIdentity = ObjectIdentity
aluWdmVwmSFC8Card = _AluWdmVwmSFC8Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 60)
)
if mibBuilder.loadTexts:
    aluWdmVwmSFC8Card.setStatus("current")
_AluWdmMonOcmCard_ObjectIdentity = ObjectIdentity
aluWdmMonOcmCard = _AluWdmMonOcmCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 61)
)
if mibBuilder.loadTexts:
    aluWdmMonOcmCard.setStatus("current")
_AluWdmSfdc8ACard_ObjectIdentity = ObjectIdentity
aluWdmSfdc8ACard = _AluWdmSfdc8ACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 62)
)
if mibBuilder.loadTexts:
    aluWdmSfdc8ACard.setStatus("current")
_AluWdmSfdc8BCard_ObjectIdentity = ObjectIdentity
aluWdmSfdc8BCard = _AluWdmSfdc8BCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 63)
)
if mibBuilder.loadTexts:
    aluWdmSfdc8BCard.setStatus("current")
_AluWdmSfdc8CCard_ObjectIdentity = ObjectIdentity
aluWdmSfdc8CCard = _AluWdmSfdc8CCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 64)
)
if mibBuilder.loadTexts:
    aluWdmSfdc8CCard.setStatus("current")
_AluWdmSfdc8DCard_ObjectIdentity = ObjectIdentity
aluWdmSfdc8DCard = _AluWdmSfdc8DCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 65)
)
if mibBuilder.loadTexts:
    aluWdmSfdc8DCard.setStatus("current")
_AluWdmSfdc8ECard_ObjectIdentity = ObjectIdentity
aluWdmSfdc8ECard = _AluWdmSfdc8ECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 66)
)
if mibBuilder.loadTexts:
    aluWdmSfdc8ECard.setStatus("current")
_NokiaSfd5ADCard_ObjectIdentity = ObjectIdentity
nokiaSfd5ADCard = _NokiaSfd5ADCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 67)
)
if mibBuilder.loadTexts:
    nokiaSfd5ADCard.setStatus("current")
_NokiaSfd5BDCard_ObjectIdentity = ObjectIdentity
nokiaSfd5BDCard = _NokiaSfd5BDCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 68)
)
if mibBuilder.loadTexts:
    nokiaSfd5BDCard.setStatus("current")
_NokiaSfd5CDCard_ObjectIdentity = ObjectIdentity
nokiaSfd5CDCard = _NokiaSfd5CDCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 69)
)
if mibBuilder.loadTexts:
    nokiaSfd5CDCard.setStatus("current")
_NokiaSfd5DDCard_ObjectIdentity = ObjectIdentity
nokiaSfd5DDCard = _NokiaSfd5DDCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 70)
)
if mibBuilder.loadTexts:
    nokiaSfd5DDCard.setStatus("current")
_NokiaSfd5AUCard_ObjectIdentity = ObjectIdentity
nokiaSfd5AUCard = _NokiaSfd5AUCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 71)
)
if mibBuilder.loadTexts:
    nokiaSfd5AUCard.setStatus("current")
_NokiaSfd5BUCard_ObjectIdentity = ObjectIdentity
nokiaSfd5BUCard = _NokiaSfd5BUCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 72)
)
if mibBuilder.loadTexts:
    nokiaSfd5BUCard.setStatus("current")
_NokiaSfd5CUCard_ObjectIdentity = ObjectIdentity
nokiaSfd5CUCard = _NokiaSfd5CUCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 73)
)
if mibBuilder.loadTexts:
    nokiaSfd5CUCard.setStatus("current")
_NokiaSfd5DUCard_ObjectIdentity = ObjectIdentity
nokiaSfd5DUCard = _NokiaSfd5DUCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 74)
)
if mibBuilder.loadTexts:
    nokiaSfd5DUCard.setStatus("current")
_NokiaDcm2pCard_ObjectIdentity = ObjectIdentity
nokiaDcm2pCard = _NokiaDcm2pCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 5, 12, 75)
)
if mibBuilder.loadTexts:
    nokiaDcm2pCard.setStatus("current")
_TropicCommonEquipmentReg_ObjectIdentity = ObjectIdentity
tropicCommonEquipmentReg = _TropicCommonEquipmentReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6)
)
if mibBuilder.loadTexts:
    tropicCommonEquipmentReg.setStatus("current")
_AluWdmPowerFilterCard_ObjectIdentity = ObjectIdentity
aluWdmPowerFilterCard = _AluWdmPowerFilterCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 4)
)
if mibBuilder.loadTexts:
    aluWdmPowerFilterCard.setStatus("current")
_AluWdmFanUnitCard_ObjectIdentity = ObjectIdentity
aluWdmFanUnitCard = _AluWdmFanUnitCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 5)
)
if mibBuilder.loadTexts:
    aluWdmFanUnitCard.setStatus("current")
_AluWdmUserInterfacePanelCard_ObjectIdentity = ObjectIdentity
aluWdmUserInterfacePanelCard = _AluWdmUserInterfacePanelCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 6)
)
if mibBuilder.loadTexts:
    aluWdmUserInterfacePanelCard.setStatus("current")
_AluWdmBusTerminationCard_ObjectIdentity = ObjectIdentity
aluWdmBusTerminationCard = _AluWdmBusTerminationCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 7)
)
if mibBuilder.loadTexts:
    aluWdmBusTerminationCard.setStatus("current")
_AluWdmBusTerminationOnlyCard_ObjectIdentity = ObjectIdentity
aluWdmBusTerminationOnlyCard = _AluWdmBusTerminationOnlyCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 8)
)
if mibBuilder.loadTexts:
    aluWdmBusTerminationOnlyCard.setStatus("current")
_AluWdmPSS8ShelfPanelCard_ObjectIdentity = ObjectIdentity
aluWdmPSS8ShelfPanelCard = _AluWdmPSS8ShelfPanelCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 9)
)
if mibBuilder.loadTexts:
    aluWdmPSS8ShelfPanelCard.setStatus("current")
_AluWdmPSS8UserInterfacePanelCard_ObjectIdentity = ObjectIdentity
aluWdmPSS8UserInterfacePanelCard = _AluWdmPSS8UserInterfacePanelCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 10)
)
if mibBuilder.loadTexts:
    aluWdmPSS8UserInterfacePanelCard.setStatus("current")
_AluWdmMultiFunctionCard_ObjectIdentity = ObjectIdentity
aluWdmMultiFunctionCard = _AluWdmMultiFunctionCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 11)
)
if mibBuilder.loadTexts:
    aluWdmMultiFunctionCard.setStatus("current")
_AluWdmPSS8PowerFilterAcCard_ObjectIdentity = ObjectIdentity
aluWdmPSS8PowerFilterAcCard = _AluWdmPSS8PowerFilterAcCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 12)
)
if mibBuilder.loadTexts:
    aluWdmPSS8PowerFilterAcCard.setStatus("current")
_AluWdmPSS96PowerFilterCard_ObjectIdentity = ObjectIdentity
aluWdmPSS96PowerFilterCard = _AluWdmPSS96PowerFilterCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 13)
)
if mibBuilder.loadTexts:
    aluWdmPSS96PowerFilterCard.setStatus("current")
_AluWdmPSS8xMultiFunctionCard_ObjectIdentity = ObjectIdentity
aluWdmPSS8xMultiFunctionCard = _AluWdmPSS8xMultiFunctionCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 14)
)
if mibBuilder.loadTexts:
    aluWdmPSS8xMultiFunctionCard.setStatus("current")
_AluWdmPSS8xPowerFilterCard_ObjectIdentity = ObjectIdentity
aluWdmPSS8xPowerFilterCard = _AluWdmPSS8xPowerFilterCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 15)
)
if mibBuilder.loadTexts:
    aluWdmPSS8xPowerFilterCard.setStatus("current")
_NokiaVwmMsFanTOCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsFanTOCard = _NokiaVwmMsFanTOCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 18)
)
if mibBuilder.loadTexts:
    nokiaVwmMsFanTOCard.setStatus("current")
_NokiaVwmMsOpsPsuCard_ObjectIdentity = ObjectIdentity
nokiaVwmMsOpsPsuCard = _NokiaVwmMsOpsPsuCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 19)
)
if mibBuilder.loadTexts:
    nokiaVwmMsOpsPsuCard.setStatus("current")
_AluWdmPSS8PowerFilterWithFCRUCard_ObjectIdentity = ObjectIdentity
aluWdmPSS8PowerFilterWithFCRUCard = _AluWdmPSS8PowerFilterWithFCRUCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 20)
)
if mibBuilder.loadTexts:
    aluWdmPSS8PowerFilterWithFCRUCard.setStatus("current")
_AluWdmPSS16IIPowerFilterWithFCRUCard_ObjectIdentity = ObjectIdentity
aluWdmPSS16IIPowerFilterWithFCRUCard = _AluWdmPSS16IIPowerFilterWithFCRUCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 21)
)
if mibBuilder.loadTexts:
    aluWdmPSS16IIPowerFilterWithFCRUCard.setStatus("current")
_AluWdmPSS12xPowerFilterCard_ObjectIdentity = ObjectIdentity
aluWdmPSS12xPowerFilterCard = _AluWdmPSS12xPowerFilterCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 22)
)
if mibBuilder.loadTexts:
    aluWdmPSS12xPowerFilterCard.setStatus("current")
_AluWdmMultiFunctionPSIMCard_ObjectIdentity = ObjectIdentity
aluWdmMultiFunctionPSIMCard = _AluWdmMultiFunctionPSIMCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 23)
)
if mibBuilder.loadTexts:
    aluWdmMultiFunctionPSIMCard.setStatus("current")
_NokiaVwmMsFanDECard_ObjectIdentity = ObjectIdentity
nokiaVwmMsFanDECard = _NokiaVwmMsFanDECard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 24)
)
if mibBuilder.loadTexts:
    nokiaVwmMsFanDECard.setStatus("current")
_AluWdmMultiFunctionPSILCard_ObjectIdentity = ObjectIdentity
aluWdmMultiFunctionPSILCard = _AluWdmMultiFunctionPSILCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 25)
)
if mibBuilder.loadTexts:
    aluWdmMultiFunctionPSILCard.setStatus("current")
_NokiaT24PFCard_ObjectIdentity = ObjectIdentity
nokiaT24PFCard = _NokiaT24PFCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 26)
)
if mibBuilder.loadTexts:
    nokiaT24PFCard.setStatus("current")
_NokiaT12PFCard_ObjectIdentity = ObjectIdentity
nokiaT12PFCard = _NokiaT12PFCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 27)
)
if mibBuilder.loadTexts:
    nokiaT12PFCard.setStatus("current")
_NokiaT24FUCard_ObjectIdentity = ObjectIdentity
nokiaT24FUCard = _NokiaT24FUCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 28)
)
if mibBuilder.loadTexts:
    nokiaT24FUCard.setStatus("current")
_NokiaVwmMsFanIICard_ObjectIdentity = ObjectIdentity
nokiaVwmMsFanIICard = _NokiaVwmMsFanIICard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 29)
)
if mibBuilder.loadTexts:
    nokiaVwmMsFanIICard.setStatus("current")
_AluWdmMultiFunctionPSIMXCard_ObjectIdentity = ObjectIdentity
aluWdmMultiFunctionPSIMXCard = _AluWdmMultiFunctionPSIMXCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 30)
)
if mibBuilder.loadTexts:
    aluWdmMultiFunctionPSIMXCard.setStatus("current")
_NokiaS24PFCard_ObjectIdentity = ObjectIdentity
nokiaS24PFCard = _NokiaS24PFCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 31)
)
if mibBuilder.loadTexts:
    nokiaS24PFCard.setStatus("current")
_NokiaS24FUCard_ObjectIdentity = ObjectIdentity
nokiaS24FUCard = _NokiaS24FUCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 6, 32)
)
if mibBuilder.loadTexts:
    nokiaS24FUCard.setStatus("current")
_TropicGeneric_ObjectIdentity = ObjectIdentity
tropicGeneric = _TropicGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2)
)
if mibBuilder.loadTexts:
    tropicGeneric.setStatus("current")
_TnSystem_ObjectIdentity = ObjectIdentity
tnSystem = _TnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1)
)
if mibBuilder.loadTexts:
    tnSystem.setStatus("current")
_TnSystemMIB_ObjectIdentity = ObjectIdentity
tnSystemMIB = _TnSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnSystemMIB.setStatus("current")
_TnNotificationMIB_ObjectIdentity = ObjectIdentity
tnNotificationMIB = _TnNotificationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnNotificationMIB.setStatus("current")
_TnLogMIB_ObjectIdentity = ObjectIdentity
tnLogMIB = _TnLogMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnLogMIB.setStatus("current")
_TnDiagnosticMIB_ObjectIdentity = ObjectIdentity
tnDiagnosticMIB = _TnDiagnosticMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnDiagnosticMIB.setStatus("current")
_TnSoftwareMIB_ObjectIdentity = ObjectIdentity
tnSoftwareMIB = _TnSoftwareMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnSoftwareMIB.setStatus("current")
_TnPowerMgmtMIB_ObjectIdentity = ObjectIdentity
tnPowerMgmtMIB = _TnPowerMgmtMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnPowerMgmtMIB.setStatus("current")
_TnUserMgmtMIB_ObjectIdentity = ObjectIdentity
tnUserMgmtMIB = _TnUserMgmtMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tnUserMgmtMIB.setStatus("current")
_TnPhMNotificationMIB_ObjectIdentity = ObjectIdentity
tnPhMNotificationMIB = _TnPhMNotificationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tnPhMNotificationMIB.setStatus("current")
_TnAsonMIB_ObjectIdentity = ObjectIdentity
tnAsonMIB = _TnAsonMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9)
)
if mibBuilder.loadTexts:
    tnAsonMIB.setStatus("current")
_TnGmplsMIB_ObjectIdentity = ObjectIdentity
tnGmplsMIB = _TnGmplsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10)
)
if mibBuilder.loadTexts:
    tnGmplsMIB.setStatus("current")
_TnGmplsObjs_ObjectIdentity = ObjectIdentity
tnGmplsObjs = _TnGmplsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tnGmplsObjs.setStatus("current")
_TnAbsNodeMIB_ObjectIdentity = ObjectIdentity
tnAbsNodeMIB = _TnAbsNodeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11)
)
if mibBuilder.loadTexts:
    tnAbsNodeMIB.setStatus("current")
_TnAbsNodeObjs_ObjectIdentity = ObjectIdentity
tnAbsNodeObjs = _TnAbsNodeObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    tnAbsNodeObjs.setStatus("current")
_TnGenericNotificationMIB_ObjectIdentity = ObjectIdentity
tnGenericNotificationMIB = _TnGenericNotificationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 12)
)
if mibBuilder.loadTexts:
    tnGenericNotificationMIB.setStatus("current")
_TnGenericLogMIB_ObjectIdentity = ObjectIdentity
tnGenericLogMIB = _TnGenericLogMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 13)
)
if mibBuilder.loadTexts:
    tnGenericLogMIB.setStatus("current")
_TnDhpMIB_ObjectIdentity = ObjectIdentity
tnDhpMIB = _TnDhpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 14)
)
if mibBuilder.loadTexts:
    tnDhpMIB.setStatus("current")
_TnDhpObjs_ObjectIdentity = ObjectIdentity
tnDhpObjs = _TnDhpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 14, 1)
)
if mibBuilder.loadTexts:
    tnDhpObjs.setStatus("current")
_TnEquipment_ObjectIdentity = ObjectIdentity
tnEquipment = _TnEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2)
)
if mibBuilder.loadTexts:
    tnEquipment.setStatus("current")
_TnShelf_ObjectIdentity = ObjectIdentity
tnShelf = _TnShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnShelf.setStatus("current")
_TnShelfMIB_ObjectIdentity = ObjectIdentity
tnShelfMIB = _TnShelfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnShelfMIB.setStatus("current")
_TnSlot_ObjectIdentity = ObjectIdentity
tnSlot = _TnSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tnSlot.setStatus("current")
_TnSlotMIB_ObjectIdentity = ObjectIdentity
tnSlotMIB = _TnSlotMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnSlotMIB.setStatus("current")
_TnCard_ObjectIdentity = ObjectIdentity
tnCard = _TnCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3)
)
if mibBuilder.loadTexts:
    tnCard.setStatus("current")
_TnCardMIB_ObjectIdentity = ObjectIdentity
tnCardMIB = _TnCardMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tnCardMIB.setStatus("current")
_TnWaveKeyMIB_ObjectIdentity = ObjectIdentity
tnWaveKeyMIB = _TnWaveKeyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tnWaveKeyMIB.setStatus("current")
_TnControlCardMIB_ObjectIdentity = ObjectIdentity
tnControlCardMIB = _TnControlCardMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    tnControlCardMIB.setStatus("current")
_TnEthernetCardMIB_ObjectIdentity = ObjectIdentity
tnEthernetCardMIB = _TnEthernetCardMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    tnEthernetCardMIB.setStatus("current")
_TnOpticalCardMIB_ObjectIdentity = ObjectIdentity
tnOpticalCardMIB = _TnOpticalCardMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5)
)
if mibBuilder.loadTexts:
    tnOpticalCardMIB.setStatus("current")
_TnSwitchCardMIB_ObjectIdentity = ObjectIdentity
tnSwitchCardMIB = _TnSwitchCardMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 6)
)
if mibBuilder.loadTexts:
    tnSwitchCardMIB.setStatus("current")
_TnAmplifierMIB_ObjectIdentity = ObjectIdentity
tnAmplifierMIB = _TnAmplifierMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 7)
)
if mibBuilder.loadTexts:
    tnAmplifierMIB.setStatus("current")
_TnPort_ObjectIdentity = ObjectIdentity
tnPort = _TnPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tnPort.setStatus("current")
_TnAccessPortMIB_ObjectIdentity = ObjectIdentity
tnAccessPortMIB = _TnAccessPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnAccessPortMIB.setStatus("current")
_TnEthernetPortMIB_ObjectIdentity = ObjectIdentity
tnEthernetPortMIB = _TnEthernetPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    tnEthernetPortMIB.setStatus("current")
_TnOpticalPortMIB_ObjectIdentity = ObjectIdentity
tnOpticalPortMIB = _TnOpticalPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    tnOpticalPortMIB.setStatus("current")
_TnSwitchPortMIB_ObjectIdentity = ObjectIdentity
tnSwitchPortMIB = _TnSwitchPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 4)
)
if mibBuilder.loadTexts:
    tnSwitchPortMIB.setStatus("current")
_TnOchMIB_ObjectIdentity = ObjectIdentity
tnOchMIB = _TnOchMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 5)
)
if mibBuilder.loadTexts:
    tnOchMIB.setStatus("current")
_TnVtsConnMIB_ObjectIdentity = ObjectIdentity
tnVtsConnMIB = _TnVtsConnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 6)
)
if mibBuilder.loadTexts:
    tnVtsConnMIB.setStatus("current")
_TnOtuOduMIB_ObjectIdentity = ObjectIdentity
tnOtuOduMIB = _TnOtuOduMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 7)
)
if mibBuilder.loadTexts:
    tnOtuOduMIB.setStatus("current")
_TnSyncEMIB_ObjectIdentity = ObjectIdentity
tnSyncEMIB = _TnSyncEMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8)
)
if mibBuilder.loadTexts:
    tnSyncEMIB.setStatus("current")
_TnPtpMIB_ObjectIdentity = ObjectIdentity
tnPtpMIB = _TnPtpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9)
)
if mibBuilder.loadTexts:
    tnPtpMIB.setStatus("current")
_TnOthMIB_ObjectIdentity = ObjectIdentity
tnOthMIB = _TnOthMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 10)
)
if mibBuilder.loadTexts:
    tnOthMIB.setStatus("current")
_TnIEEE8023brMIB_ObjectIdentity = ObjectIdentity
tnIEEE8023brMIB = _TnIEEE8023brMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11)
)
if mibBuilder.loadTexts:
    tnIEEE8023brMIB.setStatus("current")
_TnRoeMib_ObjectIdentity = ObjectIdentity
tnRoeMib = _TnRoeMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 12)
)
if mibBuilder.loadTexts:
    tnRoeMib.setStatus("current")
_TnMiscEquipment_ObjectIdentity = ObjectIdentity
tnMiscEquipment = _TnMiscEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5)
)
if mibBuilder.loadTexts:
    tnMiscEquipment.setStatus("current")
_TnFanMIB_ObjectIdentity = ObjectIdentity
tnFanMIB = _TnFanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tnFanMIB.setStatus("current")
_TnBreakerMIB_ObjectIdentity = ObjectIdentity
tnBreakerMIB = _TnBreakerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    tnBreakerMIB.setStatus("current")
_TnAlarmPanelMIB_ObjectIdentity = ObjectIdentity
tnAlarmPanelMIB = _TnAlarmPanelMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    tnAlarmPanelMIB.setStatus("current")
_TnVwmMsMIB_ObjectIdentity = ObjectIdentity
tnVwmMsMIB = _TnVwmMsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6)
)
if mibBuilder.loadTexts:
    tnVwmMsMIB.setStatus("current")
_TnPsdMIB_ObjectIdentity = ObjectIdentity
tnPsdMIB = _TnPsdMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7)
)
if mibBuilder.loadTexts:
    tnPsdMIB.setStatus("current")
_TnServices_ObjectIdentity = ObjectIdentity
tnServices = _TnServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3)
)
if mibBuilder.loadTexts:
    tnServices.setStatus("current")
_TnL1ServiceMIB_ObjectIdentity = ObjectIdentity
tnL1ServiceMIB = _TnL1ServiceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tnL1ServiceMIB.setStatus("current")
_TnL2ServiceMIB_ObjectIdentity = ObjectIdentity
tnL2ServiceMIB = _TnL2ServiceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tnL2ServiceMIB.setStatus("current")
_TnStatistics_ObjectIdentity = ObjectIdentity
tnStatistics = _TnStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4)
)
if mibBuilder.loadTexts:
    tnStatistics.setStatus("current")
_TnStatisticsMIB_ObjectIdentity = ObjectIdentity
tnStatisticsMIB = _TnStatisticsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnStatisticsMIB.setStatus("current")
_TnProtocols_ObjectIdentity = ObjectIdentity
tnProtocols = _TnProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5)
)
if mibBuilder.loadTexts:
    tnProtocols.setStatus("current")
_TnOspfMIB_ObjectIdentity = ObjectIdentity
tnOspfMIB = _TnOspfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tnOspfMIB.setStatus("current")
_TropicProducts_ObjectIdentity = ObjectIdentity
tropicProducts = _TropicProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 3)
)
if mibBuilder.loadTexts:
    tropicProducts.setStatus("current")
_TropicExpr_ObjectIdentity = ObjectIdentity
tropicExpr = _TropicExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4)
)
if mibBuilder.loadTexts:
    tropicExpr.setStatus("current")
_TnExprOpticalCardMIB_ObjectIdentity = ObjectIdentity
tnExprOpticalCardMIB = _TnExprOpticalCardMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 1)
)
if mibBuilder.loadTexts:
    tnExprOpticalCardMIB.setStatus("current")
_TnExprOpticalPortMIB_ObjectIdentity = ObjectIdentity
tnExprOpticalPortMIB = _TnExprOpticalPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 2)
)
if mibBuilder.loadTexts:
    tnExprOpticalPortMIB.setStatus("current")
_TnExprScalarsMIB_ObjectIdentity = ObjectIdentity
tnExprScalarsMIB = _TnExprScalarsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3)
)
if mibBuilder.loadTexts:
    tnExprScalarsMIB.setStatus("current")
_TnReg_ObjectIdentity = ObjectIdentity
tnReg = _TnReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5)
)
if mibBuilder.loadTexts:
    tnReg.setStatus("current")
_TnModules_ObjectIdentity = ObjectIdentity
tnModules = _TnModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1)
)
if mibBuilder.loadTexts:
    tnModules.setStatus("current")
_TnSRMIBModules_ObjectIdentity = ObjectIdentity
tnSRMIBModules = _TnSRMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3)
)
if mibBuilder.loadTexts:
    tnSRMIBModules.setStatus("current")
_TnRmdMIBModules_ObjectIdentity = ObjectIdentity
tnRmdMIBModules = _TnRmdMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 4)
)
if mibBuilder.loadTexts:
    tnRmdMIBModules.setStatus("current")
_TnProducts_ObjectIdentity = ObjectIdentity
tnProducts = _TnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6)
)
if mibBuilder.loadTexts:
    tnProducts.setStatus("current")
_TnSRMIB_ObjectIdentity = ObjectIdentity
tnSRMIB = _TnSRMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1)
)
if mibBuilder.loadTexts:
    tnSRMIB.setStatus("current")
_TnSRObjs_ObjectIdentity = ObjectIdentity
tnSRObjs = _TnSRObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2)
)
if mibBuilder.loadTexts:
    tnSRObjs.setStatus("current")
_TnSRNotifyPrefix_ObjectIdentity = ObjectIdentity
tnSRNotifyPrefix = _TnSRNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3)
)
if mibBuilder.loadTexts:
    tnSRNotifyPrefix.setStatus("current")
_TnRmdMIB_ObjectIdentity = ObjectIdentity
tnRmdMIB = _TnRmdMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4)
)
if mibBuilder.loadTexts:
    tnRmdMIB.setStatus("current")
_TnRmdObjs_ObjectIdentity = ObjectIdentity
tnRmdObjs = _TnRmdObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1)
)
if mibBuilder.loadTexts:
    tnRmdObjs.setStatus("current")
_TnSASProducts_ObjectIdentity = ObjectIdentity
tnSASProducts = _TnSASProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7)
)
if mibBuilder.loadTexts:
    tnSASProducts.setStatus("current")
_TnServiceAccessSwitches_ObjectIdentity = ObjectIdentity
tnServiceAccessSwitches = _TnServiceAccessSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2)
)
if mibBuilder.loadTexts:
    tnServiceAccessSwitches.setStatus("current")
_TnSASRegistry_ObjectIdentity = ObjectIdentity
tnSASRegistry = _TnSASRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 1)
)
if mibBuilder.loadTexts:
    tnSASRegistry.setStatus("current")
_TnSASModules_ObjectIdentity = ObjectIdentity
tnSASModules = _TnSASModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnSASModules.setStatus("current")
_TnSASMIBModules_ObjectIdentity = ObjectIdentity
tnSASMIBModules = _TnSASMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnSASMIBModules.setStatus("current")
_TnSASMIB_ObjectIdentity = ObjectIdentity
tnSASMIB = _TnSASMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2)
)
if mibBuilder.loadTexts:
    tnSASMIB.setStatus("current")
_TnSASObjs_ObjectIdentity = ObjectIdentity
tnSASObjs = _TnSASObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tnSASObjs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-GLOBAL-REG",
    **{"tropic": tropic,
       "tropicRegistry": tropicRegistry,
       "tropicModules": tropicModules,
       "tropicGlobalRegModule": tropicGlobalRegModule,
       "tnGenericModules": tnGenericModules,
       "tnSystemModules": tnSystemModules,
       "tnEquipmentModules": tnEquipmentModules,
       "tnShelfModules": tnShelfModules,
       "tnSlotModules": tnSlotModules,
       "tnCardModules": tnCardModules,
       "tnPortModules": tnPortModules,
       "tnMiscModules": tnMiscModules,
       "tnVwmMsModules": tnVwmMsModules,
       "tnPsdModules": tnPsdModules,
       "tnServiceModules": tnServiceModules,
       "tnProtocolModules": tnProtocolModules,
       "tropicExprModules": tropicExprModules,
       "tnGmplsMIBModules": tnGmplsMIBModules,
       "tnAbsNodeMIBModules": tnAbsNodeMIBModules,
       "tnDhpMIBModules": tnDhpMIBModules,
       "tnTypeDefinitionModules": tnTypeDefinitionModules,
       "tropicMetroReg": tropicMetroReg,
       "tropicMetroNodeReg": tropicMetroNodeReg,
       "tropicTRX24000": tropicTRX24000,
       "aluWdm1830PSS32": aluWdm1830PSS32,
       "aluWdm1830PSS1": aluWdm1830PSS1,
       "aluWdm1830PSS1MD4H": aluWdm1830PSS1MD4H,
       "aluWdm1830PSS1GBEH": aluWdm1830PSS1GBEH,
       "aluWdm1830PSS": aluWdm1830PSS,
       "aluWdm1830PSS4": aluWdm1830PSS4,
       "aluWdm1830PSS1MSAH": aluWdm1830PSS1MSAH,
       "nokia1830VwmMs": nokia1830VwmMs,
       "nokia1830Psd": nokia1830Psd,
       "aluWdm1830PSI": aluWdm1830PSI,
       "aluWdm1830PSIM": aluWdm1830PSIM,
       "aluWdm1830OLS": aluWdm1830OLS,
       "nokia1830TPS": nokia1830TPS,
       "nokia1830SAS": nokia1830SAS,
       "tropicShelfReg": tropicShelfReg,
       "tropicEmptyShelf": tropicEmptyShelf,
       "tropicUnknownShelf": tropicUnknownShelf,
       "aluWdmSfd44Shelf": aluWdmSfd44Shelf,
       "aluWdmDcmShelf": aluWdmDcmShelf,
       "aluWdmUniversalShelf": aluWdmUniversalShelf,
       "aluWdmSfd44bShelf": aluWdmSfd44bShelf,
       "aluWdmItlbShelf": aluWdmItlbShelf,
       "aluWdmPSS32UniversalShelf": aluWdmPSS32UniversalShelf,
       "aluWdmPSS16UniversalShelf": aluWdmPSS16UniversalShelf,
       "aluWdmSfd40Shelf": aluWdmSfd40Shelf,
       "aluWdmSfd40bShelf": aluWdmSfd40bShelf,
       "aluWdmPSS4UniversalShelf": aluWdmPSS4UniversalShelf,
       "aluWdmPSS36UniversalShelf": aluWdmPSS36UniversalShelf,
       "aluWdmPSS64UniversalShelf": aluWdmPSS64UniversalShelf,
       "aluWdmItluShelf": aluWdmItluShelf,
       "aluWdmPSS32SwitchUniversalShelf": aluWdmPSS32SwitchUniversalShelf,
       "aluWdmPSS32Switch1P2TUniversalShelf": aluWdmPSS32Switch1P2TUniversalShelf,
       "aluWdmPsc1x6Shelf": aluWdmPsc1x6Shelf,
       "aluWdmPSS8UniversalShelf": aluWdmPSS8UniversalShelf,
       "aluWdmPSS16IIUniversalShelf": aluWdmPSS16IIUniversalShelf,
       "aluWdmPSS48UniversalShelf": aluWdmPSS48UniversalShelf,
       "aluWdmPSS96UniversalShelf": aluWdmPSS96UniversalShelf,
       "aluWdmMsh8fsmShelf": aluWdmMsh8fsmShelf,
       "aluWdmVwmCwUniversalShelf": aluWdmVwmCwUniversalShelf,
       "aluWdmVwmDwUniversalShelf": aluWdmVwmDwUniversalShelf,
       "nokiaVwmMsOsu20Shelf": nokiaVwmMsOsu20Shelf,
       "nokiaVwmMsTlu9Shelf": nokiaVwmMsTlu9Shelf,
       "nokiaVwmMsPmu9UcShelf": nokiaVwmMsPmu9UcShelf,
       "nokiaVwmMsPmu9LcShelf": nokiaVwmMsPmu9LcShelf,
       "nokiaVwmMsPmu9UcmShelf": nokiaVwmMsPmu9UcmShelf,
       "nokiaVwmMsPmu9LcmShelf": nokiaVwmMsPmu9LcmShelf,
       "nokiaVwmMsItp4UcaShelf": nokiaVwmMsItp4UcaShelf,
       "nokiaVwmMsItp4UcbShelf": nokiaVwmMsItp4UcbShelf,
       "nokiaVwmMsItp4LcaShelf": nokiaVwmMsItp4LcaShelf,
       "nokiaVwmMsItp4LcbShelf": nokiaVwmMsItp4LcbShelf,
       "nokiaVwmMsSmmAoShelf": nokiaVwmMsSmmAoShelf,
       "nokiaVwmMsSmmAiShelf": nokiaVwmMsSmmAiShelf,
       "nokiaVwmMsOpsShelf": nokiaVwmMsOpsShelf,
       "aluWdmPSS8xUniversalShelf": aluWdmPSS8xUniversalShelf,
       "nokiaPsdShelf": nokiaPsdShelf,
       "nokiaVwmMsTlu9mShelf": nokiaVwmMsTlu9mShelf,
       "aluWdmPSI1TUniversalShelf": aluWdmPSI1TUniversalShelf,
       "aluWdmPSI2TUniversalShelf": aluWdmPSI2TUniversalShelf,
       "aluWdmPSI2TLUniversalShelf": aluWdmPSI2TLUniversalShelf,
       "aluWdmPSIMUniversalShelf": aluWdmPSIMUniversalShelf,
       "aluWdmPSS12xUniversalShelf": aluWdmPSS12xUniversalShelf,
       "nokiaVwmMsPmuD21AShelf": nokiaVwmMsPmuD21AShelf,
       "nokiaVwmMsPmuD21BShelf": nokiaVwmMsPmuD21BShelf,
       "nokiaVwmMsPmuD21CShelf": nokiaVwmMsPmuD21CShelf,
       "nokiaVwmMsPmuD21DShelf": nokiaVwmMsPmuD21DShelf,
       "aluWdmSfd96Shelf": aluWdmSfd96Shelf,
       "aluWdmBmuPShelf": aluWdmBmuPShelf,
       "aluWdmSplit2Shelf": aluWdmSplit2Shelf,
       "aluWdmOscCplrShelf": aluWdmOscCplrShelf,
       "aluWdmOAUnidirShelf": aluWdmOAUnidirShelf,
       "aluWdmMsh4fsbShelf": aluWdmMsh4fsbShelf,
       "nokiaVwmMsTlu200Shelf": nokiaVwmMsTlu200Shelf,
       "nokiaVwmMsADVGIShelf": nokiaVwmMsADVGIShelf,
       "aluWdmPSIL3uUniversalShelf": aluWdmPSIL3uUniversalShelf,
       "aluWdmPSIL5uUniversalShelf": aluWdmPSIL5uUniversalShelf,
       "nokiaSfd10ALmShelf": nokiaSfd10ALmShelf,
       "nokiaSfd10BLmShelf": nokiaSfd10BLmShelf,
       "nokiaSfd10CLmShelf": nokiaSfd10CLmShelf,
       "nokiaSfd10DLmShelf": nokiaSfd10DLmShelf,
       "nokiaSfd2AShelf": nokiaSfd2AShelf,
       "nokiaSfd2BShelf": nokiaSfd2BShelf,
       "nokiaSfd2CShelf": nokiaSfd2CShelf,
       "nokiaSfd2DShelf": nokiaSfd2DShelf,
       "nokiaSfd2EShelf": nokiaSfd2EShelf,
       "nokiaSfd2FShelf": nokiaSfd2FShelf,
       "nokiaSfd2GShelf": nokiaSfd2GShelf,
       "nokiaSfd2HShelf": nokiaSfd2HShelf,
       "nokiaSfd2IShelf": nokiaSfd2IShelf,
       "nokiaSfd2LShelf": nokiaSfd2LShelf,
       "nokiaSfd2MShelf": nokiaSfd2MShelf,
       "nokiaSfd2NShelf": nokiaSfd2NShelf,
       "nokiaSfd2OShelf": nokiaSfd2OShelf,
       "nokiaSfd2PShelf": nokiaSfd2PShelf,
       "nokiaSfd2QShelf": nokiaSfd2QShelf,
       "nokiaSfd2RShelf": nokiaSfd2RShelf,
       "nokiaSfd4AShelf": nokiaSfd4AShelf,
       "nokiaSfd4BShelf": nokiaSfd4BShelf,
       "nokiaSfd4CShelf": nokiaSfd4CShelf,
       "nokiaSfd4DShelf": nokiaSfd4DShelf,
       "nokiaSfd4EShelf": nokiaSfd4EShelf,
       "nokiaSfd4FShelf": nokiaSfd4FShelf,
       "nokiaSfd4GShelf": nokiaSfd4GShelf,
       "nokiaSfd4HShelf": nokiaSfd4HShelf,
       "nokiaSfd8AShelf": nokiaSfd8AShelf,
       "nokiaSfd8BShelf": nokiaSfd8BShelf,
       "nokiaSfd8CShelf": nokiaSfd8CShelf,
       "nokiaSfd8DShelf": nokiaSfd8DShelf,
       "nokiaSfc1AShelf": nokiaSfc1AShelf,
       "nokiaSfc1BShelf": nokiaSfc1BShelf,
       "nokiaSfc1CShelf": nokiaSfc1CShelf,
       "nokiaSfc1DShelf": nokiaSfc1DShelf,
       "nokiaSfc1EShelf": nokiaSfc1EShelf,
       "nokiaSfc1FShelf": nokiaSfc1FShelf,
       "nokiaSfc1GShelf": nokiaSfc1GShelf,
       "nokiaSfc1HShelf": nokiaSfc1HShelf,
       "nokiaSfc2ABShelf": nokiaSfc2ABShelf,
       "nokiaSfc2CDShelf": nokiaSfc2CDShelf,
       "nokiaSfc2EFShelf": nokiaSfc2EFShelf,
       "nokiaSfc2GHShelf": nokiaSfc2GHShelf,
       "nokiaSfc4ADShelf": nokiaSfc4ADShelf,
       "nokiaSfc4EHShelf": nokiaSfc4EHShelf,
       "nokiaSfc8UShelf": nokiaSfc8UShelf,
       "nokiaSfc8LShelf": nokiaSfc8LShelf,
       "nokiaSARO2AShelf": nokiaSARO2AShelf,
       "nokiaSARO2BShelf": nokiaSARO2BShelf,
       "nokiaSARO2CShelf": nokiaSARO2CShelf,
       "nokiaSARO2DShelf": nokiaSARO2DShelf,
       "nokiaSARO2EShelf": nokiaSARO2EShelf,
       "nokiaSARO2FShelf": nokiaSARO2FShelf,
       "nokiaSARO2GShelf": nokiaSARO2GShelf,
       "nokiaSARO2HShelf": nokiaSARO2HShelf,
       "nokiaSARO4AShelf": nokiaSARO4AShelf,
       "nokiaSARO4BShelf": nokiaSARO4BShelf,
       "nokiaSARO4CShelf": nokiaSARO4CShelf,
       "nokiaSARO4DShelf": nokiaSARO4DShelf,
       "nokiaSARO8AShelf": nokiaSARO8AShelf,
       "nokiaSARO8BShelf": nokiaSARO8BShelf,
       "nokiaLR4BOCShelf": nokiaLR4BOCShelf,
       "nokiaTPS24Shelf": nokiaTPS24Shelf,
       "nokiaTPS12Shelf": nokiaTPS12Shelf,
       "nokiaDmCt05LmShelf": nokiaDmCt05LmShelf,
       "nokiaDmCt10LmShelf": nokiaDmCt10LmShelf,
       "nokiaDmIt05LmShelf": nokiaDmIt05LmShelf,
       "nokiaDmIt10LmShelf": nokiaDmIt10LmShelf,
       "aluWdmPSIMXUniversalShelf": aluWdmPSIMXUniversalShelf,
       "aluWdmMlfsbShelf": aluWdmMlfsbShelf,
       "nokiaSfd5AShelf": nokiaSfd5AShelf,
       "nokiaSfd5BShelf": nokiaSfd5BShelf,
       "nokiaSfd5CShelf": nokiaSfd5CShelf,
       "nokiaSfd5DShelf": nokiaSfd5DShelf,
       "nokiaSfd5ADShelf": nokiaSfd5ADShelf,
       "nokiaSfd5BDShelf": nokiaSfd5BDShelf,
       "nokiaSfd5CDShelf": nokiaSfd5CDShelf,
       "nokiaSfd5DDShelf": nokiaSfd5DDShelf,
       "nokiaSfd5AUShelf": nokiaSfd5AUShelf,
       "nokiaSfd5BUShelf": nokiaSfd5BUShelf,
       "nokiaSfd5CUShelf": nokiaSfd5CUShelf,
       "nokiaSfd5DUShelf": nokiaSfd5DUShelf,
       "nokiaDcm2pShelf": nokiaDcm2pShelf,
       "nokiaSAS24Shelf": nokiaSAS24Shelf,
       "nokiaMsh8aShelf": nokiaMsh8aShelf,
       "nokiaSfd48Shelf": nokiaSfd48Shelf,
       "nokiaSfd64Shelf": nokiaSfd64Shelf,
       "tropicCardReg": tropicCardReg,
       "tropicMiscCardReg": tropicMiscCardReg,
       "tropicEmptyCard": tropicEmptyCard,
       "tropicUnknownCard": tropicUnknownCard,
       "tropicInvalidCard": tropicInvalidCard,
       "tropicReservedCard": tropicReservedCard,
       "tropicHalfHeightCarrierCard": tropicHalfHeightCarrierCard,
       "aluWdmVirtualCard": aluWdmVirtualCard,
       "aluWdmGmreCard": aluWdmGmreCard,
       "aluWdmMsh8fsmCard": aluWdmMsh8fsmCard,
       "aluWdmIroadmvCard": aluWdmIroadmvCard,
       "aluWdmIroadmfCard": aluWdmIroadmfCard,
       "aluWdmIroadm9mCard": aluWdmIroadm9mCard,
       "aluWdmIroadm9rCard": aluWdmIroadm9rCard,
       "aluWdmIroadm20Card": aluWdmIroadm20Card,
       "aluWdmSplit2Card": aluWdmSplit2Card,
       "aluWdmOscCplrCard": aluWdmOscCplrCard,
       "aluWdmMsh4fsbCard": aluWdmMsh4fsbCard,
       "aluWdmIpreampCard": aluWdmIpreampCard,
       "nokiaSfd2ACard": nokiaSfd2ACard,
       "nokiaSfd2BCard": nokiaSfd2BCard,
       "nokiaSfd2CCard": nokiaSfd2CCard,
       "nokiaSfd2DCard": nokiaSfd2DCard,
       "nokiaSfd2ECard": nokiaSfd2ECard,
       "nokiaSfd2FCard": nokiaSfd2FCard,
       "nokiaSfd2GCard": nokiaSfd2GCard,
       "nokiaSfd2HCard": nokiaSfd2HCard,
       "nokiaSfd2ICard": nokiaSfd2ICard,
       "nokiaSfd2LCard": nokiaSfd2LCard,
       "nokiaSfd2MCard": nokiaSfd2MCard,
       "nokiaSfd2NCard": nokiaSfd2NCard,
       "nokiaSfd2OCard": nokiaSfd2OCard,
       "nokiaSfd2PCard": nokiaSfd2PCard,
       "nokiaSfd2QCard": nokiaSfd2QCard,
       "nokiaSfd2RCard": nokiaSfd2RCard,
       "nokiaSfd4ACard": nokiaSfd4ACard,
       "nokiaSfd4BCard": nokiaSfd4BCard,
       "nokiaSfd4CCard": nokiaSfd4CCard,
       "nokiaSfd4DCard": nokiaSfd4DCard,
       "nokiaSfd4ECard": nokiaSfd4ECard,
       "nokiaSfd4FCard": nokiaSfd4FCard,
       "nokiaSfd4GCard": nokiaSfd4GCard,
       "nokiaSfd4HCard": nokiaSfd4HCard,
       "nokiaSfd8ACard": nokiaSfd8ACard,
       "nokiaSfd8BCard": nokiaSfd8BCard,
       "nokiaSfd8CCard": nokiaSfd8CCard,
       "nokiaSfd8DCard": nokiaSfd8DCard,
       "nokiaSfc1ACard": nokiaSfc1ACard,
       "nokiaSfc1BCard": nokiaSfc1BCard,
       "nokiaSfc1CCard": nokiaSfc1CCard,
       "nokiaSfc1DCard": nokiaSfc1DCard,
       "nokiaSfc1ECard": nokiaSfc1ECard,
       "nokiaSfc1FCard": nokiaSfc1FCard,
       "nokiaSfc1GCard": nokiaSfc1GCard,
       "nokiaSfc1HCard": nokiaSfc1HCard,
       "nokiaSfc2ABCard": nokiaSfc2ABCard,
       "nokiaSfc2CDCard": nokiaSfc2CDCard,
       "nokiaSfc2EFCard": nokiaSfc2EFCard,
       "nokiaSfc2GHCard": nokiaSfc2GHCard,
       "nokiaSfc4ADCard": nokiaSfc4ADCard,
       "nokiaSfc4EHCard": nokiaSfc4EHCard,
       "nokiaSfc8UCard": nokiaSfc8UCard,
       "nokiaSfc8LCard": nokiaSfc8LCard,
       "nokiaSARO2ACard": nokiaSARO2ACard,
       "nokiaSARO2BCard": nokiaSARO2BCard,
       "nokiaSARO2CCard": nokiaSARO2CCard,
       "nokiaSARO2DCard": nokiaSARO2DCard,
       "nokiaSARO2ECard": nokiaSARO2ECard,
       "nokiaSARO2FCard": nokiaSARO2FCard,
       "nokiaSARO2GCard": nokiaSARO2GCard,
       "nokiaSARO2HCard": nokiaSARO2HCard,
       "nokiaSARO4ACard": nokiaSARO4ACard,
       "nokiaSARO4BCard": nokiaSARO4BCard,
       "nokiaSARO4CCard": nokiaSARO4CCard,
       "nokiaSARO4DCard": nokiaSARO4DCard,
       "nokiaSARO8ACard": nokiaSARO8ACard,
       "nokiaSARO8BCard": nokiaSARO8BCard,
       "nokiaLR4BOCCard": nokiaLR4BOCCard,
       "aluWdmIrdm32Card": aluWdmIrdm32Card,
       "aluWdmOpenIrdm32Card": aluWdmOpenIrdm32Card,
       "aluWdmIrdm32lCard": aluWdmIrdm32lCard,
       "aluWdmOpenIrdm32LCard": aluWdmOpenIrdm32LCard,
       "aluWdmOpenEilaCard": aluWdmOpenEilaCard,
       "aluWdmEsreCard": aluWdmEsreCard,
       "aluWdmOmdclCard": aluWdmOmdclCard,
       "aluWdmOpenOmdclCard": aluWdmOpenOmdclCard,
       "aluWdmEilaLCard": aluWdmEilaLCard,
       "aluWdmOpenEilaLCard": aluWdmOpenEilaLCard,
       "aluWdmMlfsbCard": aluWdmMlfsbCard,
       "nokiaIr9Card": nokiaIr9Card,
       "nokiaTic48TCard": nokiaTic48TCard,
       "nokiaMsh8aCard": nokiaMsh8aCard,
       "nokiaIr4Card": nokiaIr4Card,
       "nokiaIr32AWCard": nokiaIr32AWCard,
       "nokiaOpenIr32AWCard": nokiaOpenIr32AWCard,
       "nokiaEilaAWCard": nokiaEilaAWCard,
       "nokiaOpenEilaAWCard": nokiaOpenEilaAWCard,
       "tropicControlCardReg": tropicControlCardReg,
       "tropicMasterControlCard": tropicMasterControlCard,
       "aluWdmEquipmentControllerCard": aluWdmEquipmentControllerCard,
       "aluWdmFirstLevelControllerCard": aluWdmFirstLevelControllerCard,
       "aluWdmMatrix3T8Card": aluWdmMatrix3T8Card,
       "aluWdmMatrix1T9Card": aluWdmMatrix1T9Card,
       "aluWdmPSS4EquipmentControllerCard": aluWdmPSS4EquipmentControllerCard,
       "aluWdmMatrix0CompactCard": aluWdmMatrix0CompactCard,
       "aluWdmUniversalMatrixFirstLevelControllerCard": aluWdmUniversalMatrixFirstLevelControllerCard,
       "aluWdmEndOfShelfMiddleCard": aluWdmEndOfShelfMiddleCard,
       "aluWdmUniversalMatrixFirstLevelController1p2TCard": aluWdmUniversalMatrixFirstLevelController1p2TCard,
       "aluWdmPSS8EquipmentController2Card": aluWdmPSS8EquipmentController2Card,
       "aluWdmPSS32EquipmentController2Card": aluWdmPSS32EquipmentController2Card,
       "aluWdmClockControllerCard96Card": aluWdmClockControllerCard96Card,
       "aluWdmVwmCwEquipmentControllerCard": aluWdmVwmCwEquipmentControllerCard,
       "aluWdmVwmDwEquipmentControllerCard": aluWdmVwmDwEquipmentControllerCard,
       "aluWdmPSS8EquipmentController2EncryptionCard": aluWdmPSS8EquipmentController2EncryptionCard,
       "aluWdmPSS32EquipmentController2EncryptionCard": aluWdmPSS32EquipmentController2EncryptionCard,
       "aluWdmPSIEquipmentController2Card": aluWdmPSIEquipmentController2Card,
       "aluWdmPSS8xClockEquipmentController2Card": aluWdmPSS8xClockEquipmentController2Card,
       "nokiaVwmMsOsu20Card": nokiaVwmMsOsu20Card,
       "nokiaVwmMsTlu9Card": nokiaVwmMsTlu9Card,
       "nokiaVwmMsPmu9UcCard": nokiaVwmMsPmu9UcCard,
       "nokiaVwmMsPmu9LcCard": nokiaVwmMsPmu9LcCard,
       "nokiaVwmMsPmu9UcmCard": nokiaVwmMsPmu9UcmCard,
       "nokiaVwmMsPmu9LcmCard": nokiaVwmMsPmu9LcmCard,
       "nokiaVwmMsItp4UcaCard": nokiaVwmMsItp4UcaCard,
       "nokiaVwmMsItp4UcbCard": nokiaVwmMsItp4UcbCard,
       "nokiaVwmMsItp4LcaCard": nokiaVwmMsItp4LcaCard,
       "nokiaVwmMsItp4LcbCard": nokiaVwmMsItp4LcbCard,
       "nokiaVwmMsSmmAoCard": nokiaVwmMsSmmAoCard,
       "nokiaVwmMsSmmAiCard": nokiaVwmMsSmmAiCard,
       "nokiaVwmMsOpsEmuCard": nokiaVwmMsOpsEmuCard,
       "nokiaPsdCard": nokiaPsdCard,
       "nokiaVwmMsTlu9mCard": nokiaVwmMsTlu9mCard,
       "aluWdmMiniEquipmentController2Card": aluWdmMiniEquipmentController2Card,
       "aluWdmPSS12xClockEquipmentController2Card": aluWdmPSS12xClockEquipmentController2Card,
       "nokiaVwmMsPmuD21ACard": nokiaVwmMsPmuD21ACard,
       "nokiaVwmMsPmuD21BCard": nokiaVwmMsPmuD21BCard,
       "nokiaVwmMsPmuD21CCard": nokiaVwmMsPmuD21CCard,
       "nokiaVwmMsPmuD21DCard": nokiaVwmMsPmuD21DCard,
       "nokiaVwmMsTlu200Card": nokiaVwmMsTlu200Card,
       "nokiaVwmMsADVGICard": nokiaVwmMsADVGICard,
       "aluWdmMini32GEquipmentController2Card": aluWdmMini32GEquipmentController2Card,
       "nokiaTPS24EquipmentControllerCard": nokiaTPS24EquipmentControllerCard,
       "nokiaTPS12EquipmentControllerCard": nokiaTPS12EquipmentControllerCard,
       "nokiaSAS24EquipmentControllerCard": nokiaSAS24EquipmentControllerCard,
       "nokiaEquipmentController3Card": nokiaEquipmentController3Card,
       "tropicOpticalSwitchCardReg": tropicOpticalSwitchCardReg,
       "tropicPhotonicProtectionSwitchCard": tropicPhotonicProtectionSwitchCard,
       "aluWdmOpsaCard": aluWdmOpsaCard,
       "aluWdmOpsbCard": aluWdmOpsbCard,
       "aluWdmMcs8x16Card": aluWdmMcs8x16Card,
       "aluWdmSwitchingCard": aluWdmSwitchingCard,
       "aluWdm12p120Card": aluWdm12p120Card,
       "aluWdm20p200Card": aluWdm20p200Card,
       "aluWdm1ud200Card": aluWdm1ud200Card,
       "aluWdmSwitching1T6Card": aluWdmSwitching1T6Card,
       "aluWdmMcs8x16lCard": aluWdmMcs8x16lCard,
       "nokiaVwmMsOpsOsmCard": nokiaVwmMsOpsOsmCard,
       "aluWdmSwitching4T8Card": aluWdmSwitching4T8Card,
       "aluWdmOpsflexCard": aluWdmOpsflexCard,
       "aluWdmSwitchingXST4T8Card": aluWdmSwitchingXST4T8Card,
       "nokiaVwmMsOpsOsmDsvCard": nokiaVwmMsOpsOsmDsvCard,
       "aluWdmOpsb5Card": aluWdmOpsb5Card,
       "aluWdmMcs16x15Card": aluWdmMcs16x15Card,
       "aluWdmSwitching24TCard": aluWdmSwitching24TCard,
       "aluWdmMcs16x15LCard": aluWdmMcs16x15LCard,
       "aluWdm12p120sCard": aluWdm12p120sCard,
       "nokia16p200Card": nokia16p200Card,
       "nokiaSwitchingXST4TCard": nokiaSwitchingXST4TCard,
       "nokiaSwitchingXST12TCard": nokiaSwitchingXST12TCard,
       "nokiaMxn824Card": nokiaMxn824Card,
       "nokiaSwitching48TCard": nokiaSwitching48TCard,
       "nokiaOpsumCard": nokiaOpsumCard,
       "nokiaMxn1624Card": nokiaMxn1624Card,
       "nokiaOpsumlCard": nokiaOpsumlCard,
       "tropicDWDMFilterCardReg": tropicDWDMFilterCardReg,
       "aluWdmCwr8Card": aluWdmCwr8Card,
       "aluWdmSfd44Card": aluWdmSfd44Card,
       "aluWdmSVACCard": aluWdmSVACCard,
       "aluWdmCwr8c88Card": aluWdmCwr8c88Card,
       "aluWdmSfd44bCard": aluWdmSfd44bCard,
       "aluWdmItlbCard": aluWdmItlbCard,
       "aluWdmSfd40Card": aluWdmSfd40Card,
       "aluWdmSfd40bCard": aluWdmSfd40bCard,
       "aluWdmWr2c88Card": aluWdmWr2c88Card,
       "aluWdmMVACCard": aluWdmMVACCard,
       "aluWdmItluCard": aluWdmItluCard,
       "aluWdmWr8c88aCard": aluWdmWr8c88aCard,
       "aluWdmMesh4Card": aluWdmMesh4Card,
       "aluWdmMVAC8BCard": aluWdmMVAC8BCard,
       "aluWdmWr8c88afCard": aluWdmWr8c88afCard,
       "aluWdmPsc1x6Card": aluWdmPsc1x6Card,
       "aluWdmWr20tfCard": aluWdmWr20tfCard,
       "aluWdmWr20tfmCard": aluWdmWr20tfmCard,
       "aluWdmWr20tfmlCard": aluWdmWr20tfmlCard,
       "aluWdmSfd96Card": aluWdmSfd96Card,
       "nokiaSfd10ALmCard": nokiaSfd10ALmCard,
       "nokiaSfd10BLmCard": nokiaSfd10BLmCard,
       "nokiaSfd10CLmCard": nokiaSfd10CLmCard,
       "nokiaSfd10DLmCard": nokiaSfd10DLmCard,
       "nokiaSfd48Card": nokiaSfd48Card,
       "nokiaSfd64Card": nokiaSfd64Card,
       "tropicAmplifierCardReg": tropicAmplifierCardReg,
       "aluWdmAhphgCard": aluWdmAhphgCard,
       "aluWdmAlphgCard": aluWdmAlphgCard,
       "aluWdmAhplgCard": aluWdmAhplgCard,
       "aluWdmAlpfgkCard": aluWdmAlpfgkCard,
       "aluWdmOscCard": aluWdmOscCard,
       "aluWdmA2325aCard": aluWdmA2325aCard,
       "aluWdmAlpfgtCard": aluWdmAlpfgtCard,
       "aluWdmOsctCard": aluWdmOsctCard,
       "aluWdmWtocmCard": aluWdmWtocmCard,
       "aluWdmAm2017bCard": aluWdmAm2017bCard,
       "aluWdmAm2325bCard": aluWdmAm2325bCard,
       "aluWdmRa2pCard": aluWdmRa2pCard,
       "aluWdmAm2318aCard": aluWdmAm2318aCard,
       "aluWdmAm2125aCard": aluWdmAm2125aCard,
       "aluWdmAm2125bCard": aluWdmAm2125bCard,
       "aluWdmWtocmaCard": aluWdmWtocmaCard,
       "aluWdmA2p2125Card": aluWdmA2p2125Card,
       "aluWdmAm2625aCard": aluWdmAm2625aCard,
       "aluWdmAm2032aCard": aluWdmAm2032aCard,
       "aluWdmAa2donwCard": aluWdmAa2donwCard,
       "aluWdmWtocmfCard": aluWdmWtocmfCard,
       "aluWdmAswgCard": aluWdmAswgCard,
       "aluWdmA4pswgCard": aluWdmA4pswgCard,
       "aluWdmOtdrCard": aluWdmOtdrCard,
       "aluWdmAar8aCard": aluWdmAar8aCard,
       "aluWdmMonOtdrCard": aluWdmMonOtdrCard,
       "aluWdmAwbegrCard": aluWdmAwbegrCard,
       "aluWdmAwbingCard": aluWdmAwbingCard,
       "aluWdmAwbilaCard": aluWdmAwbilaCard,
       "aluWdmRa5pCard": aluWdmRa5pCard,
       "aluWdmAa2donwBCard": aluWdmAa2donwBCard,
       "aluWdmOsctaprCard": aluWdmOsctaprCard,
       "aluWdmAar2x8aCard": aluWdmAar2x8aCard,
       "aluWdmAar2x8alCard": aluWdmAar2x8alCard,
       "aluWdmWtocmflCard": aluWdmWtocmflCard,
       "aluWdmOtdrwbCard": aluWdmOtdrwbCard,
       "aluWdmRa2p96Card": aluWdmRa2p96Card,
       "aluWdmOtdrmCard": aluWdmOtdrmCard,
       "aluWdmOAUnidirCard": aluWdmOAUnidirCard,
       "aluWdmAswglCard": aluWdmAswglCard,
       "aluWdmRa4pCard": aluWdmRa4pCard,
       "aluWdmEilaCard": aluWdmEilaCard,
       "aluWdmRa5pbCard": aluWdmRa5pbCard,
       "aluWdmAsgCard": aluWdmAsgCard,
       "nokiaAsc4Card": nokiaAsc4Card,
       "nokiaAsc2Card": nokiaAsc2Card,
       "tropicDispersionCompCardReg": tropicDispersionCompCardReg,
       "aluWdmDcmCard": aluWdmDcmCard,
       "nokiaDmCt05LmCard": nokiaDmCt05LmCard,
       "nokiaDmCt10LmCard": nokiaDmCt10LmCard,
       "nokiaDmIt05LmCard": nokiaDmIt05LmCard,
       "nokiaDmIt10LmCard": nokiaDmIt10LmCard,
       "aluWdmOpticalTransponderCardReg": aluWdmOpticalTransponderCardReg,
       "aluWdm11star1Card": aluWdm11star1Card,
       "aluWdm11stge12Card": aluWdm11stge12Card,
       "aluWdm11dpge12Card": aluWdm11dpge12Card,
       "aluWdm11stmm10Card": aluWdm11stmm10Card,
       "aluWdm4dpa4Card": aluWdm4dpa4Card,
       "aluWdm43stx4Card": aluWdm43stx4Card,
       "aluWdm4dpa2Card": aluWdm4dpa2Card,
       "aluWdm43sta1pCard": aluWdm43sta1pCard,
       "aluWdm43stx4pCard": aluWdm43stx4pCard,
       "aluWdm11qpa4Card": aluWdm11qpa4Card,
       "aluWdm112scx10Card": aluWdm112scx10Card,
       "aluWdm112sca1Card": aluWdm112sca1Card,
       "aluWdm1dpp21Card": aluWdm1dpp21Card,
       "aluWdm43scx4Card": aluWdm43scx4Card,
       "aluWdm11dpe12eCard": aluWdm11dpe12eCard,
       "aluWdm112sx10lCard": aluWdm112sx10lCard,
       "aluWdm112sa1lCard": aluWdm112sa1lCard,
       "aluWdm11dpm12Card": aluWdm11dpm12Card,
       "aluWdm43sca1Card": aluWdm43sca1Card,
       "aluWdm43scx4lCard": aluWdm43scx4lCard,
       "aluWdm112snx10Card": aluWdm112snx10Card,
       "aluWdm112sna1Card": aluWdm112sna1Card,
       "aluWdm1dpp24mCard": aluWdm1dpp24mCard,
       "aluWdmul43scupCard": aluWdmul43scupCard,
       "aluWdmul11qcupCard": aluWdmul11qcupCard,
       "aluWdm11qpen4Card": aluWdm11qpen4Card,
       "aluWdm43scx4eCard": aluWdm43scx4eCard,
       "aluWdm43scge1Card": aluWdm43scge1Card,
       "aluWdm11qpe24Card": aluWdm11qpe24Card,
       "aluWdm11star1aCard": aluWdm11star1aCard,
       "aluWdmcl10an10gCard": aluWdmcl10an10gCard,
       "aluWdmcl24anmCard": aluWdmcl24anmCard,
       "aluWdm11dpe12aCard": aluWdm11dpe12aCard,
       "aluWdmul130scupCard": aluWdmul130scupCard,
       "aluWdm130scx10Card": aluWdm130scx10Card,
       "aluWdm4qpa8Card": aluWdm4qpa8Card,
       "aluWdmOt112pdm11Card": aluWdmOt112pdm11Card,
       "aluWdmPtpctlCard": aluWdmPtpctlCard,
       "aluWdmPtpioCard": aluWdmPtpioCard,
       "aluWdmIo24et1gbCard": aluWdmIo24et1gbCard,
       "aluWdmIo4an10gCard": aluWdmIo4an10gCard,
       "aluWdmIo8et1gbCard": aluWdmIo8et1gbCard,
       "aluWdmIo10et10gCard": aluWdmIo10et10gCard,
       "aluWdmUl11qcupcCard": aluWdmUl11qcupcCard,
       "aluWdmOt520scx4Card": aluWdmOt520scx4Card,
       "aluWdm11ope8Card": aluWdm11ope8Card,
       "aluWdm11qce12xCard": aluWdm11qce12xCard,
       "aluWdmOt260scx2Card": aluWdmOt260scx2Card,
       "aluWdmOt130snx10Card": aluWdmOt130snx10Card,
       "aluWdmIo24anmbCard": aluWdmIo24anmbCard,
       "aluWdmOt11dpm8Card": aluWdmOt11dpm8Card,
       "aluWdmOt11dpm4mCard": aluWdmOt11dpm4mCard,
       "aluWdmOt11dpm4eCard": aluWdmOt11dpm4eCard,
       "aluWdmUl130scupbCard": aluWdmUl130scupbCard,
       "aluWdmOt112sdx11Card": aluWdmOt112sdx11Card,
       "aluWdmOt130sca1Card": aluWdmOt130sca1Card,
       "aluWdmIo10an10gbCard": aluWdmIo10an10gbCard,
       "aluWdmIo10et10gbCard": aluWdmIo10et10gbCard,
       "aluWdmIo4an100gCard": aluWdmIo4an100gCard,
       "aluWdmIo30an10gCard": aluWdmIo30an10gCard,
       "aluWdmIo30an300Card": aluWdmIo30an300Card,
       "aluWdmIo4an400Card": aluWdmIo4an400Card,
       "aluWdmOt130snq10Card": aluWdmOt130snq10Card,
       "aluWdmUl2uc400Card": aluWdmUl2uc400Card,
       "aluWdmUl4uc400Card": aluWdmUl4uc400Card,
       "aluWdmUl20uc200Card": aluWdmUl20uc200Card,
       "aluWdmD5x500Card": aluWdmD5x500Card,
       "aluWdmOtS11M100Card": aluWdmOtS11M100Card,
       "aluWdm12ce120Card": aluWdm12ce120Card,
       "aluWdm1ce100Card": aluWdm1ce100Card,
       "aluWdmLcI1000Card": aluWdmLcI1000Card,
       "aluWdmS13x100Card": aluWdmS13x100Card,
       "aluWdm12ce121Card": aluWdm12ce121Card,
       "aluWdmPtpioctlCard": aluWdmPtpioctlCard,
       "aluWdm11qpa4BCard": aluWdm11qpa4BCard,
       "aluWdm1ux100Card": aluWdm1ux100Card,
       "aluWdm20ax200Card": aluWdm20ax200Card,
       "aluWdm20mx80Card": aluWdm20mx80Card,
       "aluWdmS13x100eCard": aluWdmS13x100eCard,
       "aluWdmLcI2000Card": aluWdmLcI2000Card,
       "aluWdm30se300Card": aluWdm30se300Card,
       "aluWdm6se300Card": aluWdm6se300Card,
       "aluWdmD5x500lCard": aluWdmD5x500lCard,
       "aluWdmLcI2000lCard": aluWdmLcI2000lCard,
       "aluWdm20an80Card": aluWdm20an80Card,
       "aluWdm10an400Card": aluWdm10an400Card,
       "aluWdm8p20Card": aluWdm8p20Card,
       "aluWdmD5x500qCard": aluWdmD5x500qCard,
       "aluWdm18p40Card": aluWdm18p40Card,
       "aluWdmDa2c4Card": aluWdmDa2c4Card,
       "aluWdm130sla1Card": aluWdm130sla1Card,
       "aluWdm130slx10Card": aluWdm130slx10Card,
       "aluWdmBmuPCard": aluWdmBmuPCard,
       "aluWdmS2ad200Card": aluWdmS2ad200Card,
       "aluWdm2ux200Card": aluWdm2ux200Card,
       "aluWdm4mx200Card": aluWdm4mx200Card,
       "aluWdm10an1tCard": aluWdm10an1tCard,
       "aluWdm8uc1tCard": aluWdm8uc1tCard,
       "aluWdmDfc12Card": aluWdmDfc12Card,
       "nokiaT24PS1Card": nokiaT24PS1Card,
       "nokiaT12PSCard": nokiaT12PSCard,
       "aluWdmS4x400Card": aluWdmS4x400Card,
       "nokiaT24PS2Card": nokiaT24PS2Card,
       "aluWdmGenericOtCard": aluWdmGenericOtCard,
       "aluWdm1ety100Card": aluWdm1ety100Card,
       "aluWdm18P400Card": aluWdm18P400Card,
       "aluWdm4uc1tCard": aluWdm4uc1tCard,
       "nokia5mx500Card": nokia5mx500Card,
       "nokia2ux500Card": nokia2ux500Card,
       "nokiaS24PS1Card": nokiaS24PS1Card,
       "nokiaS24PS2Card": nokiaS24PS2Card,
       "nokia18ce300Card": nokia18ce300Card,
       "aluWdmStaticFilterCardReg": aluWdmStaticFilterCardReg,
       "aluWdmSFD5ACard": aluWdmSFD5ACard,
       "aluWdmSFD5BCard": aluWdmSFD5BCard,
       "aluWdmSFD5CCard": aluWdmSFD5CCard,
       "aluWdmSFD5DCard": aluWdmSFD5DCard,
       "aluWdmSFD5ECard": aluWdmSFD5ECard,
       "aluWdmSFD5FCard": aluWdmSFD5FCard,
       "aluWdmSFD5GCard": aluWdmSFD5GCard,
       "aluWdmSFD5HCard": aluWdmSFD5HCard,
       "aluWdmSFD10ACard": aluWdmSFD10ACard,
       "aluWdmSFD10BCard": aluWdmSFD10BCard,
       "aluWdmSFD10CCard": aluWdmSFD10CCard,
       "aluWdmSFD10DCard": aluWdmSFD10DCard,
       "aluWdmSFC2ACard": aluWdmSFC2ACard,
       "aluWdmSFC2BCard": aluWdmSFC2BCard,
       "aluWdmSFC2CCard": aluWdmSFC2CCard,
       "aluWdmSFC2DCard": aluWdmSFC2DCard,
       "aluWdmSFC4ACard": aluWdmSFC4ACard,
       "aluWdmSFC4BCard": aluWdmSFC4BCard,
       "aluWdmSFC8Card": aluWdmSFC8Card,
       "aluWdmSFC1ACard": aluWdmSFC1ACard,
       "aluWdmSFC1BCard": aluWdmSFC1BCard,
       "aluWdmSFC1CCard": aluWdmSFC1CCard,
       "aluWdmSFC1DCard": aluWdmSFC1DCard,
       "aluWdmSFC1ECard": aluWdmSFC1ECard,
       "aluWdmSFC1FCard": aluWdmSFC1FCard,
       "aluWdmSFC1GCard": aluWdmSFC1GCard,
       "aluWdmSFC1HCard": aluWdmSFC1HCard,
       "aluWdmSFD8ACard": aluWdmSFD8ACard,
       "aluWdmSFD8BCard": aluWdmSFD8BCard,
       "aluWdmSFD8CCard": aluWdmSFD8CCard,
       "aluWdmSFD8DCard": aluWdmSFD8DCard,
       "aluWdmSFD4ACard": aluWdmSFD4ACard,
       "aluWdmSFD4BCard": aluWdmSFD4BCard,
       "aluWdmSFD4CCard": aluWdmSFD4CCard,
       "aluWdmSFD4DCard": aluWdmSFD4DCard,
       "aluWdmSFD4ECard": aluWdmSFD4ECard,
       "aluWdmSFD4FCard": aluWdmSFD4FCard,
       "aluWdmSFD4GCard": aluWdmSFD4GCard,
       "aluWdmSFD4HCard": aluWdmSFD4HCard,
       "aluWdmSFD2ACard": aluWdmSFD2ACard,
       "aluWdmSFD2BCard": aluWdmSFD2BCard,
       "aluWdmSFD2CCard": aluWdmSFD2CCard,
       "aluWdmSFD2DCard": aluWdmSFD2DCard,
       "aluWdmSFD2ECard": aluWdmSFD2ECard,
       "aluWdmSFD2FCard": aluWdmSFD2FCard,
       "aluWdmSFD2GCard": aluWdmSFD2GCard,
       "aluWdmSFD2HCard": aluWdmSFD2HCard,
       "aluWdmSFD2ICard": aluWdmSFD2ICard,
       "aluWdmSFD2LCard": aluWdmSFD2LCard,
       "aluWdmSFD2MCard": aluWdmSFD2MCard,
       "aluWdmSFD2NCard": aluWdmSFD2NCard,
       "aluWdmSFD2OCard": aluWdmSFD2OCard,
       "aluWdmSFD2PCard": aluWdmSFD2PCard,
       "aluWdmSFD2QCard": aluWdmSFD2QCard,
       "aluWdmSFD2RCard": aluWdmSFD2RCard,
       "aluWdmVwmSFD8ACard": aluWdmVwmSFD8ACard,
       "aluWdmVwmSFD8BCard": aluWdmVwmSFD8BCard,
       "aluWdmVwmSFD8CCard": aluWdmVwmSFD8CCard,
       "aluWdmVwmSFD8DCard": aluWdmVwmSFD8DCard,
       "aluWdmVwmSFC8Card": aluWdmVwmSFC8Card,
       "aluWdmMonOcmCard": aluWdmMonOcmCard,
       "aluWdmSfdc8ACard": aluWdmSfdc8ACard,
       "aluWdmSfdc8BCard": aluWdmSfdc8BCard,
       "aluWdmSfdc8CCard": aluWdmSfdc8CCard,
       "aluWdmSfdc8DCard": aluWdmSfdc8DCard,
       "aluWdmSfdc8ECard": aluWdmSfdc8ECard,
       "nokiaSfd5ADCard": nokiaSfd5ADCard,
       "nokiaSfd5BDCard": nokiaSfd5BDCard,
       "nokiaSfd5CDCard": nokiaSfd5CDCard,
       "nokiaSfd5DDCard": nokiaSfd5DDCard,
       "nokiaSfd5AUCard": nokiaSfd5AUCard,
       "nokiaSfd5BUCard": nokiaSfd5BUCard,
       "nokiaSfd5CUCard": nokiaSfd5CUCard,
       "nokiaSfd5DUCard": nokiaSfd5DUCard,
       "nokiaDcm2pCard": nokiaDcm2pCard,
       "tropicCommonEquipmentReg": tropicCommonEquipmentReg,
       "aluWdmPowerFilterCard": aluWdmPowerFilterCard,
       "aluWdmFanUnitCard": aluWdmFanUnitCard,
       "aluWdmUserInterfacePanelCard": aluWdmUserInterfacePanelCard,
       "aluWdmBusTerminationCard": aluWdmBusTerminationCard,
       "aluWdmBusTerminationOnlyCard": aluWdmBusTerminationOnlyCard,
       "aluWdmPSS8ShelfPanelCard": aluWdmPSS8ShelfPanelCard,
       "aluWdmPSS8UserInterfacePanelCard": aluWdmPSS8UserInterfacePanelCard,
       "aluWdmMultiFunctionCard": aluWdmMultiFunctionCard,
       "aluWdmPSS8PowerFilterAcCard": aluWdmPSS8PowerFilterAcCard,
       "aluWdmPSS96PowerFilterCard": aluWdmPSS96PowerFilterCard,
       "aluWdmPSS8xMultiFunctionCard": aluWdmPSS8xMultiFunctionCard,
       "aluWdmPSS8xPowerFilterCard": aluWdmPSS8xPowerFilterCard,
       "nokiaVwmMsFanTOCard": nokiaVwmMsFanTOCard,
       "nokiaVwmMsOpsPsuCard": nokiaVwmMsOpsPsuCard,
       "aluWdmPSS8PowerFilterWithFCRUCard": aluWdmPSS8PowerFilterWithFCRUCard,
       "aluWdmPSS16IIPowerFilterWithFCRUCard": aluWdmPSS16IIPowerFilterWithFCRUCard,
       "aluWdmPSS12xPowerFilterCard": aluWdmPSS12xPowerFilterCard,
       "aluWdmMultiFunctionPSIMCard": aluWdmMultiFunctionPSIMCard,
       "nokiaVwmMsFanDECard": nokiaVwmMsFanDECard,
       "aluWdmMultiFunctionPSILCard": aluWdmMultiFunctionPSILCard,
       "nokiaT24PFCard": nokiaT24PFCard,
       "nokiaT12PFCard": nokiaT12PFCard,
       "nokiaT24FUCard": nokiaT24FUCard,
       "nokiaVwmMsFanIICard": nokiaVwmMsFanIICard,
       "aluWdmMultiFunctionPSIMXCard": aluWdmMultiFunctionPSIMXCard,
       "nokiaS24PFCard": nokiaS24PFCard,
       "nokiaS24FUCard": nokiaS24FUCard,
       "tropicGeneric": tropicGeneric,
       "tnSystem": tnSystem,
       "tnSystemMIB": tnSystemMIB,
       "tnNotificationMIB": tnNotificationMIB,
       "tnLogMIB": tnLogMIB,
       "tnDiagnosticMIB": tnDiagnosticMIB,
       "tnSoftwareMIB": tnSoftwareMIB,
       "tnPowerMgmtMIB": tnPowerMgmtMIB,
       "tnUserMgmtMIB": tnUserMgmtMIB,
       "tnPhMNotificationMIB": tnPhMNotificationMIB,
       "tnAsonMIB": tnAsonMIB,
       "tnGmplsMIB": tnGmplsMIB,
       "tnGmplsObjs": tnGmplsObjs,
       "tnAbsNodeMIB": tnAbsNodeMIB,
       "tnAbsNodeObjs": tnAbsNodeObjs,
       "tnGenericNotificationMIB": tnGenericNotificationMIB,
       "tnGenericLogMIB": tnGenericLogMIB,
       "tnDhpMIB": tnDhpMIB,
       "tnDhpObjs": tnDhpObjs,
       "tnEquipment": tnEquipment,
       "tnShelf": tnShelf,
       "tnShelfMIB": tnShelfMIB,
       "tnSlot": tnSlot,
       "tnSlotMIB": tnSlotMIB,
       "tnCard": tnCard,
       "tnCardMIB": tnCardMIB,
       "tnWaveKeyMIB": tnWaveKeyMIB,
       "tnControlCardMIB": tnControlCardMIB,
       "tnEthernetCardMIB": tnEthernetCardMIB,
       "tnOpticalCardMIB": tnOpticalCardMIB,
       "tnSwitchCardMIB": tnSwitchCardMIB,
       "tnAmplifierMIB": tnAmplifierMIB,
       "tnPort": tnPort,
       "tnAccessPortMIB": tnAccessPortMIB,
       "tnEthernetPortMIB": tnEthernetPortMIB,
       "tnOpticalPortMIB": tnOpticalPortMIB,
       "tnSwitchPortMIB": tnSwitchPortMIB,
       "tnOchMIB": tnOchMIB,
       "tnVtsConnMIB": tnVtsConnMIB,
       "tnOtuOduMIB": tnOtuOduMIB,
       "tnSyncEMIB": tnSyncEMIB,
       "tnPtpMIB": tnPtpMIB,
       "tnOthMIB": tnOthMIB,
       "tnIEEE8023brMIB": tnIEEE8023brMIB,
       "tnRoeMib": tnRoeMib,
       "tnMiscEquipment": tnMiscEquipment,
       "tnFanMIB": tnFanMIB,
       "tnBreakerMIB": tnBreakerMIB,
       "tnAlarmPanelMIB": tnAlarmPanelMIB,
       "tnVwmMsMIB": tnVwmMsMIB,
       "tnPsdMIB": tnPsdMIB,
       "tnServices": tnServices,
       "tnL1ServiceMIB": tnL1ServiceMIB,
       "tnL2ServiceMIB": tnL2ServiceMIB,
       "tnStatistics": tnStatistics,
       "tnStatisticsMIB": tnStatisticsMIB,
       "tnProtocols": tnProtocols,
       "tnOspfMIB": tnOspfMIB,
       "tropicProducts": tropicProducts,
       "tropicExpr": tropicExpr,
       "tnExprOpticalCardMIB": tnExprOpticalCardMIB,
       "tnExprOpticalPortMIB": tnExprOpticalPortMIB,
       "tnExprScalarsMIB": tnExprScalarsMIB,
       "tnReg": tnReg,
       "tnModules": tnModules,
       "tnSRMIBModules": tnSRMIBModules,
       "tnRmdMIBModules": tnRmdMIBModules,
       "tnProducts": tnProducts,
       "tnSRMIB": tnSRMIB,
       "tnSRObjs": tnSRObjs,
       "tnSRNotifyPrefix": tnSRNotifyPrefix,
       "tnRmdMIB": tnRmdMIB,
       "tnRmdObjs": tnRmdObjs,
       "tnSASProducts": tnSASProducts,
       "tnServiceAccessSwitches": tnServiceAccessSwitches,
       "tnSASRegistry": tnSASRegistry,
       "tnSASModules": tnSASModules,
       "tnSASMIBModules": tnSASMIBModules,
       "tnSASMIB": tnSASMIB,
       "tnSASObjs": tnSASObjs}
)
