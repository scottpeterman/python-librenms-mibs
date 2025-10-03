# SNMP MIB module (BCN-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecatnetworks\BCN-DNS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:25 2025
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

(bcnServices,) = mibBuilder.importSymbols(
    "BCN-SMI-MIB",
    "bcnServices")

(BcnAlarmSeverity,) = mibBuilder.importSymbols(
    "BCN-TC-MIB",
    "BcnAlarmSeverity")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

bcnDnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    bcnDnsMIB.setRevisions(
        ("2010-11-30 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcnDns_ObjectIdentity = ObjectIdentity
bcnDns = _BcnDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2)
)
_BcnDnsObjects_ObjectIdentity = ObjectIdentity
bcnDnsObjects = _BcnDnsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2)
)
_BcnDnsServiceStatus_ObjectIdentity = ObjectIdentity
bcnDnsServiceStatus = _BcnDnsServiceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    bcnDnsServiceStatus.setStatus("current")


class _BcnDnsSerOperState_Type(Integer32):
    """Custom type bcnDnsSerOperState based on Integer32"""
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
        *(("running", 1),
          ("notRunning", 2),
          ("starting", 3),
          ("stopping", 4),
          ("fault", 5))
    )


_BcnDnsSerOperState_Type.__name__ = "Integer32"
_BcnDnsSerOperState_Object = MibScalar
bcnDnsSerOperState = _BcnDnsSerOperState_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 1),
    _BcnDnsSerOperState_Type()
)
bcnDnsSerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDnsSerOperState.setStatus("current")
_BcnDnsSerNumberOfZones_Type = Gauge32
_BcnDnsSerNumberOfZones_Object = MibScalar
bcnDnsSerNumberOfZones = _BcnDnsSerNumberOfZones_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 2),
    _BcnDnsSerNumberOfZones_Type()
)
bcnDnsSerNumberOfZones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDnsSerNumberOfZones.setStatus("current")
_BcnDnsSerTransfersRunning_Type = Gauge32
_BcnDnsSerTransfersRunning_Object = MibScalar
bcnDnsSerTransfersRunning = _BcnDnsSerTransfersRunning_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 3),
    _BcnDnsSerTransfersRunning_Type()
)
bcnDnsSerTransfersRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDnsSerTransfersRunning.setStatus("current")
_BcnDnsSerTransfersDeferred_Type = Gauge32
_BcnDnsSerTransfersDeferred_Object = MibScalar
bcnDnsSerTransfersDeferred = _BcnDnsSerTransfersDeferred_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 4),
    _BcnDnsSerTransfersDeferred_Type()
)
bcnDnsSerTransfersDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDnsSerTransfersDeferred.setStatus("current")
_BcnDnsSerSOAQueriesInProgress_Type = Gauge32
_BcnDnsSerSOAQueriesInProgress_Object = MibScalar
bcnDnsSerSOAQueriesInProgress = _BcnDnsSerSOAQueriesInProgress_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 5),
    _BcnDnsSerSOAQueriesInProgress_Type()
)
bcnDnsSerSOAQueriesInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDnsSerSOAQueriesInProgress.setStatus("current")


class _BcnDnsSerQueryLogging_Type(Integer32):
    """Custom type bcnDnsSerQueryLogging based on Integer32"""
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


_BcnDnsSerQueryLogging_Type.__name__ = "Integer32"
_BcnDnsSerQueryLogging_Object = MibScalar
bcnDnsSerQueryLogging = _BcnDnsSerQueryLogging_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 6),
    _BcnDnsSerQueryLogging_Type()
)
bcnDnsSerQueryLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDnsSerQueryLogging.setStatus("current")


class _BcnDnsSerDebugLevel_Type(Integer32):
    """Custom type bcnDnsSerDebugLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_BcnDnsSerDebugLevel_Type.__name__ = "Integer32"
_BcnDnsSerDebugLevel_Object = MibScalar
bcnDnsSerDebugLevel = _BcnDnsSerDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 7),
    _BcnDnsSerDebugLevel_Type()
)
bcnDnsSerDebugLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDnsSerDebugLevel.setStatus("current")
_BcnDnsServiceStatistics_ObjectIdentity = ObjectIdentity
bcnDnsServiceStatistics = _BcnDnsServiceStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    bcnDnsServiceStatistics.setStatus("current")
_BcnDnsStatServer_ObjectIdentity = ObjectIdentity
bcnDnsStatServer = _BcnDnsStatServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    bcnDnsStatServer.setStatus("current")
_BcnDnsStatSrvQrySuccess_Type = Counter64
_BcnDnsStatSrvQrySuccess_Object = MibScalar
bcnDnsStatSrvQrySuccess = _BcnDnsStatSrvQrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 1),
    _BcnDnsStatSrvQrySuccess_Type()
)
bcnDnsStatSrvQrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDnsStatSrvQrySuccess.setStatus("current")
_BcnDnsStatSrvQryReferral_Type = Counter64
_BcnDnsStatSrvQryReferral_Object = MibScalar
bcnDnsStatSrvQryReferral = _BcnDnsStatSrvQryReferral_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 2),
    _BcnDnsStatSrvQryReferral_Type()
)
bcnDnsStatSrvQryReferral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDnsStatSrvQryReferral.setStatus("current")
_BcnDnsStatSrvQryNXRRSet_Type = Counter64
_BcnDnsStatSrvQryNXRRSet_Object = MibScalar
bcnDnsStatSrvQryNXRRSet = _BcnDnsStatSrvQryNXRRSet_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 3),
    _BcnDnsStatSrvQryNXRRSet_Type()
)
bcnDnsStatSrvQryNXRRSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDnsStatSrvQryNXRRSet.setStatus("current")
_BcnDnsStatSrvQryNXDomain_Type = Counter64
_BcnDnsStatSrvQryNXDomain_Object = MibScalar
bcnDnsStatSrvQryNXDomain = _BcnDnsStatSrvQryNXDomain_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 4),
    _BcnDnsStatSrvQryNXDomain_Type()
)
bcnDnsStatSrvQryNXDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDnsStatSrvQryNXDomain.setStatus("current")
_BcnDnsStatSrvQryRecursion_Type = Counter64
_BcnDnsStatSrvQryRecursion_Object = MibScalar
bcnDnsStatSrvQryRecursion = _BcnDnsStatSrvQryRecursion_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 5),
    _BcnDnsStatSrvQryRecursion_Type()
)
bcnDnsStatSrvQryRecursion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDnsStatSrvQryRecursion.setStatus("current")
_BcnDnsStatSrvQryFailure_Type = Counter64
_BcnDnsStatSrvQryFailure_Object = MibScalar
bcnDnsStatSrvQryFailure = _BcnDnsStatSrvQryFailure_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 6),
    _BcnDnsStatSrvQryFailure_Type()
)
bcnDnsStatSrvQryFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnDnsStatSrvQryFailure.setStatus("current")
_BcnDnsNotification_ObjectIdentity = ObjectIdentity
bcnDnsNotification = _BcnDnsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3)
)
_BcnDnsNotificationEvents_ObjectIdentity = ObjectIdentity
bcnDnsNotificationEvents = _BcnDnsNotificationEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 0)
)
_BcnDnsNotificationData_ObjectIdentity = ObjectIdentity
bcnDnsNotificationData = _BcnDnsNotificationData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 1)
)
_BcnDnsAlarmSeverity_Type = BcnAlarmSeverity
_BcnDnsAlarmSeverity_Object = MibScalar
bcnDnsAlarmSeverity = _BcnDnsAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 1, 1),
    _BcnDnsAlarmSeverity_Type()
)
bcnDnsAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnDnsAlarmSeverity.setStatus("current")
_BcnDnsAlarmInfo_Type = DisplayString
_BcnDnsAlarmInfo_Object = MibScalar
bcnDnsAlarmInfo = _BcnDnsAlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 1, 2),
    _BcnDnsAlarmInfo_Type()
)
bcnDnsAlarmInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnDnsAlarmInfo.setStatus("current")
_BcnDnsConformance_ObjectIdentity = ObjectIdentity
bcnDnsConformance = _BcnDnsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4)
)
_BcnDnsServiceCompliances_ObjectIdentity = ObjectIdentity
bcnDnsServiceCompliances = _BcnDnsServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 1)
)
_BcnDnsServiceGroups_ObjectIdentity = ObjectIdentity
bcnDnsServiceGroups = _BcnDnsServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2)
)

# Managed Objects groups

bcnDnsServiceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2, 1)
)
bcnDnsServiceStatusGroup.setObjects(
      *(("BCN-DNS-MIB", "bcnDnsSerOperState"),
        ("BCN-DNS-MIB", "bcnDnsSerNumberOfZones"),
        ("BCN-DNS-MIB", "bcnDnsSerTransfersRunning"),
        ("BCN-DNS-MIB", "bcnDnsSerTransfersDeferred"),
        ("BCN-DNS-MIB", "bcnDnsSerSOAQueriesInProgress"),
        ("BCN-DNS-MIB", "bcnDnsSerQueryLogging"),
        ("BCN-DNS-MIB", "bcnDnsSerDebugLevel"))
)
if mibBuilder.loadTexts:
    bcnDnsServiceStatusGroup.setStatus("current")

bcnDnsServerStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2, 2)
)
bcnDnsServerStatisticsGroup.setObjects(
      *(("BCN-DNS-MIB", "bcnDnsStatSrvQrySuccess"),
        ("BCN-DNS-MIB", "bcnDnsStatSrvQryReferral"),
        ("BCN-DNS-MIB", "bcnDnsStatSrvQryNXRRSet"),
        ("BCN-DNS-MIB", "bcnDnsStatSrvQryNXDomain"),
        ("BCN-DNS-MIB", "bcnDnsStatSrvQryRecursion"),
        ("BCN-DNS-MIB", "bcnDnsStatSrvQryFailure"))
)
if mibBuilder.loadTexts:
    bcnDnsServerStatisticsGroup.setStatus("current")

bcnDnsNotificationDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2, 4)
)
bcnDnsNotificationDataGroup.setObjects(
      *(("BCN-DNS-MIB", "bcnDnsAlarmSeverity"),
        ("BCN-DNS-MIB", "bcnDnsAlarmInfo"))
)
if mibBuilder.loadTexts:
    bcnDnsNotificationDataGroup.setStatus("current")


# Notification objects

bcnDnsAlarmNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 0, 1)
)
bcnDnsAlarmNotif.setObjects(
      *(("BCN-DNS-MIB", "bcnDnsSerOperState"),
        ("BCN-DNS-MIB", "bcnDnsAlarmSeverity"),
        ("BCN-DNS-MIB", "bcnDnsAlarmInfo"))
)
if mibBuilder.loadTexts:
    bcnDnsAlarmNotif.setStatus(
        "current"
    )


# Notifications groups

bcnDnsNotificationEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2, 3)
)
bcnDnsNotificationEventGroup.setObjects(
    ("BCN-DNS-MIB", "bcnDnsAlarmNotif")
)
if mibBuilder.loadTexts:
    bcnDnsNotificationEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bcnDnsStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 1, 1)
)
bcnDnsStatusCompliance.setObjects(
      *(("BCN-DNS-MIB", "bcnDnsServiceStatusGroup"),
        ("BCN-DNS-MIB", "bcnDnsServerStatisticsGroup"),
        ("BCN-DNS-MIB", "bcnDnsNotificationEventGroup"),
        ("BCN-DNS-MIB", "bcnDnsNotificationDataGroup"))
)
if mibBuilder.loadTexts:
    bcnDnsStatusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCN-DNS-MIB",
    **{"bcnDns": bcnDns,
       "bcnDnsMIB": bcnDnsMIB,
       "bcnDnsObjects": bcnDnsObjects,
       "bcnDnsServiceStatus": bcnDnsServiceStatus,
       "bcnDnsSerOperState": bcnDnsSerOperState,
       "bcnDnsSerNumberOfZones": bcnDnsSerNumberOfZones,
       "bcnDnsSerTransfersRunning": bcnDnsSerTransfersRunning,
       "bcnDnsSerTransfersDeferred": bcnDnsSerTransfersDeferred,
       "bcnDnsSerSOAQueriesInProgress": bcnDnsSerSOAQueriesInProgress,
       "bcnDnsSerQueryLogging": bcnDnsSerQueryLogging,
       "bcnDnsSerDebugLevel": bcnDnsSerDebugLevel,
       "bcnDnsServiceStatistics": bcnDnsServiceStatistics,
       "bcnDnsStatServer": bcnDnsStatServer,
       "bcnDnsStatSrvQrySuccess": bcnDnsStatSrvQrySuccess,
       "bcnDnsStatSrvQryReferral": bcnDnsStatSrvQryReferral,
       "bcnDnsStatSrvQryNXRRSet": bcnDnsStatSrvQryNXRRSet,
       "bcnDnsStatSrvQryNXDomain": bcnDnsStatSrvQryNXDomain,
       "bcnDnsStatSrvQryRecursion": bcnDnsStatSrvQryRecursion,
       "bcnDnsStatSrvQryFailure": bcnDnsStatSrvQryFailure,
       "bcnDnsNotification": bcnDnsNotification,
       "bcnDnsNotificationEvents": bcnDnsNotificationEvents,
       "bcnDnsAlarmNotif": bcnDnsAlarmNotif,
       "bcnDnsNotificationData": bcnDnsNotificationData,
       "bcnDnsAlarmSeverity": bcnDnsAlarmSeverity,
       "bcnDnsAlarmInfo": bcnDnsAlarmInfo,
       "bcnDnsConformance": bcnDnsConformance,
       "bcnDnsServiceCompliances": bcnDnsServiceCompliances,
       "bcnDnsStatusCompliance": bcnDnsStatusCompliance,
       "bcnDnsServiceGroups": bcnDnsServiceGroups,
       "bcnDnsServiceStatusGroup": bcnDnsServiceStatusGroup,
       "bcnDnsServerStatisticsGroup": bcnDnsServerStatisticsGroup,
       "bcnDnsNotificationEventGroup": bcnDnsNotificationEventGroup,
       "bcnDnsNotificationDataGroup": bcnDnsNotificationDataGroup}
)
