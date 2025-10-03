# SNMP MIB module (CISCO-ERR-DISABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCO-ERR-DISABLE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:26:21 2025
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

(VlanIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-PRIVATE-VLAN-MIB",
    "VlanIndexOrZero")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(TimeIntervalSec,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "TimeIntervalSec")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoErrDisableMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 548)
)
if mibBuilder.loadTexts:
    ciscoErrDisableMIB.setRevisions(
        ("2016-06-02 00:00",
         "2013-04-23 00:00",
         "2010-10-19 00:00",
         "2009-03-23 00:00",
         "2008-04-07 00:00",
         "2006-05-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CErrDisableFeatureID(TextualConvention, Integer32):
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
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61)
        )
    )
    namedValues = NamedValues(
        *(("udld", 1),
          ("bpduGuard", 2),
          ("channelMisconfig", 3),
          ("pagpFlap", 4),
          ("dtpFlap", 5),
          ("linkFlap", 6),
          ("l2ptGuard", 7),
          ("dot1xSecurityViolation", 8),
          ("portSecurityViolation", 9),
          ("gbicInvalid", 10),
          ("dhcpRateLimit", 11),
          ("unicastFlood", 12),
          ("vmps", 13),
          ("stormControl", 14),
          ("inlinePower", 15),
          ("arpInspection", 16),
          ("portLoopback", 17),
          ("packetBuffer", 18),
          ("macLimit", 19),
          ("linkMonitorFailure", 20),
          ("oamRemoteFailure", 21),
          ("dot1adIncompEtype", 22),
          ("dot1adIncompTunnel", 23),
          ("sfpConfigMismatch", 24),
          ("communityLimit", 25),
          ("invalidPolicy", 26),
          ("lsGroup", 27),
          ("ekey", 28),
          ("portModeFailure", 29),
          ("pppoeIaRateLimit", 30),
          ("oamRemoteCriticalEvent", 31),
          ("oamRemoteDyingGasp", 32),
          ("oamRemoteLinkFault", 33),
          ("mvrp", 34),
          ("tranceiverIncomp", 35),
          ("other", 36),
          ("portReinitLimitReached", 37),
          ("adminRxBBCreditPerfBufIncomp", 38),
          ("ficonNotEnabled", 39),
          ("adminModeIncomp", 40),
          ("adminSpeedIncomp", 41),
          ("adminRxBBCreditIncomp", 42),
          ("adminRxBufSizeIncomp", 43),
          ("eppFailure", 44),
          ("osmEPortUp", 45),
          ("osmNonEPortUp", 46),
          ("udldUniDir", 47),
          ("udldTxRxLoop", 48),
          ("udldNeighbourMismatch", 49),
          ("udldEmptyEcho", 50),
          ("udldAggrasiveModeLinkFailed", 51),
          ("excessivePortInterrupts", 52),
          ("channelErrDisabled", 53),
          ("hwProgFailed", 54),
          ("internalHandshakeFailed", 55),
          ("stpInconsistencyOnVpcPeerLink", 56),
          ("stpPortStateFailure", 57),
          ("ipConflict", 58),
          ("multipleMSapIdsRcvd", 59),
          ("oneHundredPdusWithoutAck", 60),
          ("ipQosCompatCheckFailure", 61))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoErrDisableMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoErrDisableMIBNotifs = _CiscoErrDisableMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 0)
)
_CErrDisableNotificationsPrefix_ObjectIdentity = ObjectIdentity
cErrDisableNotificationsPrefix = _CErrDisableNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 0, 1)
)
_CiscoErrDisableMIBObjects_ObjectIdentity = ObjectIdentity
ciscoErrDisableMIBObjects = _CiscoErrDisableMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1)
)
_CErrDisableGlobalObjects_ObjectIdentity = ObjectIdentity
cErrDisableGlobalObjects = _CErrDisableGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 1)
)
_CErrDisableRecoveryInterval_Type = TimeIntervalSec
_CErrDisableRecoveryInterval_Object = MibScalar
cErrDisableRecoveryInterval = _CErrDisableRecoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 1, 1),
    _CErrDisableRecoveryInterval_Type()
)
cErrDisableRecoveryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cErrDisableRecoveryInterval.setStatus("current")
_CErrDisableNotifEnable_Type = TruthValue
_CErrDisableNotifEnable_Object = MibScalar
cErrDisableNotifEnable = _CErrDisableNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 1, 2),
    _CErrDisableNotifEnable_Type()
)
cErrDisableNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cErrDisableNotifEnable.setStatus("current")
_CErrDisableNotifRate_Type = Unsigned32
_CErrDisableNotifRate_Object = MibScalar
cErrDisableNotifRate = _CErrDisableNotifRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 1, 3),
    _CErrDisableNotifRate_Type()
)
cErrDisableNotifRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cErrDisableNotifRate.setStatus("current")
if mibBuilder.loadTexts:
    cErrDisableNotifRate.setUnits("Notification/Minute")
_CErrDisableFeatureObjects_ObjectIdentity = ObjectIdentity
cErrDisableFeatureObjects = _CErrDisableFeatureObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2)
)
_CErrDisableFeatureTable_Object = MibTable
cErrDisableFeatureTable = _CErrDisableFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cErrDisableFeatureTable.setStatus("current")
_CErrDisableFeatureEntry_Object = MibTableRow
cErrDisableFeatureEntry = _CErrDisableFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1)
)
cErrDisableFeatureEntry.setIndexNames(
    (0, "CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureIndex"),
)
if mibBuilder.loadTexts:
    cErrDisableFeatureEntry.setStatus("current")
_CErrDisableFeatureIndex_Type = CErrDisableFeatureID
_CErrDisableFeatureIndex_Object = MibTableColumn
cErrDisableFeatureIndex = _CErrDisableFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 1),
    _CErrDisableFeatureIndex_Type()
)
cErrDisableFeatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cErrDisableFeatureIndex.setStatus("current")


class _CErrDisableFeatureConfigurable_Type(Bits):
    """Custom type cErrDisableFeatureConfigurable based on Bits"""
    namedValues = NamedValues(
        *(("detectionEnable", 0),
          ("recoveryEnable", 1),
          ("recoveryInterval", 2),
          ("detectShutdownVlan", 3),
          ("flapControl", 4))
    )

_CErrDisableFeatureConfigurable_Type.__name__ = "Bits"
_CErrDisableFeatureConfigurable_Object = MibTableColumn
cErrDisableFeatureConfigurable = _CErrDisableFeatureConfigurable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 2),
    _CErrDisableFeatureConfigurable_Type()
)
cErrDisableFeatureConfigurable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cErrDisableFeatureConfigurable.setStatus("current")
_CErrDisableFeatureDetectEnable_Type = TruthValue
_CErrDisableFeatureDetectEnable_Object = MibTableColumn
cErrDisableFeatureDetectEnable = _CErrDisableFeatureDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 3),
    _CErrDisableFeatureDetectEnable_Type()
)
cErrDisableFeatureDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cErrDisableFeatureDetectEnable.setStatus("current")
_CErrDisableFeatureRecoveryEnable_Type = TruthValue
_CErrDisableFeatureRecoveryEnable_Object = MibTableColumn
cErrDisableFeatureRecoveryEnable = _CErrDisableFeatureRecoveryEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 4),
    _CErrDisableFeatureRecoveryEnable_Type()
)
cErrDisableFeatureRecoveryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cErrDisableFeatureRecoveryEnable.setStatus("current")
_CErrDisableFeatureRecoveryInterval_Type = TimeIntervalSec
_CErrDisableFeatureRecoveryInterval_Object = MibTableColumn
cErrDisableFeatureRecoveryInterval = _CErrDisableFeatureRecoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 5),
    _CErrDisableFeatureRecoveryInterval_Type()
)
cErrDisableFeatureRecoveryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cErrDisableFeatureRecoveryInterval.setStatus("current")
_CErrDisableFeatureDetectShutdownVlan_Type = TruthValue
_CErrDisableFeatureDetectShutdownVlan_Object = MibTableColumn
cErrDisableFeatureDetectShutdownVlan = _CErrDisableFeatureDetectShutdownVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 6),
    _CErrDisableFeatureDetectShutdownVlan_Type()
)
cErrDisableFeatureDetectShutdownVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cErrDisableFeatureDetectShutdownVlan.setStatus("current")
_CErrDisableFeatureMaxFlapCount_Type = Unsigned32
_CErrDisableFeatureMaxFlapCount_Object = MibTableColumn
cErrDisableFeatureMaxFlapCount = _CErrDisableFeatureMaxFlapCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 7),
    _CErrDisableFeatureMaxFlapCount_Type()
)
cErrDisableFeatureMaxFlapCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cErrDisableFeatureMaxFlapCount.setStatus("current")
_CErrDisableFeatureFlapTimePeriod_Type = Unsigned32
_CErrDisableFeatureFlapTimePeriod_Object = MibTableColumn
cErrDisableFeatureFlapTimePeriod = _CErrDisableFeatureFlapTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 8),
    _CErrDisableFeatureFlapTimePeriod_Type()
)
cErrDisableFeatureFlapTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cErrDisableFeatureFlapTimePeriod.setStatus("current")
_CErrDisableIfObjects_ObjectIdentity = ObjectIdentity
cErrDisableIfObjects = _CErrDisableIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3)
)
_CErrDisableIfStatusTable_Object = MibTable
cErrDisableIfStatusTable = _CErrDisableIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cErrDisableIfStatusTable.setStatus("current")
_CErrDisableIfStatusEntry_Object = MibTableRow
cErrDisableIfStatusEntry = _CErrDisableIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1, 1)
)
cErrDisableIfStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusVlanIndex"),
)
if mibBuilder.loadTexts:
    cErrDisableIfStatusEntry.setStatus("current")
_CErrDisableIfStatusVlanIndex_Type = VlanIndexOrZero
_CErrDisableIfStatusVlanIndex_Object = MibTableColumn
cErrDisableIfStatusVlanIndex = _CErrDisableIfStatusVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1, 1, 1),
    _CErrDisableIfStatusVlanIndex_Type()
)
cErrDisableIfStatusVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cErrDisableIfStatusVlanIndex.setStatus("current")
_CErrDisableIfStatusCause_Type = CErrDisableFeatureID
_CErrDisableIfStatusCause_Object = MibTableColumn
cErrDisableIfStatusCause = _CErrDisableIfStatusCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1, 1, 2),
    _CErrDisableIfStatusCause_Type()
)
cErrDisableIfStatusCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cErrDisableIfStatusCause.setStatus("current")
_CErrDisableIfStatusTimeToRecover_Type = TimeIntervalSec
_CErrDisableIfStatusTimeToRecover_Object = MibTableColumn
cErrDisableIfStatusTimeToRecover = _CErrDisableIfStatusTimeToRecover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1, 1, 3),
    _CErrDisableIfStatusTimeToRecover_Type()
)
cErrDisableIfStatusTimeToRecover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cErrDisableIfStatusTimeToRecover.setStatus("current")
_CiscoErrDisableMIBConform_ObjectIdentity = ObjectIdentity
ciscoErrDisableMIBConform = _CiscoErrDisableMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 2)
)
_CiscoErrDisableMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoErrDisableMIBCompliances = _CiscoErrDisableMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 1)
)
_CiscoErrDisableMIBGroups_ObjectIdentity = ObjectIdentity
ciscoErrDisableMIBGroups = _CiscoErrDisableMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2)
)

# Managed Objects groups

ciscoErrDisableGlobalCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 1)
)
ciscoErrDisableGlobalCfgGroup.setObjects(
    ("CISCO-ERR-DISABLE-MIB", "cErrDisableRecoveryInterval")
)
if mibBuilder.loadTexts:
    ciscoErrDisableGlobalCfgGroup.setStatus("current")

ciscoErrDisableFeatureCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 2)
)
ciscoErrDisableFeatureCfgGroup.setObjects(
      *(("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureConfigurable"),
        ("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureDetectEnable"),
        ("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureRecoveryEnable"),
        ("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureRecoveryInterval"))
)
if mibBuilder.loadTexts:
    ciscoErrDisableFeatureCfgGroup.setStatus("current")

ciscoErrDisableIfStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 3)
)
ciscoErrDisableIfStatusGroup.setObjects(
      *(("CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusCause"),
        ("CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusTimeToRecover"))
)
if mibBuilder.loadTexts:
    ciscoErrDisableIfStatusGroup.setStatus("current")

ciscoErrDisableNotifCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 4)
)
ciscoErrDisableNotifCfgGroup.setObjects(
      *(("CISCO-ERR-DISABLE-MIB", "cErrDisableNotifEnable"),
        ("CISCO-ERR-DISABLE-MIB", "cErrDisableNotifRate"))
)
if mibBuilder.loadTexts:
    ciscoErrDisableNotifCfgGroup.setStatus("current")

ciscoErrDisableShutdownVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 7)
)
ciscoErrDisableShutdownVlanGroup.setObjects(
    ("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureDetectShutdownVlan")
)
if mibBuilder.loadTexts:
    ciscoErrDisableShutdownVlanGroup.setStatus("current")

ciscoErrDisableFeatureFlapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 8)
)
ciscoErrDisableFeatureFlapGroup.setObjects(
      *(("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureMaxFlapCount"),
        ("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureFlapTimePeriod"))
)
if mibBuilder.loadTexts:
    ciscoErrDisableFeatureFlapGroup.setStatus("current")


# Notification objects

cErrDisableInterfaceEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 0, 1, 1)
)
cErrDisableInterfaceEvent.setObjects(
    ("CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusCause")
)
if mibBuilder.loadTexts:
    cErrDisableInterfaceEvent.setStatus(
        "deprecated"
    )

cErrDisableInterfaceEventRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 0, 2)
)
cErrDisableInterfaceEventRev1.setObjects(
    ("CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusCause")
)
if mibBuilder.loadTexts:
    cErrDisableInterfaceEventRev1.setStatus(
        "current"
    )


# Notifications groups

ciscoErrDisableNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 5)
)
ciscoErrDisableNotifGroup.setObjects(
    ("CISCO-ERR-DISABLE-MIB", "cErrDisableInterfaceEvent")
)
if mibBuilder.loadTexts:
    ciscoErrDisableNotifGroup.setStatus(
        "deprecated"
    )

ciscoErrDisableNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 6)
)
ciscoErrDisableNotifGroupRev1.setObjects(
    ("CISCO-ERR-DISABLE-MIB", "cErrDisableInterfaceEventRev1")
)
if mibBuilder.loadTexts:
    ciscoErrDisableNotifGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoErrDisableMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 1, 1)
)
ciscoErrDisableMIBCompliance.setObjects(
      *(("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableGlobalCfgGroup"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableFeatureCfgGroup"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableIfStatusGroup"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifCfgGroup"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifGroup"))
)
if mibBuilder.loadTexts:
    ciscoErrDisableMIBCompliance.setStatus(
        "deprecated"
    )

ciscoErrDisableMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 1, 2)
)
ciscoErrDisableMIBComplianceRev1.setObjects(
      *(("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableGlobalCfgGroup"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableFeatureCfgGroup"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableIfStatusGroup"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifCfgGroup"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifGroupRev1"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableShutdownVlanGroup"))
)
if mibBuilder.loadTexts:
    ciscoErrDisableMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoErrDisableMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 1, 3)
)
ciscoErrDisableMIBComplianceRev2.setObjects(
      *(("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableGlobalCfgGroup"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableFeatureCfgGroup"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableIfStatusGroup"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifCfgGroup"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifGroupRev1"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableShutdownVlanGroup"),
        ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableFeatureFlapGroup"))
)
if mibBuilder.loadTexts:
    ciscoErrDisableMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ERR-DISABLE-MIB",
    **{"CErrDisableFeatureID": CErrDisableFeatureID,
       "ciscoErrDisableMIB": ciscoErrDisableMIB,
       "ciscoErrDisableMIBNotifs": ciscoErrDisableMIBNotifs,
       "cErrDisableNotificationsPrefix": cErrDisableNotificationsPrefix,
       "cErrDisableInterfaceEvent": cErrDisableInterfaceEvent,
       "cErrDisableInterfaceEventRev1": cErrDisableInterfaceEventRev1,
       "ciscoErrDisableMIBObjects": ciscoErrDisableMIBObjects,
       "cErrDisableGlobalObjects": cErrDisableGlobalObjects,
       "cErrDisableRecoveryInterval": cErrDisableRecoveryInterval,
       "cErrDisableNotifEnable": cErrDisableNotifEnable,
       "cErrDisableNotifRate": cErrDisableNotifRate,
       "cErrDisableFeatureObjects": cErrDisableFeatureObjects,
       "cErrDisableFeatureTable": cErrDisableFeatureTable,
       "cErrDisableFeatureEntry": cErrDisableFeatureEntry,
       "cErrDisableFeatureIndex": cErrDisableFeatureIndex,
       "cErrDisableFeatureConfigurable": cErrDisableFeatureConfigurable,
       "cErrDisableFeatureDetectEnable": cErrDisableFeatureDetectEnable,
       "cErrDisableFeatureRecoveryEnable": cErrDisableFeatureRecoveryEnable,
       "cErrDisableFeatureRecoveryInterval": cErrDisableFeatureRecoveryInterval,
       "cErrDisableFeatureDetectShutdownVlan": cErrDisableFeatureDetectShutdownVlan,
       "cErrDisableFeatureMaxFlapCount": cErrDisableFeatureMaxFlapCount,
       "cErrDisableFeatureFlapTimePeriod": cErrDisableFeatureFlapTimePeriod,
       "cErrDisableIfObjects": cErrDisableIfObjects,
       "cErrDisableIfStatusTable": cErrDisableIfStatusTable,
       "cErrDisableIfStatusEntry": cErrDisableIfStatusEntry,
       "cErrDisableIfStatusVlanIndex": cErrDisableIfStatusVlanIndex,
       "cErrDisableIfStatusCause": cErrDisableIfStatusCause,
       "cErrDisableIfStatusTimeToRecover": cErrDisableIfStatusTimeToRecover,
       "ciscoErrDisableMIBConform": ciscoErrDisableMIBConform,
       "ciscoErrDisableMIBCompliances": ciscoErrDisableMIBCompliances,
       "ciscoErrDisableMIBCompliance": ciscoErrDisableMIBCompliance,
       "ciscoErrDisableMIBComplianceRev1": ciscoErrDisableMIBComplianceRev1,
       "ciscoErrDisableMIBComplianceRev2": ciscoErrDisableMIBComplianceRev2,
       "ciscoErrDisableMIBGroups": ciscoErrDisableMIBGroups,
       "ciscoErrDisableGlobalCfgGroup": ciscoErrDisableGlobalCfgGroup,
       "ciscoErrDisableFeatureCfgGroup": ciscoErrDisableFeatureCfgGroup,
       "ciscoErrDisableIfStatusGroup": ciscoErrDisableIfStatusGroup,
       "ciscoErrDisableNotifCfgGroup": ciscoErrDisableNotifCfgGroup,
       "ciscoErrDisableNotifGroup": ciscoErrDisableNotifGroup,
       "ciscoErrDisableNotifGroupRev1": ciscoErrDisableNotifGroupRev1,
       "ciscoErrDisableShutdownVlanGroup": ciscoErrDisableShutdownVlanGroup,
       "ciscoErrDisableFeatureFlapGroup": ciscoErrDisableFeatureFlapGroup}
)
