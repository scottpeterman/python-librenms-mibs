# SNMP MIB module (TROPIC-CARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TROPIC-CARD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:12:25 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnCardMIB,
 tnCardModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnCardMIB",
    "tnCardModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(AluWdmCardCapacity,
 AluWdmWtClkValues,
 TropicCardCLEI,
 TropicCardHFD,
 TropicCardManufacturingPartNumber,
 TropicCardMarketingPartNumber,
 TropicCardSWGenericLoadName,
 TropicCardSerialNumber,
 TropicLEDColorType,
 TropicLEDStateType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmCardCapacity",
    "AluWdmWtClkValues",
    "TropicCardCLEI",
    "TropicCardHFD",
    "TropicCardManufacturingPartNumber",
    "TropicCardMarketingPartNumber",
    "TropicCardSWGenericLoadName",
    "TropicCardSerialNumber",
    "TropicLEDColorType",
    "TropicLEDStateType")


# MODULE-IDENTITY

tnCardMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tnCardMibModule.setRevisions(
        ("2022-08-12 12:00",
         "2022-05-06 12:00",
         "2021-06-18 12:00",
         "2021-03-19 12:00",
         "2020-12-18 12:00",
         "2020-12-04 12:00",
         "2020-11-13 12:00",
         "2020-09-11 12:00",
         "2020-06-19 12:00",
         "2020-06-12 12:00",
         "2020-03-20 12:00",
         "2020-02-21 12:00",
         "2020-02-14 12:00",
         "2019-12-13 12:00",
         "2019-10-25 12:00",
         "2019-10-18 12:00",
         "2019-08-30 12:00",
         "2019-07-12 12:00",
         "2019-06-07 12:00",
         "2019-03-22 12:00",
         "2019-02-22 12:00",
         "2019-01-25 12:00",
         "2018-05-18 12:00",
         "2018-03-09 12:00",
         "2018-02-23 12:00",
         "2017-12-26 12:00",
         "2017-09-15 12:00",
         "2017-05-26 12:00",
         "2017-04-28 12:00",
         "2017-03-31 12:00",
         "2017-02-24 12:00",
         "2017-02-10 12:00",
         "2016-11-16 12:00",
         "2016-09-09 12:00",
         "2016-08-08 12:00",
         "2016-07-29 12:00",
         "2015-10-05 12:00",
         "2015-09-30 12:00",
         "2015-07-30 12:00",
         "2015-05-29 12:00",
         "2015-03-11 12:00",
         "2015-02-06 12:00",
         "2014-02-26 12:00",
         "2013-12-26 12:00",
         "2013-12-15 12:00",
         "2013-11-18 12:00",
         "2013-08-16 12:00",
         "2013-05-21 12:00",
         "2012-09-06 12:00",
         "2012-07-17 12:00",
         "2012-07-10 12:00",
         "2011-05-23 12:00",
         "2011-05-19 12:00",
         "2009-03-31 12:00",
         "2009-02-10 12:00",
         "2009-02-01 12:00",
         "2008-09-26 12:00",
         "2008-09-24 12:00",
         "2008-09-19 12:00",
         "2008-06-05 12:00",
         "2008-05-29 12:00",
         "2008-04-11 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NokiaOAMTestUnitType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("microseconds", 1),
          ("hundred-nano-seconds", 2),
          ("nano-seconds", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TnCardConf_ObjectIdentity = ObjectIdentity
tnCardConf = _TnCardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1)
)
_TnCardGroups_ObjectIdentity = ObjectIdentity
tnCardGroups = _TnCardGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1, 1)
)
_TnCardCompliances_ObjectIdentity = ObjectIdentity
tnCardCompliances = _TnCardCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1, 2)
)
_TnCardObjs_ObjectIdentity = ObjectIdentity
tnCardObjs = _TnCardObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2)
)
_TnCardBasics_ObjectIdentity = ObjectIdentity
tnCardBasics = _TnCardBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1)
)
_TnCardTotal_Type = Integer32
_TnCardTotal_Object = MibScalar
tnCardTotal = _TnCardTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 1),
    _TnCardTotal_Type()
)
tnCardTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardTotal.setStatus("current")
_TnCardTable_Object = MibTable
tnCardTable = _TnCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnCardTable.setStatus("current")
_TnCardEntry_Object = MibTableRow
tnCardEntry = _TnCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1)
)
tnCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnCardEntry.setStatus("current")


class _TnCardName_Type(SnmpAdminString):
    """Custom type tnCardName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnCardName_Type.__name__ = "SnmpAdminString"
_TnCardName_Object = MibTableColumn
tnCardName = _TnCardName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 1),
    _TnCardName_Type()
)
tnCardName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardName.setStatus("current")


class _TnCardDescr_Type(SnmpAdminString):
    """Custom type tnCardDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnCardDescr_Type.__name__ = "SnmpAdminString"
_TnCardDescr_Object = MibTableColumn
tnCardDescr = _TnCardDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 2),
    _TnCardDescr_Type()
)
tnCardDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardDescr.setStatus("current")


class _TnCardCLEI_Type(TropicCardCLEI):
    """Custom type tnCardCLEI based on TropicCardCLEI"""
    defaultValue = OctetString("")


_TnCardCLEI_Type.__name__ = "TropicCardCLEI"
_TnCardCLEI_Object = MibTableColumn
tnCardCLEI = _TnCardCLEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 3),
    _TnCardCLEI_Type()
)
tnCardCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardCLEI.setStatus("current")


class _TnCardHFD_Type(TropicCardHFD):
    """Custom type tnCardHFD based on TropicCardHFD"""
    defaultValue = OctetString("")


_TnCardHFD_Type.__name__ = "TropicCardHFD"
_TnCardHFD_Object = MibTableColumn
tnCardHFD = _TnCardHFD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 4),
    _TnCardHFD_Type()
)
tnCardHFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardHFD.setStatus("current")


class _TnCardSerialNumber_Type(TropicCardSerialNumber):
    """Custom type tnCardSerialNumber based on TropicCardSerialNumber"""
    defaultValue = OctetString("")


_TnCardSerialNumber_Type.__name__ = "TropicCardSerialNumber"
_TnCardSerialNumber_Object = MibTableColumn
tnCardSerialNumber = _TnCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 5),
    _TnCardSerialNumber_Type()
)
tnCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardSerialNumber.setStatus("current")


class _TnCardManufacturingPartNumber_Type(TropicCardManufacturingPartNumber):
    """Custom type tnCardManufacturingPartNumber based on TropicCardManufacturingPartNumber"""
    defaultValue = OctetString("")


_TnCardManufacturingPartNumber_Type.__name__ = "TropicCardManufacturingPartNumber"
_TnCardManufacturingPartNumber_Object = MibTableColumn
tnCardManufacturingPartNumber = _TnCardManufacturingPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 6),
    _TnCardManufacturingPartNumber_Type()
)
tnCardManufacturingPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardManufacturingPartNumber.setStatus("current")


class _TnCardMarketingPartNumber_Type(TropicCardMarketingPartNumber):
    """Custom type tnCardMarketingPartNumber based on TropicCardMarketingPartNumber"""
    defaultValue = OctetString("")


_TnCardMarketingPartNumber_Type.__name__ = "TropicCardMarketingPartNumber"
_TnCardMarketingPartNumber_Object = MibTableColumn
tnCardMarketingPartNumber = _TnCardMarketingPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 7),
    _TnCardMarketingPartNumber_Type()
)
tnCardMarketingPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardMarketingPartNumber.setStatus("current")


class _TnCardSWGenericLoadName_Type(TropicCardSWGenericLoadName):
    """Custom type tnCardSWGenericLoadName based on TropicCardSWGenericLoadName"""
    defaultValue = OctetString("")


_TnCardSWGenericLoadName_Type.__name__ = "TropicCardSWGenericLoadName"
_TnCardSWGenericLoadName_Object = MibTableColumn
tnCardSWGenericLoadName = _TnCardSWGenericLoadName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 8),
    _TnCardSWGenericLoadName_Type()
)
tnCardSWGenericLoadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardSWGenericLoadName.setStatus("current")


class _TnCardHeight_Type(Integer32):
    """Custom type tnCardHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("halfHeight", 2),
          ("fullHeight", 3),
          ("extendedHeight", 4))
    )


_TnCardHeight_Type.__name__ = "Integer32"
_TnCardHeight_Object = MibTableColumn
tnCardHeight = _TnCardHeight_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 10),
    _TnCardHeight_Type()
)
tnCardHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardHeight.setStatus("current")


class _TnCardWidth_Type(Integer32):
    """Custom type tnCardWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("singleWidth", 2),
          ("doubleWidth", 3),
          ("tripleWidth", 4))
    )


_TnCardWidth_Type.__name__ = "Integer32"
_TnCardWidth_Object = MibTableColumn
tnCardWidth = _TnCardWidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 11),
    _TnCardWidth_Type()
)
tnCardWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardWidth.setStatus("current")
_TnCardTemperature_Type = Integer32
_TnCardTemperature_Object = MibTableColumn
tnCardTemperature = _TnCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 13),
    _TnCardTemperature_Type()
)
tnCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardTemperature.setStatus("current")
if mibBuilder.loadTexts:
    tnCardTemperature.setUnits("Celsius")


class _TnCardHighTemperatureThresh_Type(Integer32):
    """Custom type tnCardHighTemperatureThresh based on Integer32"""
    defaultValue = 90


_TnCardHighTemperatureThresh_Type.__name__ = "Integer32"
_TnCardHighTemperatureThresh_Object = MibTableColumn
tnCardHighTemperatureThresh = _TnCardHighTemperatureThresh_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 14),
    _TnCardHighTemperatureThresh_Type()
)
tnCardHighTemperatureThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardHighTemperatureThresh.setStatus("current")
if mibBuilder.loadTexts:
    tnCardHighTemperatureThresh.setUnits("Celsius")


class _TnCardLowTemperatureThresh_Type(Integer32):
    """Custom type tnCardLowTemperatureThresh based on Integer32"""
    defaultValue = -5


_TnCardLowTemperatureThresh_Type.__name__ = "Integer32"
_TnCardLowTemperatureThresh_Object = MibTableColumn
tnCardLowTemperatureThresh = _TnCardLowTemperatureThresh_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 15),
    _TnCardLowTemperatureThresh_Type()
)
tnCardLowTemperatureThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardLowTemperatureThresh.setStatus("current")
if mibBuilder.loadTexts:
    tnCardLowTemperatureThresh.setUnits("Celsius")


class _TnCardTemperatureTolerance_Type(Unsigned32):
    """Custom type tnCardTemperatureTolerance based on Unsigned32"""
    defaultValue = 3


_TnCardTemperatureTolerance_Type.__name__ = "Unsigned32"
_TnCardTemperatureTolerance_Object = MibTableColumn
tnCardTemperatureTolerance = _TnCardTemperatureTolerance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 16),
    _TnCardTemperatureTolerance_Type()
)
tnCardTemperatureTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardTemperatureTolerance.setStatus("current")
if mibBuilder.loadTexts:
    tnCardTemperatureTolerance.setUnits("Celsius")
_TnCardStatusLEDColor_Type = TropicLEDColorType
_TnCardStatusLEDColor_Object = MibTableColumn
tnCardStatusLEDColor = _TnCardStatusLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 17),
    _TnCardStatusLEDColor_Type()
)
tnCardStatusLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardStatusLEDColor.setStatus("current")
_TnCardStatusLEDState_Type = TropicLEDStateType
_TnCardStatusLEDState_Object = MibTableColumn
tnCardStatusLEDState = _TnCardStatusLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 18),
    _TnCardStatusLEDState_Type()
)
tnCardStatusLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardStatusLEDState.setStatus("current")
_TnCardActivityLEDColor_Type = TropicLEDColorType
_TnCardActivityLEDColor_Object = MibTableColumn
tnCardActivityLEDColor = _TnCardActivityLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 19),
    _TnCardActivityLEDColor_Type()
)
tnCardActivityLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardActivityLEDColor.setStatus("current")
_TnCardActivityLEDState_Type = TropicLEDStateType
_TnCardActivityLEDState_Object = MibTableColumn
tnCardActivityLEDState = _TnCardActivityLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 20),
    _TnCardActivityLEDState_Type()
)
tnCardActivityLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardActivityLEDState.setStatus("current")


class _TnCardCompanyID_Type(SnmpAdminString):
    """Custom type tnCardCompanyID based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardCompanyID_Type.__name__ = "SnmpAdminString"
_TnCardCompanyID_Object = MibTableColumn
tnCardCompanyID = _TnCardCompanyID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 21),
    _TnCardCompanyID_Type()
)
tnCardCompanyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardCompanyID.setStatus("current")


class _TnCardMnemonic_Type(SnmpAdminString):
    """Custom type tnCardMnemonic based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardMnemonic_Type.__name__ = "SnmpAdminString"
_TnCardMnemonic_Object = MibTableColumn
tnCardMnemonic = _TnCardMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 22),
    _TnCardMnemonic_Type()
)
tnCardMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardMnemonic.setStatus("current")


class _TnCardSWPartNum_Type(SnmpAdminString):
    """Custom type tnCardSWPartNum based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardSWPartNum_Type.__name__ = "SnmpAdminString"
_TnCardSWPartNum_Object = MibTableColumn
tnCardSWPartNum = _TnCardSWPartNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 23),
    _TnCardSWPartNum_Type()
)
tnCardSWPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardSWPartNum.setStatus("current")


class _TnCardDate_Type(SnmpAdminString):
    """Custom type tnCardDate based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardDate_Type.__name__ = "SnmpAdminString"
_TnCardDate_Object = MibTableColumn
tnCardDate = _TnCardDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 24),
    _TnCardDate_Type()
)
tnCardDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardDate.setStatus("current")


class _TnCardExtraData_Type(SnmpAdminString):
    """Custom type tnCardExtraData based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardExtraData_Type.__name__ = "SnmpAdminString"
_TnCardExtraData_Object = MibTableColumn
tnCardExtraData = _TnCardExtraData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 25),
    _TnCardExtraData_Type()
)
tnCardExtraData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardExtraData.setStatus("current")
_TnCardAnyPortsInService_Type = TruthValue
_TnCardAnyPortsInService_Object = MibTableColumn
tnCardAnyPortsInService = _TnCardAnyPortsInService_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 27),
    _TnCardAnyPortsInService_Type()
)
tnCardAnyPortsInService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardAnyPortsInService.setStatus("current")


class _TnCardLastBootedFwBundleVer_Type(SnmpAdminString):
    """Custom type tnCardLastBootedFwBundleVer based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardLastBootedFwBundleVer_Type.__name__ = "SnmpAdminString"
_TnCardLastBootedFwBundleVer_Object = MibTableColumn
tnCardLastBootedFwBundleVer = _TnCardLastBootedFwBundleVer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 28),
    _TnCardLastBootedFwBundleVer_Type()
)
tnCardLastBootedFwBundleVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardLastBootedFwBundleVer.setStatus("current")


class _TnCardNextFwBundleVer_Type(SnmpAdminString):
    """Custom type tnCardNextFwBundleVer based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardNextFwBundleVer_Type.__name__ = "SnmpAdminString"
_TnCardNextFwBundleVer_Object = MibTableColumn
tnCardNextFwBundleVer = _TnCardNextFwBundleVer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 29),
    _TnCardNextFwBundleVer_Type()
)
tnCardNextFwBundleVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardNextFwBundleVer.setStatus("current")


class _TnCardFactoryID_Type(SnmpAdminString):
    """Custom type tnCardFactoryID based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardFactoryID_Type.__name__ = "SnmpAdminString"
_TnCardFactoryID_Object = MibTableColumn
tnCardFactoryID = _TnCardFactoryID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 30),
    _TnCardFactoryID_Type()
)
tnCardFactoryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardFactoryID.setStatus("current")


class _TnCardCapacity_Type(AluWdmCardCapacity):
    """Custom type tnCardCapacity based on AluWdmCardCapacity"""
    defaultValue = 1


_TnCardCapacity_Type.__name__ = "AluWdmCardCapacity"
_TnCardCapacity_Object = MibTableColumn
tnCardCapacity = _TnCardCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 31),
    _TnCardCapacity_Type()
)
tnCardCapacity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardCapacity.setStatus("current")


class _TnCardLACPSystemPriority_Type(Unsigned32):
    """Custom type tnCardLACPSystemPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnCardLACPSystemPriority_Type.__name__ = "Unsigned32"
_TnCardLACPSystemPriority_Object = MibTableColumn
tnCardLACPSystemPriority = _TnCardLACPSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 32),
    _TnCardLACPSystemPriority_Type()
)
tnCardLACPSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardLACPSystemPriority.setStatus("current")
_TnCardMaxPower_Type = Unsigned32
_TnCardMaxPower_Object = MibTableColumn
tnCardMaxPower = _TnCardMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 33),
    _TnCardMaxPower_Type()
)
tnCardMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    tnCardMaxPower.setUnits("milli-Watts")


class _TnCardEthOamCcmFaultMgntMode_Type(Integer32):
    """Custom type tnCardEthOamCcmFaultMgntMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee", 1),
          ("itu", 2))
    )


_TnCardEthOamCcmFaultMgntMode_Type.__name__ = "Integer32"
_TnCardEthOamCcmFaultMgntMode_Object = MibTableColumn
tnCardEthOamCcmFaultMgntMode = _TnCardEthOamCcmFaultMgntMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 34),
    _TnCardEthOamCcmFaultMgntMode_Type()
)
tnCardEthOamCcmFaultMgntMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardEthOamCcmFaultMgntMode.setStatus("current")


class _TnCardClkSwitch_Type(AluWdmWtClkValues):
    """Custom type tnCardClkSwitch based on AluWdmWtClkValues"""
    defaultValue = 1


_TnCardClkSwitch_Type.__name__ = "AluWdmWtClkValues"
_TnCardClkSwitch_Object = MibTableColumn
tnCardClkSwitch = _TnCardClkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 35),
    _TnCardClkSwitch_Type()
)
tnCardClkSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardClkSwitch.setStatus("current")
_TnCardRtrvClkSwitch_Type = AluWdmWtClkValues
_TnCardRtrvClkSwitch_Object = MibTableColumn
tnCardRtrvClkSwitch = _TnCardRtrvClkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 36),
    _TnCardRtrvClkSwitch_Type()
)
tnCardRtrvClkSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardRtrvClkSwitch.setStatus("current")


class _TnCardWtClkMeasureValues_Type(OctetString):
    """Custom type tnCardWtClkMeasureValues based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TnCardWtClkMeasureValues_Type.__name__ = "OctetString"
_TnCardWtClkMeasureValues_Object = MibTableColumn
tnCardWtClkMeasureValues = _TnCardWtClkMeasureValues_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 37),
    _TnCardWtClkMeasureValues_Type()
)
tnCardWtClkMeasureValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardWtClkMeasureValues.setStatus("current")
_TnCardPower_Type = Integer32
_TnCardPower_Object = MibTableColumn
tnCardPower = _TnCardPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 38),
    _TnCardPower_Type()
)
tnCardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardPower.setStatus("current")
if mibBuilder.loadTexts:
    tnCardPower.setUnits("milli-Watts")
_TnCardCurrent_Type = Unsigned32
_TnCardCurrent_Object = MibTableColumn
tnCardCurrent = _TnCardCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 39),
    _TnCardCurrent_Type()
)
tnCardCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tnCardCurrent.setUnits("milli-Amperes")


class _TnCardUplinkAdminMode_Type(Integer32):
    """Custom type tnCardUplinkAdminMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unassigned", 0),
          ("network", 1),
          ("accessUplink", 2))
    )


_TnCardUplinkAdminMode_Type.__name__ = "Integer32"
_TnCardUplinkAdminMode_Object = MibTableColumn
tnCardUplinkAdminMode = _TnCardUplinkAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 40),
    _TnCardUplinkAdminMode_Type()
)
tnCardUplinkAdminMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardUplinkAdminMode.setStatus("current")


class _TnCardLoopbackNoServPort_Type(InterfaceIndexOrZero):
    """Custom type tnCardLoopbackNoServPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnCardLoopbackNoServPort_Type.__name__ = "InterfaceIndexOrZero"
_TnCardLoopbackNoServPort_Object = MibTableColumn
tnCardLoopbackNoServPort = _TnCardLoopbackNoServPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 41),
    _TnCardLoopbackNoServPort_Type()
)
tnCardLoopbackNoServPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardLoopbackNoServPort.setStatus("current")


class _TnCardAlmProfName_Type(OctetString):
    """Custom type tnCardAlmProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TnCardAlmProfName_Type.__name__ = "OctetString"
_TnCardAlmProfName_Object = MibTableColumn
tnCardAlmProfName = _TnCardAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 42),
    _TnCardAlmProfName_Type()
)
tnCardAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardAlmProfName.setStatus("current")


class _TnCardAlmProfEnvName_Type(OctetString):
    """Custom type tnCardAlmProfEnvName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TnCardAlmProfEnvName_Type.__name__ = "OctetString"
_TnCardAlmProfEnvName_Object = MibTableColumn
tnCardAlmProfEnvName = _TnCardAlmProfEnvName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 43),
    _TnCardAlmProfEnvName_Type()
)
tnCardAlmProfEnvName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardAlmProfEnvName.setStatus("current")


class _TnCardLicenseData_Type(SnmpAdminString):
    """Custom type tnCardLicenseData based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardLicenseData_Type.__name__ = "SnmpAdminString"
_TnCardLicenseData_Object = MibTableColumn
tnCardLicenseData = _TnCardLicenseData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 44),
    _TnCardLicenseData_Type()
)
tnCardLicenseData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardLicenseData.setStatus("current")


class _TnCardLicenseAction_Type(Integer32):
    """Custom type tnCardLicenseAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("apply", 2),
          ("delete", 3))
    )


_TnCardLicenseAction_Type.__name__ = "Integer32"
_TnCardLicenseAction_Object = MibTableColumn
tnCardLicenseAction = _TnCardLicenseAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 45),
    _TnCardLicenseAction_Type()
)
tnCardLicenseAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardLicenseAction.setStatus("current")


class _TnCardLicenseCap1Val_Type(Unsigned32):
    """Custom type tnCardLicenseCap1Val based on Unsigned32"""
    defaultValue = 0


_TnCardLicenseCap1Val_Type.__name__ = "Unsigned32"
_TnCardLicenseCap1Val_Object = MibTableColumn
tnCardLicenseCap1Val = _TnCardLicenseCap1Val_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 46),
    _TnCardLicenseCap1Val_Type()
)
tnCardLicenseCap1Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardLicenseCap1Val.setStatus("current")


class _TnCardLicenseCap2Val_Type(Unsigned32):
    """Custom type tnCardLicenseCap2Val based on Unsigned32"""
    defaultValue = 0


_TnCardLicenseCap2Val_Type.__name__ = "Unsigned32"
_TnCardLicenseCap2Val_Object = MibTableColumn
tnCardLicenseCap2Val = _TnCardLicenseCap2Val_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 47),
    _TnCardLicenseCap2Val_Type()
)
tnCardLicenseCap2Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardLicenseCap2Val.setStatus("current")


class _TnCardLicenseTimeStamp_Type(Unsigned32):
    """Custom type tnCardLicenseTimeStamp based on Unsigned32"""
    defaultValue = 0


_TnCardLicenseTimeStamp_Type.__name__ = "Unsigned32"
_TnCardLicenseTimeStamp_Object = MibTableColumn
tnCardLicenseTimeStamp = _TnCardLicenseTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 48),
    _TnCardLicenseTimeStamp_Type()
)
tnCardLicenseTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardLicenseTimeStamp.setStatus("current")


class _TnCardLicenseRmaKey_Type(SnmpAdminString):
    """Custom type tnCardLicenseRmaKey based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnCardLicenseRmaKey_Type.__name__ = "SnmpAdminString"
_TnCardLicenseRmaKey_Object = MibTableColumn
tnCardLicenseRmaKey = _TnCardLicenseRmaKey_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 49),
    _TnCardLicenseRmaKey_Type()
)
tnCardLicenseRmaKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardLicenseRmaKey.setStatus("current")


class _TnCardMirrorLoopbackNoServPort_Type(InterfaceIndexOrZero):
    """Custom type tnCardMirrorLoopbackNoServPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnCardMirrorLoopbackNoServPort_Type.__name__ = "InterfaceIndexOrZero"
_TnCardMirrorLoopbackNoServPort_Object = MibTableColumn
tnCardMirrorLoopbackNoServPort = _TnCardMirrorLoopbackNoServPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 50),
    _TnCardMirrorLoopbackNoServPort_Type()
)
tnCardMirrorLoopbackNoServPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardMirrorLoopbackNoServPort.setStatus("current")


class _TnCardDNRLEDColor_Type(Integer32):
    """Custom type tnCardDNRLEDColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("orange", 2))
    )


_TnCardDNRLEDColor_Type.__name__ = "Integer32"
_TnCardDNRLEDColor_Object = MibTableColumn
tnCardDNRLEDColor = _TnCardDNRLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 51),
    _TnCardDNRLEDColor_Type()
)
tnCardDNRLEDColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardDNRLEDColor.setStatus("current")


class _TnCardTestHdNoServPort_Type(InterfaceIndexOrZero):
    """Custom type tnCardTestHdNoServPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnCardTestHdNoServPort_Type.__name__ = "InterfaceIndexOrZero"
_TnCardTestHdNoServPort_Object = MibTableColumn
tnCardTestHdNoServPort = _TnCardTestHdNoServPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 52),
    _TnCardTestHdNoServPort_Type()
)
tnCardTestHdNoServPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardTestHdNoServPort.setStatus("current")
_TnCardAmbientTemp_Type = Integer32
_TnCardAmbientTemp_Object = MibTableColumn
tnCardAmbientTemp = _TnCardAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 53),
    _TnCardAmbientTemp_Type()
)
tnCardAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardAmbientTemp.setStatus("current")
if mibBuilder.loadTexts:
    tnCardAmbientTemp.setUnits("Celsius")
_TnCardRpmRead_Type = Integer32
_TnCardRpmRead_Object = MibTableColumn
tnCardRpmRead = _TnCardRpmRead_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 54),
    _TnCardRpmRead_Type()
)
tnCardRpmRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardRpmRead.setStatus("current")


class _TnCardL1andL2Decoupled_Type(TruthValue):
    """Custom type tnCardL1andL2Decoupled based on TruthValue"""
    defaultValue = 1


_TnCardL1andL2Decoupled_Type.__name__ = "TruthValue"
_TnCardL1andL2Decoupled_Object = MibTableColumn
tnCardL1andL2Decoupled = _TnCardL1andL2Decoupled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 55),
    _TnCardL1andL2Decoupled_Type()
)
tnCardL1andL2Decoupled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardL1andL2Decoupled.setStatus("current")


class _TnCardIntWrkMode_Type(Integer32):
    """Custom type tnCardIntWrkMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("legacy", 1),
          ("standard", 2))
    )


_TnCardIntWrkMode_Type.__name__ = "Integer32"
_TnCardIntWrkMode_Object = MibTableColumn
tnCardIntWrkMode = _TnCardIntWrkMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 56),
    _TnCardIntWrkMode_Type()
)
tnCardIntWrkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardIntWrkMode.setStatus("current")
_TnCardTotalRam_Type = Unsigned32
_TnCardTotalRam_Object = MibTableColumn
tnCardTotalRam = _TnCardTotalRam_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 57),
    _TnCardTotalRam_Type()
)
tnCardTotalRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardTotalRam.setStatus("current")


class _TnCardTransportModeOSC_Type(Integer32):
    """Custom type tnCardTransportModeOSC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 1),
          ("layer3", 2))
    )


_TnCardTransportModeOSC_Type.__name__ = "Integer32"
_TnCardTransportModeOSC_Object = MibTableColumn
tnCardTransportModeOSC = _TnCardTransportModeOSC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 58),
    _TnCardTransportModeOSC_Type()
)
tnCardTransportModeOSC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardTransportModeOSC.setStatus("current")


class _TnCardModuleCfg_Type(Integer32):
    """Custom type tnCardModuleCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("plugLimit40", 1),
          ("plugLimit32", 2),
          ("plugLimit20", 3),
          ("elplugs", 4),
          ("thirtyPlugs", 5),
          ("twelvePlugs", 6),
          ("ninePlugs", 7))
    )


_TnCardModuleCfg_Type.__name__ = "Integer32"
_TnCardModuleCfg_Object = MibTableColumn
tnCardModuleCfg = _TnCardModuleCfg_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 59),
    _TnCardModuleCfg_Type()
)
tnCardModuleCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardModuleCfg.setStatus("current")
_TnCardLicenseRestricted_Type = TruthValue
_TnCardLicenseRestricted_Object = MibTableColumn
tnCardLicenseRestricted = _TnCardLicenseRestricted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 60),
    _TnCardLicenseRestricted_Type()
)
tnCardLicenseRestricted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardLicenseRestricted.setStatus("current")


class _TnCardLineMode_Type(Integer32):
    """Custom type tnCardLineMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("fixed", 2),
          ("dynamic", 3))
    )


_TnCardLineMode_Type.__name__ = "Integer32"
_TnCardLineMode_Object = MibTableColumn
tnCardLineMode = _TnCardLineMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 61),
    _TnCardLineMode_Type()
)
tnCardLineMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardLineMode.setStatus("current")


class _TnCardInitConfProfile_Type(Unsigned32):
    """Custom type tnCardInitConfProfile based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TnCardInitConfProfile_Type.__name__ = "Unsigned32"
_TnCardInitConfProfile_Object = MibTableColumn
tnCardInitConfProfile = _TnCardInitConfProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 62),
    _TnCardInitConfProfile_Type()
)
tnCardInitConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardInitConfProfile.setStatus("current")
_TnCardVirtual_Type = TruthValue
_TnCardVirtual_Object = MibTableColumn
tnCardVirtual = _TnCardVirtual_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 63),
    _TnCardVirtual_Type()
)
tnCardVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardVirtual.setStatus("current")
_TnCardOAMTestUnit_Type = NokiaOAMTestUnitType
_TnCardOAMTestUnit_Object = MibTableColumn
tnCardOAMTestUnit = _TnCardOAMTestUnit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 64),
    _TnCardOAMTestUnit_Type()
)
tnCardOAMTestUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardOAMTestUnit.setStatus("current")


class _TnCardSlotClkStatus_Type(Integer32):
    """Custom type tnCardSlotClkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("onFreq", 2),
          ("fail", 3))
    )


_TnCardSlotClkStatus_Type.__name__ = "Integer32"
_TnCardSlotClkStatus_Object = MibTableColumn
tnCardSlotClkStatus = _TnCardSlotClkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 65),
    _TnCardSlotClkStatus_Type()
)
tnCardSlotClkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardSlotClkStatus.setStatus("current")


class _TnCardClkSelectedValue_Type(Integer32):
    """Custom type tnCardClkSelectedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("yes", 2),
          ("no", 3))
    )


_TnCardClkSelectedValue_Type.__name__ = "Integer32"
_TnCardClkSelectedValue_Object = MibTableColumn
tnCardClkSelectedValue = _TnCardClkSelectedValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 66),
    _TnCardClkSelectedValue_Type()
)
tnCardClkSelectedValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardClkSelectedValue.setStatus("current")


class _TnCardShutdownCmd_Type(Integer32):
    """Custom type tnCardShutdownCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("shutdownForce", 2))
    )


_TnCardShutdownCmd_Type.__name__ = "Integer32"
_TnCardShutdownCmd_Object = MibTableColumn
tnCardShutdownCmd = _TnCardShutdownCmd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 67),
    _TnCardShutdownCmd_Type()
)
tnCardShutdownCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardShutdownCmd.setStatus("current")
_TnCardCpuTemperature_Type = Integer32
_TnCardCpuTemperature_Object = MibTableColumn
tnCardCpuTemperature = _TnCardCpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 68),
    _TnCardCpuTemperature_Type()
)
tnCardCpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardCpuTemperature.setStatus("current")
if mibBuilder.loadTexts:
    tnCardCpuTemperature.setUnits("Celsius")
_TnCardMainDeviceTemperature_Type = Integer32
_TnCardMainDeviceTemperature_Object = MibTableColumn
tnCardMainDeviceTemperature = _TnCardMainDeviceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 69),
    _TnCardMainDeviceTemperature_Type()
)
tnCardMainDeviceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardMainDeviceTemperature.setStatus("current")
if mibBuilder.loadTexts:
    tnCardMainDeviceTemperature.setUnits("Celsius")


class _TnCardAseMode_Type(Integer32):
    """Custom type tnCardAseMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unconfigured", 1),
          ("noNoise", 2),
          ("low", 3),
          ("standard", 4))
    )


_TnCardAseMode_Type.__name__ = "Integer32"
_TnCardAseMode_Object = MibTableColumn
tnCardAseMode = _TnCardAseMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 70),
    _TnCardAseMode_Type()
)
tnCardAseMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardAseMode.setStatus("current")


class _TnCardAddPowerMode_Type(Integer32):
    """Custom type tnCardAddPowerMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_TnCardAddPowerMode_Type.__name__ = "Integer32"
_TnCardAddPowerMode_Object = MibTableColumn
tnCardAddPowerMode = _TnCardAddPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 71),
    _TnCardAddPowerMode_Type()
)
tnCardAddPowerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardAddPowerMode.setStatus("current")


class _TnCardLOLCKDetectionEnable_Type(TruthValue):
    """Custom type tnCardLOLCKDetectionEnable based on TruthValue"""
    defaultValue = 2


_TnCardLOLCKDetectionEnable_Type.__name__ = "TruthValue"
_TnCardLOLCKDetectionEnable_Object = MibTableColumn
tnCardLOLCKDetectionEnable = _TnCardLOLCKDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 72),
    _TnCardLOLCKDetectionEnable_Type()
)
tnCardLOLCKDetectionEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardLOLCKDetectionEnable.setStatus("current")


class _TnCardSapLoopbackMacAddr_Type(MacAddress):
    """Custom type tnCardSapLoopbackMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TnCardSapLoopbackMacAddr_Type.__name__ = "MacAddress"
_TnCardSapLoopbackMacAddr_Object = MibTableColumn
tnCardSapLoopbackMacAddr = _TnCardSapLoopbackMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 73),
    _TnCardSapLoopbackMacAddr_Type()
)
tnCardSapLoopbackMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardSapLoopbackMacAddr.setStatus("current")


class _TnCardMgracd_Type(Integer32):
    """Custom type tnCardMgracd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("cp", 2),
          ("mgnpln", 3),
          ("cpmgnpln", 4))
    )


_TnCardMgracd_Type.__name__ = "Integer32"
_TnCardMgracd_Object = MibTableColumn
tnCardMgracd = _TnCardMgracd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 74),
    _TnCardMgracd_Type()
)
tnCardMgracd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardMgracd.setStatus("current")
_TnCardTargetAddPortInputPower_Type = Integer32
_TnCardTargetAddPortInputPower_Object = MibTableColumn
tnCardTargetAddPortInputPower = _TnCardTargetAddPortInputPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 75),
    _TnCardTargetAddPortInputPower_Type()
)
tnCardTargetAddPortInputPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardTargetAddPortInputPower.setStatus("current")
if mibBuilder.loadTexts:
    tnCardTargetAddPortInputPower.setUnits("mBm")
_TnCardPassThroughBandwidthUsage_Type = Integer32
_TnCardPassThroughBandwidthUsage_Object = MibTableColumn
tnCardPassThroughBandwidthUsage = _TnCardPassThroughBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 76),
    _TnCardPassThroughBandwidthUsage_Type()
)
tnCardPassThroughBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardPassThroughBandwidthUsage.setStatus("current")


class _TnCardUDCChanType_Type(Integer32):
    """Custom type tnCardUDCChanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gcc0", 1),
          ("gcc0Tcm", 2))
    )


_TnCardUDCChanType_Type.__name__ = "Integer32"
_TnCardUDCChanType_Object = MibTableColumn
tnCardUDCChanType = _TnCardUDCChanType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 77),
    _TnCardUDCChanType_Type()
)
tnCardUDCChanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardUDCChanType.setStatus("current")


class _TnCardUDCStatus_Type(Integer32):
    """Custom type tnCardUDCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_TnCardUDCStatus_Type.__name__ = "Integer32"
_TnCardUDCStatus_Object = MibTableColumn
tnCardUDCStatus = _TnCardUDCStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 2, 1, 78),
    _TnCardUDCStatus_Type()
)
tnCardUDCStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardUDCStatus.setStatus("current")
_TnCardAssemblyTable_Object = MibTable
tnCardAssemblyTable = _TnCardAssemblyTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnCardAssemblyTable.setStatus("current")
_TnCardAssemblyEntry_Object = MibTableRow
tnCardAssemblyEntry = _TnCardAssemblyEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1)
)
tnCardAssemblyEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-CARD-MIB", "tnCardAssemblyIndex"),
)
if mibBuilder.loadTexts:
    tnCardAssemblyEntry.setStatus("current")


class _TnCardAssemblyIndex_Type(Integer32):
    """Custom type tnCardAssemblyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TnCardAssemblyIndex_Type.__name__ = "Integer32"
_TnCardAssemblyIndex_Object = MibTableColumn
tnCardAssemblyIndex = _TnCardAssemblyIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1, 1),
    _TnCardAssemblyIndex_Type()
)
tnCardAssemblyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCardAssemblyIndex.setStatus("current")


class _TnCardAssemblyName_Type(SnmpAdminString):
    """Custom type tnCardAssemblyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnCardAssemblyName_Type.__name__ = "SnmpAdminString"
_TnCardAssemblyName_Object = MibTableColumn
tnCardAssemblyName = _TnCardAssemblyName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1, 2),
    _TnCardAssemblyName_Type()
)
tnCardAssemblyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardAssemblyName.setStatus("current")
_TnCardAssemblyCLEI_Type = TropicCardCLEI
_TnCardAssemblyCLEI_Object = MibTableColumn
tnCardAssemblyCLEI = _TnCardAssemblyCLEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1, 3),
    _TnCardAssemblyCLEI_Type()
)
tnCardAssemblyCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardAssemblyCLEI.setStatus("current")
_TnCardAssemblyHFD_Type = TropicCardHFD
_TnCardAssemblyHFD_Object = MibTableColumn
tnCardAssemblyHFD = _TnCardAssemblyHFD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1, 4),
    _TnCardAssemblyHFD_Type()
)
tnCardAssemblyHFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardAssemblyHFD.setStatus("current")
_TnCardAssemblySerialNumber_Type = TropicCardSerialNumber
_TnCardAssemblySerialNumber_Object = MibTableColumn
tnCardAssemblySerialNumber = _TnCardAssemblySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1, 5),
    _TnCardAssemblySerialNumber_Type()
)
tnCardAssemblySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardAssemblySerialNumber.setStatus("current")
_TnCardAssemblyManufacturingPartNumber_Type = TropicCardManufacturingPartNumber
_TnCardAssemblyManufacturingPartNumber_Object = MibTableColumn
tnCardAssemblyManufacturingPartNumber = _TnCardAssemblyManufacturingPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1, 6),
    _TnCardAssemblyManufacturingPartNumber_Type()
)
tnCardAssemblyManufacturingPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardAssemblyManufacturingPartNumber.setStatus("current")
_TnCardAssemblyMarketingPartNumber_Type = TropicCardMarketingPartNumber
_TnCardAssemblyMarketingPartNumber_Object = MibTableColumn
tnCardAssemblyMarketingPartNumber = _TnCardAssemblyMarketingPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 3, 1, 7),
    _TnCardAssemblyMarketingPartNumber_Type()
)
tnCardAssemblyMarketingPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardAssemblyMarketingPartNumber.setStatus("current")
_TnCardDbSyncTable_Object = MibTable
tnCardDbSyncTable = _TnCardDbSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnCardDbSyncTable.setStatus("current")
_TnCardDbSyncEntry_Object = MibTableRow
tnCardDbSyncEntry = _TnCardDbSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 5, 1)
)
tnCardDbSyncEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnCardDbSyncEntry.setStatus("current")


class _TnCardDBSyncEnabledByUser_Type(TruthValue):
    """Custom type tnCardDBSyncEnabledByUser based on TruthValue"""
    defaultValue = 2


_TnCardDBSyncEnabledByUser_Type.__name__ = "TruthValue"
_TnCardDBSyncEnabledByUser_Object = MibTableColumn
tnCardDBSyncEnabledByUser = _TnCardDBSyncEnabledByUser_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 5, 1, 1),
    _TnCardDBSyncEnabledByUser_Type()
)
tnCardDBSyncEnabledByUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardDBSyncEnabledByUser.setStatus("current")
_TnCardPrbsTestIdTable_Object = MibTable
tnCardPrbsTestIdTable = _TnCardPrbsTestIdTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnCardPrbsTestIdTable.setStatus("current")
_TnCardPrbsTestIdEntry_Object = MibTableRow
tnCardPrbsTestIdEntry = _TnCardPrbsTestIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 6, 1)
)
tnCardPrbsTestIdEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnCardPrbsTestIdEntry.setStatus("current")


class _TnCardPrbsTestIdOidList_Type(SnmpAdminString):
    """Custom type tnCardPrbsTestIdOidList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_TnCardPrbsTestIdOidList_Type.__name__ = "SnmpAdminString"
_TnCardPrbsTestIdOidList_Object = MibTableColumn
tnCardPrbsTestIdOidList = _TnCardPrbsTestIdOidList_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 2, 1, 6, 1, 1),
    _TnCardPrbsTestIdOidList_Type()
)
tnCardPrbsTestIdOidList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardPrbsTestIdOidList.setStatus("current")

# Managed Objects groups

tnCardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1, 1, 1)
)
tnCardScalarsGroup.setObjects(
    ("TROPIC-CARD-MIB", "tnCardTotal")
)
if mibBuilder.loadTexts:
    tnCardScalarsGroup.setStatus("current")

tnCardTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1, 1, 2)
)
tnCardTableGroup.setObjects(
      *(("TROPIC-CARD-MIB", "tnCardName"),
        ("TROPIC-CARD-MIB", "tnCardDescr"),
        ("TROPIC-CARD-MIB", "tnCardCLEI"),
        ("TROPIC-CARD-MIB", "tnCardHFD"),
        ("TROPIC-CARD-MIB", "tnCardSerialNumber"),
        ("TROPIC-CARD-MIB", "tnCardManufacturingPartNumber"),
        ("TROPIC-CARD-MIB", "tnCardMarketingPartNumber"),
        ("TROPIC-CARD-MIB", "tnCardSWGenericLoadName"),
        ("TROPIC-CARD-MIB", "tnCardHeight"),
        ("TROPIC-CARD-MIB", "tnCardWidth"),
        ("TROPIC-CARD-MIB", "tnCardTemperature"),
        ("TROPIC-CARD-MIB", "tnCardHighTemperatureThresh"),
        ("TROPIC-CARD-MIB", "tnCardLowTemperatureThresh"),
        ("TROPIC-CARD-MIB", "tnCardTemperatureTolerance"),
        ("TROPIC-CARD-MIB", "tnCardStatusLEDColor"),
        ("TROPIC-CARD-MIB", "tnCardStatusLEDState"),
        ("TROPIC-CARD-MIB", "tnCardActivityLEDColor"),
        ("TROPIC-CARD-MIB", "tnCardActivityLEDState"),
        ("TROPIC-CARD-MIB", "tnCardCompanyID"),
        ("TROPIC-CARD-MIB", "tnCardMnemonic"),
        ("TROPIC-CARD-MIB", "tnCardSWPartNum"),
        ("TROPIC-CARD-MIB", "tnCardDate"),
        ("TROPIC-CARD-MIB", "tnCardExtraData"),
        ("TROPIC-CARD-MIB", "tnCardAnyPortsInService"),
        ("TROPIC-CARD-MIB", "tnCardLastBootedFwBundleVer"),
        ("TROPIC-CARD-MIB", "tnCardNextFwBundleVer"),
        ("TROPIC-CARD-MIB", "tnCardFactoryID"),
        ("TROPIC-CARD-MIB", "tnCardCapacity"),
        ("TROPIC-CARD-MIB", "tnCardLACPSystemPriority"),
        ("TROPIC-CARD-MIB", "tnCardMaxPower"),
        ("TROPIC-CARD-MIB", "tnCardEthOamCcmFaultMgntMode"),
        ("TROPIC-CARD-MIB", "tnCardClkSwitch"),
        ("TROPIC-CARD-MIB", "tnCardRtrvClkSwitch"),
        ("TROPIC-CARD-MIB", "tnCardWtClkMeasureValues"),
        ("TROPIC-CARD-MIB", "tnCardPower"),
        ("TROPIC-CARD-MIB", "tnCardCurrent"),
        ("TROPIC-CARD-MIB", "tnCardUplinkAdminMode"),
        ("TROPIC-CARD-MIB", "tnCardLoopbackNoServPort"),
        ("TROPIC-CARD-MIB", "tnCardAlmProfName"),
        ("TROPIC-CARD-MIB", "tnCardAlmProfEnvName"),
        ("TROPIC-CARD-MIB", "tnCardLicenseData"),
        ("TROPIC-CARD-MIB", "tnCardLicenseAction"),
        ("TROPIC-CARD-MIB", "tnCardLicenseCap1Val"),
        ("TROPIC-CARD-MIB", "tnCardLicenseCap2Val"),
        ("TROPIC-CARD-MIB", "tnCardLicenseTimeStamp"),
        ("TROPIC-CARD-MIB", "tnCardLicenseRmaKey"),
        ("TROPIC-CARD-MIB", "tnCardMirrorLoopbackNoServPort"),
        ("TROPIC-CARD-MIB", "tnCardDNRLEDColor"),
        ("TROPIC-CARD-MIB", "tnCardTestHdNoServPort"),
        ("TROPIC-CARD-MIB", "tnCardAmbientTemp"),
        ("TROPIC-CARD-MIB", "tnCardRpmRead"),
        ("TROPIC-CARD-MIB", "tnCardL1andL2Decoupled"),
        ("TROPIC-CARD-MIB", "tnCardIntWrkMode"),
        ("TROPIC-CARD-MIB", "tnCardTotalRam"),
        ("TROPIC-CARD-MIB", "tnCardTransportModeOSC"),
        ("TROPIC-CARD-MIB", "tnCardModuleCfg"),
        ("TROPIC-CARD-MIB", "tnCardLicenseRestricted"),
        ("TROPIC-CARD-MIB", "tnCardLineMode"),
        ("TROPIC-CARD-MIB", "tnCardInitConfProfile"),
        ("TROPIC-CARD-MIB", "tnCardVirtual"),
        ("TROPIC-CARD-MIB", "tnCardOAMTestUnit"),
        ("TROPIC-CARD-MIB", "tnCardSlotClkStatus"),
        ("TROPIC-CARD-MIB", "tnCardClkSelectedValue"),
        ("TROPIC-CARD-MIB", "tnCardShutdownCmd"),
        ("TROPIC-CARD-MIB", "tnCardCpuTemperature"),
        ("TROPIC-CARD-MIB", "tnCardMainDeviceTemperature"),
        ("TROPIC-CARD-MIB", "tnCardAseMode"),
        ("TROPIC-CARD-MIB", "tnCardAddPowerMode"),
        ("TROPIC-CARD-MIB", "tnCardLOLCKDetectionEnable"),
        ("TROPIC-CARD-MIB", "tnCardSapLoopbackMacAddr"),
        ("TROPIC-CARD-MIB", "tnCardMgracd"),
        ("TROPIC-CARD-MIB", "tnCardTargetAddPortInputPower"),
        ("TROPIC-CARD-MIB", "tnCardPassThroughBandwidthUsage"),
        ("TROPIC-CARD-MIB", "tnCardUDCChanType"),
        ("TROPIC-CARD-MIB", "tnCardUDCStatus"))
)
if mibBuilder.loadTexts:
    tnCardTableGroup.setStatus("current")

tnCardAssemblyTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1, 1, 3)
)
tnCardAssemblyTableGroup.setObjects(
      *(("TROPIC-CARD-MIB", "tnCardAssemblyName"),
        ("TROPIC-CARD-MIB", "tnCardAssemblyCLEI"),
        ("TROPIC-CARD-MIB", "tnCardAssemblyHFD"),
        ("TROPIC-CARD-MIB", "tnCardAssemblySerialNumber"),
        ("TROPIC-CARD-MIB", "tnCardAssemblyManufacturingPartNumber"),
        ("TROPIC-CARD-MIB", "tnCardAssemblyMarketingPartNumber"))
)
if mibBuilder.loadTexts:
    tnCardAssemblyTableGroup.setStatus("current")

tnCardPrbsTestIdTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1, 1, 5)
)
tnCardPrbsTestIdTableGroup.setObjects(
    ("TROPIC-CARD-MIB", "tnCardPrbsTestIdOidList")
)
if mibBuilder.loadTexts:
    tnCardPrbsTestIdTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnCardCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 1, 1, 2, 1)
)
tnCardCompliance.setObjects(
      *(("TROPIC-CARD-MIB", "tnCardScalarsGroup"),
        ("TROPIC-CARD-MIB", "tnCardTableGroup"),
        ("TROPIC-CARD-MIB", "tnCardAssemblyTableGroup"),
        ("TROPIC-CARD-MIB", "tnCardPrbsTestIdTableGroup"))
)
if mibBuilder.loadTexts:
    tnCardCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-CARD-MIB",
    **{"NokiaOAMTestUnitType": NokiaOAMTestUnitType,
       "tnCardMibModule": tnCardMibModule,
       "tnCardConf": tnCardConf,
       "tnCardGroups": tnCardGroups,
       "tnCardScalarsGroup": tnCardScalarsGroup,
       "tnCardTableGroup": tnCardTableGroup,
       "tnCardAssemblyTableGroup": tnCardAssemblyTableGroup,
       "tnCardPrbsTestIdTableGroup": tnCardPrbsTestIdTableGroup,
       "tnCardCompliances": tnCardCompliances,
       "tnCardCompliance": tnCardCompliance,
       "tnCardObjs": tnCardObjs,
       "tnCardBasics": tnCardBasics,
       "tnCardTotal": tnCardTotal,
       "tnCardTable": tnCardTable,
       "tnCardEntry": tnCardEntry,
       "tnCardName": tnCardName,
       "tnCardDescr": tnCardDescr,
       "tnCardCLEI": tnCardCLEI,
       "tnCardHFD": tnCardHFD,
       "tnCardSerialNumber": tnCardSerialNumber,
       "tnCardManufacturingPartNumber": tnCardManufacturingPartNumber,
       "tnCardMarketingPartNumber": tnCardMarketingPartNumber,
       "tnCardSWGenericLoadName": tnCardSWGenericLoadName,
       "tnCardHeight": tnCardHeight,
       "tnCardWidth": tnCardWidth,
       "tnCardTemperature": tnCardTemperature,
       "tnCardHighTemperatureThresh": tnCardHighTemperatureThresh,
       "tnCardLowTemperatureThresh": tnCardLowTemperatureThresh,
       "tnCardTemperatureTolerance": tnCardTemperatureTolerance,
       "tnCardStatusLEDColor": tnCardStatusLEDColor,
       "tnCardStatusLEDState": tnCardStatusLEDState,
       "tnCardActivityLEDColor": tnCardActivityLEDColor,
       "tnCardActivityLEDState": tnCardActivityLEDState,
       "tnCardCompanyID": tnCardCompanyID,
       "tnCardMnemonic": tnCardMnemonic,
       "tnCardSWPartNum": tnCardSWPartNum,
       "tnCardDate": tnCardDate,
       "tnCardExtraData": tnCardExtraData,
       "tnCardAnyPortsInService": tnCardAnyPortsInService,
       "tnCardLastBootedFwBundleVer": tnCardLastBootedFwBundleVer,
       "tnCardNextFwBundleVer": tnCardNextFwBundleVer,
       "tnCardFactoryID": tnCardFactoryID,
       "tnCardCapacity": tnCardCapacity,
       "tnCardLACPSystemPriority": tnCardLACPSystemPriority,
       "tnCardMaxPower": tnCardMaxPower,
       "tnCardEthOamCcmFaultMgntMode": tnCardEthOamCcmFaultMgntMode,
       "tnCardClkSwitch": tnCardClkSwitch,
       "tnCardRtrvClkSwitch": tnCardRtrvClkSwitch,
       "tnCardWtClkMeasureValues": tnCardWtClkMeasureValues,
       "tnCardPower": tnCardPower,
       "tnCardCurrent": tnCardCurrent,
       "tnCardUplinkAdminMode": tnCardUplinkAdminMode,
       "tnCardLoopbackNoServPort": tnCardLoopbackNoServPort,
       "tnCardAlmProfName": tnCardAlmProfName,
       "tnCardAlmProfEnvName": tnCardAlmProfEnvName,
       "tnCardLicenseData": tnCardLicenseData,
       "tnCardLicenseAction": tnCardLicenseAction,
       "tnCardLicenseCap1Val": tnCardLicenseCap1Val,
       "tnCardLicenseCap2Val": tnCardLicenseCap2Val,
       "tnCardLicenseTimeStamp": tnCardLicenseTimeStamp,
       "tnCardLicenseRmaKey": tnCardLicenseRmaKey,
       "tnCardMirrorLoopbackNoServPort": tnCardMirrorLoopbackNoServPort,
       "tnCardDNRLEDColor": tnCardDNRLEDColor,
       "tnCardTestHdNoServPort": tnCardTestHdNoServPort,
       "tnCardAmbientTemp": tnCardAmbientTemp,
       "tnCardRpmRead": tnCardRpmRead,
       "tnCardL1andL2Decoupled": tnCardL1andL2Decoupled,
       "tnCardIntWrkMode": tnCardIntWrkMode,
       "tnCardTotalRam": tnCardTotalRam,
       "tnCardTransportModeOSC": tnCardTransportModeOSC,
       "tnCardModuleCfg": tnCardModuleCfg,
       "tnCardLicenseRestricted": tnCardLicenseRestricted,
       "tnCardLineMode": tnCardLineMode,
       "tnCardInitConfProfile": tnCardInitConfProfile,
       "tnCardVirtual": tnCardVirtual,
       "tnCardOAMTestUnit": tnCardOAMTestUnit,
       "tnCardSlotClkStatus": tnCardSlotClkStatus,
       "tnCardClkSelectedValue": tnCardClkSelectedValue,
       "tnCardShutdownCmd": tnCardShutdownCmd,
       "tnCardCpuTemperature": tnCardCpuTemperature,
       "tnCardMainDeviceTemperature": tnCardMainDeviceTemperature,
       "tnCardAseMode": tnCardAseMode,
       "tnCardAddPowerMode": tnCardAddPowerMode,
       "tnCardLOLCKDetectionEnable": tnCardLOLCKDetectionEnable,
       "tnCardSapLoopbackMacAddr": tnCardSapLoopbackMacAddr,
       "tnCardMgracd": tnCardMgracd,
       "tnCardTargetAddPortInputPower": tnCardTargetAddPortInputPower,
       "tnCardPassThroughBandwidthUsage": tnCardPassThroughBandwidthUsage,
       "tnCardUDCChanType": tnCardUDCChanType,
       "tnCardUDCStatus": tnCardUDCStatus,
       "tnCardAssemblyTable": tnCardAssemblyTable,
       "tnCardAssemblyEntry": tnCardAssemblyEntry,
       "tnCardAssemblyIndex": tnCardAssemblyIndex,
       "tnCardAssemblyName": tnCardAssemblyName,
       "tnCardAssemblyCLEI": tnCardAssemblyCLEI,
       "tnCardAssemblyHFD": tnCardAssemblyHFD,
       "tnCardAssemblySerialNumber": tnCardAssemblySerialNumber,
       "tnCardAssemblyManufacturingPartNumber": tnCardAssemblyManufacturingPartNumber,
       "tnCardAssemblyMarketingPartNumber": tnCardAssemblyMarketingPartNumber,
       "tnCardDbSyncTable": tnCardDbSyncTable,
       "tnCardDbSyncEntry": tnCardDbSyncEntry,
       "tnCardDBSyncEnabledByUser": tnCardDBSyncEnabledByUser,
       "tnCardPrbsTestIdTable": tnCardPrbsTestIdTable,
       "tnCardPrbsTestIdEntry": tnCardPrbsTestIdEntry,
       "tnCardPrbsTestIdOidList": tnCardPrbsTestIdOidList}
)
