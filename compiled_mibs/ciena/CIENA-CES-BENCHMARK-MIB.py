# SNMP MIB module (CIENA-CES-BENCHMARK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-BENCHMARK-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:27 2025
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications,
 cienaCesStatistics) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications",
    "cienaCesStatistics")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesBenchmarkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkMIB.setRevisions(
        ("2016-11-11 00:00",
         "2016-10-14 00:00",
         "2016-10-07 00:00",
         "2016-10-04 00:00",
         "2016-09-07 00:00",
         "2016-06-01 00:00",
         "2016-05-13 00:00",
         "2016-04-26 00:00",
         "2016-03-30 00:00",
         "2016-03-14 00:00",
         "2016-03-10 00:00",
         "2016-03-03 00:00",
         "2016-02-24 00:00",
         "2016-02-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CienaCesBenchmarkLatencyPdvTestState(TextualConvention, Integer32):
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
        *(("idle", 1),
          ("sendingTraffic", 2),
          ("waitingForTimestampData", 3),
          ("waitingForResidualPackets", 4),
          ("processingResults", 5),
          ("stoppedByIntervalTimer", 6),
          ("stoppedByDurationTimer", 7),
          ("stoppedByUser", 8),
          ("done", 9))
    )



class CienaCesBenchmarkThroughputTestState(TextualConvention, Integer32):
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
        *(("idle", 1),
          ("running", 2),
          ("waitingForResidualPackets", 3),
          ("processingResults", 4),
          ("stoppedByIntervalTimer", 5),
          ("stoppedByDurationTimer", 6),
          ("stoppedByUser", 7),
          ("done", 8),
          ("txMaxThroughputForYellowTest", 9))
    )



class CienaCesBenchmarkFramelossTestState(TextualConvention, Integer32):
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
        *(("idle", 1),
          ("runningFirstTest", 2),
          ("waitingForResidualFirstPackets", 3),
          ("processingFirstResults", 4),
          ("runningSecondTest", 5),
          ("waitingForResidualSecondPackets", 6),
          ("processingSecondResults", 7),
          ("stoppedByIntervalTimer", 8),
          ("stoppedByDurationTimer", 9),
          ("stoppedByUser", 10),
          ("done", 11))
    )



class CienaCesBenchmarkRfc2544TestState(TextualConvention, Integer32):
    status = "current"
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
        *(("idle", 1),
          ("running", 2),
          ("stoppedByIntervalTimer", 3),
          ("stoppedByDurationTimer", 4),
          ("stoppedByUser", 5),
          ("done", 6))
    )



class CienaCesBenchmarkY1564TestState(TextualConvention, Integer32):
    status = "current"
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
        *(("idle", 1),
          ("running", 2),
          ("stoppedByIntervalTimer", 3),
          ("stoppedByDurationTimer", 4),
          ("stoppedByUser", 5),
          ("done", 6))
    )



class CienaCesBenchmarkColorTest(TextualConvention, Integer32):
    status = "current"
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
        *(("green", 1),
          ("yellow", 2),
          ("greenYellow", 3),
          ("greenYellowRed", 4))
    )



class CienaCesBenchmarkKpiResult(TextualConvention, Integer32):
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
        *(("notAvailable", 1),
          ("pass", 2),
          ("fail", 3))
    )



class CienaCesBenchmarkAdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )



class CienaCesBenchmarkThroughputKpiPercent(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-4"


class CienaCesBenchmarkFramelossKpiPercent(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-4"


class CienaCesBenchmarkThroughputResult(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"


class CienaCesBenchmarkFramelossResult(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"


class CienaCesBenchmarkPcpBitmap(TextualConvention, Bits):
    status = "current"
    displayHint = "x"
    namedValues = NamedValues(
        *(("pcp0", 0),
          ("pcp1", 1),
          ("pcp2", 2),
          ("pcp3", 3),
          ("pcp4", 4),
          ("pcp5", 5),
          ("pcp6", 6),
          ("pcp7", 7))
    )


# MIB Managed Objects in the order of their OIDs

_CienaCesBenchmarkMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesBenchmarkMIBObjects = _CienaCesBenchmarkMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1)
)
_CienaCesBenchmarkModule_ObjectIdentity = ObjectIdentity
cienaCesBenchmarkModule = _CienaCesBenchmarkModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1)
)
_CienaCesBenchmarkGlobalObjects_ObjectIdentity = ObjectIdentity
cienaCesBenchmarkGlobalObjects = _CienaCesBenchmarkGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1)
)
_CienaCesBenchmarkGlobalAdminState_Type = CienaCesBenchmarkAdminState
_CienaCesBenchmarkGlobalAdminState_Object = MibScalar
cienaCesBenchmarkGlobalAdminState = _CienaCesBenchmarkGlobalAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 1),
    _CienaCesBenchmarkGlobalAdminState_Type()
)
cienaCesBenchmarkGlobalAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalAdminState.setStatus("current")


class _CienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId_Type(Integer32):
    """Custom type cienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId_Type.__name__ = "Integer32"
_CienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId_Object = MibScalar
cienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId = _CienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 2),
    _CienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId_Type()
)
cienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId.setStatus("current")


class _CienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId_Type(Integer32):
    """Custom type cienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId_Type.__name__ = "Integer32"
_CienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId_Object = MibScalar
cienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId = _CienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 3),
    _CienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId_Type()
)
cienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId.setStatus("current")


class _CienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId_Type(Integer32):
    """Custom type cienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId_Type.__name__ = "Integer32"
_CienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId_Object = MibScalar
cienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId = _CienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 4),
    _CienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId_Type()
)
cienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId.setStatus("current")
_CienaCesBenchmarkGlobalPlatformMaxConfigEntities_Type = Integer32
_CienaCesBenchmarkGlobalPlatformMaxConfigEntities_Object = MibScalar
cienaCesBenchmarkGlobalPlatformMaxConfigEntities = _CienaCesBenchmarkGlobalPlatformMaxConfigEntities_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 5),
    _CienaCesBenchmarkGlobalPlatformMaxConfigEntities_Type()
)
cienaCesBenchmarkGlobalPlatformMaxConfigEntities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalPlatformMaxConfigEntities.setStatus("current")
_CienaCesBenchmarkGlobalPlatformMaxConfigTestInstances_Type = Integer32
_CienaCesBenchmarkGlobalPlatformMaxConfigTestInstances_Object = MibScalar
cienaCesBenchmarkGlobalPlatformMaxConfigTestInstances = _CienaCesBenchmarkGlobalPlatformMaxConfigTestInstances_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 6),
    _CienaCesBenchmarkGlobalPlatformMaxConfigTestInstances_Type()
)
cienaCesBenchmarkGlobalPlatformMaxConfigTestInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalPlatformMaxConfigTestInstances.setStatus("current")
_CienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles_Type = Integer32
_CienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles_Object = MibScalar
cienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles = _CienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 7),
    _CienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles_Type()
)
cienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles.setStatus("current")
_CienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles_Type = Integer32
_CienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles_Object = MibScalar
cienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles = _CienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 8),
    _CienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles_Type()
)
cienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles.setStatus("current")
_CienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles_Type = Integer32
_CienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles_Object = MibScalar
cienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles = _CienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 9),
    _CienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles_Type()
)
cienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles.setStatus("current")
_CienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences_Type = Integer32
_CienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences_Object = MibScalar
cienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences = _CienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 10),
    _CienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences_Type()
)
cienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences.setStatus("current")
_CienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests_Type = Integer32
_CienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests_Object = MibScalar
cienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests = _CienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 11),
    _CienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests_Type()
)
cienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests.setStatus("current")
_CienaCesBenchmarkGlobalConfiguredEntities_Type = Integer32
_CienaCesBenchmarkGlobalConfiguredEntities_Object = MibScalar
cienaCesBenchmarkGlobalConfiguredEntities = _CienaCesBenchmarkGlobalConfiguredEntities_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 12),
    _CienaCesBenchmarkGlobalConfiguredEntities_Type()
)
cienaCesBenchmarkGlobalConfiguredEntities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalConfiguredEntities.setStatus("current")
_CienaCesBenchmarkGlobalConfiguredTestInstances_Type = Integer32
_CienaCesBenchmarkGlobalConfiguredTestInstances_Object = MibScalar
cienaCesBenchmarkGlobalConfiguredTestInstances = _CienaCesBenchmarkGlobalConfiguredTestInstances_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 13),
    _CienaCesBenchmarkGlobalConfiguredTestInstances_Type()
)
cienaCesBenchmarkGlobalConfiguredTestInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalConfiguredTestInstances.setStatus("current")
_CienaCesBenchmarkGlobalConfiguredProfiles_Type = Integer32
_CienaCesBenchmarkGlobalConfiguredProfiles_Object = MibScalar
cienaCesBenchmarkGlobalConfiguredProfiles = _CienaCesBenchmarkGlobalConfiguredProfiles_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 14),
    _CienaCesBenchmarkGlobalConfiguredProfiles_Type()
)
cienaCesBenchmarkGlobalConfiguredProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalConfiguredProfiles.setStatus("current")
_CienaCesBenchmarkGlobalConfiguredEmixSequences_Type = Integer32
_CienaCesBenchmarkGlobalConfiguredEmixSequences_Object = MibScalar
cienaCesBenchmarkGlobalConfiguredEmixSequences = _CienaCesBenchmarkGlobalConfiguredEmixSequences_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 15),
    _CienaCesBenchmarkGlobalConfiguredEmixSequences_Type()
)
cienaCesBenchmarkGlobalConfiguredEmixSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalConfiguredEmixSequences.setStatus("current")
_CienaCesBenchmarkGlobalConfiguredKpiProfiles_Type = Integer32
_CienaCesBenchmarkGlobalConfiguredKpiProfiles_Object = MibScalar
cienaCesBenchmarkGlobalConfiguredKpiProfiles = _CienaCesBenchmarkGlobalConfiguredKpiProfiles_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 16),
    _CienaCesBenchmarkGlobalConfiguredKpiProfiles_Type()
)
cienaCesBenchmarkGlobalConfiguredKpiProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalConfiguredKpiProfiles.setStatus("current")
_CienaCesBenchmarkGlobalConfiguredBwAllocProfiles_Type = Integer32
_CienaCesBenchmarkGlobalConfiguredBwAllocProfiles_Object = MibScalar
cienaCesBenchmarkGlobalConfiguredBwAllocProfiles = _CienaCesBenchmarkGlobalConfiguredBwAllocProfiles_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 17),
    _CienaCesBenchmarkGlobalConfiguredBwAllocProfiles_Type()
)
cienaCesBenchmarkGlobalConfiguredBwAllocProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalConfiguredBwAllocProfiles.setStatus("current")
_CienaCesBenchmarkGlobalEnabledTestInstances_Type = Integer32
_CienaCesBenchmarkGlobalEnabledTestInstances_Object = MibScalar
cienaCesBenchmarkGlobalEnabledTestInstances = _CienaCesBenchmarkGlobalEnabledTestInstances_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 18),
    _CienaCesBenchmarkGlobalEnabledTestInstances_Type()
)
cienaCesBenchmarkGlobalEnabledTestInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalEnabledTestInstances.setStatus("current")
_CienaCesBenchmarkGlobalGeneratorRunningTestInstances_Type = Integer32
_CienaCesBenchmarkGlobalGeneratorRunningTestInstances_Object = MibScalar
cienaCesBenchmarkGlobalGeneratorRunningTestInstances = _CienaCesBenchmarkGlobalGeneratorRunningTestInstances_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 1, 19),
    _CienaCesBenchmarkGlobalGeneratorRunningTestInstances_Type()
)
cienaCesBenchmarkGlobalGeneratorRunningTestInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGlobalGeneratorRunningTestInstances.setStatus("current")
_CienaCesBenchmarkEntityTable_Object = MibTable
cienaCesBenchmarkEntityTable = _CienaCesBenchmarkEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityTable.setStatus("current")
_CienaCesBenchmarkEntityEntry_Object = MibTableRow
cienaCesBenchmarkEntityEntry = _CienaCesBenchmarkEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1)
)
cienaCesBenchmarkEntityEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEntityEntryId"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntry.setStatus("current")
_CienaCesBenchmarkEntityEntryId_Type = Integer32
_CienaCesBenchmarkEntityEntryId_Object = MibTableColumn
cienaCesBenchmarkEntityEntryId = _CienaCesBenchmarkEntityEntryId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 1),
    _CienaCesBenchmarkEntityEntryId_Type()
)
cienaCesBenchmarkEntityEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryId.setStatus("current")


class _CienaCesBenchmarkEntityEntryName_Type(DisplayString):
    """Custom type cienaCesBenchmarkEntityEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 46),
    )


_CienaCesBenchmarkEntityEntryName_Type.__name__ = "DisplayString"
_CienaCesBenchmarkEntityEntryName_Object = MibTableColumn
cienaCesBenchmarkEntityEntryName = _CienaCesBenchmarkEntityEntryName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 2),
    _CienaCesBenchmarkEntityEntryName_Type()
)
cienaCesBenchmarkEntityEntryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryName.setStatus("current")


class _CienaCesBenchmarkEntityEntryRole_Type(Integer32):
    """Custom type cienaCesBenchmarkEntityEntryRole based on Integer32"""
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
        *(("none", 1),
          ("reflector", 2),
          ("generator", 3))
    )


_CienaCesBenchmarkEntityEntryRole_Type.__name__ = "Integer32"
_CienaCesBenchmarkEntityEntryRole_Object = MibTableColumn
cienaCesBenchmarkEntityEntryRole = _CienaCesBenchmarkEntityEntryRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 3),
    _CienaCesBenchmarkEntityEntryRole_Type()
)
cienaCesBenchmarkEntityEntryRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryRole.setStatus("current")


class _CienaCesBenchmarkEntityEntryPortId_Type(Integer32):
    """Custom type cienaCesBenchmarkEntityEntryPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesBenchmarkEntityEntryPortId_Type.__name__ = "Integer32"
_CienaCesBenchmarkEntityEntryPortId_Object = MibTableColumn
cienaCesBenchmarkEntityEntryPortId = _CienaCesBenchmarkEntityEntryPortId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 4),
    _CienaCesBenchmarkEntityEntryPortId_Type()
)
cienaCesBenchmarkEntityEntryPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryPortId.setStatus("current")


class _CienaCesBenchmarkEntityEntryMode_Type(Integer32):
    """Custom type cienaCesBenchmarkEntityEntryMode based on Integer32"""
    defaultValue = 2

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
        *(("none", 1),
          ("inService", 2),
          ("outOfService", 3),
          ("vidOutOfService", 4),
          ("evcOutOfService", 5))
    )


_CienaCesBenchmarkEntityEntryMode_Type.__name__ = "Integer32"
_CienaCesBenchmarkEntityEntryMode_Object = MibTableColumn
cienaCesBenchmarkEntityEntryMode = _CienaCesBenchmarkEntityEntryMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 5),
    _CienaCesBenchmarkEntityEntryMode_Type()
)
cienaCesBenchmarkEntityEntryMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryMode.setStatus("current")


class _CienaCesBenchmarkEntityEntryAdminState_Type(CienaCesBenchmarkAdminState):
    """Custom type cienaCesBenchmarkEntityEntryAdminState based on CienaCesBenchmarkAdminState"""
    defaultValue = 1


_CienaCesBenchmarkEntityEntryAdminState_Type.__name__ = "CienaCesBenchmarkAdminState"
_CienaCesBenchmarkEntityEntryAdminState_Object = MibTableColumn
cienaCesBenchmarkEntityEntryAdminState = _CienaCesBenchmarkEntityEntryAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 6),
    _CienaCesBenchmarkEntityEntryAdminState_Type()
)
cienaCesBenchmarkEntityEntryAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryAdminState.setStatus("current")
_CienaCesBenchmarkEntityEntryLocalMac_Type = MacAddress
_CienaCesBenchmarkEntityEntryLocalMac_Object = MibTableColumn
cienaCesBenchmarkEntityEntryLocalMac = _CienaCesBenchmarkEntityEntryLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 7),
    _CienaCesBenchmarkEntityEntryLocalMac_Type()
)
cienaCesBenchmarkEntityEntryLocalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryLocalMac.setStatus("current")
_CienaCesBenchmarkEntityEntrySlotId_Type = Integer32
_CienaCesBenchmarkEntityEntrySlotId_Object = MibTableColumn
cienaCesBenchmarkEntityEntrySlotId = _CienaCesBenchmarkEntityEntrySlotId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 8),
    _CienaCesBenchmarkEntityEntrySlotId_Type()
)
cienaCesBenchmarkEntityEntrySlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntrySlotId.setStatus("current")


class _CienaCesBenchmarkEntityEntryReflectorVendorType_Type(Integer32):
    """Custom type cienaCesBenchmarkEntityEntryReflectorVendorType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ciena", 2))
    )


_CienaCesBenchmarkEntityEntryReflectorVendorType_Type.__name__ = "Integer32"
_CienaCesBenchmarkEntityEntryReflectorVendorType_Object = MibTableColumn
cienaCesBenchmarkEntityEntryReflectorVendorType = _CienaCesBenchmarkEntityEntryReflectorVendorType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 9),
    _CienaCesBenchmarkEntityEntryReflectorVendorType_Type()
)
cienaCesBenchmarkEntityEntryReflectorVendorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryReflectorVendorType.setStatus("current")


class _CienaCesBenchmarkEntityEntryReflectionLevel_Type(Integer32):
    """Custom type cienaCesBenchmarkEntityEntryReflectionLevel based on Integer32"""
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
        *(("none", 1),
          ("l2only", 2),
          ("l2ToL3IPv4only", 3),
          ("l2ToL3IPv6only", 4),
          ("l2ToL4IPv4only", 5),
          ("l2ToL4IPv6only", 6),
          ("l2ToL4", 7))
    )


_CienaCesBenchmarkEntityEntryReflectionLevel_Type.__name__ = "Integer32"
_CienaCesBenchmarkEntityEntryReflectionLevel_Object = MibTableColumn
cienaCesBenchmarkEntityEntryReflectionLevel = _CienaCesBenchmarkEntityEntryReflectionLevel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 10),
    _CienaCesBenchmarkEntityEntryReflectionLevel_Type()
)
cienaCesBenchmarkEntityEntryReflectionLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryReflectionLevel.setStatus("current")


class _CienaCesBenchmarkEntityEntryGeneratorHFrameSize_Type(Integer32):
    """Custom type cienaCesBenchmarkEntityEntryGeneratorHFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9216),
    )


_CienaCesBenchmarkEntityEntryGeneratorHFrameSize_Type.__name__ = "Integer32"
_CienaCesBenchmarkEntityEntryGeneratorHFrameSize_Object = MibTableColumn
cienaCesBenchmarkEntityEntryGeneratorHFrameSize = _CienaCesBenchmarkEntityEntryGeneratorHFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 11),
    _CienaCesBenchmarkEntityEntryGeneratorHFrameSize_Type()
)
cienaCesBenchmarkEntityEntryGeneratorHFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryGeneratorHFrameSize.setStatus("current")
_CienaCesBenchmarkEntityEntryMaxConfigTestInstances_Type = Integer32
_CienaCesBenchmarkEntityEntryMaxConfigTestInstances_Object = MibTableColumn
cienaCesBenchmarkEntityEntryMaxConfigTestInstances = _CienaCesBenchmarkEntityEntryMaxConfigTestInstances_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 12),
    _CienaCesBenchmarkEntityEntryMaxConfigTestInstances_Type()
)
cienaCesBenchmarkEntityEntryMaxConfigTestInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryMaxConfigTestInstances.setStatus("current")
_CienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances_Type = Integer32
_CienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances_Object = MibTableColumn
cienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances = _CienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 13),
    _CienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances_Type()
)
cienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances.setStatus("current")
_CienaCesBenchmarkEntityEntryOperEnabled_Type = TruthValue
_CienaCesBenchmarkEntityEntryOperEnabled_Object = MibTableColumn
cienaCesBenchmarkEntityEntryOperEnabled = _CienaCesBenchmarkEntityEntryOperEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 14),
    _CienaCesBenchmarkEntityEntryOperEnabled_Type()
)
cienaCesBenchmarkEntityEntryOperEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryOperEnabled.setStatus("current")
_CienaCesBenchmarkEntityEntryNumTestInstancesConfigured_Type = Integer32
_CienaCesBenchmarkEntityEntryNumTestInstancesConfigured_Object = MibTableColumn
cienaCesBenchmarkEntityEntryNumTestInstancesConfigured = _CienaCesBenchmarkEntityEntryNumTestInstancesConfigured_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 15),
    _CienaCesBenchmarkEntityEntryNumTestInstancesConfigured_Type()
)
cienaCesBenchmarkEntityEntryNumTestInstancesConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryNumTestInstancesConfigured.setStatus("current")
_CienaCesBenchmarkEntityEntryNumTestInstancesEnabled_Type = Integer32
_CienaCesBenchmarkEntityEntryNumTestInstancesEnabled_Object = MibTableColumn
cienaCesBenchmarkEntityEntryNumTestInstancesEnabled = _CienaCesBenchmarkEntityEntryNumTestInstancesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 16),
    _CienaCesBenchmarkEntityEntryNumTestInstancesEnabled_Type()
)
cienaCesBenchmarkEntityEntryNumTestInstancesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryNumTestInstancesEnabled.setStatus("current")
_CienaCesBenchmarkEntityEntryGenNumTestInstancesRunning_Type = Integer32
_CienaCesBenchmarkEntityEntryGenNumTestInstancesRunning_Object = MibTableColumn
cienaCesBenchmarkEntityEntryGenNumTestInstancesRunning = _CienaCesBenchmarkEntityEntryGenNumTestInstancesRunning_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 17),
    _CienaCesBenchmarkEntityEntryGenNumTestInstancesRunning_Type()
)
cienaCesBenchmarkEntityEntryGenNumTestInstancesRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryGenNumTestInstancesRunning.setStatus("current")
_CienaCesBenchmarkEntityEntryBwAvailable_Type = Integer32
_CienaCesBenchmarkEntityEntryBwAvailable_Object = MibTableColumn
cienaCesBenchmarkEntityEntryBwAvailable = _CienaCesBenchmarkEntityEntryBwAvailable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 18),
    _CienaCesBenchmarkEntityEntryBwAvailable_Type()
)
cienaCesBenchmarkEntityEntryBwAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryBwAvailable.setStatus("current")
_CienaCesBenchmarkEntityEntryGenBwUsedByRunningTests_Type = Integer32
_CienaCesBenchmarkEntityEntryGenBwUsedByRunningTests_Object = MibTableColumn
cienaCesBenchmarkEntityEntryGenBwUsedByRunningTests = _CienaCesBenchmarkEntityEntryGenBwUsedByRunningTests_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 19),
    _CienaCesBenchmarkEntityEntryGenBwUsedByRunningTests_Type()
)
cienaCesBenchmarkEntityEntryGenBwUsedByRunningTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryGenBwUsedByRunningTests.setStatus("current")
_CienaCesBenchmarkEntityEntryAvailableHwSessions_Type = Integer32
_CienaCesBenchmarkEntityEntryAvailableHwSessions_Object = MibTableColumn
cienaCesBenchmarkEntityEntryAvailableHwSessions = _CienaCesBenchmarkEntityEntryAvailableHwSessions_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 20),
    _CienaCesBenchmarkEntityEntryAvailableHwSessions_Type()
)
cienaCesBenchmarkEntityEntryAvailableHwSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryAvailableHwSessions.setStatus("current")
_CienaCesBenchmarkEntityEntryAllocatedHwSessions_Type = Integer32
_CienaCesBenchmarkEntityEntryAllocatedHwSessions_Object = MibTableColumn
cienaCesBenchmarkEntityEntryAllocatedHwSessions = _CienaCesBenchmarkEntityEntryAllocatedHwSessions_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 21),
    _CienaCesBenchmarkEntityEntryAllocatedHwSessions_Type()
)
cienaCesBenchmarkEntityEntryAllocatedHwSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryAllocatedHwSessions.setStatus("current")
_CienaCesBenchmarkEntityEntryRowStatus_Type = RowStatus
_CienaCesBenchmarkEntityEntryRowStatus_Object = MibTableColumn
cienaCesBenchmarkEntityEntryRowStatus = _CienaCesBenchmarkEntityEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 22),
    _CienaCesBenchmarkEntityEntryRowStatus_Type()
)
cienaCesBenchmarkEntityEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryRowStatus.setStatus("current")
_CienaCesBenchmarkEntityEntryClearStats_Type = TruthValue
_CienaCesBenchmarkEntityEntryClearStats_Object = MibTableColumn
cienaCesBenchmarkEntityEntryClearStats = _CienaCesBenchmarkEntityEntryClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 23),
    _CienaCesBenchmarkEntityEntryClearStats_Type()
)
cienaCesBenchmarkEntityEntryClearStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryClearStats.setStatus("current")
_CienaCesBenchmarkEntityEntryReflectorMacValidation_Type = TruthValue
_CienaCesBenchmarkEntityEntryReflectorMacValidation_Object = MibTableColumn
cienaCesBenchmarkEntityEntryReflectorMacValidation = _CienaCesBenchmarkEntityEntryReflectorMacValidation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 2, 1, 24),
    _CienaCesBenchmarkEntityEntryReflectorMacValidation_Type()
)
cienaCesBenchmarkEntityEntryReflectorMacValidation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityEntryReflectorMacValidation.setStatus("current")
_CienaCesBenchmarkEntityStatsTable_Object = MibTable
cienaCesBenchmarkEntityStatsTable = _CienaCesBenchmarkEntityStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsTable.setStatus("current")
_CienaCesBenchmarkEntityStatsEntry_Object = MibTableRow
cienaCesBenchmarkEntityStatsEntry = _CienaCesBenchmarkEntityStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1)
)
cienaCesBenchmarkEntityStatsEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEntityEntryId"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntry.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryClear_Type = TruthValue
_CienaCesBenchmarkEntityStatsEntryClear_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryClear = _CienaCesBenchmarkEntityStatsEntryClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 1),
    _CienaCesBenchmarkEntityStatsEntryClear_Type()
)
cienaCesBenchmarkEntityStatsEntryClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryClear.setStatus("obsolete")
_CienaCesBenchmarkEntityStatsEntryPortTxBytes_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxBytes_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxBytes = _CienaCesBenchmarkEntityStatsEntryPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 2),
    _CienaCesBenchmarkEntityStatsEntryPortTxBytes_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTxBytes.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTxPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxPkts = _CienaCesBenchmarkEntityStatsEntryPortTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 3),
    _CienaCesBenchmarkEntityStatsEntryPortTxPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTxPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts = _CienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 4),
    _CienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTxUcastPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxUcastPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxUcastPkts = _CienaCesBenchmarkEntityStatsEntryPortTxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 5),
    _CienaCesBenchmarkEntityStatsEntryPortTxUcastPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTxUcastPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTxMcastPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxMcastPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxMcastPkts = _CienaCesBenchmarkEntityStatsEntryPortTxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 6),
    _CienaCesBenchmarkEntityStatsEntryPortTxMcastPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTxMcastPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTxBcastPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxBcastPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxBcastPkts = _CienaCesBenchmarkEntityStatsEntryPortTxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 7),
    _CienaCesBenchmarkEntityStatsEntryPortTxBcastPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTxBcastPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts = _CienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 8),
    _CienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxOversizePkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxOversizePkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxOversizePkts = _CienaCesBenchmarkEntityStatsEntryPortRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 9),
    _CienaCesBenchmarkEntityStatsEntryPortRxOversizePkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxOversizePkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts = _CienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 10),
    _CienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts = _CienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 11),
    _CienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTxPausePkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxPausePkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxPausePkts = _CienaCesBenchmarkEntityStatsEntryPortTxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 12),
    _CienaCesBenchmarkEntityStatsEntryPortTxPausePkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTxPausePkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTxDropPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxDropPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxDropPkts = _CienaCesBenchmarkEntityStatsEntryPortTxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 13),
    _CienaCesBenchmarkEntityStatsEntryPortTxDropPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTxDropPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts = _CienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 14),
    _CienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts = _CienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 15),
    _CienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts = _CienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 16),
    _CienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts = _CienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 17),
    _CienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts = _CienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 18),
    _CienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts = _CienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 19),
    _CienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts = _CienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 20),
    _CienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts = _CienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 21),
    _CienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts = _CienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 22),
    _CienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts = _CienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 23),
    _CienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts = _CienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 24),
    _CienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxBytes_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxBytes_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxBytes = _CienaCesBenchmarkEntityStatsEntryPortRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 25),
    _CienaCesBenchmarkEntityStatsEntryPortRxBytes_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxBytes.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxPkts = _CienaCesBenchmarkEntityStatsEntryPortRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 26),
    _CienaCesBenchmarkEntityStatsEntryPortRxPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts = _CienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 27),
    _CienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxDeferPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxDeferPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxDeferPkts = _CienaCesBenchmarkEntityStatsEntryPortRxDeferPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 28),
    _CienaCesBenchmarkEntityStatsEntryPortRxDeferPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxDeferPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxDeferPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxGiantPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxGiantPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxGiantPkts = _CienaCesBenchmarkEntityStatsEntryPortRxGiantPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 29),
    _CienaCesBenchmarkEntityStatsEntryPortRxGiantPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxGiantPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxGiantPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts = _CienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 30),
    _CienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts = _CienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 31),
    _CienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts = _CienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 32),
    _CienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts = _CienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 33),
    _CienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxPausePkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxPausePkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxPausePkts = _CienaCesBenchmarkEntityStatsEntryPortRxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 34),
    _CienaCesBenchmarkEntityStatsEntryPortRxPausePkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxPausePkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxUcastPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxUcastPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxUcastPkts = _CienaCesBenchmarkEntityStatsEntryPortRxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 35),
    _CienaCesBenchmarkEntityStatsEntryPortRxUcastPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxUcastPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxMcastPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxMcastPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxMcastPkts = _CienaCesBenchmarkEntityStatsEntryPortRxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 36),
    _CienaCesBenchmarkEntityStatsEntryPortRxMcastPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxMcastPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRxBcastPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxBcastPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxBcastPkts = _CienaCesBenchmarkEntityStatsEntryPortRxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 37),
    _CienaCesBenchmarkEntityStatsEntryPortRxBcastPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRxBcastPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts = _CienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 38),
    _CienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts = _CienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 39),
    _CienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts = _CienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 40),
    _CienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts = _CienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 41),
    _CienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts = _CienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 42),
    _CienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts = _CienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 43),
    _CienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts = _CienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 44),
    _CienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts = _CienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 45),
    _CienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts = _CienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 46),
    _CienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts_Type()
)
cienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts = _CienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 47),
    _CienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts = _CienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 48),
    _CienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts.setStatus("current")
_CienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts_Type = Counter64
_CienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts_Object = MibTableColumn
cienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts = _CienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 3, 1, 49),
    _CienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts_Type()
)
cienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts.setStatus("current")
_CienaCesBenchmarkEmixSequenceTable_Object = MibTable
cienaCesBenchmarkEmixSequenceTable = _CienaCesBenchmarkEmixSequenceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixSequenceTable.setStatus("current")
_CienaCesBenchmarkEmixSequenceEntry_Object = MibTableRow
cienaCesBenchmarkEmixSequenceEntry = _CienaCesBenchmarkEmixSequenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 4, 1)
)
cienaCesBenchmarkEmixSequenceEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEmixSequenceId"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixSequenceEntry.setStatus("current")


class _CienaCesBenchmarkEmixSequenceId_Type(Integer32):
    """Custom type cienaCesBenchmarkEmixSequenceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CienaCesBenchmarkEmixSequenceId_Type.__name__ = "Integer32"
_CienaCesBenchmarkEmixSequenceId_Object = MibTableColumn
cienaCesBenchmarkEmixSequenceId = _CienaCesBenchmarkEmixSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 4, 1, 1),
    _CienaCesBenchmarkEmixSequenceId_Type()
)
cienaCesBenchmarkEmixSequenceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixSequenceId.setStatus("current")


class _CienaCesBenchmarkEmixSequenceName_Type(DisplayString):
    """Custom type cienaCesBenchmarkEmixSequenceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 46),
    )


_CienaCesBenchmarkEmixSequenceName_Type.__name__ = "DisplayString"
_CienaCesBenchmarkEmixSequenceName_Object = MibTableColumn
cienaCesBenchmarkEmixSequenceName = _CienaCesBenchmarkEmixSequenceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 4, 1, 2),
    _CienaCesBenchmarkEmixSequenceName_Type()
)
cienaCesBenchmarkEmixSequenceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixSequenceName.setStatus("current")


class _CienaCesBenchmarkEmixSequence_Type(DisplayString):
    """Custom type cienaCesBenchmarkEmixSequence based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CienaCesBenchmarkEmixSequence_Type.__name__ = "DisplayString"
_CienaCesBenchmarkEmixSequence_Object = MibTableColumn
cienaCesBenchmarkEmixSequence = _CienaCesBenchmarkEmixSequence_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 4, 1, 3),
    _CienaCesBenchmarkEmixSequence_Type()
)
cienaCesBenchmarkEmixSequence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixSequence.setStatus("current")


class _CienaCesBenchmarkEmixSequenceUFrameSize_Type(Integer32):
    """Custom type cienaCesBenchmarkEmixSequenceUFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9216),
    )


_CienaCesBenchmarkEmixSequenceUFrameSize_Type.__name__ = "Integer32"
_CienaCesBenchmarkEmixSequenceUFrameSize_Object = MibTableColumn
cienaCesBenchmarkEmixSequenceUFrameSize = _CienaCesBenchmarkEmixSequenceUFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 4, 1, 4),
    _CienaCesBenchmarkEmixSequenceUFrameSize_Type()
)
cienaCesBenchmarkEmixSequenceUFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixSequenceUFrameSize.setStatus("current")
_CienaCesBenchmarkEmixSequenceNumOfRef_Type = Integer32
_CienaCesBenchmarkEmixSequenceNumOfRef_Object = MibTableColumn
cienaCesBenchmarkEmixSequenceNumOfRef = _CienaCesBenchmarkEmixSequenceNumOfRef_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 4, 1, 5),
    _CienaCesBenchmarkEmixSequenceNumOfRef_Type()
)
cienaCesBenchmarkEmixSequenceNumOfRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixSequenceNumOfRef.setStatus("current")
_CienaCesBenchmarkEmixSequenceUserCreated_Type = TruthValue
_CienaCesBenchmarkEmixSequenceUserCreated_Object = MibTableColumn
cienaCesBenchmarkEmixSequenceUserCreated = _CienaCesBenchmarkEmixSequenceUserCreated_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 4, 1, 6),
    _CienaCesBenchmarkEmixSequenceUserCreated_Type()
)
cienaCesBenchmarkEmixSequenceUserCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixSequenceUserCreated.setStatus("current")
_CienaCesBenchmarkEmixSequenceRowStatus_Type = RowStatus
_CienaCesBenchmarkEmixSequenceRowStatus_Object = MibTableColumn
cienaCesBenchmarkEmixSequenceRowStatus = _CienaCesBenchmarkEmixSequenceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 4, 1, 7),
    _CienaCesBenchmarkEmixSequenceRowStatus_Type()
)
cienaCesBenchmarkEmixSequenceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixSequenceRowStatus.setStatus("current")
_CienaCesBenchmarkEmixFrameSizeTable_Object = MibTable
cienaCesBenchmarkEmixFrameSizeTable = _CienaCesBenchmarkEmixFrameSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixFrameSizeTable.setStatus("current")
_CienaCesBenchmarkEmixFrameSizeEntry_Object = MibTableRow
cienaCesBenchmarkEmixFrameSizeEntry = _CienaCesBenchmarkEmixFrameSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 5, 1)
)
cienaCesBenchmarkEmixFrameSizeEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEntityEntryId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEmixSequenceId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEmixFrameSizeIndex"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixFrameSizeEntry.setStatus("current")


class _CienaCesBenchmarkEmixFrameSizeIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkEmixFrameSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CienaCesBenchmarkEmixFrameSizeIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkEmixFrameSizeIndex_Object = MibTableColumn
cienaCesBenchmarkEmixFrameSizeIndex = _CienaCesBenchmarkEmixFrameSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 5, 1, 1),
    _CienaCesBenchmarkEmixFrameSizeIndex_Type()
)
cienaCesBenchmarkEmixFrameSizeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixFrameSizeIndex.setStatus("current")


class _CienaCesBenchmarkEmixFrameSizeEntryFrameSize_Type(Integer32):
    """Custom type cienaCesBenchmarkEmixFrameSizeEntryFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9216),
    )


_CienaCesBenchmarkEmixFrameSizeEntryFrameSize_Type.__name__ = "Integer32"
_CienaCesBenchmarkEmixFrameSizeEntryFrameSize_Object = MibTableColumn
cienaCesBenchmarkEmixFrameSizeEntryFrameSize = _CienaCesBenchmarkEmixFrameSizeEntryFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 5, 1, 2),
    _CienaCesBenchmarkEmixFrameSizeEntryFrameSize_Type()
)
cienaCesBenchmarkEmixFrameSizeEntryFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixFrameSizeEntryFrameSize.setStatus("current")
_CienaCesBenchmarkEmixAvgFrameSizeTable_Object = MibTable
cienaCesBenchmarkEmixAvgFrameSizeTable = _CienaCesBenchmarkEmixAvgFrameSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixAvgFrameSizeTable.setStatus("current")
_CienaCesBenchmarkEmixAvgFrameSizeEntry_Object = MibTableRow
cienaCesBenchmarkEmixAvgFrameSizeEntry = _CienaCesBenchmarkEmixAvgFrameSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 6, 1)
)
cienaCesBenchmarkEmixAvgFrameSizeEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEntityEntryId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEmixSequenceId"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixAvgFrameSizeEntry.setStatus("current")


class _CienaCesBenchmarkEmixAvgFrameSize_Type(Integer32):
    """Custom type cienaCesBenchmarkEmixAvgFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9216),
    )


_CienaCesBenchmarkEmixAvgFrameSize_Type.__name__ = "Integer32"
_CienaCesBenchmarkEmixAvgFrameSize_Object = MibTableColumn
cienaCesBenchmarkEmixAvgFrameSize = _CienaCesBenchmarkEmixAvgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 6, 1, 1),
    _CienaCesBenchmarkEmixAvgFrameSize_Type()
)
cienaCesBenchmarkEmixAvgFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixAvgFrameSize.setStatus("current")
_CienaCesBenchmarkKpiProfileTable_Object = MibTable
cienaCesBenchmarkKpiProfileTable = _CienaCesBenchmarkKpiProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiProfileTable.setStatus("current")
_CienaCesBenchmarkKpiProfileEntry_Object = MibTableRow
cienaCesBenchmarkKpiProfileEntry = _CienaCesBenchmarkKpiProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 7, 1)
)
cienaCesBenchmarkKpiProfileEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiProfileId"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiProfileEntry.setStatus("current")


class _CienaCesBenchmarkKpiProfileId_Type(Integer32):
    """Custom type cienaCesBenchmarkKpiProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CienaCesBenchmarkKpiProfileId_Type.__name__ = "Integer32"
_CienaCesBenchmarkKpiProfileId_Object = MibTableColumn
cienaCesBenchmarkKpiProfileId = _CienaCesBenchmarkKpiProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 7, 1, 1),
    _CienaCesBenchmarkKpiProfileId_Type()
)
cienaCesBenchmarkKpiProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiProfileId.setStatus("current")


class _CienaCesBenchmarkKpiProfileName_Type(DisplayString):
    """Custom type cienaCesBenchmarkKpiProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 46),
    )


_CienaCesBenchmarkKpiProfileName_Type.__name__ = "DisplayString"
_CienaCesBenchmarkKpiProfileName_Object = MibTableColumn
cienaCesBenchmarkKpiProfileName = _CienaCesBenchmarkKpiProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 7, 1, 2),
    _CienaCesBenchmarkKpiProfileName_Type()
)
cienaCesBenchmarkKpiProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiProfileName.setStatus("current")
_CienaCesBenchmarkKpiProfileNumOfRef_Type = Integer32
_CienaCesBenchmarkKpiProfileNumOfRef_Object = MibTableColumn
cienaCesBenchmarkKpiProfileNumOfRef = _CienaCesBenchmarkKpiProfileNumOfRef_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 7, 1, 3),
    _CienaCesBenchmarkKpiProfileNumOfRef_Type()
)
cienaCesBenchmarkKpiProfileNumOfRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiProfileNumOfRef.setStatus("current")
_CienaCesBenchmarkKpiProfileRowStatus_Type = RowStatus
_CienaCesBenchmarkKpiProfileRowStatus_Object = MibTableColumn
cienaCesBenchmarkKpiProfileRowStatus = _CienaCesBenchmarkKpiProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 7, 1, 4),
    _CienaCesBenchmarkKpiProfileRowStatus_Type()
)
cienaCesBenchmarkKpiProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiProfileRowStatus.setStatus("current")
_CienaCesBenchmarkKpiPcpColorTable_Object = MibTable
cienaCesBenchmarkKpiPcpColorTable = _CienaCesBenchmarkKpiPcpColorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiPcpColorTable.setStatus("current")
_CienaCesBenchmarkKpiPcpColorEntry_Object = MibTableRow
cienaCesBenchmarkKpiPcpColorEntry = _CienaCesBenchmarkKpiPcpColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 8, 1)
)
cienaCesBenchmarkKpiPcpColorEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiProfileId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiPcpIndex"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiColorIndex"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiPcpColorEntry.setStatus("current")


class _CienaCesBenchmarkKpiPcpIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkKpiPcpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesBenchmarkKpiPcpIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkKpiPcpIndex_Object = MibTableColumn
cienaCesBenchmarkKpiPcpIndex = _CienaCesBenchmarkKpiPcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 8, 1, 1),
    _CienaCesBenchmarkKpiPcpIndex_Type()
)
cienaCesBenchmarkKpiPcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiPcpIndex.setStatus("current")


class _CienaCesBenchmarkKpiColorIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkKpiColorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CienaCesBenchmarkKpiColorIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkKpiColorIndex_Object = MibTableColumn
cienaCesBenchmarkKpiColorIndex = _CienaCesBenchmarkKpiColorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 8, 1, 2),
    _CienaCesBenchmarkKpiColorIndex_Type()
)
cienaCesBenchmarkKpiColorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiColorIndex.setStatus("current")


class _CienaCesBenchmarkKpiPcp_Type(Integer32):
    """Custom type cienaCesBenchmarkKpiPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesBenchmarkKpiPcp_Type.__name__ = "Integer32"
_CienaCesBenchmarkKpiPcp_Object = MibTableColumn
cienaCesBenchmarkKpiPcp = _CienaCesBenchmarkKpiPcp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 8, 1, 3),
    _CienaCesBenchmarkKpiPcp_Type()
)
cienaCesBenchmarkKpiPcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiPcp.setStatus("current")
_CienaCesBenchmarkKpiColor_Type = CienaCesBenchmarkColorTest
_CienaCesBenchmarkKpiColor_Object = MibTableColumn
cienaCesBenchmarkKpiColor = _CienaCesBenchmarkKpiColor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 8, 1, 4),
    _CienaCesBenchmarkKpiColor_Type()
)
cienaCesBenchmarkKpiColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiColor.setStatus("current")
_CienaCesBenchmarkKpiThroughput_Type = CienaCesBenchmarkThroughputKpiPercent
_CienaCesBenchmarkKpiThroughput_Object = MibTableColumn
cienaCesBenchmarkKpiThroughput = _CienaCesBenchmarkKpiThroughput_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 8, 1, 5),
    _CienaCesBenchmarkKpiThroughput_Type()
)
cienaCesBenchmarkKpiThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiThroughput.setStatus("current")
_CienaCesBenchmarkKpiFrameloss_Type = CienaCesBenchmarkFramelossKpiPercent
_CienaCesBenchmarkKpiFrameloss_Object = MibTableColumn
cienaCesBenchmarkKpiFrameloss = _CienaCesBenchmarkKpiFrameloss_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 8, 1, 6),
    _CienaCesBenchmarkKpiFrameloss_Type()
)
cienaCesBenchmarkKpiFrameloss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiFrameloss.setStatus("current")
_CienaCesBenchmarkKpiLatency_Type = Integer32
_CienaCesBenchmarkKpiLatency_Object = MibTableColumn
cienaCesBenchmarkKpiLatency = _CienaCesBenchmarkKpiLatency_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 8, 1, 7),
    _CienaCesBenchmarkKpiLatency_Type()
)
cienaCesBenchmarkKpiLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiLatency.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiLatency.setUnits("microseconds")
_CienaCesBenchmarkKpiPdv_Type = Integer32
_CienaCesBenchmarkKpiPdv_Object = MibTableColumn
cienaCesBenchmarkKpiPdv = _CienaCesBenchmarkKpiPdv_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 8, 1, 8),
    _CienaCesBenchmarkKpiPdv_Type()
)
cienaCesBenchmarkKpiPdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiPdv.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesBenchmarkKpiPdv.setUnits("microseconds")
_CienaCesBenchmarkBwAllocProfileTable_Object = MibTable
cienaCesBenchmarkBwAllocProfileTable = _CienaCesBenchmarkBwAllocProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkBwAllocProfileTable.setStatus("current")
_CienaCesBenchmarkBwAllocProfileEntry_Object = MibTableRow
cienaCesBenchmarkBwAllocProfileEntry = _CienaCesBenchmarkBwAllocProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 9, 1)
)
cienaCesBenchmarkBwAllocProfileEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkBwAllocProfileId"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkBwAllocProfileEntry.setStatus("current")


class _CienaCesBenchmarkBwAllocProfileId_Type(Integer32):
    """Custom type cienaCesBenchmarkBwAllocProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CienaCesBenchmarkBwAllocProfileId_Type.__name__ = "Integer32"
_CienaCesBenchmarkBwAllocProfileId_Object = MibTableColumn
cienaCesBenchmarkBwAllocProfileId = _CienaCesBenchmarkBwAllocProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 9, 1, 1),
    _CienaCesBenchmarkBwAllocProfileId_Type()
)
cienaCesBenchmarkBwAllocProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkBwAllocProfileId.setStatus("current")


class _CienaCesBenchmarkBwAllocProfileName_Type(DisplayString):
    """Custom type cienaCesBenchmarkBwAllocProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 46),
    )


_CienaCesBenchmarkBwAllocProfileName_Type.__name__ = "DisplayString"
_CienaCesBenchmarkBwAllocProfileName_Object = MibTableColumn
cienaCesBenchmarkBwAllocProfileName = _CienaCesBenchmarkBwAllocProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 9, 1, 2),
    _CienaCesBenchmarkBwAllocProfileName_Type()
)
cienaCesBenchmarkBwAllocProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkBwAllocProfileName.setStatus("current")
_CienaCesBenchmarkBwAllocProfileNumOfRef_Type = Integer32
_CienaCesBenchmarkBwAllocProfileNumOfRef_Object = MibTableColumn
cienaCesBenchmarkBwAllocProfileNumOfRef = _CienaCesBenchmarkBwAllocProfileNumOfRef_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 9, 1, 3),
    _CienaCesBenchmarkBwAllocProfileNumOfRef_Type()
)
cienaCesBenchmarkBwAllocProfileNumOfRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkBwAllocProfileNumOfRef.setStatus("current")
_CienaCesBenchmarkBwAllocProfileRowStatus_Type = RowStatus
_CienaCesBenchmarkBwAllocProfileRowStatus_Object = MibTableColumn
cienaCesBenchmarkBwAllocProfileRowStatus = _CienaCesBenchmarkBwAllocProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 9, 1, 4),
    _CienaCesBenchmarkBwAllocProfileRowStatus_Type()
)
cienaCesBenchmarkBwAllocProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkBwAllocProfileRowStatus.setStatus("current")
_CienaCesBenchmarkBwRatioTable_Object = MibTable
cienaCesBenchmarkBwRatioTable = _CienaCesBenchmarkBwRatioTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkBwRatioTable.setStatus("current")
_CienaCesBenchmarkBwRatioEntry_Object = MibTableRow
cienaCesBenchmarkBwRatioEntry = _CienaCesBenchmarkBwRatioEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 10, 1)
)
cienaCesBenchmarkBwRatioEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkBwAllocProfileId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkBwRatioPcpIndex"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkBwRatioEntry.setStatus("current")


class _CienaCesBenchmarkBwRatioPcpIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkBwRatioPcpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesBenchmarkBwRatioPcpIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkBwRatioPcpIndex_Object = MibTableColumn
cienaCesBenchmarkBwRatioPcpIndex = _CienaCesBenchmarkBwRatioPcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 10, 1, 1),
    _CienaCesBenchmarkBwRatioPcpIndex_Type()
)
cienaCesBenchmarkBwRatioPcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkBwRatioPcpIndex.setStatus("current")


class _CienaCesBenchmarkBwRatioPcp_Type(Integer32):
    """Custom type cienaCesBenchmarkBwRatioPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesBenchmarkBwRatioPcp_Type.__name__ = "Integer32"
_CienaCesBenchmarkBwRatioPcp_Object = MibTableColumn
cienaCesBenchmarkBwRatioPcp = _CienaCesBenchmarkBwRatioPcp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 10, 1, 2),
    _CienaCesBenchmarkBwRatioPcp_Type()
)
cienaCesBenchmarkBwRatioPcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkBwRatioPcp.setStatus("current")


class _CienaCesBenchmarkBwRatio_Type(Integer32):
    """Custom type cienaCesBenchmarkBwRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CienaCesBenchmarkBwRatio_Type.__name__ = "Integer32"
_CienaCesBenchmarkBwRatio_Object = MibTableColumn
cienaCesBenchmarkBwRatio = _CienaCesBenchmarkBwRatio_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 10, 1, 3),
    _CienaCesBenchmarkBwRatio_Type()
)
cienaCesBenchmarkBwRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesBenchmarkBwRatio.setStatus("current")
_CienaCesBenchmarkProfileTable_Object = MibTable
cienaCesBenchmarkProfileTable = _CienaCesBenchmarkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileTable.setStatus("current")
_CienaCesBenchmarkProfileEntry_Object = MibTableRow
cienaCesBenchmarkProfileEntry = _CienaCesBenchmarkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1)
)
cienaCesBenchmarkProfileEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkProfileEntryId"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntry.setStatus("current")
_CienaCesBenchmarkProfileEntryId_Type = Integer32
_CienaCesBenchmarkProfileEntryId_Object = MibTableColumn
cienaCesBenchmarkProfileEntryId = _CienaCesBenchmarkProfileEntryId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 1),
    _CienaCesBenchmarkProfileEntryId_Type()
)
cienaCesBenchmarkProfileEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryId.setStatus("current")


class _CienaCesBenchmarkProfileEntryName_Type(DisplayString):
    """Custom type cienaCesBenchmarkProfileEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 46),
    )


_CienaCesBenchmarkProfileEntryName_Type.__name__ = "DisplayString"
_CienaCesBenchmarkProfileEntryName_Object = MibTableColumn
cienaCesBenchmarkProfileEntryName = _CienaCesBenchmarkProfileEntryName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 2),
    _CienaCesBenchmarkProfileEntryName_Type()
)
cienaCesBenchmarkProfileEntryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryName.setStatus("current")


class _CienaCesBenchmarkProfileEntryBandwidth_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CienaCesBenchmarkProfileEntryBandwidth_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryBandwidth_Object = MibTableColumn
cienaCesBenchmarkProfileEntryBandwidth = _CienaCesBenchmarkProfileEntryBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 3),
    _CienaCesBenchmarkProfileEntryBandwidth_Type()
)
cienaCesBenchmarkProfileEntryBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryBandwidth.setStatus("current")


class _CienaCesBenchmarkProfileEntryExcessBandwidth_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryExcessBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CienaCesBenchmarkProfileEntryExcessBandwidth_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryExcessBandwidth_Object = MibTableColumn
cienaCesBenchmarkProfileEntryExcessBandwidth = _CienaCesBenchmarkProfileEntryExcessBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 4),
    _CienaCesBenchmarkProfileEntryExcessBandwidth_Type()
)
cienaCesBenchmarkProfileEntryExcessBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryExcessBandwidth.setStatus("current")


class _CienaCesBenchmarkProfileEntryInterval_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryInterval based on Integer32"""
    defaultValue = 4

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
        *(("t15min", 1),
          ("t1hr", 2),
          ("t6hr", 3),
          ("tCompletion", 4),
          ("t2hr", 5))
    )


_CienaCesBenchmarkProfileEntryInterval_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryInterval_Object = MibTableColumn
cienaCesBenchmarkProfileEntryInterval = _CienaCesBenchmarkProfileEntryInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 5),
    _CienaCesBenchmarkProfileEntryInterval_Type()
)
cienaCesBenchmarkProfileEntryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryInterval.setStatus("current")


class _CienaCesBenchmarkProfileEntryDuration_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryDuration based on Integer32"""
    defaultValue = 6

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
        *(("t15min", 1),
          ("t1hr", 2),
          ("t6hr", 3),
          ("t24hr", 4),
          ("tIndefinite", 5),
          ("tOnce", 6))
    )


_CienaCesBenchmarkProfileEntryDuration_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryDuration_Object = MibTableColumn
cienaCesBenchmarkProfileEntryDuration = _CienaCesBenchmarkProfileEntryDuration_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 6),
    _CienaCesBenchmarkProfileEntryDuration_Type()
)
cienaCesBenchmarkProfileEntryDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryDuration.setStatus("current")


class _CienaCesBenchmarkProfileEntrySetFrameSizeList_Type(DisplayString):
    """Custom type cienaCesBenchmarkProfileEntrySetFrameSizeList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CienaCesBenchmarkProfileEntrySetFrameSizeList_Type.__name__ = "DisplayString"
_CienaCesBenchmarkProfileEntrySetFrameSizeList_Object = MibTableColumn
cienaCesBenchmarkProfileEntrySetFrameSizeList = _CienaCesBenchmarkProfileEntrySetFrameSizeList_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 7),
    _CienaCesBenchmarkProfileEntrySetFrameSizeList_Type()
)
cienaCesBenchmarkProfileEntrySetFrameSizeList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntrySetFrameSizeList.setStatus("current")


class _CienaCesBenchmarkProfileEntryMaxSearches_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryMaxSearches based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CienaCesBenchmarkProfileEntryMaxSearches_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryMaxSearches_Object = MibTableColumn
cienaCesBenchmarkProfileEntryMaxSearches = _CienaCesBenchmarkProfileEntryMaxSearches_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 8),
    _CienaCesBenchmarkProfileEntryMaxSearches_Type()
)
cienaCesBenchmarkProfileEntryMaxSearches.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryMaxSearches.setStatus("current")


class _CienaCesBenchmarkProfileEntryMaxSamples_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryMaxSamples based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 20),
    )


_CienaCesBenchmarkProfileEntryMaxSamples_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryMaxSamples_Object = MibTableColumn
cienaCesBenchmarkProfileEntryMaxSamples = _CienaCesBenchmarkProfileEntryMaxSamples_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 9),
    _CienaCesBenchmarkProfileEntryMaxSamples_Type()
)
cienaCesBenchmarkProfileEntryMaxSamples.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryMaxSamples.setStatus("current")


class _CienaCesBenchmarkProfileEntrySamplingInterval_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntrySamplingInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CienaCesBenchmarkProfileEntrySamplingInterval_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntrySamplingInterval_Object = MibTableColumn
cienaCesBenchmarkProfileEntrySamplingInterval = _CienaCesBenchmarkProfileEntrySamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 10),
    _CienaCesBenchmarkProfileEntrySamplingInterval_Type()
)
cienaCesBenchmarkProfileEntrySamplingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntrySamplingInterval.setStatus("current")


class _CienaCesBenchmarkProfileEntryFrameLossStartBw_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryFrameLossStartBw based on Integer32"""
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
        *(("profileBandwidth", 1),
          ("maximumThroughput", 2),
          ("maximumLineRate", 3))
    )


_CienaCesBenchmarkProfileEntryFrameLossStartBw_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryFrameLossStartBw_Object = MibTableColumn
cienaCesBenchmarkProfileEntryFrameLossStartBw = _CienaCesBenchmarkProfileEntryFrameLossStartBw_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 11),
    _CienaCesBenchmarkProfileEntryFrameLossStartBw_Type()
)
cienaCesBenchmarkProfileEntryFrameLossStartBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryFrameLossStartBw.setStatus("current")


class _CienaCesBenchmarkProfileEntryVidValidation_Type(TruthValue):
    """Custom type cienaCesBenchmarkProfileEntryVidValidation based on TruthValue"""
    defaultValue = 1


_CienaCesBenchmarkProfileEntryVidValidation_Type.__name__ = "TruthValue"
_CienaCesBenchmarkProfileEntryVidValidation_Object = MibTableColumn
cienaCesBenchmarkProfileEntryVidValidation = _CienaCesBenchmarkProfileEntryVidValidation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 12),
    _CienaCesBenchmarkProfileEntryVidValidation_Type()
)
cienaCesBenchmarkProfileEntryVidValidation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryVidValidation.setStatus("current")


class _CienaCesBenchmarkProfileEntryPcpValidation_Type(TruthValue):
    """Custom type cienaCesBenchmarkProfileEntryPcpValidation based on TruthValue"""
    defaultValue = 1


_CienaCesBenchmarkProfileEntryPcpValidation_Type.__name__ = "TruthValue"
_CienaCesBenchmarkProfileEntryPcpValidation_Object = MibTableColumn
cienaCesBenchmarkProfileEntryPcpValidation = _CienaCesBenchmarkProfileEntryPcpValidation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 13),
    _CienaCesBenchmarkProfileEntryPcpValidation_Type()
)
cienaCesBenchmarkProfileEntryPcpValidation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryPcpValidation.setStatus("current")


class _CienaCesBenchmarkProfileEntryColorValidation_Type(TruthValue):
    """Custom type cienaCesBenchmarkProfileEntryColorValidation based on TruthValue"""
    defaultValue = 1


_CienaCesBenchmarkProfileEntryColorValidation_Type.__name__ = "TruthValue"
_CienaCesBenchmarkProfileEntryColorValidation_Object = MibTableColumn
cienaCesBenchmarkProfileEntryColorValidation = _CienaCesBenchmarkProfileEntryColorValidation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 14),
    _CienaCesBenchmarkProfileEntryColorValidation_Type()
)
cienaCesBenchmarkProfileEntryColorValidation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryColorValidation.setStatus("current")


class _CienaCesBenchmarkProfileEntryKpiProfileId_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryKpiProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CienaCesBenchmarkProfileEntryKpiProfileId_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryKpiProfileId_Object = MibTableColumn
cienaCesBenchmarkProfileEntryKpiProfileId = _CienaCesBenchmarkProfileEntryKpiProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 15),
    _CienaCesBenchmarkProfileEntryKpiProfileId_Type()
)
cienaCesBenchmarkProfileEntryKpiProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryKpiProfileId.setStatus("current")


class _CienaCesBenchmarkProfileEntryBwAllocProfileId_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryBwAllocProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CienaCesBenchmarkProfileEntryBwAllocProfileId_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryBwAllocProfileId_Object = MibTableColumn
cienaCesBenchmarkProfileEntryBwAllocProfileId = _CienaCesBenchmarkProfileEntryBwAllocProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 16),
    _CienaCesBenchmarkProfileEntryBwAllocProfileId_Type()
)
cienaCesBenchmarkProfileEntryBwAllocProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryBwAllocProfileId.setStatus("current")


class _CienaCesBenchmarkProfileEntryEmixSequenceId_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryEmixSequenceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CienaCesBenchmarkProfileEntryEmixSequenceId_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryEmixSequenceId_Object = MibTableColumn
cienaCesBenchmarkProfileEntryEmixSequenceId = _CienaCesBenchmarkProfileEntryEmixSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 17),
    _CienaCesBenchmarkProfileEntryEmixSequenceId_Type()
)
cienaCesBenchmarkProfileEntryEmixSequenceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryEmixSequenceId.setStatus("current")


class _CienaCesBenchmarkProfileEntryEncapType_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryEncapType based on Integer32"""
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
        *(("untagged", 1),
          ("dot1q", 2),
          ("qinq", 3))
    )


_CienaCesBenchmarkProfileEntryEncapType_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryEncapType_Object = MibTableColumn
cienaCesBenchmarkProfileEntryEncapType = _CienaCesBenchmarkProfileEntryEncapType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 18),
    _CienaCesBenchmarkProfileEntryEncapType_Type()
)
cienaCesBenchmarkProfileEntryEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryEncapType.setStatus("current")


class _CienaCesBenchmarkProfileEntryPduType_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryPduType based on Integer32"""
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
        *(("ethernet", 1),
          ("ip", 2),
          ("udpecho", 3))
    )


_CienaCesBenchmarkProfileEntryPduType_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryPduType_Object = MibTableColumn
cienaCesBenchmarkProfileEntryPduType = _CienaCesBenchmarkProfileEntryPduType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 19),
    _CienaCesBenchmarkProfileEntryPduType_Type()
)
cienaCesBenchmarkProfileEntryPduType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryPduType.setStatus("current")
_CienaCesBenchmarkProfileEntryDstmac_Type = MacAddress
_CienaCesBenchmarkProfileEntryDstmac_Object = MibTableColumn
cienaCesBenchmarkProfileEntryDstmac = _CienaCesBenchmarkProfileEntryDstmac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 20),
    _CienaCesBenchmarkProfileEntryDstmac_Type()
)
cienaCesBenchmarkProfileEntryDstmac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryDstmac.setStatus("current")


class _CienaCesBenchmarkProfileEntrySVid_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntrySVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CienaCesBenchmarkProfileEntrySVid_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntrySVid_Object = MibTableColumn
cienaCesBenchmarkProfileEntrySVid = _CienaCesBenchmarkProfileEntrySVid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 21),
    _CienaCesBenchmarkProfileEntrySVid_Type()
)
cienaCesBenchmarkProfileEntrySVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntrySVid.setStatus("current")
_CienaCesBenchmarkProfileEntrySPcp_Type = CienaCesBenchmarkPcpBitmap
_CienaCesBenchmarkProfileEntrySPcp_Object = MibTableColumn
cienaCesBenchmarkProfileEntrySPcp = _CienaCesBenchmarkProfileEntrySPcp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 22),
    _CienaCesBenchmarkProfileEntrySPcp_Type()
)
cienaCesBenchmarkProfileEntrySPcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntrySPcp.setStatus("current")
_CienaCesBenchmarkProfileEntrySColor_Type = CienaCesBenchmarkColorTest
_CienaCesBenchmarkProfileEntrySColor_Object = MibTableColumn
cienaCesBenchmarkProfileEntrySColor = _CienaCesBenchmarkProfileEntrySColor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 23),
    _CienaCesBenchmarkProfileEntrySColor_Type()
)
cienaCesBenchmarkProfileEntrySColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntrySColor.setStatus("current")


class _CienaCesBenchmarkProfileEntryCVid_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryCVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CienaCesBenchmarkProfileEntryCVid_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryCVid_Object = MibTableColumn
cienaCesBenchmarkProfileEntryCVid = _CienaCesBenchmarkProfileEntryCVid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 24),
    _CienaCesBenchmarkProfileEntryCVid_Type()
)
cienaCesBenchmarkProfileEntryCVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryCVid.setStatus("current")
_CienaCesBenchmarkProfileEntryCPcp_Type = CienaCesBenchmarkPcpBitmap
_CienaCesBenchmarkProfileEntryCPcp_Object = MibTableColumn
cienaCesBenchmarkProfileEntryCPcp = _CienaCesBenchmarkProfileEntryCPcp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 25),
    _CienaCesBenchmarkProfileEntryCPcp_Type()
)
cienaCesBenchmarkProfileEntryCPcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryCPcp.setStatus("current")
_CienaCesBenchmarkProfileEntryCColor_Type = CienaCesBenchmarkColorTest
_CienaCesBenchmarkProfileEntryCColor_Object = MibTableColumn
cienaCesBenchmarkProfileEntryCColor = _CienaCesBenchmarkProfileEntryCColor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 26),
    _CienaCesBenchmarkProfileEntryCColor_Type()
)
cienaCesBenchmarkProfileEntryCColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryCColor.setStatus("current")


class _CienaCesBenchmarkProfileEntryTpid_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryTpid based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesBenchmarkProfileEntryTpid_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryTpid_Object = MibTableColumn
cienaCesBenchmarkProfileEntryTpid = _CienaCesBenchmarkProfileEntryTpid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 27),
    _CienaCesBenchmarkProfileEntryTpid_Type()
)
cienaCesBenchmarkProfileEntryTpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryTpid.setStatus("current")


class _CienaCesBenchmarkProfileEntryDscp_Type(Integer32):
    """Custom type cienaCesBenchmarkProfileEntryDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CienaCesBenchmarkProfileEntryDscp_Type.__name__ = "Integer32"
_CienaCesBenchmarkProfileEntryDscp_Object = MibTableColumn
cienaCesBenchmarkProfileEntryDscp = _CienaCesBenchmarkProfileEntryDscp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 28),
    _CienaCesBenchmarkProfileEntryDscp_Type()
)
cienaCesBenchmarkProfileEntryDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryDscp.setStatus("current")
_CienaCesBenchmarkProfileEntrySrcInetAddrType_Type = InetAddressType
_CienaCesBenchmarkProfileEntrySrcInetAddrType_Object = MibTableColumn
cienaCesBenchmarkProfileEntrySrcInetAddrType = _CienaCesBenchmarkProfileEntrySrcInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 29),
    _CienaCesBenchmarkProfileEntrySrcInetAddrType_Type()
)
cienaCesBenchmarkProfileEntrySrcInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntrySrcInetAddrType.setStatus("current")
_CienaCesBenchmarkProfileEntrySrcInetAddr_Type = InetAddress
_CienaCesBenchmarkProfileEntrySrcInetAddr_Object = MibTableColumn
cienaCesBenchmarkProfileEntrySrcInetAddr = _CienaCesBenchmarkProfileEntrySrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 30),
    _CienaCesBenchmarkProfileEntrySrcInetAddr_Type()
)
cienaCesBenchmarkProfileEntrySrcInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntrySrcInetAddr.setStatus("current")
_CienaCesBenchmarkProfileEntryDstInetAddrType_Type = InetAddressType
_CienaCesBenchmarkProfileEntryDstInetAddrType_Object = MibTableColumn
cienaCesBenchmarkProfileEntryDstInetAddrType = _CienaCesBenchmarkProfileEntryDstInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 31),
    _CienaCesBenchmarkProfileEntryDstInetAddrType_Type()
)
cienaCesBenchmarkProfileEntryDstInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryDstInetAddrType.setStatus("current")
_CienaCesBenchmarkProfileEntryDstInetAddr_Type = InetAddress
_CienaCesBenchmarkProfileEntryDstInetAddr_Object = MibTableColumn
cienaCesBenchmarkProfileEntryDstInetAddr = _CienaCesBenchmarkProfileEntryDstInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 32),
    _CienaCesBenchmarkProfileEntryDstInetAddr_Type()
)
cienaCesBenchmarkProfileEntryDstInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryDstInetAddr.setStatus("current")


class _CienaCesBenchmarkProfileEntryCustomPayload_Type(OctetString):
    """Custom type cienaCesBenchmarkProfileEntryCustomPayload based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CienaCesBenchmarkProfileEntryCustomPayload_Type.__name__ = "OctetString"
_CienaCesBenchmarkProfileEntryCustomPayload_Object = MibTableColumn
cienaCesBenchmarkProfileEntryCustomPayload = _CienaCesBenchmarkProfileEntryCustomPayload_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 33),
    _CienaCesBenchmarkProfileEntryCustomPayload_Type()
)
cienaCesBenchmarkProfileEntryCustomPayload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryCustomPayload.setStatus("current")


class _CienaCesBenchmarkProfileEntryThroughputTest_Type(TruthValue):
    """Custom type cienaCesBenchmarkProfileEntryThroughputTest based on TruthValue"""
    defaultValue = 2


_CienaCesBenchmarkProfileEntryThroughputTest_Type.__name__ = "TruthValue"
_CienaCesBenchmarkProfileEntryThroughputTest_Object = MibTableColumn
cienaCesBenchmarkProfileEntryThroughputTest = _CienaCesBenchmarkProfileEntryThroughputTest_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 34),
    _CienaCesBenchmarkProfileEntryThroughputTest_Type()
)
cienaCesBenchmarkProfileEntryThroughputTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryThroughputTest.setStatus("current")


class _CienaCesBenchmarkProfileEntryFramelossTest_Type(TruthValue):
    """Custom type cienaCesBenchmarkProfileEntryFramelossTest based on TruthValue"""
    defaultValue = 2


_CienaCesBenchmarkProfileEntryFramelossTest_Type.__name__ = "TruthValue"
_CienaCesBenchmarkProfileEntryFramelossTest_Object = MibTableColumn
cienaCesBenchmarkProfileEntryFramelossTest = _CienaCesBenchmarkProfileEntryFramelossTest_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 35),
    _CienaCesBenchmarkProfileEntryFramelossTest_Type()
)
cienaCesBenchmarkProfileEntryFramelossTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryFramelossTest.setStatus("current")


class _CienaCesBenchmarkProfileEntryLatencyTest_Type(TruthValue):
    """Custom type cienaCesBenchmarkProfileEntryLatencyTest based on TruthValue"""
    defaultValue = 2


_CienaCesBenchmarkProfileEntryLatencyTest_Type.__name__ = "TruthValue"
_CienaCesBenchmarkProfileEntryLatencyTest_Object = MibTableColumn
cienaCesBenchmarkProfileEntryLatencyTest = _CienaCesBenchmarkProfileEntryLatencyTest_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 36),
    _CienaCesBenchmarkProfileEntryLatencyTest_Type()
)
cienaCesBenchmarkProfileEntryLatencyTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryLatencyTest.setStatus("current")


class _CienaCesBenchmarkProfileEntryPdvTest_Type(TruthValue):
    """Custom type cienaCesBenchmarkProfileEntryPdvTest based on TruthValue"""
    defaultValue = 2


_CienaCesBenchmarkProfileEntryPdvTest_Type.__name__ = "TruthValue"
_CienaCesBenchmarkProfileEntryPdvTest_Object = MibTableColumn
cienaCesBenchmarkProfileEntryPdvTest = _CienaCesBenchmarkProfileEntryPdvTest_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 37),
    _CienaCesBenchmarkProfileEntryPdvTest_Type()
)
cienaCesBenchmarkProfileEntryPdvTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryPdvTest.setStatus("current")
_CienaCesBenchmarkProfileEntryBurstTest_Type = TruthValue
_CienaCesBenchmarkProfileEntryBurstTest_Object = MibTableColumn
cienaCesBenchmarkProfileEntryBurstTest = _CienaCesBenchmarkProfileEntryBurstTest_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 38),
    _CienaCesBenchmarkProfileEntryBurstTest_Type()
)
cienaCesBenchmarkProfileEntryBurstTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryBurstTest.setStatus("current")


class _CienaCesBenchmarkProfileEntryRfc2544Suite_Type(TruthValue):
    """Custom type cienaCesBenchmarkProfileEntryRfc2544Suite based on TruthValue"""
    defaultValue = 2


_CienaCesBenchmarkProfileEntryRfc2544Suite_Type.__name__ = "TruthValue"
_CienaCesBenchmarkProfileEntryRfc2544Suite_Object = MibTableColumn
cienaCesBenchmarkProfileEntryRfc2544Suite = _CienaCesBenchmarkProfileEntryRfc2544Suite_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 39),
    _CienaCesBenchmarkProfileEntryRfc2544Suite_Type()
)
cienaCesBenchmarkProfileEntryRfc2544Suite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryRfc2544Suite.setStatus("current")


class _CienaCesBenchmarkProfileEntryY1564Test_Type(TruthValue):
    """Custom type cienaCesBenchmarkProfileEntryY1564Test based on TruthValue"""
    defaultValue = 2


_CienaCesBenchmarkProfileEntryY1564Test_Type.__name__ = "TruthValue"
_CienaCesBenchmarkProfileEntryY1564Test_Object = MibTableColumn
cienaCesBenchmarkProfileEntryY1564Test = _CienaCesBenchmarkProfileEntryY1564Test_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 40),
    _CienaCesBenchmarkProfileEntryY1564Test_Type()
)
cienaCesBenchmarkProfileEntryY1564Test.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryY1564Test.setStatus("current")
_CienaCesBenchmarkProfileEntryHwSessionsRequired_Type = Integer32
_CienaCesBenchmarkProfileEntryHwSessionsRequired_Object = MibTableColumn
cienaCesBenchmarkProfileEntryHwSessionsRequired = _CienaCesBenchmarkProfileEntryHwSessionsRequired_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 41),
    _CienaCesBenchmarkProfileEntryHwSessionsRequired_Type()
)
cienaCesBenchmarkProfileEntryHwSessionsRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryHwSessionsRequired.setStatus("current")
_CienaCesBenchmarkProfileEntryNumOfRef_Type = Integer32
_CienaCesBenchmarkProfileEntryNumOfRef_Object = MibTableColumn
cienaCesBenchmarkProfileEntryNumOfRef = _CienaCesBenchmarkProfileEntryNumOfRef_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 42),
    _CienaCesBenchmarkProfileEntryNumOfRef_Type()
)
cienaCesBenchmarkProfileEntryNumOfRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryNumOfRef.setStatus("current")
_CienaCesBenchmarkProfileEntryRowStatus_Type = RowStatus
_CienaCesBenchmarkProfileEntryRowStatus_Object = MibTableColumn
cienaCesBenchmarkProfileEntryRowStatus = _CienaCesBenchmarkProfileEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 11, 1, 43),
    _CienaCesBenchmarkProfileEntryRowStatus_Type()
)
cienaCesBenchmarkProfileEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkProfileEntryRowStatus.setStatus("current")
_CienaCesBenchmarkTestInstanceTable_Object = MibTable
cienaCesBenchmarkTestInstanceTable = _CienaCesBenchmarkTestInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceTable.setStatus("current")
_CienaCesBenchmarkTestInstanceEntry_Object = MibTableRow
cienaCesBenchmarkTestInstanceEntry = _CienaCesBenchmarkTestInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1)
)
cienaCesBenchmarkTestInstanceEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntry.setStatus("current")
_CienaCesBenchmarkTestInstanceEntryId_Type = Integer32
_CienaCesBenchmarkTestInstanceEntryId_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntryId = _CienaCesBenchmarkTestInstanceEntryId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 1),
    _CienaCesBenchmarkTestInstanceEntryId_Type()
)
cienaCesBenchmarkTestInstanceEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntryId.setStatus("current")


class _CienaCesBenchmarkTestInstanceEntryName_Type(DisplayString):
    """Custom type cienaCesBenchmarkTestInstanceEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 46),
    )


_CienaCesBenchmarkTestInstanceEntryName_Type.__name__ = "DisplayString"
_CienaCesBenchmarkTestInstanceEntryName_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntryName = _CienaCesBenchmarkTestInstanceEntryName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 2),
    _CienaCesBenchmarkTestInstanceEntryName_Type()
)
cienaCesBenchmarkTestInstanceEntryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntryName.setStatus("current")
_CienaCesBenchmarkTestInstanceEntrySubPortId_Type = Integer32
_CienaCesBenchmarkTestInstanceEntrySubPortId_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntrySubPortId = _CienaCesBenchmarkTestInstanceEntrySubPortId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 3),
    _CienaCesBenchmarkTestInstanceEntrySubPortId_Type()
)
cienaCesBenchmarkTestInstanceEntrySubPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntrySubPortId.setStatus("current")
_CienaCesBenchmarkTestInstanceEntryProfileId_Type = Integer32
_CienaCesBenchmarkTestInstanceEntryProfileId_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntryProfileId = _CienaCesBenchmarkTestInstanceEntryProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 4),
    _CienaCesBenchmarkTestInstanceEntryProfileId_Type()
)
cienaCesBenchmarkTestInstanceEntryProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntryProfileId.setStatus("current")
_CienaCesBenchmarkTestInstanceEntrySvid_Type = Integer32
_CienaCesBenchmarkTestInstanceEntrySvid_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntrySvid = _CienaCesBenchmarkTestInstanceEntrySvid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 5),
    _CienaCesBenchmarkTestInstanceEntrySvid_Type()
)
cienaCesBenchmarkTestInstanceEntrySvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntrySvid.setStatus("current")
_CienaCesBenchmarkTestInstanceEntryCvid_Type = Integer32
_CienaCesBenchmarkTestInstanceEntryCvid_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntryCvid = _CienaCesBenchmarkTestInstanceEntryCvid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 6),
    _CienaCesBenchmarkTestInstanceEntryCvid_Type()
)
cienaCesBenchmarkTestInstanceEntryCvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntryCvid.setStatus("current")
_CienaCesBenchmarkTestInstanceEntryUntagged_Type = TruthValue
_CienaCesBenchmarkTestInstanceEntryUntagged_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntryUntagged = _CienaCesBenchmarkTestInstanceEntryUntagged_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 7),
    _CienaCesBenchmarkTestInstanceEntryUntagged_Type()
)
cienaCesBenchmarkTestInstanceEntryUntagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntryUntagged.setStatus("current")
_CienaCesBenchmarkTestInstanceEntryDstMac_Type = MacAddress
_CienaCesBenchmarkTestInstanceEntryDstMac_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntryDstMac = _CienaCesBenchmarkTestInstanceEntryDstMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 8),
    _CienaCesBenchmarkTestInstanceEntryDstMac_Type()
)
cienaCesBenchmarkTestInstanceEntryDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntryDstMac.setStatus("current")
_CienaCesBenchmarkTestInstanceEntryAdminState_Type = CienaCesBenchmarkAdminState
_CienaCesBenchmarkTestInstanceEntryAdminState_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntryAdminState = _CienaCesBenchmarkTestInstanceEntryAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 9),
    _CienaCesBenchmarkTestInstanceEntryAdminState_Type()
)
cienaCesBenchmarkTestInstanceEntryAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntryAdminState.setStatus("current")
_CienaCesBenchmarkTestInstanceEntryStarted_Type = TruthValue
_CienaCesBenchmarkTestInstanceEntryStarted_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntryStarted = _CienaCesBenchmarkTestInstanceEntryStarted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 10),
    _CienaCesBenchmarkTestInstanceEntryStarted_Type()
)
cienaCesBenchmarkTestInstanceEntryStarted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntryStarted.setStatus("current")
_CienaCesBenchmarkTestInstanceEntryCurrentInterval_Type = Integer32
_CienaCesBenchmarkTestInstanceEntryCurrentInterval_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntryCurrentInterval = _CienaCesBenchmarkTestInstanceEntryCurrentInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 11),
    _CienaCesBenchmarkTestInstanceEntryCurrentInterval_Type()
)
cienaCesBenchmarkTestInstanceEntryCurrentInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntryCurrentInterval.setStatus("current")
_CienaCesBenchmarkTestInstanceEntryTotalIntervals_Type = Integer32
_CienaCesBenchmarkTestInstanceEntryTotalIntervals_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntryTotalIntervals = _CienaCesBenchmarkTestInstanceEntryTotalIntervals_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 12),
    _CienaCesBenchmarkTestInstanceEntryTotalIntervals_Type()
)
cienaCesBenchmarkTestInstanceEntryTotalIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntryTotalIntervals.setStatus("current")
_CienaCesBenchmarkTestInstanceEntryLastIterStart_Type = DateAndTime
_CienaCesBenchmarkTestInstanceEntryLastIterStart_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntryLastIterStart = _CienaCesBenchmarkTestInstanceEntryLastIterStart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 13),
    _CienaCesBenchmarkTestInstanceEntryLastIterStart_Type()
)
cienaCesBenchmarkTestInstanceEntryLastIterStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntryLastIterStart.setStatus("current")
_CienaCesBenchmarkTestInstanceEntryClearStats_Type = TruthValue
_CienaCesBenchmarkTestInstanceEntryClearStats_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntryClearStats = _CienaCesBenchmarkTestInstanceEntryClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 14),
    _CienaCesBenchmarkTestInstanceEntryClearStats_Type()
)
cienaCesBenchmarkTestInstanceEntryClearStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntryClearStats.setStatus("current")
_CienaCesBenchmarkTestInstanceEntryRowStatus_Type = RowStatus
_CienaCesBenchmarkTestInstanceEntryRowStatus_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntryRowStatus = _CienaCesBenchmarkTestInstanceEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 15),
    _CienaCesBenchmarkTestInstanceEntryRowStatus_Type()
)
cienaCesBenchmarkTestInstanceEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntryRowStatus.setStatus("current")
_CienaCesBenchmarkTestInstanceEntryAssocEntityId_Type = Integer32
_CienaCesBenchmarkTestInstanceEntryAssocEntityId_Object = MibTableColumn
cienaCesBenchmarkTestInstanceEntryAssocEntityId = _CienaCesBenchmarkTestInstanceEntryAssocEntityId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 12, 1, 16),
    _CienaCesBenchmarkTestInstanceEntryAssocEntityId_Type()
)
cienaCesBenchmarkTestInstanceEntryAssocEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceEntryAssocEntityId.setStatus("current")
_CienaCesBenchmarkGenTestSessionAllocationTable_Object = MibTable
cienaCesBenchmarkGenTestSessionAllocationTable = _CienaCesBenchmarkGenTestSessionAllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionAllocationTable.setStatus("current")
_CienaCesBenchmarkGenTestSessionAllocationEntry_Object = MibTableRow
cienaCesBenchmarkGenTestSessionAllocationEntry = _CienaCesBenchmarkGenTestSessionAllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1)
)
cienaCesBenchmarkGenTestSessionAllocationEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEntityEntryId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionPcpIndex"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionColorIndex"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionAllocationEntry.setStatus("current")


class _CienaCesBenchmarkGenTestSessionPcpIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionPcpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesBenchmarkGenTestSessionPcpIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionPcpIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionPcpIndex = _CienaCesBenchmarkGenTestSessionPcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 1),
    _CienaCesBenchmarkGenTestSessionPcpIndex_Type()
)
cienaCesBenchmarkGenTestSessionPcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPcpIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionColorIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionColorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CienaCesBenchmarkGenTestSessionColorIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionColorIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionColorIndex = _CienaCesBenchmarkGenTestSessionColorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 2),
    _CienaCesBenchmarkGenTestSessionColorIndex_Type()
)
cienaCesBenchmarkGenTestSessionColorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionColorIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionPcp_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesBenchmarkGenTestSessionPcp_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionPcp_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionPcp = _CienaCesBenchmarkGenTestSessionPcp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 3),
    _CienaCesBenchmarkGenTestSessionPcp_Type()
)
cienaCesBenchmarkGenTestSessionPcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPcp.setStatus("current")
_CienaCesBenchmarkGenTestSessionColor_Type = CienaCesBenchmarkColorTest
_CienaCesBenchmarkGenTestSessionColor_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionColor = _CienaCesBenchmarkGenTestSessionColor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 4),
    _CienaCesBenchmarkGenTestSessionColor_Type()
)
cienaCesBenchmarkGenTestSessionColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionColor.setStatus("current")


class _CienaCesBenchmarkGenTestSessionId_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CienaCesBenchmarkGenTestSessionId_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionId_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionId = _CienaCesBenchmarkGenTestSessionId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 5),
    _CienaCesBenchmarkGenTestSessionId_Type()
)
cienaCesBenchmarkGenTestSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionId.setStatus("current")
_CienaCesBenchmarkGenTestSessionEmixSequenceId_Type = Integer32
_CienaCesBenchmarkGenTestSessionEmixSequenceId_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionEmixSequenceId = _CienaCesBenchmarkGenTestSessionEmixSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 6),
    _CienaCesBenchmarkGenTestSessionEmixSequenceId_Type()
)
cienaCesBenchmarkGenTestSessionEmixSequenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionEmixSequenceId.setStatus("current")
_CienaCesBenchmarkGenTestSessionCurrentPktSize_Type = Integer32
_CienaCesBenchmarkGenTestSessionCurrentPktSize_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionCurrentPktSize = _CienaCesBenchmarkGenTestSessionCurrentPktSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 7),
    _CienaCesBenchmarkGenTestSessionCurrentPktSize_Type()
)
cienaCesBenchmarkGenTestSessionCurrentPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionCurrentPktSize.setStatus("current")
_CienaCesBenchmarkGenTestSessionThroughputTestState_Type = CienaCesBenchmarkThroughputTestState
_CienaCesBenchmarkGenTestSessionThroughputTestState_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputTestState = _CienaCesBenchmarkGenTestSessionThroughputTestState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 8),
    _CienaCesBenchmarkGenTestSessionThroughputTestState_Type()
)
cienaCesBenchmarkGenTestSessionThroughputTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputTestState.setStatus("current")
_CienaCesBenchmarkGenTestSessionFramelossTestState_Type = CienaCesBenchmarkFramelossTestState
_CienaCesBenchmarkGenTestSessionFramelossTestState_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossTestState = _CienaCesBenchmarkGenTestSessionFramelossTestState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 9),
    _CienaCesBenchmarkGenTestSessionFramelossTestState_Type()
)
cienaCesBenchmarkGenTestSessionFramelossTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossTestState.setStatus("current")
_CienaCesBenchmarkGenTestSessionLatencyTestState_Type = CienaCesBenchmarkLatencyPdvTestState
_CienaCesBenchmarkGenTestSessionLatencyTestState_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyTestState = _CienaCesBenchmarkGenTestSessionLatencyTestState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 10),
    _CienaCesBenchmarkGenTestSessionLatencyTestState_Type()
)
cienaCesBenchmarkGenTestSessionLatencyTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyTestState.setStatus("current")
_CienaCesBenchmarkGenTestSessionPdvTestState_Type = CienaCesBenchmarkLatencyPdvTestState
_CienaCesBenchmarkGenTestSessionPdvTestState_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionPdvTestState = _CienaCesBenchmarkGenTestSessionPdvTestState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 11),
    _CienaCesBenchmarkGenTestSessionPdvTestState_Type()
)
cienaCesBenchmarkGenTestSessionPdvTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPdvTestState.setStatus("current")
_CienaCesBenchmarkGenTestSessionRfc2544TestState_Type = CienaCesBenchmarkRfc2544TestState
_CienaCesBenchmarkGenTestSessionRfc2544TestState_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionRfc2544TestState = _CienaCesBenchmarkGenTestSessionRfc2544TestState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 12),
    _CienaCesBenchmarkGenTestSessionRfc2544TestState_Type()
)
cienaCesBenchmarkGenTestSessionRfc2544TestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionRfc2544TestState.setStatus("current")
_CienaCesBenchmarkGenTestSessionY1564TestState_Type = CienaCesBenchmarkY1564TestState
_CienaCesBenchmarkGenTestSessionY1564TestState_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionY1564TestState = _CienaCesBenchmarkGenTestSessionY1564TestState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 13),
    _CienaCesBenchmarkGenTestSessionY1564TestState_Type()
)
cienaCesBenchmarkGenTestSessionY1564TestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionY1564TestState.setStatus("current")
_CienaCesBenchmarkGenTestSessionCurrentRate_Type = Integer32
_CienaCesBenchmarkGenTestSessionCurrentRate_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionCurrentRate = _CienaCesBenchmarkGenTestSessionCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 14),
    _CienaCesBenchmarkGenTestSessionCurrentRate_Type()
)
cienaCesBenchmarkGenTestSessionCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionCurrentRate.setStatus("current")
_CienaCesBenchmarkGenTestSessionSamplesCompleted_Type = Integer32
_CienaCesBenchmarkGenTestSessionSamplesCompleted_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionSamplesCompleted = _CienaCesBenchmarkGenTestSessionSamplesCompleted_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 13, 1, 15),
    _CienaCesBenchmarkGenTestSessionSamplesCompleted_Type()
)
cienaCesBenchmarkGenTestSessionSamplesCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionSamplesCompleted.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsTable_Object = MibTable
cienaCesBenchmarkTestInstanceStatsTable = _CienaCesBenchmarkTestInstanceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsTable.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsEntry_Object = MibTableRow
cienaCesBenchmarkTestInstanceStatsEntry = _CienaCesBenchmarkTestInstanceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1)
)
cienaCesBenchmarkTestInstanceStatsEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEntityEntryId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsEntry.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsRxPkts_Type = Counter64
_CienaCesBenchmarkTestInstanceStatsRxPkts_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxPkts = _CienaCesBenchmarkTestInstanceStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 1),
    _CienaCesBenchmarkTestInstanceStatsRxPkts_Type()
)
cienaCesBenchmarkTestInstanceStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsRxPkts.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsRxIpv4Pkts_Type = Counter64
_CienaCesBenchmarkTestInstanceStatsRxIpv4Pkts_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxIpv4Pkts = _CienaCesBenchmarkTestInstanceStatsRxIpv4Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 2),
    _CienaCesBenchmarkTestInstanceStatsRxIpv4Pkts_Type()
)
cienaCesBenchmarkTestInstanceStatsRxIpv4Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsRxIpv4Pkts.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts_Type = Counter64
_CienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts = _CienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 3),
    _CienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts_Type()
)
cienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsRxIpv6Pkts_Type = Counter64
_CienaCesBenchmarkTestInstanceStatsRxIpv6Pkts_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxIpv6Pkts = _CienaCesBenchmarkTestInstanceStatsRxIpv6Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 4),
    _CienaCesBenchmarkTestInstanceStatsRxIpv6Pkts_Type()
)
cienaCesBenchmarkTestInstanceStatsRxIpv6Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsRxIpv6Pkts.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts_Type = Counter64
_CienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts = _CienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 5),
    _CienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts_Type()
)
cienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsRxNonIpPkts_Type = Counter64
_CienaCesBenchmarkTestInstanceStatsRxNonIpPkts_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxNonIpPkts = _CienaCesBenchmarkTestInstanceStatsRxNonIpPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 6),
    _CienaCesBenchmarkTestInstanceStatsRxNonIpPkts_Type()
)
cienaCesBenchmarkTestInstanceStatsRxNonIpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsRxNonIpPkts.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts_Type = Counter64
_CienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts = _CienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 7),
    _CienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts_Type()
)
cienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsRxDuplicatePkts_Type = Counter64
_CienaCesBenchmarkTestInstanceStatsRxDuplicatePkts_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxDuplicatePkts = _CienaCesBenchmarkTestInstanceStatsRxDuplicatePkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 8),
    _CienaCesBenchmarkTestInstanceStatsRxDuplicatePkts_Type()
)
cienaCesBenchmarkTestInstanceStatsRxDuplicatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsRxDuplicatePkts.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow_Type = TruthValue
_CienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow = _CienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 9),
    _CienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow_Type()
)
cienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsRxOOOPkts_Type = Counter64
_CienaCesBenchmarkTestInstanceStatsRxOOOPkts_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxOOOPkts = _CienaCesBenchmarkTestInstanceStatsRxOOOPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 10),
    _CienaCesBenchmarkTestInstanceStatsRxOOOPkts_Type()
)
cienaCesBenchmarkTestInstanceStatsRxOOOPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsRxOOOPkts.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow_Type = TruthValue
_CienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow = _CienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 11),
    _CienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow_Type()
)
cienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts_Type = Counter64
_CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts = _CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 12),
    _CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts_Type()
)
cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow_Type = TruthValue
_CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow = _CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 13),
    _CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow_Type()
)
cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts_Type = Counter64
_CienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts = _CienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 14),
    _CienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts_Type()
)
cienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts.setStatus("current")
_CienaCesBenchmarkTestInstanceStatsTxPkts_Type = Counter64
_CienaCesBenchmarkTestInstanceStatsTxPkts_Object = MibTableColumn
cienaCesBenchmarkTestInstanceStatsTxPkts = _CienaCesBenchmarkTestInstanceStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 14, 1, 15),
    _CienaCesBenchmarkTestInstanceStatsTxPkts_Type()
)
cienaCesBenchmarkTestInstanceStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestInstanceStatsTxPkts.setStatus("current")
_CienaCesBenchmarkGenTestSessionThroughputResultsTable_Object = MibTable
cienaCesBenchmarkGenTestSessionThroughputResultsTable = _CienaCesBenchmarkGenTestSessionThroughputResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 15)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputResultsTable.setStatus("current")
_CienaCesBenchmarkGenTestSessionThroughputResultsEntry_Object = MibTableRow
cienaCesBenchmarkGenTestSessionThroughputResultsEntry = _CienaCesBenchmarkGenTestSessionThroughputResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 15, 1)
)
cienaCesBenchmarkGenTestSessionThroughputResultsEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEntityEntryId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionThroughputResultsColorIndex"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputResultsEntry.setStatus("current")


class _CienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex = _CienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 15, 1, 1),
    _CienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex_Type()
)
cienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionThroughputResultsColorIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionThroughputResultsColorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CienaCesBenchmarkGenTestSessionThroughputResultsColorIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionThroughputResultsColorIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsColorIndex = _CienaCesBenchmarkGenTestSessionThroughputResultsColorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 15, 1, 2),
    _CienaCesBenchmarkGenTestSessionThroughputResultsColorIndex_Type()
)
cienaCesBenchmarkGenTestSessionThroughputResultsColorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputResultsColorIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex = _CienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 15, 1, 3),
    _CienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex_Type()
)
cienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionThroughputResultsPcp_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionThroughputResultsPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesBenchmarkGenTestSessionThroughputResultsPcp_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionThroughputResultsPcp_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsPcp = _CienaCesBenchmarkGenTestSessionThroughputResultsPcp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 15, 1, 4),
    _CienaCesBenchmarkGenTestSessionThroughputResultsPcp_Type()
)
cienaCesBenchmarkGenTestSessionThroughputResultsPcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputResultsPcp.setStatus("current")
_CienaCesBenchmarkGenTestSessionThroughputResultsColor_Type = CienaCesBenchmarkColorTest
_CienaCesBenchmarkGenTestSessionThroughputResultsColor_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsColor = _CienaCesBenchmarkGenTestSessionThroughputResultsColor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 15, 1, 5),
    _CienaCesBenchmarkGenTestSessionThroughputResultsColor_Type()
)
cienaCesBenchmarkGenTestSessionThroughputResultsColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputResultsColor.setStatus("current")
_CienaCesBenchmarkGenTestSessionThroughputResultsFrameSize_Type = Integer32
_CienaCesBenchmarkGenTestSessionThroughputResultsFrameSize_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsFrameSize = _CienaCesBenchmarkGenTestSessionThroughputResultsFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 15, 1, 6),
    _CienaCesBenchmarkGenTestSessionThroughputResultsFrameSize_Type()
)
cienaCesBenchmarkGenTestSessionThroughputResultsFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputResultsFrameSize.setStatus("current")


class _CienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId = _CienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 15, 1, 7),
    _CienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId_Type()
)
cienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId.setStatus("current")
_CienaCesBenchmarkGenTestSessionThroughputResultsMin_Type = CienaCesBenchmarkThroughputResult
_CienaCesBenchmarkGenTestSessionThroughputResultsMin_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsMin = _CienaCesBenchmarkGenTestSessionThroughputResultsMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 15, 1, 8),
    _CienaCesBenchmarkGenTestSessionThroughputResultsMin_Type()
)
cienaCesBenchmarkGenTestSessionThroughputResultsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputResultsMin.setStatus("current")
_CienaCesBenchmarkGenTestSessionThroughputResultsMax_Type = CienaCesBenchmarkThroughputResult
_CienaCesBenchmarkGenTestSessionThroughputResultsMax_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsMax = _CienaCesBenchmarkGenTestSessionThroughputResultsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 15, 1, 9),
    _CienaCesBenchmarkGenTestSessionThroughputResultsMax_Type()
)
cienaCesBenchmarkGenTestSessionThroughputResultsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputResultsMax.setStatus("current")
_CienaCesBenchmarkGenTestSessionThroughputResultsAvg_Type = CienaCesBenchmarkThroughputResult
_CienaCesBenchmarkGenTestSessionThroughputResultsAvg_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsAvg = _CienaCesBenchmarkGenTestSessionThroughputResultsAvg_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 15, 1, 10),
    _CienaCesBenchmarkGenTestSessionThroughputResultsAvg_Type()
)
cienaCesBenchmarkGenTestSessionThroughputResultsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputResultsAvg.setStatus("current")
_CienaCesBenchmarkGenTestSessionThroughputResultsIterations_Type = Integer32
_CienaCesBenchmarkGenTestSessionThroughputResultsIterations_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsIterations = _CienaCesBenchmarkGenTestSessionThroughputResultsIterations_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 15, 1, 11),
    _CienaCesBenchmarkGenTestSessionThroughputResultsIterations_Type()
)
cienaCesBenchmarkGenTestSessionThroughputResultsIterations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputResultsIterations.setStatus("current")
_CienaCesBenchmarkGenTestSessionThroughputResultsKpiResult_Type = CienaCesBenchmarkKpiResult
_CienaCesBenchmarkGenTestSessionThroughputResultsKpiResult_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsKpiResult = _CienaCesBenchmarkGenTestSessionThroughputResultsKpiResult_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 15, 1, 12),
    _CienaCesBenchmarkGenTestSessionThroughputResultsKpiResult_Type()
)
cienaCesBenchmarkGenTestSessionThroughputResultsKpiResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionThroughputResultsKpiResult.setStatus("current")
_CienaCesBenchmarkGenTestSessionFramelossResultsTable_Object = MibTable
cienaCesBenchmarkGenTestSessionFramelossResultsTable = _CienaCesBenchmarkGenTestSessionFramelossResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsTable.setStatus("current")
_CienaCesBenchmarkGenTestSessionFramelossResultsEntry_Object = MibTableRow
cienaCesBenchmarkGenTestSessionFramelossResultsEntry = _CienaCesBenchmarkGenTestSessionFramelossResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16, 1)
)
cienaCesBenchmarkGenTestSessionFramelossResultsEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEntityEntryId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionFramelossResultsColorIndex"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionFramelossResultsRateIndex"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsEntry.setStatus("current")


class _CienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex = _CienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16, 1, 1),
    _CienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex_Type()
)
cienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionFramelossResultsColorIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionFramelossResultsColorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CienaCesBenchmarkGenTestSessionFramelossResultsColorIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionFramelossResultsColorIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsColorIndex = _CienaCesBenchmarkGenTestSessionFramelossResultsColorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16, 1, 2),
    _CienaCesBenchmarkGenTestSessionFramelossResultsColorIndex_Type()
)
cienaCesBenchmarkGenTestSessionFramelossResultsColorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsColorIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex = _CienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16, 1, 3),
    _CienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex_Type()
)
cienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionFramelossResultsRateIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionFramelossResultsRateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CienaCesBenchmarkGenTestSessionFramelossResultsRateIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionFramelossResultsRateIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsRateIndex = _CienaCesBenchmarkGenTestSessionFramelossResultsRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16, 1, 4),
    _CienaCesBenchmarkGenTestSessionFramelossResultsRateIndex_Type()
)
cienaCesBenchmarkGenTestSessionFramelossResultsRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsRateIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionFramelossResultsPcp_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionFramelossResultsPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesBenchmarkGenTestSessionFramelossResultsPcp_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionFramelossResultsPcp_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsPcp = _CienaCesBenchmarkGenTestSessionFramelossResultsPcp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16, 1, 5),
    _CienaCesBenchmarkGenTestSessionFramelossResultsPcp_Type()
)
cienaCesBenchmarkGenTestSessionFramelossResultsPcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsPcp.setStatus("current")
_CienaCesBenchmarkGenTestSessionFramelossResultsColor_Type = CienaCesBenchmarkColorTest
_CienaCesBenchmarkGenTestSessionFramelossResultsColor_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsColor = _CienaCesBenchmarkGenTestSessionFramelossResultsColor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16, 1, 6),
    _CienaCesBenchmarkGenTestSessionFramelossResultsColor_Type()
)
cienaCesBenchmarkGenTestSessionFramelossResultsColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsColor.setStatus("current")
_CienaCesBenchmarkGenTestSessionFramelossResultsFrameSize_Type = Integer32
_CienaCesBenchmarkGenTestSessionFramelossResultsFrameSize_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsFrameSize = _CienaCesBenchmarkGenTestSessionFramelossResultsFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16, 1, 7),
    _CienaCesBenchmarkGenTestSessionFramelossResultsFrameSize_Type()
)
cienaCesBenchmarkGenTestSessionFramelossResultsFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsFrameSize.setStatus("current")


class _CienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId = _CienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16, 1, 8),
    _CienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId_Type()
)
cienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId.setStatus("current")
_CienaCesBenchmarkGenTestSessionFramelossResultsRate_Type = Integer32
_CienaCesBenchmarkGenTestSessionFramelossResultsRate_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsRate = _CienaCesBenchmarkGenTestSessionFramelossResultsRate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16, 1, 9),
    _CienaCesBenchmarkGenTestSessionFramelossResultsRate_Type()
)
cienaCesBenchmarkGenTestSessionFramelossResultsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsRate.setStatus("current")
_CienaCesBenchmarkGenTestSessionFramelossResultsFirst_Type = CienaCesBenchmarkFramelossResult
_CienaCesBenchmarkGenTestSessionFramelossResultsFirst_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsFirst = _CienaCesBenchmarkGenTestSessionFramelossResultsFirst_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16, 1, 10),
    _CienaCesBenchmarkGenTestSessionFramelossResultsFirst_Type()
)
cienaCesBenchmarkGenTestSessionFramelossResultsFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsFirst.setStatus("current")
_CienaCesBenchmarkGenTestSessionFramelossResultsSecond_Type = CienaCesBenchmarkFramelossResult
_CienaCesBenchmarkGenTestSessionFramelossResultsSecond_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsSecond = _CienaCesBenchmarkGenTestSessionFramelossResultsSecond_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16, 1, 11),
    _CienaCesBenchmarkGenTestSessionFramelossResultsSecond_Type()
)
cienaCesBenchmarkGenTestSessionFramelossResultsSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsSecond.setStatus("current")
_CienaCesBenchmarkGenTestSessionFramelossResultsKpiResult_Type = CienaCesBenchmarkKpiResult
_CienaCesBenchmarkGenTestSessionFramelossResultsKpiResult_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsKpiResult = _CienaCesBenchmarkGenTestSessionFramelossResultsKpiResult_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16, 1, 12),
    _CienaCesBenchmarkGenTestSessionFramelossResultsKpiResult_Type()
)
cienaCesBenchmarkGenTestSessionFramelossResultsKpiResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsKpiResult.setStatus("current")
_CienaCesBenchmarkGenTestSessionFramelossResultsResult_Type = CienaCesBenchmarkFramelossResult
_CienaCesBenchmarkGenTestSessionFramelossResultsResult_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsResult = _CienaCesBenchmarkGenTestSessionFramelossResultsResult_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 16, 1, 13),
    _CienaCesBenchmarkGenTestSessionFramelossResultsResult_Type()
)
cienaCesBenchmarkGenTestSessionFramelossResultsResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionFramelossResultsResult.setStatus("current")
_CienaCesBenchmarkGenTestSessionLatencyResultsTable_Object = MibTable
cienaCesBenchmarkGenTestSessionLatencyResultsTable = _CienaCesBenchmarkGenTestSessionLatencyResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 17)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyResultsTable.setStatus("current")
_CienaCesBenchmarkGenTestSessionLatencyResultsEntry_Object = MibTableRow
cienaCesBenchmarkGenTestSessionLatencyResultsEntry = _CienaCesBenchmarkGenTestSessionLatencyResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 17, 1)
)
cienaCesBenchmarkGenTestSessionLatencyResultsEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEntityEntryId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionLatencyResultsColorIndex"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyResultsEntry.setStatus("current")


class _CienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex = _CienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 17, 1, 1),
    _CienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex_Type()
)
cienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionLatencyResultsColorIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionLatencyResultsColorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CienaCesBenchmarkGenTestSessionLatencyResultsColorIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionLatencyResultsColorIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsColorIndex = _CienaCesBenchmarkGenTestSessionLatencyResultsColorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 17, 1, 2),
    _CienaCesBenchmarkGenTestSessionLatencyResultsColorIndex_Type()
)
cienaCesBenchmarkGenTestSessionLatencyResultsColorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyResultsColorIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex = _CienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 17, 1, 3),
    _CienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex_Type()
)
cienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionLatencyResultsPcp_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionLatencyResultsPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesBenchmarkGenTestSessionLatencyResultsPcp_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionLatencyResultsPcp_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsPcp = _CienaCesBenchmarkGenTestSessionLatencyResultsPcp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 17, 1, 4),
    _CienaCesBenchmarkGenTestSessionLatencyResultsPcp_Type()
)
cienaCesBenchmarkGenTestSessionLatencyResultsPcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyResultsPcp.setStatus("current")
_CienaCesBenchmarkGenTestSessionLatencyResultsColor_Type = CienaCesBenchmarkColorTest
_CienaCesBenchmarkGenTestSessionLatencyResultsColor_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsColor = _CienaCesBenchmarkGenTestSessionLatencyResultsColor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 17, 1, 5),
    _CienaCesBenchmarkGenTestSessionLatencyResultsColor_Type()
)
cienaCesBenchmarkGenTestSessionLatencyResultsColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyResultsColor.setStatus("current")
_CienaCesBenchmarkGenTestSessionLatencyResultsFrameSize_Type = Integer32
_CienaCesBenchmarkGenTestSessionLatencyResultsFrameSize_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsFrameSize = _CienaCesBenchmarkGenTestSessionLatencyResultsFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 17, 1, 6),
    _CienaCesBenchmarkGenTestSessionLatencyResultsFrameSize_Type()
)
cienaCesBenchmarkGenTestSessionLatencyResultsFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyResultsFrameSize.setStatus("current")


class _CienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId = _CienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 17, 1, 7),
    _CienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId_Type()
)
cienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId.setStatus("current")
_CienaCesBenchmarkGenTestSessionLatencyResultsMin_Type = Unsigned32
_CienaCesBenchmarkGenTestSessionLatencyResultsMin_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsMin = _CienaCesBenchmarkGenTestSessionLatencyResultsMin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 17, 1, 8),
    _CienaCesBenchmarkGenTestSessionLatencyResultsMin_Type()
)
cienaCesBenchmarkGenTestSessionLatencyResultsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyResultsMin.setStatus("current")
_CienaCesBenchmarkGenTestSessionLatencyResultsMax_Type = Unsigned32
_CienaCesBenchmarkGenTestSessionLatencyResultsMax_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsMax = _CienaCesBenchmarkGenTestSessionLatencyResultsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 17, 1, 9),
    _CienaCesBenchmarkGenTestSessionLatencyResultsMax_Type()
)
cienaCesBenchmarkGenTestSessionLatencyResultsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyResultsMax.setStatus("current")
_CienaCesBenchmarkGenTestSessionLatencyResultsAvg_Type = Unsigned32
_CienaCesBenchmarkGenTestSessionLatencyResultsAvg_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsAvg = _CienaCesBenchmarkGenTestSessionLatencyResultsAvg_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 17, 1, 10),
    _CienaCesBenchmarkGenTestSessionLatencyResultsAvg_Type()
)
cienaCesBenchmarkGenTestSessionLatencyResultsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyResultsAvg.setStatus("current")
_CienaCesBenchmarkGenTestSessionLatencyResultsSamples_Type = Integer32
_CienaCesBenchmarkGenTestSessionLatencyResultsSamples_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsSamples = _CienaCesBenchmarkGenTestSessionLatencyResultsSamples_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 17, 1, 11),
    _CienaCesBenchmarkGenTestSessionLatencyResultsSamples_Type()
)
cienaCesBenchmarkGenTestSessionLatencyResultsSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyResultsSamples.setStatus("current")
_CienaCesBenchmarkGenTestSessionLatencyResultsKpiResult_Type = CienaCesBenchmarkKpiResult
_CienaCesBenchmarkGenTestSessionLatencyResultsKpiResult_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsKpiResult = _CienaCesBenchmarkGenTestSessionLatencyResultsKpiResult_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 17, 1, 12),
    _CienaCesBenchmarkGenTestSessionLatencyResultsKpiResult_Type()
)
cienaCesBenchmarkGenTestSessionLatencyResultsKpiResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionLatencyResultsKpiResult.setStatus("current")
_CienaCesBenchmarkGenTestSessionPdvResultsTable_Object = MibTable
cienaCesBenchmarkGenTestSessionPdvResultsTable = _CienaCesBenchmarkGenTestSessionPdvResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 18)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPdvResultsTable.setStatus("current")
_CienaCesBenchmarkGenTestSessionPdvResultsEntry_Object = MibTableRow
cienaCesBenchmarkGenTestSessionPdvResultsEntry = _CienaCesBenchmarkGenTestSessionPdvResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 18, 1)
)
cienaCesBenchmarkGenTestSessionPdvResultsEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEntityEntryId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionPdvResultsPcpIndex"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionPdvResultsColorIndex"),
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPdvResultsEntry.setStatus("current")


class _CienaCesBenchmarkGenTestSessionPdvResultsPcpIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionPdvResultsPcpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesBenchmarkGenTestSessionPdvResultsPcpIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionPdvResultsPcpIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsPcpIndex = _CienaCesBenchmarkGenTestSessionPdvResultsPcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 18, 1, 1),
    _CienaCesBenchmarkGenTestSessionPdvResultsPcpIndex_Type()
)
cienaCesBenchmarkGenTestSessionPdvResultsPcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPdvResultsPcpIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionPdvResultsColorIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionPdvResultsColorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CienaCesBenchmarkGenTestSessionPdvResultsColorIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionPdvResultsColorIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsColorIndex = _CienaCesBenchmarkGenTestSessionPdvResultsColorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 18, 1, 2),
    _CienaCesBenchmarkGenTestSessionPdvResultsColorIndex_Type()
)
cienaCesBenchmarkGenTestSessionPdvResultsColorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPdvResultsColorIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex = _CienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 18, 1, 3),
    _CienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex_Type()
)
cienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex.setStatus("current")


class _CienaCesBenchmarkGenTestSessionPdvResultsPcp_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionPdvResultsPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesBenchmarkGenTestSessionPdvResultsPcp_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionPdvResultsPcp_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsPcp = _CienaCesBenchmarkGenTestSessionPdvResultsPcp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 18, 1, 4),
    _CienaCesBenchmarkGenTestSessionPdvResultsPcp_Type()
)
cienaCesBenchmarkGenTestSessionPdvResultsPcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPdvResultsPcp.setStatus("current")
_CienaCesBenchmarkGenTestSessionPdvResultsColor_Type = CienaCesBenchmarkColorTest
_CienaCesBenchmarkGenTestSessionPdvResultsColor_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsColor = _CienaCesBenchmarkGenTestSessionPdvResultsColor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 18, 1, 5),
    _CienaCesBenchmarkGenTestSessionPdvResultsColor_Type()
)
cienaCesBenchmarkGenTestSessionPdvResultsColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPdvResultsColor.setStatus("current")
_CienaCesBenchmarkGenTestSessionPdvResultsFrameSize_Type = Integer32
_CienaCesBenchmarkGenTestSessionPdvResultsFrameSize_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsFrameSize = _CienaCesBenchmarkGenTestSessionPdvResultsFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 18, 1, 6),
    _CienaCesBenchmarkGenTestSessionPdvResultsFrameSize_Type()
)
cienaCesBenchmarkGenTestSessionPdvResultsFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPdvResultsFrameSize.setStatus("current")


class _CienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId_Type(Integer32):
    """Custom type cienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId_Type.__name__ = "Integer32"
_CienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId = _CienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 18, 1, 7),
    _CienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId_Type()
)
cienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId.setStatus("current")
_CienaCesBenchmarkGenTestSessionPdvResultsAvg_Type = Unsigned32
_CienaCesBenchmarkGenTestSessionPdvResultsAvg_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsAvg = _CienaCesBenchmarkGenTestSessionPdvResultsAvg_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 18, 1, 8),
    _CienaCesBenchmarkGenTestSessionPdvResultsAvg_Type()
)
cienaCesBenchmarkGenTestSessionPdvResultsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPdvResultsAvg.setStatus("current")
_CienaCesBenchmarkGenTestSessionPdvResultsSamples_Type = Integer32
_CienaCesBenchmarkGenTestSessionPdvResultsSamples_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsSamples = _CienaCesBenchmarkGenTestSessionPdvResultsSamples_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 18, 1, 9),
    _CienaCesBenchmarkGenTestSessionPdvResultsSamples_Type()
)
cienaCesBenchmarkGenTestSessionPdvResultsSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPdvResultsSamples.setStatus("current")
_CienaCesBenchmarkGenTestSessionPdvResultsKpiResult_Type = CienaCesBenchmarkKpiResult
_CienaCesBenchmarkGenTestSessionPdvResultsKpiResult_Object = MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsKpiResult = _CienaCesBenchmarkGenTestSessionPdvResultsKpiResult_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 18, 1, 10),
    _CienaCesBenchmarkGenTestSessionPdvResultsKpiResult_Type()
)
cienaCesBenchmarkGenTestSessionPdvResultsKpiResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkGenTestSessionPdvResultsKpiResult.setStatus("current")
_CienaCesBenchmarkEmixCharacterSetTable_Object = MibTable
cienaCesBenchmarkEmixCharacterSetTable = _CienaCesBenchmarkEmixCharacterSetTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 19)
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixCharacterSetTable.setStatus("current")
_CienaCesBenchmarkEmixCharacterSetEntry_Object = MibTableRow
cienaCesBenchmarkEmixCharacterSetEntry = _CienaCesBenchmarkEmixCharacterSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 19, 1)
)
cienaCesBenchmarkEmixCharacterSetEntry.setIndexNames(
    (0, "CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEmixCharacterSetEntryIndex"),
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixCharacterSetEntry.setStatus("current")


class _CienaCesBenchmarkEmixCharacterSetEntryIndex_Type(Integer32):
    """Custom type cienaCesBenchmarkEmixCharacterSetEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_CienaCesBenchmarkEmixCharacterSetEntryIndex_Type.__name__ = "Integer32"
_CienaCesBenchmarkEmixCharacterSetEntryIndex_Object = MibTableColumn
cienaCesBenchmarkEmixCharacterSetEntryIndex = _CienaCesBenchmarkEmixCharacterSetEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 19, 1, 1),
    _CienaCesBenchmarkEmixCharacterSetEntryIndex_Type()
)
cienaCesBenchmarkEmixCharacterSetEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixCharacterSetEntryIndex.setStatus("current")


class _CienaCesBenchmarkEmixCharacterSetEntryCharacter_Type(DisplayString):
    """Custom type cienaCesBenchmarkEmixCharacterSetEntryCharacter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_CienaCesBenchmarkEmixCharacterSetEntryCharacter_Type.__name__ = "DisplayString"
_CienaCesBenchmarkEmixCharacterSetEntryCharacter_Object = MibTableColumn
cienaCesBenchmarkEmixCharacterSetEntryCharacter = _CienaCesBenchmarkEmixCharacterSetEntryCharacter_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 19, 1, 2),
    _CienaCesBenchmarkEmixCharacterSetEntryCharacter_Type()
)
cienaCesBenchmarkEmixCharacterSetEntryCharacter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixCharacterSetEntryCharacter.setStatus("current")


class _CienaCesBenchmarkEmixCharacterSetEntryFrameSize_Type(DisplayString):
    """Custom type cienaCesBenchmarkEmixCharacterSetEntryFrameSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_CienaCesBenchmarkEmixCharacterSetEntryFrameSize_Type.__name__ = "DisplayString"
_CienaCesBenchmarkEmixCharacterSetEntryFrameSize_Object = MibTableColumn
cienaCesBenchmarkEmixCharacterSetEntryFrameSize = _CienaCesBenchmarkEmixCharacterSetEntryFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 39, 1, 1, 19, 1, 3),
    _CienaCesBenchmarkEmixCharacterSetEntryFrameSize_Type()
)
cienaCesBenchmarkEmixCharacterSetEntryFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBenchmarkEmixCharacterSetEntryFrameSize.setStatus("current")
_CienaCesBenchmarkNotifications_ObjectIdentity = ObjectIdentity
cienaCesBenchmarkNotifications = _CienaCesBenchmarkNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 39)
)

# Managed Objects groups


# Notification objects

cienaCesBenchmarkTestStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 39, 1)
)
cienaCesBenchmarkTestStarted.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEntityEntryPortId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryName"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntrySvid"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryCvid"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryDstMac"))
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestStarted.setStatus(
        "current"
    )

cienaCesBenchmarkTestStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 39, 2)
)
cienaCesBenchmarkTestStopped.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryName"))
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestStopped.setStatus(
        "current"
    )

cienaCesBenchmarkTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 39, 3)
)
cienaCesBenchmarkTestCompleted.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryName"))
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestCompleted.setStatus(
        "current"
    )

cienaCesBenchmarkTestFailedThroughputKpi = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 39, 4)
)
cienaCesBenchmarkTestFailedThroughputKpi.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryName"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiProfileId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiPcp"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiColor"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionCurrentPktSize"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEmixSequenceId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionThroughputResultsMax"))
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestFailedThroughputKpi.setStatus(
        "current"
    )

cienaCesBenchmarkTestFailedFramelossKpi = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 39, 5)
)
cienaCesBenchmarkTestFailedFramelossKpi.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryName"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiProfileId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiPcp"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiColor"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionCurrentPktSize"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEmixSequenceId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionFramelossResultsResult"))
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestFailedFramelossKpi.setStatus(
        "current"
    )

cienaCesBenchmarkTestFailedLatencyKpi = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 39, 6)
)
cienaCesBenchmarkTestFailedLatencyKpi.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryName"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiProfileId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiPcp"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiColor"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionCurrentPktSize"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEmixSequenceId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionLatencyResultsMax"))
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestFailedLatencyKpi.setStatus(
        "current"
    )

cienaCesBenchmarkTestFailedPdvKpi = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 39, 7)
)
cienaCesBenchmarkTestFailedPdvKpi.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryName"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiProfileId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiPcp"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkKpiColor"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionCurrentPktSize"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkEmixSequenceId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionPdvResultsAvg"))
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestFailedPdvKpi.setStatus(
        "current"
    )

cienaCesBenchmarkTestIterationCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 39, 8)
)
cienaCesBenchmarkTestIterationCompleted.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryId"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkTestInstanceEntryName"),
        ("CIENA-CES-BENCHMARK-MIB", "cienaCesBenchmarkGenTestSessionThroughputResultsIterations"))
)
if mibBuilder.loadTexts:
    cienaCesBenchmarkTestIterationCompleted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-BENCHMARK-MIB",
    **{"CienaCesBenchmarkLatencyPdvTestState": CienaCesBenchmarkLatencyPdvTestState,
       "CienaCesBenchmarkThroughputTestState": CienaCesBenchmarkThroughputTestState,
       "CienaCesBenchmarkFramelossTestState": CienaCesBenchmarkFramelossTestState,
       "CienaCesBenchmarkRfc2544TestState": CienaCesBenchmarkRfc2544TestState,
       "CienaCesBenchmarkY1564TestState": CienaCesBenchmarkY1564TestState,
       "CienaCesBenchmarkColorTest": CienaCesBenchmarkColorTest,
       "CienaCesBenchmarkKpiResult": CienaCesBenchmarkKpiResult,
       "CienaCesBenchmarkAdminState": CienaCesBenchmarkAdminState,
       "CienaCesBenchmarkThroughputKpiPercent": CienaCesBenchmarkThroughputKpiPercent,
       "CienaCesBenchmarkFramelossKpiPercent": CienaCesBenchmarkFramelossKpiPercent,
       "CienaCesBenchmarkThroughputResult": CienaCesBenchmarkThroughputResult,
       "CienaCesBenchmarkFramelossResult": CienaCesBenchmarkFramelossResult,
       "CienaCesBenchmarkPcpBitmap": CienaCesBenchmarkPcpBitmap,
       "cienaCesBenchmarkMIB": cienaCesBenchmarkMIB,
       "cienaCesBenchmarkMIBObjects": cienaCesBenchmarkMIBObjects,
       "cienaCesBenchmarkModule": cienaCesBenchmarkModule,
       "cienaCesBenchmarkGlobalObjects": cienaCesBenchmarkGlobalObjects,
       "cienaCesBenchmarkGlobalAdminState": cienaCesBenchmarkGlobalAdminState,
       "cienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId": cienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId,
       "cienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId": cienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId,
       "cienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId": cienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId,
       "cienaCesBenchmarkGlobalPlatformMaxConfigEntities": cienaCesBenchmarkGlobalPlatformMaxConfigEntities,
       "cienaCesBenchmarkGlobalPlatformMaxConfigTestInstances": cienaCesBenchmarkGlobalPlatformMaxConfigTestInstances,
       "cienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles": cienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles,
       "cienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles": cienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles,
       "cienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles": cienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles,
       "cienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences": cienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences,
       "cienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests": cienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests,
       "cienaCesBenchmarkGlobalConfiguredEntities": cienaCesBenchmarkGlobalConfiguredEntities,
       "cienaCesBenchmarkGlobalConfiguredTestInstances": cienaCesBenchmarkGlobalConfiguredTestInstances,
       "cienaCesBenchmarkGlobalConfiguredProfiles": cienaCesBenchmarkGlobalConfiguredProfiles,
       "cienaCesBenchmarkGlobalConfiguredEmixSequences": cienaCesBenchmarkGlobalConfiguredEmixSequences,
       "cienaCesBenchmarkGlobalConfiguredKpiProfiles": cienaCesBenchmarkGlobalConfiguredKpiProfiles,
       "cienaCesBenchmarkGlobalConfiguredBwAllocProfiles": cienaCesBenchmarkGlobalConfiguredBwAllocProfiles,
       "cienaCesBenchmarkGlobalEnabledTestInstances": cienaCesBenchmarkGlobalEnabledTestInstances,
       "cienaCesBenchmarkGlobalGeneratorRunningTestInstances": cienaCesBenchmarkGlobalGeneratorRunningTestInstances,
       "cienaCesBenchmarkEntityTable": cienaCesBenchmarkEntityTable,
       "cienaCesBenchmarkEntityEntry": cienaCesBenchmarkEntityEntry,
       "cienaCesBenchmarkEntityEntryId": cienaCesBenchmarkEntityEntryId,
       "cienaCesBenchmarkEntityEntryName": cienaCesBenchmarkEntityEntryName,
       "cienaCesBenchmarkEntityEntryRole": cienaCesBenchmarkEntityEntryRole,
       "cienaCesBenchmarkEntityEntryPortId": cienaCesBenchmarkEntityEntryPortId,
       "cienaCesBenchmarkEntityEntryMode": cienaCesBenchmarkEntityEntryMode,
       "cienaCesBenchmarkEntityEntryAdminState": cienaCesBenchmarkEntityEntryAdminState,
       "cienaCesBenchmarkEntityEntryLocalMac": cienaCesBenchmarkEntityEntryLocalMac,
       "cienaCesBenchmarkEntityEntrySlotId": cienaCesBenchmarkEntityEntrySlotId,
       "cienaCesBenchmarkEntityEntryReflectorVendorType": cienaCesBenchmarkEntityEntryReflectorVendorType,
       "cienaCesBenchmarkEntityEntryReflectionLevel": cienaCesBenchmarkEntityEntryReflectionLevel,
       "cienaCesBenchmarkEntityEntryGeneratorHFrameSize": cienaCesBenchmarkEntityEntryGeneratorHFrameSize,
       "cienaCesBenchmarkEntityEntryMaxConfigTestInstances": cienaCesBenchmarkEntityEntryMaxConfigTestInstances,
       "cienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances": cienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances,
       "cienaCesBenchmarkEntityEntryOperEnabled": cienaCesBenchmarkEntityEntryOperEnabled,
       "cienaCesBenchmarkEntityEntryNumTestInstancesConfigured": cienaCesBenchmarkEntityEntryNumTestInstancesConfigured,
       "cienaCesBenchmarkEntityEntryNumTestInstancesEnabled": cienaCesBenchmarkEntityEntryNumTestInstancesEnabled,
       "cienaCesBenchmarkEntityEntryGenNumTestInstancesRunning": cienaCesBenchmarkEntityEntryGenNumTestInstancesRunning,
       "cienaCesBenchmarkEntityEntryBwAvailable": cienaCesBenchmarkEntityEntryBwAvailable,
       "cienaCesBenchmarkEntityEntryGenBwUsedByRunningTests": cienaCesBenchmarkEntityEntryGenBwUsedByRunningTests,
       "cienaCesBenchmarkEntityEntryAvailableHwSessions": cienaCesBenchmarkEntityEntryAvailableHwSessions,
       "cienaCesBenchmarkEntityEntryAllocatedHwSessions": cienaCesBenchmarkEntityEntryAllocatedHwSessions,
       "cienaCesBenchmarkEntityEntryRowStatus": cienaCesBenchmarkEntityEntryRowStatus,
       "cienaCesBenchmarkEntityEntryClearStats": cienaCesBenchmarkEntityEntryClearStats,
       "cienaCesBenchmarkEntityEntryReflectorMacValidation": cienaCesBenchmarkEntityEntryReflectorMacValidation,
       "cienaCesBenchmarkEntityStatsTable": cienaCesBenchmarkEntityStatsTable,
       "cienaCesBenchmarkEntityStatsEntry": cienaCesBenchmarkEntityStatsEntry,
       "cienaCesBenchmarkEntityStatsEntryClear": cienaCesBenchmarkEntityStatsEntryClear,
       "cienaCesBenchmarkEntityStatsEntryPortTxBytes": cienaCesBenchmarkEntityStatsEntryPortTxBytes,
       "cienaCesBenchmarkEntityStatsEntryPortTxPkts": cienaCesBenchmarkEntityStatsEntryPortTxPkts,
       "cienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts": cienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts,
       "cienaCesBenchmarkEntityStatsEntryPortTxUcastPkts": cienaCesBenchmarkEntityStatsEntryPortTxUcastPkts,
       "cienaCesBenchmarkEntityStatsEntryPortTxMcastPkts": cienaCesBenchmarkEntityStatsEntryPortTxMcastPkts,
       "cienaCesBenchmarkEntityStatsEntryPortTxBcastPkts": cienaCesBenchmarkEntityStatsEntryPortTxBcastPkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts": cienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxOversizePkts": cienaCesBenchmarkEntityStatsEntryPortRxOversizePkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts": cienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts": cienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts,
       "cienaCesBenchmarkEntityStatsEntryPortTxPausePkts": cienaCesBenchmarkEntityStatsEntryPortTxPausePkts,
       "cienaCesBenchmarkEntityStatsEntryPortTxDropPkts": cienaCesBenchmarkEntityStatsEntryPortTxDropPkts,
       "cienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts": cienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts,
       "cienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts": cienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts,
       "cienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts": cienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts,
       "cienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts": cienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts": cienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts": cienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts": cienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts": cienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts": cienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts": cienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts": cienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxBytes": cienaCesBenchmarkEntityStatsEntryPortRxBytes,
       "cienaCesBenchmarkEntityStatsEntryPortRxPkts": cienaCesBenchmarkEntityStatsEntryPortRxPkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts": cienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxDeferPkts": cienaCesBenchmarkEntityStatsEntryPortRxDeferPkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxGiantPkts": cienaCesBenchmarkEntityStatsEntryPortRxGiantPkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts": cienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts": cienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts": cienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts": cienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxPausePkts": cienaCesBenchmarkEntityStatsEntryPortRxPausePkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxUcastPkts": cienaCesBenchmarkEntityStatsEntryPortRxUcastPkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxMcastPkts": cienaCesBenchmarkEntityStatsEntryPortRxMcastPkts,
       "cienaCesBenchmarkEntityStatsEntryPortRxBcastPkts": cienaCesBenchmarkEntityStatsEntryPortRxBcastPkts,
       "cienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts": cienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts,
       "cienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts": cienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts": cienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts": cienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts": cienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts": cienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts": cienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts": cienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts,
       "cienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts": cienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts,
       "cienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts": cienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts,
       "cienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts": cienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts,
       "cienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts": cienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts,
       "cienaCesBenchmarkEmixSequenceTable": cienaCesBenchmarkEmixSequenceTable,
       "cienaCesBenchmarkEmixSequenceEntry": cienaCesBenchmarkEmixSequenceEntry,
       "cienaCesBenchmarkEmixSequenceId": cienaCesBenchmarkEmixSequenceId,
       "cienaCesBenchmarkEmixSequenceName": cienaCesBenchmarkEmixSequenceName,
       "cienaCesBenchmarkEmixSequence": cienaCesBenchmarkEmixSequence,
       "cienaCesBenchmarkEmixSequenceUFrameSize": cienaCesBenchmarkEmixSequenceUFrameSize,
       "cienaCesBenchmarkEmixSequenceNumOfRef": cienaCesBenchmarkEmixSequenceNumOfRef,
       "cienaCesBenchmarkEmixSequenceUserCreated": cienaCesBenchmarkEmixSequenceUserCreated,
       "cienaCesBenchmarkEmixSequenceRowStatus": cienaCesBenchmarkEmixSequenceRowStatus,
       "cienaCesBenchmarkEmixFrameSizeTable": cienaCesBenchmarkEmixFrameSizeTable,
       "cienaCesBenchmarkEmixFrameSizeEntry": cienaCesBenchmarkEmixFrameSizeEntry,
       "cienaCesBenchmarkEmixFrameSizeIndex": cienaCesBenchmarkEmixFrameSizeIndex,
       "cienaCesBenchmarkEmixFrameSizeEntryFrameSize": cienaCesBenchmarkEmixFrameSizeEntryFrameSize,
       "cienaCesBenchmarkEmixAvgFrameSizeTable": cienaCesBenchmarkEmixAvgFrameSizeTable,
       "cienaCesBenchmarkEmixAvgFrameSizeEntry": cienaCesBenchmarkEmixAvgFrameSizeEntry,
       "cienaCesBenchmarkEmixAvgFrameSize": cienaCesBenchmarkEmixAvgFrameSize,
       "cienaCesBenchmarkKpiProfileTable": cienaCesBenchmarkKpiProfileTable,
       "cienaCesBenchmarkKpiProfileEntry": cienaCesBenchmarkKpiProfileEntry,
       "cienaCesBenchmarkKpiProfileId": cienaCesBenchmarkKpiProfileId,
       "cienaCesBenchmarkKpiProfileName": cienaCesBenchmarkKpiProfileName,
       "cienaCesBenchmarkKpiProfileNumOfRef": cienaCesBenchmarkKpiProfileNumOfRef,
       "cienaCesBenchmarkKpiProfileRowStatus": cienaCesBenchmarkKpiProfileRowStatus,
       "cienaCesBenchmarkKpiPcpColorTable": cienaCesBenchmarkKpiPcpColorTable,
       "cienaCesBenchmarkKpiPcpColorEntry": cienaCesBenchmarkKpiPcpColorEntry,
       "cienaCesBenchmarkKpiPcpIndex": cienaCesBenchmarkKpiPcpIndex,
       "cienaCesBenchmarkKpiColorIndex": cienaCesBenchmarkKpiColorIndex,
       "cienaCesBenchmarkKpiPcp": cienaCesBenchmarkKpiPcp,
       "cienaCesBenchmarkKpiColor": cienaCesBenchmarkKpiColor,
       "cienaCesBenchmarkKpiThroughput": cienaCesBenchmarkKpiThroughput,
       "cienaCesBenchmarkKpiFrameloss": cienaCesBenchmarkKpiFrameloss,
       "cienaCesBenchmarkKpiLatency": cienaCesBenchmarkKpiLatency,
       "cienaCesBenchmarkKpiPdv": cienaCesBenchmarkKpiPdv,
       "cienaCesBenchmarkBwAllocProfileTable": cienaCesBenchmarkBwAllocProfileTable,
       "cienaCesBenchmarkBwAllocProfileEntry": cienaCesBenchmarkBwAllocProfileEntry,
       "cienaCesBenchmarkBwAllocProfileId": cienaCesBenchmarkBwAllocProfileId,
       "cienaCesBenchmarkBwAllocProfileName": cienaCesBenchmarkBwAllocProfileName,
       "cienaCesBenchmarkBwAllocProfileNumOfRef": cienaCesBenchmarkBwAllocProfileNumOfRef,
       "cienaCesBenchmarkBwAllocProfileRowStatus": cienaCesBenchmarkBwAllocProfileRowStatus,
       "cienaCesBenchmarkBwRatioTable": cienaCesBenchmarkBwRatioTable,
       "cienaCesBenchmarkBwRatioEntry": cienaCesBenchmarkBwRatioEntry,
       "cienaCesBenchmarkBwRatioPcpIndex": cienaCesBenchmarkBwRatioPcpIndex,
       "cienaCesBenchmarkBwRatioPcp": cienaCesBenchmarkBwRatioPcp,
       "cienaCesBenchmarkBwRatio": cienaCesBenchmarkBwRatio,
       "cienaCesBenchmarkProfileTable": cienaCesBenchmarkProfileTable,
       "cienaCesBenchmarkProfileEntry": cienaCesBenchmarkProfileEntry,
       "cienaCesBenchmarkProfileEntryId": cienaCesBenchmarkProfileEntryId,
       "cienaCesBenchmarkProfileEntryName": cienaCesBenchmarkProfileEntryName,
       "cienaCesBenchmarkProfileEntryBandwidth": cienaCesBenchmarkProfileEntryBandwidth,
       "cienaCesBenchmarkProfileEntryExcessBandwidth": cienaCesBenchmarkProfileEntryExcessBandwidth,
       "cienaCesBenchmarkProfileEntryInterval": cienaCesBenchmarkProfileEntryInterval,
       "cienaCesBenchmarkProfileEntryDuration": cienaCesBenchmarkProfileEntryDuration,
       "cienaCesBenchmarkProfileEntrySetFrameSizeList": cienaCesBenchmarkProfileEntrySetFrameSizeList,
       "cienaCesBenchmarkProfileEntryMaxSearches": cienaCesBenchmarkProfileEntryMaxSearches,
       "cienaCesBenchmarkProfileEntryMaxSamples": cienaCesBenchmarkProfileEntryMaxSamples,
       "cienaCesBenchmarkProfileEntrySamplingInterval": cienaCesBenchmarkProfileEntrySamplingInterval,
       "cienaCesBenchmarkProfileEntryFrameLossStartBw": cienaCesBenchmarkProfileEntryFrameLossStartBw,
       "cienaCesBenchmarkProfileEntryVidValidation": cienaCesBenchmarkProfileEntryVidValidation,
       "cienaCesBenchmarkProfileEntryPcpValidation": cienaCesBenchmarkProfileEntryPcpValidation,
       "cienaCesBenchmarkProfileEntryColorValidation": cienaCesBenchmarkProfileEntryColorValidation,
       "cienaCesBenchmarkProfileEntryKpiProfileId": cienaCesBenchmarkProfileEntryKpiProfileId,
       "cienaCesBenchmarkProfileEntryBwAllocProfileId": cienaCesBenchmarkProfileEntryBwAllocProfileId,
       "cienaCesBenchmarkProfileEntryEmixSequenceId": cienaCesBenchmarkProfileEntryEmixSequenceId,
       "cienaCesBenchmarkProfileEntryEncapType": cienaCesBenchmarkProfileEntryEncapType,
       "cienaCesBenchmarkProfileEntryPduType": cienaCesBenchmarkProfileEntryPduType,
       "cienaCesBenchmarkProfileEntryDstmac": cienaCesBenchmarkProfileEntryDstmac,
       "cienaCesBenchmarkProfileEntrySVid": cienaCesBenchmarkProfileEntrySVid,
       "cienaCesBenchmarkProfileEntrySPcp": cienaCesBenchmarkProfileEntrySPcp,
       "cienaCesBenchmarkProfileEntrySColor": cienaCesBenchmarkProfileEntrySColor,
       "cienaCesBenchmarkProfileEntryCVid": cienaCesBenchmarkProfileEntryCVid,
       "cienaCesBenchmarkProfileEntryCPcp": cienaCesBenchmarkProfileEntryCPcp,
       "cienaCesBenchmarkProfileEntryCColor": cienaCesBenchmarkProfileEntryCColor,
       "cienaCesBenchmarkProfileEntryTpid": cienaCesBenchmarkProfileEntryTpid,
       "cienaCesBenchmarkProfileEntryDscp": cienaCesBenchmarkProfileEntryDscp,
       "cienaCesBenchmarkProfileEntrySrcInetAddrType": cienaCesBenchmarkProfileEntrySrcInetAddrType,
       "cienaCesBenchmarkProfileEntrySrcInetAddr": cienaCesBenchmarkProfileEntrySrcInetAddr,
       "cienaCesBenchmarkProfileEntryDstInetAddrType": cienaCesBenchmarkProfileEntryDstInetAddrType,
       "cienaCesBenchmarkProfileEntryDstInetAddr": cienaCesBenchmarkProfileEntryDstInetAddr,
       "cienaCesBenchmarkProfileEntryCustomPayload": cienaCesBenchmarkProfileEntryCustomPayload,
       "cienaCesBenchmarkProfileEntryThroughputTest": cienaCesBenchmarkProfileEntryThroughputTest,
       "cienaCesBenchmarkProfileEntryFramelossTest": cienaCesBenchmarkProfileEntryFramelossTest,
       "cienaCesBenchmarkProfileEntryLatencyTest": cienaCesBenchmarkProfileEntryLatencyTest,
       "cienaCesBenchmarkProfileEntryPdvTest": cienaCesBenchmarkProfileEntryPdvTest,
       "cienaCesBenchmarkProfileEntryBurstTest": cienaCesBenchmarkProfileEntryBurstTest,
       "cienaCesBenchmarkProfileEntryRfc2544Suite": cienaCesBenchmarkProfileEntryRfc2544Suite,
       "cienaCesBenchmarkProfileEntryY1564Test": cienaCesBenchmarkProfileEntryY1564Test,
       "cienaCesBenchmarkProfileEntryHwSessionsRequired": cienaCesBenchmarkProfileEntryHwSessionsRequired,
       "cienaCesBenchmarkProfileEntryNumOfRef": cienaCesBenchmarkProfileEntryNumOfRef,
       "cienaCesBenchmarkProfileEntryRowStatus": cienaCesBenchmarkProfileEntryRowStatus,
       "cienaCesBenchmarkTestInstanceTable": cienaCesBenchmarkTestInstanceTable,
       "cienaCesBenchmarkTestInstanceEntry": cienaCesBenchmarkTestInstanceEntry,
       "cienaCesBenchmarkTestInstanceEntryId": cienaCesBenchmarkTestInstanceEntryId,
       "cienaCesBenchmarkTestInstanceEntryName": cienaCesBenchmarkTestInstanceEntryName,
       "cienaCesBenchmarkTestInstanceEntrySubPortId": cienaCesBenchmarkTestInstanceEntrySubPortId,
       "cienaCesBenchmarkTestInstanceEntryProfileId": cienaCesBenchmarkTestInstanceEntryProfileId,
       "cienaCesBenchmarkTestInstanceEntrySvid": cienaCesBenchmarkTestInstanceEntrySvid,
       "cienaCesBenchmarkTestInstanceEntryCvid": cienaCesBenchmarkTestInstanceEntryCvid,
       "cienaCesBenchmarkTestInstanceEntryUntagged": cienaCesBenchmarkTestInstanceEntryUntagged,
       "cienaCesBenchmarkTestInstanceEntryDstMac": cienaCesBenchmarkTestInstanceEntryDstMac,
       "cienaCesBenchmarkTestInstanceEntryAdminState": cienaCesBenchmarkTestInstanceEntryAdminState,
       "cienaCesBenchmarkTestInstanceEntryStarted": cienaCesBenchmarkTestInstanceEntryStarted,
       "cienaCesBenchmarkTestInstanceEntryCurrentInterval": cienaCesBenchmarkTestInstanceEntryCurrentInterval,
       "cienaCesBenchmarkTestInstanceEntryTotalIntervals": cienaCesBenchmarkTestInstanceEntryTotalIntervals,
       "cienaCesBenchmarkTestInstanceEntryLastIterStart": cienaCesBenchmarkTestInstanceEntryLastIterStart,
       "cienaCesBenchmarkTestInstanceEntryClearStats": cienaCesBenchmarkTestInstanceEntryClearStats,
       "cienaCesBenchmarkTestInstanceEntryRowStatus": cienaCesBenchmarkTestInstanceEntryRowStatus,
       "cienaCesBenchmarkTestInstanceEntryAssocEntityId": cienaCesBenchmarkTestInstanceEntryAssocEntityId,
       "cienaCesBenchmarkGenTestSessionAllocationTable": cienaCesBenchmarkGenTestSessionAllocationTable,
       "cienaCesBenchmarkGenTestSessionAllocationEntry": cienaCesBenchmarkGenTestSessionAllocationEntry,
       "cienaCesBenchmarkGenTestSessionPcpIndex": cienaCesBenchmarkGenTestSessionPcpIndex,
       "cienaCesBenchmarkGenTestSessionColorIndex": cienaCesBenchmarkGenTestSessionColorIndex,
       "cienaCesBenchmarkGenTestSessionPcp": cienaCesBenchmarkGenTestSessionPcp,
       "cienaCesBenchmarkGenTestSessionColor": cienaCesBenchmarkGenTestSessionColor,
       "cienaCesBenchmarkGenTestSessionId": cienaCesBenchmarkGenTestSessionId,
       "cienaCesBenchmarkGenTestSessionEmixSequenceId": cienaCesBenchmarkGenTestSessionEmixSequenceId,
       "cienaCesBenchmarkGenTestSessionCurrentPktSize": cienaCesBenchmarkGenTestSessionCurrentPktSize,
       "cienaCesBenchmarkGenTestSessionThroughputTestState": cienaCesBenchmarkGenTestSessionThroughputTestState,
       "cienaCesBenchmarkGenTestSessionFramelossTestState": cienaCesBenchmarkGenTestSessionFramelossTestState,
       "cienaCesBenchmarkGenTestSessionLatencyTestState": cienaCesBenchmarkGenTestSessionLatencyTestState,
       "cienaCesBenchmarkGenTestSessionPdvTestState": cienaCesBenchmarkGenTestSessionPdvTestState,
       "cienaCesBenchmarkGenTestSessionRfc2544TestState": cienaCesBenchmarkGenTestSessionRfc2544TestState,
       "cienaCesBenchmarkGenTestSessionY1564TestState": cienaCesBenchmarkGenTestSessionY1564TestState,
       "cienaCesBenchmarkGenTestSessionCurrentRate": cienaCesBenchmarkGenTestSessionCurrentRate,
       "cienaCesBenchmarkGenTestSessionSamplesCompleted": cienaCesBenchmarkGenTestSessionSamplesCompleted,
       "cienaCesBenchmarkTestInstanceStatsTable": cienaCesBenchmarkTestInstanceStatsTable,
       "cienaCesBenchmarkTestInstanceStatsEntry": cienaCesBenchmarkTestInstanceStatsEntry,
       "cienaCesBenchmarkTestInstanceStatsRxPkts": cienaCesBenchmarkTestInstanceStatsRxPkts,
       "cienaCesBenchmarkTestInstanceStatsRxIpv4Pkts": cienaCesBenchmarkTestInstanceStatsRxIpv4Pkts,
       "cienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts": cienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts,
       "cienaCesBenchmarkTestInstanceStatsRxIpv6Pkts": cienaCesBenchmarkTestInstanceStatsRxIpv6Pkts,
       "cienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts": cienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts,
       "cienaCesBenchmarkTestInstanceStatsRxNonIpPkts": cienaCesBenchmarkTestInstanceStatsRxNonIpPkts,
       "cienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts": cienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts,
       "cienaCesBenchmarkTestInstanceStatsRxDuplicatePkts": cienaCesBenchmarkTestInstanceStatsRxDuplicatePkts,
       "cienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow": cienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow,
       "cienaCesBenchmarkTestInstanceStatsRxOOOPkts": cienaCesBenchmarkTestInstanceStatsRxOOOPkts,
       "cienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow": cienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow,
       "cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts": cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts,
       "cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow": cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow,
       "cienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts": cienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts,
       "cienaCesBenchmarkTestInstanceStatsTxPkts": cienaCesBenchmarkTestInstanceStatsTxPkts,
       "cienaCesBenchmarkGenTestSessionThroughputResultsTable": cienaCesBenchmarkGenTestSessionThroughputResultsTable,
       "cienaCesBenchmarkGenTestSessionThroughputResultsEntry": cienaCesBenchmarkGenTestSessionThroughputResultsEntry,
       "cienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex": cienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex,
       "cienaCesBenchmarkGenTestSessionThroughputResultsColorIndex": cienaCesBenchmarkGenTestSessionThroughputResultsColorIndex,
       "cienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex": cienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex,
       "cienaCesBenchmarkGenTestSessionThroughputResultsPcp": cienaCesBenchmarkGenTestSessionThroughputResultsPcp,
       "cienaCesBenchmarkGenTestSessionThroughputResultsColor": cienaCesBenchmarkGenTestSessionThroughputResultsColor,
       "cienaCesBenchmarkGenTestSessionThroughputResultsFrameSize": cienaCesBenchmarkGenTestSessionThroughputResultsFrameSize,
       "cienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId": cienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId,
       "cienaCesBenchmarkGenTestSessionThroughputResultsMin": cienaCesBenchmarkGenTestSessionThroughputResultsMin,
       "cienaCesBenchmarkGenTestSessionThroughputResultsMax": cienaCesBenchmarkGenTestSessionThroughputResultsMax,
       "cienaCesBenchmarkGenTestSessionThroughputResultsAvg": cienaCesBenchmarkGenTestSessionThroughputResultsAvg,
       "cienaCesBenchmarkGenTestSessionThroughputResultsIterations": cienaCesBenchmarkGenTestSessionThroughputResultsIterations,
       "cienaCesBenchmarkGenTestSessionThroughputResultsKpiResult": cienaCesBenchmarkGenTestSessionThroughputResultsKpiResult,
       "cienaCesBenchmarkGenTestSessionFramelossResultsTable": cienaCesBenchmarkGenTestSessionFramelossResultsTable,
       "cienaCesBenchmarkGenTestSessionFramelossResultsEntry": cienaCesBenchmarkGenTestSessionFramelossResultsEntry,
       "cienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex": cienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex,
       "cienaCesBenchmarkGenTestSessionFramelossResultsColorIndex": cienaCesBenchmarkGenTestSessionFramelossResultsColorIndex,
       "cienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex": cienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex,
       "cienaCesBenchmarkGenTestSessionFramelossResultsRateIndex": cienaCesBenchmarkGenTestSessionFramelossResultsRateIndex,
       "cienaCesBenchmarkGenTestSessionFramelossResultsPcp": cienaCesBenchmarkGenTestSessionFramelossResultsPcp,
       "cienaCesBenchmarkGenTestSessionFramelossResultsColor": cienaCesBenchmarkGenTestSessionFramelossResultsColor,
       "cienaCesBenchmarkGenTestSessionFramelossResultsFrameSize": cienaCesBenchmarkGenTestSessionFramelossResultsFrameSize,
       "cienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId": cienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId,
       "cienaCesBenchmarkGenTestSessionFramelossResultsRate": cienaCesBenchmarkGenTestSessionFramelossResultsRate,
       "cienaCesBenchmarkGenTestSessionFramelossResultsFirst": cienaCesBenchmarkGenTestSessionFramelossResultsFirst,
       "cienaCesBenchmarkGenTestSessionFramelossResultsSecond": cienaCesBenchmarkGenTestSessionFramelossResultsSecond,
       "cienaCesBenchmarkGenTestSessionFramelossResultsKpiResult": cienaCesBenchmarkGenTestSessionFramelossResultsKpiResult,
       "cienaCesBenchmarkGenTestSessionFramelossResultsResult": cienaCesBenchmarkGenTestSessionFramelossResultsResult,
       "cienaCesBenchmarkGenTestSessionLatencyResultsTable": cienaCesBenchmarkGenTestSessionLatencyResultsTable,
       "cienaCesBenchmarkGenTestSessionLatencyResultsEntry": cienaCesBenchmarkGenTestSessionLatencyResultsEntry,
       "cienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex": cienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex,
       "cienaCesBenchmarkGenTestSessionLatencyResultsColorIndex": cienaCesBenchmarkGenTestSessionLatencyResultsColorIndex,
       "cienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex": cienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex,
       "cienaCesBenchmarkGenTestSessionLatencyResultsPcp": cienaCesBenchmarkGenTestSessionLatencyResultsPcp,
       "cienaCesBenchmarkGenTestSessionLatencyResultsColor": cienaCesBenchmarkGenTestSessionLatencyResultsColor,
       "cienaCesBenchmarkGenTestSessionLatencyResultsFrameSize": cienaCesBenchmarkGenTestSessionLatencyResultsFrameSize,
       "cienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId": cienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId,
       "cienaCesBenchmarkGenTestSessionLatencyResultsMin": cienaCesBenchmarkGenTestSessionLatencyResultsMin,
       "cienaCesBenchmarkGenTestSessionLatencyResultsMax": cienaCesBenchmarkGenTestSessionLatencyResultsMax,
       "cienaCesBenchmarkGenTestSessionLatencyResultsAvg": cienaCesBenchmarkGenTestSessionLatencyResultsAvg,
       "cienaCesBenchmarkGenTestSessionLatencyResultsSamples": cienaCesBenchmarkGenTestSessionLatencyResultsSamples,
       "cienaCesBenchmarkGenTestSessionLatencyResultsKpiResult": cienaCesBenchmarkGenTestSessionLatencyResultsKpiResult,
       "cienaCesBenchmarkGenTestSessionPdvResultsTable": cienaCesBenchmarkGenTestSessionPdvResultsTable,
       "cienaCesBenchmarkGenTestSessionPdvResultsEntry": cienaCesBenchmarkGenTestSessionPdvResultsEntry,
       "cienaCesBenchmarkGenTestSessionPdvResultsPcpIndex": cienaCesBenchmarkGenTestSessionPdvResultsPcpIndex,
       "cienaCesBenchmarkGenTestSessionPdvResultsColorIndex": cienaCesBenchmarkGenTestSessionPdvResultsColorIndex,
       "cienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex": cienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex,
       "cienaCesBenchmarkGenTestSessionPdvResultsPcp": cienaCesBenchmarkGenTestSessionPdvResultsPcp,
       "cienaCesBenchmarkGenTestSessionPdvResultsColor": cienaCesBenchmarkGenTestSessionPdvResultsColor,
       "cienaCesBenchmarkGenTestSessionPdvResultsFrameSize": cienaCesBenchmarkGenTestSessionPdvResultsFrameSize,
       "cienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId": cienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId,
       "cienaCesBenchmarkGenTestSessionPdvResultsAvg": cienaCesBenchmarkGenTestSessionPdvResultsAvg,
       "cienaCesBenchmarkGenTestSessionPdvResultsSamples": cienaCesBenchmarkGenTestSessionPdvResultsSamples,
       "cienaCesBenchmarkGenTestSessionPdvResultsKpiResult": cienaCesBenchmarkGenTestSessionPdvResultsKpiResult,
       "cienaCesBenchmarkEmixCharacterSetTable": cienaCesBenchmarkEmixCharacterSetTable,
       "cienaCesBenchmarkEmixCharacterSetEntry": cienaCesBenchmarkEmixCharacterSetEntry,
       "cienaCesBenchmarkEmixCharacterSetEntryIndex": cienaCesBenchmarkEmixCharacterSetEntryIndex,
       "cienaCesBenchmarkEmixCharacterSetEntryCharacter": cienaCesBenchmarkEmixCharacterSetEntryCharacter,
       "cienaCesBenchmarkEmixCharacterSetEntryFrameSize": cienaCesBenchmarkEmixCharacterSetEntryFrameSize,
       "cienaCesBenchmarkNotifications": cienaCesBenchmarkNotifications,
       "cienaCesBenchmarkTestStarted": cienaCesBenchmarkTestStarted,
       "cienaCesBenchmarkTestStopped": cienaCesBenchmarkTestStopped,
       "cienaCesBenchmarkTestCompleted": cienaCesBenchmarkTestCompleted,
       "cienaCesBenchmarkTestFailedThroughputKpi": cienaCesBenchmarkTestFailedThroughputKpi,
       "cienaCesBenchmarkTestFailedFramelossKpi": cienaCesBenchmarkTestFailedFramelossKpi,
       "cienaCesBenchmarkTestFailedLatencyKpi": cienaCesBenchmarkTestFailedLatencyKpi,
       "cienaCesBenchmarkTestFailedPdvKpi": cienaCesBenchmarkTestFailedPdvKpi,
       "cienaCesBenchmarkTestIterationCompleted": cienaCesBenchmarkTestIterationCompleted}
)
