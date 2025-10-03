# SNMP MIB module (MNI-PROTEUS-AMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mni\MNI-PROTEUS-AMT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:48 2025
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class LIMType(Integer32):
    """Custom type LIMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              99)
        )
    )
    namedValues = NamedValues(
        *(("limNotInstalled", 1),
          ("lim2xE1", 2),
          ("lim4xE1", 3),
          ("lim8xE1", 4),
          ("lim16xE1", 5),
          ("lim1xE3", 6),
          ("limEth100", 7),
          ("limEth100SG", 8),
          ("limGigEth", 9),
          ("lim155Mb", 10),
          ("lim2xDS1", 11),
          ("lim4xDS1", 12),
          ("lim8xDS1", 13),
          ("lim16xDS1", 14),
          ("lim1xDS3", 15),
          ("lim12xDS1", 16),
          ("lim12xE1", 17),
          ("lim32xDS1", 18),
          ("lim32xE1", 19),
          ("lim2xE3", 20),
          ("lim2xDS3", 21),
          ("limUBus", 22),
          ("lim4xDS3", 23),
          ("lim4xE3", 24),
          ("lim32xDS1E1", 25),
          ("lim16xDS1E1", 26),
          ("lim3xE3", 27),
          ("lim3xDS3", 28),
          ("lim28xDS1", 29),
          ("lim21xE1", 30),
          ("lim28xE1", 31),
          ("lim32xSHARP", 32),
          ("limUBusNoGigE", 33),
          ("lim64xE1", 34),
          ("lim64xDS1", 35),
          ("lim96xE1", 36),
          ("lim96xDS1", 37),
          ("lim100xE1", 38),
          ("lim118xDS1", 39),
          ("lim120xDS1", 40),
          ("lim120xSHARP", 41),
          ("lim4DS328DS1", 42),
          ("lim8GigE32DS1", 43),
          ("lim8GigE32E1", 44),
          ("lim8GigE32DS1E1", 45),
          ("limOther", 99))
    )





class ModulationType(Integer32):
    """Custom type ModulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              18,
              20,
              22,
              23,
              24,
              34,
              36,
              37,
              38,
              39,
              99)
        )
    )
    namedValues = NamedValues(
        *(("modQPSK", 2),
          ("mod8PSK", 3),
          ("mod16QAM", 4),
          ("mod32QAM", 5),
          ("mod64QAM", 6),
          ("mod128QAM", 7),
          ("mod256QAM", 8),
          ("modQPSK12", 18),
          ("mod16TCM34", 20),
          ("mod64TCM56", 22),
          ("mod128TCM67", 23),
          ("mod256TCM78", 24),
          ("modQPSK34", 34),
          ("mod16TCM78", 36),
          ("mod32TCM910", 37),
          ("mod64TCM1112", 38),
          ("mod128TCM1314", 39),
          ("modOther", 99))
    )





class ITUSeverity(Integer32):
    """Custom type ITUSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("indeterminate", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )





class AccessLevel(Integer32):
    """Custom type AccessLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              10)
        )
    )
    namedValues = NamedValues(
        *(("guest", 2),
          ("admin", 6),
          ("factory", 10))
    )





class Display64(DisplayString):
    """Custom type Display64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )





class RateLimit(Integer32):
    """Custom type RateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              256,
              512,
              1024,
              2048,
              4096,
              8192,
              16384,
              32768,
              65336,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("kbps128", 128),
          ("kbps256", 256),
          ("kbps512", 512),
          ("mbps1", 1024),
          ("mbps2", 2048),
          ("mbps4", 4096),
          ("mbps8", 8192),
          ("mbps16", 16384),
          ("mbps32", 32768),
          ("mbps64", 65336),
          ("mbps100", 100000))
    )





class IfBandwidth(Integer32):
    """Custom type IfBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              99)
        )
    )
    namedValues = NamedValues(
        *(("ifBoardNotInstalled", 1),
          ("ifBW3-5", 2),
          ("ifBW7", 3),
          ("ifBW14", 4),
          ("ifBW28", 5),
          ("ifBW5", 6),
          ("ifBW10", 7),
          ("ifBW20", 8),
          ("ifBW25", 9),
          ("ifBW2-5", 10),
          ("ifBW30", 11),
          ("ifBW3-75", 12),
          ("ifBW40", 13),
          ("ifBW50", 14),
          ("ifBW56", 15),
          ("ifBW60", 16),
          ("ifOther", 99))
    )





class LanSpeed(Integer32):
    """Custom type LanSpeed based on Integer32"""
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
        *(("lanAutoNegotiate", 1),
          ("lan10BaseTHalf", 2),
          ("lan100BaseTHalf", 3),
          ("lan100BaseTFull", 4),
          ("lanPoweredDown", 5),
          ("lan10BaseTFull", 6),
          ("lan1000BaseTFull", 7))
    )





class SHARPBERStatus(Integer32):
    """Custom type SHARPBERStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("berGT3Eminus3", 1),
          ("ber1Eminus3", 2),
          ("ber3Eminus4", 3),
          ("ber1Eminus4", 4),
          ("ber3Eminus5", 5),
          ("ber1Eminus5", 6),
          ("ber3Eminus6", 7),
          ("ber1Eminus6", 8),
          ("ber3Eminus7", 9),
          ("ber1Eminus7", 10),
          ("ber3Eminus8", 11),
          ("ber1Eminus8", 12),
          ("ber3Eminus9", 13),
          ("ber1Eminus9", 14),
          ("notReady", 15),
          ("noError", 16),
          ("notUsed", 17),
          ("ais", 18),
          ("oof", 19),
          ("los", 20),
          ("unknown", 21))
    )





class SHARPBERThresh(Integer32):
    """Custom type SHARPBERThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              8,
              10,
              12,
              14,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ber1Eminus3", 2),
          ("ber1Eminus4", 4),
          ("ber1Eminus5", 6),
          ("ber1Eminus6", 8),
          ("ber1Eminus7", 10),
          ("ber1Eminus8", 12),
          ("ber1Eminus9", 14),
          ("notUsed", 17))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Microwave_networks_ObjectIdentity = ObjectIdentity
microwave_networks = _Microwave_networks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323)
)
_MnRegistrations_ObjectIdentity = ObjectIdentity
mnRegistrations = _MnRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 11)
)
_MnRegSysObjID_ObjectIdentity = ObjectIdentity
mnRegSysObjID = _MnRegSysObjID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 11, 1)
)
_MnRegSysProtAMT_ObjectIdentity = ObjectIdentity
mnRegSysProtAMT = _MnRegSysProtAMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 11, 1, 1)
)
_MnRegSysProtAMTL_ObjectIdentity = ObjectIdentity
mnRegSysProtAMTL = _MnRegSysProtAMTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 11, 1, 2)
)
_MnRegSysProtAMTM_ObjectIdentity = ObjectIdentity
mnRegSysProtAMTM = _MnRegSysProtAMTM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 11, 1, 3)
)
_MnRegSysProtMX_ObjectIdentity = ObjectIdentity
mnRegSysProtMX = _MnRegSysProtMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 11, 1, 4)
)
_MnRegSysProtMXD_ObjectIdentity = ObjectIdentity
mnRegSysProtMXD = _MnRegSysProtMXD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 11, 1, 5)
)
_MnRegSysProtHE32_ObjectIdentity = ObjectIdentity
mnRegSysProtHE32 = _MnRegSysProtHE32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 11, 1, 6)
)
_MnModules_ObjectIdentity = ObjectIdentity
mnModules = _MnModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 11, 2)
)
_MnCommon_ObjectIdentity = ObjectIdentity
mnCommon = _MnCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 12)
)
_MnProducts_ObjectIdentity = ObjectIdentity
mnProducts = _MnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13)
)
_MnProtAMTV1MIB_ObjectIdentity = ObjectIdentity
mnProtAMTV1MIB = _MnProtAMTV1MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1)
)
_MnPrFV2Notifications_ObjectIdentity = ObjectIdentity
mnPrFV2Notifications = _MnPrFV2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 0)
)
_MnPrStatusObjects_ObjectIdentity = ObjectIdentity
mnPrStatusObjects = _MnPrStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1)
)
_MnPrLinkStatusObjects_ObjectIdentity = ObjectIdentity
mnPrLinkStatusObjects = _MnPrLinkStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 1)
)
_MnPrLinkStatLinkUp_Type = TruthValue
_MnPrLinkStatLinkUp_Object = MibScalar
mnPrLinkStatLinkUp = _MnPrLinkStatLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 1, 1),
    _MnPrLinkStatLinkUp_Type()
)
mnPrLinkStatLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLinkStatLinkUp.setStatus("mandatory")


class _MnPrLinkStatReachable_Type(Integer32):
    """Custom type mnPrLinkStatReachable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MnPrLinkStatReachable_Type.__name__ = "Integer32"
_MnPrLinkStatReachable_Object = MibScalar
mnPrLinkStatReachable = _MnPrLinkStatReachable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 1, 8),
    _MnPrLinkStatReachable_Type()
)
mnPrLinkStatReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLinkStatReachable.setStatus("mandatory")
_MnPrLinkStatAccessLevel_Type = AccessLevel
_MnPrLinkStatAccessLevel_Object = MibScalar
mnPrLinkStatAccessLevel = _MnPrLinkStatAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 1, 9),
    _MnPrLinkStatAccessLevel_Type()
)
mnPrLinkStatAccessLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLinkStatAccessLevel.setStatus("mandatory")
_MnPrLinkStatLastErrorText_Type = DisplayString
_MnPrLinkStatLastErrorText_Object = MibScalar
mnPrLinkStatLastErrorText = _MnPrLinkStatLastErrorText_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 1, 10),
    _MnPrLinkStatLastErrorText_Type()
)
mnPrLinkStatLastErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLinkStatLastErrorText.setStatus("mandatory")


class _MnPrLinkStatLocalRadioIndex_Type(Integer32):
    """Custom type mnPrLinkStatLocalRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MnPrLinkStatLocalRadioIndex_Type.__name__ = "Integer32"
_MnPrLinkStatLocalRadioIndex_Object = MibScalar
mnPrLinkStatLocalRadioIndex = _MnPrLinkStatLocalRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 1, 11),
    _MnPrLinkStatLocalRadioIndex_Type()
)
mnPrLinkStatLocalRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLinkStatLocalRadioIndex.setStatus("mandatory")
_MnPrRadStatTable_Object = MibTable
mnPrRadStatTable = _MnPrRadStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mnPrRadStatTable.setStatus("mandatory")
_MnPrRadStatEntry_Object = MibTableRow
mnPrRadStatEntry = _MnPrRadStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1)
)
mnPrRadStatEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
)
if mibBuilder.loadTexts:
    mnPrRadStatEntry.setStatus("mandatory")


class _MnRadioIndex_Type(Integer32):
    """Custom type mnRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MnRadioIndex_Type.__name__ = "Integer32"
_MnRadioIndex_Object = MibTableColumn
mnRadioIndex = _MnRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 1),
    _MnRadioIndex_Type()
)
mnRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnRadioIndex.setStatus("mandatory")
_MnPrRadStatCurSeverity_Type = ITUSeverity
_MnPrRadStatCurSeverity_Object = MibTableColumn
mnPrRadStatCurSeverity = _MnPrRadStatCurSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 2),
    _MnPrRadStatCurSeverity_Type()
)
mnPrRadStatCurSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatCurSeverity.setStatus("mandatory")
_MnPrRadStatLatchSeverity_Type = ITUSeverity
_MnPrRadStatLatchSeverity_Object = MibTableColumn
mnPrRadStatLatchSeverity = _MnPrRadStatLatchSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 3),
    _MnPrRadStatLatchSeverity_Type()
)
mnPrRadStatLatchSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatLatchSeverity.setStatus("mandatory")
_MnPrRadStatMinorAlarm_Type = TruthValue
_MnPrRadStatMinorAlarm_Object = MibTableColumn
mnPrRadStatMinorAlarm = _MnPrRadStatMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 4),
    _MnPrRadStatMinorAlarm_Type()
)
mnPrRadStatMinorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatMinorAlarm.setStatus("mandatory")
_MnPrRadStatControlOn_Type = TruthValue
_MnPrRadStatControlOn_Object = MibTableColumn
mnPrRadStatControlOn = _MnPrRadStatControlOn_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 5),
    _MnPrRadStatControlOn_Type()
)
mnPrRadStatControlOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatControlOn.setStatus("mandatory")


class _MnPrRadStatCurAlarmList_Type(OctetString):
    """Custom type mnPrRadStatCurAlarmList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_MnPrRadStatCurAlarmList_Type.__name__ = "OctetString"
_MnPrRadStatCurAlarmList_Object = MibTableColumn
mnPrRadStatCurAlarmList = _MnPrRadStatCurAlarmList_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 6),
    _MnPrRadStatCurAlarmList_Type()
)
mnPrRadStatCurAlarmList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatCurAlarmList.setStatus("mandatory")
_MnPrRadStatUptime_Type = Integer32
_MnPrRadStatUptime_Object = MibTableColumn
mnPrRadStatUptime = _MnPrRadStatUptime_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 8),
    _MnPrRadStatUptime_Type()
)
mnPrRadStatUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatUptime.setStatus("mandatory")
_MnPrRadStatLastAlarmChangeTime_Type = TimeTicks
_MnPrRadStatLastAlarmChangeTime_Object = MibTableColumn
mnPrRadStatLastAlarmChangeTime = _MnPrRadStatLastAlarmChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 10),
    _MnPrRadStatLastAlarmChangeTime_Type()
)
mnPrRadStatLastAlarmChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatLastAlarmChangeTime.setStatus("mandatory")
_MnPrRadStatLastCCChangeTime_Type = TimeTicks
_MnPrRadStatLastCCChangeTime_Object = MibTableColumn
mnPrRadStatLastCCChangeTime = _MnPrRadStatLastCCChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 12),
    _MnPrRadStatLastCCChangeTime_Type()
)
mnPrRadStatLastCCChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatLastCCChangeTime.setStatus("mandatory")
_MnPrRadStatLatchedTimeString_Type = DisplayString
_MnPrRadStatLatchedTimeString_Object = MibTableColumn
mnPrRadStatLatchedTimeString = _MnPrRadStatLatchedTimeString_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 13),
    _MnPrRadStatLatchedTimeString_Type()
)
mnPrRadStatLatchedTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatLatchedTimeString.setStatus("mandatory")


class _MnPrRadStatImageBooted_Type(Integer32):
    """Custom type mnPrRadStatImageBooted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_MnPrRadStatImageBooted_Type.__name__ = "Integer32"
_MnPrRadStatImageBooted_Object = MibTableColumn
mnPrRadStatImageBooted = _MnPrRadStatImageBooted_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 14),
    _MnPrRadStatImageBooted_Type()
)
mnPrRadStatImageBooted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatImageBooted.setStatus("mandatory")
_MnPrRadStatIFBoardType_Type = IfBandwidth
_MnPrRadStatIFBoardType_Object = MibTableColumn
mnPrRadStatIFBoardType = _MnPrRadStatIFBoardType_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 15),
    _MnPrRadStatIFBoardType_Type()
)
mnPrRadStatIFBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatIFBoardType.setStatus("mandatory")


class _MnPrRadStatPSVoltage_Type(Integer32):
    """Custom type mnPrRadStatPSVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("volt24", 1),
          ("volt48", 2),
          ("other", 99))
    )


_MnPrRadStatPSVoltage_Type.__name__ = "Integer32"
_MnPrRadStatPSVoltage_Object = MibTableColumn
mnPrRadStatPSVoltage = _MnPrRadStatPSVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 16),
    _MnPrRadStatPSVoltage_Type()
)
mnPrRadStatPSVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatPSVoltage.setStatus("mandatory")


class _MnPrRadStatODUFreqBand_Type(Integer32):
    """Custom type mnPrRadStatODUFreqBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_MnPrRadStatODUFreqBand_Type.__name__ = "Integer32"
_MnPrRadStatODUFreqBand_Object = MibTableColumn
mnPrRadStatODUFreqBand = _MnPrRadStatODUFreqBand_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 17),
    _MnPrRadStatODUFreqBand_Type()
)
mnPrRadStatODUFreqBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatODUFreqBand.setStatus("mandatory")


class _MnPrRadStatODUSubBand_Type(Integer32):
    """Custom type mnPrRadStatODUSubBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("subbandA", 1),
          ("subbandB", 2),
          ("subbandOther", 99))
    )


_MnPrRadStatODUSubBand_Type.__name__ = "Integer32"
_MnPrRadStatODUSubBand_Object = MibTableColumn
mnPrRadStatODUSubBand = _MnPrRadStatODUSubBand_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 18),
    _MnPrRadStatODUSubBand_Type()
)
mnPrRadStatODUSubBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatODUSubBand.setStatus("mandatory")
_MnPrRadStatODUTxHigh_Type = TruthValue
_MnPrRadStatODUTxHigh_Object = MibTableColumn
mnPrRadStatODUTxHigh = _MnPrRadStatODUTxHigh_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 19),
    _MnPrRadStatODUTxHigh_Type()
)
mnPrRadStatODUTxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatODUTxHigh.setStatus("mandatory")
_MnPrRadStatMinTxFreq_Type = Integer32
_MnPrRadStatMinTxFreq_Object = MibTableColumn
mnPrRadStatMinTxFreq = _MnPrRadStatMinTxFreq_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 20),
    _MnPrRadStatMinTxFreq_Type()
)
mnPrRadStatMinTxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatMinTxFreq.setStatus("mandatory")
_MnPrRadStatMaxTxFreq_Type = Integer32
_MnPrRadStatMaxTxFreq_Object = MibTableColumn
mnPrRadStatMaxTxFreq = _MnPrRadStatMaxTxFreq_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 21),
    _MnPrRadStatMaxTxFreq_Type()
)
mnPrRadStatMaxTxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatMaxTxFreq.setStatus("mandatory")
_MnPrRadStatMinRxFreq_Type = Integer32
_MnPrRadStatMinRxFreq_Object = MibTableColumn
mnPrRadStatMinRxFreq = _MnPrRadStatMinRxFreq_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 22),
    _MnPrRadStatMinRxFreq_Type()
)
mnPrRadStatMinRxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatMinRxFreq.setStatus("mandatory")
_MnPrRadStatMaxRxFreq_Type = Integer32
_MnPrRadStatMaxRxFreq_Object = MibTableColumn
mnPrRadStatMaxRxFreq = _MnPrRadStatMaxRxFreq_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 23),
    _MnPrRadStatMaxRxFreq_Type()
)
mnPrRadStatMaxRxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatMaxRxFreq.setStatus("mandatory")


class _MnPrRadStatProtType_Type(Integer32):
    """Custom type mnPrRadStatProtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unprotected", 1),
          ("primaryA", 2),
          ("secondaryB", 3))
    )


_MnPrRadStatProtType_Type.__name__ = "Integer32"
_MnPrRadStatProtType_Object = MibTableColumn
mnPrRadStatProtType = _MnPrRadStatProtType_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 24),
    _MnPrRadStatProtType_Type()
)
mnPrRadStatProtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatProtType.setStatus("mandatory")
_MnPrRadStatProtOtherRadioAlarm_Type = TruthValue
_MnPrRadStatProtOtherRadioAlarm_Object = MibTableColumn
mnPrRadStatProtOtherRadioAlarm = _MnPrRadStatProtOtherRadioAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 25),
    _MnPrRadStatProtOtherRadioAlarm_Type()
)
mnPrRadStatProtOtherRadioAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatProtOtherRadioAlarm.setStatus("mandatory")
_MnPrRadStatProtManualMode_Type = TruthValue
_MnPrRadStatProtManualMode_Object = MibTableColumn
mnPrRadStatProtManualMode = _MnPrRadStatProtManualMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 26),
    _MnPrRadStatProtManualMode_Type()
)
mnPrRadStatProtManualMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatProtManualMode.setStatus("mandatory")
_MnPrRadStatProtOnlineState_Type = TruthValue
_MnPrRadStatProtOnlineState_Object = MibTableColumn
mnPrRadStatProtOnlineState = _MnPrRadStatProtOnlineState_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 27),
    _MnPrRadStatProtOnlineState_Type()
)
mnPrRadStatProtOnlineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatProtOnlineState.setStatus("mandatory")
_MnPrRadStatMinTxPower_Type = Integer32
_MnPrRadStatMinTxPower_Object = MibTableColumn
mnPrRadStatMinTxPower = _MnPrRadStatMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 28),
    _MnPrRadStatMinTxPower_Type()
)
mnPrRadStatMinTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatMinTxPower.setStatus("mandatory")
_MnPrRadStatMaxTxPower_Type = Integer32
_MnPrRadStatMaxTxPower_Object = MibTableColumn
mnPrRadStatMaxTxPower = _MnPrRadStatMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 29),
    _MnPrRadStatMaxTxPower_Type()
)
mnPrRadStatMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatMaxTxPower.setStatus("mandatory")
_MnPrRadStatPerfHistDuration_Type = DisplayString
_MnPrRadStatPerfHistDuration_Object = MibTableColumn
mnPrRadStatPerfHistDuration = _MnPrRadStatPerfHistDuration_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 30),
    _MnPrRadStatPerfHistDuration_Type()
)
mnPrRadStatPerfHistDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatPerfHistDuration.setStatus("mandatory")
_MnPrRadStatPerfHistMinDuration_Type = DisplayString
_MnPrRadStatPerfHistMinDuration_Object = MibTableColumn
mnPrRadStatPerfHistMinDuration = _MnPrRadStatPerfHistMinDuration_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 31),
    _MnPrRadStatPerfHistMinDuration_Type()
)
mnPrRadStatPerfHistMinDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatPerfHistMinDuration.setStatus("mandatory")
_MnPrRadStatPerfHistRecords_Type = Integer32
_MnPrRadStatPerfHistRecords_Object = MibTableColumn
mnPrRadStatPerfHistRecords = _MnPrRadStatPerfHistRecords_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 32),
    _MnPrRadStatPerfHistRecords_Type()
)
mnPrRadStatPerfHistRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatPerfHistRecords.setStatus("mandatory")
_MnPrRadStatPerfHistMinRecords_Type = Integer32
_MnPrRadStatPerfHistMinRecords_Object = MibTableColumn
mnPrRadStatPerfHistMinRecords = _MnPrRadStatPerfHistMinRecords_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 33),
    _MnPrRadStatPerfHistMinRecords_Type()
)
mnPrRadStatPerfHistMinRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatPerfHistMinRecords.setStatus("mandatory")
_MnPrRadStatPerfHistMaxVarIndex_Type = Integer32
_MnPrRadStatPerfHistMaxVarIndex_Object = MibTableColumn
mnPrRadStatPerfHistMaxVarIndex = _MnPrRadStatPerfHistMaxVarIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 34),
    _MnPrRadStatPerfHistMaxVarIndex_Type()
)
mnPrRadStatPerfHistMaxVarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatPerfHistMaxVarIndex.setStatus("mandatory")
_MnPrRadStatTrSpace_Type = Integer32
_MnPrRadStatTrSpace_Object = MibTableColumn
mnPrRadStatTrSpace = _MnPrRadStatTrSpace_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 35),
    _MnPrRadStatTrSpace_Type()
)
mnPrRadStatTrSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatTrSpace.setStatus("mandatory")
_MnPrRadStatModulation_Type = ModulationType
_MnPrRadStatModulation_Object = MibTableColumn
mnPrRadStatModulation = _MnPrRadStatModulation_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 36),
    _MnPrRadStatModulation_Type()
)
mnPrRadStatModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatModulation.setStatus("mandatory")


class _MnPrRadStatProtToggleMode_Type(Integer32):
    """Custom type mnPrRadStatProtToggleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("positionAuto", 1),
          ("positionPri", 2),
          ("positionSec", 3))
    )


_MnPrRadStatProtToggleMode_Type.__name__ = "Integer32"
_MnPrRadStatProtToggleMode_Object = MibTableColumn
mnPrRadStatProtToggleMode = _MnPrRadStatProtToggleMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 41),
    _MnPrRadStatProtToggleMode_Type()
)
mnPrRadStatProtToggleMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatProtToggleMode.setStatus("mandatory")
_MnPrRadStatModulationInst_Type = ModulationType
_MnPrRadStatModulationInst_Object = MibTableColumn
mnPrRadStatModulationInst = _MnPrRadStatModulationInst_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 42),
    _MnPrRadStatModulationInst_Type()
)
mnPrRadStatModulationInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatModulationInst.setStatus("mandatory")
_MnPrRadStatModulationConf_Type = ModulationType
_MnPrRadStatModulationConf_Object = MibTableColumn
mnPrRadStatModulationConf = _MnPrRadStatModulationConf_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 43),
    _MnPrRadStatModulationConf_Type()
)
mnPrRadStatModulationConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatModulationConf.setStatus("mandatory")
_MnPrRadStatModulationProp_Type = ModulationType
_MnPrRadStatModulationProp_Object = MibTableColumn
mnPrRadStatModulationProp = _MnPrRadStatModulationProp_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 44),
    _MnPrRadStatModulationProp_Type()
)
mnPrRadStatModulationProp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatModulationProp.setStatus("mandatory")
_MnPrRadStatSysGainConf_Type = Integer32
_MnPrRadStatSysGainConf_Object = MibTableColumn
mnPrRadStatSysGainConf = _MnPrRadStatSysGainConf_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 45),
    _MnPrRadStatSysGainConf_Type()
)
mnPrRadStatSysGainConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatSysGainConf.setStatus("mandatory")
_MnPrRadStatSysGainProp_Type = Integer32
_MnPrRadStatSysGainProp_Object = MibTableColumn
mnPrRadStatSysGainProp = _MnPrRadStatSysGainProp_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 46),
    _MnPrRadStatSysGainProp_Type()
)
mnPrRadStatSysGainProp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatSysGainProp.setStatus("mandatory")


class _MnPrRadStatLoopSwitchStat_Type(Integer32):
    """Custom type mnPrRadStatLoopSwitchStat based on Integer32"""
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
        *(("detected", 1),
          ("broken", 2),
          ("offline", 3),
          ("unknown", 4))
    )


_MnPrRadStatLoopSwitchStat_Type.__name__ = "Integer32"
_MnPrRadStatLoopSwitchStat_Object = MibTableColumn
mnPrRadStatLoopSwitchStat = _MnPrRadStatLoopSwitchStat_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 2, 1, 47),
    _MnPrRadStatLoopSwitchStat_Type()
)
mnPrRadStatLoopSwitchStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadStatLoopSwitchStat.setStatus("mandatory")
_MnPrRouteStatTable_Object = MibTable
mnPrRouteStatTable = _MnPrRouteStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mnPrRouteStatTable.setStatus("mandatory")
_MnPrRouteStatEntry_Object = MibTableRow
mnPrRouteStatEntry = _MnPrRouteStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 3, 1)
)
mnPrRouteStatEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrRouteStatIndex"),
)
if mibBuilder.loadTexts:
    mnPrRouteStatEntry.setStatus("mandatory")


class _MnPrRouteStatIndex_Type(Integer32):
    """Custom type mnPrRouteStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MnPrRouteStatIndex_Type.__name__ = "Integer32"
_MnPrRouteStatIndex_Object = MibTableColumn
mnPrRouteStatIndex = _MnPrRouteStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 3, 1, 1),
    _MnPrRouteStatIndex_Type()
)
mnPrRouteStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRouteStatIndex.setStatus("mandatory")
_MnPrRouteStatDestination_Type = IpAddress
_MnPrRouteStatDestination_Object = MibTableColumn
mnPrRouteStatDestination = _MnPrRouteStatDestination_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 3, 1, 2),
    _MnPrRouteStatDestination_Type()
)
mnPrRouteStatDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRouteStatDestination.setStatus("mandatory")
_MnPrRouteStatMask_Type = IpAddress
_MnPrRouteStatMask_Object = MibTableColumn
mnPrRouteStatMask = _MnPrRouteStatMask_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 3, 1, 3),
    _MnPrRouteStatMask_Type()
)
mnPrRouteStatMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRouteStatMask.setStatus("mandatory")
_MnPrRouteStatNextHop_Type = IpAddress
_MnPrRouteStatNextHop_Object = MibTableColumn
mnPrRouteStatNextHop = _MnPrRouteStatNextHop_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 3, 1, 4),
    _MnPrRouteStatNextHop_Type()
)
mnPrRouteStatNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRouteStatNextHop.setStatus("mandatory")
_MnPrRouteStatMetric_Type = Integer32
_MnPrRouteStatMetric_Object = MibTableColumn
mnPrRouteStatMetric = _MnPrRouteStatMetric_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 3, 1, 5),
    _MnPrRouteStatMetric_Type()
)
mnPrRouteStatMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRouteStatMetric.setStatus("mandatory")
_MnPrRouteStatInterface_Type = Integer32
_MnPrRouteStatInterface_Object = MibTableColumn
mnPrRouteStatInterface = _MnPrRouteStatInterface_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 3, 1, 6),
    _MnPrRouteStatInterface_Type()
)
mnPrRouteStatInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRouteStatInterface.setStatus("mandatory")
_MnPrRouteStatType_Type = DisplayString
_MnPrRouteStatType_Object = MibTableColumn
mnPrRouteStatType = _MnPrRouteStatType_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 3, 1, 7),
    _MnPrRouteStatType_Type()
)
mnPrRouteStatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRouteStatType.setStatus("mandatory")
_MnPrRouteStatHowAdded_Type = DisplayString
_MnPrRouteStatHowAdded_Object = MibTableColumn
mnPrRouteStatHowAdded = _MnPrRouteStatHowAdded_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 3, 1, 8),
    _MnPrRouteStatHowAdded_Type()
)
mnPrRouteStatHowAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRouteStatHowAdded.setStatus("mandatory")
_MnPrOpResultTable_Object = MibTable
mnPrOpResultTable = _MnPrOpResultTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 4)
)
if mibBuilder.loadTexts:
    mnPrOpResultTable.setStatus("mandatory")
_MnPrOpResultEntry_Object = MibTableRow
mnPrOpResultEntry = _MnPrOpResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 4, 1)
)
mnPrOpResultEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrOpResultIndex"),
)
if mibBuilder.loadTexts:
    mnPrOpResultEntry.setStatus("mandatory")


class _MnPrOpResultIndex_Type(Integer32):
    """Custom type mnPrOpResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MnPrOpResultIndex_Type.__name__ = "Integer32"
_MnPrOpResultIndex_Object = MibTableColumn
mnPrOpResultIndex = _MnPrOpResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 4, 1, 1),
    _MnPrOpResultIndex_Type()
)
mnPrOpResultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrOpResultIndex.setStatus("mandatory")
_MnPrOpResultLevel_Type = Integer32
_MnPrOpResultLevel_Object = MibTableColumn
mnPrOpResultLevel = _MnPrOpResultLevel_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 4, 1, 2),
    _MnPrOpResultLevel_Type()
)
mnPrOpResultLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrOpResultLevel.setStatus("mandatory")
_MnPrOpResultMessage_Type = DisplayString
_MnPrOpResultMessage_Object = MibTableColumn
mnPrOpResultMessage = _MnPrOpResultMessage_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 4, 1, 3),
    _MnPrOpResultMessage_Type()
)
mnPrOpResultMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrOpResultMessage.setStatus("mandatory")
_MnPrOpResultArgument_Type = Integer32
_MnPrOpResultArgument_Object = MibTableColumn
mnPrOpResultArgument = _MnPrOpResultArgument_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 1, 4, 1, 4),
    _MnPrOpResultArgument_Type()
)
mnPrOpResultArgument.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrOpResultArgument.setStatus("mandatory")
_MnPrAlarmObjects_ObjectIdentity = ObjectIdentity
mnPrAlarmObjects = _MnPrAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2)
)
_MnPrCurAlarmTable_Object = MibTable
mnPrCurAlarmTable = _MnPrCurAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mnPrCurAlarmTable.setStatus("mandatory")
_MnPrCurAlarmEntry_Object = MibTableRow
mnPrCurAlarmEntry = _MnPrCurAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 3, 1)
)
mnPrCurAlarmEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrCurAlarmID"),
)
if mibBuilder.loadTexts:
    mnPrCurAlarmEntry.setStatus("mandatory")


class _MnPrCurAlarmID_Type(Integer32):
    """Custom type mnPrCurAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MnPrCurAlarmID_Type.__name__ = "Integer32"
_MnPrCurAlarmID_Object = MibTableColumn
mnPrCurAlarmID = _MnPrCurAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 3, 1, 1),
    _MnPrCurAlarmID_Type()
)
mnPrCurAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrCurAlarmID.setStatus("mandatory")
_MnPrCurAlarmText_Type = DisplayString
_MnPrCurAlarmText_Object = MibTableColumn
mnPrCurAlarmText = _MnPrCurAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 3, 1, 3),
    _MnPrCurAlarmText_Type()
)
mnPrCurAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrCurAlarmText.setStatus("mandatory")
_MnPrLatAlarmTable_Object = MibTable
mnPrLatAlarmTable = _MnPrLatAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 5)
)
if mibBuilder.loadTexts:
    mnPrLatAlarmTable.setStatus("mandatory")
_MnPrLatAlarmEntry_Object = MibTableRow
mnPrLatAlarmEntry = _MnPrLatAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 5, 1)
)
mnPrLatAlarmEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrLatAlarmID"),
)
if mibBuilder.loadTexts:
    mnPrLatAlarmEntry.setStatus("mandatory")


class _MnPrLatAlarmID_Type(Integer32):
    """Custom type mnPrLatAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MnPrLatAlarmID_Type.__name__ = "Integer32"
_MnPrLatAlarmID_Object = MibTableColumn
mnPrLatAlarmID = _MnPrLatAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 5, 1, 1),
    _MnPrLatAlarmID_Type()
)
mnPrLatAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLatAlarmID.setStatus("mandatory")
_MnPrLatAlarmText_Type = DisplayString
_MnPrLatAlarmText_Object = MibTableColumn
mnPrLatAlarmText = _MnPrLatAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 5, 1, 2),
    _MnPrLatAlarmText_Type()
)
mnPrLatAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLatAlarmText.setStatus("mandatory")
_MnPrAlarmLogTable_Object = MibTable
mnPrAlarmLogTable = _MnPrAlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mnPrAlarmLogTable.setStatus("mandatory")
_MnPrAlarmLogEntry_Object = MibTableRow
mnPrAlarmLogEntry = _MnPrAlarmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 6, 1)
)
mnPrAlarmLogEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrAlarmLogIndex"),
)
if mibBuilder.loadTexts:
    mnPrAlarmLogEntry.setStatus("mandatory")


class _MnPrAlarmLogIndex_Type(Integer32):
    """Custom type mnPrAlarmLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_MnPrAlarmLogIndex_Type.__name__ = "Integer32"
_MnPrAlarmLogIndex_Object = MibTableColumn
mnPrAlarmLogIndex = _MnPrAlarmLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 6, 1, 1),
    _MnPrAlarmLogIndex_Type()
)
mnPrAlarmLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrAlarmLogIndex.setStatus("mandatory")
_MnPrAlarmLogText_Type = DisplayString
_MnPrAlarmLogText_Object = MibTableColumn
mnPrAlarmLogText = _MnPrAlarmLogText_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 6, 1, 2),
    _MnPrAlarmLogText_Type()
)
mnPrAlarmLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrAlarmLogText.setStatus("mandatory")
_MnPrEventLogTable_Object = MibTable
mnPrEventLogTable = _MnPrEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 7)
)
if mibBuilder.loadTexts:
    mnPrEventLogTable.setStatus("mandatory")
_MnPrEventLogEntry_Object = MibTableRow
mnPrEventLogEntry = _MnPrEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 7, 1)
)
mnPrEventLogEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrEventLogIndex"),
)
if mibBuilder.loadTexts:
    mnPrEventLogEntry.setStatus("mandatory")


class _MnPrEventLogIndex_Type(Integer32):
    """Custom type mnPrEventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_MnPrEventLogIndex_Type.__name__ = "Integer32"
_MnPrEventLogIndex_Object = MibTableColumn
mnPrEventLogIndex = _MnPrEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 7, 1, 1),
    _MnPrEventLogIndex_Type()
)
mnPrEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrEventLogIndex.setStatus("mandatory")
_MnPrEventLogText_Type = DisplayString
_MnPrEventLogText_Object = MibTableColumn
mnPrEventLogText = _MnPrEventLogText_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 2, 7, 1, 2),
    _MnPrEventLogText_Type()
)
mnPrEventLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrEventLogText.setStatus("mandatory")
_MnPrNotifyObjects_ObjectIdentity = ObjectIdentity
mnPrNotifyObjects = _MnPrNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 3)
)
_MnPrNotifyID_Type = Integer32
_MnPrNotifyID_Object = MibScalar
mnPrNotifyID = _MnPrNotifyID_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 3, 1),
    _MnPrNotifyID_Type()
)
mnPrNotifyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrNotifyID.setStatus("mandatory")
_MnPrNotifyText_Type = DisplayString
_MnPrNotifyText_Object = MibScalar
mnPrNotifyText = _MnPrNotifyText_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 3, 2),
    _MnPrNotifyText_Type()
)
mnPrNotifyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrNotifyText.setStatus("mandatory")


class _MnPrNotifyParameter_Type(Integer32):
    """Custom type mnPrNotifyParameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MnPrNotifyParameter_Type.__name__ = "Integer32"
_MnPrNotifyParameter_Object = MibScalar
mnPrNotifyParameter = _MnPrNotifyParameter_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 3, 3),
    _MnPrNotifyParameter_Type()
)
mnPrNotifyParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrNotifyParameter.setStatus("mandatory")


class _MnPrNotifySeverity_Type(Integer32):
    """Custom type mnPrNotifySeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MnPrNotifySeverity_Type.__name__ = "Integer32"
_MnPrNotifySeverity_Object = MibScalar
mnPrNotifySeverity = _MnPrNotifySeverity_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 3, 4),
    _MnPrNotifySeverity_Type()
)
mnPrNotifySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrNotifySeverity.setStatus("mandatory")


class _MnPrNotifyRadioIndex_Type(Integer32):
    """Custom type mnPrNotifyRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MnPrNotifyRadioIndex_Type.__name__ = "Integer32"
_MnPrNotifyRadioIndex_Object = MibScalar
mnPrNotifyRadioIndex = _MnPrNotifyRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 3, 5),
    _MnPrNotifyRadioIndex_Type()
)
mnPrNotifyRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrNotifyRadioIndex.setStatus("mandatory")
_MnPrNotifyRadioName_Type = DisplayString
_MnPrNotifyRadioName_Object = MibScalar
mnPrNotifyRadioName = _MnPrNotifyRadioName_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 3, 6),
    _MnPrNotifyRadioName_Type()
)
mnPrNotifyRadioName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrNotifyRadioName.setStatus("mandatory")
_MnPrNotifyTimeStamp_Type = DateAndTime
_MnPrNotifyTimeStamp_Object = MibScalar
mnPrNotifyTimeStamp = _MnPrNotifyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 3, 7),
    _MnPrNotifyTimeStamp_Type()
)
mnPrNotifyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrNotifyTimeStamp.setStatus("mandatory")
_MnPrPerformanceObjects_ObjectIdentity = ObjectIdentity
mnPrPerformanceObjects = _MnPrPerformanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4)
)
_MnPrPerfBaseTable_Object = MibTable
mnPrPerfBaseTable = _MnPrPerfBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mnPrPerfBaseTable.setStatus("mandatory")
_MnPrPerfBaseEntry_Object = MibTableRow
mnPrPerfBaseEntry = _MnPrPerfBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1)
)
mnPrPerfBaseEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnInterfaceIndex"),
)
if mibBuilder.loadTexts:
    mnPrPerfBaseEntry.setStatus("mandatory")


class _MnInterfaceIndex_Type(Integer32):
    """Custom type mnInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_MnInterfaceIndex_Type.__name__ = "Integer32"
_MnInterfaceIndex_Object = MibTableColumn
mnInterfaceIndex = _MnInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 1),
    _MnInterfaceIndex_Type()
)
mnInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnInterfaceIndex.setStatus("mandatory")


class _MnPrPerfBaseTxPower_Type(Integer32):
    """Custom type mnPrPerfBaseTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 30),
    )


_MnPrPerfBaseTxPower_Type.__name__ = "Integer32"
_MnPrPerfBaseTxPower_Object = MibTableColumn
mnPrPerfBaseTxPower = _MnPrPerfBaseTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 2),
    _MnPrPerfBaseTxPower_Type()
)
mnPrPerfBaseTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseTxPower.setStatus("mandatory")


class _MnPrPerfBaseRSL_Type(Integer32):
    """Custom type mnPrPerfBaseRSL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_MnPrPerfBaseRSL_Type.__name__ = "Integer32"
_MnPrPerfBaseRSL_Object = MibTableColumn
mnPrPerfBaseRSL = _MnPrPerfBaseRSL_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 3),
    _MnPrPerfBaseRSL_Type()
)
mnPrPerfBaseRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseRSL.setStatus("mandatory")


class _MnPrPerfBaseFadeMargin_Type(Integer32):
    """Custom type mnPrPerfBaseFadeMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_MnPrPerfBaseFadeMargin_Type.__name__ = "Integer32"
_MnPrPerfBaseFadeMargin_Object = MibTableColumn
mnPrPerfBaseFadeMargin = _MnPrPerfBaseFadeMargin_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 4),
    _MnPrPerfBaseFadeMargin_Type()
)
mnPrPerfBaseFadeMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseFadeMargin.setStatus("mandatory")
_MnPrPerfBaseElapsedSecs_Type = Counter32
_MnPrPerfBaseElapsedSecs_Object = MibTableColumn
mnPrPerfBaseElapsedSecs = _MnPrPerfBaseElapsedSecs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 5),
    _MnPrPerfBaseElapsedSecs_Type()
)
mnPrPerfBaseElapsedSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseElapsedSecs.setStatus("mandatory")
_MnPrPerfBaseASs_Type = Counter32
_MnPrPerfBaseASs_Object = MibTableColumn
mnPrPerfBaseASs = _MnPrPerfBaseASs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 6),
    _MnPrPerfBaseASs_Type()
)
mnPrPerfBaseASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseASs.setStatus("mandatory")
_MnPrPerfBaseUSs_Type = Counter32
_MnPrPerfBaseUSs_Object = MibTableColumn
mnPrPerfBaseUSs = _MnPrPerfBaseUSs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 7),
    _MnPrPerfBaseUSs_Type()
)
mnPrPerfBaseUSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseUSs.setStatus("mandatory")
_MnPrPerfBaseESs_Type = Counter32
_MnPrPerfBaseESs_Object = MibTableColumn
mnPrPerfBaseESs = _MnPrPerfBaseESs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 8),
    _MnPrPerfBaseESs_Type()
)
mnPrPerfBaseESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseESs.setStatus("mandatory")
_MnPrPerfBaseSESs_Type = Counter32
_MnPrPerfBaseSESs_Object = MibTableColumn
mnPrPerfBaseSESs = _MnPrPerfBaseSESs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 9),
    _MnPrPerfBaseSESs_Type()
)
mnPrPerfBaseSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseSESs.setStatus("mandatory")
_MnPrPerfBaseTotalBlocks_Type = Display64
_MnPrPerfBaseTotalBlocks_Object = MibTableColumn
mnPrPerfBaseTotalBlocks = _MnPrPerfBaseTotalBlocks_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 10),
    _MnPrPerfBaseTotalBlocks_Type()
)
mnPrPerfBaseTotalBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseTotalBlocks.setStatus("mandatory")
_MnPrPerfBaseErrBlocks_Type = Display64
_MnPrPerfBaseErrBlocks_Object = MibTableColumn
mnPrPerfBaseErrBlocks = _MnPrPerfBaseErrBlocks_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 11),
    _MnPrPerfBaseErrBlocks_Type()
)
mnPrPerfBaseErrBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseErrBlocks.setStatus("mandatory")
_MnPrPerfBaseBBEs_Type = Display64
_MnPrPerfBaseBBEs_Object = MibTableColumn
mnPrPerfBaseBBEs = _MnPrPerfBaseBBEs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 12),
    _MnPrPerfBaseBBEs_Type()
)
mnPrPerfBaseBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseBBEs.setStatus("mandatory")
_MnPrPerfBaseSNR_Type = DisplayString
_MnPrPerfBaseSNR_Object = MibTableColumn
mnPrPerfBaseSNR = _MnPrPerfBaseSNR_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 13),
    _MnPrPerfBaseSNR_Type()
)
mnPrPerfBaseSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseSNR.setStatus("mandatory")
_MnPrPerfBaseDecoderStress_Type = DisplayString
_MnPrPerfBaseDecoderStress_Object = MibTableColumn
mnPrPerfBaseDecoderStress = _MnPrPerfBaseDecoderStress_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 14),
    _MnPrPerfBaseDecoderStress_Type()
)
mnPrPerfBaseDecoderStress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseDecoderStress.setStatus("mandatory")
_MnPrPerfBaseAcmTxProfile_Type = DisplayString
_MnPrPerfBaseAcmTxProfile_Object = MibTableColumn
mnPrPerfBaseAcmTxProfile = _MnPrPerfBaseAcmTxProfile_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 15),
    _MnPrPerfBaseAcmTxProfile_Type()
)
mnPrPerfBaseAcmTxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseAcmTxProfile.setStatus("mandatory")
_MnPrPerfBaseAcmRxProfile_Type = DisplayString
_MnPrPerfBaseAcmRxProfile_Object = MibTableColumn
mnPrPerfBaseAcmRxProfile = _MnPrPerfBaseAcmRxProfile_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 16),
    _MnPrPerfBaseAcmRxProfile_Type()
)
mnPrPerfBaseAcmRxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseAcmRxProfile.setStatus("mandatory")
_MnPrPerfBaseLinkCapMbps_Type = Integer32
_MnPrPerfBaseLinkCapMbps_Object = MibTableColumn
mnPrPerfBaseLinkCapMbps = _MnPrPerfBaseLinkCapMbps_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 17),
    _MnPrPerfBaseLinkCapMbps_Type()
)
mnPrPerfBaseLinkCapMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseLinkCapMbps.setStatus("mandatory")
_MnPrPerfBaseRxEtherMbps_Type = DisplayString
_MnPrPerfBaseRxEtherMbps_Object = MibTableColumn
mnPrPerfBaseRxEtherMbps = _MnPrPerfBaseRxEtherMbps_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 18),
    _MnPrPerfBaseRxEtherMbps_Type()
)
mnPrPerfBaseRxEtherMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseRxEtherMbps.setStatus("mandatory")
_MnPrPerfBaseDemodErrBlocks_Type = Display64
_MnPrPerfBaseDemodErrBlocks_Object = MibTableColumn
mnPrPerfBaseDemodErrBlocks = _MnPrPerfBaseDemodErrBlocks_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 19),
    _MnPrPerfBaseDemodErrBlocks_Type()
)
mnPrPerfBaseDemodErrBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseDemodErrBlocks.setStatus("mandatory")
_MnPrPerfBaseRFUTemp_Type = Integer32
_MnPrPerfBaseRFUTemp_Object = MibTableColumn
mnPrPerfBaseRFUTemp = _MnPrPerfBaseRFUTemp_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 20),
    _MnPrPerfBaseRFUTemp_Type()
)
mnPrPerfBaseRFUTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseRFUTemp.setStatus("mandatory")


class _MnPrPerfBaseRSL1_Type(Integer32):
    """Custom type mnPrPerfBaseRSL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_MnPrPerfBaseRSL1_Type.__name__ = "Integer32"
_MnPrPerfBaseRSL1_Object = MibTableColumn
mnPrPerfBaseRSL1 = _MnPrPerfBaseRSL1_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 21),
    _MnPrPerfBaseRSL1_Type()
)
mnPrPerfBaseRSL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseRSL1.setStatus("mandatory")


class _MnPrPerfBaseRSL2_Type(Integer32):
    """Custom type mnPrPerfBaseRSL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_MnPrPerfBaseRSL2_Type.__name__ = "Integer32"
_MnPrPerfBaseRSL2_Object = MibTableColumn
mnPrPerfBaseRSL2 = _MnPrPerfBaseRSL2_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 1, 1, 22),
    _MnPrPerfBaseRSL2_Type()
)
mnPrPerfBaseRSL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfBaseRSL2.setStatus("mandatory")
_MnPrPerfSumIntTable_Object = MibTable
mnPrPerfSumIntTable = _MnPrPerfSumIntTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 2)
)
if mibBuilder.loadTexts:
    mnPrPerfSumIntTable.setStatus("mandatory")
_MnPrPerfSumIntEntry_Object = MibTableRow
mnPrPerfSumIntEntry = _MnPrPerfSumIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 2, 1)
)
mnPrPerfSumIntEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnInterfaceIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnIntervalIndex"),
)
if mibBuilder.loadTexts:
    mnPrPerfSumIntEntry.setStatus("mandatory")


class _MnIntervalIndex_Type(Integer32):
    """Custom type mnIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("lastSecond", 1),
          ("lastMinute", 2),
          ("lastHour", 3),
          ("lastDay", 4),
          ("lastWeek", 5))
    )


_MnIntervalIndex_Type.__name__ = "Integer32"
_MnIntervalIndex_Object = MibTableColumn
mnIntervalIndex = _MnIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 2, 1, 1),
    _MnIntervalIndex_Type()
)
mnIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnIntervalIndex.setStatus("mandatory")
_MnPrPerfSumIntESs_Type = Counter32
_MnPrPerfSumIntESs_Object = MibTableColumn
mnPrPerfSumIntESs = _MnPrPerfSumIntESs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 2, 1, 2),
    _MnPrPerfSumIntESs_Type()
)
mnPrPerfSumIntESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfSumIntESs.setStatus("mandatory")
_MnPrPerfSumIntSESs_Type = Counter32
_MnPrPerfSumIntSESs_Object = MibTableColumn
mnPrPerfSumIntSESs = _MnPrPerfSumIntSESs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 2, 1, 3),
    _MnPrPerfSumIntSESs_Type()
)
mnPrPerfSumIntSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfSumIntSESs.setStatus("mandatory")
_MnPrPerfSumIntBER_Type = DisplayString
_MnPrPerfSumIntBER_Object = MibTableColumn
mnPrPerfSumIntBER = _MnPrPerfSumIntBER_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 2, 1, 4),
    _MnPrPerfSumIntBER_Type()
)
mnPrPerfSumIntBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfSumIntBER.setStatus("mandatory")
_MnPrPerfSumIntElapsedSecs_Type = Counter32
_MnPrPerfSumIntElapsedSecs_Object = MibTableColumn
mnPrPerfSumIntElapsedSecs = _MnPrPerfSumIntElapsedSecs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 2, 1, 5),
    _MnPrPerfSumIntElapsedSecs_Type()
)
mnPrPerfSumIntElapsedSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfSumIntElapsedSecs.setStatus("mandatory")
_MnPrPerfSumIntASs_Type = Counter32
_MnPrPerfSumIntASs_Object = MibTableColumn
mnPrPerfSumIntASs = _MnPrPerfSumIntASs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 2, 1, 6),
    _MnPrPerfSumIntASs_Type()
)
mnPrPerfSumIntASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfSumIntASs.setStatus("mandatory")
_MnPrPerfCustIntTable_Object = MibTable
mnPrPerfCustIntTable = _MnPrPerfCustIntTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3)
)
if mibBuilder.loadTexts:
    mnPrPerfCustIntTable.setStatus("mandatory")
_MnPrPerfCustIntEntry_Object = MibTableRow
mnPrPerfCustIntEntry = _MnPrPerfCustIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1)
)
mnPrPerfCustIntEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnInterfaceIndex"),
)
if mibBuilder.loadTexts:
    mnPrPerfCustIntEntry.setStatus("mandatory")
_MnPrPerfCustIntTxPowerAvg_Type = DisplayString
_MnPrPerfCustIntTxPowerAvg_Object = MibTableColumn
mnPrPerfCustIntTxPowerAvg = _MnPrPerfCustIntTxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 1),
    _MnPrPerfCustIntTxPowerAvg_Type()
)
mnPrPerfCustIntTxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntTxPowerAvg.setStatus("mandatory")


class _MnPrPerfCustIntTxPowerMax_Type(Integer32):
    """Custom type mnPrPerfCustIntTxPowerMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 30),
    )


_MnPrPerfCustIntTxPowerMax_Type.__name__ = "Integer32"
_MnPrPerfCustIntTxPowerMax_Object = MibTableColumn
mnPrPerfCustIntTxPowerMax = _MnPrPerfCustIntTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 2),
    _MnPrPerfCustIntTxPowerMax_Type()
)
mnPrPerfCustIntTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntTxPowerMax.setStatus("mandatory")


class _MnPrPerfCustIntTxPowerMin_Type(Integer32):
    """Custom type mnPrPerfCustIntTxPowerMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 30),
    )


_MnPrPerfCustIntTxPowerMin_Type.__name__ = "Integer32"
_MnPrPerfCustIntTxPowerMin_Object = MibTableColumn
mnPrPerfCustIntTxPowerMin = _MnPrPerfCustIntTxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 3),
    _MnPrPerfCustIntTxPowerMin_Type()
)
mnPrPerfCustIntTxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntTxPowerMin.setStatus("mandatory")
_MnPrPerfCustIntRSLAvg_Type = DisplayString
_MnPrPerfCustIntRSLAvg_Object = MibTableColumn
mnPrPerfCustIntRSLAvg = _MnPrPerfCustIntRSLAvg_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 4),
    _MnPrPerfCustIntRSLAvg_Type()
)
mnPrPerfCustIntRSLAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntRSLAvg.setStatus("mandatory")


class _MnPrPerfCustIntRSLMax_Type(Integer32):
    """Custom type mnPrPerfCustIntRSLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_MnPrPerfCustIntRSLMax_Type.__name__ = "Integer32"
_MnPrPerfCustIntRSLMax_Object = MibTableColumn
mnPrPerfCustIntRSLMax = _MnPrPerfCustIntRSLMax_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 5),
    _MnPrPerfCustIntRSLMax_Type()
)
mnPrPerfCustIntRSLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntRSLMax.setStatus("mandatory")


class _MnPrPerfCustIntRSLMin_Type(Integer32):
    """Custom type mnPrPerfCustIntRSLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_MnPrPerfCustIntRSLMin_Type.__name__ = "Integer32"
_MnPrPerfCustIntRSLMin_Object = MibTableColumn
mnPrPerfCustIntRSLMin = _MnPrPerfCustIntRSLMin_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 6),
    _MnPrPerfCustIntRSLMin_Type()
)
mnPrPerfCustIntRSLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntRSLMin.setStatus("mandatory")
_MnPrPerfCustIntElapsedSecs_Type = Counter32
_MnPrPerfCustIntElapsedSecs_Object = MibTableColumn
mnPrPerfCustIntElapsedSecs = _MnPrPerfCustIntElapsedSecs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 7),
    _MnPrPerfCustIntElapsedSecs_Type()
)
mnPrPerfCustIntElapsedSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntElapsedSecs.setStatus("mandatory")
_MnPrPerfCustIntASs_Type = Counter32
_MnPrPerfCustIntASs_Object = MibTableColumn
mnPrPerfCustIntASs = _MnPrPerfCustIntASs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 8),
    _MnPrPerfCustIntASs_Type()
)
mnPrPerfCustIntASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntASs.setStatus("mandatory")
_MnPrPerfCustIntUSs_Type = Counter32
_MnPrPerfCustIntUSs_Object = MibTableColumn
mnPrPerfCustIntUSs = _MnPrPerfCustIntUSs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 9),
    _MnPrPerfCustIntUSs_Type()
)
mnPrPerfCustIntUSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntUSs.setStatus("mandatory")
_MnPrPerfCustIntESs_Type = Counter32
_MnPrPerfCustIntESs_Object = MibTableColumn
mnPrPerfCustIntESs = _MnPrPerfCustIntESs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 10),
    _MnPrPerfCustIntESs_Type()
)
mnPrPerfCustIntESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntESs.setStatus("mandatory")
_MnPrPerfCustIntSESs_Type = Counter32
_MnPrPerfCustIntSESs_Object = MibTableColumn
mnPrPerfCustIntSESs = _MnPrPerfCustIntSESs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 11),
    _MnPrPerfCustIntSESs_Type()
)
mnPrPerfCustIntSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntSESs.setStatus("mandatory")
_MnPrPerfCustIntTotalBlocks_Type = Display64
_MnPrPerfCustIntTotalBlocks_Object = MibTableColumn
mnPrPerfCustIntTotalBlocks = _MnPrPerfCustIntTotalBlocks_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 12),
    _MnPrPerfCustIntTotalBlocks_Type()
)
mnPrPerfCustIntTotalBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntTotalBlocks.setStatus("mandatory")
_MnPrPerfCustIntErrBlocks_Type = Display64
_MnPrPerfCustIntErrBlocks_Object = MibTableColumn
mnPrPerfCustIntErrBlocks = _MnPrPerfCustIntErrBlocks_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 13),
    _MnPrPerfCustIntErrBlocks_Type()
)
mnPrPerfCustIntErrBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntErrBlocks.setStatus("mandatory")
_MnPrPerfCustIntBBEs_Type = Display64
_MnPrPerfCustIntBBEs_Object = MibTableColumn
mnPrPerfCustIntBBEs = _MnPrPerfCustIntBBEs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 14),
    _MnPrPerfCustIntBBEs_Type()
)
mnPrPerfCustIntBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntBBEs.setStatus("mandatory")
_MnPrPerfCustIntESRatio_Type = DisplayString
_MnPrPerfCustIntESRatio_Object = MibTableColumn
mnPrPerfCustIntESRatio = _MnPrPerfCustIntESRatio_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 15),
    _MnPrPerfCustIntESRatio_Type()
)
mnPrPerfCustIntESRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntESRatio.setStatus("mandatory")
_MnPrPerfCustIntSESRatio_Type = DisplayString
_MnPrPerfCustIntSESRatio_Object = MibTableColumn
mnPrPerfCustIntSESRatio = _MnPrPerfCustIntSESRatio_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 16),
    _MnPrPerfCustIntSESRatio_Type()
)
mnPrPerfCustIntSESRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntSESRatio.setStatus("mandatory")
_MnPrPerfCustIntBER_Type = DisplayString
_MnPrPerfCustIntBER_Object = MibTableColumn
mnPrPerfCustIntBER = _MnPrPerfCustIntBER_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 17),
    _MnPrPerfCustIntBER_Type()
)
mnPrPerfCustIntBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntBER.setStatus("mandatory")
_MnPrPerfCustIntBBER_Type = DisplayString
_MnPrPerfCustIntBBER_Object = MibTableColumn
mnPrPerfCustIntBBER = _MnPrPerfCustIntBBER_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 3, 1, 18),
    _MnPrPerfCustIntBBER_Type()
)
mnPrPerfCustIntBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfCustIntBBER.setStatus("mandatory")
_MnPrPerfHistObjects_ObjectIdentity = ObjectIdentity
mnPrPerfHistObjects = _MnPrPerfHistObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4)
)
_MnPrPerfHistTable_Object = MibTable
mnPrPerfHistTable = _MnPrPerfHistTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    mnPrPerfHistTable.setStatus("mandatory")
_MnPrPerfHistEntry_Object = MibTableRow
mnPrPerfHistEntry = _MnPrPerfHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1)
)
mnPrPerfHistEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnInterfaceIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrPerfHistIndex"),
)
if mibBuilder.loadTexts:
    mnPrPerfHistEntry.setStatus("mandatory")


class _MnPrPerfHistIndex_Type(Integer32):
    """Custom type mnPrPerfHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_MnPrPerfHistIndex_Type.__name__ = "Integer32"
_MnPrPerfHistIndex_Object = MibTableColumn
mnPrPerfHistIndex = _MnPrPerfHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 1),
    _MnPrPerfHistIndex_Type()
)
mnPrPerfHistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistIndex.setStatus("mandatory")
_MnPrPerfHistTimestamp_Type = DateAndTime
_MnPrPerfHistTimestamp_Object = MibTableColumn
mnPrPerfHistTimestamp = _MnPrPerfHistTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 2),
    _MnPrPerfHistTimestamp_Type()
)
mnPrPerfHistTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistTimestamp.setStatus("mandatory")
_MnPrPerfHistElapsedSecs_Type = Counter32
_MnPrPerfHistElapsedSecs_Object = MibTableColumn
mnPrPerfHistElapsedSecs = _MnPrPerfHistElapsedSecs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 3),
    _MnPrPerfHistElapsedSecs_Type()
)
mnPrPerfHistElapsedSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistElapsedSecs.setStatus("mandatory")
_MnPrPerfHistDowntime_Type = Counter32
_MnPrPerfHistDowntime_Object = MibTableColumn
mnPrPerfHistDowntime = _MnPrPerfHistDowntime_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 4),
    _MnPrPerfHistDowntime_Type()
)
mnPrPerfHistDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistDowntime.setStatus("mandatory")
_MnPrPerfHistASs_Type = Counter32
_MnPrPerfHistASs_Object = MibTableColumn
mnPrPerfHistASs = _MnPrPerfHistASs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 5),
    _MnPrPerfHistASs_Type()
)
mnPrPerfHistASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistASs.setStatus("mandatory")
_MnPrPerfHistUSs_Type = Counter32
_MnPrPerfHistUSs_Object = MibTableColumn
mnPrPerfHistUSs = _MnPrPerfHistUSs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 6),
    _MnPrPerfHistUSs_Type()
)
mnPrPerfHistUSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistUSs.setStatus("mandatory")
_MnPrPerfHistESs_Type = Counter32
_MnPrPerfHistESs_Object = MibTableColumn
mnPrPerfHistESs = _MnPrPerfHistESs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 7),
    _MnPrPerfHistESs_Type()
)
mnPrPerfHistESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistESs.setStatus("mandatory")
_MnPrPerfHistSESs_Type = Counter32
_MnPrPerfHistSESs_Object = MibTableColumn
mnPrPerfHistSESs = _MnPrPerfHistSESs_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 8),
    _MnPrPerfHistSESs_Type()
)
mnPrPerfHistSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistSESs.setStatus("mandatory")
_MnPrPerfHistTotalBlocks_Type = Display64
_MnPrPerfHistTotalBlocks_Object = MibTableColumn
mnPrPerfHistTotalBlocks = _MnPrPerfHistTotalBlocks_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 9),
    _MnPrPerfHistTotalBlocks_Type()
)
mnPrPerfHistTotalBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistTotalBlocks.setStatus("mandatory")
_MnPrPerfHistErrBlocks_Type = Display64
_MnPrPerfHistErrBlocks_Object = MibTableColumn
mnPrPerfHistErrBlocks = _MnPrPerfHistErrBlocks_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 10),
    _MnPrPerfHistErrBlocks_Type()
)
mnPrPerfHistErrBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistErrBlocks.setStatus("mandatory")
_MnPrPerfHistErrBackBlocks_Type = Display64
_MnPrPerfHistErrBackBlocks_Object = MibTableColumn
mnPrPerfHistErrBackBlocks = _MnPrPerfHistErrBackBlocks_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 11),
    _MnPrPerfHistErrBackBlocks_Type()
)
mnPrPerfHistErrBackBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistErrBackBlocks.setStatus("mandatory")
_MnPrPerfHistTotalBytes_Type = Display64
_MnPrPerfHistTotalBytes_Object = MibTableColumn
mnPrPerfHistTotalBytes = _MnPrPerfHistTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 12),
    _MnPrPerfHistTotalBytes_Type()
)
mnPrPerfHistTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistTotalBytes.setStatus("mandatory")
_MnPrPerfHistErrBytes_Type = Display64
_MnPrPerfHistErrBytes_Object = MibTableColumn
mnPrPerfHistErrBytes = _MnPrPerfHistErrBytes_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 13),
    _MnPrPerfHistErrBytes_Type()
)
mnPrPerfHistErrBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistErrBytes.setStatus("mandatory")
_MnPrPerfHistTotalBackBytes_Type = Display64
_MnPrPerfHistTotalBackBytes_Object = MibTableColumn
mnPrPerfHistTotalBackBytes = _MnPrPerfHistTotalBackBytes_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 14),
    _MnPrPerfHistTotalBackBytes_Type()
)
mnPrPerfHistTotalBackBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistTotalBackBytes.setStatus("mandatory")
_MnPrPerfHistErrBackBytes_Type = Display64
_MnPrPerfHistErrBackBytes_Object = MibTableColumn
mnPrPerfHistErrBackBytes = _MnPrPerfHistErrBackBytes_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 15),
    _MnPrPerfHistErrBackBytes_Type()
)
mnPrPerfHistErrBackBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistErrBackBytes.setStatus("mandatory")
_MnPrPerfHistESRatio_Type = DisplayString
_MnPrPerfHistESRatio_Object = MibTableColumn
mnPrPerfHistESRatio = _MnPrPerfHistESRatio_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 16),
    _MnPrPerfHistESRatio_Type()
)
mnPrPerfHistESRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistESRatio.setStatus("mandatory")
_MnPrPerfHistSESRatio_Type = DisplayString
_MnPrPerfHistSESRatio_Object = MibTableColumn
mnPrPerfHistSESRatio = _MnPrPerfHistSESRatio_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 17),
    _MnPrPerfHistSESRatio_Type()
)
mnPrPerfHistSESRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistSESRatio.setStatus("mandatory")
_MnPrPerfHistBER_Type = DisplayString
_MnPrPerfHistBER_Object = MibTableColumn
mnPrPerfHistBER = _MnPrPerfHistBER_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 18),
    _MnPrPerfHistBER_Type()
)
mnPrPerfHistBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistBER.setStatus("mandatory")
_MnPrPerfHistBBER_Type = DisplayString
_MnPrPerfHistBBER_Object = MibTableColumn
mnPrPerfHistBBER = _MnPrPerfHistBBER_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 19),
    _MnPrPerfHistBBER_Type()
)
mnPrPerfHistBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistBBER.setStatus("mandatory")


class _MnPrPerfHistTxPower_Type(Integer32):
    """Custom type mnPrPerfHistTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 30),
    )


_MnPrPerfHistTxPower_Type.__name__ = "Integer32"
_MnPrPerfHistTxPower_Object = MibTableColumn
mnPrPerfHistTxPower = _MnPrPerfHistTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 20),
    _MnPrPerfHistTxPower_Type()
)
mnPrPerfHistTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistTxPower.setStatus("mandatory")


class _MnPrPerfHistTxPowerMin_Type(Integer32):
    """Custom type mnPrPerfHistTxPowerMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 30),
    )


_MnPrPerfHistTxPowerMin_Type.__name__ = "Integer32"
_MnPrPerfHistTxPowerMin_Object = MibTableColumn
mnPrPerfHistTxPowerMin = _MnPrPerfHistTxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 21),
    _MnPrPerfHistTxPowerMin_Type()
)
mnPrPerfHistTxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistTxPowerMin.setStatus("mandatory")


class _MnPrPerfHistTxPowerMax_Type(Integer32):
    """Custom type mnPrPerfHistTxPowerMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 30),
    )


_MnPrPerfHistTxPowerMax_Type.__name__ = "Integer32"
_MnPrPerfHistTxPowerMax_Object = MibTableColumn
mnPrPerfHistTxPowerMax = _MnPrPerfHistTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 22),
    _MnPrPerfHistTxPowerMax_Type()
)
mnPrPerfHistTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistTxPowerMax.setStatus("mandatory")
_MnPrPerfHistTxPowerAvg_Type = DisplayString
_MnPrPerfHistTxPowerAvg_Object = MibTableColumn
mnPrPerfHistTxPowerAvg = _MnPrPerfHistTxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 23),
    _MnPrPerfHistTxPowerAvg_Type()
)
mnPrPerfHistTxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistTxPowerAvg.setStatus("mandatory")


class _MnPrPerfHistRSL_Type(Integer32):
    """Custom type mnPrPerfHistRSL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_MnPrPerfHistRSL_Type.__name__ = "Integer32"
_MnPrPerfHistRSL_Object = MibTableColumn
mnPrPerfHistRSL = _MnPrPerfHistRSL_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 24),
    _MnPrPerfHistRSL_Type()
)
mnPrPerfHistRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistRSL.setStatus("mandatory")


class _MnPrPerfHistRSLMin_Type(Integer32):
    """Custom type mnPrPerfHistRSLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_MnPrPerfHistRSLMin_Type.__name__ = "Integer32"
_MnPrPerfHistRSLMin_Object = MibTableColumn
mnPrPerfHistRSLMin = _MnPrPerfHistRSLMin_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 25),
    _MnPrPerfHistRSLMin_Type()
)
mnPrPerfHistRSLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistRSLMin.setStatus("mandatory")


class _MnPrPerfHistRSLMax_Type(Integer32):
    """Custom type mnPrPerfHistRSLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_MnPrPerfHistRSLMax_Type.__name__ = "Integer32"
_MnPrPerfHistRSLMax_Object = MibTableColumn
mnPrPerfHistRSLMax = _MnPrPerfHistRSLMax_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 26),
    _MnPrPerfHistRSLMax_Type()
)
mnPrPerfHistRSLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistRSLMax.setStatus("mandatory")
_MnPrPerfHistRSLAvg_Type = DisplayString
_MnPrPerfHistRSLAvg_Object = MibTableColumn
mnPrPerfHistRSLAvg = _MnPrPerfHistRSLAvg_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 27),
    _MnPrPerfHistRSLAvg_Type()
)
mnPrPerfHistRSLAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistRSLAvg.setStatus("mandatory")
_MnPrPerfHistAlarmBMP_Type = Display64
_MnPrPerfHistAlarmBMP_Object = MibTableColumn
mnPrPerfHistAlarmBMP = _MnPrPerfHistAlarmBMP_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 1, 1, 28),
    _MnPrPerfHistAlarmBMP_Type()
)
mnPrPerfHistAlarmBMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistAlarmBMP.setStatus("mandatory")
_MnPrPerfHistCsvHdrTable_Object = MibTable
mnPrPerfHistCsvHdrTable = _MnPrPerfHistCsvHdrTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    mnPrPerfHistCsvHdrTable.setStatus("mandatory")
_MnPrPerfHistCsvHdrEntry_Object = MibTableRow
mnPrPerfHistCsvHdrEntry = _MnPrPerfHistCsvHdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 2, 1)
)
mnPrPerfHistCsvHdrEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnInterfaceIndex"),
)
if mibBuilder.loadTexts:
    mnPrPerfHistCsvHdrEntry.setStatus("mandatory")
_MnPrPerfHistCsvHdr_Type = DisplayString
_MnPrPerfHistCsvHdr_Object = MibTableColumn
mnPrPerfHistCsvHdr = _MnPrPerfHistCsvHdr_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 2, 1, 1),
    _MnPrPerfHistCsvHdr_Type()
)
mnPrPerfHistCsvHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistCsvHdr.setStatus("mandatory")
_MnPrPerfHistCsvDataTable_Object = MibTable
mnPrPerfHistCsvDataTable = _MnPrPerfHistCsvDataTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 3)
)
if mibBuilder.loadTexts:
    mnPrPerfHistCsvDataTable.setStatus("mandatory")
_MnPrPerfHistCsvDataEntry_Object = MibTableRow
mnPrPerfHistCsvDataEntry = _MnPrPerfHistCsvDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 3, 1)
)
mnPrPerfHistCsvDataEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnInterfaceIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrPerfHistIndex"),
)
if mibBuilder.loadTexts:
    mnPrPerfHistCsvDataEntry.setStatus("mandatory")
_MnPrPerfHistCsvData_Type = DisplayString
_MnPrPerfHistCsvData_Object = MibTableColumn
mnPrPerfHistCsvData = _MnPrPerfHistCsvData_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 4, 4, 3, 1, 1),
    _MnPrPerfHistCsvData_Type()
)
mnPrPerfHistCsvData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistCsvData.setStatus("mandatory")
_MnPrControlObjects_ObjectIdentity = ObjectIdentity
mnPrControlObjects = _MnPrControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5)
)
_MnPrRadCtlTable_Object = MibTable
mnPrRadCtlTable = _MnPrRadCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mnPrRadCtlTable.setStatus("mandatory")
_MnPrRadCtlEntry_Object = MibTableRow
mnPrRadCtlEntry = _MnPrRadCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 1, 1)
)
mnPrRadCtlEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
)
if mibBuilder.loadTexts:
    mnPrRadCtlEntry.setStatus("mandatory")
_MnPrRadCtlDigAggLoopback_Type = TruthValue
_MnPrRadCtlDigAggLoopback_Object = MibTableColumn
mnPrRadCtlDigAggLoopback = _MnPrRadCtlDigAggLoopback_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 1, 1, 1),
    _MnPrRadCtlDigAggLoopback_Type()
)
mnPrRadCtlDigAggLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRadCtlDigAggLoopback.setStatus("mandatory")


class _MnPrRadCtlBERTTxPattern_Type(Integer32):
    """Custom type mnPrRadCtlBERTTxPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableBERT", 1),
          ("pseudoRandomNumber", 2))
    )


_MnPrRadCtlBERTTxPattern_Type.__name__ = "Integer32"
_MnPrRadCtlBERTTxPattern_Object = MibTableColumn
mnPrRadCtlBERTTxPattern = _MnPrRadCtlBERTTxPattern_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 1, 1, 2),
    _MnPrRadCtlBERTTxPattern_Type()
)
mnPrRadCtlBERTTxPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRadCtlBERTTxPattern.setStatus("mandatory")
_MnPrRadCtlBERTTimeString_Type = DisplayString
_MnPrRadCtlBERTTimeString_Object = MibTableColumn
mnPrRadCtlBERTTimeString = _MnPrRadCtlBERTTimeString_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 1, 1, 3),
    _MnPrRadCtlBERTTimeString_Type()
)
mnPrRadCtlBERTTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadCtlBERTTimeString.setStatus("mandatory")
_MnPrRadCtlBERTTotal_Type = Display64
_MnPrRadCtlBERTTotal_Object = MibTableColumn
mnPrRadCtlBERTTotal = _MnPrRadCtlBERTTotal_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 1, 1, 4),
    _MnPrRadCtlBERTTotal_Type()
)
mnPrRadCtlBERTTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadCtlBERTTotal.setStatus("mandatory")
_MnPrRadCtlBERTErrors_Type = Display64
_MnPrRadCtlBERTErrors_Object = MibTableColumn
mnPrRadCtlBERTErrors = _MnPrRadCtlBERTErrors_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 1, 1, 5),
    _MnPrRadCtlBERTErrors_Type()
)
mnPrRadCtlBERTErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadCtlBERTErrors.setStatus("mandatory")
_MnPrRadCtlBERTBER_Type = DisplayString
_MnPrRadCtlBERTBER_Object = MibTableColumn
mnPrRadCtlBERTBER = _MnPrRadCtlBERTBER_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 1, 1, 6),
    _MnPrRadCtlBERTBER_Type()
)
mnPrRadCtlBERTBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRadCtlBERTBER.setStatus("mandatory")


class _MnPrRadCtrDigAggLoopTime_Type(Integer32):
    """Custom type mnPrRadCtrDigAggLoopTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MnPrRadCtrDigAggLoopTime_Type.__name__ = "Integer32"
_MnPrRadCtrDigAggLoopTime_Object = MibTableColumn
mnPrRadCtrDigAggLoopTime = _MnPrRadCtrDigAggLoopTime_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 1, 1, 7),
    _MnPrRadCtrDigAggLoopTime_Type()
)
mnPrRadCtrDigAggLoopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRadCtrDigAggLoopTime.setStatus("mandatory")
_MnPrRadCtlODUMute_Type = TruthValue
_MnPrRadCtlODUMute_Object = MibTableColumn
mnPrRadCtlODUMute = _MnPrRadCtlODUMute_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 1, 1, 8),
    _MnPrRadCtlODUMute_Type()
)
mnPrRadCtlODUMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRadCtlODUMute.setStatus("mandatory")


class _MnPrRadCtlODUMuteTime_Type(Integer32):
    """Custom type mnPrRadCtlODUMuteTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MnPrRadCtlODUMuteTime_Type.__name__ = "Integer32"
_MnPrRadCtlODUMuteTime_Object = MibTableColumn
mnPrRadCtlODUMuteTime = _MnPrRadCtlODUMuteTime_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 1, 1, 9),
    _MnPrRadCtlODUMuteTime_Type()
)
mnPrRadCtlODUMuteTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRadCtlODUMuteTime.setStatus("mandatory")
_MnPrLIMCtlTable_Object = MibTable
mnPrLIMCtlTable = _MnPrLIMCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 2)
)
if mibBuilder.loadTexts:
    mnPrLIMCtlTable.setStatus("mandatory")
_MnPrLIMCtlEntry_Object = MibTableRow
mnPrLIMCtlEntry = _MnPrLIMCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 2, 1)
)
mnPrLIMCtlEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnLIMIndex"),
)
if mibBuilder.loadTexts:
    mnPrLIMCtlEntry.setStatus("mandatory")


class _MnLIMIndex_Type(Integer32):
    """Custom type mnLIMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_MnLIMIndex_Type.__name__ = "Integer32"
_MnLIMIndex_Object = MibTableColumn
mnLIMIndex = _MnLIMIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 2, 1, 1),
    _MnLIMIndex_Type()
)
mnLIMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnLIMIndex.setStatus("mandatory")


class _MnPrLIMCtlBERTTrib_Type(Integer32):
    """Custom type mnPrLIMCtlBERTTrib based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_MnPrLIMCtlBERTTrib_Type.__name__ = "Integer32"
_MnPrLIMCtlBERTTrib_Object = MibTableColumn
mnPrLIMCtlBERTTrib = _MnPrLIMCtlBERTTrib_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 2, 1, 2),
    _MnPrLIMCtlBERTTrib_Type()
)
mnPrLIMCtlBERTTrib.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrLIMCtlBERTTrib.setStatus("mandatory")


class _MnPrLIMCtlBERTTxPattern_Type(Integer32):
    """Custom type mnPrLIMCtlBERTTxPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableBERT", 1),
          ("pseudoRandomNumber", 2))
    )


_MnPrLIMCtlBERTTxPattern_Type.__name__ = "Integer32"
_MnPrLIMCtlBERTTxPattern_Object = MibTableColumn
mnPrLIMCtlBERTTxPattern = _MnPrLIMCtlBERTTxPattern_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 2, 1, 3),
    _MnPrLIMCtlBERTTxPattern_Type()
)
mnPrLIMCtlBERTTxPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrLIMCtlBERTTxPattern.setStatus("mandatory")
_MnPrLIMCtlBERTTimeString_Type = DisplayString
_MnPrLIMCtlBERTTimeString_Object = MibTableColumn
mnPrLIMCtlBERTTimeString = _MnPrLIMCtlBERTTimeString_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 2, 1, 4),
    _MnPrLIMCtlBERTTimeString_Type()
)
mnPrLIMCtlBERTTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLIMCtlBERTTimeString.setStatus("mandatory")
_MnPrLIMCtlBERTTotal_Type = Display64
_MnPrLIMCtlBERTTotal_Object = MibTableColumn
mnPrLIMCtlBERTTotal = _MnPrLIMCtlBERTTotal_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 2, 1, 5),
    _MnPrLIMCtlBERTTotal_Type()
)
mnPrLIMCtlBERTTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLIMCtlBERTTotal.setStatus("mandatory")
_MnPrLIMCtlBERTErrors_Type = Display64
_MnPrLIMCtlBERTErrors_Object = MibTableColumn
mnPrLIMCtlBERTErrors = _MnPrLIMCtlBERTErrors_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 2, 1, 6),
    _MnPrLIMCtlBERTErrors_Type()
)
mnPrLIMCtlBERTErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLIMCtlBERTErrors.setStatus("mandatory")
_MnPrLIMCtlBERTBER_Type = DisplayString
_MnPrLIMCtlBERTBER_Object = MibTableColumn
mnPrLIMCtlBERTBER = _MnPrLIMCtlBERTBER_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 2, 1, 7),
    _MnPrLIMCtlBERTBER_Type()
)
mnPrLIMCtlBERTBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLIMCtlBERTBER.setStatus("mandatory")
_MnPrTribCtlTable_Object = MibTable
mnPrTribCtlTable = _MnPrTribCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 3)
)
if mibBuilder.loadTexts:
    mnPrTribCtlTable.setStatus("mandatory")
_MnPrTribCtlEntry_Object = MibTableRow
mnPrTribCtlEntry = _MnPrTribCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 3, 1)
)
mnPrTribCtlEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnTribIndex"),
)
if mibBuilder.loadTexts:
    mnPrTribCtlEntry.setStatus("mandatory")


class _MnTribIndex_Type(Integer32):
    """Custom type mnTribIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_MnTribIndex_Type.__name__ = "Integer32"
_MnTribIndex_Object = MibTableColumn
mnTribIndex = _MnTribIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 3, 1, 1),
    _MnTribIndex_Type()
)
mnTribIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnTribIndex.setStatus("mandatory")
_MnPrTribCtlLocalLoopback_Type = TruthValue
_MnPrTribCtlLocalLoopback_Object = MibTableColumn
mnPrTribCtlLocalLoopback = _MnPrTribCtlLocalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 3, 1, 2),
    _MnPrTribCtlLocalLoopback_Type()
)
mnPrTribCtlLocalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrTribCtlLocalLoopback.setStatus("mandatory")
_MnPrTribCtlRemoteLoopback_Type = TruthValue
_MnPrTribCtlRemoteLoopback_Object = MibTableColumn
mnPrTribCtlRemoteLoopback = _MnPrTribCtlRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 5, 3, 1, 3),
    _MnPrTribCtlRemoteLoopback_Type()
)
mnPrTribCtlRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrTribCtlRemoteLoopback.setStatus("mandatory")
_MnPrConfigurationObjects_ObjectIdentity = ObjectIdentity
mnPrConfigurationObjects = _MnPrConfigurationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6)
)
_MnPrInventTable_Object = MibTable
mnPrInventTable = _MnPrInventTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 1)
)
if mibBuilder.loadTexts:
    mnPrInventTable.setStatus("mandatory")
_MnPrInventEntry_Object = MibTableRow
mnPrInventEntry = _MnPrInventEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 1, 1)
)
mnPrInventEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrInventCompIndex"),
)
if mibBuilder.loadTexts:
    mnPrInventEntry.setStatus("mandatory")


class _MnPrInventCompIndex_Type(Integer32):
    """Custom type mnPrInventCompIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_MnPrInventCompIndex_Type.__name__ = "Integer32"
_MnPrInventCompIndex_Object = MibTableColumn
mnPrInventCompIndex = _MnPrInventCompIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 1, 1, 1),
    _MnPrInventCompIndex_Type()
)
mnPrInventCompIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrInventCompIndex.setStatus("mandatory")
_MnPrInventCompText_Type = DisplayString
_MnPrInventCompText_Object = MibTableColumn
mnPrInventCompText = _MnPrInventCompText_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 1, 1, 2),
    _MnPrInventCompText_Type()
)
mnPrInventCompText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrInventCompText.setStatus("mandatory")
_MnPrInventModPartText_Type = DisplayString
_MnPrInventModPartText_Object = MibTableColumn
mnPrInventModPartText = _MnPrInventModPartText_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 1, 1, 3),
    _MnPrInventModPartText_Type()
)
mnPrInventModPartText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrInventModPartText.setStatus("mandatory")
_MnPrInventCheckSumText_Type = DisplayString
_MnPrInventCheckSumText_Object = MibTableColumn
mnPrInventCheckSumText = _MnPrInventCheckSumText_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 1, 1, 4),
    _MnPrInventCheckSumText_Type()
)
mnPrInventCheckSumText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrInventCheckSumText.setStatus("mandatory")
_MnPrInventVersionText_Type = DisplayString
_MnPrInventVersionText_Object = MibTableColumn
mnPrInventVersionText = _MnPrInventVersionText_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 1, 1, 5),
    _MnPrInventVersionText_Type()
)
mnPrInventVersionText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrInventVersionText.setStatus("mandatory")
_MnPrInventSerialText_Type = DisplayString
_MnPrInventSerialText_Object = MibTableColumn
mnPrInventSerialText = _MnPrInventSerialText_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 1, 1, 7),
    _MnPrInventSerialText_Type()
)
mnPrInventSerialText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrInventSerialText.setStatus("mandatory")


class _MnPrInventCompStatus_Type(Integer32):
    """Custom type mnPrInventCompStatus based on Integer32"""
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
          ("outOfService", 2),
          ("inService", 3))
    )


_MnPrInventCompStatus_Type.__name__ = "Integer32"
_MnPrInventCompStatus_Object = MibTableColumn
mnPrInventCompStatus = _MnPrInventCompStatus_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 1, 1, 8),
    _MnPrInventCompStatus_Type()
)
mnPrInventCompStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrInventCompStatus.setStatus("mandatory")
_MnPrInventCompType_Type = Integer32
_MnPrInventCompType_Object = MibTableColumn
mnPrInventCompType = _MnPrInventCompType_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 1, 1, 9),
    _MnPrInventCompType_Type()
)
mnPrInventCompType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrInventCompType.setStatus("mandatory")
_MnPrODUConfTable_Object = MibTable
mnPrODUConfTable = _MnPrODUConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 2)
)
if mibBuilder.loadTexts:
    mnPrODUConfTable.setStatus("mandatory")
_MnPrODUConfEntry_Object = MibTableRow
mnPrODUConfEntry = _MnPrODUConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 2, 1)
)
mnPrODUConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
)
if mibBuilder.loadTexts:
    mnPrODUConfEntry.setStatus("mandatory")
_MnPrODUConfTxFreq_Type = Integer32
_MnPrODUConfTxFreq_Object = MibTableColumn
mnPrODUConfTxFreq = _MnPrODUConfTxFreq_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 2, 1, 1),
    _MnPrODUConfTxFreq_Type()
)
mnPrODUConfTxFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrODUConfTxFreq.setStatus("mandatory")
_MnPrODUConfRxFreq_Type = Integer32
_MnPrODUConfRxFreq_Object = MibTableColumn
mnPrODUConfRxFreq = _MnPrODUConfRxFreq_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 2, 1, 2),
    _MnPrODUConfRxFreq_Type()
)
mnPrODUConfRxFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrODUConfRxFreq.setStatus("mandatory")
_MnPrODUConfTxPower_Type = Integer32
_MnPrODUConfTxPower_Object = MibTableColumn
mnPrODUConfTxPower = _MnPrODUConfTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 2, 1, 3),
    _MnPrODUConfTxPower_Type()
)
mnPrODUConfTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrODUConfTxPower.setStatus("mandatory")
_MnPrODUConfATPCEnable_Type = TruthValue
_MnPrODUConfATPCEnable_Object = MibTableColumn
mnPrODUConfATPCEnable = _MnPrODUConfATPCEnable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 2, 1, 4),
    _MnPrODUConfATPCEnable_Type()
)
mnPrODUConfATPCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrODUConfATPCEnable.setStatus("mandatory")
_MnPrODUConfATPCTargetRSL_Type = Integer32
_MnPrODUConfATPCTargetRSL_Object = MibTableColumn
mnPrODUConfATPCTargetRSL = _MnPrODUConfATPCTargetRSL_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 2, 1, 5),
    _MnPrODUConfATPCTargetRSL_Type()
)
mnPrODUConfATPCTargetRSL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrODUConfATPCTargetRSL.setStatus("mandatory")
_MnPrODUConfMute_Type = TruthValue
_MnPrODUConfMute_Object = MibTableColumn
mnPrODUConfMute = _MnPrODUConfMute_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 2, 1, 6),
    _MnPrODUConfMute_Type()
)
mnPrODUConfMute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrODUConfMute.setStatus("mandatory")


class _MnPrODUConfCurInversion_Type(Integer32):
    """Custom type mnPrODUConfCurInversion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("defaultInversion", 1),
          ("noInversion", 2),
          ("invertRx", 3),
          ("invertTx", 4),
          ("invertBoth", 5))
    )


_MnPrODUConfCurInversion_Type.__name__ = "Integer32"
_MnPrODUConfCurInversion_Object = MibTableColumn
mnPrODUConfCurInversion = _MnPrODUConfCurInversion_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 2, 1, 7),
    _MnPrODUConfCurInversion_Type()
)
mnPrODUConfCurInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrODUConfCurInversion.setStatus("mandatory")


class _MnPrODUConfDefInversion_Type(Integer32):
    """Custom type mnPrODUConfDefInversion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noInversion", 2),
          ("invertRx", 3),
          ("invertTx", 4),
          ("invertBoth", 5))
    )


_MnPrODUConfDefInversion_Type.__name__ = "Integer32"
_MnPrODUConfDefInversion_Object = MibTableColumn
mnPrODUConfDefInversion = _MnPrODUConfDefInversion_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 2, 1, 8),
    _MnPrODUConfDefInversion_Type()
)
mnPrODUConfDefInversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrODUConfDefInversion.setStatus("mandatory")
_MnPrIDUConfTable_Object = MibTable
mnPrIDUConfTable = _MnPrIDUConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3)
)
if mibBuilder.loadTexts:
    mnPrIDUConfTable.setStatus("mandatory")
_MnPrIDUConfEntry_Object = MibTableRow
mnPrIDUConfEntry = _MnPrIDUConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1)
)
mnPrIDUConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
)
if mibBuilder.loadTexts:
    mnPrIDUConfEntry.setStatus("mandatory")


class _MnPrIDUConfProtMode_Type(Integer32):
    """Custom type mnPrIDUConfProtMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unprotected", 1),
          ("hotStandbyProtected", 2),
          ("hsTXsdRX", 3),
          ("sdTXsdRX", 4),
          ("npTXsdRX", 5),
          ("fdTXfdRX", 6))
    )


_MnPrIDUConfProtMode_Type.__name__ = "Integer32"
_MnPrIDUConfProtMode_Object = MibTableColumn
mnPrIDUConfProtMode = _MnPrIDUConfProtMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 1),
    _MnPrIDUConfProtMode_Type()
)
mnPrIDUConfProtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfProtMode.setStatus("mandatory")
_MnPrIDUConfProtOnlineRequest_Type = TruthValue
_MnPrIDUConfProtOnlineRequest_Object = MibTableColumn
mnPrIDUConfProtOnlineRequest = _MnPrIDUConfProtOnlineRequest_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 2),
    _MnPrIDUConfProtOnlineRequest_Type()
)
mnPrIDUConfProtOnlineRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfProtOnlineRequest.setStatus("mandatory")


class _MnPrIDUConfOrderwireCode_Type(DisplayString):
    """Custom type mnPrIDUConfOrderwireCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_MnPrIDUConfOrderwireCode_Type.__name__ = "DisplayString"
_MnPrIDUConfOrderwireCode_Object = MibTableColumn
mnPrIDUConfOrderwireCode = _MnPrIDUConfOrderwireCode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 3),
    _MnPrIDUConfOrderwireCode_Type()
)
mnPrIDUConfOrderwireCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfOrderwireCode.setStatus("mandatory")


class _MnPrIDUConfOrderwireMode_Type(Integer32):
    """Custom type mnPrIDUConfOrderwireMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voice", 1),
          ("data", 2))
    )


_MnPrIDUConfOrderwireMode_Type.__name__ = "Integer32"
_MnPrIDUConfOrderwireMode_Object = MibTableColumn
mnPrIDUConfOrderwireMode = _MnPrIDUConfOrderwireMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 4),
    _MnPrIDUConfOrderwireMode_Type()
)
mnPrIDUConfOrderwireMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfOrderwireMode.setStatus("mandatory")


class _MnPrIDUConfAUX1Rate_Type(Integer32):
    """Custom type mnPrIDUConfAUX1Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("baud9600", 9600),
          ("baud19200", 19200))
    )


_MnPrIDUConfAUX1Rate_Type.__name__ = "Integer32"
_MnPrIDUConfAUX1Rate_Object = MibTableColumn
mnPrIDUConfAUX1Rate = _MnPrIDUConfAUX1Rate_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 5),
    _MnPrIDUConfAUX1Rate_Type()
)
mnPrIDUConfAUX1Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfAUX1Rate.setStatus("mandatory")


class _MnPrIDUConfAUX2Rate_Type(Integer32):
    """Custom type mnPrIDUConfAUX2Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("baud9600", 9600),
          ("baud19200", 19200))
    )


_MnPrIDUConfAUX2Rate_Type.__name__ = "Integer32"
_MnPrIDUConfAUX2Rate_Object = MibTableColumn
mnPrIDUConfAUX2Rate = _MnPrIDUConfAUX2Rate_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 6),
    _MnPrIDUConfAUX2Rate_Type()
)
mnPrIDUConfAUX2Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfAUX2Rate.setStatus("mandatory")


class _MnPrIDUConfCraftBaud_Type(Integer32):
    """Custom type mnPrIDUConfCraftBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9600,
              19200,
              38400,
              57600)
        )
    )
    namedValues = NamedValues(
        *(("baud9600", 9600),
          ("baud19200", 19200),
          ("baud38400", 38400),
          ("baud57600", 57600))
    )


_MnPrIDUConfCraftBaud_Type.__name__ = "Integer32"
_MnPrIDUConfCraftBaud_Object = MibTableColumn
mnPrIDUConfCraftBaud = _MnPrIDUConfCraftBaud_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 7),
    _MnPrIDUConfCraftBaud_Type()
)
mnPrIDUConfCraftBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfCraftBaud.setStatus("mandatory")


class _MnPrIDUConfProposedCapacity_Type(Integer32):
    """Custom type mnPrIDUConfProposedCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MnPrIDUConfProposedCapacity_Type.__name__ = "Integer32"
_MnPrIDUConfProposedCapacity_Object = MibTableColumn
mnPrIDUConfProposedCapacity = _MnPrIDUConfProposedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 8),
    _MnPrIDUConfProposedCapacity_Type()
)
mnPrIDUConfProposedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrIDUConfProposedCapacity.setStatus("mandatory")


class _MnPrIDUConfAllocateLimA_Type(Integer32):
    """Custom type mnPrIDUConfAllocateLimA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MnPrIDUConfAllocateLimA_Type.__name__ = "Integer32"
_MnPrIDUConfAllocateLimA_Object = MibTableColumn
mnPrIDUConfAllocateLimA = _MnPrIDUConfAllocateLimA_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 9),
    _MnPrIDUConfAllocateLimA_Type()
)
mnPrIDUConfAllocateLimA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfAllocateLimA.setStatus("mandatory")
_MnPrIDUConfProtTwinAddress_Type = IpAddress
_MnPrIDUConfProtTwinAddress_Object = MibTableColumn
mnPrIDUConfProtTwinAddress = _MnPrIDUConfProtTwinAddress_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 10),
    _MnPrIDUConfProtTwinAddress_Type()
)
mnPrIDUConfProtTwinAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfProtTwinAddress.setStatus("mandatory")
_MnPrIDUConfIFBandwidthProposed_Type = IfBandwidth
_MnPrIDUConfIFBandwidthProposed_Object = MibTableColumn
mnPrIDUConfIFBandwidthProposed = _MnPrIDUConfIFBandwidthProposed_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 11),
    _MnPrIDUConfIFBandwidthProposed_Type()
)
mnPrIDUConfIFBandwidthProposed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfIFBandwidthProposed.setStatus("mandatory")
_MnPrIDUConfIFBandwidthConf_Type = IfBandwidth
_MnPrIDUConfIFBandwidthConf_Object = MibTableColumn
mnPrIDUConfIFBandwidthConf = _MnPrIDUConfIFBandwidthConf_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 12),
    _MnPrIDUConfIFBandwidthConf_Type()
)
mnPrIDUConfIFBandwidthConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrIDUConfIFBandwidthConf.setStatus("mandatory")
_MnPrIDUConfNmsPortSpeed_Type = LanSpeed
_MnPrIDUConfNmsPortSpeed_Object = MibTableColumn
mnPrIDUConfNmsPortSpeed = _MnPrIDUConfNmsPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 13),
    _MnPrIDUConfNmsPortSpeed_Type()
)
mnPrIDUConfNmsPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfNmsPortSpeed.setStatus("mandatory")


class _MnPrIDUConfNmsPortMode_Type(Integer32):
    """Custom type mnPrIDUConfNmsPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgmtOutOfBand", 1),
          ("mgmtInBand", 2))
    )


_MnPrIDUConfNmsPortMode_Type.__name__ = "Integer32"
_MnPrIDUConfNmsPortMode_Object = MibTableColumn
mnPrIDUConfNmsPortMode = _MnPrIDUConfNmsPortMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 14),
    _MnPrIDUConfNmsPortMode_Type()
)
mnPrIDUConfNmsPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfNmsPortMode.setStatus("mandatory")
_MnPrIDUConfCapacityConf_Type = Integer32
_MnPrIDUConfCapacityConf_Object = MibTableColumn
mnPrIDUConfCapacityConf = _MnPrIDUConfCapacityConf_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 19),
    _MnPrIDUConfCapacityConf_Type()
)
mnPrIDUConfCapacityConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfCapacityConf.setStatus("mandatory")
_MnPrIDUConfCapacityProp_Type = Integer32
_MnPrIDUConfCapacityProp_Object = MibTableColumn
mnPrIDUConfCapacityProp = _MnPrIDUConfCapacityProp_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 20),
    _MnPrIDUConfCapacityProp_Type()
)
mnPrIDUConfCapacityProp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfCapacityProp.setStatus("mandatory")


class _MnPrIDUConfIntEthStatusInst_Type(Integer32):
    """Custom type mnPrIDUConfIntEthStatusInst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licensed", 1),
          ("unLicensed", 2))
    )


_MnPrIDUConfIntEthStatusInst_Type.__name__ = "Integer32"
_MnPrIDUConfIntEthStatusInst_Object = MibTableColumn
mnPrIDUConfIntEthStatusInst = _MnPrIDUConfIntEthStatusInst_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 21),
    _MnPrIDUConfIntEthStatusInst_Type()
)
mnPrIDUConfIntEthStatusInst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfIntEthStatusInst.setStatus("mandatory")


class _MnPrIDUConfIntEthStatusConf_Type(Integer32):
    """Custom type mnPrIDUConfIntEthStatusConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneHundredBaseT", 1),
          ("notInstalled", 2))
    )


_MnPrIDUConfIntEthStatusConf_Type.__name__ = "Integer32"
_MnPrIDUConfIntEthStatusConf_Object = MibTableColumn
mnPrIDUConfIntEthStatusConf = _MnPrIDUConfIntEthStatusConf_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 22),
    _MnPrIDUConfIntEthStatusConf_Type()
)
mnPrIDUConfIntEthStatusConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfIntEthStatusConf.setStatus("mandatory")


class _MnPrIDUConfIntEthStatusProp_Type(Integer32):
    """Custom type mnPrIDUConfIntEthStatusProp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneHundredBaseT", 1),
          ("notInstalled", 2))
    )


_MnPrIDUConfIntEthStatusProp_Type.__name__ = "Integer32"
_MnPrIDUConfIntEthStatusProp_Object = MibTableColumn
mnPrIDUConfIntEthStatusProp = _MnPrIDUConfIntEthStatusProp_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 23),
    _MnPrIDUConfIntEthStatusProp_Type()
)
mnPrIDUConfIntEthStatusProp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfIntEthStatusProp.setStatus("mandatory")
_MnPrIDUConfIntEthCapacityInst_Type = Integer32
_MnPrIDUConfIntEthCapacityInst_Object = MibTableColumn
mnPrIDUConfIntEthCapacityInst = _MnPrIDUConfIntEthCapacityInst_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 24),
    _MnPrIDUConfIntEthCapacityInst_Type()
)
mnPrIDUConfIntEthCapacityInst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfIntEthCapacityInst.setStatus("mandatory")
_MnPrIDUConfIntEthCapacityConf_Type = Integer32
_MnPrIDUConfIntEthCapacityConf_Object = MibTableColumn
mnPrIDUConfIntEthCapacityConf = _MnPrIDUConfIntEthCapacityConf_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 25),
    _MnPrIDUConfIntEthCapacityConf_Type()
)
mnPrIDUConfIntEthCapacityConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfIntEthCapacityConf.setStatus("mandatory")
_MnPrIDUConfIntEthCapacityProp_Type = Integer32
_MnPrIDUConfIntEthCapacityProp_Object = MibTableColumn
mnPrIDUConfIntEthCapacityProp = _MnPrIDUConfIntEthCapacityProp_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 26),
    _MnPrIDUConfIntEthCapacityProp_Type()
)
mnPrIDUConfIntEthCapacityProp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfIntEthCapacityProp.setStatus("mandatory")


class _MnPrIDUConfLoopSwitchMode_Type(Integer32):
    """Custom type mnPrIDUConfLoopSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("pass", 2),
          ("switch", 3))
    )


_MnPrIDUConfLoopSwitchMode_Type.__name__ = "Integer32"
_MnPrIDUConfLoopSwitchMode_Object = MibTableColumn
mnPrIDUConfLoopSwitchMode = _MnPrIDUConfLoopSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 27),
    _MnPrIDUConfLoopSwitchMode_Type()
)
mnPrIDUConfLoopSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfLoopSwitchMode.setStatus("mandatory")
_MnPrIDUConfStatLicCapacity_Type = Integer32
_MnPrIDUConfStatLicCapacity_Object = MibTableColumn
mnPrIDUConfStatLicCapacity = _MnPrIDUConfStatLicCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 3, 1, 28),
    _MnPrIDUConfStatLicCapacity_Type()
)
mnPrIDUConfStatLicCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIDUConfStatLicCapacity.setStatus("mandatory")
_MnPrLIMConfTable_Object = MibTable
mnPrLIMConfTable = _MnPrLIMConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 4)
)
if mibBuilder.loadTexts:
    mnPrLIMConfTable.setStatus("mandatory")
_MnPrLIMConfEntry_Object = MibTableRow
mnPrLIMConfEntry = _MnPrLIMConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 4, 1)
)
mnPrLIMConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnLIMIndex"),
)
if mibBuilder.loadTexts:
    mnPrLIMConfEntry.setStatus("mandatory")
_MnPrLIMConfTypeInstalled_Type = LIMType
_MnPrLIMConfTypeInstalled_Object = MibTableColumn
mnPrLIMConfTypeInstalled = _MnPrLIMConfTypeInstalled_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 4, 1, 1),
    _MnPrLIMConfTypeInstalled_Type()
)
mnPrLIMConfTypeInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLIMConfTypeInstalled.setStatus("mandatory")
_MnPrLIMConfTypeProposed_Type = LIMType
_MnPrLIMConfTypeProposed_Object = MibTableColumn
mnPrLIMConfTypeProposed = _MnPrLIMConfTypeProposed_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 4, 1, 2),
    _MnPrLIMConfTypeProposed_Type()
)
mnPrLIMConfTypeProposed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrLIMConfTypeProposed.setStatus("mandatory")
_MnPrLIMConfTypeConf_Type = LIMType
_MnPrLIMConfTypeConf_Object = MibTableColumn
mnPrLIMConfTypeConf = _MnPrLIMConfTypeConf_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 4, 1, 3),
    _MnPrLIMConfTypeConf_Type()
)
mnPrLIMConfTypeConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLIMConfTypeConf.setStatus("mandatory")


class _MnPrLIMConfCapacity_Type(Integer32):
    """Custom type mnPrLIMConfCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MnPrLIMConfCapacity_Type.__name__ = "Integer32"
_MnPrLIMConfCapacity_Object = MibTableColumn
mnPrLIMConfCapacity = _MnPrLIMConfCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 4, 1, 4),
    _MnPrLIMConfCapacity_Type()
)
mnPrLIMConfCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLIMConfCapacity.setStatus("mandatory")
_MnPrLIMConfCapacityInst_Type = Integer32
_MnPrLIMConfCapacityInst_Object = MibTableColumn
mnPrLIMConfCapacityInst = _MnPrLIMConfCapacityInst_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 4, 1, 5),
    _MnPrLIMConfCapacityInst_Type()
)
mnPrLIMConfCapacityInst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrLIMConfCapacityInst.setStatus("mandatory")
_MnPrLIMConfCapacityConf_Type = Integer32
_MnPrLIMConfCapacityConf_Object = MibTableColumn
mnPrLIMConfCapacityConf = _MnPrLIMConfCapacityConf_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 4, 1, 6),
    _MnPrLIMConfCapacityConf_Type()
)
mnPrLIMConfCapacityConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrLIMConfCapacityConf.setStatus("mandatory")
_MnPrLIMConfCapacityProp_Type = Integer32
_MnPrLIMConfCapacityProp_Object = MibTableColumn
mnPrLIMConfCapacityProp = _MnPrLIMConfCapacityProp_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 4, 1, 7),
    _MnPrLIMConfCapacityProp_Type()
)
mnPrLIMConfCapacityProp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrLIMConfCapacityProp.setStatus("mandatory")


class _MnPrLIMConfSHARPInstalled_Type(Integer32):
    """Custom type mnPrLIMConfSHARPInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("notInstalled", 3))
    )


_MnPrLIMConfSHARPInstalled_Type.__name__ = "Integer32"
_MnPrLIMConfSHARPInstalled_Object = MibTableColumn
mnPrLIMConfSHARPInstalled = _MnPrLIMConfSHARPInstalled_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 4, 1, 8),
    _MnPrLIMConfSHARPInstalled_Type()
)
mnPrLIMConfSHARPInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrLIMConfSHARPInstalled.setStatus("mandatory")
_MnPrTribConfTable_Object = MibTable
mnPrTribConfTable = _MnPrTribConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 5)
)
if mibBuilder.loadTexts:
    mnPrTribConfTable.setStatus("mandatory")
_MnPrTribConfEntry_Object = MibTableRow
mnPrTribConfEntry = _MnPrTribConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 5, 1)
)
mnPrTribConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnTribIndex"),
)
if mibBuilder.loadTexts:
    mnPrTribConfEntry.setStatus("mandatory")
_MnPrTribConfAdminEquipped_Type = TruthValue
_MnPrTribConfAdminEquipped_Object = MibTableColumn
mnPrTribConfAdminEquipped = _MnPrTribConfAdminEquipped_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 5, 1, 1),
    _MnPrTribConfAdminEquipped_Type()
)
mnPrTribConfAdminEquipped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrTribConfAdminEquipped.setStatus("mandatory")
_MnPrSysConfTable_Object = MibTable
mnPrSysConfTable = _MnPrSysConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6)
)
if mibBuilder.loadTexts:
    mnPrSysConfTable.setStatus("mandatory")
_MnPrSysConfEntry_Object = MibTableRow
mnPrSysConfEntry = _MnPrSysConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1)
)
mnPrSysConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
)
if mibBuilder.loadTexts:
    mnPrSysConfEntry.setStatus("mandatory")
_MnPrSysConfRadioName_Type = DisplayString
_MnPrSysConfRadioName_Object = MibTableColumn
mnPrSysConfRadioName = _MnPrSysConfRadioName_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 1),
    _MnPrSysConfRadioName_Type()
)
mnPrSysConfRadioName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSysConfRadioName.setStatus("mandatory")
_MnPrSysConfLocation_Type = DisplayString
_MnPrSysConfLocation_Object = MibTableColumn
mnPrSysConfLocation = _MnPrSysConfLocation_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 2),
    _MnPrSysConfLocation_Type()
)
mnPrSysConfLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSysConfLocation.setStatus("mandatory")
_MnPrSysConfContact_Type = DisplayString
_MnPrSysConfContact_Object = MibTableColumn
mnPrSysConfContact = _MnPrSysConfContact_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 3),
    _MnPrSysConfContact_Type()
)
mnPrSysConfContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSysConfContact.setStatus("mandatory")
_MnPrSysConfDateAndTime_Type = DateAndTime
_MnPrSysConfDateAndTime_Object = MibTableColumn
mnPrSysConfDateAndTime = _MnPrSysConfDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 4),
    _MnPrSysConfDateAndTime_Type()
)
mnPrSysConfDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSysConfDateAndTime.setStatus("mandatory")
_MnPrSysConfLicenseKey_Type = DisplayString
_MnPrSysConfLicenseKey_Object = MibTableColumn
mnPrSysConfLicenseKey = _MnPrSysConfLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 5),
    _MnPrSysConfLicenseKey_Type()
)
mnPrSysConfLicenseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSysConfLicenseKey.setStatus("mandatory")
_MnPrSysConfThroughPut_Type = Integer32
_MnPrSysConfThroughPut_Object = MibTableColumn
mnPrSysConfThroughPut = _MnPrSysConfThroughPut_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 6),
    _MnPrSysConfThroughPut_Type()
)
mnPrSysConfThroughPut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrSysConfThroughPut.setStatus("mandatory")
_MnPrSysConfTimeZone_Type = DisplayString
_MnPrSysConfTimeZone_Object = MibTableColumn
mnPrSysConfTimeZone = _MnPrSysConfTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 7),
    _MnPrSysConfTimeZone_Type()
)
mnPrSysConfTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSysConfTimeZone.setStatus("mandatory")
_MnPrSysConfDaylightSavings_Type = TruthValue
_MnPrSysConfDaylightSavings_Object = MibTableColumn
mnPrSysConfDaylightSavings = _MnPrSysConfDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 8),
    _MnPrSysConfDaylightSavings_Type()
)
mnPrSysConfDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSysConfDaylightSavings.setStatus("mandatory")
_MnPrSysConfDpmStatus_Type = Integer32
_MnPrSysConfDpmStatus_Object = MibTableColumn
mnPrSysConfDpmStatus = _MnPrSysConfDpmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 9),
    _MnPrSysConfDpmStatus_Type()
)
mnPrSysConfDpmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrSysConfDpmStatus.setStatus("mandatory")
_MnPrSysConfDpmPolicy_Type = Integer32
_MnPrSysConfDpmPolicy_Object = MibTableColumn
mnPrSysConfDpmPolicy = _MnPrSysConfDpmPolicy_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 10),
    _MnPrSysConfDpmPolicy_Type()
)
mnPrSysConfDpmPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSysConfDpmPolicy.setStatus("mandatory")


class _MnPrSysConfEncMode_Type(Integer32):
    """Custom type mnPrSysConfEncMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("aes128", 2),
          ("aes192", 3),
          ("aes256", 4),
          ("armTransition", 5))
    )


_MnPrSysConfEncMode_Type.__name__ = "Integer32"
_MnPrSysConfEncMode_Object = MibTableColumn
mnPrSysConfEncMode = _MnPrSysConfEncMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 11),
    _MnPrSysConfEncMode_Type()
)
mnPrSysConfEncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSysConfEncMode.setStatus("mandatory")
_MnPrSysConfEncPassword_Type = DisplayString
_MnPrSysConfEncPassword_Object = MibTableColumn
mnPrSysConfEncPassword = _MnPrSysConfEncPassword_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 12),
    _MnPrSysConfEncPassword_Type()
)
mnPrSysConfEncPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSysConfEncPassword.setStatus("mandatory")


class _MnPrSysConfEncFailPolicy_Type(Integer32):
    """Custom type mnPrSysConfEncFailPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nofallback", 1),
          ("fallback", 2))
    )


_MnPrSysConfEncFailPolicy_Type.__name__ = "Integer32"
_MnPrSysConfEncFailPolicy_Object = MibTableColumn
mnPrSysConfEncFailPolicy = _MnPrSysConfEncFailPolicy_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 13),
    _MnPrSysConfEncFailPolicy_Type()
)
mnPrSysConfEncFailPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSysConfEncFailPolicy.setStatus("mandatory")
_MnPrSysConfFIPSKeyActivate_Type = TruthValue
_MnPrSysConfFIPSKeyActivate_Object = MibTableColumn
mnPrSysConfFIPSKeyActivate = _MnPrSysConfFIPSKeyActivate_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 14),
    _MnPrSysConfFIPSKeyActivate_Type()
)
mnPrSysConfFIPSKeyActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSysConfFIPSKeyActivate.setStatus("mandatory")


class _MnPrSysConfFIPSMode_Type(Integer32):
    """Custom type mnPrSysConfFIPSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_MnPrSysConfFIPSMode_Type.__name__ = "Integer32"
_MnPrSysConfFIPSMode_Object = MibTableColumn
mnPrSysConfFIPSMode = _MnPrSysConfFIPSMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 6, 1, 15),
    _MnPrSysConfFIPSMode_Type()
)
mnPrSysConfFIPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSysConfFIPSMode.setStatus("mandatory")
_MnPrUserConfTable_Object = MibTable
mnPrUserConfTable = _MnPrUserConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 7)
)
if mibBuilder.loadTexts:
    mnPrUserConfTable.setStatus("mandatory")
_MnPrUserConfEntry_Object = MibTableRow
mnPrUserConfEntry = _MnPrUserConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 7, 1)
)
mnPrUserConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrUserConfIndex"),
)
if mibBuilder.loadTexts:
    mnPrUserConfEntry.setStatus("mandatory")


class _MnPrUserConfIndex_Type(Integer32):
    """Custom type mnPrUserConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MnPrUserConfIndex_Type.__name__ = "Integer32"
_MnPrUserConfIndex_Object = MibTableColumn
mnPrUserConfIndex = _MnPrUserConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 7, 1, 1),
    _MnPrUserConfIndex_Type()
)
mnPrUserConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrUserConfIndex.setStatus("mandatory")
_MnPrUserConfUsername_Type = DisplayString
_MnPrUserConfUsername_Object = MibTableColumn
mnPrUserConfUsername = _MnPrUserConfUsername_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 7, 1, 2),
    _MnPrUserConfUsername_Type()
)
mnPrUserConfUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrUserConfUsername.setStatus("mandatory")
_MnPrUserConfPasswordSet_Type = DisplayString
_MnPrUserConfPasswordSet_Object = MibTableColumn
mnPrUserConfPasswordSet = _MnPrUserConfPasswordSet_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 7, 1, 3),
    _MnPrUserConfPasswordSet_Type()
)
mnPrUserConfPasswordSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrUserConfPasswordSet.setStatus("mandatory")
_MnPrUserConfAccessLevel_Type = AccessLevel
_MnPrUserConfAccessLevel_Object = MibTableColumn
mnPrUserConfAccessLevel = _MnPrUserConfAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 7, 1, 4),
    _MnPrUserConfAccessLevel_Type()
)
mnPrUserConfAccessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrUserConfAccessLevel.setStatus("mandatory")


class _MnPrUserConfAuthProtocol_Type(Integer32):
    """Custom type mnPrUserConfAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthProtocol", 1),
          ("md5AuthProtocol", 2),
          ("shaAuthProtocol", 3))
    )


_MnPrUserConfAuthProtocol_Type.__name__ = "Integer32"
_MnPrUserConfAuthProtocol_Object = MibTableColumn
mnPrUserConfAuthProtocol = _MnPrUserConfAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 7, 1, 5),
    _MnPrUserConfAuthProtocol_Type()
)
mnPrUserConfAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrUserConfAuthProtocol.setStatus("mandatory")


class _MnPrUserConfPrivProtocol_Type(Integer32):
    """Custom type mnPrUserConfPrivProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noPrivProtocol", 1),
          ("desPrivProtocol", 2),
          ("aes128PrivProtocol", 4))
    )


_MnPrUserConfPrivProtocol_Type.__name__ = "Integer32"
_MnPrUserConfPrivProtocol_Object = MibTableColumn
mnPrUserConfPrivProtocol = _MnPrUserConfPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 7, 1, 6),
    _MnPrUserConfPrivProtocol_Type()
)
mnPrUserConfPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrUserConfPrivProtocol.setStatus("mandatory")
_MnPrUserConfPrivPwdSet_Type = DisplayString
_MnPrUserConfPrivPwdSet_Object = MibTableColumn
mnPrUserConfPrivPwdSet = _MnPrUserConfPrivPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 7, 1, 7),
    _MnPrUserConfPrivPwdSet_Type()
)
mnPrUserConfPrivPwdSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrUserConfPrivPwdSet.setStatus("mandatory")
_MnPrAlarmConfTable_Object = MibTable
mnPrAlarmConfTable = _MnPrAlarmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 8)
)
if mibBuilder.loadTexts:
    mnPrAlarmConfTable.setStatus("mandatory")
_MnPrAlarmConfEntry_Object = MibTableRow
mnPrAlarmConfEntry = _MnPrAlarmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 8, 1)
)
mnPrAlarmConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnAlarmIndex"),
)
if mibBuilder.loadTexts:
    mnPrAlarmConfEntry.setStatus("mandatory")


class _MnAlarmIndex_Type(Integer32):
    """Custom type mnAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MnAlarmIndex_Type.__name__ = "Integer32"
_MnAlarmIndex_Object = MibTableColumn
mnAlarmIndex = _MnAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 8, 1, 1),
    _MnAlarmIndex_Type()
)
mnAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnAlarmIndex.setStatus("mandatory")
_MnPrAlarmConfName_Type = DisplayString
_MnPrAlarmConfName_Object = MibTableColumn
mnPrAlarmConfName = _MnPrAlarmConfName_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 8, 1, 2),
    _MnPrAlarmConfName_Type()
)
mnPrAlarmConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrAlarmConfName.setStatus("mandatory")
_MnPrAlarmConfUserName_Type = DisplayString
_MnPrAlarmConfUserName_Object = MibTableColumn
mnPrAlarmConfUserName = _MnPrAlarmConfUserName_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 8, 1, 3),
    _MnPrAlarmConfUserName_Type()
)
mnPrAlarmConfUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrAlarmConfUserName.setStatus("mandatory")
_MnPrAlarmConfAbrev_Type = DisplayString
_MnPrAlarmConfAbrev_Object = MibTableColumn
mnPrAlarmConfAbrev = _MnPrAlarmConfAbrev_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 8, 1, 4),
    _MnPrAlarmConfAbrev_Type()
)
mnPrAlarmConfAbrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrAlarmConfAbrev.setStatus("mandatory")
_MnPrAlarmConfMap_Type = Integer32
_MnPrAlarmConfMap_Object = MibTableColumn
mnPrAlarmConfMap = _MnPrAlarmConfMap_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 8, 1, 5),
    _MnPrAlarmConfMap_Type()
)
mnPrAlarmConfMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrAlarmConfMap.setStatus("mandatory")


class _MnPrAlarmConfCircuitType_Type(Integer32):
    """Custom type mnPrAlarmConfCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("circuitOpen", 1),
          ("circuitClosed", 2),
          ("circuitNone", 99))
    )


_MnPrAlarmConfCircuitType_Type.__name__ = "Integer32"
_MnPrAlarmConfCircuitType_Object = MibTableColumn
mnPrAlarmConfCircuitType = _MnPrAlarmConfCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 8, 1, 6),
    _MnPrAlarmConfCircuitType_Type()
)
mnPrAlarmConfCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrAlarmConfCircuitType.setStatus("mandatory")
_MnPrAlarmConfThreshold_Type = Integer32
_MnPrAlarmConfThreshold_Object = MibTableColumn
mnPrAlarmConfThreshold = _MnPrAlarmConfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 8, 1, 7),
    _MnPrAlarmConfThreshold_Type()
)
mnPrAlarmConfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrAlarmConfThreshold.setStatus("mandatory")
_MnPrAlarmConfSet_Type = TruthValue
_MnPrAlarmConfSet_Object = MibTableColumn
mnPrAlarmConfSet = _MnPrAlarmConfSet_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 8, 1, 8),
    _MnPrAlarmConfSet_Type()
)
mnPrAlarmConfSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrAlarmConfSet.setStatus("mandatory")
_MnPrNMConfTable_Object = MibTable
mnPrNMConfTable = _MnPrNMConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 9)
)
if mibBuilder.loadTexts:
    mnPrNMConfTable.setStatus("mandatory")
_MnPrNMConfEntry_Object = MibTableRow
mnPrNMConfEntry = _MnPrNMConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 9, 1)
)
mnPrNMConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
)
if mibBuilder.loadTexts:
    mnPrNMConfEntry.setStatus("mandatory")
_MnPrNMConfDefGateway_Type = IpAddress
_MnPrNMConfDefGateway_Object = MibTableColumn
mnPrNMConfDefGateway = _MnPrNMConfDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 9, 1, 1),
    _MnPrNMConfDefGateway_Type()
)
mnPrNMConfDefGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrNMConfDefGateway.setStatus("mandatory")


class _MnPrNMConfTrapMode_Type(Integer32):
    """Custom type mnPrNMConfTrapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("silent", 1),
          ("terse", 2),
          ("verbose", 3))
    )


_MnPrNMConfTrapMode_Type.__name__ = "Integer32"
_MnPrNMConfTrapMode_Object = MibTableColumn
mnPrNMConfTrapMode = _MnPrNMConfTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 9, 1, 2),
    _MnPrNMConfTrapMode_Type()
)
mnPrNMConfTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrNMConfTrapMode.setStatus("mandatory")
_MnPrNMConfTFTPAddr_Type = IpAddress
_MnPrNMConfTFTPAddr_Object = MibTableColumn
mnPrNMConfTFTPAddr = _MnPrNMConfTFTPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 9, 1, 3),
    _MnPrNMConfTFTPAddr_Type()
)
mnPrNMConfTFTPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrNMConfTFTPAddr.setStatus("mandatory")
_MnPrNMConfTFTPFile_Type = DisplayString
_MnPrNMConfTFTPFile_Object = MibTableColumn
mnPrNMConfTFTPFile = _MnPrNMConfTFTPFile_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 9, 1, 4),
    _MnPrNMConfTFTPFile_Type()
)
mnPrNMConfTFTPFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrNMConfTFTPFile.setStatus("mandatory")
_MnPrNMConfSNTPAddr_Type = IpAddress
_MnPrNMConfSNTPAddr_Object = MibTableColumn
mnPrNMConfSNTPAddr = _MnPrNMConfSNTPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 9, 1, 5),
    _MnPrNMConfSNTPAddr_Type()
)
mnPrNMConfSNTPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrNMConfSNTPAddr.setStatus("mandatory")


class _MnPrNMConfSNTPInterval_Type(Integer32):
    """Custom type mnPrNMConfSNTPInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MnPrNMConfSNTPInterval_Type.__name__ = "Integer32"
_MnPrNMConfSNTPInterval_Object = MibTableColumn
mnPrNMConfSNTPInterval = _MnPrNMConfSNTPInterval_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 9, 1, 6),
    _MnPrNMConfSNTPInterval_Type()
)
mnPrNMConfSNTPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrNMConfSNTPInterval.setStatus("mandatory")


class _MnPrNMConfSNTPTimeout_Type(Integer32):
    """Custom type mnPrNMConfSNTPTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_MnPrNMConfSNTPTimeout_Type.__name__ = "Integer32"
_MnPrNMConfSNTPTimeout_Object = MibTableColumn
mnPrNMConfSNTPTimeout = _MnPrNMConfSNTPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 9, 1, 7),
    _MnPrNMConfSNTPTimeout_Type()
)
mnPrNMConfSNTPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrNMConfSNTPTimeout.setStatus("mandatory")


class _MnPrNMConfAuthMode_Type(Integer32):
    """Custom type mnPrNMConfAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("localradius", 3))
    )


_MnPrNMConfAuthMode_Type.__name__ = "Integer32"
_MnPrNMConfAuthMode_Object = MibTableColumn
mnPrNMConfAuthMode = _MnPrNMConfAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 9, 1, 8),
    _MnPrNMConfAuthMode_Type()
)
mnPrNMConfAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrNMConfAuthMode.setStatus("mandatory")


class _MnPrNMConfRADTimeout_Type(Integer32):
    """Custom type mnPrNMConfRADTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MnPrNMConfRADTimeout_Type.__name__ = "Integer32"
_MnPrNMConfRADTimeout_Object = MibTableColumn
mnPrNMConfRADTimeout = _MnPrNMConfRADTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 9, 1, 9),
    _MnPrNMConfRADTimeout_Type()
)
mnPrNMConfRADTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrNMConfRADTimeout.setStatus("mandatory")


class _MnPrNMConfRADRetries_Type(Integer32):
    """Custom type mnPrNMConfRADRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MnPrNMConfRADRetries_Type.__name__ = "Integer32"
_MnPrNMConfRADRetries_Object = MibTableColumn
mnPrNMConfRADRetries = _MnPrNMConfRADRetries_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 9, 1, 10),
    _MnPrNMConfRADRetries_Type()
)
mnPrNMConfRADRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrNMConfRADRetries.setStatus("mandatory")


class _MnPrNMConfRADDeadtime_Type(Integer32):
    """Custom type mnPrNMConfRADDeadtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_MnPrNMConfRADDeadtime_Type.__name__ = "Integer32"
_MnPrNMConfRADDeadtime_Object = MibTableColumn
mnPrNMConfRADDeadtime = _MnPrNMConfRADDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 9, 1, 11),
    _MnPrNMConfRADDeadtime_Type()
)
mnPrNMConfRADDeadtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrNMConfRADDeadtime.setStatus("mandatory")


class _MnPrNMConfRADMinPwdLen_Type(Integer32):
    """Custom type mnPrNMConfRADMinPwdLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_MnPrNMConfRADMinPwdLen_Type.__name__ = "Integer32"
_MnPrNMConfRADMinPwdLen_Object = MibTableColumn
mnPrNMConfRADMinPwdLen = _MnPrNMConfRADMinPwdLen_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 9, 1, 12),
    _MnPrNMConfRADMinPwdLen_Type()
)
mnPrNMConfRADMinPwdLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrNMConfRADMinPwdLen.setStatus("mandatory")
_MnPrIPIfConfTable_Object = MibTable
mnPrIPIfConfTable = _MnPrIPIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 10)
)
if mibBuilder.loadTexts:
    mnPrIPIfConfTable.setStatus("mandatory")
_MnPrIPIfConfEntry_Object = MibTableRow
mnPrIPIfConfEntry = _MnPrIPIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 10, 1)
)
mnPrIPIfConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnIPIfIndex"),
)
if mibBuilder.loadTexts:
    mnPrIPIfConfEntry.setStatus("mandatory")


class _MnIPIfIndex_Type(Integer32):
    """Custom type mnIPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("ipoair", 3),
          ("ppp", 4))
    )


_MnIPIfIndex_Type.__name__ = "Integer32"
_MnIPIfIndex_Object = MibTableColumn
mnIPIfIndex = _MnIPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 10, 1, 1),
    _MnIPIfIndex_Type()
)
mnIPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnIPIfIndex.setStatus("mandatory")
_MnPrIPIfConfIPAddr_Type = IpAddress
_MnPrIPIfConfIPAddr_Object = MibTableColumn
mnPrIPIfConfIPAddr = _MnPrIPIfConfIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 10, 1, 2),
    _MnPrIPIfConfIPAddr_Type()
)
mnPrIPIfConfIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIPIfConfIPAddr.setStatus("mandatory")
_MnPrIPIfConfSubnetMask_Type = IpAddress
_MnPrIPIfConfSubnetMask_Object = MibTableColumn
mnPrIPIfConfSubnetMask = _MnPrIPIfConfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 10, 1, 3),
    _MnPrIPIfConfSubnetMask_Type()
)
mnPrIPIfConfSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIPIfConfSubnetMask.setStatus("mandatory")


class _MnPrIPIfConfRouting_Type(Integer32):
    """Custom type mnPrIPIfConfRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rip", 2))
    )


_MnPrIPIfConfRouting_Type.__name__ = "Integer32"
_MnPrIPIfConfRouting_Object = MibTableColumn
mnPrIPIfConfRouting = _MnPrIPIfConfRouting_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 10, 1, 4),
    _MnPrIPIfConfRouting_Type()
)
mnPrIPIfConfRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIPIfConfRouting.setStatus("mandatory")
_MnPrIPIfConfRoutingBit_Type = Integer32
_MnPrIPIfConfRoutingBit_Object = MibTableColumn
mnPrIPIfConfRoutingBit = _MnPrIPIfConfRoutingBit_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 10, 1, 5),
    _MnPrIPIfConfRoutingBit_Type()
)
mnPrIPIfConfRoutingBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIPIfConfRoutingBit.setStatus("mandatory")
_MnPrIPIfConfCustomAddress_Type = IpAddress
_MnPrIPIfConfCustomAddress_Object = MibTableColumn
mnPrIPIfConfCustomAddress = _MnPrIPIfConfCustomAddress_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 10, 1, 6),
    _MnPrIPIfConfCustomAddress_Type()
)
mnPrIPIfConfCustomAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIPIfConfCustomAddress.setStatus("mandatory")
_MnPrIPIfConfCustomSubnet_Type = IpAddress
_MnPrIPIfConfCustomSubnet_Object = MibTableColumn
mnPrIPIfConfCustomSubnet = _MnPrIPIfConfCustomSubnet_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 10, 1, 7),
    _MnPrIPIfConfCustomSubnet_Type()
)
mnPrIPIfConfCustomSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrIPIfConfCustomSubnet.setStatus("mandatory")
_MnPrRouteConfTable_Object = MibTable
mnPrRouteConfTable = _MnPrRouteConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 11)
)
if mibBuilder.loadTexts:
    mnPrRouteConfTable.setStatus("mandatory")
_MnPrRouteConfEntry_Object = MibTableRow
mnPrRouteConfEntry = _MnPrRouteConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 11, 1)
)
mnPrRouteConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrRouteConfIndex"),
)
if mibBuilder.loadTexts:
    mnPrRouteConfEntry.setStatus("mandatory")


class _MnPrRouteConfIndex_Type(Integer32):
    """Custom type mnPrRouteConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_MnPrRouteConfIndex_Type.__name__ = "Integer32"
_MnPrRouteConfIndex_Object = MibTableColumn
mnPrRouteConfIndex = _MnPrRouteConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 11, 1, 1),
    _MnPrRouteConfIndex_Type()
)
mnPrRouteConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRouteConfIndex.setStatus("mandatory")
_MnPrRouteConfDest_Type = IpAddress
_MnPrRouteConfDest_Object = MibTableColumn
mnPrRouteConfDest = _MnPrRouteConfDest_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 11, 1, 2),
    _MnPrRouteConfDest_Type()
)
mnPrRouteConfDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRouteConfDest.setStatus("mandatory")
_MnPrRouteConfMask_Type = IpAddress
_MnPrRouteConfMask_Object = MibTableColumn
mnPrRouteConfMask = _MnPrRouteConfMask_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 11, 1, 3),
    _MnPrRouteConfMask_Type()
)
mnPrRouteConfMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRouteConfMask.setStatus("mandatory")
_MnPrRouteConfNextHop_Type = IpAddress
_MnPrRouteConfNextHop_Object = MibTableColumn
mnPrRouteConfNextHop = _MnPrRouteConfNextHop_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 11, 1, 4),
    _MnPrRouteConfNextHop_Type()
)
mnPrRouteConfNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRouteConfNextHop.setStatus("mandatory")
_MnPrRouteConfMetric_Type = Integer32
_MnPrRouteConfMetric_Object = MibTableColumn
mnPrRouteConfMetric = _MnPrRouteConfMetric_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 11, 1, 5),
    _MnPrRouteConfMetric_Type()
)
mnPrRouteConfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRouteConfMetric.setStatus("mandatory")
_MnPrRouteConfRowStatus_Type = RowStatus
_MnPrRouteConfRowStatus_Object = MibTableColumn
mnPrRouteConfRowStatus = _MnPrRouteConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 11, 1, 6),
    _MnPrRouteConfRowStatus_Type()
)
mnPrRouteConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRouteConfRowStatus.setStatus("mandatory")
_MnPrTrapConfTable_Object = MibTable
mnPrTrapConfTable = _MnPrTrapConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 12)
)
if mibBuilder.loadTexts:
    mnPrTrapConfTable.setStatus("mandatory")
_MnPrTrapConfEntry_Object = MibTableRow
mnPrTrapConfEntry = _MnPrTrapConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 12, 1)
)
mnPrTrapConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnTrapIndex"),
)
if mibBuilder.loadTexts:
    mnPrTrapConfEntry.setStatus("mandatory")


class _MnTrapIndex_Type(Integer32):
    """Custom type mnTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MnTrapIndex_Type.__name__ = "Integer32"
_MnTrapIndex_Object = MibTableColumn
mnTrapIndex = _MnTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 12, 1, 1),
    _MnTrapIndex_Type()
)
mnTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnTrapIndex.setStatus("mandatory")
_MnPrTrapConfTrapAddr_Type = IpAddress
_MnPrTrapConfTrapAddr_Object = MibTableColumn
mnPrTrapConfTrapAddr = _MnPrTrapConfTrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 12, 1, 2),
    _MnPrTrapConfTrapAddr_Type()
)
mnPrTrapConfTrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrTrapConfTrapAddr.setStatus("mandatory")
_MnPrTrapConfTrapComm_Type = DisplayString
_MnPrTrapConfTrapComm_Object = MibTableColumn
mnPrTrapConfTrapComm = _MnPrTrapConfTrapComm_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 12, 1, 3),
    _MnPrTrapConfTrapComm_Type()
)
mnPrTrapConfTrapComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrTrapConfTrapComm.setStatus("mandatory")
_MnPrTrapConfRowStatus_Type = RowStatus
_MnPrTrapConfRowStatus_Object = MibTableColumn
mnPrTrapConfRowStatus = _MnPrTrapConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 12, 1, 4),
    _MnPrTrapConfRowStatus_Type()
)
mnPrTrapConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrTrapConfRowStatus.setStatus("mandatory")
_MnPrPPPConfTable_Object = MibTable
mnPrPPPConfTable = _MnPrPPPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 13)
)
if mibBuilder.loadTexts:
    mnPrPPPConfTable.setStatus("mandatory")
_MnPrPPPConfEntry_Object = MibTableRow
mnPrPPPConfEntry = _MnPrPPPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 13, 1)
)
mnPrPPPConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
)
if mibBuilder.loadTexts:
    mnPrPPPConfEntry.setStatus("mandatory")
_MnPrPPPConfBaudRate_Type = Integer32
_MnPrPPPConfBaudRate_Object = MibTableColumn
mnPrPPPConfBaudRate = _MnPrPPPConfBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 13, 1, 1),
    _MnPrPPPConfBaudRate_Type()
)
mnPrPPPConfBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrPPPConfBaudRate.setStatus("mandatory")
_MnPrPPPConfInitString_Type = DisplayString
_MnPrPPPConfInitString_Object = MibTableColumn
mnPrPPPConfInitString = _MnPrPPPConfInitString_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 13, 1, 2),
    _MnPrPPPConfInitString_Type()
)
mnPrPPPConfInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrPPPConfInitString.setStatus("mandatory")
_MnPrPPPConfChapUser_Type = DisplayString
_MnPrPPPConfChapUser_Object = MibTableColumn
mnPrPPPConfChapUser = _MnPrPPPConfChapUser_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 13, 1, 3),
    _MnPrPPPConfChapUser_Type()
)
mnPrPPPConfChapUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrPPPConfChapUser.setStatus("mandatory")
_MnPrPPPConfChapSecret_Type = DisplayString
_MnPrPPPConfChapSecret_Object = MibTableColumn
mnPrPPPConfChapSecret = _MnPrPPPConfChapSecret_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 13, 1, 4),
    _MnPrPPPConfChapSecret_Type()
)
mnPrPPPConfChapSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrPPPConfChapSecret.setStatus("mandatory")
_MnPrPerfHistConfigObjects_ObjectIdentity = ObjectIdentity
mnPrPerfHistConfigObjects = _MnPrPerfHistConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 14)
)
_MnPrPerfHistConfTable_Object = MibTable
mnPrPerfHistConfTable = _MnPrPerfHistConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 14, 1)
)
if mibBuilder.loadTexts:
    mnPrPerfHistConfTable.setStatus("mandatory")
_MnPrPerfHistConfEntry_Object = MibTableRow
mnPrPerfHistConfEntry = _MnPrPerfHistConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 14, 1, 1)
)
mnPrPerfHistConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
)
if mibBuilder.loadTexts:
    mnPrPerfHistConfEntry.setStatus("mandatory")
_MnPrPerfHistConfEnable_Type = TruthValue
_MnPrPerfHistConfEnable_Object = MibTableColumn
mnPrPerfHistConfEnable = _MnPrPerfHistConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 14, 1, 1, 1),
    _MnPrPerfHistConfEnable_Type()
)
mnPrPerfHistConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrPerfHistConfEnable.setStatus("mandatory")
_MnPrPerfHistConfInterval_Type = Integer32
_MnPrPerfHistConfInterval_Object = MibTableColumn
mnPrPerfHistConfInterval = _MnPrPerfHistConfInterval_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 14, 1, 1, 2),
    _MnPrPerfHistConfInterval_Type()
)
mnPrPerfHistConfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrPerfHistConfInterval.setStatus("mandatory")
_MnPrPerfHistConfFilename_Type = DisplayString
_MnPrPerfHistConfFilename_Object = MibTableColumn
mnPrPerfHistConfFilename = _MnPrPerfHistConfFilename_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 14, 1, 1, 3),
    _MnPrPerfHistConfFilename_Type()
)
mnPrPerfHistConfFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrPerfHistConfFilename.setStatus("mandatory")
_MnPrPerfHistConfUploadInterval_Type = Integer32
_MnPrPerfHistConfUploadInterval_Object = MibTableColumn
mnPrPerfHistConfUploadInterval = _MnPrPerfHistConfUploadInterval_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 14, 1, 1, 4),
    _MnPrPerfHistConfUploadInterval_Type()
)
mnPrPerfHistConfUploadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrPerfHistConfUploadInterval.setStatus("mandatory")
_MnPrPerfHistConfVarTable_Object = MibTable
mnPrPerfHistConfVarTable = _MnPrPerfHistConfVarTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 14, 2)
)
if mibBuilder.loadTexts:
    mnPrPerfHistConfVarTable.setStatus("mandatory")
_MnPrPerfHistConfVarEntry_Object = MibTableRow
mnPrPerfHistConfVarEntry = _MnPrPerfHistConfVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 14, 2, 1)
)
mnPrPerfHistConfVarEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrPerfHistConfVarIndex"),
)
if mibBuilder.loadTexts:
    mnPrPerfHistConfVarEntry.setStatus("mandatory")


class _MnPrPerfHistConfVarIndex_Type(Integer32):
    """Custom type mnPrPerfHistConfVarIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MnPrPerfHistConfVarIndex_Type.__name__ = "Integer32"
_MnPrPerfHistConfVarIndex_Object = MibTableColumn
mnPrPerfHistConfVarIndex = _MnPrPerfHistConfVarIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 14, 2, 1, 1),
    _MnPrPerfHistConfVarIndex_Type()
)
mnPrPerfHistConfVarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistConfVarIndex.setStatus("mandatory")
_MnPrPerfHistConfVarName_Type = DisplayString
_MnPrPerfHistConfVarName_Object = MibTableColumn
mnPrPerfHistConfVarName = _MnPrPerfHistConfVarName_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 14, 2, 1, 2),
    _MnPrPerfHistConfVarName_Type()
)
mnPrPerfHistConfVarName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrPerfHistConfVarName.setStatus("mandatory")
_MnPrPerfHistConfVarEnable_Type = TruthValue
_MnPrPerfHistConfVarEnable_Object = MibTableColumn
mnPrPerfHistConfVarEnable = _MnPrPerfHistConfVarEnable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 14, 2, 1, 3),
    _MnPrPerfHistConfVarEnable_Type()
)
mnPrPerfHistConfVarEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrPerfHistConfVarEnable.setStatus("mandatory")
_MnPrTribE1ConfTable_Object = MibTable
mnPrTribE1ConfTable = _MnPrTribE1ConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 15)
)
if mibBuilder.loadTexts:
    mnPrTribE1ConfTable.setStatus("mandatory")
_MnPrTribE1ConfEntry_Object = MibTableRow
mnPrTribE1ConfEntry = _MnPrTribE1ConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 15, 1)
)
mnPrTribE1ConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnTribIndex"),
)
if mibBuilder.loadTexts:
    mnPrTribE1ConfEntry.setStatus("mandatory")


class _MnPrTribE1ConfLineType_Type(Integer32):
    """Custom type mnPrTribE1ConfLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encodeHdb3B8zs", 1),
          ("encodeAmi", 2))
    )


_MnPrTribE1ConfLineType_Type.__name__ = "Integer32"
_MnPrTribE1ConfLineType_Object = MibTableColumn
mnPrTribE1ConfLineType = _MnPrTribE1ConfLineType_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 15, 1, 1),
    _MnPrTribE1ConfLineType_Type()
)
mnPrTribE1ConfLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrTribE1ConfLineType.setStatus("mandatory")
_MnPrAuxConfTable_Object = MibTable
mnPrAuxConfTable = _MnPrAuxConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 16)
)
if mibBuilder.loadTexts:
    mnPrAuxConfTable.setStatus("mandatory")
_MnPrAuxConfEntry_Object = MibTableRow
mnPrAuxConfEntry = _MnPrAuxConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 16, 1)
)
mnPrAuxConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrAuxIndex"),
)
if mibBuilder.loadTexts:
    mnPrAuxConfEntry.setStatus("mandatory")


class _MnPrAuxIndex_Type(Integer32):
    """Custom type mnPrAuxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MnPrAuxIndex_Type.__name__ = "Integer32"
_MnPrAuxIndex_Object = MibTableColumn
mnPrAuxIndex = _MnPrAuxIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 16, 1, 1),
    _MnPrAuxIndex_Type()
)
mnPrAuxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrAuxIndex.setStatus("mandatory")


class _MnPrAuxConfBaudRate_Type(Integer32):
    """Custom type mnPrAuxConfBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9600,
              14400,
              19200,
              28800,
              38400,
              48000,
              56000,
              57600,
              64000)
        )
    )
    namedValues = NamedValues(
        *(("baud9600", 9600),
          ("baud14400", 14400),
          ("baud19200", 19200),
          ("baud28800", 28800),
          ("baud38400", 38400),
          ("baud48000", 48000),
          ("baud56000", 56000),
          ("baud57600", 57600),
          ("baud64000", 64000))
    )


_MnPrAuxConfBaudRate_Type.__name__ = "Integer32"
_MnPrAuxConfBaudRate_Object = MibTableColumn
mnPrAuxConfBaudRate = _MnPrAuxConfBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 16, 1, 2),
    _MnPrAuxConfBaudRate_Type()
)
mnPrAuxConfBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrAuxConfBaudRate.setStatus("mandatory")


class _MnPrAuxConfParity_Type(Integer32):
    """Custom type mnPrAuxConfParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noParity", 1),
          ("evenParity", 2),
          ("oddParity", 3))
    )


_MnPrAuxConfParity_Type.__name__ = "Integer32"
_MnPrAuxConfParity_Object = MibTableColumn
mnPrAuxConfParity = _MnPrAuxConfParity_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 16, 1, 3),
    _MnPrAuxConfParity_Type()
)
mnPrAuxConfParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrAuxConfParity.setStatus("mandatory")


class _MnPrAuxConfInversion_Type(Integer32):
    """Custom type mnPrAuxConfInversion based on Integer32"""
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
        *(("noInversion", 1),
          ("invertInput", 2),
          ("invertOutput", 3),
          ("invertBoth", 4))
    )


_MnPrAuxConfInversion_Type.__name__ = "Integer32"
_MnPrAuxConfInversion_Object = MibTableColumn
mnPrAuxConfInversion = _MnPrAuxConfInversion_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 16, 1, 4),
    _MnPrAuxConfInversion_Type()
)
mnPrAuxConfInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrAuxConfInversion.setStatus("mandatory")


class _MnPrAuxConfStopBits_Type(Integer32):
    """Custom type mnPrAuxConfStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneStopBit", 1),
          ("twoStopBits", 2))
    )


_MnPrAuxConfStopBits_Type.__name__ = "Integer32"
_MnPrAuxConfStopBits_Object = MibTableColumn
mnPrAuxConfStopBits = _MnPrAuxConfStopBits_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 16, 1, 5),
    _MnPrAuxConfStopBits_Type()
)
mnPrAuxConfStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrAuxConfStopBits.setStatus("mandatory")
_MnPrEthPortConfTable_Object = MibTable
mnPrEthPortConfTable = _MnPrEthPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 17)
)
if mibBuilder.loadTexts:
    mnPrEthPortConfTable.setStatus("mandatory")
_MnPrEthPortConfEntry_Object = MibTableRow
mnPrEthPortConfEntry = _MnPrEthPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 17, 1)
)
mnPrEthPortConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrEthPortIndex"),
)
if mibBuilder.loadTexts:
    mnPrEthPortConfEntry.setStatus("mandatory")


class _MnPrEthPortIndex_Type(Integer32):
    """Custom type mnPrEthPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_MnPrEthPortIndex_Type.__name__ = "Integer32"
_MnPrEthPortIndex_Object = MibTableColumn
mnPrEthPortIndex = _MnPrEthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 17, 1, 1),
    _MnPrEthPortIndex_Type()
)
mnPrEthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrEthPortIndex.setStatus("mandatory")
_MnPrEthPortConfSpeed_Type = LanSpeed
_MnPrEthPortConfSpeed_Object = MibTableColumn
mnPrEthPortConfSpeed = _MnPrEthPortConfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 17, 1, 2),
    _MnPrEthPortConfSpeed_Type()
)
mnPrEthPortConfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrEthPortConfSpeed.setStatus("mandatory")
_MnPrSwitchPlaneConfTable_Object = MibTable
mnPrSwitchPlaneConfTable = _MnPrSwitchPlaneConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 18)
)
if mibBuilder.loadTexts:
    mnPrSwitchPlaneConfTable.setStatus("mandatory")
_MnPrSwitchPlaneConfEntry_Object = MibTableRow
mnPrSwitchPlaneConfEntry = _MnPrSwitchPlaneConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 18, 1)
)
mnPrSwitchPlaneConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrSwitchPlaneIndex"),
)
if mibBuilder.loadTexts:
    mnPrSwitchPlaneConfEntry.setStatus("mandatory")


class _MnPrSwitchPlaneIndex_Type(Integer32):
    """Custom type mnPrSwitchPlaneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_MnPrSwitchPlaneIndex_Type.__name__ = "Integer32"
_MnPrSwitchPlaneIndex_Object = MibTableColumn
mnPrSwitchPlaneIndex = _MnPrSwitchPlaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 18, 1, 1),
    _MnPrSwitchPlaneIndex_Type()
)
mnPrSwitchPlaneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrSwitchPlaneIndex.setStatus("mandatory")


class _MnPrSwitchPlaneConfStatus_Type(Integer32):
    """Custom type mnPrSwitchPlaneConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              7,
              11,
              15,
              19,
              23,
              27,
              31)
        )
    )
    namedValues = NamedValues(
        *(("isTrue", 1),
          ("isFalse", 2),
          ("oos", 3),
          ("is", 7),
          ("oosAlm", 11),
          ("isAlm", 15),
          ("oosOlr", 19),
          ("isOlr", 23),
          ("oosAlmOlr", 27),
          ("isAlmOlr", 31))
    )


_MnPrSwitchPlaneConfStatus_Type.__name__ = "Integer32"
_MnPrSwitchPlaneConfStatus_Object = MibTableColumn
mnPrSwitchPlaneConfStatus = _MnPrSwitchPlaneConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 18, 1, 2),
    _MnPrSwitchPlaneConfStatus_Type()
)
mnPrSwitchPlaneConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrSwitchPlaneConfStatus.setStatus("mandatory")
_MnPrSwitchPlaneConfOnlineReq_Type = TruthValue
_MnPrSwitchPlaneConfOnlineReq_Object = MibTableColumn
mnPrSwitchPlaneConfOnlineReq = _MnPrSwitchPlaneConfOnlineReq_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 18, 1, 3),
    _MnPrSwitchPlaneConfOnlineReq_Type()
)
mnPrSwitchPlaneConfOnlineReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSwitchPlaneConfOnlineReq.setStatus("mandatory")
_MnPrDpmCiConfTable_Object = MibTable
mnPrDpmCiConfTable = _MnPrDpmCiConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 19)
)
if mibBuilder.loadTexts:
    mnPrDpmCiConfTable.setStatus("mandatory")
_MnPrDpmCiConfEntry_Object = MibTableRow
mnPrDpmCiConfEntry = _MnPrDpmCiConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 19, 1)
)
mnPrDpmCiConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrDpmCiIndex"),
)
if mibBuilder.loadTexts:
    mnPrDpmCiConfEntry.setStatus("mandatory")


class _MnPrDpmCiIndex_Type(Integer32):
    """Custom type mnPrDpmCiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10001, 42999),
    )


_MnPrDpmCiIndex_Type.__name__ = "Integer32"
_MnPrDpmCiIndex_Object = MibTableColumn
mnPrDpmCiIndex = _MnPrDpmCiIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 19, 1, 1),
    _MnPrDpmCiIndex_Type()
)
mnPrDpmCiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrDpmCiIndex.setStatus("mandatory")
_MnPrDpmCiConfType_Type = Integer32
_MnPrDpmCiConfType_Object = MibTableColumn
mnPrDpmCiConfType = _MnPrDpmCiConfType_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 19, 1, 2),
    _MnPrDpmCiConfType_Type()
)
mnPrDpmCiConfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrDpmCiConfType.setStatus("mandatory")
_MnPrDpmCiConfFullName_Type = DisplayString
_MnPrDpmCiConfFullName_Object = MibTableColumn
mnPrDpmCiConfFullName = _MnPrDpmCiConfFullName_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 19, 1, 3),
    _MnPrDpmCiConfFullName_Type()
)
mnPrDpmCiConfFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrDpmCiConfFullName.setStatus("mandatory")
_MnPrDpmCiConfSharpCapable_Type = TruthValue
_MnPrDpmCiConfSharpCapable_Object = MibTableColumn
mnPrDpmCiConfSharpCapable = _MnPrDpmCiConfSharpCapable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 19, 1, 4),
    _MnPrDpmCiConfSharpCapable_Type()
)
mnPrDpmCiConfSharpCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrDpmCiConfSharpCapable.setStatus("mandatory")
_MnPrDpmCiConfActCgName_Type = DisplayString
_MnPrDpmCiConfActCgName_Object = MibTableColumn
mnPrDpmCiConfActCgName = _MnPrDpmCiConfActCgName_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 19, 1, 5),
    _MnPrDpmCiConfActCgName_Type()
)
mnPrDpmCiConfActCgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrDpmCiConfActCgName.setStatus("mandatory")
_MnPrDpmCiConfActSharpEnabled_Type = TruthValue
_MnPrDpmCiConfActSharpEnabled_Object = MibTableColumn
mnPrDpmCiConfActSharpEnabled = _MnPrDpmCiConfActSharpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 19, 1, 6),
    _MnPrDpmCiConfActSharpEnabled_Type()
)
mnPrDpmCiConfActSharpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrDpmCiConfActSharpEnabled.setStatus("mandatory")
_MnPrDpmCiConfActOtherIntf_Type = DisplayString
_MnPrDpmCiConfActOtherIntf_Object = MibTableColumn
mnPrDpmCiConfActOtherIntf = _MnPrDpmCiConfActOtherIntf_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 19, 1, 7),
    _MnPrDpmCiConfActOtherIntf_Type()
)
mnPrDpmCiConfActOtherIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrDpmCiConfActOtherIntf.setStatus("mandatory")
_MnPrDpmCiConfPropAvailable_Type = TruthValue
_MnPrDpmCiConfPropAvailable_Object = MibTableColumn
mnPrDpmCiConfPropAvailable = _MnPrDpmCiConfPropAvailable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 19, 1, 8),
    _MnPrDpmCiConfPropAvailable_Type()
)
mnPrDpmCiConfPropAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrDpmCiConfPropAvailable.setStatus("mandatory")
_MnPrDpmCiConfPropCgName_Type = DisplayString
_MnPrDpmCiConfPropCgName_Object = MibTableColumn
mnPrDpmCiConfPropCgName = _MnPrDpmCiConfPropCgName_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 19, 1, 9),
    _MnPrDpmCiConfPropCgName_Type()
)
mnPrDpmCiConfPropCgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrDpmCiConfPropCgName.setStatus("mandatory")
_MnPrDpmCiConfPropSharpEnabled_Type = TruthValue
_MnPrDpmCiConfPropSharpEnabled_Object = MibTableColumn
mnPrDpmCiConfPropSharpEnabled = _MnPrDpmCiConfPropSharpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 19, 1, 10),
    _MnPrDpmCiConfPropSharpEnabled_Type()
)
mnPrDpmCiConfPropSharpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrDpmCiConfPropSharpEnabled.setStatus("mandatory")
_MnPrDpmCiConfPropOtherIntf_Type = DisplayString
_MnPrDpmCiConfPropOtherIntf_Object = MibTableColumn
mnPrDpmCiConfPropOtherIntf = _MnPrDpmCiConfPropOtherIntf_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 19, 1, 11),
    _MnPrDpmCiConfPropOtherIntf_Type()
)
mnPrDpmCiConfPropOtherIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrDpmCiConfPropOtherIntf.setStatus("mandatory")
_MnPrDpmCgConfTable_Object = MibTable
mnPrDpmCgConfTable = _MnPrDpmCgConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 20)
)
if mibBuilder.loadTexts:
    mnPrDpmCgConfTable.setStatus("mandatory")
_MnPrDpmCgConfEntry_Object = MibTableRow
mnPrDpmCgConfEntry = _MnPrDpmCgConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 20, 1)
)
mnPrDpmCgConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrDpmCgIndex"),
)
if mibBuilder.loadTexts:
    mnPrDpmCgConfEntry.setStatus("mandatory")


class _MnPrDpmCgIndex_Type(Integer32):
    """Custom type mnPrDpmCgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1999),
    )


_MnPrDpmCgIndex_Type.__name__ = "Integer32"
_MnPrDpmCgIndex_Object = MibTableColumn
mnPrDpmCgIndex = _MnPrDpmCgIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 20, 1, 1),
    _MnPrDpmCgIndex_Type()
)
mnPrDpmCgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrDpmCgIndex.setStatus("mandatory")
_MnPrDpmCgConfName_Type = DisplayString
_MnPrDpmCgConfName_Object = MibTableColumn
mnPrDpmCgConfName = _MnPrDpmCgConfName_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 20, 1, 2),
    _MnPrDpmCgConfName_Type()
)
mnPrDpmCgConfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrDpmCgConfName.setStatus("mandatory")
_MnPrDpmCgConfType_Type = Integer32
_MnPrDpmCgConfType_Object = MibTableColumn
mnPrDpmCgConfType = _MnPrDpmCgConfType_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 20, 1, 3),
    _MnPrDpmCgConfType_Type()
)
mnPrDpmCgConfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrDpmCgConfType.setStatus("mandatory")
_MnPrDpmCgConfCount_Type = Integer32
_MnPrDpmCgConfCount_Object = MibTableColumn
mnPrDpmCgConfCount = _MnPrDpmCgConfCount_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 20, 1, 4),
    _MnPrDpmCgConfCount_Type()
)
mnPrDpmCgConfCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrDpmCgConfCount.setStatus("mandatory")
_MnPrDpmCgConfChMinRate_Type = Integer32
_MnPrDpmCgConfChMinRate_Object = MibTableColumn
mnPrDpmCgConfChMinRate = _MnPrDpmCgConfChMinRate_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 20, 1, 6),
    _MnPrDpmCgConfChMinRate_Type()
)
mnPrDpmCgConfChMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrDpmCgConfChMinRate.setStatus("mandatory")
_MnPrDpmCgConfChMaxRate_Type = Integer32
_MnPrDpmCgConfChMaxRate_Object = MibTableColumn
mnPrDpmCgConfChMaxRate = _MnPrDpmCgConfChMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 20, 1, 7),
    _MnPrDpmCgConfChMaxRate_Type()
)
mnPrDpmCgConfChMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrDpmCgConfChMaxRate.setStatus("mandatory")
_MnPrDpmCgConfChAllocRate_Type = Integer32
_MnPrDpmCgConfChAllocRate_Object = MibTableColumn
mnPrDpmCgConfChAllocRate = _MnPrDpmCgConfChAllocRate_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 20, 1, 8),
    _MnPrDpmCgConfChAllocRate_Type()
)
mnPrDpmCgConfChAllocRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrDpmCgConfChAllocRate.setStatus("mandatory")
_MnPrDpmCgConfIntf1_Type = DisplayString
_MnPrDpmCgConfIntf1_Object = MibTableColumn
mnPrDpmCgConfIntf1 = _MnPrDpmCgConfIntf1_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 20, 1, 9),
    _MnPrDpmCgConfIntf1_Type()
)
mnPrDpmCgConfIntf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrDpmCgConfIntf1.setStatus("mandatory")
_MnPrDpmCgConfSharpEnabled1_Type = TruthValue
_MnPrDpmCgConfSharpEnabled1_Object = MibTableColumn
mnPrDpmCgConfSharpEnabled1 = _MnPrDpmCgConfSharpEnabled1_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 20, 1, 10),
    _MnPrDpmCgConfSharpEnabled1_Type()
)
mnPrDpmCgConfSharpEnabled1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrDpmCgConfSharpEnabled1.setStatus("mandatory")
_MnPrDpmCgConfIntf2_Type = DisplayString
_MnPrDpmCgConfIntf2_Object = MibTableColumn
mnPrDpmCgConfIntf2 = _MnPrDpmCgConfIntf2_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 20, 1, 11),
    _MnPrDpmCgConfIntf2_Type()
)
mnPrDpmCgConfIntf2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrDpmCgConfIntf2.setStatus("mandatory")
_MnPrDpmCgConfSharpEnabled2_Type = TruthValue
_MnPrDpmCgConfSharpEnabled2_Object = MibTableColumn
mnPrDpmCgConfSharpEnabled2 = _MnPrDpmCgConfSharpEnabled2_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 20, 1, 12),
    _MnPrDpmCgConfSharpEnabled2_Type()
)
mnPrDpmCgConfSharpEnabled2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrDpmCgConfSharpEnabled2.setStatus("mandatory")
_MnPrDpmCgConfRowStatus_Type = RowStatus
_MnPrDpmCgConfRowStatus_Object = MibTableColumn
mnPrDpmCgConfRowStatus = _MnPrDpmCgConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 20, 1, 13),
    _MnPrDpmCgConfRowStatus_Type()
)
mnPrDpmCgConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrDpmCgConfRowStatus.setStatus("mandatory")
_MnPrSHARPChanTable_Object = MibTable
mnPrSHARPChanTable = _MnPrSHARPChanTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 21)
)
if mibBuilder.loadTexts:
    mnPrSHARPChanTable.setStatus("mandatory")
_MnPrSHARPChanEntry_Object = MibTableRow
mnPrSHARPChanEntry = _MnPrSHARPChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 21, 1)
)
mnPrSHARPChanEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrDpmCiIndex"),
)
if mibBuilder.loadTexts:
    mnPrSHARPChanEntry.setStatus("mandatory")


class _MnPrSHARPChanStatus_Type(Integer32):
    """Custom type mnPrSHARPChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("normal", 2),
          ("notProtected", 3),
          ("channelFail", 4),
          ("limFail", 5),
          ("unknown", 6))
    )


_MnPrSHARPChanStatus_Type.__name__ = "Integer32"
_MnPrSHARPChanStatus_Object = MibTableColumn
mnPrSHARPChanStatus = _MnPrSHARPChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 21, 1, 1),
    _MnPrSHARPChanStatus_Type()
)
mnPrSHARPChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrSHARPChanStatus.setStatus("mandatory")


class _MnPrSHARPChanActiveChan_Type(Integer32):
    """Custom type mnPrSHARPChanActiveChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("unknown", 3))
    )


_MnPrSHARPChanActiveChan_Type.__name__ = "Integer32"
_MnPrSHARPChanActiveChan_Object = MibTableColumn
mnPrSHARPChanActiveChan = _MnPrSHARPChanActiveChan_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 21, 1, 2),
    _MnPrSHARPChanActiveChan_Type()
)
mnPrSHARPChanActiveChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrSHARPChanActiveChan.setStatus("mandatory")
_MnPrSHARPChanMasterBER_Type = SHARPBERStatus
_MnPrSHARPChanMasterBER_Object = MibTableColumn
mnPrSHARPChanMasterBER = _MnPrSHARPChanMasterBER_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 21, 1, 3),
    _MnPrSHARPChanMasterBER_Type()
)
mnPrSHARPChanMasterBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrSHARPChanMasterBER.setStatus("mandatory")
_MnPrSHARPChanSlaveBER_Type = SHARPBERStatus
_MnPrSHARPChanSlaveBER_Object = MibTableColumn
mnPrSHARPChanSlaveBER = _MnPrSHARPChanSlaveBER_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 21, 1, 4),
    _MnPrSHARPChanSlaveBER_Type()
)
mnPrSHARPChanSlaveBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrSHARPChanSlaveBER.setStatus("mandatory")


class _MnPrSHARPChanEnable_Type(Integer32):
    """Custom type mnPrSHARPChanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_MnPrSHARPChanEnable_Type.__name__ = "Integer32"
_MnPrSHARPChanEnable_Object = MibTableColumn
mnPrSHARPChanEnable = _MnPrSHARPChanEnable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 21, 1, 6),
    _MnPrSHARPChanEnable_Type()
)
mnPrSHARPChanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSHARPChanEnable.setStatus("mandatory")


class _MnPrSHARPChanSwitchMode_Type(Integer32):
    """Custom type mnPrSHARPChanSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 2))
    )


_MnPrSHARPChanSwitchMode_Type.__name__ = "Integer32"
_MnPrSHARPChanSwitchMode_Object = MibTableColumn
mnPrSHARPChanSwitchMode = _MnPrSHARPChanSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 21, 1, 7),
    _MnPrSHARPChanSwitchMode_Type()
)
mnPrSHARPChanSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSHARPChanSwitchMode.setStatus("mandatory")
_MnPrSHARPChanMasterThresh_Type = SHARPBERThresh
_MnPrSHARPChanMasterThresh_Object = MibTableColumn
mnPrSHARPChanMasterThresh = _MnPrSHARPChanMasterThresh_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 21, 1, 8),
    _MnPrSHARPChanMasterThresh_Type()
)
mnPrSHARPChanMasterThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSHARPChanMasterThresh.setStatus("mandatory")
_MnPrSHARPChanSlaveThresh_Type = SHARPBERThresh
_MnPrSHARPChanSlaveThresh_Object = MibTableColumn
mnPrSHARPChanSlaveThresh = _MnPrSHARPChanSlaveThresh_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 21, 1, 9),
    _MnPrSHARPChanSlaveThresh_Type()
)
mnPrSHARPChanSlaveThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSHARPChanSlaveThresh.setStatus("mandatory")


class _MnPrSHARPChanManualForce_Type(Integer32):
    """Custom type mnPrSHARPChanManualForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noForce", 1),
          ("forceMaster", 2),
          ("forceSlave", 3),
          ("forceMasterOperNA", 4),
          ("forceSlaveOperNA", 5))
    )


_MnPrSHARPChanManualForce_Type.__name__ = "Integer32"
_MnPrSHARPChanManualForce_Object = MibTableColumn
mnPrSHARPChanManualForce = _MnPrSHARPChanManualForce_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 21, 1, 10),
    _MnPrSHARPChanManualForce_Type()
)
mnPrSHARPChanManualForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSHARPChanManualForce.setStatus("mandatory")


class _MnPrSHARPChanSwitchPref_Type(Integer32):
    """Custom type mnPrSHARPChanSwitchPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noPreference", 1),
          ("masterNonRevert", 2),
          ("masterRevert", 3),
          ("slaveNonRevert", 4),
          ("slaveRevert", 5))
    )


_MnPrSHARPChanSwitchPref_Type.__name__ = "Integer32"
_MnPrSHARPChanSwitchPref_Object = MibTableColumn
mnPrSHARPChanSwitchPref = _MnPrSHARPChanSwitchPref_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 21, 1, 11),
    _MnPrSHARPChanSwitchPref_Type()
)
mnPrSHARPChanSwitchPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSHARPChanSwitchPref.setStatus("mandatory")
_MnPrTribXConfTable_Object = MibTable
mnPrTribXConfTable = _MnPrTribXConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 22)
)
if mibBuilder.loadTexts:
    mnPrTribXConfTable.setStatus("mandatory")
_MnPrTribXConfEntry_Object = MibTableRow
mnPrTribXConfEntry = _MnPrTribXConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 22, 1)
)
mnPrTribXConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrDpmCiIndex"),
)
if mibBuilder.loadTexts:
    mnPrTribXConfEntry.setStatus("mandatory")
_MnPrTribXConfAdminEquipped_Type = TruthValue
_MnPrTribXConfAdminEquipped_Object = MibTableColumn
mnPrTribXConfAdminEquipped = _MnPrTribXConfAdminEquipped_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 22, 1, 1),
    _MnPrTribXConfAdminEquipped_Type()
)
mnPrTribXConfAdminEquipped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrTribXConfAdminEquipped.setStatus("mandatory")


class _MnPrTribXConfLineType_Type(Integer32):
    """Custom type mnPrTribXConfLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encodeHdb3B8zs", 1),
          ("encodeAmi", 2))
    )


_MnPrTribXConfLineType_Type.__name__ = "Integer32"
_MnPrTribXConfLineType_Object = MibTableColumn
mnPrTribXConfLineType = _MnPrTribXConfLineType_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 22, 1, 2),
    _MnPrTribXConfLineType_Type()
)
mnPrTribXConfLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrTribXConfLineType.setStatus("mandatory")
_MnPrTribXConfLocalLoopback_Type = TruthValue
_MnPrTribXConfLocalLoopback_Object = MibTableColumn
mnPrTribXConfLocalLoopback = _MnPrTribXConfLocalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 22, 1, 3),
    _MnPrTribXConfLocalLoopback_Type()
)
mnPrTribXConfLocalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrTribXConfLocalLoopback.setStatus("mandatory")
_MnPrTribXConfRemoteLoopback_Type = TruthValue
_MnPrTribXConfRemoteLoopback_Object = MibTableColumn
mnPrTribXConfRemoteLoopback = _MnPrTribXConfRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 22, 1, 4),
    _MnPrTribXConfRemoteLoopback_Type()
)
mnPrTribXConfRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrTribXConfRemoteLoopback.setStatus("mandatory")
_MnPrTribXConfTribStatus_Type = Integer32
_MnPrTribXConfTribStatus_Object = MibTableColumn
mnPrTribXConfTribStatus = _MnPrTribXConfTribStatus_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 22, 1, 5),
    _MnPrTribXConfTribStatus_Type()
)
mnPrTribXConfTribStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrTribXConfTribStatus.setStatus("mandatory")
_MnPrEthSwTable_Object = MibTable
mnPrEthSwTable = _MnPrEthSwTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 23)
)
if mibBuilder.loadTexts:
    mnPrEthSwTable.setStatus("mandatory")
_MnPrEthSwEntry_Object = MibTableRow
mnPrEthSwEntry = _MnPrEthSwEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 23, 1)
)
mnPrEthSwEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrEthSwIndex"),
)
if mibBuilder.loadTexts:
    mnPrEthSwEntry.setStatus("mandatory")


class _MnPrEthSwIndex_Type(Integer32):
    """Custom type mnPrEthSwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_MnPrEthSwIndex_Type.__name__ = "Integer32"
_MnPrEthSwIndex_Object = MibTableColumn
mnPrEthSwIndex = _MnPrEthSwIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 23, 1, 1),
    _MnPrEthSwIndex_Type()
)
mnPrEthSwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrEthSwIndex.setStatus("mandatory")


class _MnPrEthSwStatRRPStatus_Type(Integer32):
    """Custom type mnPrEthSwStatRRPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ringok", 1),
          ("ringbroken", 2),
          ("offline", 3),
          ("notapplicable", 4),
          ("notsupported", 5))
    )


_MnPrEthSwStatRRPStatus_Type.__name__ = "Integer32"
_MnPrEthSwStatRRPStatus_Object = MibTableColumn
mnPrEthSwStatRRPStatus = _MnPrEthSwStatRRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 23, 1, 2),
    _MnPrEthSwStatRRPStatus_Type()
)
mnPrEthSwStatRRPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrEthSwStatRRPStatus.setStatus("mandatory")


class _MnPrEthSwConfRRPMode_Type(Integer32):
    """Custom type mnPrEthSwConfRRPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("passthrough", 2),
          ("switch", 3))
    )


_MnPrEthSwConfRRPMode_Type.__name__ = "Integer32"
_MnPrEthSwConfRRPMode_Object = MibTableColumn
mnPrEthSwConfRRPMode = _MnPrEthSwConfRRPMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 23, 1, 3),
    _MnPrEthSwConfRRPMode_Type()
)
mnPrEthSwConfRRPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrEthSwConfRRPMode.setStatus("mandatory")


class _MnPrEthSwConfRRPPollInterval_Type(Integer32):
    """Custom type mnPrEthSwConfRRPPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_MnPrEthSwConfRRPPollInterval_Type.__name__ = "Integer32"
_MnPrEthSwConfRRPPollInterval_Object = MibTableColumn
mnPrEthSwConfRRPPollInterval = _MnPrEthSwConfRRPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 23, 1, 4),
    _MnPrEthSwConfRRPPollInterval_Type()
)
mnPrEthSwConfRRPPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrEthSwConfRRPPollInterval.setStatus("mandatory")


class _MnPrEthSwConfRRPThreshold_Type(Integer32):
    """Custom type mnPrEthSwConfRRPThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 50000),
    )


_MnPrEthSwConfRRPThreshold_Type.__name__ = "Integer32"
_MnPrEthSwConfRRPThreshold_Object = MibTableColumn
mnPrEthSwConfRRPThreshold = _MnPrEthSwConfRRPThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 23, 1, 5),
    _MnPrEthSwConfRRPThreshold_Type()
)
mnPrEthSwConfRRPThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrEthSwConfRRPThreshold.setStatus("mandatory")


class _MnPrEthSwConfRRPFwdDelay_Type(Integer32):
    """Custom type mnPrEthSwConfRRPFwdDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_MnPrEthSwConfRRPFwdDelay_Type.__name__ = "Integer32"
_MnPrEthSwConfRRPFwdDelay_Object = MibTableColumn
mnPrEthSwConfRRPFwdDelay = _MnPrEthSwConfRRPFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 23, 1, 6),
    _MnPrEthSwConfRRPFwdDelay_Type()
)
mnPrEthSwConfRRPFwdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrEthSwConfRRPFwdDelay.setStatus("mandatory")
_MnPrEthSwConfRRPRingID_Type = DisplayString
_MnPrEthSwConfRRPRingID_Object = MibTableColumn
mnPrEthSwConfRRPRingID = _MnPrEthSwConfRRPRingID_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 23, 1, 7),
    _MnPrEthSwConfRRPRingID_Type()
)
mnPrEthSwConfRRPRingID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrEthSwConfRRPRingID.setStatus("mandatory")
_MnPrAcmTable_Object = MibTable
mnPrAcmTable = _MnPrAcmTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 24)
)
if mibBuilder.loadTexts:
    mnPrAcmTable.setStatus("mandatory")
_MnPrAcmEntry_Object = MibTableRow
mnPrAcmEntry = _MnPrAcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 24, 1)
)
mnPrAcmEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
)
if mibBuilder.loadTexts:
    mnPrAcmEntry.setStatus("mandatory")


class _MnPrAcmModeProp_Type(Integer32):
    """Custom type mnPrAcmModeProp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acmdisabled", 1),
          ("acmrxtx", 2))
    )


_MnPrAcmModeProp_Type.__name__ = "Integer32"
_MnPrAcmModeProp_Object = MibTableColumn
mnPrAcmModeProp = _MnPrAcmModeProp_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 24, 1, 1),
    _MnPrAcmModeProp_Type()
)
mnPrAcmModeProp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrAcmModeProp.setStatus("mandatory")


class _MnPrAcmModeConf_Type(Integer32):
    """Custom type mnPrAcmModeConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acmdisabled", 1),
          ("acmrxtx", 2))
    )


_MnPrAcmModeConf_Type.__name__ = "Integer32"
_MnPrAcmModeConf_Object = MibTableColumn
mnPrAcmModeConf = _MnPrAcmModeConf_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 24, 1, 2),
    _MnPrAcmModeConf_Type()
)
mnPrAcmModeConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrAcmModeConf.setStatus("mandatory")
_MnPrAcmMaxCapProp_Type = Integer32
_MnPrAcmMaxCapProp_Object = MibTableColumn
mnPrAcmMaxCapProp = _MnPrAcmMaxCapProp_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 24, 1, 3),
    _MnPrAcmMaxCapProp_Type()
)
mnPrAcmMaxCapProp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrAcmMaxCapProp.setStatus("mandatory")
_MnPrAcmMaxCapConf_Type = Integer32
_MnPrAcmMaxCapConf_Object = MibTableColumn
mnPrAcmMaxCapConf = _MnPrAcmMaxCapConf_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 24, 1, 4),
    _MnPrAcmMaxCapConf_Type()
)
mnPrAcmMaxCapConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrAcmMaxCapConf.setStatus("mandatory")
_MnPrAcmMinEthThreshProp_Type = Integer32
_MnPrAcmMinEthThreshProp_Object = MibTableColumn
mnPrAcmMinEthThreshProp = _MnPrAcmMinEthThreshProp_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 24, 1, 5),
    _MnPrAcmMinEthThreshProp_Type()
)
mnPrAcmMinEthThreshProp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrAcmMinEthThreshProp.setStatus("mandatory")
_MnPrAcmMinEthThreshConf_Type = Integer32
_MnPrAcmMinEthThreshConf_Object = MibTableColumn
mnPrAcmMinEthThreshConf = _MnPrAcmMinEthThreshConf_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 24, 1, 6),
    _MnPrAcmMinEthThreshConf_Type()
)
mnPrAcmMinEthThreshConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrAcmMinEthThreshConf.setStatus("mandatory")
_MnPrAcmTxPower_Type = Integer32
_MnPrAcmTxPower_Object = MibTableColumn
mnPrAcmTxPower = _MnPrAcmTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 24, 1, 7),
    _MnPrAcmTxPower_Type()
)
mnPrAcmTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrAcmTxPower.setStatus("mandatory")
_MnPrAcmMaxTxPower_Type = Integer32
_MnPrAcmMaxTxPower_Object = MibTableColumn
mnPrAcmMaxTxPower = _MnPrAcmMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 24, 1, 8),
    _MnPrAcmMaxTxPower_Type()
)
mnPrAcmMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrAcmMaxTxPower.setStatus("mandatory")
_MnPrAcmProfileHeader_Type = DisplayString
_MnPrAcmProfileHeader_Object = MibTableColumn
mnPrAcmProfileHeader = _MnPrAcmProfileHeader_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 24, 1, 9),
    _MnPrAcmProfileHeader_Type()
)
mnPrAcmProfileHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrAcmProfileHeader.setStatus("mandatory")
_MnPrAcmProfileTable_Object = MibTable
mnPrAcmProfileTable = _MnPrAcmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 25)
)
if mibBuilder.loadTexts:
    mnPrAcmProfileTable.setStatus("mandatory")
_MnPrAcmProfileEntry_Object = MibTableRow
mnPrAcmProfileEntry = _MnPrAcmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 25, 1)
)
mnPrAcmProfileEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrAcmProfileIndex"),
)
if mibBuilder.loadTexts:
    mnPrAcmProfileEntry.setStatus("mandatory")


class _MnPrAcmProfileIndex_Type(Integer32):
    """Custom type mnPrAcmProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MnPrAcmProfileIndex_Type.__name__ = "Integer32"
_MnPrAcmProfileIndex_Object = MibTableColumn
mnPrAcmProfileIndex = _MnPrAcmProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 25, 1, 1),
    _MnPrAcmProfileIndex_Type()
)
mnPrAcmProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrAcmProfileIndex.setStatus("mandatory")
_MnPrAcmProfileText_Type = DisplayString
_MnPrAcmProfileText_Object = MibTableColumn
mnPrAcmProfileText = _MnPrAcmProfileText_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 25, 1, 2),
    _MnPrAcmProfileText_Type()
)
mnPrAcmProfileText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrAcmProfileText.setStatus("mandatory")
_MnPrRADSrvConfTable_Object = MibTable
mnPrRADSrvConfTable = _MnPrRADSrvConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 26)
)
if mibBuilder.loadTexts:
    mnPrRADSrvConfTable.setStatus("mandatory")
_MnPrRADSrvConfEntry_Object = MibTableRow
mnPrRADSrvConfEntry = _MnPrRADSrvConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 26, 1)
)
mnPrRADSrvConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrRADSrvIndex"),
)
if mibBuilder.loadTexts:
    mnPrRADSrvConfEntry.setStatus("mandatory")


class _MnPrRADSrvIndex_Type(Integer32):
    """Custom type mnPrRADSrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MnPrRADSrvIndex_Type.__name__ = "Integer32"
_MnPrRADSrvIndex_Object = MibTableColumn
mnPrRADSrvIndex = _MnPrRADSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 26, 1, 1),
    _MnPrRADSrvIndex_Type()
)
mnPrRADSrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRADSrvIndex.setStatus("mandatory")
_MnPrRADSrvConfName_Type = DisplayString
_MnPrRADSrvConfName_Object = MibTableColumn
mnPrRADSrvConfName = _MnPrRADSrvConfName_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 26, 1, 2),
    _MnPrRADSrvConfName_Type()
)
mnPrRADSrvConfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRADSrvConfName.setStatus("mandatory")


class _MnPrRADSrvConfAuthPort_Type(Integer32):
    """Custom type mnPrRADSrvConfAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_MnPrRADSrvConfAuthPort_Type.__name__ = "Integer32"
_MnPrRADSrvConfAuthPort_Object = MibTableColumn
mnPrRADSrvConfAuthPort = _MnPrRADSrvConfAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 26, 1, 3),
    _MnPrRADSrvConfAuthPort_Type()
)
mnPrRADSrvConfAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRADSrvConfAuthPort.setStatus("mandatory")
_MnPrRADSrvConfSecret_Type = DisplayString
_MnPrRADSrvConfSecret_Object = MibTableColumn
mnPrRADSrvConfSecret = _MnPrRADSrvConfSecret_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 26, 1, 4),
    _MnPrRADSrvConfSecret_Type()
)
mnPrRADSrvConfSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRADSrvConfSecret.setStatus("mandatory")
_MnPrRRPPTable_Object = MibTable
mnPrRRPPTable = _MnPrRRPPTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27)
)
if mibBuilder.loadTexts:
    mnPrRRPPTable.setStatus("mandatory")
_MnPrRRPPEntry_Object = MibTableRow
mnPrRRPPEntry = _MnPrRRPPEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27, 1)
)
mnPrRRPPEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrRRPPIndex"),
)
if mibBuilder.loadTexts:
    mnPrRRPPEntry.setStatus("mandatory")


class _MnPrRRPPIndex_Type(Integer32):
    """Custom type mnPrRRPPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MnPrRRPPIndex_Type.__name__ = "Integer32"
_MnPrRRPPIndex_Object = MibTableColumn
mnPrRRPPIndex = _MnPrRRPPIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27, 1, 1),
    _MnPrRRPPIndex_Type()
)
mnPrRRPPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRRPPIndex.setStatus("mandatory")
_MnPrRRPPRowStatus_Type = RowStatus
_MnPrRRPPRowStatus_Object = MibTableColumn
mnPrRRPPRowStatus = _MnPrRRPPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27, 1, 2),
    _MnPrRRPPRowStatus_Type()
)
mnPrRRPPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRRPPRowStatus.setStatus("mandatory")


class _MnPrRRPPStatus_Type(Integer32):
    """Custom type mnPrRRPPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ringok", 1),
          ("ringbroken", 2),
          ("offline", 3),
          ("notapplicable", 4),
          ("notsupported", 5))
    )


_MnPrRRPPStatus_Type.__name__ = "Integer32"
_MnPrRRPPStatus_Object = MibTableColumn
mnPrRRPPStatus = _MnPrRRPPStatus_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27, 1, 3),
    _MnPrRRPPStatus_Type()
)
mnPrRRPPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRRPPStatus.setStatus("mandatory")


class _MnPrRRPPConfMode_Type(Integer32):
    """Custom type mnPrRRPPConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("passthrough", 2),
          ("switch", 3))
    )


_MnPrRRPPConfMode_Type.__name__ = "Integer32"
_MnPrRRPPConfMode_Object = MibTableColumn
mnPrRRPPConfMode = _MnPrRRPPConfMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27, 1, 4),
    _MnPrRRPPConfMode_Type()
)
mnPrRRPPConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRRPPConfMode.setStatus("mandatory")


class _MnPrRRPPConfPollInterval_Type(Integer32):
    """Custom type mnPrRRPPConfPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_MnPrRRPPConfPollInterval_Type.__name__ = "Integer32"
_MnPrRRPPConfPollInterval_Object = MibTableColumn
mnPrRRPPConfPollInterval = _MnPrRRPPConfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27, 1, 5),
    _MnPrRRPPConfPollInterval_Type()
)
mnPrRRPPConfPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRRPPConfPollInterval.setStatus("mandatory")


class _MnPrRRPPConfThreshold_Type(Integer32):
    """Custom type mnPrRRPPConfThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 50000),
    )


_MnPrRRPPConfThreshold_Type.__name__ = "Integer32"
_MnPrRRPPConfThreshold_Object = MibTableColumn
mnPrRRPPConfThreshold = _MnPrRRPPConfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27, 1, 6),
    _MnPrRRPPConfThreshold_Type()
)
mnPrRRPPConfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRRPPConfThreshold.setStatus("mandatory")


class _MnPrRRPPConfFwdDelay_Type(Integer32):
    """Custom type mnPrRRPPConfFwdDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_MnPrRRPPConfFwdDelay_Type.__name__ = "Integer32"
_MnPrRRPPConfFwdDelay_Object = MibTableColumn
mnPrRRPPConfFwdDelay = _MnPrRRPPConfFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27, 1, 7),
    _MnPrRRPPConfFwdDelay_Type()
)
mnPrRRPPConfFwdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRRPPConfFwdDelay.setStatus("mandatory")


class _MnPrRRPPConfLdpVlan_Type(Integer32):
    """Custom type mnPrRRPPConfLdpVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MnPrRRPPConfLdpVlan_Type.__name__ = "Integer32"
_MnPrRRPPConfLdpVlan_Object = MibTableColumn
mnPrRRPPConfLdpVlan = _MnPrRRPPConfLdpVlan_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27, 1, 8),
    _MnPrRRPPConfLdpVlan_Type()
)
mnPrRRPPConfLdpVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRRPPConfLdpVlan.setStatus("mandatory")


class _MnPrRRPPConfRingPort1_Type(Integer32):
    """Custom type mnPrRRPPConfRingPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 21),
    )


_MnPrRRPPConfRingPort1_Type.__name__ = "Integer32"
_MnPrRRPPConfRingPort1_Object = MibTableColumn
mnPrRRPPConfRingPort1 = _MnPrRRPPConfRingPort1_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27, 1, 9),
    _MnPrRRPPConfRingPort1_Type()
)
mnPrRRPPConfRingPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRRPPConfRingPort1.setStatus("mandatory")


class _MnPrRRPPConfRingPort2_Type(Integer32):
    """Custom type mnPrRRPPConfRingPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 21),
    )


_MnPrRRPPConfRingPort2_Type.__name__ = "Integer32"
_MnPrRRPPConfRingPort2_Object = MibTableColumn
mnPrRRPPConfRingPort2 = _MnPrRRPPConfRingPort2_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27, 1, 10),
    _MnPrRRPPConfRingPort2_Type()
)
mnPrRRPPConfRingPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrRRPPConfRingPort2.setStatus("mandatory")
_MnPrRRPPConfProtVlans_Type = DisplayString
_MnPrRRPPConfProtVlans_Object = MibTableColumn
mnPrRRPPConfProtVlans = _MnPrRRPPConfProtVlans_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27, 1, 11),
    _MnPrRRPPConfProtVlans_Type()
)
mnPrRRPPConfProtVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRRPPConfProtVlans.setStatus("mandatory")
_MnPrRRPPConfADPorts_Type = DisplayString
_MnPrRRPPConfADPorts_Object = MibTableColumn
mnPrRRPPConfADPorts = _MnPrRRPPConfADPorts_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27, 1, 12),
    _MnPrRRPPConfADPorts_Type()
)
mnPrRRPPConfADPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRRPPConfADPorts.setStatus("mandatory")
_MnPrRRPPADPortAvailability_Type = Display64
_MnPrRRPPADPortAvailability_Object = MibTableColumn
mnPrRRPPADPortAvailability = _MnPrRRPPADPortAvailability_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 27, 1, 13),
    _MnPrRRPPADPortAvailability_Type()
)
mnPrRRPPADPortAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrRRPPADPortAvailability.setStatus("mandatory")
_MnPrCUConfTable_Object = MibTable
mnPrCUConfTable = _MnPrCUConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 28)
)
if mibBuilder.loadTexts:
    mnPrCUConfTable.setStatus("mandatory")
_MnPrCUConfEntry_Object = MibTableRow
mnPrCUConfEntry = _MnPrCUConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 28, 1)
)
mnPrCUConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
)
if mibBuilder.loadTexts:
    mnPrCUConfEntry.setStatus("mandatory")


class _MnPrCUConfRRPPLLFHysterSetTime_Type(Integer32):
    """Custom type mnPrCUConfRRPPLLFHysterSetTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MnPrCUConfRRPPLLFHysterSetTime_Type.__name__ = "Integer32"
_MnPrCUConfRRPPLLFHysterSetTime_Object = MibTableColumn
mnPrCUConfRRPPLLFHysterSetTime = _MnPrCUConfRRPPLLFHysterSetTime_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 28, 1, 1),
    _MnPrCUConfRRPPLLFHysterSetTime_Type()
)
mnPrCUConfRRPPLLFHysterSetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrCUConfRRPPLLFHysterSetTime.setStatus("mandatory")


class _MnPrCUConfRRPPLLFHysterClrTime_Type(Integer32):
    """Custom type mnPrCUConfRRPPLLFHysterClrTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MnPrCUConfRRPPLLFHysterClrTime_Type.__name__ = "Integer32"
_MnPrCUConfRRPPLLFHysterClrTime_Object = MibTableColumn
mnPrCUConfRRPPLLFHysterClrTime = _MnPrCUConfRRPPLLFHysterClrTime_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 6, 28, 1, 2),
    _MnPrCUConfRRPPLLFHysterClrTime_Type()
)
mnPrCUConfRRPPLLFHysterClrTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrCUConfRRPPLLFHysterClrTime.setStatus("mandatory")
_MnPrUtilityObjects_ObjectIdentity = ObjectIdentity
mnPrUtilityObjects = _MnPrUtilityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 7)
)
_MnPrSCPCtlTable_Object = MibTable
mnPrSCPCtlTable = _MnPrSCPCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 7, 1)
)
if mibBuilder.loadTexts:
    mnPrSCPCtlTable.setStatus("mandatory")
_MnPrSCPCtlEntry_Object = MibTableRow
mnPrSCPCtlEntry = _MnPrSCPCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 7, 1, 1)
)
mnPrSCPCtlEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
)
if mibBuilder.loadTexts:
    mnPrSCPCtlEntry.setStatus("mandatory")


class _MnPrSCPCtlCmd_Type(Integer32):
    """Custom type mnPrSCPCtlCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              39,
              40,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("resetLatchedAlarms", 2),
          ("resetCustomPerformanceInterval", 3),
          ("bootPrimaryImage", 4),
          ("bootSecondaryImage", 5),
          ("reconfigureModem", 6),
          ("restoreConfFactoryDefaults", 7),
          ("copySWSecImageToPriImage", 8),
          ("copySWPriImageToSecImage", 9),
          ("tftpDownloadSWBootloader", 10),
          ("tftpDownloadSWSecondaryImage", 11),
          ("tftpDownloadFpgaModemTx", 12),
          ("tftpDownloadFpgaModemRx", 13),
          ("tftpDownloadFpgaE1", 14),
          ("tftpDownloadFpgaE3", 15),
          ("tftpDownloadImage", 16),
          ("alarmSetClear", 17),
          ("tftpDownloadFpgaEth", 18),
          ("sshKeyGen", 19),
          ("sntpPollNow", 20),
          ("sendPING", 21),
          ("resetAlarmLog", 22),
          ("resetEventLog", 23),
          ("copySWSecImageFromFarToNear", 24),
          ("restoreAlarmFactoryDefaults", 25),
          ("changeAggregateBERT", 26),
          ("resetLimABERTStats", 27),
          ("resetLimBBERTStats", 28),
          ("resetAggBERTStats", 29),
          ("resetPerformanceHistory", 30),
          ("uploadPerformanceHistory", 31),
          ("resendTraps", 32),
          ("copyImage", 33),
          ("evaluateConfig", 34),
          ("passwordChangeResponse", 35),
          ("copySIM", 36),
          ("modifyChannelGroups", 37),
          ("synchPerformanceHistory", 39),
          ("revertPropToCurConfig", 40),
          ("resetSystemLog", 41),
          ("resetEthStats", 42),
          ("uploadDiagSnapshot", 43),
          ("addRrppVlan", 44))
    )


_MnPrSCPCtlCmd_Type.__name__ = "Integer32"
_MnPrSCPCtlCmd_Object = MibTableColumn
mnPrSCPCtlCmd = _MnPrSCPCtlCmd_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 7, 1, 1, 1),
    _MnPrSCPCtlCmd_Type()
)
mnPrSCPCtlCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSCPCtlCmd.setStatus("mandatory")
_MnPrSCPCtlCmdStringArg_Type = DisplayString
_MnPrSCPCtlCmdStringArg_Object = MibTableColumn
mnPrSCPCtlCmdStringArg = _MnPrSCPCtlCmdStringArg_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 7, 1, 1, 2),
    _MnPrSCPCtlCmdStringArg_Type()
)
mnPrSCPCtlCmdStringArg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSCPCtlCmdStringArg.setStatus("mandatory")
_MnPrSCPCtlCmdNumArg_Type = Integer32
_MnPrSCPCtlCmdNumArg_Object = MibTableColumn
mnPrSCPCtlCmdNumArg = _MnPrSCPCtlCmdNumArg_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 7, 1, 1, 3),
    _MnPrSCPCtlCmdNumArg_Type()
)
mnPrSCPCtlCmdNumArg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrSCPCtlCmdNumArg.setStatus("mandatory")


class _MnPrSCPCtlCmdProgress_Type(Integer32):
    """Custom type mnPrSCPCtlCmdProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MnPrSCPCtlCmdProgress_Type.__name__ = "Integer32"
_MnPrSCPCtlCmdProgress_Object = MibTableColumn
mnPrSCPCtlCmdProgress = _MnPrSCPCtlCmdProgress_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 7, 1, 1, 4),
    _MnPrSCPCtlCmdProgress_Type()
)
mnPrSCPCtlCmdProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrSCPCtlCmdProgress.setStatus("mandatory")


class _MnPrSCPCtlCmdResult_Type(Integer32):
    """Custom type mnPrSCPCtlCmdResult based on Integer32"""
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
        *(("inProgress", 1),
          ("success", 2),
          ("failure", 3),
          ("aborted", 4))
    )


_MnPrSCPCtlCmdResult_Type.__name__ = "Integer32"
_MnPrSCPCtlCmdResult_Object = MibTableColumn
mnPrSCPCtlCmdResult = _MnPrSCPCtlCmdResult_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 7, 1, 1, 5),
    _MnPrSCPCtlCmdResult_Type()
)
mnPrSCPCtlCmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrSCPCtlCmdResult.setStatus("mandatory")
_MnPrDiagSnapTable_Object = MibTable
mnPrDiagSnapTable = _MnPrDiagSnapTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 7, 2)
)
if mibBuilder.loadTexts:
    mnPrDiagSnapTable.setStatus("mandatory")
_MnPrDiagSnapEntry_Object = MibTableRow
mnPrDiagSnapEntry = _MnPrDiagSnapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 7, 2, 1)
)
mnPrDiagSnapEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
)
if mibBuilder.loadTexts:
    mnPrDiagSnapEntry.setStatus("mandatory")


class _MnPrDiagSnapBuffer_Type(OctetString):
    """Custom type mnPrDiagSnapBuffer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_MnPrDiagSnapBuffer_Type.__name__ = "OctetString"
_MnPrDiagSnapBuffer_Object = MibTableColumn
mnPrDiagSnapBuffer = _MnPrDiagSnapBuffer_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 7, 2, 1, 1),
    _MnPrDiagSnapBuffer_Type()
)
mnPrDiagSnapBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrDiagSnapBuffer.setStatus("mandatory")


class _MnPrDiagSnapSource_Type(Integer32):
    """Custom type mnPrDiagSnapSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("adcoutput", 2),
          ("slicerinput", 3))
    )


_MnPrDiagSnapSource_Type.__name__ = "Integer32"
_MnPrDiagSnapSource_Object = MibTableColumn
mnPrDiagSnapSource = _MnPrDiagSnapSource_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 7, 2, 1, 2),
    _MnPrDiagSnapSource_Type()
)
mnPrDiagSnapSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrDiagSnapSource.setStatus("mandatory")


class _MnPrDiagSnapOverride_Type(Integer32):
    """Custom type mnPrDiagSnapOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("override", 2))
    )


_MnPrDiagSnapOverride_Type.__name__ = "Integer32"
_MnPrDiagSnapOverride_Object = MibTableColumn
mnPrDiagSnapOverride = _MnPrDiagSnapOverride_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 7, 2, 1, 3),
    _MnPrDiagSnapOverride_Type()
)
mnPrDiagSnapOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrDiagSnapOverride.setStatus("mandatory")
_MnPrVlanObjects_ObjectIdentity = ObjectIdentity
mnPrVlanObjects = _MnPrVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8)
)
_MnPrVlanDeviceConfTable_Object = MibTable
mnPrVlanDeviceConfTable = _MnPrVlanDeviceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mnPrVlanDeviceConfTable.setStatus("mandatory")
_MnPrVlanDeviceConfEntry_Object = MibTableRow
mnPrVlanDeviceConfEntry = _MnPrVlanDeviceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1)
)
mnPrVlanDeviceConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnLIMIndex"),
)
if mibBuilder.loadTexts:
    mnPrVlanDeviceConfEntry.setStatus("mandatory")
_MnPrVlanDeviceCapabilities_Type = OctetString
_MnPrVlanDeviceCapabilities_Object = MibTableColumn
mnPrVlanDeviceCapabilities = _MnPrVlanDeviceCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 1),
    _MnPrVlanDeviceCapabilities_Type()
)
mnPrVlanDeviceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanDeviceCapabilities.setStatus("mandatory")


class _MnPrVlanDeviceTfcClsEnabled_Type(TruthValue):
    """Custom type mnPrVlanDeviceTfcClsEnabled based on TruthValue"""
    defaultValue = 1


_MnPrVlanDeviceTfcClsEnabled_Type.__name__ = "TruthValue"
_MnPrVlanDeviceTfcClsEnabled_Object = MibTableColumn
mnPrVlanDeviceTfcClsEnabled = _MnPrVlanDeviceTfcClsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 2),
    _MnPrVlanDeviceTfcClsEnabled_Type()
)
mnPrVlanDeviceTfcClsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanDeviceTfcClsEnabled.setStatus("mandatory")


class _MnPrVlanDeviceNumTrafficClasses_Type(Integer32):
    """Custom type mnPrVlanDeviceNumTrafficClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MnPrVlanDeviceNumTrafficClasses_Type.__name__ = "Integer32"
_MnPrVlanDeviceNumTrafficClasses_Object = MibTableColumn
mnPrVlanDeviceNumTrafficClasses = _MnPrVlanDeviceNumTrafficClasses_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 3),
    _MnPrVlanDeviceNumTrafficClasses_Type()
)
mnPrVlanDeviceNumTrafficClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanDeviceNumTrafficClasses.setStatus("mandatory")


class _MnPrVlanTrafficClassOrder_Type(Integer32):
    """Custom type mnPrVlanTrafficClassOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021pIpV4ipV6Default", 1),
          ("ipV4ipV6Ieee8021pDefault", 2),
          ("ieee8021pDefault", 3),
          ("ipV4ipV6Default", 4),
          ("default", 5))
    )


_MnPrVlanTrafficClassOrder_Type.__name__ = "Integer32"
_MnPrVlanTrafficClassOrder_Object = MibTableColumn
mnPrVlanTrafficClassOrder = _MnPrVlanTrafficClassOrder_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 4),
    _MnPrVlanTrafficClassOrder_Type()
)
mnPrVlanTrafficClassOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanTrafficClassOrder.setStatus("mandatory")
_MnPrVlanTrafficClassWieghted_Type = TruthValue
_MnPrVlanTrafficClassWieghted_Object = MibTableColumn
mnPrVlanTrafficClassWieghted = _MnPrVlanTrafficClassWieghted_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 5),
    _MnPrVlanTrafficClassWieghted_Type()
)
mnPrVlanTrafficClassWieghted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanTrafficClassWieghted.setStatus("mandatory")


class _MnPrVlanDeviceVlanVersionNumber_Type(Integer32):
    """Custom type mnPrVlanDeviceVlanVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version1", 1)
    )


_MnPrVlanDeviceVlanVersionNumber_Type.__name__ = "Integer32"
_MnPrVlanDeviceVlanVersionNumber_Object = MibTableColumn
mnPrVlanDeviceVlanVersionNumber = _MnPrVlanDeviceVlanVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 6),
    _MnPrVlanDeviceVlanVersionNumber_Type()
)
mnPrVlanDeviceVlanVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanDeviceVlanVersionNumber.setStatus("mandatory")
_MnPrVlanDeviceMaxVlanId_Type = Integer32
_MnPrVlanDeviceMaxVlanId_Object = MibTableColumn
mnPrVlanDeviceMaxVlanId = _MnPrVlanDeviceMaxVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 7),
    _MnPrVlanDeviceMaxVlanId_Type()
)
mnPrVlanDeviceMaxVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanDeviceMaxVlanId.setStatus("mandatory")
_MnPrVlanDeviceMaxSupportedVlans_Type = Integer32
_MnPrVlanDeviceMaxSupportedVlans_Object = MibTableColumn
mnPrVlanDeviceMaxSupportedVlans = _MnPrVlanDeviceMaxSupportedVlans_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 8),
    _MnPrVlanDeviceMaxSupportedVlans_Type()
)
mnPrVlanDeviceMaxSupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanDeviceMaxSupportedVlans.setStatus("mandatory")
_MnPrVlanDeviceNumVlans_Type = Integer32
_MnPrVlanDeviceNumVlans_Object = MibTableColumn
mnPrVlanDeviceNumVlans = _MnPrVlanDeviceNumVlans_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 9),
    _MnPrVlanDeviceNumVlans_Type()
)
mnPrVlanDeviceNumVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanDeviceNumVlans.setStatus("mandatory")
_MnPrVlanDeviceNumDeletes_Type = Counter32
_MnPrVlanDeviceNumDeletes_Object = MibTableColumn
mnPrVlanDeviceNumDeletes = _MnPrVlanDeviceNumDeletes_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 10),
    _MnPrVlanDeviceNumDeletes_Type()
)
mnPrVlanDeviceNumDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanDeviceNumDeletes.setStatus("mandatory")


class _MnPrVlanDeviceLinkLossForwarding_Type(Integer32):
    """Custom type mnPrVlanDeviceLinkLossForwarding based on Integer32"""
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
        *(("noLlf", 1),
          ("totalLlf", 2),
          ("linkPortOnly", 3),
          ("totalLlfFeLos", 4))
    )


_MnPrVlanDeviceLinkLossForwarding_Type.__name__ = "Integer32"
_MnPrVlanDeviceLinkLossForwarding_Object = MibTableColumn
mnPrVlanDeviceLinkLossForwarding = _MnPrVlanDeviceLinkLossForwarding_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 11),
    _MnPrVlanDeviceLinkLossForwarding_Type()
)
mnPrVlanDeviceLinkLossForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanDeviceLinkLossForwarding.setStatus("mandatory")
_MnPrVlanDevice1qEnabled_Type = TruthValue
_MnPrVlanDevice1qEnabled_Object = MibTableColumn
mnPrVlanDevice1qEnabled = _MnPrVlanDevice1qEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 12),
    _MnPrVlanDevice1qEnabled_Type()
)
mnPrVlanDevice1qEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanDevice1qEnabled.setStatus("mandatory")
_MnPrVlanDeviceIgnoreTags_Type = TruthValue
_MnPrVlanDeviceIgnoreTags_Object = MibTableColumn
mnPrVlanDeviceIgnoreTags = _MnPrVlanDeviceIgnoreTags_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 13),
    _MnPrVlanDeviceIgnoreTags_Type()
)
mnPrVlanDeviceIgnoreTags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanDeviceIgnoreTags.setStatus("mandatory")


class _MnPrVlanDeviceRateLimitUnit_Type(Integer32):
    """Custom type mnPrVlanDeviceRateLimitUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MnPrVlanDeviceRateLimitUnit_Type.__name__ = "Integer32"
_MnPrVlanDeviceRateLimitUnit_Object = MibTableColumn
mnPrVlanDeviceRateLimitUnit = _MnPrVlanDeviceRateLimitUnit_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 14),
    _MnPrVlanDeviceRateLimitUnit_Type()
)
mnPrVlanDeviceRateLimitUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanDeviceRateLimitUnit.setStatus("mandatory")
_MnPrVlanDeviceLinkUntagEnable_Type = TruthValue
_MnPrVlanDeviceLinkUntagEnable_Object = MibTableColumn
mnPrVlanDeviceLinkUntagEnable = _MnPrVlanDeviceLinkUntagEnable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 15),
    _MnPrVlanDeviceLinkUntagEnable_Type()
)
mnPrVlanDeviceLinkUntagEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanDeviceLinkUntagEnable.setStatus("mandatory")


class _MnPrVlanDeviceLinkFrameMode_Type(Integer32):
    """Custom type mnPrVlanDeviceLinkFrameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameModeNormal", 1),
          ("frameModeProvider", 2))
    )


_MnPrVlanDeviceLinkFrameMode_Type.__name__ = "Integer32"
_MnPrVlanDeviceLinkFrameMode_Object = MibTableColumn
mnPrVlanDeviceLinkFrameMode = _MnPrVlanDeviceLinkFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 1, 1, 16),
    _MnPrVlanDeviceLinkFrameMode_Type()
)
mnPrVlanDeviceLinkFrameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanDeviceLinkFrameMode.setStatus("mandatory")
_MnPrVlanPortConfTable_Object = MibTable
mnPrVlanPortConfTable = _MnPrVlanPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2)
)
if mibBuilder.loadTexts:
    mnPrVlanPortConfTable.setStatus("mandatory")
_MnPrVlanPortConfEntry_Object = MibTableRow
mnPrVlanPortConfEntry = _MnPrVlanPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1)
)
mnPrVlanPortConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnTribIndex"),
)
if mibBuilder.loadTexts:
    mnPrVlanPortConfEntry.setStatus("mandatory")
_MnPrVlanPortCapabilities_Type = OctetString
_MnPrVlanPortCapabilities_Object = MibTableColumn
mnPrVlanPortCapabilities = _MnPrVlanPortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 1),
    _MnPrVlanPortCapabilities_Type()
)
mnPrVlanPortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanPortCapabilities.setStatus("mandatory")


class _MnPrVlanPortDefaultUserPriority_Type(Integer32):
    """Custom type mnPrVlanPortDefaultUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MnPrVlanPortDefaultUserPriority_Type.__name__ = "Integer32"
_MnPrVlanPortDefaultUserPriority_Object = MibTableColumn
mnPrVlanPortDefaultUserPriority = _MnPrVlanPortDefaultUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 2),
    _MnPrVlanPortDefaultUserPriority_Type()
)
mnPrVlanPortDefaultUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortDefaultUserPriority.setStatus("mandatory")


class _MnPrVlanPortPvid_Type(Integer32):
    """Custom type mnPrVlanPortPvid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MnPrVlanPortPvid_Type.__name__ = "Integer32"
_MnPrVlanPortPvid_Object = MibTableColumn
mnPrVlanPortPvid = _MnPrVlanPortPvid_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 3),
    _MnPrVlanPortPvid_Type()
)
mnPrVlanPortPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortPvid.setStatus("mandatory")


class _MnPrVlanPortAcceptableFrameTypes_Type(Integer32):
    """Custom type mnPrVlanPortAcceptableFrameTypes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admitAll", 1),
          ("admitOnlyVlanTagged", 2))
    )


_MnPrVlanPortAcceptableFrameTypes_Type.__name__ = "Integer32"
_MnPrVlanPortAcceptableFrameTypes_Object = MibTableColumn
mnPrVlanPortAcceptableFrameTypes = _MnPrVlanPortAcceptableFrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 4),
    _MnPrVlanPortAcceptableFrameTypes_Type()
)
mnPrVlanPortAcceptableFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortAcceptableFrameTypes.setStatus("mandatory")


class _MnPrVlanPortIngressFiltering_Type(TruthValue):
    """Custom type mnPrVlanPortIngressFiltering based on TruthValue"""
    defaultValue = 2


_MnPrVlanPortIngressFiltering_Type.__name__ = "TruthValue"
_MnPrVlanPortIngressFiltering_Object = MibTableColumn
mnPrVlanPortIngressFiltering = _MnPrVlanPortIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 5),
    _MnPrVlanPortIngressFiltering_Type()
)
mnPrVlanPortIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortIngressFiltering.setStatus("mandatory")


class _MnPrVlanPortGvrpStatus_Type(TruthValue):
    """Custom type mnPrVlanPortGvrpStatus based on TruthValue"""
    defaultValue = 2


_MnPrVlanPortGvrpStatus_Type.__name__ = "TruthValue"
_MnPrVlanPortGvrpStatus_Object = MibTableColumn
mnPrVlanPortGvrpStatus = _MnPrVlanPortGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 6),
    _MnPrVlanPortGvrpStatus_Type()
)
mnPrVlanPortGvrpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanPortGvrpStatus.setStatus("mandatory")
_MnPrVlanPortLineSpeed_Type = LanSpeed
_MnPrVlanPortLineSpeed_Object = MibTableColumn
mnPrVlanPortLineSpeed = _MnPrVlanPortLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 9),
    _MnPrVlanPortLineSpeed_Type()
)
mnPrVlanPortLineSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortLineSpeed.setStatus("mandatory")
_MnPrVlanPortRateLimitPri0_Type = RateLimit
_MnPrVlanPortRateLimitPri0_Object = MibTableColumn
mnPrVlanPortRateLimitPri0 = _MnPrVlanPortRateLimitPri0_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 10),
    _MnPrVlanPortRateLimitPri0_Type()
)
mnPrVlanPortRateLimitPri0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortRateLimitPri0.setStatus("mandatory")
_MnPrVlanPortRateLimitPri1_Type = RateLimit
_MnPrVlanPortRateLimitPri1_Object = MibTableColumn
mnPrVlanPortRateLimitPri1 = _MnPrVlanPortRateLimitPri1_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 11),
    _MnPrVlanPortRateLimitPri1_Type()
)
mnPrVlanPortRateLimitPri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortRateLimitPri1.setStatus("mandatory")
_MnPrVlanPortRateLimitPri2_Type = RateLimit
_MnPrVlanPortRateLimitPri2_Object = MibTableColumn
mnPrVlanPortRateLimitPri2 = _MnPrVlanPortRateLimitPri2_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 12),
    _MnPrVlanPortRateLimitPri2_Type()
)
mnPrVlanPortRateLimitPri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortRateLimitPri2.setStatus("mandatory")
_MnPrVlanPortRateLimitPri3_Type = RateLimit
_MnPrVlanPortRateLimitPri3_Object = MibTableColumn
mnPrVlanPortRateLimitPri3 = _MnPrVlanPortRateLimitPri3_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 13),
    _MnPrVlanPortRateLimitPri3_Type()
)
mnPrVlanPortRateLimitPri3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortRateLimitPri3.setStatus("mandatory")
_MnPrVlanPortUntagEnable_Type = TruthValue
_MnPrVlanPortUntagEnable_Object = MibTableColumn
mnPrVlanPortUntagEnable = _MnPrVlanPortUntagEnable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 14),
    _MnPrVlanPortUntagEnable_Type()
)
mnPrVlanPortUntagEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortUntagEnable.setStatus("mandatory")


class _MnPrVlanPortMaxFrameSize_Type(Integer32):
    """Custom type mnPrVlanPortMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 10240),
    )


_MnPrVlanPortMaxFrameSize_Type.__name__ = "Integer32"
_MnPrVlanPortMaxFrameSize_Object = MibTableColumn
mnPrVlanPortMaxFrameSize = _MnPrVlanPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 15),
    _MnPrVlanPortMaxFrameSize_Type()
)
mnPrVlanPortMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortMaxFrameSize.setStatus("mandatory")


class _MnPrVlanPortRateLimitMult_Type(Integer32):
    """Custom type mnPrVlanPortRateLimitMult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MnPrVlanPortRateLimitMult_Type.__name__ = "Integer32"
_MnPrVlanPortRateLimitMult_Object = MibTableColumn
mnPrVlanPortRateLimitMult = _MnPrVlanPortRateLimitMult_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 16),
    _MnPrVlanPortRateLimitMult_Type()
)
mnPrVlanPortRateLimitMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortRateLimitMult.setStatus("mandatory")


class _MnPrVlanPortRateControlMode_Type(Integer32):
    """Custom type mnPrVlanPortRateControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_MnPrVlanPortRateControlMode_Type.__name__ = "Integer32"
_MnPrVlanPortRateControlMode_Object = MibTableColumn
mnPrVlanPortRateControlMode = _MnPrVlanPortRateControlMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 17),
    _MnPrVlanPortRateControlMode_Type()
)
mnPrVlanPortRateControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortRateControlMode.setStatus("mandatory")


class _MnPrVlanPortFrameMode_Type(Integer32):
    """Custom type mnPrVlanPortFrameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameModeNormal", 1),
          ("frameModeProvider", 2))
    )


_MnPrVlanPortFrameMode_Type.__name__ = "Integer32"
_MnPrVlanPortFrameMode_Object = MibTableColumn
mnPrVlanPortFrameMode = _MnPrVlanPortFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 18),
    _MnPrVlanPortFrameMode_Type()
)
mnPrVlanPortFrameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortFrameMode.setStatus("mandatory")


class _MnPrVlanPortIngressFilterMode_Type(Integer32):
    """Custom type mnPrVlanPortIngressFilterMode based on Integer32"""
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
        *(("qModeDisabled", 1),
          ("qModeFallback", 2),
          ("qModeCheck", 3),
          ("qModeSecure", 4))
    )


_MnPrVlanPortIngressFilterMode_Type.__name__ = "Integer32"
_MnPrVlanPortIngressFilterMode_Object = MibTableColumn
mnPrVlanPortIngressFilterMode = _MnPrVlanPortIngressFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 20),
    _MnPrVlanPortIngressFilterMode_Type()
)
mnPrVlanPortIngressFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortIngressFilterMode.setStatus("mandatory")
_MnPrVlanPortIngressRateLimit_Type = Integer32
_MnPrVlanPortIngressRateLimit_Object = MibTableColumn
mnPrVlanPortIngressRateLimit = _MnPrVlanPortIngressRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 21),
    _MnPrVlanPortIngressRateLimit_Type()
)
mnPrVlanPortIngressRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortIngressRateLimit.setStatus("mandatory")
_MnPrVlanPortIngressBurstAlloc_Type = Integer32
_MnPrVlanPortIngressBurstAlloc_Object = MibTableColumn
mnPrVlanPortIngressBurstAlloc = _MnPrVlanPortIngressBurstAlloc_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 22),
    _MnPrVlanPortIngressBurstAlloc_Type()
)
mnPrVlanPortIngressBurstAlloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortIngressBurstAlloc.setStatus("mandatory")


class _MnPrVlanPortLearningMode_Type(Integer32):
    """Custom type mnPrVlanPortLearningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_MnPrVlanPortLearningMode_Type.__name__ = "Integer32"
_MnPrVlanPortLearningMode_Object = MibTableColumn
mnPrVlanPortLearningMode = _MnPrVlanPortLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 23),
    _MnPrVlanPortLearningMode_Type()
)
mnPrVlanPortLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortLearningMode.setStatus("mandatory")


class _MnPrVlanPortFloodMode_Type(Integer32):
    """Custom type mnPrVlanPortFloodMode based on Integer32"""
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
        *(("blockUnkDestAddr", 1),
          ("blockUnkMulticastAddr", 2),
          ("blockUnkUnicastAddr", 3),
          ("egressAllUnkDestAddr", 4))
    )


_MnPrVlanPortFloodMode_Type.__name__ = "Integer32"
_MnPrVlanPortFloodMode_Object = MibTableColumn
mnPrVlanPortFloodMode = _MnPrVlanPortFloodMode_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 24),
    _MnPrVlanPortFloodMode_Type()
)
mnPrVlanPortFloodMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortFloodMode.setStatus("mandatory")


class _MnPrVlanPortEthertype_Type(Integer32):
    """Custom type mnPrVlanPortEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MnPrVlanPortEthertype_Type.__name__ = "Integer32"
_MnPrVlanPortEthertype_Object = MibTableColumn
mnPrVlanPortEthertype = _MnPrVlanPortEthertype_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 2, 1, 25),
    _MnPrVlanPortEthertype_Type()
)
mnPrVlanPortEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanPortEthertype.setStatus("mandatory")
_MnPr1qVlanCurrentTable_Object = MibTable
mnPr1qVlanCurrentTable = _MnPr1qVlanCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 3)
)
if mibBuilder.loadTexts:
    mnPr1qVlanCurrentTable.setStatus("mandatory")
_MnPr1qVlanCurrentEntry_Object = MibTableRow
mnPr1qVlanCurrentEntry = _MnPr1qVlanCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 3, 1)
)
mnPr1qVlanCurrentEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnTribIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPr1qVlanIndex"),
)
if mibBuilder.loadTexts:
    mnPr1qVlanCurrentEntry.setStatus("mandatory")


class _MnPr1qVlanIndex_Type(Integer32):
    """Custom type mnPr1qVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MnPr1qVlanIndex_Type.__name__ = "Integer32"
_MnPr1qVlanIndex_Object = MibTableColumn
mnPr1qVlanIndex = _MnPr1qVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 3, 1, 1),
    _MnPr1qVlanIndex_Type()
)
mnPr1qVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mnPr1qVlanIndex.setStatus("mandatory")


class _MnPr1qVlanId_Type(Integer32):
    """Custom type mnPr1qVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MnPr1qVlanId_Type.__name__ = "Integer32"
_MnPr1qVlanId_Object = MibTableColumn
mnPr1qVlanId = _MnPr1qVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 3, 1, 2),
    _MnPr1qVlanId_Type()
)
mnPr1qVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPr1qVlanId.setStatus("mandatory")
_MnPr1qVlanFdbId_Type = Integer32
_MnPr1qVlanFdbId_Object = MibTableColumn
mnPr1qVlanFdbId = _MnPr1qVlanFdbId_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 3, 1, 3),
    _MnPr1qVlanFdbId_Type()
)
mnPr1qVlanFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPr1qVlanFdbId.setStatus("mandatory")
_MnPr1qVlanCurrentEgressPorts_Type = DisplayString
_MnPr1qVlanCurrentEgressPorts_Object = MibTableColumn
mnPr1qVlanCurrentEgressPorts = _MnPr1qVlanCurrentEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 3, 1, 4),
    _MnPr1qVlanCurrentEgressPorts_Type()
)
mnPr1qVlanCurrentEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPr1qVlanCurrentEgressPorts.setStatus("mandatory")
_MnPr1qVlanCurrentUntaggedPorts_Type = DisplayString
_MnPr1qVlanCurrentUntaggedPorts_Object = MibTableColumn
mnPr1qVlanCurrentUntaggedPorts = _MnPr1qVlanCurrentUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 3, 1, 5),
    _MnPr1qVlanCurrentUntaggedPorts_Type()
)
mnPr1qVlanCurrentUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPr1qVlanCurrentUntaggedPorts.setStatus("mandatory")


class _MnPr1qVlanStatus_Type(Integer32):
    """Custom type mnPr1qVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("permanent", 2),
          ("dynamicGvrp", 3))
    )


_MnPr1qVlanStatus_Type.__name__ = "Integer32"
_MnPr1qVlanStatus_Object = MibTableColumn
mnPr1qVlanStatus = _MnPr1qVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 3, 1, 6),
    _MnPr1qVlanStatus_Type()
)
mnPr1qVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPr1qVlanStatus.setStatus("mandatory")
_MnPr1qVlanCreationTime_Type = TimeTicks
_MnPr1qVlanCreationTime_Object = MibTableColumn
mnPr1qVlanCreationTime = _MnPr1qVlanCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 3, 1, 7),
    _MnPr1qVlanCreationTime_Type()
)
mnPr1qVlanCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPr1qVlanCreationTime.setStatus("mandatory")
_MnPr1qVlanStaticTable_Object = MibTable
mnPr1qVlanStaticTable = _MnPr1qVlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 4)
)
if mibBuilder.loadTexts:
    mnPr1qVlanStaticTable.setStatus("mandatory")
_MnPr1qVlanStaticEntry_Object = MibTableRow
mnPr1qVlanStaticEntry = _MnPr1qVlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 4, 1)
)
mnPr1qVlanStaticEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnTribIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPr1qVlanIndex"),
)
if mibBuilder.loadTexts:
    mnPr1qVlanStaticEntry.setStatus("mandatory")


class _MnPr1qVlanStaticId_Type(Integer32):
    """Custom type mnPr1qVlanStaticId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MnPr1qVlanStaticId_Type.__name__ = "Integer32"
_MnPr1qVlanStaticId_Object = MibTableColumn
mnPr1qVlanStaticId = _MnPr1qVlanStaticId_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 4, 1, 1),
    _MnPr1qVlanStaticId_Type()
)
mnPr1qVlanStaticId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPr1qVlanStaticId.setStatus("mandatory")


class _MnPr1qVlanStaticName_Type(DisplayString):
    """Custom type mnPr1qVlanStaticName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MnPr1qVlanStaticName_Type.__name__ = "DisplayString"
_MnPr1qVlanStaticName_Object = MibTableColumn
mnPr1qVlanStaticName = _MnPr1qVlanStaticName_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 4, 1, 2),
    _MnPr1qVlanStaticName_Type()
)
mnPr1qVlanStaticName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPr1qVlanStaticName.setStatus("mandatory")
_MnPr1qVlanStaticEgressPorts_Type = DisplayString
_MnPr1qVlanStaticEgressPorts_Object = MibTableColumn
mnPr1qVlanStaticEgressPorts = _MnPr1qVlanStaticEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 4, 1, 3),
    _MnPr1qVlanStaticEgressPorts_Type()
)
mnPr1qVlanStaticEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPr1qVlanStaticEgressPorts.setStatus("mandatory")
_MnPr1qVlanForbiddenEgressPorts_Type = DisplayString
_MnPr1qVlanForbiddenEgressPorts_Object = MibTableColumn
mnPr1qVlanForbiddenEgressPorts = _MnPr1qVlanForbiddenEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 4, 1, 4),
    _MnPr1qVlanForbiddenEgressPorts_Type()
)
mnPr1qVlanForbiddenEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPr1qVlanForbiddenEgressPorts.setStatus("mandatory")
_MnPr1qVlanStaticUntaggedPorts_Type = DisplayString
_MnPr1qVlanStaticUntaggedPorts_Object = MibTableColumn
mnPr1qVlanStaticUntaggedPorts = _MnPr1qVlanStaticUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 4, 1, 5),
    _MnPr1qVlanStaticUntaggedPorts_Type()
)
mnPr1qVlanStaticUntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPr1qVlanStaticUntaggedPorts.setStatus("mandatory")
_MnPr1qVlanStaticRowStatus_Type = RowStatus
_MnPr1qVlanStaticRowStatus_Object = MibTableColumn
mnPr1qVlanStaticRowStatus = _MnPr1qVlanStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 4, 1, 6),
    _MnPr1qVlanStaticRowStatus_Type()
)
mnPr1qVlanStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPr1qVlanStaticRowStatus.setStatus("mandatory")


class _MnPr1qVlanStaticFID_Type(Integer32):
    """Custom type mnPr1qVlanStaticFID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MnPr1qVlanStaticFID_Type.__name__ = "Integer32"
_MnPr1qVlanStaticFID_Object = MibTableColumn
mnPr1qVlanStaticFID = _MnPr1qVlanStaticFID_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 4, 1, 7),
    _MnPr1qVlanStaticFID_Type()
)
mnPr1qVlanStaticFID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPr1qVlanStaticFID.setStatus("mandatory")


class _MnPr1qVlanStaticRingID_Type(Integer32):
    """Custom type mnPr1qVlanStaticRingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_MnPr1qVlanStaticRingID_Type.__name__ = "Integer32"
_MnPr1qVlanStaticRingID_Object = MibTableColumn
mnPr1qVlanStaticRingID = _MnPr1qVlanStaticRingID_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 4, 1, 8),
    _MnPr1qVlanStaticRingID_Type()
)
mnPr1qVlanStaticRingID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPr1qVlanStaticRingID.setStatus("mandatory")
_MnPrVlanDeviceTrafficClassTable_Object = MibTable
mnPrVlanDeviceTrafficClassTable = _MnPrVlanDeviceTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 5)
)
if mibBuilder.loadTexts:
    mnPrVlanDeviceTrafficClassTable.setStatus("mandatory")
_MnPrVlanDeviceTrafficClassEntry_Object = MibTableRow
mnPrVlanDeviceTrafficClassEntry = _MnPrVlanDeviceTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 5, 1)
)
mnPrVlanDeviceTrafficClassEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnTribIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrVlanDeviceTrafficClassIndex"),
)
if mibBuilder.loadTexts:
    mnPrVlanDeviceTrafficClassEntry.setStatus("mandatory")


class _MnPrVlanDeviceTrafficClassIndex_Type(Integer32):
    """Custom type mnPrVlanDeviceTrafficClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MnPrVlanDeviceTrafficClassIndex_Type.__name__ = "Integer32"
_MnPrVlanDeviceTrafficClassIndex_Object = MibTableColumn
mnPrVlanDeviceTrafficClassIndex = _MnPrVlanDeviceTrafficClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 5, 1, 1),
    _MnPrVlanDeviceTrafficClassIndex_Type()
)
mnPrVlanDeviceTrafficClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanDeviceTrafficClassIndex.setStatus("mandatory")


class _MnPrVlanDeviceTfcClsPriority_Type(Integer32):
    """Custom type mnPrVlanDeviceTfcClsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MnPrVlanDeviceTfcClsPriority_Type.__name__ = "Integer32"
_MnPrVlanDeviceTfcClsPriority_Object = MibTableColumn
mnPrVlanDeviceTfcClsPriority = _MnPrVlanDeviceTfcClsPriority_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 5, 1, 2),
    _MnPrVlanDeviceTfcClsPriority_Type()
)
mnPrVlanDeviceTfcClsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanDeviceTfcClsPriority.setStatus("mandatory")


class _MnPrVlanDeviceTrafficClass_Type(Integer32):
    """Custom type mnPrVlanDeviceTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MnPrVlanDeviceTrafficClass_Type.__name__ = "Integer32"
_MnPrVlanDeviceTrafficClass_Object = MibTableColumn
mnPrVlanDeviceTrafficClass = _MnPrVlanDeviceTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 5, 1, 3),
    _MnPrVlanDeviceTrafficClass_Type()
)
mnPrVlanDeviceTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanDeviceTrafficClass.setStatus("mandatory")
_MnPrVlanDeviceTosTable_Object = MibTable
mnPrVlanDeviceTosTable = _MnPrVlanDeviceTosTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 6)
)
if mibBuilder.loadTexts:
    mnPrVlanDeviceTosTable.setStatus("mandatory")
_MnPrVlanDeviceTosEntry_Object = MibTableRow
mnPrVlanDeviceTosEntry = _MnPrVlanDeviceTosEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 6, 1)
)
mnPrVlanDeviceTosEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnTribIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrVlanDeviceTosIndex"),
)
if mibBuilder.loadTexts:
    mnPrVlanDeviceTosEntry.setStatus("mandatory")


class _MnPrVlanDeviceTosIndex_Type(Integer32):
    """Custom type mnPrVlanDeviceTosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MnPrVlanDeviceTosIndex_Type.__name__ = "Integer32"
_MnPrVlanDeviceTosIndex_Object = MibTableColumn
mnPrVlanDeviceTosIndex = _MnPrVlanDeviceTosIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 6, 1, 1),
    _MnPrVlanDeviceTosIndex_Type()
)
mnPrVlanDeviceTosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanDeviceTosIndex.setStatus("mandatory")


class _MnPrVlanDeviceTosTrafficClass_Type(Integer32):
    """Custom type mnPrVlanDeviceTosTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MnPrVlanDeviceTosTrafficClass_Type.__name__ = "Integer32"
_MnPrVlanDeviceTosTrafficClass_Object = MibTableColumn
mnPrVlanDeviceTosTrafficClass = _MnPrVlanDeviceTosTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 6, 1, 2),
    _MnPrVlanDeviceTosTrafficClass_Type()
)
mnPrVlanDeviceTosTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanDeviceTosTrafficClass.setStatus("mandatory")


class _MnPrVlanDeviceTos_Type(Integer32):
    """Custom type mnPrVlanDeviceTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MnPrVlanDeviceTos_Type.__name__ = "Integer32"
_MnPrVlanDeviceTos_Object = MibTableColumn
mnPrVlanDeviceTos = _MnPrVlanDeviceTos_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 6, 1, 3),
    _MnPrVlanDeviceTos_Type()
)
mnPrVlanDeviceTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanDeviceTos.setStatus("mandatory")
_MnPrVlanDeviceDscpTable_Object = MibTable
mnPrVlanDeviceDscpTable = _MnPrVlanDeviceDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 7)
)
if mibBuilder.loadTexts:
    mnPrVlanDeviceDscpTable.setStatus("mandatory")
_MnPrVlanDeviceDscpEntry_Object = MibTableRow
mnPrVlanDeviceDscpEntry = _MnPrVlanDeviceDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 7, 1)
)
mnPrVlanDeviceDscpEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnTribIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrVlanDeviceDscpIndex"),
)
if mibBuilder.loadTexts:
    mnPrVlanDeviceDscpEntry.setStatus("mandatory")


class _MnPrVlanDeviceDscpIndex_Type(Integer32):
    """Custom type mnPrVlanDeviceDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MnPrVlanDeviceDscpIndex_Type.__name__ = "Integer32"
_MnPrVlanDeviceDscpIndex_Object = MibTableColumn
mnPrVlanDeviceDscpIndex = _MnPrVlanDeviceDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 7, 1, 1),
    _MnPrVlanDeviceDscpIndex_Type()
)
mnPrVlanDeviceDscpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanDeviceDscpIndex.setStatus("mandatory")


class _MnPrVlanDeviceDscpValueToMap_Type(Integer32):
    """Custom type mnPrVlanDeviceDscpValueToMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MnPrVlanDeviceDscpValueToMap_Type.__name__ = "Integer32"
_MnPrVlanDeviceDscpValueToMap_Object = MibTableColumn
mnPrVlanDeviceDscpValueToMap = _MnPrVlanDeviceDscpValueToMap_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 7, 1, 2),
    _MnPrVlanDeviceDscpValueToMap_Type()
)
mnPrVlanDeviceDscpValueToMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrVlanDeviceDscpValueToMap.setStatus("mandatory")


class _MnPrVlanDeviceDscpQosClass_Type(Integer32):
    """Custom type mnPrVlanDeviceDscpQosClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MnPrVlanDeviceDscpQosClass_Type.__name__ = "Integer32"
_MnPrVlanDeviceDscpQosClass_Object = MibTableColumn
mnPrVlanDeviceDscpQosClass = _MnPrVlanDeviceDscpQosClass_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 8, 7, 1, 3),
    _MnPrVlanDeviceDscpQosClass_Type()
)
mnPrVlanDeviceDscpQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrVlanDeviceDscpQosClass.setStatus("mandatory")
_MnPrSecurityObjects_ObjectIdentity = ObjectIdentity
mnPrSecurityObjects = _MnPrSecurityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 9)
)
_MnPrProtocolConfTable_Object = MibTable
mnPrProtocolConfTable = _MnPrProtocolConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 9, 3)
)
if mibBuilder.loadTexts:
    mnPrProtocolConfTable.setStatus("mandatory")
_MnPrProtocolConfEntry_Object = MibTableRow
mnPrProtocolConfEntry = _MnPrProtocolConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 9, 3, 1)
)
mnPrProtocolConfEntry.setIndexNames(
    (0, "MNI-PROTEUS-AMT-MIB", "mnRadioIndex"),
    (0, "MNI-PROTEUS-AMT-MIB", "mnPrProtocolIndex"),
)
if mibBuilder.loadTexts:
    mnPrProtocolConfEntry.setStatus("mandatory")


class _MnPrProtocolIndex_Type(Integer32):
    """Custom type mnPrProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("serialCLI", 1),
          ("telnetCLI", 2),
          ("snmpV1", 3),
          ("ssh", 4),
          ("serialEM", 5),
          ("snmpV2c", 6),
          ("snmpV3", 7),
          ("sce", 8),
          ("ppp", 9),
          ("snmpV3NANP", 10),
          ("snmpV3ANP", 11),
          ("snmpV3AP", 12))
    )


_MnPrProtocolIndex_Type.__name__ = "Integer32"
_MnPrProtocolIndex_Object = MibTableColumn
mnPrProtocolIndex = _MnPrProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 9, 3, 1, 1),
    _MnPrProtocolIndex_Type()
)
mnPrProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnPrProtocolIndex.setStatus("mandatory")


class _MnPrProtocolConfAccess_Type(Integer32):
    """Custom type mnPrProtocolConfAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 1),
          ("readOnlyAccess", 3),
          ("readWriteAccess", 7))
    )


_MnPrProtocolConfAccess_Type.__name__ = "Integer32"
_MnPrProtocolConfAccess_Object = MibTableColumn
mnPrProtocolConfAccess = _MnPrProtocolConfAccess_Object(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 9, 3, 1, 2),
    _MnPrProtocolConfAccess_Type()
)
mnPrProtocolConfAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnPrProtocolConfAccess.setStatus("mandatory")
_MnCapabilities_ObjectIdentity = ObjectIdentity
mnCapabilities = _MnCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 14)
)
_MnExperimental_ObjectIdentity = ObjectIdentity
mnExperimental = _MnExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3323, 15)
)

# Managed Objects groups


# Notification objects

mnPrNotificationMajorAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 3323, 11, 1, 1, 0, 1)
)
mnPrNotificationMajorAlarmSet.setObjects(
      *(("MNI-PROTEUS-AMT-MIB", "mnPrNotifyID"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyText"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyParameter"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifySeverity"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioIndex"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioName"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyTimeStamp"))
)
if mibBuilder.loadTexts:
    mnPrNotificationMajorAlarmSet.setStatus(
        ""
    )

mnPrNotificationAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3323, 11, 1, 1, 0, 2)
)
mnPrNotificationAlarmClear.setObjects(
      *(("MNI-PROTEUS-AMT-MIB", "mnPrNotifyID"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyText"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyParameter"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifySeverity"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioIndex"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioName"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyTimeStamp"))
)
if mibBuilder.loadTexts:
    mnPrNotificationAlarmClear.setStatus(
        ""
    )

mnPrNotificationMinorAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 3323, 11, 1, 1, 0, 3)
)
mnPrNotificationMinorAlarmSet.setObjects(
      *(("MNI-PROTEUS-AMT-MIB", "mnPrNotifyID"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyText"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyParameter"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifySeverity"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioIndex"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioName"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyTimeStamp"))
)
if mibBuilder.loadTexts:
    mnPrNotificationMinorAlarmSet.setStatus(
        ""
    )

mnPrNotificationInfoAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 3323, 11, 1, 1, 0, 4)
)
mnPrNotificationInfoAlarmSet.setObjects(
      *(("MNI-PROTEUS-AMT-MIB", "mnPrNotifyID"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyText"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyParameter"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifySeverity"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioIndex"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioName"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyTimeStamp"))
)
if mibBuilder.loadTexts:
    mnPrNotificationInfoAlarmSet.setStatus(
        ""
    )

mnPrFNotificationMajorAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 0, 1)
)
mnPrFNotificationMajorAlarmSet.setObjects(
      *(("MNI-PROTEUS-AMT-MIB", "mnPrNotifyID"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyText"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyParameter"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifySeverity"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioIndex"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioName"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyTimeStamp"))
)
if mibBuilder.loadTexts:
    mnPrFNotificationMajorAlarmSet.setStatus(
        ""
    )

mnPrFNotificationAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 0, 2)
)
mnPrFNotificationAlarmClear.setObjects(
      *(("MNI-PROTEUS-AMT-MIB", "mnPrNotifyID"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyText"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyParameter"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifySeverity"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioIndex"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioName"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyTimeStamp"))
)
if mibBuilder.loadTexts:
    mnPrFNotificationAlarmClear.setStatus(
        ""
    )

mnPrFNotificationMinorAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 0, 3)
)
mnPrFNotificationMinorAlarmSet.setObjects(
      *(("MNI-PROTEUS-AMT-MIB", "mnPrNotifyID"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyText"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyParameter"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifySeverity"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioIndex"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioName"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyTimeStamp"))
)
if mibBuilder.loadTexts:
    mnPrFNotificationMinorAlarmSet.setStatus(
        ""
    )

mnPrFNotificationInfoAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 3323, 13, 1, 0, 4)
)
mnPrFNotificationInfoAlarmSet.setObjects(
      *(("MNI-PROTEUS-AMT-MIB", "mnPrNotifyID"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyText"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyParameter"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifySeverity"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioIndex"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyRadioName"),
        ("MNI-PROTEUS-AMT-MIB", "mnPrNotifyTimeStamp"))
)
if mibBuilder.loadTexts:
    mnPrFNotificationInfoAlarmSet.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MNI-PROTEUS-AMT-MIB",
    **{"LIMType": LIMType,
       "ModulationType": ModulationType,
       "ITUSeverity": ITUSeverity,
       "AccessLevel": AccessLevel,
       "Display64": Display64,
       "RateLimit": RateLimit,
       "IfBandwidth": IfBandwidth,
       "LanSpeed": LanSpeed,
       "SHARPBERStatus": SHARPBERStatus,
       "SHARPBERThresh": SHARPBERThresh,
       "microwave-networks": microwave_networks,
       "mnRegistrations": mnRegistrations,
       "mnRegSysObjID": mnRegSysObjID,
       "mnRegSysProtAMT": mnRegSysProtAMT,
       "mnPrNotificationMajorAlarmSet": mnPrNotificationMajorAlarmSet,
       "mnPrNotificationAlarmClear": mnPrNotificationAlarmClear,
       "mnPrNotificationMinorAlarmSet": mnPrNotificationMinorAlarmSet,
       "mnPrNotificationInfoAlarmSet": mnPrNotificationInfoAlarmSet,
       "mnRegSysProtAMTL": mnRegSysProtAMTL,
       "mnRegSysProtAMTM": mnRegSysProtAMTM,
       "mnRegSysProtMX": mnRegSysProtMX,
       "mnRegSysProtMXD": mnRegSysProtMXD,
       "mnRegSysProtHE32": mnRegSysProtHE32,
       "mnModules": mnModules,
       "mnCommon": mnCommon,
       "mnProducts": mnProducts,
       "mnProtAMTV1MIB": mnProtAMTV1MIB,
       "mnPrFV2Notifications": mnPrFV2Notifications,
       "mnPrFNotificationMajorAlarmSet": mnPrFNotificationMajorAlarmSet,
       "mnPrFNotificationAlarmClear": mnPrFNotificationAlarmClear,
       "mnPrFNotificationMinorAlarmSet": mnPrFNotificationMinorAlarmSet,
       "mnPrFNotificationInfoAlarmSet": mnPrFNotificationInfoAlarmSet,
       "mnPrStatusObjects": mnPrStatusObjects,
       "mnPrLinkStatusObjects": mnPrLinkStatusObjects,
       "mnPrLinkStatLinkUp": mnPrLinkStatLinkUp,
       "mnPrLinkStatReachable": mnPrLinkStatReachable,
       "mnPrLinkStatAccessLevel": mnPrLinkStatAccessLevel,
       "mnPrLinkStatLastErrorText": mnPrLinkStatLastErrorText,
       "mnPrLinkStatLocalRadioIndex": mnPrLinkStatLocalRadioIndex,
       "mnPrRadStatTable": mnPrRadStatTable,
       "mnPrRadStatEntry": mnPrRadStatEntry,
       "mnRadioIndex": mnRadioIndex,
       "mnPrRadStatCurSeverity": mnPrRadStatCurSeverity,
       "mnPrRadStatLatchSeverity": mnPrRadStatLatchSeverity,
       "mnPrRadStatMinorAlarm": mnPrRadStatMinorAlarm,
       "mnPrRadStatControlOn": mnPrRadStatControlOn,
       "mnPrRadStatCurAlarmList": mnPrRadStatCurAlarmList,
       "mnPrRadStatUptime": mnPrRadStatUptime,
       "mnPrRadStatLastAlarmChangeTime": mnPrRadStatLastAlarmChangeTime,
       "mnPrRadStatLastCCChangeTime": mnPrRadStatLastCCChangeTime,
       "mnPrRadStatLatchedTimeString": mnPrRadStatLatchedTimeString,
       "mnPrRadStatImageBooted": mnPrRadStatImageBooted,
       "mnPrRadStatIFBoardType": mnPrRadStatIFBoardType,
       "mnPrRadStatPSVoltage": mnPrRadStatPSVoltage,
       "mnPrRadStatODUFreqBand": mnPrRadStatODUFreqBand,
       "mnPrRadStatODUSubBand": mnPrRadStatODUSubBand,
       "mnPrRadStatODUTxHigh": mnPrRadStatODUTxHigh,
       "mnPrRadStatMinTxFreq": mnPrRadStatMinTxFreq,
       "mnPrRadStatMaxTxFreq": mnPrRadStatMaxTxFreq,
       "mnPrRadStatMinRxFreq": mnPrRadStatMinRxFreq,
       "mnPrRadStatMaxRxFreq": mnPrRadStatMaxRxFreq,
       "mnPrRadStatProtType": mnPrRadStatProtType,
       "mnPrRadStatProtOtherRadioAlarm": mnPrRadStatProtOtherRadioAlarm,
       "mnPrRadStatProtManualMode": mnPrRadStatProtManualMode,
       "mnPrRadStatProtOnlineState": mnPrRadStatProtOnlineState,
       "mnPrRadStatMinTxPower": mnPrRadStatMinTxPower,
       "mnPrRadStatMaxTxPower": mnPrRadStatMaxTxPower,
       "mnPrRadStatPerfHistDuration": mnPrRadStatPerfHistDuration,
       "mnPrRadStatPerfHistMinDuration": mnPrRadStatPerfHistMinDuration,
       "mnPrRadStatPerfHistRecords": mnPrRadStatPerfHistRecords,
       "mnPrRadStatPerfHistMinRecords": mnPrRadStatPerfHistMinRecords,
       "mnPrRadStatPerfHistMaxVarIndex": mnPrRadStatPerfHistMaxVarIndex,
       "mnPrRadStatTrSpace": mnPrRadStatTrSpace,
       "mnPrRadStatModulation": mnPrRadStatModulation,
       "mnPrRadStatProtToggleMode": mnPrRadStatProtToggleMode,
       "mnPrRadStatModulationInst": mnPrRadStatModulationInst,
       "mnPrRadStatModulationConf": mnPrRadStatModulationConf,
       "mnPrRadStatModulationProp": mnPrRadStatModulationProp,
       "mnPrRadStatSysGainConf": mnPrRadStatSysGainConf,
       "mnPrRadStatSysGainProp": mnPrRadStatSysGainProp,
       "mnPrRadStatLoopSwitchStat": mnPrRadStatLoopSwitchStat,
       "mnPrRouteStatTable": mnPrRouteStatTable,
       "mnPrRouteStatEntry": mnPrRouteStatEntry,
       "mnPrRouteStatIndex": mnPrRouteStatIndex,
       "mnPrRouteStatDestination": mnPrRouteStatDestination,
       "mnPrRouteStatMask": mnPrRouteStatMask,
       "mnPrRouteStatNextHop": mnPrRouteStatNextHop,
       "mnPrRouteStatMetric": mnPrRouteStatMetric,
       "mnPrRouteStatInterface": mnPrRouteStatInterface,
       "mnPrRouteStatType": mnPrRouteStatType,
       "mnPrRouteStatHowAdded": mnPrRouteStatHowAdded,
       "mnPrOpResultTable": mnPrOpResultTable,
       "mnPrOpResultEntry": mnPrOpResultEntry,
       "mnPrOpResultIndex": mnPrOpResultIndex,
       "mnPrOpResultLevel": mnPrOpResultLevel,
       "mnPrOpResultMessage": mnPrOpResultMessage,
       "mnPrOpResultArgument": mnPrOpResultArgument,
       "mnPrAlarmObjects": mnPrAlarmObjects,
       "mnPrCurAlarmTable": mnPrCurAlarmTable,
       "mnPrCurAlarmEntry": mnPrCurAlarmEntry,
       "mnPrCurAlarmID": mnPrCurAlarmID,
       "mnPrCurAlarmText": mnPrCurAlarmText,
       "mnPrLatAlarmTable": mnPrLatAlarmTable,
       "mnPrLatAlarmEntry": mnPrLatAlarmEntry,
       "mnPrLatAlarmID": mnPrLatAlarmID,
       "mnPrLatAlarmText": mnPrLatAlarmText,
       "mnPrAlarmLogTable": mnPrAlarmLogTable,
       "mnPrAlarmLogEntry": mnPrAlarmLogEntry,
       "mnPrAlarmLogIndex": mnPrAlarmLogIndex,
       "mnPrAlarmLogText": mnPrAlarmLogText,
       "mnPrEventLogTable": mnPrEventLogTable,
       "mnPrEventLogEntry": mnPrEventLogEntry,
       "mnPrEventLogIndex": mnPrEventLogIndex,
       "mnPrEventLogText": mnPrEventLogText,
       "mnPrNotifyObjects": mnPrNotifyObjects,
       "mnPrNotifyID": mnPrNotifyID,
       "mnPrNotifyText": mnPrNotifyText,
       "mnPrNotifyParameter": mnPrNotifyParameter,
       "mnPrNotifySeverity": mnPrNotifySeverity,
       "mnPrNotifyRadioIndex": mnPrNotifyRadioIndex,
       "mnPrNotifyRadioName": mnPrNotifyRadioName,
       "mnPrNotifyTimeStamp": mnPrNotifyTimeStamp,
       "mnPrPerformanceObjects": mnPrPerformanceObjects,
       "mnPrPerfBaseTable": mnPrPerfBaseTable,
       "mnPrPerfBaseEntry": mnPrPerfBaseEntry,
       "mnInterfaceIndex": mnInterfaceIndex,
       "mnPrPerfBaseTxPower": mnPrPerfBaseTxPower,
       "mnPrPerfBaseRSL": mnPrPerfBaseRSL,
       "mnPrPerfBaseFadeMargin": mnPrPerfBaseFadeMargin,
       "mnPrPerfBaseElapsedSecs": mnPrPerfBaseElapsedSecs,
       "mnPrPerfBaseASs": mnPrPerfBaseASs,
       "mnPrPerfBaseUSs": mnPrPerfBaseUSs,
       "mnPrPerfBaseESs": mnPrPerfBaseESs,
       "mnPrPerfBaseSESs": mnPrPerfBaseSESs,
       "mnPrPerfBaseTotalBlocks": mnPrPerfBaseTotalBlocks,
       "mnPrPerfBaseErrBlocks": mnPrPerfBaseErrBlocks,
       "mnPrPerfBaseBBEs": mnPrPerfBaseBBEs,
       "mnPrPerfBaseSNR": mnPrPerfBaseSNR,
       "mnPrPerfBaseDecoderStress": mnPrPerfBaseDecoderStress,
       "mnPrPerfBaseAcmTxProfile": mnPrPerfBaseAcmTxProfile,
       "mnPrPerfBaseAcmRxProfile": mnPrPerfBaseAcmRxProfile,
       "mnPrPerfBaseLinkCapMbps": mnPrPerfBaseLinkCapMbps,
       "mnPrPerfBaseRxEtherMbps": mnPrPerfBaseRxEtherMbps,
       "mnPrPerfBaseDemodErrBlocks": mnPrPerfBaseDemodErrBlocks,
       "mnPrPerfBaseRFUTemp": mnPrPerfBaseRFUTemp,
       "mnPrPerfBaseRSL1": mnPrPerfBaseRSL1,
       "mnPrPerfBaseRSL2": mnPrPerfBaseRSL2,
       "mnPrPerfSumIntTable": mnPrPerfSumIntTable,
       "mnPrPerfSumIntEntry": mnPrPerfSumIntEntry,
       "mnIntervalIndex": mnIntervalIndex,
       "mnPrPerfSumIntESs": mnPrPerfSumIntESs,
       "mnPrPerfSumIntSESs": mnPrPerfSumIntSESs,
       "mnPrPerfSumIntBER": mnPrPerfSumIntBER,
       "mnPrPerfSumIntElapsedSecs": mnPrPerfSumIntElapsedSecs,
       "mnPrPerfSumIntASs": mnPrPerfSumIntASs,
       "mnPrPerfCustIntTable": mnPrPerfCustIntTable,
       "mnPrPerfCustIntEntry": mnPrPerfCustIntEntry,
       "mnPrPerfCustIntTxPowerAvg": mnPrPerfCustIntTxPowerAvg,
       "mnPrPerfCustIntTxPowerMax": mnPrPerfCustIntTxPowerMax,
       "mnPrPerfCustIntTxPowerMin": mnPrPerfCustIntTxPowerMin,
       "mnPrPerfCustIntRSLAvg": mnPrPerfCustIntRSLAvg,
       "mnPrPerfCustIntRSLMax": mnPrPerfCustIntRSLMax,
       "mnPrPerfCustIntRSLMin": mnPrPerfCustIntRSLMin,
       "mnPrPerfCustIntElapsedSecs": mnPrPerfCustIntElapsedSecs,
       "mnPrPerfCustIntASs": mnPrPerfCustIntASs,
       "mnPrPerfCustIntUSs": mnPrPerfCustIntUSs,
       "mnPrPerfCustIntESs": mnPrPerfCustIntESs,
       "mnPrPerfCustIntSESs": mnPrPerfCustIntSESs,
       "mnPrPerfCustIntTotalBlocks": mnPrPerfCustIntTotalBlocks,
       "mnPrPerfCustIntErrBlocks": mnPrPerfCustIntErrBlocks,
       "mnPrPerfCustIntBBEs": mnPrPerfCustIntBBEs,
       "mnPrPerfCustIntESRatio": mnPrPerfCustIntESRatio,
       "mnPrPerfCustIntSESRatio": mnPrPerfCustIntSESRatio,
       "mnPrPerfCustIntBER": mnPrPerfCustIntBER,
       "mnPrPerfCustIntBBER": mnPrPerfCustIntBBER,
       "mnPrPerfHistObjects": mnPrPerfHistObjects,
       "mnPrPerfHistTable": mnPrPerfHistTable,
       "mnPrPerfHistEntry": mnPrPerfHistEntry,
       "mnPrPerfHistIndex": mnPrPerfHistIndex,
       "mnPrPerfHistTimestamp": mnPrPerfHistTimestamp,
       "mnPrPerfHistElapsedSecs": mnPrPerfHistElapsedSecs,
       "mnPrPerfHistDowntime": mnPrPerfHistDowntime,
       "mnPrPerfHistASs": mnPrPerfHistASs,
       "mnPrPerfHistUSs": mnPrPerfHistUSs,
       "mnPrPerfHistESs": mnPrPerfHistESs,
       "mnPrPerfHistSESs": mnPrPerfHistSESs,
       "mnPrPerfHistTotalBlocks": mnPrPerfHistTotalBlocks,
       "mnPrPerfHistErrBlocks": mnPrPerfHistErrBlocks,
       "mnPrPerfHistErrBackBlocks": mnPrPerfHistErrBackBlocks,
       "mnPrPerfHistTotalBytes": mnPrPerfHistTotalBytes,
       "mnPrPerfHistErrBytes": mnPrPerfHistErrBytes,
       "mnPrPerfHistTotalBackBytes": mnPrPerfHistTotalBackBytes,
       "mnPrPerfHistErrBackBytes": mnPrPerfHistErrBackBytes,
       "mnPrPerfHistESRatio": mnPrPerfHistESRatio,
       "mnPrPerfHistSESRatio": mnPrPerfHistSESRatio,
       "mnPrPerfHistBER": mnPrPerfHistBER,
       "mnPrPerfHistBBER": mnPrPerfHistBBER,
       "mnPrPerfHistTxPower": mnPrPerfHistTxPower,
       "mnPrPerfHistTxPowerMin": mnPrPerfHistTxPowerMin,
       "mnPrPerfHistTxPowerMax": mnPrPerfHistTxPowerMax,
       "mnPrPerfHistTxPowerAvg": mnPrPerfHistTxPowerAvg,
       "mnPrPerfHistRSL": mnPrPerfHistRSL,
       "mnPrPerfHistRSLMin": mnPrPerfHistRSLMin,
       "mnPrPerfHistRSLMax": mnPrPerfHistRSLMax,
       "mnPrPerfHistRSLAvg": mnPrPerfHistRSLAvg,
       "mnPrPerfHistAlarmBMP": mnPrPerfHistAlarmBMP,
       "mnPrPerfHistCsvHdrTable": mnPrPerfHistCsvHdrTable,
       "mnPrPerfHistCsvHdrEntry": mnPrPerfHistCsvHdrEntry,
       "mnPrPerfHistCsvHdr": mnPrPerfHistCsvHdr,
       "mnPrPerfHistCsvDataTable": mnPrPerfHistCsvDataTable,
       "mnPrPerfHistCsvDataEntry": mnPrPerfHistCsvDataEntry,
       "mnPrPerfHistCsvData": mnPrPerfHistCsvData,
       "mnPrControlObjects": mnPrControlObjects,
       "mnPrRadCtlTable": mnPrRadCtlTable,
       "mnPrRadCtlEntry": mnPrRadCtlEntry,
       "mnPrRadCtlDigAggLoopback": mnPrRadCtlDigAggLoopback,
       "mnPrRadCtlBERTTxPattern": mnPrRadCtlBERTTxPattern,
       "mnPrRadCtlBERTTimeString": mnPrRadCtlBERTTimeString,
       "mnPrRadCtlBERTTotal": mnPrRadCtlBERTTotal,
       "mnPrRadCtlBERTErrors": mnPrRadCtlBERTErrors,
       "mnPrRadCtlBERTBER": mnPrRadCtlBERTBER,
       "mnPrRadCtrDigAggLoopTime": mnPrRadCtrDigAggLoopTime,
       "mnPrRadCtlODUMute": mnPrRadCtlODUMute,
       "mnPrRadCtlODUMuteTime": mnPrRadCtlODUMuteTime,
       "mnPrLIMCtlTable": mnPrLIMCtlTable,
       "mnPrLIMCtlEntry": mnPrLIMCtlEntry,
       "mnLIMIndex": mnLIMIndex,
       "mnPrLIMCtlBERTTrib": mnPrLIMCtlBERTTrib,
       "mnPrLIMCtlBERTTxPattern": mnPrLIMCtlBERTTxPattern,
       "mnPrLIMCtlBERTTimeString": mnPrLIMCtlBERTTimeString,
       "mnPrLIMCtlBERTTotal": mnPrLIMCtlBERTTotal,
       "mnPrLIMCtlBERTErrors": mnPrLIMCtlBERTErrors,
       "mnPrLIMCtlBERTBER": mnPrLIMCtlBERTBER,
       "mnPrTribCtlTable": mnPrTribCtlTable,
       "mnPrTribCtlEntry": mnPrTribCtlEntry,
       "mnTribIndex": mnTribIndex,
       "mnPrTribCtlLocalLoopback": mnPrTribCtlLocalLoopback,
       "mnPrTribCtlRemoteLoopback": mnPrTribCtlRemoteLoopback,
       "mnPrConfigurationObjects": mnPrConfigurationObjects,
       "mnPrInventTable": mnPrInventTable,
       "mnPrInventEntry": mnPrInventEntry,
       "mnPrInventCompIndex": mnPrInventCompIndex,
       "mnPrInventCompText": mnPrInventCompText,
       "mnPrInventModPartText": mnPrInventModPartText,
       "mnPrInventCheckSumText": mnPrInventCheckSumText,
       "mnPrInventVersionText": mnPrInventVersionText,
       "mnPrInventSerialText": mnPrInventSerialText,
       "mnPrInventCompStatus": mnPrInventCompStatus,
       "mnPrInventCompType": mnPrInventCompType,
       "mnPrODUConfTable": mnPrODUConfTable,
       "mnPrODUConfEntry": mnPrODUConfEntry,
       "mnPrODUConfTxFreq": mnPrODUConfTxFreq,
       "mnPrODUConfRxFreq": mnPrODUConfRxFreq,
       "mnPrODUConfTxPower": mnPrODUConfTxPower,
       "mnPrODUConfATPCEnable": mnPrODUConfATPCEnable,
       "mnPrODUConfATPCTargetRSL": mnPrODUConfATPCTargetRSL,
       "mnPrODUConfMute": mnPrODUConfMute,
       "mnPrODUConfCurInversion": mnPrODUConfCurInversion,
       "mnPrODUConfDefInversion": mnPrODUConfDefInversion,
       "mnPrIDUConfTable": mnPrIDUConfTable,
       "mnPrIDUConfEntry": mnPrIDUConfEntry,
       "mnPrIDUConfProtMode": mnPrIDUConfProtMode,
       "mnPrIDUConfProtOnlineRequest": mnPrIDUConfProtOnlineRequest,
       "mnPrIDUConfOrderwireCode": mnPrIDUConfOrderwireCode,
       "mnPrIDUConfOrderwireMode": mnPrIDUConfOrderwireMode,
       "mnPrIDUConfAUX1Rate": mnPrIDUConfAUX1Rate,
       "mnPrIDUConfAUX2Rate": mnPrIDUConfAUX2Rate,
       "mnPrIDUConfCraftBaud": mnPrIDUConfCraftBaud,
       "mnPrIDUConfProposedCapacity": mnPrIDUConfProposedCapacity,
       "mnPrIDUConfAllocateLimA": mnPrIDUConfAllocateLimA,
       "mnPrIDUConfProtTwinAddress": mnPrIDUConfProtTwinAddress,
       "mnPrIDUConfIFBandwidthProposed": mnPrIDUConfIFBandwidthProposed,
       "mnPrIDUConfIFBandwidthConf": mnPrIDUConfIFBandwidthConf,
       "mnPrIDUConfNmsPortSpeed": mnPrIDUConfNmsPortSpeed,
       "mnPrIDUConfNmsPortMode": mnPrIDUConfNmsPortMode,
       "mnPrIDUConfCapacityConf": mnPrIDUConfCapacityConf,
       "mnPrIDUConfCapacityProp": mnPrIDUConfCapacityProp,
       "mnPrIDUConfIntEthStatusInst": mnPrIDUConfIntEthStatusInst,
       "mnPrIDUConfIntEthStatusConf": mnPrIDUConfIntEthStatusConf,
       "mnPrIDUConfIntEthStatusProp": mnPrIDUConfIntEthStatusProp,
       "mnPrIDUConfIntEthCapacityInst": mnPrIDUConfIntEthCapacityInst,
       "mnPrIDUConfIntEthCapacityConf": mnPrIDUConfIntEthCapacityConf,
       "mnPrIDUConfIntEthCapacityProp": mnPrIDUConfIntEthCapacityProp,
       "mnPrIDUConfLoopSwitchMode": mnPrIDUConfLoopSwitchMode,
       "mnPrIDUConfStatLicCapacity": mnPrIDUConfStatLicCapacity,
       "mnPrLIMConfTable": mnPrLIMConfTable,
       "mnPrLIMConfEntry": mnPrLIMConfEntry,
       "mnPrLIMConfTypeInstalled": mnPrLIMConfTypeInstalled,
       "mnPrLIMConfTypeProposed": mnPrLIMConfTypeProposed,
       "mnPrLIMConfTypeConf": mnPrLIMConfTypeConf,
       "mnPrLIMConfCapacity": mnPrLIMConfCapacity,
       "mnPrLIMConfCapacityInst": mnPrLIMConfCapacityInst,
       "mnPrLIMConfCapacityConf": mnPrLIMConfCapacityConf,
       "mnPrLIMConfCapacityProp": mnPrLIMConfCapacityProp,
       "mnPrLIMConfSHARPInstalled": mnPrLIMConfSHARPInstalled,
       "mnPrTribConfTable": mnPrTribConfTable,
       "mnPrTribConfEntry": mnPrTribConfEntry,
       "mnPrTribConfAdminEquipped": mnPrTribConfAdminEquipped,
       "mnPrSysConfTable": mnPrSysConfTable,
       "mnPrSysConfEntry": mnPrSysConfEntry,
       "mnPrSysConfRadioName": mnPrSysConfRadioName,
       "mnPrSysConfLocation": mnPrSysConfLocation,
       "mnPrSysConfContact": mnPrSysConfContact,
       "mnPrSysConfDateAndTime": mnPrSysConfDateAndTime,
       "mnPrSysConfLicenseKey": mnPrSysConfLicenseKey,
       "mnPrSysConfThroughPut": mnPrSysConfThroughPut,
       "mnPrSysConfTimeZone": mnPrSysConfTimeZone,
       "mnPrSysConfDaylightSavings": mnPrSysConfDaylightSavings,
       "mnPrSysConfDpmStatus": mnPrSysConfDpmStatus,
       "mnPrSysConfDpmPolicy": mnPrSysConfDpmPolicy,
       "mnPrSysConfEncMode": mnPrSysConfEncMode,
       "mnPrSysConfEncPassword": mnPrSysConfEncPassword,
       "mnPrSysConfEncFailPolicy": mnPrSysConfEncFailPolicy,
       "mnPrSysConfFIPSKeyActivate": mnPrSysConfFIPSKeyActivate,
       "mnPrSysConfFIPSMode": mnPrSysConfFIPSMode,
       "mnPrUserConfTable": mnPrUserConfTable,
       "mnPrUserConfEntry": mnPrUserConfEntry,
       "mnPrUserConfIndex": mnPrUserConfIndex,
       "mnPrUserConfUsername": mnPrUserConfUsername,
       "mnPrUserConfPasswordSet": mnPrUserConfPasswordSet,
       "mnPrUserConfAccessLevel": mnPrUserConfAccessLevel,
       "mnPrUserConfAuthProtocol": mnPrUserConfAuthProtocol,
       "mnPrUserConfPrivProtocol": mnPrUserConfPrivProtocol,
       "mnPrUserConfPrivPwdSet": mnPrUserConfPrivPwdSet,
       "mnPrAlarmConfTable": mnPrAlarmConfTable,
       "mnPrAlarmConfEntry": mnPrAlarmConfEntry,
       "mnAlarmIndex": mnAlarmIndex,
       "mnPrAlarmConfName": mnPrAlarmConfName,
       "mnPrAlarmConfUserName": mnPrAlarmConfUserName,
       "mnPrAlarmConfAbrev": mnPrAlarmConfAbrev,
       "mnPrAlarmConfMap": mnPrAlarmConfMap,
       "mnPrAlarmConfCircuitType": mnPrAlarmConfCircuitType,
       "mnPrAlarmConfThreshold": mnPrAlarmConfThreshold,
       "mnPrAlarmConfSet": mnPrAlarmConfSet,
       "mnPrNMConfTable": mnPrNMConfTable,
       "mnPrNMConfEntry": mnPrNMConfEntry,
       "mnPrNMConfDefGateway": mnPrNMConfDefGateway,
       "mnPrNMConfTrapMode": mnPrNMConfTrapMode,
       "mnPrNMConfTFTPAddr": mnPrNMConfTFTPAddr,
       "mnPrNMConfTFTPFile": mnPrNMConfTFTPFile,
       "mnPrNMConfSNTPAddr": mnPrNMConfSNTPAddr,
       "mnPrNMConfSNTPInterval": mnPrNMConfSNTPInterval,
       "mnPrNMConfSNTPTimeout": mnPrNMConfSNTPTimeout,
       "mnPrNMConfAuthMode": mnPrNMConfAuthMode,
       "mnPrNMConfRADTimeout": mnPrNMConfRADTimeout,
       "mnPrNMConfRADRetries": mnPrNMConfRADRetries,
       "mnPrNMConfRADDeadtime": mnPrNMConfRADDeadtime,
       "mnPrNMConfRADMinPwdLen": mnPrNMConfRADMinPwdLen,
       "mnPrIPIfConfTable": mnPrIPIfConfTable,
       "mnPrIPIfConfEntry": mnPrIPIfConfEntry,
       "mnIPIfIndex": mnIPIfIndex,
       "mnPrIPIfConfIPAddr": mnPrIPIfConfIPAddr,
       "mnPrIPIfConfSubnetMask": mnPrIPIfConfSubnetMask,
       "mnPrIPIfConfRouting": mnPrIPIfConfRouting,
       "mnPrIPIfConfRoutingBit": mnPrIPIfConfRoutingBit,
       "mnPrIPIfConfCustomAddress": mnPrIPIfConfCustomAddress,
       "mnPrIPIfConfCustomSubnet": mnPrIPIfConfCustomSubnet,
       "mnPrRouteConfTable": mnPrRouteConfTable,
       "mnPrRouteConfEntry": mnPrRouteConfEntry,
       "mnPrRouteConfIndex": mnPrRouteConfIndex,
       "mnPrRouteConfDest": mnPrRouteConfDest,
       "mnPrRouteConfMask": mnPrRouteConfMask,
       "mnPrRouteConfNextHop": mnPrRouteConfNextHop,
       "mnPrRouteConfMetric": mnPrRouteConfMetric,
       "mnPrRouteConfRowStatus": mnPrRouteConfRowStatus,
       "mnPrTrapConfTable": mnPrTrapConfTable,
       "mnPrTrapConfEntry": mnPrTrapConfEntry,
       "mnTrapIndex": mnTrapIndex,
       "mnPrTrapConfTrapAddr": mnPrTrapConfTrapAddr,
       "mnPrTrapConfTrapComm": mnPrTrapConfTrapComm,
       "mnPrTrapConfRowStatus": mnPrTrapConfRowStatus,
       "mnPrPPPConfTable": mnPrPPPConfTable,
       "mnPrPPPConfEntry": mnPrPPPConfEntry,
       "mnPrPPPConfBaudRate": mnPrPPPConfBaudRate,
       "mnPrPPPConfInitString": mnPrPPPConfInitString,
       "mnPrPPPConfChapUser": mnPrPPPConfChapUser,
       "mnPrPPPConfChapSecret": mnPrPPPConfChapSecret,
       "mnPrPerfHistConfigObjects": mnPrPerfHistConfigObjects,
       "mnPrPerfHistConfTable": mnPrPerfHistConfTable,
       "mnPrPerfHistConfEntry": mnPrPerfHistConfEntry,
       "mnPrPerfHistConfEnable": mnPrPerfHistConfEnable,
       "mnPrPerfHistConfInterval": mnPrPerfHistConfInterval,
       "mnPrPerfHistConfFilename": mnPrPerfHistConfFilename,
       "mnPrPerfHistConfUploadInterval": mnPrPerfHistConfUploadInterval,
       "mnPrPerfHistConfVarTable": mnPrPerfHistConfVarTable,
       "mnPrPerfHistConfVarEntry": mnPrPerfHistConfVarEntry,
       "mnPrPerfHistConfVarIndex": mnPrPerfHistConfVarIndex,
       "mnPrPerfHistConfVarName": mnPrPerfHistConfVarName,
       "mnPrPerfHistConfVarEnable": mnPrPerfHistConfVarEnable,
       "mnPrTribE1ConfTable": mnPrTribE1ConfTable,
       "mnPrTribE1ConfEntry": mnPrTribE1ConfEntry,
       "mnPrTribE1ConfLineType": mnPrTribE1ConfLineType,
       "mnPrAuxConfTable": mnPrAuxConfTable,
       "mnPrAuxConfEntry": mnPrAuxConfEntry,
       "mnPrAuxIndex": mnPrAuxIndex,
       "mnPrAuxConfBaudRate": mnPrAuxConfBaudRate,
       "mnPrAuxConfParity": mnPrAuxConfParity,
       "mnPrAuxConfInversion": mnPrAuxConfInversion,
       "mnPrAuxConfStopBits": mnPrAuxConfStopBits,
       "mnPrEthPortConfTable": mnPrEthPortConfTable,
       "mnPrEthPortConfEntry": mnPrEthPortConfEntry,
       "mnPrEthPortIndex": mnPrEthPortIndex,
       "mnPrEthPortConfSpeed": mnPrEthPortConfSpeed,
       "mnPrSwitchPlaneConfTable": mnPrSwitchPlaneConfTable,
       "mnPrSwitchPlaneConfEntry": mnPrSwitchPlaneConfEntry,
       "mnPrSwitchPlaneIndex": mnPrSwitchPlaneIndex,
       "mnPrSwitchPlaneConfStatus": mnPrSwitchPlaneConfStatus,
       "mnPrSwitchPlaneConfOnlineReq": mnPrSwitchPlaneConfOnlineReq,
       "mnPrDpmCiConfTable": mnPrDpmCiConfTable,
       "mnPrDpmCiConfEntry": mnPrDpmCiConfEntry,
       "mnPrDpmCiIndex": mnPrDpmCiIndex,
       "mnPrDpmCiConfType": mnPrDpmCiConfType,
       "mnPrDpmCiConfFullName": mnPrDpmCiConfFullName,
       "mnPrDpmCiConfSharpCapable": mnPrDpmCiConfSharpCapable,
       "mnPrDpmCiConfActCgName": mnPrDpmCiConfActCgName,
       "mnPrDpmCiConfActSharpEnabled": mnPrDpmCiConfActSharpEnabled,
       "mnPrDpmCiConfActOtherIntf": mnPrDpmCiConfActOtherIntf,
       "mnPrDpmCiConfPropAvailable": mnPrDpmCiConfPropAvailable,
       "mnPrDpmCiConfPropCgName": mnPrDpmCiConfPropCgName,
       "mnPrDpmCiConfPropSharpEnabled": mnPrDpmCiConfPropSharpEnabled,
       "mnPrDpmCiConfPropOtherIntf": mnPrDpmCiConfPropOtherIntf,
       "mnPrDpmCgConfTable": mnPrDpmCgConfTable,
       "mnPrDpmCgConfEntry": mnPrDpmCgConfEntry,
       "mnPrDpmCgIndex": mnPrDpmCgIndex,
       "mnPrDpmCgConfName": mnPrDpmCgConfName,
       "mnPrDpmCgConfType": mnPrDpmCgConfType,
       "mnPrDpmCgConfCount": mnPrDpmCgConfCount,
       "mnPrDpmCgConfChMinRate": mnPrDpmCgConfChMinRate,
       "mnPrDpmCgConfChMaxRate": mnPrDpmCgConfChMaxRate,
       "mnPrDpmCgConfChAllocRate": mnPrDpmCgConfChAllocRate,
       "mnPrDpmCgConfIntf1": mnPrDpmCgConfIntf1,
       "mnPrDpmCgConfSharpEnabled1": mnPrDpmCgConfSharpEnabled1,
       "mnPrDpmCgConfIntf2": mnPrDpmCgConfIntf2,
       "mnPrDpmCgConfSharpEnabled2": mnPrDpmCgConfSharpEnabled2,
       "mnPrDpmCgConfRowStatus": mnPrDpmCgConfRowStatus,
       "mnPrSHARPChanTable": mnPrSHARPChanTable,
       "mnPrSHARPChanEntry": mnPrSHARPChanEntry,
       "mnPrSHARPChanStatus": mnPrSHARPChanStatus,
       "mnPrSHARPChanActiveChan": mnPrSHARPChanActiveChan,
       "mnPrSHARPChanMasterBER": mnPrSHARPChanMasterBER,
       "mnPrSHARPChanSlaveBER": mnPrSHARPChanSlaveBER,
       "mnPrSHARPChanEnable": mnPrSHARPChanEnable,
       "mnPrSHARPChanSwitchMode": mnPrSHARPChanSwitchMode,
       "mnPrSHARPChanMasterThresh": mnPrSHARPChanMasterThresh,
       "mnPrSHARPChanSlaveThresh": mnPrSHARPChanSlaveThresh,
       "mnPrSHARPChanManualForce": mnPrSHARPChanManualForce,
       "mnPrSHARPChanSwitchPref": mnPrSHARPChanSwitchPref,
       "mnPrTribXConfTable": mnPrTribXConfTable,
       "mnPrTribXConfEntry": mnPrTribXConfEntry,
       "mnPrTribXConfAdminEquipped": mnPrTribXConfAdminEquipped,
       "mnPrTribXConfLineType": mnPrTribXConfLineType,
       "mnPrTribXConfLocalLoopback": mnPrTribXConfLocalLoopback,
       "mnPrTribXConfRemoteLoopback": mnPrTribXConfRemoteLoopback,
       "mnPrTribXConfTribStatus": mnPrTribXConfTribStatus,
       "mnPrEthSwTable": mnPrEthSwTable,
       "mnPrEthSwEntry": mnPrEthSwEntry,
       "mnPrEthSwIndex": mnPrEthSwIndex,
       "mnPrEthSwStatRRPStatus": mnPrEthSwStatRRPStatus,
       "mnPrEthSwConfRRPMode": mnPrEthSwConfRRPMode,
       "mnPrEthSwConfRRPPollInterval": mnPrEthSwConfRRPPollInterval,
       "mnPrEthSwConfRRPThreshold": mnPrEthSwConfRRPThreshold,
       "mnPrEthSwConfRRPFwdDelay": mnPrEthSwConfRRPFwdDelay,
       "mnPrEthSwConfRRPRingID": mnPrEthSwConfRRPRingID,
       "mnPrAcmTable": mnPrAcmTable,
       "mnPrAcmEntry": mnPrAcmEntry,
       "mnPrAcmModeProp": mnPrAcmModeProp,
       "mnPrAcmModeConf": mnPrAcmModeConf,
       "mnPrAcmMaxCapProp": mnPrAcmMaxCapProp,
       "mnPrAcmMaxCapConf": mnPrAcmMaxCapConf,
       "mnPrAcmMinEthThreshProp": mnPrAcmMinEthThreshProp,
       "mnPrAcmMinEthThreshConf": mnPrAcmMinEthThreshConf,
       "mnPrAcmTxPower": mnPrAcmTxPower,
       "mnPrAcmMaxTxPower": mnPrAcmMaxTxPower,
       "mnPrAcmProfileHeader": mnPrAcmProfileHeader,
       "mnPrAcmProfileTable": mnPrAcmProfileTable,
       "mnPrAcmProfileEntry": mnPrAcmProfileEntry,
       "mnPrAcmProfileIndex": mnPrAcmProfileIndex,
       "mnPrAcmProfileText": mnPrAcmProfileText,
       "mnPrRADSrvConfTable": mnPrRADSrvConfTable,
       "mnPrRADSrvConfEntry": mnPrRADSrvConfEntry,
       "mnPrRADSrvIndex": mnPrRADSrvIndex,
       "mnPrRADSrvConfName": mnPrRADSrvConfName,
       "mnPrRADSrvConfAuthPort": mnPrRADSrvConfAuthPort,
       "mnPrRADSrvConfSecret": mnPrRADSrvConfSecret,
       "mnPrRRPPTable": mnPrRRPPTable,
       "mnPrRRPPEntry": mnPrRRPPEntry,
       "mnPrRRPPIndex": mnPrRRPPIndex,
       "mnPrRRPPRowStatus": mnPrRRPPRowStatus,
       "mnPrRRPPStatus": mnPrRRPPStatus,
       "mnPrRRPPConfMode": mnPrRRPPConfMode,
       "mnPrRRPPConfPollInterval": mnPrRRPPConfPollInterval,
       "mnPrRRPPConfThreshold": mnPrRRPPConfThreshold,
       "mnPrRRPPConfFwdDelay": mnPrRRPPConfFwdDelay,
       "mnPrRRPPConfLdpVlan": mnPrRRPPConfLdpVlan,
       "mnPrRRPPConfRingPort1": mnPrRRPPConfRingPort1,
       "mnPrRRPPConfRingPort2": mnPrRRPPConfRingPort2,
       "mnPrRRPPConfProtVlans": mnPrRRPPConfProtVlans,
       "mnPrRRPPConfADPorts": mnPrRRPPConfADPorts,
       "mnPrRRPPADPortAvailability": mnPrRRPPADPortAvailability,
       "mnPrCUConfTable": mnPrCUConfTable,
       "mnPrCUConfEntry": mnPrCUConfEntry,
       "mnPrCUConfRRPPLLFHysterSetTime": mnPrCUConfRRPPLLFHysterSetTime,
       "mnPrCUConfRRPPLLFHysterClrTime": mnPrCUConfRRPPLLFHysterClrTime,
       "mnPrUtilityObjects": mnPrUtilityObjects,
       "mnPrSCPCtlTable": mnPrSCPCtlTable,
       "mnPrSCPCtlEntry": mnPrSCPCtlEntry,
       "mnPrSCPCtlCmd": mnPrSCPCtlCmd,
       "mnPrSCPCtlCmdStringArg": mnPrSCPCtlCmdStringArg,
       "mnPrSCPCtlCmdNumArg": mnPrSCPCtlCmdNumArg,
       "mnPrSCPCtlCmdProgress": mnPrSCPCtlCmdProgress,
       "mnPrSCPCtlCmdResult": mnPrSCPCtlCmdResult,
       "mnPrDiagSnapTable": mnPrDiagSnapTable,
       "mnPrDiagSnapEntry": mnPrDiagSnapEntry,
       "mnPrDiagSnapBuffer": mnPrDiagSnapBuffer,
       "mnPrDiagSnapSource": mnPrDiagSnapSource,
       "mnPrDiagSnapOverride": mnPrDiagSnapOverride,
       "mnPrVlanObjects": mnPrVlanObjects,
       "mnPrVlanDeviceConfTable": mnPrVlanDeviceConfTable,
       "mnPrVlanDeviceConfEntry": mnPrVlanDeviceConfEntry,
       "mnPrVlanDeviceCapabilities": mnPrVlanDeviceCapabilities,
       "mnPrVlanDeviceTfcClsEnabled": mnPrVlanDeviceTfcClsEnabled,
       "mnPrVlanDeviceNumTrafficClasses": mnPrVlanDeviceNumTrafficClasses,
       "mnPrVlanTrafficClassOrder": mnPrVlanTrafficClassOrder,
       "mnPrVlanTrafficClassWieghted": mnPrVlanTrafficClassWieghted,
       "mnPrVlanDeviceVlanVersionNumber": mnPrVlanDeviceVlanVersionNumber,
       "mnPrVlanDeviceMaxVlanId": mnPrVlanDeviceMaxVlanId,
       "mnPrVlanDeviceMaxSupportedVlans": mnPrVlanDeviceMaxSupportedVlans,
       "mnPrVlanDeviceNumVlans": mnPrVlanDeviceNumVlans,
       "mnPrVlanDeviceNumDeletes": mnPrVlanDeviceNumDeletes,
       "mnPrVlanDeviceLinkLossForwarding": mnPrVlanDeviceLinkLossForwarding,
       "mnPrVlanDevice1qEnabled": mnPrVlanDevice1qEnabled,
       "mnPrVlanDeviceIgnoreTags": mnPrVlanDeviceIgnoreTags,
       "mnPrVlanDeviceRateLimitUnit": mnPrVlanDeviceRateLimitUnit,
       "mnPrVlanDeviceLinkUntagEnable": mnPrVlanDeviceLinkUntagEnable,
       "mnPrVlanDeviceLinkFrameMode": mnPrVlanDeviceLinkFrameMode,
       "mnPrVlanPortConfTable": mnPrVlanPortConfTable,
       "mnPrVlanPortConfEntry": mnPrVlanPortConfEntry,
       "mnPrVlanPortCapabilities": mnPrVlanPortCapabilities,
       "mnPrVlanPortDefaultUserPriority": mnPrVlanPortDefaultUserPriority,
       "mnPrVlanPortPvid": mnPrVlanPortPvid,
       "mnPrVlanPortAcceptableFrameTypes": mnPrVlanPortAcceptableFrameTypes,
       "mnPrVlanPortIngressFiltering": mnPrVlanPortIngressFiltering,
       "mnPrVlanPortGvrpStatus": mnPrVlanPortGvrpStatus,
       "mnPrVlanPortLineSpeed": mnPrVlanPortLineSpeed,
       "mnPrVlanPortRateLimitPri0": mnPrVlanPortRateLimitPri0,
       "mnPrVlanPortRateLimitPri1": mnPrVlanPortRateLimitPri1,
       "mnPrVlanPortRateLimitPri2": mnPrVlanPortRateLimitPri2,
       "mnPrVlanPortRateLimitPri3": mnPrVlanPortRateLimitPri3,
       "mnPrVlanPortUntagEnable": mnPrVlanPortUntagEnable,
       "mnPrVlanPortMaxFrameSize": mnPrVlanPortMaxFrameSize,
       "mnPrVlanPortRateLimitMult": mnPrVlanPortRateLimitMult,
       "mnPrVlanPortRateControlMode": mnPrVlanPortRateControlMode,
       "mnPrVlanPortFrameMode": mnPrVlanPortFrameMode,
       "mnPrVlanPortIngressFilterMode": mnPrVlanPortIngressFilterMode,
       "mnPrVlanPortIngressRateLimit": mnPrVlanPortIngressRateLimit,
       "mnPrVlanPortIngressBurstAlloc": mnPrVlanPortIngressBurstAlloc,
       "mnPrVlanPortLearningMode": mnPrVlanPortLearningMode,
       "mnPrVlanPortFloodMode": mnPrVlanPortFloodMode,
       "mnPrVlanPortEthertype": mnPrVlanPortEthertype,
       "mnPr1qVlanCurrentTable": mnPr1qVlanCurrentTable,
       "mnPr1qVlanCurrentEntry": mnPr1qVlanCurrentEntry,
       "mnPr1qVlanIndex": mnPr1qVlanIndex,
       "mnPr1qVlanId": mnPr1qVlanId,
       "mnPr1qVlanFdbId": mnPr1qVlanFdbId,
       "mnPr1qVlanCurrentEgressPorts": mnPr1qVlanCurrentEgressPorts,
       "mnPr1qVlanCurrentUntaggedPorts": mnPr1qVlanCurrentUntaggedPorts,
       "mnPr1qVlanStatus": mnPr1qVlanStatus,
       "mnPr1qVlanCreationTime": mnPr1qVlanCreationTime,
       "mnPr1qVlanStaticTable": mnPr1qVlanStaticTable,
       "mnPr1qVlanStaticEntry": mnPr1qVlanStaticEntry,
       "mnPr1qVlanStaticId": mnPr1qVlanStaticId,
       "mnPr1qVlanStaticName": mnPr1qVlanStaticName,
       "mnPr1qVlanStaticEgressPorts": mnPr1qVlanStaticEgressPorts,
       "mnPr1qVlanForbiddenEgressPorts": mnPr1qVlanForbiddenEgressPorts,
       "mnPr1qVlanStaticUntaggedPorts": mnPr1qVlanStaticUntaggedPorts,
       "mnPr1qVlanStaticRowStatus": mnPr1qVlanStaticRowStatus,
       "mnPr1qVlanStaticFID": mnPr1qVlanStaticFID,
       "mnPr1qVlanStaticRingID": mnPr1qVlanStaticRingID,
       "mnPrVlanDeviceTrafficClassTable": mnPrVlanDeviceTrafficClassTable,
       "mnPrVlanDeviceTrafficClassEntry": mnPrVlanDeviceTrafficClassEntry,
       "mnPrVlanDeviceTrafficClassIndex": mnPrVlanDeviceTrafficClassIndex,
       "mnPrVlanDeviceTfcClsPriority": mnPrVlanDeviceTfcClsPriority,
       "mnPrVlanDeviceTrafficClass": mnPrVlanDeviceTrafficClass,
       "mnPrVlanDeviceTosTable": mnPrVlanDeviceTosTable,
       "mnPrVlanDeviceTosEntry": mnPrVlanDeviceTosEntry,
       "mnPrVlanDeviceTosIndex": mnPrVlanDeviceTosIndex,
       "mnPrVlanDeviceTosTrafficClass": mnPrVlanDeviceTosTrafficClass,
       "mnPrVlanDeviceTos": mnPrVlanDeviceTos,
       "mnPrVlanDeviceDscpTable": mnPrVlanDeviceDscpTable,
       "mnPrVlanDeviceDscpEntry": mnPrVlanDeviceDscpEntry,
       "mnPrVlanDeviceDscpIndex": mnPrVlanDeviceDscpIndex,
       "mnPrVlanDeviceDscpValueToMap": mnPrVlanDeviceDscpValueToMap,
       "mnPrVlanDeviceDscpQosClass": mnPrVlanDeviceDscpQosClass,
       "mnPrSecurityObjects": mnPrSecurityObjects,
       "mnPrProtocolConfTable": mnPrProtocolConfTable,
       "mnPrProtocolConfEntry": mnPrProtocolConfEntry,
       "mnPrProtocolIndex": mnPrProtocolIndex,
       "mnPrProtocolConfAccess": mnPrProtocolConfAccess,
       "mnCapabilities": mnCapabilities,
       "mnExperimental": mnExperimental}
)
