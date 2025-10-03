# SNMP MIB module (COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\hpmsm\COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB.my
# Produced by pysmi-1.6.2 at Thu Oct  2 11:52:03 2025
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

(ColubrisSSIDOrNone,) = mibBuilder.importSymbols(
    "COLUBRIS-TC",
    "ColubrisSSIDOrNone")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

colubrisPublicAccessRetentionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisPublicAccessRetentionMIBObjects_ObjectIdentity = ObjectIdentity
colubrisPublicAccessRetentionMIBObjects = _ColubrisPublicAccessRetentionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1)
)
_PublicAccessRetentionSessionsGroup_ObjectIdentity = ObjectIdentity
publicAccessRetentionSessionsGroup = _PublicAccessRetentionSessionsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1)
)


class _PublicAccessRetentionSessionsMaxCount_Type(Unsigned32):
    """Custom type publicAccessRetentionSessionsMaxCount based on Unsigned32"""
    defaultValue = 0


_PublicAccessRetentionSessionsMaxCount_Type.__name__ = "Unsigned32"
_PublicAccessRetentionSessionsMaxCount_Object = MibScalar
publicAccessRetentionSessionsMaxCount = _PublicAccessRetentionSessionsMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 1),
    _PublicAccessRetentionSessionsMaxCount_Type()
)
publicAccessRetentionSessionsMaxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionsMaxCount.setStatus("current")


class _PublicAccessRetentionSessionsMaxTime_Type(Integer32):
    """Custom type publicAccessRetentionSessionsMaxTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1200),
    )


_PublicAccessRetentionSessionsMaxTime_Type.__name__ = "Integer32"
_PublicAccessRetentionSessionsMaxTime_Object = MibScalar
publicAccessRetentionSessionsMaxTime = _PublicAccessRetentionSessionsMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 2),
    _PublicAccessRetentionSessionsMaxTime_Type()
)
publicAccessRetentionSessionsMaxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionsMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionsMaxTime.setUnits("seconds")
_PublicAccessRetentionSessionTable_Object = MibTable
publicAccessRetentionSessionTable = _PublicAccessRetentionSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3)
)
if mibBuilder.loadTexts:
    publicAccessRetentionSessionTable.setStatus("current")
_PublicAccessRetentionSessionEntry_Object = MibTableRow
publicAccessRetentionSessionEntry = _PublicAccessRetentionSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1)
)
publicAccessRetentionSessionEntry.setIndexNames(
    (0, "COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionIndex"),
)
if mibBuilder.loadTexts:
    publicAccessRetentionSessionEntry.setStatus("current")


class _PublicAccessRetentionSessionIndex_Type(Integer32):
    """Custom type publicAccessRetentionSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PublicAccessRetentionSessionIndex_Type.__name__ = "Integer32"
_PublicAccessRetentionSessionIndex_Object = MibTableColumn
publicAccessRetentionSessionIndex = _PublicAccessRetentionSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 1),
    _PublicAccessRetentionSessionIndex_Type()
)
publicAccessRetentionSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionIndex.setStatus("current")


class _PublicAccessRetentionSessionState_Type(Integer32):
    """Custom type publicAccessRetentionSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unassigned", 0),
          ("connected", 2),
          ("reconnecting", 3),
          ("disconnecting", 4),
          ("disconnected", 5),
          ("disconnectingAdministrative", 6),
          ("disconnectedAdministrative", 7))
    )


_PublicAccessRetentionSessionState_Type.__name__ = "Integer32"
_PublicAccessRetentionSessionState_Object = MibTableColumn
publicAccessRetentionSessionState = _PublicAccessRetentionSessionState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 2),
    _PublicAccessRetentionSessionState_Type()
)
publicAccessRetentionSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionState.setStatus("current")


class _PublicAccessRetentionSessionUserName_Type(OctetString):
    """Custom type publicAccessRetentionSessionUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_PublicAccessRetentionSessionUserName_Type.__name__ = "OctetString"
_PublicAccessRetentionSessionUserName_Object = MibTableColumn
publicAccessRetentionSessionUserName = _PublicAccessRetentionSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 3),
    _PublicAccessRetentionSessionUserName_Type()
)
publicAccessRetentionSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionUserName.setStatus("current")
_PublicAccessRetentionSessionStartTime_Type = DateAndTime
_PublicAccessRetentionSessionStartTime_Object = MibTableColumn
publicAccessRetentionSessionStartTime = _PublicAccessRetentionSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 4),
    _PublicAccessRetentionSessionStartTime_Type()
)
publicAccessRetentionSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionStartTime.setStatus("current")
_PublicAccessRetentionSessionDuration_Type = Counter32
_PublicAccessRetentionSessionDuration_Object = MibTableColumn
publicAccessRetentionSessionDuration = _PublicAccessRetentionSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 5),
    _PublicAccessRetentionSessionDuration_Type()
)
publicAccessRetentionSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionDuration.setStatus("current")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionDuration.setUnits("seconds")
_PublicAccessRetentionSessionStationIpAddress_Type = IpAddress
_PublicAccessRetentionSessionStationIpAddress_Object = MibTableColumn
publicAccessRetentionSessionStationIpAddress = _PublicAccessRetentionSessionStationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 6),
    _PublicAccessRetentionSessionStationIpAddress_Type()
)
publicAccessRetentionSessionStationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionStationIpAddress.setStatus("current")
_PublicAccessRetentionSessionPacketsSent_Type = Counter32
_PublicAccessRetentionSessionPacketsSent_Object = MibTableColumn
publicAccessRetentionSessionPacketsSent = _PublicAccessRetentionSessionPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 7),
    _PublicAccessRetentionSessionPacketsSent_Type()
)
publicAccessRetentionSessionPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionPacketsSent.setStatus("current")
_PublicAccessRetentionSessionPacketsReceived_Type = Counter32
_PublicAccessRetentionSessionPacketsReceived_Object = MibTableColumn
publicAccessRetentionSessionPacketsReceived = _PublicAccessRetentionSessionPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 8),
    _PublicAccessRetentionSessionPacketsReceived_Type()
)
publicAccessRetentionSessionPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionPacketsReceived.setStatus("current")
_PublicAccessRetentionSessionBytesSent_Type = Counter64
_PublicAccessRetentionSessionBytesSent_Object = MibTableColumn
publicAccessRetentionSessionBytesSent = _PublicAccessRetentionSessionBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 9),
    _PublicAccessRetentionSessionBytesSent_Type()
)
publicAccessRetentionSessionBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionBytesSent.setStatus("current")
_PublicAccessRetentionSessionBytesReceived_Type = Counter64
_PublicAccessRetentionSessionBytesReceived_Object = MibTableColumn
publicAccessRetentionSessionBytesReceived = _PublicAccessRetentionSessionBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 10),
    _PublicAccessRetentionSessionBytesReceived_Type()
)
publicAccessRetentionSessionBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionBytesReceived.setStatus("current")
_PublicAccessRetentionSessionSSID_Type = ColubrisSSIDOrNone
_PublicAccessRetentionSessionSSID_Object = MibTableColumn
publicAccessRetentionSessionSSID = _PublicAccessRetentionSessionSSID_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 11),
    _PublicAccessRetentionSessionSSID_Type()
)
publicAccessRetentionSessionSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessRetentionSessionSSID.setStatus("current")
_PublicAccessRetentionPeriodicStatsGroup_ObjectIdentity = ObjectIdentity
publicAccessRetentionPeriodicStatsGroup = _PublicAccessRetentionPeriodicStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2)
)


class _PublicAccessRetentionPeriodicStatsMaxCount_Type(Integer32):
    """Custom type publicAccessRetentionPeriodicStatsMaxCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_PublicAccessRetentionPeriodicStatsMaxCount_Type.__name__ = "Integer32"
_PublicAccessRetentionPeriodicStatsMaxCount_Object = MibScalar
publicAccessRetentionPeriodicStatsMaxCount = _PublicAccessRetentionPeriodicStatsMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 1),
    _PublicAccessRetentionPeriodicStatsMaxCount_Type()
)
publicAccessRetentionPeriodicStatsMaxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publicAccessRetentionPeriodicStatsMaxCount.setStatus("current")


class _PublicAccessRetentionPeriodicStatsDuration_Type(Integer32):
    """Custom type publicAccessRetentionPeriodicStatsDuration based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1200),
    )


_PublicAccessRetentionPeriodicStatsDuration_Type.__name__ = "Integer32"
_PublicAccessRetentionPeriodicStatsDuration_Object = MibScalar
publicAccessRetentionPeriodicStatsDuration = _PublicAccessRetentionPeriodicStatsDuration_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 2),
    _PublicAccessRetentionPeriodicStatsDuration_Type()
)
publicAccessRetentionPeriodicStatsDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publicAccessRetentionPeriodicStatsDuration.setStatus("current")
if mibBuilder.loadTexts:
    publicAccessRetentionPeriodicStatsDuration.setUnits("seconds")
_PublicAccessRetentionPeriodTable_Object = MibTable
publicAccessRetentionPeriodTable = _PublicAccessRetentionPeriodTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3)
)
if mibBuilder.loadTexts:
    publicAccessRetentionPeriodTable.setStatus("current")
_PublicAccessRetentionPeriodEntry_Object = MibTableRow
publicAccessRetentionPeriodEntry = _PublicAccessRetentionPeriodEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1)
)
publicAccessRetentionPeriodEntry.setIndexNames(
    (0, "COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodIndex"),
)
if mibBuilder.loadTexts:
    publicAccessRetentionPeriodEntry.setStatus("current")


class _PublicAccessRetentionPeriodIndex_Type(Integer32):
    """Custom type publicAccessRetentionPeriodIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_PublicAccessRetentionPeriodIndex_Type.__name__ = "Integer32"
_PublicAccessRetentionPeriodIndex_Object = MibTableColumn
publicAccessRetentionPeriodIndex = _PublicAccessRetentionPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 1),
    _PublicAccessRetentionPeriodIndex_Type()
)
publicAccessRetentionPeriodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    publicAccessRetentionPeriodIndex.setStatus("current")
_PublicAccessRetentionPeriodStartTime_Type = DateAndTime
_PublicAccessRetentionPeriodStartTime_Object = MibTableColumn
publicAccessRetentionPeriodStartTime = _PublicAccessRetentionPeriodStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 2),
    _PublicAccessRetentionPeriodStartTime_Type()
)
publicAccessRetentionPeriodStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessRetentionPeriodStartTime.setStatus("current")
_PublicAccessRetentionPeriodStopTime_Type = DateAndTime
_PublicAccessRetentionPeriodStopTime_Object = MibTableColumn
publicAccessRetentionPeriodStopTime = _PublicAccessRetentionPeriodStopTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 3),
    _PublicAccessRetentionPeriodStopTime_Type()
)
publicAccessRetentionPeriodStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessRetentionPeriodStopTime.setStatus("current")
_PublicAccessRetentionPeriodHighestSessionCount_Type = Counter32
_PublicAccessRetentionPeriodHighestSessionCount_Object = MibTableColumn
publicAccessRetentionPeriodHighestSessionCount = _PublicAccessRetentionPeriodHighestSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 4),
    _PublicAccessRetentionPeriodHighestSessionCount_Type()
)
publicAccessRetentionPeriodHighestSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessRetentionPeriodHighestSessionCount.setStatus("current")
_PublicAccessRetentionPeriodTotalSessionCount_Type = Counter32
_PublicAccessRetentionPeriodTotalSessionCount_Object = MibTableColumn
publicAccessRetentionPeriodTotalSessionCount = _PublicAccessRetentionPeriodTotalSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 5),
    _PublicAccessRetentionPeriodTotalSessionCount_Type()
)
publicAccessRetentionPeriodTotalSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    publicAccessRetentionPeriodTotalSessionCount.setStatus("current")
_PublicAccessRetentionMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
publicAccessRetentionMIBNotificationPrefix = _PublicAccessRetentionMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 2)
)
_PublicAccessRetentionMIBNotifications_ObjectIdentity = ObjectIdentity
publicAccessRetentionMIBNotifications = _PublicAccessRetentionMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 2, 0)
)
_ColubrisPublicAccessRetentionMIBConformance_ObjectIdentity = ObjectIdentity
colubrisPublicAccessRetentionMIBConformance = _ColubrisPublicAccessRetentionMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 3)
)
_ColubrisPublicAccessRetentionMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisPublicAccessRetentionMIBCompliances = _ColubrisPublicAccessRetentionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 1)
)
_ColubrisPublicAccessRetentionMIBGroups_ObjectIdentity = ObjectIdentity
colubrisPublicAccessRetentionMIBGroups = _ColubrisPublicAccessRetentionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 2)
)

# Managed Objects groups

colubrisPublicAccessRetentionSessionsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 2, 1)
)
colubrisPublicAccessRetentionSessionsMIBGroup.setObjects(
      *(("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxCount"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxTime"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionState"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionUserName"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionStartTime"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionDuration"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionStationIpAddress"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionPacketsSent"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionPacketsReceived"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionBytesSent"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionBytesReceived"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionSSID"))
)
if mibBuilder.loadTexts:
    colubrisPublicAccessRetentionSessionsMIBGroup.setStatus("current")

colubrisPublicAccessRetentionPeriodicStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 2, 2)
)
colubrisPublicAccessRetentionPeriodicStatsMIBGroup.setObjects(
      *(("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodicStatsDuration"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodicStatsMaxCount"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodStartTime"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodStopTime"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodHighestSessionCount"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodTotalSessionCount"))
)
if mibBuilder.loadTexts:
    colubrisPublicAccessRetentionPeriodicStatsMIBGroup.setStatus("current")


# Notification objects

publicAccessRetentionSessionMaxCountReachedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 2, 0, 1)
)
publicAccessRetentionSessionMaxCountReachedTrap.setObjects(
      *(("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxCount"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxTime"))
)
if mibBuilder.loadTexts:
    publicAccessRetentionSessionMaxCountReachedTrap.setStatus(
        "current"
    )


# Notifications groups

colubrisPublicAccessRetentionNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 2, 3)
)
colubrisPublicAccessRetentionNotificationGroup.setObjects(
    ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionMaxCountReachedTrap")
)
if mibBuilder.loadTexts:
    colubrisPublicAccessRetentionNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

colubrisPublicAccessRetentionMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 1, 1)
)
colubrisPublicAccessRetentionMIBCompliance.setObjects(
      *(("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "colubrisPublicAccessRetentionSessionsMIBGroup"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "colubrisPublicAccessRetentionPeriodicStatsMIBGroup"),
        ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "colubrisPublicAccessRetentionNotificationGroup"))
)
if mibBuilder.loadTexts:
    colubrisPublicAccessRetentionMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB",
    **{"colubrisPublicAccessRetentionMIB": colubrisPublicAccessRetentionMIB,
       "colubrisPublicAccessRetentionMIBObjects": colubrisPublicAccessRetentionMIBObjects,
       "publicAccessRetentionSessionsGroup": publicAccessRetentionSessionsGroup,
       "publicAccessRetentionSessionsMaxCount": publicAccessRetentionSessionsMaxCount,
       "publicAccessRetentionSessionsMaxTime": publicAccessRetentionSessionsMaxTime,
       "publicAccessRetentionSessionTable": publicAccessRetentionSessionTable,
       "publicAccessRetentionSessionEntry": publicAccessRetentionSessionEntry,
       "publicAccessRetentionSessionIndex": publicAccessRetentionSessionIndex,
       "publicAccessRetentionSessionState": publicAccessRetentionSessionState,
       "publicAccessRetentionSessionUserName": publicAccessRetentionSessionUserName,
       "publicAccessRetentionSessionStartTime": publicAccessRetentionSessionStartTime,
       "publicAccessRetentionSessionDuration": publicAccessRetentionSessionDuration,
       "publicAccessRetentionSessionStationIpAddress": publicAccessRetentionSessionStationIpAddress,
       "publicAccessRetentionSessionPacketsSent": publicAccessRetentionSessionPacketsSent,
       "publicAccessRetentionSessionPacketsReceived": publicAccessRetentionSessionPacketsReceived,
       "publicAccessRetentionSessionBytesSent": publicAccessRetentionSessionBytesSent,
       "publicAccessRetentionSessionBytesReceived": publicAccessRetentionSessionBytesReceived,
       "publicAccessRetentionSessionSSID": publicAccessRetentionSessionSSID,
       "publicAccessRetentionPeriodicStatsGroup": publicAccessRetentionPeriodicStatsGroup,
       "publicAccessRetentionPeriodicStatsMaxCount": publicAccessRetentionPeriodicStatsMaxCount,
       "publicAccessRetentionPeriodicStatsDuration": publicAccessRetentionPeriodicStatsDuration,
       "publicAccessRetentionPeriodTable": publicAccessRetentionPeriodTable,
       "publicAccessRetentionPeriodEntry": publicAccessRetentionPeriodEntry,
       "publicAccessRetentionPeriodIndex": publicAccessRetentionPeriodIndex,
       "publicAccessRetentionPeriodStartTime": publicAccessRetentionPeriodStartTime,
       "publicAccessRetentionPeriodStopTime": publicAccessRetentionPeriodStopTime,
       "publicAccessRetentionPeriodHighestSessionCount": publicAccessRetentionPeriodHighestSessionCount,
       "publicAccessRetentionPeriodTotalSessionCount": publicAccessRetentionPeriodTotalSessionCount,
       "publicAccessRetentionMIBNotificationPrefix": publicAccessRetentionMIBNotificationPrefix,
       "publicAccessRetentionMIBNotifications": publicAccessRetentionMIBNotifications,
       "publicAccessRetentionSessionMaxCountReachedTrap": publicAccessRetentionSessionMaxCountReachedTrap,
       "colubrisPublicAccessRetentionMIBConformance": colubrisPublicAccessRetentionMIBConformance,
       "colubrisPublicAccessRetentionMIBCompliances": colubrisPublicAccessRetentionMIBCompliances,
       "colubrisPublicAccessRetentionMIBCompliance": colubrisPublicAccessRetentionMIBCompliance,
       "colubrisPublicAccessRetentionMIBGroups": colubrisPublicAccessRetentionMIBGroups,
       "colubrisPublicAccessRetentionSessionsMIBGroup": colubrisPublicAccessRetentionSessionsMIBGroup,
       "colubrisPublicAccessRetentionPeriodicStatsMIBGroup": colubrisPublicAccessRetentionPeriodicStatsMIBGroup,
       "colubrisPublicAccessRetentionNotificationGroup": colubrisPublicAccessRetentionNotificationGroup}
)
