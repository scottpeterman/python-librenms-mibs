# SNMP MIB module (DLINKSW-TIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-TIME-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:02 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwTimeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 10)
)
if mibBuilder.loadTexts:
    dlinkSwTimeMIB.setRevisions(
        ("2013-03-19 00:00",
         "2013-08-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DlinkTimeSummerTimeValue(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(6, 6),
    )



# MIB Managed Objects in the order of their OIDs

_DTimeMIBNotifications_ObjectIdentity = ObjectIdentity
dTimeMIBNotifications = _DTimeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 0)
)
_DTimeMIBObjects_ObjectIdentity = ObjectIdentity
dTimeMIBObjects = _DTimeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1)
)
_DTimeGeneral_ObjectIdentity = ObjectIdentity
dTimeGeneral = _DTimeGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 1)
)
_DTimeSntpEnabled_Type = TruthValue
_DTimeSntpEnabled_Object = MibScalar
dTimeSntpEnabled = _DTimeSntpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 1, 1),
    _DTimeSntpEnabled_Type()
)
dTimeSntpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTimeSntpEnabled.setStatus("current")
_DTimeSntpBcastClientEnabled_Type = TruthValue
_DTimeSntpBcastClientEnabled_Object = MibScalar
dTimeSntpBcastClientEnabled = _DTimeSntpBcastClientEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 1, 2),
    _DTimeSntpBcastClientEnabled_Type()
)
dTimeSntpBcastClientEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTimeSntpBcastClientEnabled.setStatus("current")


class _DTimeSntpPollInterval_Type(Unsigned32):
    """Custom type dTimeSntpPollInterval based on Unsigned32"""
    defaultValue = 720

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 99999),
    )


_DTimeSntpPollInterval_Type.__name__ = "Unsigned32"
_DTimeSntpPollInterval_Object = MibScalar
dTimeSntpPollInterval = _DTimeSntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 1, 3),
    _DTimeSntpPollInterval_Type()
)
dTimeSntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTimeSntpPollInterval.setStatus("current")
_DTimeSntpSourceIfIndex_Type = InterfaceIndexOrZero
_DTimeSntpSourceIfIndex_Object = MibScalar
dTimeSntpSourceIfIndex = _DTimeSntpSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 1, 4),
    _DTimeSntpSourceIfIndex_Type()
)
dTimeSntpSourceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTimeSntpSourceIfIndex.setStatus("current")
_DTimeClock_ObjectIdentity = ObjectIdentity
dTimeClock = _DTimeClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 2)
)
_DTimeManagedClock_Type = DateAndTime
_DTimeManagedClock_Object = MibScalar
dTimeManagedClock = _DTimeManagedClock_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 2, 1),
    _DTimeManagedClock_Type()
)
dTimeManagedClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTimeManagedClock.setStatus("current")


class _DTimeCurrentTimeSource_Type(Integer32):
    """Custom type dTimeCurrentTimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sntp", 1),
          ("noTimeSource", 2))
    )


_DTimeCurrentTimeSource_Type.__name__ = "Integer32"
_DTimeCurrentTimeSource_Object = MibScalar
dTimeCurrentTimeSource = _DTimeCurrentTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 2, 2),
    _DTimeCurrentTimeSource_Type()
)
dTimeCurrentTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTimeCurrentTimeSource.setStatus("current")
_DTimeCurrentTime_Type = DateAndTime
_DTimeCurrentTime_Object = MibScalar
dTimeCurrentTime = _DTimeCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 2, 3),
    _DTimeCurrentTime_Type()
)
dTimeCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTimeCurrentTime.setStatus("current")
_DTimeSummerTime_ObjectIdentity = ObjectIdentity
dTimeSummerTime = _DTimeSummerTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 2, 5)
)


class _DTimeSummerTimeAutoSwitchMode_Type(Integer32):
    """Custom type dTimeSummerTimeAutoSwitchMode based on Integer32"""
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
        *(("disable", 1),
          ("recurring", 2),
          ("date", 3))
    )


_DTimeSummerTimeAutoSwitchMode_Type.__name__ = "Integer32"
_DTimeSummerTimeAutoSwitchMode_Object = MibScalar
dTimeSummerTimeAutoSwitchMode = _DTimeSummerTimeAutoSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 2, 5, 1),
    _DTimeSummerTimeAutoSwitchMode_Type()
)
dTimeSummerTimeAutoSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTimeSummerTimeAutoSwitchMode.setStatus("current")
_DTimeSummerTimeStart_Type = DlinkTimeSummerTimeValue
_DTimeSummerTimeStart_Object = MibScalar
dTimeSummerTimeStart = _DTimeSummerTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 2, 5, 2),
    _DTimeSummerTimeStart_Type()
)
dTimeSummerTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTimeSummerTimeStart.setStatus("current")
_DTimeSummerTimeEnd_Type = DlinkTimeSummerTimeValue
_DTimeSummerTimeEnd_Object = MibScalar
dTimeSummerTimeEnd = _DTimeSummerTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 2, 5, 3),
    _DTimeSummerTimeEnd_Type()
)
dTimeSummerTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTimeSummerTimeEnd.setStatus("current")


class _DTimeSummerTimeOffset_Type(Integer32):
    """Custom type dTimeSummerTimeOffset based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(120, 120),
    )


_DTimeSummerTimeOffset_Type.__name__ = "Integer32"
_DTimeSummerTimeOffset_Object = MibScalar
dTimeSummerTimeOffset = _DTimeSummerTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 2, 5, 4),
    _DTimeSummerTimeOffset_Type()
)
dTimeSummerTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTimeSummerTimeOffset.setStatus("current")
if mibBuilder.loadTexts:
    dTimeSummerTimeOffset.setUnits("Minutes")
_DTimeServer_ObjectIdentity = ObjectIdentity
dTimeServer = _DTimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 3)
)
_DTimeSntpServerTableNum_Type = Unsigned32
_DTimeSntpServerTableNum_Object = MibScalar
dTimeSntpServerTableNum = _DTimeSntpServerTableNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 3, 1),
    _DTimeSntpServerTableNum_Type()
)
dTimeSntpServerTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTimeSntpServerTableNum.setStatus("current")
_DTimeSntpServerTable_Object = MibTable
dTimeSntpServerTable = _DTimeSntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dTimeSntpServerTable.setStatus("current")
_DTimeSntpServerEntry_Object = MibTableRow
dTimeSntpServerEntry = _DTimeSntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 3, 2, 1)
)
dTimeSntpServerEntry.setIndexNames(
    (0, "DLINKSW-TIME-MIB", "dTimeSntpServerAddrType"),
    (0, "DLINKSW-TIME-MIB", "dTimeSntpServerAddr"),
    (0, "DLINKSW-TIME-MIB", "dTimeSntpServerVrfName"),
)
if mibBuilder.loadTexts:
    dTimeSntpServerEntry.setStatus("current")
_DTimeSntpServerAddrType_Type = InetAddressType
_DTimeSntpServerAddrType_Object = MibTableColumn
dTimeSntpServerAddrType = _DTimeSntpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 3, 2, 1, 1),
    _DTimeSntpServerAddrType_Type()
)
dTimeSntpServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dTimeSntpServerAddrType.setStatus("current")
_DTimeSntpServerAddr_Type = InetAddress
_DTimeSntpServerAddr_Object = MibTableColumn
dTimeSntpServerAddr = _DTimeSntpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 3, 2, 1, 2),
    _DTimeSntpServerAddr_Type()
)
dTimeSntpServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dTimeSntpServerAddr.setStatus("current")
_DTimeSntpServerVrfName_Type = DisplayString
_DTimeSntpServerVrfName_Object = MibTableColumn
dTimeSntpServerVrfName = _DTimeSntpServerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 3, 2, 1, 3),
    _DTimeSntpServerVrfName_Type()
)
dTimeSntpServerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dTimeSntpServerVrfName.setStatus("current")
_DTimeSntpServerRowStatus_Type = RowStatus
_DTimeSntpServerRowStatus_Object = MibTableColumn
dTimeSntpServerRowStatus = _DTimeSntpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 3, 2, 1, 4),
    _DTimeSntpServerRowStatus_Type()
)
dTimeSntpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dTimeSntpServerRowStatus.setStatus("current")
_DTimeSntpServerVersion_Type = Unsigned32
_DTimeSntpServerVersion_Object = MibTableColumn
dTimeSntpServerVersion = _DTimeSntpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 3, 2, 1, 5),
    _DTimeSntpServerVersion_Type()
)
dTimeSntpServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTimeSntpServerVersion.setStatus("current")
_DTimeSntpServerLastReceive_Type = Unsigned32
_DTimeSntpServerLastReceive_Object = MibTableColumn
dTimeSntpServerLastReceive = _DTimeSntpServerLastReceive_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 3, 2, 1, 6),
    _DTimeSntpServerLastReceive_Type()
)
dTimeSntpServerLastReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTimeSntpServerLastReceive.setStatus("current")
if mibBuilder.loadTexts:
    dTimeSntpServerLastReceive.setUnits("seconds")
_DTimeSntpServerSynced_Type = TruthValue
_DTimeSntpServerSynced_Object = MibTableColumn
dTimeSntpServerSynced = _DTimeSntpServerSynced_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 3, 2, 1, 7),
    _DTimeSntpServerSynced_Type()
)
dTimeSntpServerSynced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTimeSntpServerSynced.setStatus("current")
_DTimeSntpServerBcast_Type = TruthValue
_DTimeSntpServerBcast_Object = MibTableColumn
dTimeSntpServerBcast = _DTimeSntpServerBcast_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 1, 3, 2, 1, 8),
    _DTimeSntpServerBcast_Type()
)
dTimeSntpServerBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTimeSntpServerBcast.setStatus("current")
_DTimeMIBConformance_ObjectIdentity = ObjectIdentity
dTimeMIBConformance = _DTimeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 2)
)
_DTimeCompliances_ObjectIdentity = ObjectIdentity
dTimeCompliances = _DTimeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 2, 1)
)
_DTimeGroups_ObjectIdentity = ObjectIdentity
dTimeGroups = _DTimeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 2, 2)
)

# Managed Objects groups

dTimeSysInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 2, 2, 1)
)
dTimeSysInfoGroup.setObjects(
      *(("DLINKSW-TIME-MIB", "dTimeCurrentTimeSource"),
        ("DLINKSW-TIME-MIB", "dTimeCurrentTime"))
)
if mibBuilder.loadTexts:
    dTimeSysInfoGroup.setStatus("current")

dTimeClockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 2, 2, 2)
)
dTimeClockGroup.setObjects(
    ("DLINKSW-TIME-MIB", "dTimeManagedClock")
)
if mibBuilder.loadTexts:
    dTimeClockGroup.setStatus("current")

dTimeSntpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 2, 2, 3)
)
dTimeSntpGroup.setObjects(
      *(("DLINKSW-TIME-MIB", "dTimeSntpEnabled"),
        ("DLINKSW-TIME-MIB", "dTimeSntpBcastClientEnabled"),
        ("DLINKSW-TIME-MIB", "dTimeSntpPollInterval"),
        ("DLINKSW-TIME-MIB", "dTimeSntpSourceIfIndex"),
        ("DLINKSW-TIME-MIB", "dTimeSntpServerTableNum"),
        ("DLINKSW-TIME-MIB", "dTimeSntpServerRowStatus"),
        ("DLINKSW-TIME-MIB", "dTimeSntpServerVersion"),
        ("DLINKSW-TIME-MIB", "dTimeSntpServerLastReceive"),
        ("DLINKSW-TIME-MIB", "dTimeSntpServerSynced"),
        ("DLINKSW-TIME-MIB", "dTimeSntpServerBcast"))
)
if mibBuilder.loadTexts:
    dTimeSntpGroup.setStatus("current")

dTimeSummerTimeCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 2, 2, 4)
)
dTimeSummerTimeCfgGroup.setObjects(
      *(("DLINKSW-TIME-MIB", "dTimeSummerTimeAutoSwitchMode"),
        ("DLINKSW-TIME-MIB", "dTimeSummerTimeStart"),
        ("DLINKSW-TIME-MIB", "dTimeSummerTimeEnd"),
        ("DLINKSW-TIME-MIB", "dTimeSummerTimeOffset"),
        ("DLINKSW-TIME-MIB", "dTimeSntpServerTableNum"),
        ("DLINKSW-TIME-MIB", "dTimeSntpServerRowStatus"))
)
if mibBuilder.loadTexts:
    dTimeSummerTimeCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dTimeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 10, 2, 1, 1)
)
dTimeCompliance.setObjects(
      *(("DLINKSW-TIME-MIB", "dTimeSysInfoGroup"),
        ("DLINKSW-TIME-MIB", "dTimeClockGroup"),
        ("DLINKSW-TIME-MIB", "dTimeSntpGroup"),
        ("DLINKSW-TIME-MIB", "dTimeSummerTimeCfgGroup"))
)
if mibBuilder.loadTexts:
    dTimeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-TIME-MIB",
    **{"DlinkTimeSummerTimeValue": DlinkTimeSummerTimeValue,
       "dlinkSwTimeMIB": dlinkSwTimeMIB,
       "dTimeMIBNotifications": dTimeMIBNotifications,
       "dTimeMIBObjects": dTimeMIBObjects,
       "dTimeGeneral": dTimeGeneral,
       "dTimeSntpEnabled": dTimeSntpEnabled,
       "dTimeSntpBcastClientEnabled": dTimeSntpBcastClientEnabled,
       "dTimeSntpPollInterval": dTimeSntpPollInterval,
       "dTimeSntpSourceIfIndex": dTimeSntpSourceIfIndex,
       "dTimeClock": dTimeClock,
       "dTimeManagedClock": dTimeManagedClock,
       "dTimeCurrentTimeSource": dTimeCurrentTimeSource,
       "dTimeCurrentTime": dTimeCurrentTime,
       "dTimeSummerTime": dTimeSummerTime,
       "dTimeSummerTimeAutoSwitchMode": dTimeSummerTimeAutoSwitchMode,
       "dTimeSummerTimeStart": dTimeSummerTimeStart,
       "dTimeSummerTimeEnd": dTimeSummerTimeEnd,
       "dTimeSummerTimeOffset": dTimeSummerTimeOffset,
       "dTimeServer": dTimeServer,
       "dTimeSntpServerTableNum": dTimeSntpServerTableNum,
       "dTimeSntpServerTable": dTimeSntpServerTable,
       "dTimeSntpServerEntry": dTimeSntpServerEntry,
       "dTimeSntpServerAddrType": dTimeSntpServerAddrType,
       "dTimeSntpServerAddr": dTimeSntpServerAddr,
       "dTimeSntpServerVrfName": dTimeSntpServerVrfName,
       "dTimeSntpServerRowStatus": dTimeSntpServerRowStatus,
       "dTimeSntpServerVersion": dTimeSntpServerVersion,
       "dTimeSntpServerLastReceive": dTimeSntpServerLastReceive,
       "dTimeSntpServerSynced": dTimeSntpServerSynced,
       "dTimeSntpServerBcast": dTimeSntpServerBcast,
       "dTimeMIBConformance": dTimeMIBConformance,
       "dTimeCompliances": dTimeCompliances,
       "dTimeCompliance": dTimeCompliance,
       "dTimeGroups": dTimeGroups,
       "dTimeSysInfoGroup": dTimeSysInfoGroup,
       "dTimeClockGroup": dTimeClockGroup,
       "dTimeSntpGroup": dTimeSntpGroup,
       "dTimeSummerTimeCfgGroup": dTimeSummerTimeCfgGroup}
)
