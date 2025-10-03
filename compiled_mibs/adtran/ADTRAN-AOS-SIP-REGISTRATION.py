# SNMP MIB module (ADTRAN-AOS-SIP-REGISTRATION) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adtran\ADTRAN-AOS-SIP-REGISTRATION
# Produced by pysmi-1.6.2 at Thu Oct  2 11:14:26 2025
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

(adGenAOSConformance,
 adGenAOSVoice) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSConformance",
    "adGenAOSVoice")

(adIdentityShared,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adGenAOSSipRegistration = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 5, 4)
)
if mibBuilder.loadTexts:
    adGenAOSSipRegistration.setRevisions(
        ("2010-11-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdSipRegistration_ObjectIdentity = ObjectIdentity
adSipRegistration = _AdSipRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4)
)
_AdSipRegistrationTraps_ObjectIdentity = ObjectIdentity
adSipRegistrationTraps = _AdSipRegistrationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 0)
)
_AdSipTrunkRegistrationAlarmTrunkIdentity_Type = DisplayString
_AdSipTrunkRegistrationAlarmTrunkIdentity_Object = MibScalar
adSipTrunkRegistrationAlarmTrunkIdentity = _AdSipTrunkRegistrationAlarmTrunkIdentity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 1),
    _AdSipTrunkRegistrationAlarmTrunkIdentity_Type()
)
adSipTrunkRegistrationAlarmTrunkIdentity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationAlarmTrunkIdentity.setStatus("current")
_AdSipTrunkRegistrationAlarmSipIdentity_Type = DisplayString
_AdSipTrunkRegistrationAlarmSipIdentity_Object = MibScalar
adSipTrunkRegistrationAlarmSipIdentity = _AdSipTrunkRegistrationAlarmSipIdentity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 2),
    _AdSipTrunkRegistrationAlarmSipIdentity_Type()
)
adSipTrunkRegistrationAlarmSipIdentity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationAlarmSipIdentity.setStatus("current")
_AdSipTrunkRegistrationAlarmRegistrar_Type = IpAddress
_AdSipTrunkRegistrationAlarmRegistrar_Object = MibScalar
adSipTrunkRegistrationAlarmRegistrar = _AdSipTrunkRegistrationAlarmRegistrar_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 3),
    _AdSipTrunkRegistrationAlarmRegistrar_Type()
)
adSipTrunkRegistrationAlarmRegistrar.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationAlarmRegistrar.setStatus("current")
_AdSipTrunkRegistrationAlarmTimestamp_Type = Unsigned32
_AdSipTrunkRegistrationAlarmTimestamp_Object = MibScalar
adSipTrunkRegistrationAlarmTimestamp = _AdSipTrunkRegistrationAlarmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 4),
    _AdSipTrunkRegistrationAlarmTimestamp_Type()
)
adSipTrunkRegistrationAlarmTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationAlarmTimestamp.setStatus("current")
_AdSipTrunkRegistrationTable_Object = MibTable
adSipTrunkRegistrationTable = _AdSipTrunkRegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5)
)
if mibBuilder.loadTexts:
    adSipTrunkRegistrationTable.setStatus("current")
_AdSipTrunkRegistrationEntry_Object = MibTableRow
adSipTrunkRegistrationEntry = _AdSipTrunkRegistrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1)
)
adSipTrunkRegistrationEntry.setIndexNames(
    (0, "ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationTableIndex"),
)
if mibBuilder.loadTexts:
    adSipTrunkRegistrationEntry.setStatus("current")
_AdSipTrunkRegistrationTableIndex_Type = Unsigned32
_AdSipTrunkRegistrationTableIndex_Object = MibTableColumn
adSipTrunkRegistrationTableIndex = _AdSipTrunkRegistrationTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 1),
    _AdSipTrunkRegistrationTableIndex_Type()
)
adSipTrunkRegistrationTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationTableIndex.setStatus("current")
_AdSipTrunkRegistrationTrunkIdentity_Type = DisplayString
_AdSipTrunkRegistrationTrunkIdentity_Object = MibTableColumn
adSipTrunkRegistrationTrunkIdentity = _AdSipTrunkRegistrationTrunkIdentity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 2),
    _AdSipTrunkRegistrationTrunkIdentity_Type()
)
adSipTrunkRegistrationTrunkIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationTrunkIdentity.setStatus("current")
_AdSipTrunkRegistrationSipIdentity_Type = DisplayString
_AdSipTrunkRegistrationSipIdentity_Object = MibTableColumn
adSipTrunkRegistrationSipIdentity = _AdSipTrunkRegistrationSipIdentity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 3),
    _AdSipTrunkRegistrationSipIdentity_Type()
)
adSipTrunkRegistrationSipIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationSipIdentity.setStatus("current")
_AdSipTrunkRegistrationStatus_Type = DisplayString
_AdSipTrunkRegistrationStatus_Object = MibTableColumn
adSipTrunkRegistrationStatus = _AdSipTrunkRegistrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 4),
    _AdSipTrunkRegistrationStatus_Type()
)
adSipTrunkRegistrationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationStatus.setStatus("current")
_AdSipTrunkRegistrarIpAddress_Type = DisplayString
_AdSipTrunkRegistrarIpAddress_Object = MibTableColumn
adSipTrunkRegistrarIpAddress = _AdSipTrunkRegistrarIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 5),
    _AdSipTrunkRegistrarIpAddress_Type()
)
adSipTrunkRegistrarIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adSipTrunkRegistrarIpAddress.setStatus("current")
_AdSipTrunkRegistrationGrantTime_Type = Unsigned32
_AdSipTrunkRegistrationGrantTime_Object = MibTableColumn
adSipTrunkRegistrationGrantTime = _AdSipTrunkRegistrationGrantTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 6),
    _AdSipTrunkRegistrationGrantTime_Type()
)
adSipTrunkRegistrationGrantTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationGrantTime.setStatus("current")
_AdSipTrunkRegistrationExpireTime_Type = Unsigned32
_AdSipTrunkRegistrationExpireTime_Object = MibTableColumn
adSipTrunkRegistrationExpireTime = _AdSipTrunkRegistrationExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 7),
    _AdSipTrunkRegistrationExpireTime_Type()
)
adSipTrunkRegistrationExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationExpireTime.setStatus("current")
_AdSipTrunkRegistrationSuccesses_Type = Unsigned32
_AdSipTrunkRegistrationSuccesses_Object = MibTableColumn
adSipTrunkRegistrationSuccesses = _AdSipTrunkRegistrationSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 8),
    _AdSipTrunkRegistrationSuccesses_Type()
)
adSipTrunkRegistrationSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationSuccesses.setStatus("current")
_AdSipTrunkRegistrationFailures_Type = Unsigned32
_AdSipTrunkRegistrationFailures_Object = MibTableColumn
adSipTrunkRegistrationFailures = _AdSipTrunkRegistrationFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 9),
    _AdSipTrunkRegistrationFailures_Type()
)
adSipTrunkRegistrationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationFailures.setStatus("current")
_AdSipTrunkRegistrationRequests_Type = Unsigned32
_AdSipTrunkRegistrationRequests_Object = MibTableColumn
adSipTrunkRegistrationRequests = _AdSipTrunkRegistrationRequests_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 10),
    _AdSipTrunkRegistrationRequests_Type()
)
adSipTrunkRegistrationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationRequests.setStatus("current")
_AdSipTrunkRegistrationChallenges_Type = Unsigned32
_AdSipTrunkRegistrationChallenges_Object = MibTableColumn
adSipTrunkRegistrationChallenges = _AdSipTrunkRegistrationChallenges_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 11),
    _AdSipTrunkRegistrationChallenges_Type()
)
adSipTrunkRegistrationChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationChallenges.setStatus("current")
_AdSipTrunkRegistrationRollovers_Type = Unsigned32
_AdSipTrunkRegistrationRollovers_Object = MibTableColumn
adSipTrunkRegistrationRollovers = _AdSipTrunkRegistrationRollovers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 12),
    _AdSipTrunkRegistrationRollovers_Type()
)
adSipTrunkRegistrationRollovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adSipTrunkRegistrationRollovers.setStatus("current")
_AdSipRegistrationConformance_ObjectIdentity = ObjectIdentity
adSipRegistrationConformance = _AdSipRegistrationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12)
)
_AdSipRegistrationGroups_ObjectIdentity = ObjectIdentity
adSipRegistrationGroups = _AdSipRegistrationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1)
)
_AdSipRegistrationCompliances_ObjectIdentity = ObjectIdentity
adSipRegistrationCompliances = _AdSipRegistrationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 2)
)

# Managed Objects groups

adSipRegistrationNotificationUtilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 2)
)
adSipRegistrationNotificationUtilityGroup.setObjects(
      *(("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTrunkIdentity"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmSipIdentity"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmRegistrar"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTimestamp"))
)
if mibBuilder.loadTexts:
    adSipRegistrationNotificationUtilityGroup.setStatus("current")

adSipRegistrationStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 3)
)
adSipRegistrationStatisticsGroup.setObjects(
      *(("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationTrunkIdentity"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationSipIdentity"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationStatus"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrarIpAddress"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationGrantTime"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationExpireTime"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationSuccesses"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationFailures"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationRequests"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationChallenges"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationRollovers"))
)
if mibBuilder.loadTexts:
    adSipRegistrationStatisticsGroup.setStatus("current")


# Notification objects

adSipTrunkRegistrationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 0, 1)
)
adSipTrunkRegistrationAlarm.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTrunkIdentity"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmSipIdentity"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmRegistrar"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTimestamp"))
)
if mibBuilder.loadTexts:
    adSipTrunkRegistrationAlarm.setStatus(
        "current"
    )


# Notifications groups

adSipRegistrationNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 1)
)
adSipRegistrationNotificationGroup.setObjects(
    ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarm")
)
if mibBuilder.loadTexts:
    adSipRegistrationNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adSipRegistrationFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 2, 1)
)
adSipRegistrationFullCompliance.setObjects(
      *(("ADTRAN-AOS-SIP-REGISTRATION", "adSipRegistrationNotificationUtilityGroup"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipRegistrationNotificationGroup"),
        ("ADTRAN-AOS-SIP-REGISTRATION", "adSipRegistrationStatisticsGroup"))
)
if mibBuilder.loadTexts:
    adSipRegistrationFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-SIP-REGISTRATION",
    **{"adSipRegistration": adSipRegistration,
       "adSipRegistrationTraps": adSipRegistrationTraps,
       "adSipTrunkRegistrationAlarm": adSipTrunkRegistrationAlarm,
       "adSipTrunkRegistrationAlarmTrunkIdentity": adSipTrunkRegistrationAlarmTrunkIdentity,
       "adSipTrunkRegistrationAlarmSipIdentity": adSipTrunkRegistrationAlarmSipIdentity,
       "adSipTrunkRegistrationAlarmRegistrar": adSipTrunkRegistrationAlarmRegistrar,
       "adSipTrunkRegistrationAlarmTimestamp": adSipTrunkRegistrationAlarmTimestamp,
       "adSipTrunkRegistrationTable": adSipTrunkRegistrationTable,
       "adSipTrunkRegistrationEntry": adSipTrunkRegistrationEntry,
       "adSipTrunkRegistrationTableIndex": adSipTrunkRegistrationTableIndex,
       "adSipTrunkRegistrationTrunkIdentity": adSipTrunkRegistrationTrunkIdentity,
       "adSipTrunkRegistrationSipIdentity": adSipTrunkRegistrationSipIdentity,
       "adSipTrunkRegistrationStatus": adSipTrunkRegistrationStatus,
       "adSipTrunkRegistrarIpAddress": adSipTrunkRegistrarIpAddress,
       "adSipTrunkRegistrationGrantTime": adSipTrunkRegistrationGrantTime,
       "adSipTrunkRegistrationExpireTime": adSipTrunkRegistrationExpireTime,
       "adSipTrunkRegistrationSuccesses": adSipTrunkRegistrationSuccesses,
       "adSipTrunkRegistrationFailures": adSipTrunkRegistrationFailures,
       "adSipTrunkRegistrationRequests": adSipTrunkRegistrationRequests,
       "adSipTrunkRegistrationChallenges": adSipTrunkRegistrationChallenges,
       "adSipTrunkRegistrationRollovers": adSipTrunkRegistrationRollovers,
       "adSipRegistrationConformance": adSipRegistrationConformance,
       "adSipRegistrationGroups": adSipRegistrationGroups,
       "adSipRegistrationNotificationGroup": adSipRegistrationNotificationGroup,
       "adSipRegistrationNotificationUtilityGroup": adSipRegistrationNotificationUtilityGroup,
       "adSipRegistrationStatisticsGroup": adSipRegistrationStatisticsGroup,
       "adSipRegistrationCompliances": adSipRegistrationCompliances,
       "adSipRegistrationFullCompliance": adSipRegistrationFullCompliance,
       "adGenAOSSipRegistration": adGenAOSSipRegistration}
)
