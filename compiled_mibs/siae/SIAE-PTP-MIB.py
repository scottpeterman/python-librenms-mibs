# SNMP MIB module (SIAE-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-PTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:25 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(AlarmSeverityCode,
 AlarmStatus) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "AlarmSeverityCode",
    "AlarmStatus")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ptp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ClockDomainType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 43),
    )



class ClockProfileType(TextualConvention, Integer32):
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
        *(("default", 1),
          ("telecom", 2),
          ("vendorspecific", 3))
    )



class ClockQualityAccuracyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              46,
              47,
              48,
              49,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("reserved00", 1),
          ("nanoSecond25", 32),
          ("nanoSecond100", 33),
          ("nanoSecond250", 34),
          ("microSec1", 35),
          ("microSec2dot5", 36),
          ("microSec10", 37),
          ("microSec25", 38),
          ("microSec100", 39),
          ("microSec250", 40),
          ("milliSec1", 41),
          ("milliSec2dot5", 42),
          ("milliSec10", 43),
          ("milliSec25", 44),
          ("milliSec100", 45),
          ("milliSec250", 46),
          ("second1", 47),
          ("second10", 48),
          ("secondGreater10", 49),
          ("unknown", 254),
          ("reserved255", 255))
    )



class ClockQualityClassType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ClockStateType(TextualConvention, Integer32):
    status = "current"
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
        *(("freerun", 1),
          ("acquiring", 2),
          ("locked", 3),
          ("holdoverInSpec", 4),
          ("holdoverOutOfSpec", 5))
    )



class ClockTimeSourceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              96,
              144,
              160,
              255)
        )
    )
    namedValues = NamedValues(
        *(("atomicClock", 16),
          ("gps", 32),
          ("terrestrialRadio", 48),
          ("ptp", 64),
          ("ntp", 80),
          ("handSet", 96),
          ("other", 144),
          ("internalOscillator", 160),
          ("reserved", 255))
    )



class ClockInstanceType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ClockPPSInstanceType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ClockPortNumber(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ClockPortState(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("initializing", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("preMaster", 5),
          ("master", 6),
          ("passive", 7),
          ("uncalibrated", 8),
          ("slave", 9))
    )



class ClockMechanismType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("e2e", 1)
    )



class ClockTimeInterval(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class ClockType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("boundaryClock", 2)
    )



class PtpClockToDFormatType(TextualConvention, Integer32):
    status = "current"
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("telecomTimeEvent", 1),
          ("telecomTimeAnnounce", 2),
          ("telecomGNSSstatus", 3),
          ("nmeazda", 4),
          ("iso8601", 5),
          ("ntp", 6),
          ("ublox", 7),
          ("chinaMobile", 8),
          ("chinaTelecom", 9),
          ("bcm", 10),
          ("bcmts", 11))
    )



# MIB Managed Objects in the order of their OIDs



class _PtpMibVersion_Type(Integer32):
    """Custom type ptpMibVersion based on Integer32"""
    defaultValue = 1


_PtpMibVersion_Type.__name__ = "Integer32"
_PtpMibVersion_Object = MibScalar
ptpMibVersion = _PtpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 1),
    _PtpMibVersion_Type()
)
ptpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpMibVersion.setStatus("current")
_PtpProfileDataSet_ObjectIdentity = ObjectIdentity
ptpProfileDataSet = _PtpProfileDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 2)
)
_PtpSystemProfile_Type = ClockProfileType
_PtpSystemProfile_Object = MibScalar
ptpSystemProfile = _PtpSystemProfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 2, 1),
    _PtpSystemProfile_Type()
)
ptpSystemProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpSystemProfile.setStatus("current")


class _PtpProfileName_Type(DisplayString):
    """Custom type ptpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PtpProfileName_Type.__name__ = "DisplayString"
_PtpProfileName_Object = MibScalar
ptpProfileName = _PtpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 2, 2),
    _PtpProfileName_Type()
)
ptpProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpProfileName.setStatus("current")


class _PtpProfilePrimaryVersion_Type(Integer32):
    """Custom type ptpProfilePrimaryVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PtpProfilePrimaryVersion_Type.__name__ = "Integer32"
_PtpProfilePrimaryVersion_Object = MibScalar
ptpProfilePrimaryVersion = _PtpProfilePrimaryVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 2, 3),
    _PtpProfilePrimaryVersion_Type()
)
ptpProfilePrimaryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpProfilePrimaryVersion.setStatus("current")


class _PtpProfileRevisionNumber_Type(Integer32):
    """Custom type ptpProfileRevisionNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PtpProfileRevisionNumber_Type.__name__ = "Integer32"
_PtpProfileRevisionNumber_Object = MibScalar
ptpProfileRevisionNumber = _PtpProfileRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 2, 4),
    _PtpProfileRevisionNumber_Type()
)
ptpProfileRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpProfileRevisionNumber.setStatus("current")


class _PtpProfileIdentifier_Type(OctetString):
    """Custom type ptpProfileIdentifier based on OctetString"""
    defaultHexValue = "0019A7010100"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_PtpProfileIdentifier_Type.__name__ = "OctetString"
_PtpProfileIdentifier_Object = MibScalar
ptpProfileIdentifier = _PtpProfileIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 2, 5),
    _PtpProfileIdentifier_Type()
)
ptpProfileIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpProfileIdentifier.setStatus("current")
_PtpSpecificDataSet_ObjectIdentity = ObjectIdentity
ptpSpecificDataSet = _PtpSpecificDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3)
)
_PtpSpecificDataSetTable_Object = MibTable
ptpSpecificDataSetTable = _PtpSpecificDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3, 1)
)
if mibBuilder.loadTexts:
    ptpSpecificDataSetTable.setStatus("current")
_PtpSpecificDataSetEntry_Object = MibTableRow
ptpSpecificDataSetEntry = _PtpSpecificDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3, 1, 1)
)
ptpSpecificDataSetEntry.setIndexNames(
    (0, "SIAE-PTP-MIB", "ptpClockDomainIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockTypeIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpSpecificDataSetEntry.setStatus("current")


class _PtpAdminStatus_Type(Integer32):
    """Custom type ptpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_PtpAdminStatus_Type.__name__ = "Integer32"
_PtpAdminStatus_Object = MibTableColumn
ptpAdminStatus = _PtpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3, 1, 1, 1),
    _PtpAdminStatus_Type()
)
ptpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpAdminStatus.setStatus("current")


class _PtpStaticPortRole_Type(TruthValue):
    """Custom type ptpStaticPortRole based on TruthValue"""
    defaultValue = 2


_PtpStaticPortRole_Type.__name__ = "TruthValue"
_PtpStaticPortRole_Object = MibTableColumn
ptpStaticPortRole = _PtpStaticPortRole_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3, 1, 1, 2),
    _PtpStaticPortRole_Type()
)
ptpStaticPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpStaticPortRole.setStatus("current")
_PtpClockState_Type = ClockStateType
_PtpClockState_Object = MibTableColumn
ptpClockState = _PtpClockState_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3, 1, 1, 3),
    _PtpClockState_Type()
)
ptpClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockState.setStatus("current")


class _PtpCompliance_Type(Integer32):
    """Custom type ptpCompliance based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strictCompatibility", 1),
          ("looseCompatibility", 2))
    )


_PtpCompliance_Type.__name__ = "Integer32"
_PtpCompliance_Object = MibTableColumn
ptpCompliance = _PtpCompliance_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3, 1, 1, 4),
    _PtpCompliance_Type()
)
ptpCompliance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpCompliance.setStatus("current")
_PtpSpecificAlarmTable_Object = MibTable
ptpSpecificAlarmTable = _PtpSpecificAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3, 2)
)
if mibBuilder.loadTexts:
    ptpSpecificAlarmTable.setStatus("current")
_PtpSpecificAlarmEntry_Object = MibTableRow
ptpSpecificAlarmEntry = _PtpSpecificAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3, 2, 1)
)
ptpSpecificAlarmEntry.setIndexNames(
    (0, "SIAE-PTP-MIB", "ptpClockDomainIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockTypeIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpSpecificAlarmEntry.setStatus("current")
_PtpFreeRunningAlarm_Type = AlarmStatus
_PtpFreeRunningAlarm_Object = MibTableColumn
ptpFreeRunningAlarm = _PtpFreeRunningAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3, 2, 1, 1),
    _PtpFreeRunningAlarm_Type()
)
ptpFreeRunningAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpFreeRunningAlarm.setStatus("current")
_PtpHoldoverInSpecAlarm_Type = AlarmStatus
_PtpHoldoverInSpecAlarm_Object = MibTableColumn
ptpHoldoverInSpecAlarm = _PtpHoldoverInSpecAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3, 2, 1, 2),
    _PtpHoldoverInSpecAlarm_Type()
)
ptpHoldoverInSpecAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpHoldoverInSpecAlarm.setStatus("current")
_PtpHoldoverOutOfSpecAlarm_Type = AlarmStatus
_PtpHoldoverOutOfSpecAlarm_Object = MibTableColumn
ptpHoldoverOutOfSpecAlarm = _PtpHoldoverOutOfSpecAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3, 2, 1, 3),
    _PtpHoldoverOutOfSpecAlarm_Type()
)
ptpHoldoverOutOfSpecAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpHoldoverOutOfSpecAlarm.setStatus("current")


class _PtpFreeRunningAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type ptpFreeRunningAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_PtpFreeRunningAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PtpFreeRunningAlarmSeverityCode_Object = MibScalar
ptpFreeRunningAlarmSeverityCode = _PtpFreeRunningAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3, 3),
    _PtpFreeRunningAlarmSeverityCode_Type()
)
ptpFreeRunningAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpFreeRunningAlarmSeverityCode.setStatus("current")


class _PtpHoldoverInSpecAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type ptpHoldoverInSpecAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_PtpHoldoverInSpecAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PtpHoldoverInSpecAlarmSeverityCode_Object = MibScalar
ptpHoldoverInSpecAlarmSeverityCode = _PtpHoldoverInSpecAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3, 4),
    _PtpHoldoverInSpecAlarmSeverityCode_Type()
)
ptpHoldoverInSpecAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpHoldoverInSpecAlarmSeverityCode.setStatus("current")


class _PtpHoldoverOutOfSpecAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type ptpHoldoverOutOfSpecAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PtpHoldoverOutOfSpecAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PtpHoldoverOutOfSpecAlarmSeverityCode_Object = MibScalar
ptpHoldoverOutOfSpecAlarmSeverityCode = _PtpHoldoverOutOfSpecAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 3, 5),
    _PtpHoldoverOutOfSpecAlarmSeverityCode_Type()
)
ptpHoldoverOutOfSpecAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpHoldoverOutOfSpecAlarmSeverityCode.setStatus("current")
_PtpDefaultDataSet_ObjectIdentity = ObjectIdentity
ptpDefaultDataSet = _PtpDefaultDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4)
)
_PtpClockDataSetTable_Object = MibTable
ptpClockDataSetTable = _PtpClockDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1)
)
if mibBuilder.loadTexts:
    ptpClockDataSetTable.setStatus("current")
_PtpClockDataSetEntry_Object = MibTableRow
ptpClockDataSetEntry = _PtpClockDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1)
)
ptpClockDataSetEntry.setIndexNames(
    (0, "SIAE-PTP-MIB", "ptpClockDomainIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockTypeIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpClockDataSetEntry.setStatus("current")
_PtpClockDomainIndex_Type = ClockDomainType
_PtpClockDomainIndex_Object = MibTableColumn
ptpClockDomainIndex = _PtpClockDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1, 1),
    _PtpClockDomainIndex_Type()
)
ptpClockDomainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockDomainIndex.setStatus("current")
_PtpClockTypeIndex_Type = ClockType
_PtpClockTypeIndex_Object = MibTableColumn
ptpClockTypeIndex = _PtpClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1, 2),
    _PtpClockTypeIndex_Type()
)
ptpClockTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockTypeIndex.setStatus("current")


class _PtpClockInstanceIndex_Type(ClockInstanceType):
    """Custom type ptpClockInstanceIndex based on ClockInstanceType"""
    subtypeSpec = ClockInstanceType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PtpClockInstanceIndex_Type.__name__ = "ClockInstanceType"
_PtpClockInstanceIndex_Object = MibTableColumn
ptpClockInstanceIndex = _PtpClockInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1, 3),
    _PtpClockInstanceIndex_Type()
)
ptpClockInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockInstanceIndex.setStatus("current")


class _PtpClockIdentity_Type(OctetString):
    """Custom type ptpClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_PtpClockIdentity_Type.__name__ = "OctetString"
_PtpClockIdentity_Object = MibTableColumn
ptpClockIdentity = _PtpClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1, 4),
    _PtpClockIdentity_Type()
)
ptpClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockIdentity.setStatus("current")


class _PtpClockTwoStepFlag_Type(TruthValue):
    """Custom type ptpClockTwoStepFlag based on TruthValue"""
    defaultValue = 2


_PtpClockTwoStepFlag_Type.__name__ = "TruthValue"
_PtpClockTwoStepFlag_Object = MibTableColumn
ptpClockTwoStepFlag = _PtpClockTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1, 5),
    _PtpClockTwoStepFlag_Type()
)
ptpClockTwoStepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockTwoStepFlag.setStatus("current")


class _PtpClockNumberPorts_Type(Integer32):
    """Custom type ptpClockNumberPorts based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_PtpClockNumberPorts_Type.__name__ = "Integer32"
_PtpClockNumberPorts_Object = MibTableColumn
ptpClockNumberPorts = _PtpClockNumberPorts_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1, 6),
    _PtpClockNumberPorts_Type()
)
ptpClockNumberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockNumberPorts.setStatus("current")


class _PtpClockClass_Type(ClockQualityClassType):
    """Custom type ptpClockClass based on ClockQualityClassType"""
    defaultValue = 248


_PtpClockClass_Type.__name__ = "ClockQualityClassType"
_PtpClockClass_Object = MibTableColumn
ptpClockClass = _PtpClockClass_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1, 7),
    _PtpClockClass_Type()
)
ptpClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockClass.setStatus("current")


class _PtpClockAccuracy_Type(ClockQualityAccuracyType):
    """Custom type ptpClockAccuracy based on ClockQualityAccuracyType"""
    defaultValue = 254


_PtpClockAccuracy_Type.__name__ = "ClockQualityAccuracyType"
_PtpClockAccuracy_Object = MibTableColumn
ptpClockAccuracy = _PtpClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1, 8),
    _PtpClockAccuracy_Type()
)
ptpClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockAccuracy.setStatus("current")


class _PtpClockOffsetScaledLogVariance_Type(Integer32):
    """Custom type ptpClockOffsetScaledLogVariance based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PtpClockOffsetScaledLogVariance_Type.__name__ = "Integer32"
_PtpClockOffsetScaledLogVariance_Object = MibTableColumn
ptpClockOffsetScaledLogVariance = _PtpClockOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1, 9),
    _PtpClockOffsetScaledLogVariance_Type()
)
ptpClockOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockOffsetScaledLogVariance.setStatus("current")


class _PtpClockPriority1_Type(Integer32):
    """Custom type ptpClockPriority1 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 128),
    )


_PtpClockPriority1_Type.__name__ = "Integer32"
_PtpClockPriority1_Object = MibTableColumn
ptpClockPriority1 = _PtpClockPriority1_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1, 10),
    _PtpClockPriority1_Type()
)
ptpClockPriority1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpClockPriority1.setStatus("current")


class _PtpClockPriority2_Type(Integer32):
    """Custom type ptpClockPriority2 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PtpClockPriority2_Type.__name__ = "Integer32"
_PtpClockPriority2_Object = MibTableColumn
ptpClockPriority2 = _PtpClockPriority2_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1, 11),
    _PtpClockPriority2_Type()
)
ptpClockPriority2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpClockPriority2.setStatus("current")


class _PtpClockSlaveOnly_Type(TruthValue):
    """Custom type ptpClockSlaveOnly based on TruthValue"""
    defaultValue = 2


_PtpClockSlaveOnly_Type.__name__ = "TruthValue"
_PtpClockSlaveOnly_Object = MibTableColumn
ptpClockSlaveOnly = _PtpClockSlaveOnly_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1, 12),
    _PtpClockSlaveOnly_Type()
)
ptpClockSlaveOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpClockSlaveOnly.setStatus("current")


class _PtpClockLocalPriority_Type(Integer32):
    """Custom type ptpClockLocalPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PtpClockLocalPriority_Type.__name__ = "Integer32"
_PtpClockLocalPriority_Object = MibTableColumn
ptpClockLocalPriority = _PtpClockLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1, 13),
    _PtpClockLocalPriority_Type()
)
ptpClockLocalPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpClockLocalPriority.setStatus("current")
_PtpClockRowStatus_Type = RowStatus
_PtpClockRowStatus_Object = MibTableColumn
ptpClockRowStatus = _PtpClockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 4, 1, 1, 14),
    _PtpClockRowStatus_Type()
)
ptpClockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpClockRowStatus.setStatus("current")
_PtpCurrentDataSet_ObjectIdentity = ObjectIdentity
ptpCurrentDataSet = _PtpCurrentDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 5)
)
_PtpCurrentDataSetTable_Object = MibTable
ptpCurrentDataSetTable = _PtpCurrentDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 5, 1)
)
if mibBuilder.loadTexts:
    ptpCurrentDataSetTable.setStatus("current")
_PtpCurrentDataSetEntry_Object = MibTableRow
ptpCurrentDataSetEntry = _PtpCurrentDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 5, 1, 1)
)
ptpCurrentDataSetEntry.setIndexNames(
    (0, "SIAE-PTP-MIB", "ptpClockDomainIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockTypeIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpCurrentDataSetEntry.setStatus("current")
_PtpCurrentStepsRemoved_Type = Integer32
_PtpCurrentStepsRemoved_Object = MibTableColumn
ptpCurrentStepsRemoved = _PtpCurrentStepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 5, 1, 1, 1),
    _PtpCurrentStepsRemoved_Type()
)
ptpCurrentStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpCurrentStepsRemoved.setStatus("current")
_PtpCurrentOffsetFromMaster_Type = ClockTimeInterval
_PtpCurrentOffsetFromMaster_Object = MibTableColumn
ptpCurrentOffsetFromMaster = _PtpCurrentOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 5, 1, 1, 2),
    _PtpCurrentOffsetFromMaster_Type()
)
ptpCurrentOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpCurrentOffsetFromMaster.setStatus("current")
_PtpCurrentMeanPathDelay_Type = ClockTimeInterval
_PtpCurrentMeanPathDelay_Object = MibTableColumn
ptpCurrentMeanPathDelay = _PtpCurrentMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 5, 1, 1, 3),
    _PtpCurrentMeanPathDelay_Type()
)
ptpCurrentMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpCurrentMeanPathDelay.setStatus("current")
_PtpParentDataSet_ObjectIdentity = ObjectIdentity
ptpParentDataSet = _PtpParentDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 6)
)
_PtpParentDataSetTable_Object = MibTable
ptpParentDataSetTable = _PtpParentDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 6, 1)
)
if mibBuilder.loadTexts:
    ptpParentDataSetTable.setStatus("current")
_PtpParentDataSetEntry_Object = MibTableRow
ptpParentDataSetEntry = _PtpParentDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 6, 1, 1)
)
ptpParentDataSetEntry.setIndexNames(
    (0, "SIAE-PTP-MIB", "ptpClockDomainIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockTypeIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpParentDataSetEntry.setStatus("current")


class _PtpParentClockIdentity_Type(OctetString):
    """Custom type ptpParentClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_PtpParentClockIdentity_Type.__name__ = "OctetString"
_PtpParentClockIdentity_Object = MibTableColumn
ptpParentClockIdentity = _PtpParentClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 6, 1, 1, 1),
    _PtpParentClockIdentity_Type()
)
ptpParentClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpParentClockIdentity.setStatus("current")
_PtpParentPortNumber_Type = ClockPortNumber
_PtpParentPortNumber_Object = MibTableColumn
ptpParentPortNumber = _PtpParentPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 6, 1, 1, 2),
    _PtpParentPortNumber_Type()
)
ptpParentPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpParentPortNumber.setStatus("current")


class _PtpParentGMClockIdentity_Type(OctetString):
    """Custom type ptpParentGMClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_PtpParentGMClockIdentity_Type.__name__ = "OctetString"
_PtpParentGMClockIdentity_Object = MibTableColumn
ptpParentGMClockIdentity = _PtpParentGMClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 6, 1, 1, 3),
    _PtpParentGMClockIdentity_Type()
)
ptpParentGMClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpParentGMClockIdentity.setStatus("current")
_PtpParentGMClockClass_Type = ClockQualityClassType
_PtpParentGMClockClass_Object = MibTableColumn
ptpParentGMClockClass = _PtpParentGMClockClass_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 6, 1, 1, 4),
    _PtpParentGMClockClass_Type()
)
ptpParentGMClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpParentGMClockClass.setStatus("current")
_PtpParentGMClockAccuracy_Type = ClockQualityAccuracyType
_PtpParentGMClockAccuracy_Object = MibTableColumn
ptpParentGMClockAccuracy = _PtpParentGMClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 6, 1, 1, 5),
    _PtpParentGMClockAccuracy_Type()
)
ptpParentGMClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpParentGMClockAccuracy.setStatus("current")


class _PtpParentGMClockOffsetScaledLogVariance_Type(Integer32):
    """Custom type ptpParentGMClockOffsetScaledLogVariance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PtpParentGMClockOffsetScaledLogVariance_Type.__name__ = "Integer32"
_PtpParentGMClockOffsetScaledLogVariance_Object = MibTableColumn
ptpParentGMClockOffsetScaledLogVariance = _PtpParentGMClockOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 6, 1, 1, 6),
    _PtpParentGMClockOffsetScaledLogVariance_Type()
)
ptpParentGMClockOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpParentGMClockOffsetScaledLogVariance.setStatus("current")


class _PtpParentGMPriority1_Type(Integer32):
    """Custom type ptpParentGMPriority1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PtpParentGMPriority1_Type.__name__ = "Integer32"
_PtpParentGMPriority1_Object = MibTableColumn
ptpParentGMPriority1 = _PtpParentGMPriority1_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 6, 1, 1, 7),
    _PtpParentGMPriority1_Type()
)
ptpParentGMPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpParentGMPriority1.setStatus("current")


class _PtpParentGMPriority2_Type(Integer32):
    """Custom type ptpParentGMPriority2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PtpParentGMPriority2_Type.__name__ = "Integer32"
_PtpParentGMPriority2_Object = MibTableColumn
ptpParentGMPriority2 = _PtpParentGMPriority2_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 6, 1, 1, 8),
    _PtpParentGMPriority2_Type()
)
ptpParentGMPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpParentGMPriority2.setStatus("current")
_PtpTimePropertiesDataSet_ObjectIdentity = ObjectIdentity
ptpTimePropertiesDataSet = _PtpTimePropertiesDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 7)
)
_PtpTimeDataSetTable_Object = MibTable
ptpTimeDataSetTable = _PtpTimeDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 7, 1)
)
if mibBuilder.loadTexts:
    ptpTimeDataSetTable.setStatus("current")
_PtpTimeDataSetEntry_Object = MibTableRow
ptpTimeDataSetEntry = _PtpTimeDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 7, 1, 1)
)
ptpTimeDataSetEntry.setIndexNames(
    (0, "SIAE-PTP-MIB", "ptpClockDomainIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockTypeIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpTimeDataSetEntry.setStatus("current")


class _PtpTimeCurrentUTCOffset_Type(Integer32):
    """Custom type ptpTimeCurrentUTCOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PtpTimeCurrentUTCOffset_Type.__name__ = "Integer32"
_PtpTimeCurrentUTCOffset_Object = MibTableColumn
ptpTimeCurrentUTCOffset = _PtpTimeCurrentUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 7, 1, 1, 1),
    _PtpTimeCurrentUTCOffset_Type()
)
ptpTimeCurrentUTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpTimeCurrentUTCOffset.setStatus("current")
_PtpTimeCurrentUTCOffsetValid_Type = TruthValue
_PtpTimeCurrentUTCOffsetValid_Object = MibTableColumn
ptpTimeCurrentUTCOffsetValid = _PtpTimeCurrentUTCOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 7, 1, 1, 2),
    _PtpTimeCurrentUTCOffsetValid_Type()
)
ptpTimeCurrentUTCOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpTimeCurrentUTCOffsetValid.setStatus("current")
_PtpTimeLeap59_Type = TruthValue
_PtpTimeLeap59_Object = MibTableColumn
ptpTimeLeap59 = _PtpTimeLeap59_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 7, 1, 1, 3),
    _PtpTimeLeap59_Type()
)
ptpTimeLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpTimeLeap59.setStatus("current")
_PtpTimeLeap61_Type = TruthValue
_PtpTimeLeap61_Object = MibTableColumn
ptpTimeLeap61 = _PtpTimeLeap61_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 7, 1, 1, 4),
    _PtpTimeLeap61_Type()
)
ptpTimeLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpTimeLeap61.setStatus("current")
_PtpTimeTimeTraceable_Type = TruthValue
_PtpTimeTimeTraceable_Object = MibTableColumn
ptpTimeTimeTraceable = _PtpTimeTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 7, 1, 1, 5),
    _PtpTimeTimeTraceable_Type()
)
ptpTimeTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpTimeTimeTraceable.setStatus("current")
_PtpTimeFrequencyTraceable_Type = TruthValue
_PtpTimeFrequencyTraceable_Object = MibTableColumn
ptpTimeFrequencyTraceable = _PtpTimeFrequencyTraceable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 7, 1, 1, 6),
    _PtpTimeFrequencyTraceable_Type()
)
ptpTimeFrequencyTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpTimeFrequencyTraceable.setStatus("current")
_PtpTimescale_Type = TruthValue
_PtpTimescale_Object = MibTableColumn
ptpTimescale = _PtpTimescale_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 7, 1, 1, 7),
    _PtpTimescale_Type()
)
ptpTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpTimescale.setStatus("current")


class _PtpTimeTimeSource_Type(ClockTimeSourceType):
    """Custom type ptpTimeTimeSource based on ClockTimeSourceType"""
    defaultValue = 160


_PtpTimeTimeSource_Type.__name__ = "ClockTimeSourceType"
_PtpTimeTimeSource_Object = MibTableColumn
ptpTimeTimeSource = _PtpTimeTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 7, 1, 1, 8),
    _PtpTimeTimeSource_Type()
)
ptpTimeTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpTimeTimeSource.setStatus("current")
_PtpPortDataSet_ObjectIdentity = ObjectIdentity
ptpPortDataSet = _PtpPortDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8)
)
_PtpPortDataSetTable_Object = MibTable
ptpPortDataSetTable = _PtpPortDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1)
)
if mibBuilder.loadTexts:
    ptpPortDataSetTable.setStatus("current")
_PtpPortDataSetEntry_Object = MibTableRow
ptpPortDataSetEntry = _PtpPortDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1)
)
ptpPortDataSetEntry.setIndexNames(
    (0, "SIAE-PTP-MIB", "ptpClockDomainIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockTypeIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockInstanceIndex"),
    (0, "SIAE-PTP-MIB", "ptpPortIndex"),
)
if mibBuilder.loadTexts:
    ptpPortDataSetEntry.setStatus("current")
_PtpPortIndex_Type = ClockPortNumber
_PtpPortIndex_Object = MibTableColumn
ptpPortIndex = _PtpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 1),
    _PtpPortIndex_Type()
)
ptpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortIndex.setStatus("current")


class _PtpPortClockIdentity_Type(OctetString):
    """Custom type ptpPortClockIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_PtpPortClockIdentity_Type.__name__ = "OctetString"
_PtpPortClockIdentity_Object = MibTableColumn
ptpPortClockIdentity = _PtpPortClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 2),
    _PtpPortClockIdentity_Type()
)
ptpPortClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortClockIdentity.setStatus("current")
_PtpPortIfIndex_Type = InterfaceIndex
_PtpPortIfIndex_Object = MibTableColumn
ptpPortIfIndex = _PtpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 3),
    _PtpPortIfIndex_Type()
)
ptpPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpPortIfIndex.setStatus("current")


class _PtpPortStaticRole_Type(Integer32):
    """Custom type ptpPortStaticRole based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("master", 6),
          ("passive", 7),
          ("slave", 9))
    )


_PtpPortStaticRole_Type.__name__ = "Integer32"
_PtpPortStaticRole_Object = MibTableColumn
ptpPortStaticRole = _PtpPortStaticRole_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 4),
    _PtpPortStaticRole_Type()
)
ptpPortStaticRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpPortStaticRole.setStatus("current")


class _PtpPortAdminStatus_Type(Integer32):
    """Custom type ptpPortAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_PtpPortAdminStatus_Type.__name__ = "Integer32"
_PtpPortAdminStatus_Object = MibTableColumn
ptpPortAdminStatus = _PtpPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 5),
    _PtpPortAdminStatus_Type()
)
ptpPortAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpPortAdminStatus.setStatus("current")
_PtpPortState_Type = ClockPortState
_PtpPortState_Object = MibTableColumn
ptpPortState = _PtpPortState_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 6),
    _PtpPortState_Type()
)
ptpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortState.setStatus("current")


class _PtpPortMinDelayReqInterval_Type(Integer32):
    """Custom type ptpPortMinDelayReqInterval based on Integer32"""
    defaultValue = -4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, 7),
    )


_PtpPortMinDelayReqInterval_Type.__name__ = "Integer32"
_PtpPortMinDelayReqInterval_Object = MibTableColumn
ptpPortMinDelayReqInterval = _PtpPortMinDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 7),
    _PtpPortMinDelayReqInterval_Type()
)
ptpPortMinDelayReqInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpPortMinDelayReqInterval.setStatus("current")


class _PtpPortLogAnnounceInterval_Type(Integer32):
    """Custom type ptpPortLogAnnounceInterval based on Integer32"""
    defaultValue = -3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 6),
    )


_PtpPortLogAnnounceInterval_Type.__name__ = "Integer32"
_PtpPortLogAnnounceInterval_Object = MibTableColumn
ptpPortLogAnnounceInterval = _PtpPortLogAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 8),
    _PtpPortLogAnnounceInterval_Type()
)
ptpPortLogAnnounceInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpPortLogAnnounceInterval.setStatus("current")


class _PtpPortAnnounceReceiptTimeout_Type(Integer32):
    """Custom type ptpPortAnnounceReceiptTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_PtpPortAnnounceReceiptTimeout_Type.__name__ = "Integer32"
_PtpPortAnnounceReceiptTimeout_Object = MibTableColumn
ptpPortAnnounceReceiptTimeout = _PtpPortAnnounceReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 9),
    _PtpPortAnnounceReceiptTimeout_Type()
)
ptpPortAnnounceReceiptTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpPortAnnounceReceiptTimeout.setStatus("current")


class _PtpPortSyncInterval_Type(Integer32):
    """Custom type ptpPortSyncInterval based on Integer32"""
    defaultValue = -4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, 0),
    )


_PtpPortSyncInterval_Type.__name__ = "Integer32"
_PtpPortSyncInterval_Object = MibTableColumn
ptpPortSyncInterval = _PtpPortSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 10),
    _PtpPortSyncInterval_Type()
)
ptpPortSyncInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpPortSyncInterval.setStatus("current")


class _PtpPortDelayMechanism_Type(ClockMechanismType):
    """Custom type ptpPortDelayMechanism based on ClockMechanismType"""
    defaultValue = 1


_PtpPortDelayMechanism_Type.__name__ = "ClockMechanismType"
_PtpPortDelayMechanism_Object = MibTableColumn
ptpPortDelayMechanism = _PtpPortDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 11),
    _PtpPortDelayMechanism_Type()
)
ptpPortDelayMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortDelayMechanism.setStatus("current")


class _PtpPortVersionNumber_Type(Integer32):
    """Custom type ptpPortVersionNumber based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_PtpPortVersionNumber_Type.__name__ = "Integer32"
_PtpPortVersionNumber_Object = MibTableColumn
ptpPortVersionNumber = _PtpPortVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 12),
    _PtpPortVersionNumber_Type()
)
ptpPortVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortVersionNumber.setStatus("current")


class _PtpPortNotSlave_Type(TruthValue):
    """Custom type ptpPortNotSlave based on TruthValue"""
    defaultValue = 1


_PtpPortNotSlave_Type.__name__ = "TruthValue"
_PtpPortNotSlave_Object = MibTableColumn
ptpPortNotSlave = _PtpPortNotSlave_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 13),
    _PtpPortNotSlave_Type()
)
ptpPortNotSlave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpPortNotSlave.setStatus("current")


class _PtpPortLocalPriority_Type(Integer32):
    """Custom type ptpPortLocalPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PtpPortLocalPriority_Type.__name__ = "Integer32"
_PtpPortLocalPriority_Object = MibTableColumn
ptpPortLocalPriority = _PtpPortLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 14),
    _PtpPortLocalPriority_Type()
)
ptpPortLocalPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpPortLocalPriority.setStatus("current")


class _PtpPortDestMacAddress_Type(Integer32):
    """Custom type ptpPortDestMacAddress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwardable", 1),
          ("nonForwardable", 2))
    )


_PtpPortDestMacAddress_Type.__name__ = "Integer32"
_PtpPortDestMacAddress_Object = MibTableColumn
ptpPortDestMacAddress = _PtpPortDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 15),
    _PtpPortDestMacAddress_Type()
)
ptpPortDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpPortDestMacAddress.setStatus("current")


class _PtpPortTxAsymmetryCompensation_Type(Integer32):
    """Custom type ptpPortTxAsymmetryCompensation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_PtpPortTxAsymmetryCompensation_Type.__name__ = "Integer32"
_PtpPortTxAsymmetryCompensation_Object = MibTableColumn
ptpPortTxAsymmetryCompensation = _PtpPortTxAsymmetryCompensation_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 16),
    _PtpPortTxAsymmetryCompensation_Type()
)
ptpPortTxAsymmetryCompensation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpPortTxAsymmetryCompensation.setStatus("current")


class _PtpPortRxAsymmetryCompensation_Type(Integer32):
    """Custom type ptpPortRxAsymmetryCompensation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_PtpPortRxAsymmetryCompensation_Type.__name__ = "Integer32"
_PtpPortRxAsymmetryCompensation_Object = MibTableColumn
ptpPortRxAsymmetryCompensation = _PtpPortRxAsymmetryCompensation_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 17),
    _PtpPortRxAsymmetryCompensation_Type()
)
ptpPortRxAsymmetryCompensation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpPortRxAsymmetryCompensation.setStatus("current")
_PtpPortRowStatus_Type = RowStatus
_PtpPortRowStatus_Object = MibTableColumn
ptpPortRowStatus = _PtpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 1, 1, 18),
    _PtpPortRowStatus_Type()
)
ptpPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ptpPortRowStatus.setStatus("current")
_PtpPortAlarmTable_Object = MibTable
ptpPortAlarmTable = _PtpPortAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 2)
)
if mibBuilder.loadTexts:
    ptpPortAlarmTable.setStatus("current")
_PtpPortAlarmEntry_Object = MibTableRow
ptpPortAlarmEntry = _PtpPortAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 2, 1)
)
ptpPortAlarmEntry.setIndexNames(
    (0, "SIAE-PTP-MIB", "ptpClockDomainIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockTypeIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockInstanceIndex"),
    (0, "SIAE-PTP-MIB", "ptpPortIndex"),
)
if mibBuilder.loadTexts:
    ptpPortAlarmEntry.setStatus("current")
_PtpPortFaultyAlarm_Type = AlarmStatus
_PtpPortFaultyAlarm_Object = MibTableColumn
ptpPortFaultyAlarm = _PtpPortFaultyAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 2, 1, 1),
    _PtpPortFaultyAlarm_Type()
)
ptpPortFaultyAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortFaultyAlarm.setStatus("current")
_PtpPortInitializingAlarm_Type = AlarmStatus
_PtpPortInitializingAlarm_Object = MibTableColumn
ptpPortInitializingAlarm = _PtpPortInitializingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 2, 1, 2),
    _PtpPortInitializingAlarm_Type()
)
ptpPortInitializingAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortInitializingAlarm.setStatus("current")
_PtpPortUncalibratedAlarm_Type = AlarmStatus
_PtpPortUncalibratedAlarm_Object = MibTableColumn
ptpPortUncalibratedAlarm = _PtpPortUncalibratedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 2, 1, 3),
    _PtpPortUncalibratedAlarm_Type()
)
ptpPortUncalibratedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortUncalibratedAlarm.setStatus("current")
_PtpPortListeningAlarm_Type = AlarmStatus
_PtpPortListeningAlarm_Object = MibTableColumn
ptpPortListeningAlarm = _PtpPortListeningAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 2, 1, 4),
    _PtpPortListeningAlarm_Type()
)
ptpPortListeningAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortListeningAlarm.setStatus("current")
_PtpPortActiveStatus_Type = AlarmStatus
_PtpPortActiveStatus_Object = MibTableColumn
ptpPortActiveStatus = _PtpPortActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 2, 1, 5),
    _PtpPortActiveStatus_Type()
)
ptpPortActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortActiveStatus.setStatus("current")
_PtpPortRadioAlarmTable_Object = MibTable
ptpPortRadioAlarmTable = _PtpPortRadioAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 3)
)
if mibBuilder.loadTexts:
    ptpPortRadioAlarmTable.setStatus("current")
_PtpPortRadioAlarmEntry_Object = MibTableRow
ptpPortRadioAlarmEntry = _PtpPortRadioAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 3, 1)
)
ptpPortRadioAlarmEntry.setIndexNames(
    (0, "SIAE-PTP-MIB", "ptpClockDomainIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockTypeIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockInstanceIndex"),
    (0, "SIAE-PTP-MIB", "ptpPortIndex"),
)
if mibBuilder.loadTexts:
    ptpPortRadioAlarmEntry.setStatus("current")
_PtpPortRadioCapacityAlarm_Type = AlarmStatus
_PtpPortRadioCapacityAlarm_Object = MibTableColumn
ptpPortRadioCapacityAlarm = _PtpPortRadioCapacityAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 3, 1, 1),
    _PtpPortRadioCapacityAlarm_Type()
)
ptpPortRadioCapacityAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortRadioCapacityAlarm.setStatus("current")


class _PtpPortFaultyAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type ptpPortFaultyAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PtpPortFaultyAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PtpPortFaultyAlarmSeverityCode_Object = MibScalar
ptpPortFaultyAlarmSeverityCode = _PtpPortFaultyAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 4),
    _PtpPortFaultyAlarmSeverityCode_Type()
)
ptpPortFaultyAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpPortFaultyAlarmSeverityCode.setStatus("current")


class _PtpPortInitializingAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type ptpPortInitializingAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_PtpPortInitializingAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PtpPortInitializingAlarmSeverityCode_Object = MibScalar
ptpPortInitializingAlarmSeverityCode = _PtpPortInitializingAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 5),
    _PtpPortInitializingAlarmSeverityCode_Type()
)
ptpPortInitializingAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpPortInitializingAlarmSeverityCode.setStatus("current")


class _PtpPortUncalibratedAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type ptpPortUncalibratedAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_PtpPortUncalibratedAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PtpPortUncalibratedAlarmSeverityCode_Object = MibScalar
ptpPortUncalibratedAlarmSeverityCode = _PtpPortUncalibratedAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 6),
    _PtpPortUncalibratedAlarmSeverityCode_Type()
)
ptpPortUncalibratedAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpPortUncalibratedAlarmSeverityCode.setStatus("current")


class _PtpPortListeningAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type ptpPortListeningAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_PtpPortListeningAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PtpPortListeningAlarmSeverityCode_Object = MibScalar
ptpPortListeningAlarmSeverityCode = _PtpPortListeningAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 7),
    _PtpPortListeningAlarmSeverityCode_Type()
)
ptpPortListeningAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpPortListeningAlarmSeverityCode.setStatus("current")


class _PtpPortActiveStatusSeverityCode_Type(AlarmSeverityCode):
    """Custom type ptpPortActiveStatusSeverityCode based on AlarmSeverityCode"""
    defaultValue = 2


_PtpPortActiveStatusSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PtpPortActiveStatusSeverityCode_Object = MibScalar
ptpPortActiveStatusSeverityCode = _PtpPortActiveStatusSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 8),
    _PtpPortActiveStatusSeverityCode_Type()
)
ptpPortActiveStatusSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpPortActiveStatusSeverityCode.setStatus("current")


class _PtpPortRadioCapacityAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type ptpPortRadioCapacityAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_PtpPortRadioCapacityAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_PtpPortRadioCapacityAlarmSeverityCode_Object = MibScalar
ptpPortRadioCapacityAlarmSeverityCode = _PtpPortRadioCapacityAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 8, 9),
    _PtpPortRadioCapacityAlarmSeverityCode_Type()
)
ptpPortRadioCapacityAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpPortRadioCapacityAlarmSeverityCode.setStatus("current")
_PtpClockPPSDataSet_ObjectIdentity = ObjectIdentity
ptpClockPPSDataSet = _PtpClockPPSDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9)
)
_PtpClockPPSDataSetTable_Object = MibTable
ptpClockPPSDataSetTable = _PtpClockPPSDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9, 1)
)
if mibBuilder.loadTexts:
    ptpClockPPSDataSetTable.setStatus("current")
_PtpClockPPSDataSetEntry_Object = MibTableRow
ptpClockPPSDataSetEntry = _PtpClockPPSDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9, 1, 1)
)
ptpClockPPSDataSetEntry.setIndexNames(
    (0, "SIAE-PTP-MIB", "ptpClockDomainIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockTypeIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockInstanceIndex"),
    (0, "SIAE-PTP-MIB", "ptpClockPPSInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpClockPPSDataSetEntry.setStatus("current")


class _PtpClockPPSInstanceIndex_Type(ClockPPSInstanceType):
    """Custom type ptpClockPPSInstanceIndex based on ClockPPSInstanceType"""
    defaultValue = 0


_PtpClockPPSInstanceIndex_Type.__name__ = "ClockPPSInstanceType"
_PtpClockPPSInstanceIndex_Object = MibTableColumn
ptpClockPPSInstanceIndex = _PtpClockPPSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9, 1, 1, 1),
    _PtpClockPPSInstanceIndex_Type()
)
ptpClockPPSInstanceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpClockPPSInstanceIndex.setStatus("current")


class _PtpClockPPSInstanceCapability_Type(Unsigned32):
    """Custom type ptpClockPPSInstanceCapability based on Unsigned32"""
    defaultValue = 0


_PtpClockPPSInstanceCapability_Type.__name__ = "Unsigned32"
_PtpClockPPSInstanceCapability_Object = MibTableColumn
ptpClockPPSInstanceCapability = _PtpClockPPSInstanceCapability_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9, 1, 1, 2),
    _PtpClockPPSInstanceCapability_Type()
)
ptpClockPPSInstanceCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPPSInstanceCapability.setStatus("current")


class _PtpClockPPSDirection_Type(Integer32):
    """Custom type ptpClockPPSDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_PtpClockPPSDirection_Type.__name__ = "Integer32"
_PtpClockPPSDirection_Object = MibTableColumn
ptpClockPPSDirection = _PtpClockPPSDirection_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9, 1, 1, 3),
    _PtpClockPPSDirection_Type()
)
ptpClockPPSDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpClockPPSDirection.setStatus("current")


class _PtpClockPPSLabel_Type(DisplayString):
    """Custom type ptpClockPPSLabel based on DisplayString"""
    defaultValue = OctetString("PPS")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PtpClockPPSLabel_Type.__name__ = "DisplayString"
_PtpClockPPSLabel_Object = MibTableColumn
ptpClockPPSLabel = _PtpClockPPSLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9, 1, 1, 4),
    _PtpClockPPSLabel_Type()
)
ptpClockPPSLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPPSLabel.setStatus("current")


class _PtpClockPPSAdminStatus_Type(Integer32):
    """Custom type ptpClockPPSAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_PtpClockPPSAdminStatus_Type.__name__ = "Integer32"
_PtpClockPPSAdminStatus_Object = MibTableColumn
ptpClockPPSAdminStatus = _PtpClockPPSAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9, 1, 1, 5),
    _PtpClockPPSAdminStatus_Type()
)
ptpClockPPSAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpClockPPSAdminStatus.setStatus("current")
_PtpClockPPSOffsetEnabled_Type = TruthValue
_PtpClockPPSOffsetEnabled_Object = MibTableColumn
ptpClockPPSOffsetEnabled = _PtpClockPPSOffsetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9, 1, 1, 6),
    _PtpClockPPSOffsetEnabled_Type()
)
ptpClockPPSOffsetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpClockPPSOffsetEnabled.setStatus("current")
_PtpClockPPSOffsetValue_Type = Integer32
_PtpClockPPSOffsetValue_Object = MibTableColumn
ptpClockPPSOffsetValue = _PtpClockPPSOffsetValue_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9, 1, 1, 7),
    _PtpClockPPSOffsetValue_Type()
)
ptpClockPPSOffsetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpClockPPSOffsetValue.setStatus("current")


class _PtpClockToDLabel_Type(DisplayString):
    """Custom type ptpClockToDLabel based on DisplayString"""
    defaultValue = OctetString("ToD")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PtpClockToDLabel_Type.__name__ = "DisplayString"
_PtpClockToDLabel_Object = MibTableColumn
ptpClockToDLabel = _PtpClockToDLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9, 1, 1, 8),
    _PtpClockToDLabel_Type()
)
ptpClockToDLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockToDLabel.setStatus("current")


class _PtpClockToDAdminStatus_Type(Integer32):
    """Custom type ptpClockToDAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_PtpClockToDAdminStatus_Type.__name__ = "Integer32"
_PtpClockToDAdminStatus_Object = MibTableColumn
ptpClockToDAdminStatus = _PtpClockToDAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9, 1, 1, 9),
    _PtpClockToDAdminStatus_Type()
)
ptpClockToDAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpClockToDAdminStatus.setStatus("current")


class _PtpClockToDDelay_Type(Unsigned32):
    """Custom type ptpClockToDDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_PtpClockToDDelay_Type.__name__ = "Unsigned32"
_PtpClockToDDelay_Object = MibTableColumn
ptpClockToDDelay = _PtpClockToDDelay_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9, 1, 1, 10),
    _PtpClockToDDelay_Type()
)
ptpClockToDDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpClockToDDelay.setStatus("current")


class _PtpClockToDBaudrate_Type(Unsigned32):
    """Custom type ptpClockToDBaudrate based on Unsigned32"""
    defaultValue = 9600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 300),
        ValueRangeConstraint(600, 600),
        ValueRangeConstraint(1200, 1200),
        ValueRangeConstraint(1800, 1800),
        ValueRangeConstraint(2400, 2400),
        ValueRangeConstraint(4800, 4800),
        ValueRangeConstraint(9600, 9600),
        ValueRangeConstraint(19200, 19200),
        ValueRangeConstraint(38400, 38400),
        ValueRangeConstraint(57600, 57600),
        ValueRangeConstraint(115200, 115200),
        ValueRangeConstraint(230400, 230400),
    )


_PtpClockToDBaudrate_Type.__name__ = "Unsigned32"
_PtpClockToDBaudrate_Object = MibTableColumn
ptpClockToDBaudrate = _PtpClockToDBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9, 1, 1, 11),
    _PtpClockToDBaudrate_Type()
)
ptpClockToDBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpClockToDBaudrate.setStatus("current")


class _PtpClockToDFormat_Type(PtpClockToDFormatType):
    """Custom type ptpClockToDFormat based on PtpClockToDFormatType"""
    defaultValue = 1


_PtpClockToDFormat_Type.__name__ = "PtpClockToDFormatType"
_PtpClockToDFormat_Object = MibTableColumn
ptpClockToDFormat = _PtpClockToDFormat_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 9, 1, 1, 12),
    _PtpClockToDFormat_Type()
)
ptpClockToDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpClockToDFormat.setStatus("current")
_PtpRadioAsymmetryDataSet_ObjectIdentity = ObjectIdentity
ptpRadioAsymmetryDataSet = _PtpRadioAsymmetryDataSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 10)
)
_PtpRadioAsymmetryDataSetTable_Object = MibTable
ptpRadioAsymmetryDataSetTable = _PtpRadioAsymmetryDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 10, 1)
)
if mibBuilder.loadTexts:
    ptpRadioAsymmetryDataSetTable.setStatus("current")
_PtpRadioAsymmetryDataSetEntry_Object = MibTableRow
ptpRadioAsymmetryDataSetEntry = _PtpRadioAsymmetryDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 10, 1, 1)
)
ptpRadioAsymmetryDataSetEntry.setIndexNames(
    (0, "SIAE-PTP-MIB", "ptpRadioBrIndex"),
)
if mibBuilder.loadTexts:
    ptpRadioAsymmetryDataSetEntry.setStatus("current")
_PtpRadioBrIndex_Type = Integer32
_PtpRadioBrIndex_Object = MibTableColumn
ptpRadioBrIndex = _PtpRadioBrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 10, 1, 1, 1),
    _PtpRadioBrIndex_Type()
)
ptpRadioBrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpRadioBrIndex.setStatus("current")


class _PtpRadioOffset_Type(Integer32):
    """Custom type ptpRadioOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_PtpRadioOffset_Type.__name__ = "Integer32"
_PtpRadioOffset_Object = MibTableColumn
ptpRadioOffset = _PtpRadioOffset_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 100, 10, 1, 1, 2),
    _PtpRadioOffset_Type()
)
ptpRadioOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpRadioOffset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-PTP-MIB",
    **{"ClockDomainType": ClockDomainType,
       "ClockProfileType": ClockProfileType,
       "ClockQualityAccuracyType": ClockQualityAccuracyType,
       "ClockQualityClassType": ClockQualityClassType,
       "ClockStateType": ClockStateType,
       "ClockTimeSourceType": ClockTimeSourceType,
       "ClockInstanceType": ClockInstanceType,
       "ClockPPSInstanceType": ClockPPSInstanceType,
       "ClockPortNumber": ClockPortNumber,
       "ClockPortState": ClockPortState,
       "ClockMechanismType": ClockMechanismType,
       "ClockTimeInterval": ClockTimeInterval,
       "ClockType": ClockType,
       "PtpClockToDFormatType": PtpClockToDFormatType,
       "ptp": ptp,
       "ptpMibVersion": ptpMibVersion,
       "ptpProfileDataSet": ptpProfileDataSet,
       "ptpSystemProfile": ptpSystemProfile,
       "ptpProfileName": ptpProfileName,
       "ptpProfilePrimaryVersion": ptpProfilePrimaryVersion,
       "ptpProfileRevisionNumber": ptpProfileRevisionNumber,
       "ptpProfileIdentifier": ptpProfileIdentifier,
       "ptpSpecificDataSet": ptpSpecificDataSet,
       "ptpSpecificDataSetTable": ptpSpecificDataSetTable,
       "ptpSpecificDataSetEntry": ptpSpecificDataSetEntry,
       "ptpAdminStatus": ptpAdminStatus,
       "ptpStaticPortRole": ptpStaticPortRole,
       "ptpClockState": ptpClockState,
       "ptpCompliance": ptpCompliance,
       "ptpSpecificAlarmTable": ptpSpecificAlarmTable,
       "ptpSpecificAlarmEntry": ptpSpecificAlarmEntry,
       "ptpFreeRunningAlarm": ptpFreeRunningAlarm,
       "ptpHoldoverInSpecAlarm": ptpHoldoverInSpecAlarm,
       "ptpHoldoverOutOfSpecAlarm": ptpHoldoverOutOfSpecAlarm,
       "ptpFreeRunningAlarmSeverityCode": ptpFreeRunningAlarmSeverityCode,
       "ptpHoldoverInSpecAlarmSeverityCode": ptpHoldoverInSpecAlarmSeverityCode,
       "ptpHoldoverOutOfSpecAlarmSeverityCode": ptpHoldoverOutOfSpecAlarmSeverityCode,
       "ptpDefaultDataSet": ptpDefaultDataSet,
       "ptpClockDataSetTable": ptpClockDataSetTable,
       "ptpClockDataSetEntry": ptpClockDataSetEntry,
       "ptpClockDomainIndex": ptpClockDomainIndex,
       "ptpClockTypeIndex": ptpClockTypeIndex,
       "ptpClockInstanceIndex": ptpClockInstanceIndex,
       "ptpClockIdentity": ptpClockIdentity,
       "ptpClockTwoStepFlag": ptpClockTwoStepFlag,
       "ptpClockNumberPorts": ptpClockNumberPorts,
       "ptpClockClass": ptpClockClass,
       "ptpClockAccuracy": ptpClockAccuracy,
       "ptpClockOffsetScaledLogVariance": ptpClockOffsetScaledLogVariance,
       "ptpClockPriority1": ptpClockPriority1,
       "ptpClockPriority2": ptpClockPriority2,
       "ptpClockSlaveOnly": ptpClockSlaveOnly,
       "ptpClockLocalPriority": ptpClockLocalPriority,
       "ptpClockRowStatus": ptpClockRowStatus,
       "ptpCurrentDataSet": ptpCurrentDataSet,
       "ptpCurrentDataSetTable": ptpCurrentDataSetTable,
       "ptpCurrentDataSetEntry": ptpCurrentDataSetEntry,
       "ptpCurrentStepsRemoved": ptpCurrentStepsRemoved,
       "ptpCurrentOffsetFromMaster": ptpCurrentOffsetFromMaster,
       "ptpCurrentMeanPathDelay": ptpCurrentMeanPathDelay,
       "ptpParentDataSet": ptpParentDataSet,
       "ptpParentDataSetTable": ptpParentDataSetTable,
       "ptpParentDataSetEntry": ptpParentDataSetEntry,
       "ptpParentClockIdentity": ptpParentClockIdentity,
       "ptpParentPortNumber": ptpParentPortNumber,
       "ptpParentGMClockIdentity": ptpParentGMClockIdentity,
       "ptpParentGMClockClass": ptpParentGMClockClass,
       "ptpParentGMClockAccuracy": ptpParentGMClockAccuracy,
       "ptpParentGMClockOffsetScaledLogVariance": ptpParentGMClockOffsetScaledLogVariance,
       "ptpParentGMPriority1": ptpParentGMPriority1,
       "ptpParentGMPriority2": ptpParentGMPriority2,
       "ptpTimePropertiesDataSet": ptpTimePropertiesDataSet,
       "ptpTimeDataSetTable": ptpTimeDataSetTable,
       "ptpTimeDataSetEntry": ptpTimeDataSetEntry,
       "ptpTimeCurrentUTCOffset": ptpTimeCurrentUTCOffset,
       "ptpTimeCurrentUTCOffsetValid": ptpTimeCurrentUTCOffsetValid,
       "ptpTimeLeap59": ptpTimeLeap59,
       "ptpTimeLeap61": ptpTimeLeap61,
       "ptpTimeTimeTraceable": ptpTimeTimeTraceable,
       "ptpTimeFrequencyTraceable": ptpTimeFrequencyTraceable,
       "ptpTimescale": ptpTimescale,
       "ptpTimeTimeSource": ptpTimeTimeSource,
       "ptpPortDataSet": ptpPortDataSet,
       "ptpPortDataSetTable": ptpPortDataSetTable,
       "ptpPortDataSetEntry": ptpPortDataSetEntry,
       "ptpPortIndex": ptpPortIndex,
       "ptpPortClockIdentity": ptpPortClockIdentity,
       "ptpPortIfIndex": ptpPortIfIndex,
       "ptpPortStaticRole": ptpPortStaticRole,
       "ptpPortAdminStatus": ptpPortAdminStatus,
       "ptpPortState": ptpPortState,
       "ptpPortMinDelayReqInterval": ptpPortMinDelayReqInterval,
       "ptpPortLogAnnounceInterval": ptpPortLogAnnounceInterval,
       "ptpPortAnnounceReceiptTimeout": ptpPortAnnounceReceiptTimeout,
       "ptpPortSyncInterval": ptpPortSyncInterval,
       "ptpPortDelayMechanism": ptpPortDelayMechanism,
       "ptpPortVersionNumber": ptpPortVersionNumber,
       "ptpPortNotSlave": ptpPortNotSlave,
       "ptpPortLocalPriority": ptpPortLocalPriority,
       "ptpPortDestMacAddress": ptpPortDestMacAddress,
       "ptpPortTxAsymmetryCompensation": ptpPortTxAsymmetryCompensation,
       "ptpPortRxAsymmetryCompensation": ptpPortRxAsymmetryCompensation,
       "ptpPortRowStatus": ptpPortRowStatus,
       "ptpPortAlarmTable": ptpPortAlarmTable,
       "ptpPortAlarmEntry": ptpPortAlarmEntry,
       "ptpPortFaultyAlarm": ptpPortFaultyAlarm,
       "ptpPortInitializingAlarm": ptpPortInitializingAlarm,
       "ptpPortUncalibratedAlarm": ptpPortUncalibratedAlarm,
       "ptpPortListeningAlarm": ptpPortListeningAlarm,
       "ptpPortActiveStatus": ptpPortActiveStatus,
       "ptpPortRadioAlarmTable": ptpPortRadioAlarmTable,
       "ptpPortRadioAlarmEntry": ptpPortRadioAlarmEntry,
       "ptpPortRadioCapacityAlarm": ptpPortRadioCapacityAlarm,
       "ptpPortFaultyAlarmSeverityCode": ptpPortFaultyAlarmSeverityCode,
       "ptpPortInitializingAlarmSeverityCode": ptpPortInitializingAlarmSeverityCode,
       "ptpPortUncalibratedAlarmSeverityCode": ptpPortUncalibratedAlarmSeverityCode,
       "ptpPortListeningAlarmSeverityCode": ptpPortListeningAlarmSeverityCode,
       "ptpPortActiveStatusSeverityCode": ptpPortActiveStatusSeverityCode,
       "ptpPortRadioCapacityAlarmSeverityCode": ptpPortRadioCapacityAlarmSeverityCode,
       "ptpClockPPSDataSet": ptpClockPPSDataSet,
       "ptpClockPPSDataSetTable": ptpClockPPSDataSetTable,
       "ptpClockPPSDataSetEntry": ptpClockPPSDataSetEntry,
       "ptpClockPPSInstanceIndex": ptpClockPPSInstanceIndex,
       "ptpClockPPSInstanceCapability": ptpClockPPSInstanceCapability,
       "ptpClockPPSDirection": ptpClockPPSDirection,
       "ptpClockPPSLabel": ptpClockPPSLabel,
       "ptpClockPPSAdminStatus": ptpClockPPSAdminStatus,
       "ptpClockPPSOffsetEnabled": ptpClockPPSOffsetEnabled,
       "ptpClockPPSOffsetValue": ptpClockPPSOffsetValue,
       "ptpClockToDLabel": ptpClockToDLabel,
       "ptpClockToDAdminStatus": ptpClockToDAdminStatus,
       "ptpClockToDDelay": ptpClockToDDelay,
       "ptpClockToDBaudrate": ptpClockToDBaudrate,
       "ptpClockToDFormat": ptpClockToDFormat,
       "ptpRadioAsymmetryDataSet": ptpRadioAsymmetryDataSet,
       "ptpRadioAsymmetryDataSetTable": ptpRadioAsymmetryDataSetTable,
       "ptpRadioAsymmetryDataSetEntry": ptpRadioAsymmetryDataSetEntry,
       "ptpRadioBrIndex": ptpRadioBrIndex,
       "ptpRadioOffset": ptpRadioOffset}
)
