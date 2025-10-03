# SNMP MIB module (WLSX-HA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos\WLSX-HA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:46 2025
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

(ArubaEnableValue,
 ArubaHaConnectivityStatus,
 ArubaHaRole) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaEnableValue",
    "ArubaHaConnectivityStatus",
    "ArubaHaRole")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

wlsxHaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20)
)
if mibBuilder.loadTexts:
    wlsxHaMIB.setRevisions(
        ("2020-08-14 17:45",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxHighAvalabilityInfoGroup_ObjectIdentity = ObjectIdentity
wlsxHighAvalabilityInfoGroup = _WlsxHighAvalabilityInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1)
)
_WlsxHighAvalabilityConfigTable_Object = MibTable
wlsxHighAvalabilityConfigTable = _WlsxHighAvalabilityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxHighAvalabilityConfigTable.setStatus("current")
_WlsxHighAvalabilityConfigEntry_Object = MibTableRow
wlsxHighAvalabilityConfigEntry = _WlsxHighAvalabilityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1)
)
wlsxHighAvalabilityConfigEntry.setIndexNames(
    (0, "WLSX-HA-MIB", "haProfileName"),
)
if mibBuilder.loadTexts:
    wlsxHighAvalabilityConfigEntry.setStatus("current")


class _HaProfileName_Type(DisplayString):
    """Custom type haProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HaProfileName_Type.__name__ = "DisplayString"
_HaProfileName_Object = MibTableColumn
haProfileName = _HaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 1),
    _HaProfileName_Type()
)
haProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    haProfileName.setStatus("current")


class _HaMembership_Type(DisplayString):
    """Custom type haMembership based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HaMembership_Type.__name__ = "DisplayString"
_HaMembership_Object = MibTableColumn
haMembership = _HaMembership_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 2),
    _HaMembership_Type()
)
haMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haMembership.setStatus("current")
_HaState_Type = ArubaEnableValue
_HaState_Object = MibTableColumn
haState = _HaState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 3),
    _HaState_Type()
)
haState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haState.setStatus("current")
_HaRole_Type = ArubaHaRole
_HaRole_Object = MibTableColumn
haRole = _HaRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 4),
    _HaRole_Type()
)
haRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haRole.setStatus("current")
_HaPreemption_Type = ArubaEnableValue
_HaPreemption_Object = MibTableColumn
haPreemption = _HaPreemption_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 5),
    _HaPreemption_Type()
)
haPreemption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haPreemption.setStatus("current")
_HaOversubscription_Type = ArubaEnableValue
_HaOversubscription_Object = MibTableColumn
haOversubscription = _HaOversubscription_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 6),
    _HaOversubscription_Type()
)
haOversubscription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haOversubscription.setStatus("current")
_HaStateSync_Type = ArubaEnableValue
_HaStateSync_Object = MibTableColumn
haStateSync = _HaStateSync_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 7),
    _HaStateSync_Type()
)
haStateSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haStateSync.setStatus("current")


class _HaPresharedKey_Type(DisplayString):
    """Custom type haPresharedKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 32),
    )


_HaPresharedKey_Type.__name__ = "DisplayString"
_HaPresharedKey_Object = MibTableColumn
haPresharedKey = _HaPresharedKey_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 8),
    _HaPresharedKey_Type()
)
haPresharedKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haPresharedKey.setStatus("current")
_HaIntercontrollerHbt_Type = ArubaEnableValue
_HaIntercontrollerHbt_Object = MibTableColumn
haIntercontrollerHbt = _HaIntercontrollerHbt_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 9),
    _HaIntercontrollerHbt_Type()
)
haIntercontrollerHbt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haIntercontrollerHbt.setStatus("current")
_HaHbtThreshold_Type = Unsigned32
_HaHbtThreshold_Object = MibTableColumn
haHbtThreshold = _HaHbtThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 10),
    _HaHbtThreshold_Type()
)
haHbtThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haHbtThreshold.setStatus("current")
_HaHbtInterval_Type = Unsigned32
_HaHbtInterval_Object = MibTableColumn
haHbtInterval = _HaHbtInterval_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 11),
    _HaHbtInterval_Type()
)
haHbtInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haHbtInterval.setStatus("current")
_WlsxHighAvalabilityApTable_Object = MibTable
wlsxHighAvalabilityApTable = _WlsxHighAvalabilityApTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 2)
)
if mibBuilder.loadTexts:
    wlsxHighAvalabilityApTable.setStatus("current")
_WlsxHighAvalabilityApEntry_Object = MibTableRow
wlsxHighAvalabilityApEntry = _WlsxHighAvalabilityApEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 2, 1)
)
wlsxHighAvalabilityApEntry.setIndexNames(
    (0, "WLSX-HA-MIB", "haProfileName"),
)
if mibBuilder.loadTexts:
    wlsxHighAvalabilityApEntry.setStatus("current")
_HaActiveAPs_Type = Gauge32
_HaActiveAPs_Object = MibTableColumn
haActiveAPs = _HaActiveAPs_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 2, 1, 1),
    _HaActiveAPs_Type()
)
haActiveAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haActiveAPs.setStatus("current")
_HaStandbyAPs_Type = Gauge32
_HaStandbyAPs_Object = MibTableColumn
haStandbyAPs = _HaStandbyAPs_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 2, 1, 2),
    _HaStandbyAPs_Type()
)
haStandbyAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haStandbyAPs.setStatus("current")
_HaTotalAPs_Type = Gauge32
_HaTotalAPs_Object = MibTableColumn
haTotalAPs = _HaTotalAPs_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 2, 1, 3),
    _HaTotalAPs_Type()
)
haTotalAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haTotalAPs.setStatus("current")
_WlsxIntercontrollerHbtTable_Object = MibTable
wlsxIntercontrollerHbtTable = _WlsxIntercontrollerHbtTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3)
)
if mibBuilder.loadTexts:
    wlsxIntercontrollerHbtTable.setStatus("current")
_WlsxIntercontrollerHbtEntry_Object = MibTableRow
wlsxIntercontrollerHbtEntry = _WlsxIntercontrollerHbtEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1)
)
wlsxIntercontrollerHbtEntry.setIndexNames(
    (0, "WLSX-HA-MIB", "haActiveCtrl"),
)
if mibBuilder.loadTexts:
    wlsxIntercontrollerHbtEntry.setStatus("current")


class _HaActiveCtrl_Type(DisplayString):
    """Custom type haActiveCtrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HaActiveCtrl_Type.__name__ = "DisplayString"
_HaActiveCtrl_Object = MibTableColumn
haActiveCtrl = _HaActiveCtrl_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1, 1),
    _HaActiveCtrl_Type()
)
haActiveCtrl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    haActiveCtrl.setStatus("current")


class _HaActiveCtrlIp_Type(DisplayString):
    """Custom type haActiveCtrlIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HaActiveCtrlIp_Type.__name__ = "DisplayString"
_HaActiveCtrlIp_Object = MibTableColumn
haActiveCtrlIp = _HaActiveCtrlIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1, 2),
    _HaActiveCtrlIp_Type()
)
haActiveCtrlIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haActiveCtrlIp.setStatus("current")
_HaReferenceCnt_Type = Gauge32
_HaReferenceCnt_Object = MibTableColumn
haReferenceCnt = _HaReferenceCnt_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1, 3),
    _HaReferenceCnt_Type()
)
haReferenceCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haReferenceCnt.setStatus("current")
_HaTotalHbtRequestsSent_Type = Counter32
_HaTotalHbtRequestsSent_Object = MibTableColumn
haTotalHbtRequestsSent = _HaTotalHbtRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1, 4),
    _HaTotalHbtRequestsSent_Type()
)
haTotalHbtRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haTotalHbtRequestsSent.setStatus("current")
_HaTotalHbtResponsesRcvd_Type = Counter32
_HaTotalHbtResponsesRcvd_Object = MibTableColumn
haTotalHbtResponsesRcvd = _HaTotalHbtResponsesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1, 5),
    _HaTotalHbtResponsesRcvd_Type()
)
haTotalHbtResponsesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haTotalHbtResponsesRcvd.setStatus("current")
_HaLastMissedHbtCnt_Type = Gauge32
_HaLastMissedHbtCnt_Object = MibTableColumn
haLastMissedHbtCnt = _HaLastMissedHbtCnt_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1, 6),
    _HaLastMissedHbtCnt_Type()
)
haLastMissedHbtCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haLastMissedHbtCnt.setStatus("current")


class _HaLastHbtMissedTime_Type(DisplayString):
    """Custom type haLastHbtMissedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HaLastHbtMissedTime_Type.__name__ = "DisplayString"
_HaLastHbtMissedTime_Object = MibTableColumn
haLastHbtMissedTime = _HaLastHbtMissedTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1, 7),
    _HaLastHbtMissedTime_Type()
)
haLastHbtMissedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haLastHbtMissedTime.setStatus("current")
_WlsxStateSyncTable_Object = MibTable
wlsxStateSyncTable = _WlsxStateSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4)
)
if mibBuilder.loadTexts:
    wlsxStateSyncTable.setStatus("current")
_WlsxStateSyncEntry_Object = MibTableRow
wlsxStateSyncEntry = _WlsxStateSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4, 1)
)
wlsxStateSyncEntry.setIndexNames(
    (0, "WLSX-HA-MIB", "haProfileName"),
)
if mibBuilder.loadTexts:
    wlsxStateSyncEntry.setStatus("current")
_HaActivePmkCacheEntries_Type = Gauge32
_HaActivePmkCacheEntries_Object = MibTableColumn
haActivePmkCacheEntries = _HaActivePmkCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4, 1, 1),
    _HaActivePmkCacheEntries_Type()
)
haActivePmkCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haActivePmkCacheEntries.setStatus("current")
_HaReplicatedPmkCacheEntries_Type = Gauge32
_HaReplicatedPmkCacheEntries_Object = MibTableColumn
haReplicatedPmkCacheEntries = _HaReplicatedPmkCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4, 1, 2),
    _HaReplicatedPmkCacheEntries_Type()
)
haReplicatedPmkCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haReplicatedPmkCacheEntries.setStatus("current")
_HaTotalPmkCacheEntries_Type = Gauge32
_HaTotalPmkCacheEntries_Object = MibTableColumn
haTotalPmkCacheEntries = _HaTotalPmkCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4, 1, 3),
    _HaTotalPmkCacheEntries_Type()
)
haTotalPmkCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haTotalPmkCacheEntries.setStatus("current")
_HaActiveKeyCacheEntries_Type = Gauge32
_HaActiveKeyCacheEntries_Object = MibTableColumn
haActiveKeyCacheEntries = _HaActiveKeyCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4, 1, 4),
    _HaActiveKeyCacheEntries_Type()
)
haActiveKeyCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haActiveKeyCacheEntries.setStatus("current")
_HaReplicatedKeyCacheEntries_Type = Gauge32
_HaReplicatedKeyCacheEntries_Object = MibTableColumn
haReplicatedKeyCacheEntries = _HaReplicatedKeyCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4, 1, 5),
    _HaReplicatedKeyCacheEntries_Type()
)
haReplicatedKeyCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haReplicatedKeyCacheEntries.setStatus("current")
_HaTotalKeyCacheEntries_Type = Gauge32
_HaTotalKeyCacheEntries_Object = MibTableColumn
haTotalKeyCacheEntries = _HaTotalKeyCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4, 1, 6),
    _HaTotalKeyCacheEntries_Type()
)
haTotalKeyCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haTotalKeyCacheEntries.setStatus("current")
_WlsxHighAvalabilityTunnelTable_Object = MibTable
wlsxHighAvalabilityTunnelTable = _WlsxHighAvalabilityTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 5)
)
if mibBuilder.loadTexts:
    wlsxHighAvalabilityTunnelTable.setStatus("current")
_WlsxHighAvalabilityTunnelEntry_Object = MibTableRow
wlsxHighAvalabilityTunnelEntry = _WlsxHighAvalabilityTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 5, 1)
)
wlsxHighAvalabilityTunnelEntry.setIndexNames(
    (0, "WLSX-HA-MIB", "haProfileName"),
)
if mibBuilder.loadTexts:
    wlsxHighAvalabilityTunnelEntry.setStatus("current")
_HaActiveVapTunnels_Type = Gauge32
_HaActiveVapTunnels_Object = MibTableColumn
haActiveVapTunnels = _HaActiveVapTunnels_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 5, 1, 1),
    _HaActiveVapTunnels_Type()
)
haActiveVapTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haActiveVapTunnels.setStatus("current")
_HaStandbyVapTunnels_Type = Gauge32
_HaStandbyVapTunnels_Object = MibTableColumn
haStandbyVapTunnels = _HaStandbyVapTunnels_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 5, 1, 2),
    _HaStandbyVapTunnels_Type()
)
haStandbyVapTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haStandbyVapTunnels.setStatus("current")
_HaTotalVapTunnels_Type = Gauge32
_HaTotalVapTunnels_Object = MibTableColumn
haTotalVapTunnels = _HaTotalVapTunnels_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 5, 1, 3),
    _HaTotalVapTunnels_Type()
)
haTotalVapTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haTotalVapTunnels.setStatus("current")
_HaAPHbtTunnels_Type = Gauge32
_HaAPHbtTunnels_Object = MibTableColumn
haAPHbtTunnels = _HaAPHbtTunnels_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 5, 1, 4),
    _HaAPHbtTunnels_Type()
)
haAPHbtTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haAPHbtTunnels.setStatus("current")
_WlsxHighAvalabilityTraps_ObjectIdentity = ObjectIdentity
wlsxHighAvalabilityTraps = _WlsxHighAvalabilityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2)
)
_WlsxHaTrapObjectsGroup_ObjectIdentity = ObjectIdentity
wlsxHaTrapObjectsGroup = _WlsxHaTrapObjectsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1)
)
_WlsxHaV4Status_Type = ArubaEnableValue
_WlsxHaV4Status_Object = MibScalar
wlsxHaV4Status = _WlsxHaV4Status_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 1),
    _WlsxHaV4Status_Type()
)
wlsxHaV4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxHaV4Status.setStatus("current")
_WlsxHaV4Role_Type = ArubaHaRole
_WlsxHaV4Role_Object = MibScalar
wlsxHaV4Role = _WlsxHaV4Role_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 2),
    _WlsxHaV4Role_Type()
)
wlsxHaV4Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxHaV4Role.setStatus("current")
_WlsxHaV6Status_Type = ArubaEnableValue
_WlsxHaV6Status_Object = MibScalar
wlsxHaV6Status = _WlsxHaV6Status_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 3),
    _WlsxHaV6Status_Type()
)
wlsxHaV6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxHaV6Status.setStatus("current")
_WlsxHaV6Role_Type = ArubaHaRole
_WlsxHaV6Role_Object = MibScalar
wlsxHaV6Role = _WlsxHaV6Role_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 4),
    _WlsxHaV6Role_Type()
)
wlsxHaV6Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxHaV6Role.setStatus("current")


class _WlsxHaAPName_Type(DisplayString):
    """Custom type wlsxHaAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_WlsxHaAPName_Type.__name__ = "DisplayString"
_WlsxHaAPName_Object = MibScalar
wlsxHaAPName = _WlsxHaAPName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 5),
    _WlsxHaAPName_Type()
)
wlsxHaAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxHaAPName.setStatus("current")


class _WlsxHaActiveControllerIp_Type(DisplayString):
    """Custom type wlsxHaActiveControllerIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_WlsxHaActiveControllerIp_Type.__name__ = "DisplayString"
_WlsxHaActiveControllerIp_Object = MibScalar
wlsxHaActiveControllerIp = _WlsxHaActiveControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 6),
    _WlsxHaActiveControllerIp_Type()
)
wlsxHaActiveControllerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxHaActiveControllerIp.setStatus("current")


class _WlsxHaStandbyControllerIp_Type(DisplayString):
    """Custom type wlsxHaStandbyControllerIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_WlsxHaStandbyControllerIp_Type.__name__ = "DisplayString"
_WlsxHaStandbyControllerIp_Object = MibScalar
wlsxHaStandbyControllerIp = _WlsxHaStandbyControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 7),
    _WlsxHaStandbyControllerIp_Type()
)
wlsxHaStandbyControllerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxHaStandbyControllerIp.setStatus("current")
_WlsxTrapHaConnectivityStatus_Type = ArubaHaConnectivityStatus
_WlsxTrapHaConnectivityStatus_Object = MibScalar
wlsxTrapHaConnectivityStatus = _WlsxTrapHaConnectivityStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 8),
    _WlsxTrapHaConnectivityStatus_Type()
)
wlsxTrapHaConnectivityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxTrapHaConnectivityStatus.setStatus("current")
_WlsxTrapHaIntercontrollerHbtMissCnt_Type = Integer32
_WlsxTrapHaIntercontrollerHbtMissCnt_Object = MibScalar
wlsxTrapHaIntercontrollerHbtMissCnt = _WlsxTrapHaIntercontrollerHbtMissCnt_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 9),
    _WlsxTrapHaIntercontrollerHbtMissCnt_Type()
)
wlsxTrapHaIntercontrollerHbtMissCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxTrapHaIntercontrollerHbtMissCnt.setStatus("current")


class _WlsxTrapHaHbtMissTimeStamp_Type(DisplayString):
    """Custom type wlsxTrapHaHbtMissTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_WlsxTrapHaHbtMissTimeStamp_Type.__name__ = "DisplayString"
_WlsxTrapHaHbtMissTimeStamp_Object = MibScalar
wlsxTrapHaHbtMissTimeStamp = _WlsxTrapHaHbtMissTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 10),
    _WlsxTrapHaHbtMissTimeStamp_Type()
)
wlsxTrapHaHbtMissTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxTrapHaHbtMissTimeStamp.setStatus("current")
_WlsxTrapHaStandbyApCnt_Type = Integer32
_WlsxTrapHaStandbyApCnt_Object = MibScalar
wlsxTrapHaStandbyApCnt = _WlsxTrapHaStandbyApCnt_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 11),
    _WlsxTrapHaStandbyApCnt_Type()
)
wlsxTrapHaStandbyApCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxTrapHaStandbyApCnt.setStatus("current")
_WlsxHaTrapDefinitionGroup_ObjectIdentity = ObjectIdentity
wlsxHaTrapDefinitionGroup = _WlsxHaTrapDefinitionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 2)
)

# Managed Objects groups


# Notification objects

wlsxHaState = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 2, 1)
)
wlsxHaState.setObjects(
      *(("WLSX-HA-MIB", "wlsxHaV4Status"),
        ("WLSX-HA-MIB", "wlsxHaV4Role"),
        ("WLSX-HA-MIB", "wlsxHaV6Status"),
        ("WLSX-HA-MIB", "wlsxHaV6Role"))
)
if mibBuilder.loadTexts:
    wlsxHaState.setStatus(
        "current"
    )

wlsxHaStandbyIpSentFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 2, 2)
)
wlsxHaStandbyIpSentFailed.setObjects(
      *(("WLSX-HA-MIB", "wlsxHaStandbyControllerIp"),
        ("WLSX-HA-MIB", "wlsxHaAPName"))
)
if mibBuilder.loadTexts:
    wlsxHaStandbyIpSentFailed.setStatus(
        "current"
    )

wlsxHaStandbyConnectivityState = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 2, 3)
)
wlsxHaStandbyConnectivityState.setObjects(
      *(("WLSX-HA-MIB", "wlsxHaAPName"),
        ("WLSX-HA-MIB", "wlsxHaStandbyControllerIp"),
        ("WLSX-HA-MIB", "wlsxTrapHaConnectivityStatus"))
)
if mibBuilder.loadTexts:
    wlsxHaStandbyConnectivityState.setStatus(
        "current"
    )

wlsxHaIntercontrollerHbtMiss = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 2, 4)
)
wlsxHaIntercontrollerHbtMiss.setObjects(
      *(("WLSX-HA-MIB", "wlsxTrapHaIntercontrollerHbtMissCnt"),
        ("WLSX-HA-MIB", "wlsxHaActiveControllerIp"),
        ("WLSX-HA-MIB", "wlsxTrapHaHbtMissTimeStamp"))
)
if mibBuilder.loadTexts:
    wlsxHaIntercontrollerHbtMiss.setStatus(
        "current"
    )

wlsxHaFailoverTrigger = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 2, 5)
)
wlsxHaFailoverTrigger.setObjects(
      *(("WLSX-HA-MIB", "wlsxHaActiveControllerIp"),
        ("WLSX-HA-MIB", "wlsxTrapHaStandbyApCnt"))
)
if mibBuilder.loadTexts:
    wlsxHaFailoverTrigger.setStatus(
        "current"
    )

wlsxHaFailoverRequestFromAp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 2, 6)
)
wlsxHaFailoverRequestFromAp.setObjects(
    ("WLSX-HA-MIB", "wlsxHaAPName")
)
if mibBuilder.loadTexts:
    wlsxHaFailoverRequestFromAp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-HA-MIB",
    **{"wlsxHaMIB": wlsxHaMIB,
       "wlsxHighAvalabilityInfoGroup": wlsxHighAvalabilityInfoGroup,
       "wlsxHighAvalabilityConfigTable": wlsxHighAvalabilityConfigTable,
       "wlsxHighAvalabilityConfigEntry": wlsxHighAvalabilityConfigEntry,
       "haProfileName": haProfileName,
       "haMembership": haMembership,
       "haState": haState,
       "haRole": haRole,
       "haPreemption": haPreemption,
       "haOversubscription": haOversubscription,
       "haStateSync": haStateSync,
       "haPresharedKey": haPresharedKey,
       "haIntercontrollerHbt": haIntercontrollerHbt,
       "haHbtThreshold": haHbtThreshold,
       "haHbtInterval": haHbtInterval,
       "wlsxHighAvalabilityApTable": wlsxHighAvalabilityApTable,
       "wlsxHighAvalabilityApEntry": wlsxHighAvalabilityApEntry,
       "haActiveAPs": haActiveAPs,
       "haStandbyAPs": haStandbyAPs,
       "haTotalAPs": haTotalAPs,
       "wlsxIntercontrollerHbtTable": wlsxIntercontrollerHbtTable,
       "wlsxIntercontrollerHbtEntry": wlsxIntercontrollerHbtEntry,
       "haActiveCtrl": haActiveCtrl,
       "haActiveCtrlIp": haActiveCtrlIp,
       "haReferenceCnt": haReferenceCnt,
       "haTotalHbtRequestsSent": haTotalHbtRequestsSent,
       "haTotalHbtResponsesRcvd": haTotalHbtResponsesRcvd,
       "haLastMissedHbtCnt": haLastMissedHbtCnt,
       "haLastHbtMissedTime": haLastHbtMissedTime,
       "wlsxStateSyncTable": wlsxStateSyncTable,
       "wlsxStateSyncEntry": wlsxStateSyncEntry,
       "haActivePmkCacheEntries": haActivePmkCacheEntries,
       "haReplicatedPmkCacheEntries": haReplicatedPmkCacheEntries,
       "haTotalPmkCacheEntries": haTotalPmkCacheEntries,
       "haActiveKeyCacheEntries": haActiveKeyCacheEntries,
       "haReplicatedKeyCacheEntries": haReplicatedKeyCacheEntries,
       "haTotalKeyCacheEntries": haTotalKeyCacheEntries,
       "wlsxHighAvalabilityTunnelTable": wlsxHighAvalabilityTunnelTable,
       "wlsxHighAvalabilityTunnelEntry": wlsxHighAvalabilityTunnelEntry,
       "haActiveVapTunnels": haActiveVapTunnels,
       "haStandbyVapTunnels": haStandbyVapTunnels,
       "haTotalVapTunnels": haTotalVapTunnels,
       "haAPHbtTunnels": haAPHbtTunnels,
       "wlsxHighAvalabilityTraps": wlsxHighAvalabilityTraps,
       "wlsxHaTrapObjectsGroup": wlsxHaTrapObjectsGroup,
       "wlsxHaV4Status": wlsxHaV4Status,
       "wlsxHaV4Role": wlsxHaV4Role,
       "wlsxHaV6Status": wlsxHaV6Status,
       "wlsxHaV6Role": wlsxHaV6Role,
       "wlsxHaAPName": wlsxHaAPName,
       "wlsxHaActiveControllerIp": wlsxHaActiveControllerIp,
       "wlsxHaStandbyControllerIp": wlsxHaStandbyControllerIp,
       "wlsxTrapHaConnectivityStatus": wlsxTrapHaConnectivityStatus,
       "wlsxTrapHaIntercontrollerHbtMissCnt": wlsxTrapHaIntercontrollerHbtMissCnt,
       "wlsxTrapHaHbtMissTimeStamp": wlsxTrapHaHbtMissTimeStamp,
       "wlsxTrapHaStandbyApCnt": wlsxTrapHaStandbyApCnt,
       "wlsxHaTrapDefinitionGroup": wlsxHaTrapDefinitionGroup,
       "wlsxHaState": wlsxHaState,
       "wlsxHaStandbyIpSentFailed": wlsxHaStandbyIpSentFailed,
       "wlsxHaStandbyConnectivityState": wlsxHaStandbyConnectivityState,
       "wlsxHaIntercontrollerHbtMiss": wlsxHaIntercontrollerHbtMiss,
       "wlsxHaFailoverTrigger": wlsxHaFailoverTrigger,
       "wlsxHaFailoverRequestFromAp": wlsxHaFailoverRequestFromAp}
)
