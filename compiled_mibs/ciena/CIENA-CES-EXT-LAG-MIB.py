# SNMP MIB module (CIENA-CES-EXT-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-EXT-LAG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:35 2025
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
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesExtLagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cienaCesExtLagMIB.setRevisions(
        ("2018-02-13 00:00",
         "2017-06-07 00:00",
         "2016-09-28 00:00",
         "2016-09-16 00:00",
         "2016-09-14 00:00",
         "2016-09-07 00:00",
         "2016-08-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesExtLagMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesExtLagMIBObjects = _CienaCesExtLagMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1)
)
_CienaCesExtLag_ObjectIdentity = ObjectIdentity
cienaCesExtLag = _CienaCesExtLag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1)
)
_CienaCesMaxLags_Type = Unsigned32
_CienaCesMaxLags_Object = MibScalar
cienaCesMaxLags = _CienaCesMaxLags_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 1),
    _CienaCesMaxLags_Type()
)
cienaCesMaxLags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesMaxLags.setStatus("current")
_CienaCesNumLags_Type = Unsigned32
_CienaCesNumLags_Object = MibScalar
cienaCesNumLags = _CienaCesNumLags_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 2),
    _CienaCesNumLags_Type()
)
cienaCesNumLags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesNumLags.setStatus("current")
_CienaCesExtLagTable_Object = MibTable
cienaCesExtLagTable = _CienaCesExtLagTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cienaCesExtLagTable.setStatus("current")
_CienaCesExtLagEntry_Object = MibTableRow
cienaCesExtLagEntry = _CienaCesExtLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1)
)
cienaCesExtLagEntry.setIndexNames(
    (0, "CIENA-CES-EXT-LAG-MIB", "cienaCesExtAggId"),
)
if mibBuilder.loadTexts:
    cienaCesExtLagEntry.setStatus("current")


class _CienaCesExtAggId_Type(Integer32):
    """Custom type cienaCesExtAggId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CienaCesExtAggId_Type.__name__ = "Integer32"
_CienaCesExtAggId_Object = MibTableColumn
cienaCesExtAggId = _CienaCesExtAggId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 1),
    _CienaCesExtAggId_Type()
)
cienaCesExtAggId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggId.setStatus("current")


class _CienaCesExtAggName_Type(DisplayString):
    """Custom type cienaCesExtAggName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesExtAggName_Type.__name__ = "DisplayString"
_CienaCesExtAggName_Object = MibTableColumn
cienaCesExtAggName = _CienaCesExtAggName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 2),
    _CienaCesExtAggName_Type()
)
cienaCesExtAggName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggName.setStatus("current")


class _CienaCesExtAggIndex_Type(Integer32):
    """Custom type cienaCesExtAggIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CienaCesExtAggIndex_Type.__name__ = "Integer32"
_CienaCesExtAggIndex_Object = MibTableColumn
cienaCesExtAggIndex = _CienaCesExtAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 3),
    _CienaCesExtAggIndex_Type()
)
cienaCesExtAggIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggIndex.setStatus("current")


class _CienaCesExtAggMode_Type(Integer32):
    """Custom type cienaCesExtAggMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lacp", 1),
          ("manual", 2))
    )


_CienaCesExtAggMode_Type.__name__ = "Integer32"
_CienaCesExtAggMode_Object = MibTableColumn
cienaCesExtAggMode = _CienaCesExtAggMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 4),
    _CienaCesExtAggMode_Type()
)
cienaCesExtAggMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggMode.setStatus("current")


class _CienaCesExtLagProtectionRevertState_Type(Integer32):
    """Custom type cienaCesExtLagProtectionRevertState based on Integer32"""
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


_CienaCesExtLagProtectionRevertState_Type.__name__ = "Integer32"
_CienaCesExtLagProtectionRevertState_Object = MibTableColumn
cienaCesExtLagProtectionRevertState = _CienaCesExtLagProtectionRevertState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 5),
    _CienaCesExtLagProtectionRevertState_Type()
)
cienaCesExtLagProtectionRevertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtLagProtectionRevertState.setStatus("current")


class _CienaCesExtLagProtectionRevertTimer_Type(Integer32):
    """Custom type cienaCesExtLagProtectionRevertTimer based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_CienaCesExtLagProtectionRevertTimer_Type.__name__ = "Integer32"
_CienaCesExtLagProtectionRevertTimer_Object = MibTableColumn
cienaCesExtLagProtectionRevertTimer = _CienaCesExtLagProtectionRevertTimer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 6),
    _CienaCesExtLagProtectionRevertTimer_Type()
)
cienaCesExtLagProtectionRevertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtLagProtectionRevertTimer.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesExtLagProtectionRevertTimer.setUnits("msec")
_CienaCesExtAggTotalAddedPorts_Type = Unsigned32
_CienaCesExtAggTotalAddedPorts_Object = MibTableColumn
cienaCesExtAggTotalAddedPorts = _CienaCesExtAggTotalAddedPorts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 7),
    _CienaCesExtAggTotalAddedPorts_Type()
)
cienaCesExtAggTotalAddedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggTotalAddedPorts.setStatus("current")
_CienaCesExtAggTotalProtectionPorts_Type = Unsigned32
_CienaCesExtAggTotalProtectionPorts_Object = MibTableColumn
cienaCesExtAggTotalProtectionPorts = _CienaCesExtAggTotalProtectionPorts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 8),
    _CienaCesExtAggTotalProtectionPorts_Type()
)
cienaCesExtAggTotalProtectionPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggTotalProtectionPorts.setStatus("current")


class _CienaCesExtLagProtectionMode_Type(Integer32):
    """Custom type cienaCesExtLagProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("proprietary", 1),
          ("standard", 2),
          ("none", 3))
    )


_CienaCesExtLagProtectionMode_Type.__name__ = "Integer32"
_CienaCesExtLagProtectionMode_Object = MibTableColumn
cienaCesExtLagProtectionMode = _CienaCesExtLagProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 9),
    _CienaCesExtLagProtectionMode_Type()
)
cienaCesExtLagProtectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtLagProtectionMode.setStatus("current")
_CienaCesExtAggICL_Type = DisplayString
_CienaCesExtAggICL_Object = MibTableColumn
cienaCesExtAggICL = _CienaCesExtAggICL_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 10),
    _CienaCesExtAggICL_Type()
)
cienaCesExtAggICL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggICL.setStatus("current")


class _CienaCesExtAggRole_Type(Integer32):
    """Custom type cienaCesExtAggRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2),
          ("none", 3))
    )


_CienaCesExtAggRole_Type.__name__ = "Integer32"
_CienaCesExtAggRole_Object = MibTableColumn
cienaCesExtAggRole = _CienaCesExtAggRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 11),
    _CienaCesExtAggRole_Type()
)
cienaCesExtAggRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggRole.setStatus("current")
_CienaCesExtAggRgNodeId_Type = Unsigned32
_CienaCesExtAggRgNodeId_Object = MibTableColumn
cienaCesExtAggRgNodeId = _CienaCesExtAggRgNodeId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 12),
    _CienaCesExtAggRgNodeId_Type()
)
cienaCesExtAggRgNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggRgNodeId.setStatus("current")
_CienaCesExtAggRgDynamicPriority_Type = Unsigned32
_CienaCesExtAggRgDynamicPriority_Object = MibTableColumn
cienaCesExtAggRgDynamicPriority = _CienaCesExtAggRgDynamicPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 13),
    _CienaCesExtAggRgDynamicPriority_Type()
)
cienaCesExtAggRgDynamicPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggRgDynamicPriority.setStatus("current")
_CienaCesExtAggRgOperKey_Type = Unsigned32
_CienaCesExtAggRgOperKey_Object = MibTableColumn
cienaCesExtAggRgOperKey = _CienaCesExtAggRgOperKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 14),
    _CienaCesExtAggRgOperKey_Type()
)
cienaCesExtAggRgOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggRgOperKey.setStatus("current")


class _CienaCesExtAggRedundancyState_Type(Integer32):
    """Custom type cienaCesExtAggRedundancyState based on Integer32"""
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
        *(("down", 1),
          ("unavailable", 2),
          ("active", 3),
          ("standby", 4),
          ("standalone", 5),
          ("none", 6))
    )


_CienaCesExtAggRedundancyState_Type.__name__ = "Integer32"
_CienaCesExtAggRedundancyState_Object = MibTableColumn
cienaCesExtAggRedundancyState = _CienaCesExtAggRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 15),
    _CienaCesExtAggRedundancyState_Type()
)
cienaCesExtAggRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggRedundancyState.setStatus("current")


class _CienaCesExtAggConnectState_Type(Integer32):
    """Custom type cienaCesExtAggConnectState based on Integer32"""
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
        *(("init", 1),
          ("disconnected", 2),
          ("connected", 3),
          ("mismatch", 4),
          ("none", 5))
    )


_CienaCesExtAggConnectState_Type.__name__ = "Integer32"
_CienaCesExtAggConnectState_Object = MibTableColumn
cienaCesExtAggConnectState = _CienaCesExtAggConnectState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 16),
    _CienaCesExtAggConnectState_Type()
)
cienaCesExtAggConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggConnectState.setStatus("current")


class _CienaCesExtAggRgMismatchStatus_Type(Integer32):
    """Custom type cienaCesExtAggRgMismatchStatus based on Integer32"""
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
        *(("no", 1),
          ("rgpeer", 2),
          ("partner", 3),
          ("version", 4),
          ("none", 5))
    )


_CienaCesExtAggRgMismatchStatus_Type.__name__ = "Integer32"
_CienaCesExtAggRgMismatchStatus_Object = MibTableColumn
cienaCesExtAggRgMismatchStatus = _CienaCesExtAggRgMismatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 17),
    _CienaCesExtAggRgMismatchStatus_Type()
)
cienaCesExtAggRgMismatchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggRgMismatchStatus.setStatus("current")
_CienaCesExtAggPeerSystemMac_Type = MacAddress
_CienaCesExtAggPeerSystemMac_Object = MibTableColumn
cienaCesExtAggPeerSystemMac = _CienaCesExtAggPeerSystemMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 18),
    _CienaCesExtAggPeerSystemMac_Type()
)
cienaCesExtAggPeerSystemMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggPeerSystemMac.setStatus("current")
_CienaCesExtAggPeerRgNodeId_Type = Unsigned32
_CienaCesExtAggPeerRgNodeId_Object = MibTableColumn
cienaCesExtAggPeerRgNodeId = _CienaCesExtAggPeerRgNodeId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 19),
    _CienaCesExtAggPeerRgNodeId_Type()
)
cienaCesExtAggPeerRgNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggPeerRgNodeId.setStatus("current")
_CienaCesExtAggPeerRgDynamicPriority_Type = Unsigned32
_CienaCesExtAggPeerRgDynamicPriority_Object = MibTableColumn
cienaCesExtAggPeerRgDynamicPriority = _CienaCesExtAggPeerRgDynamicPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 20),
    _CienaCesExtAggPeerRgDynamicPriority_Type()
)
cienaCesExtAggPeerRgDynamicPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggPeerRgDynamicPriority.setStatus("current")
_CienaCesExtAggPeerRgOperKey_Type = Unsigned32
_CienaCesExtAggPeerRgOperKey_Object = MibTableColumn
cienaCesExtAggPeerRgOperKey = _CienaCesExtAggPeerRgOperKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 21),
    _CienaCesExtAggPeerRgOperKey_Type()
)
cienaCesExtAggPeerRgOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggPeerRgOperKey.setStatus("current")
_CienaCesExtAggPeerRgNumAddedPorts_Type = Unsigned32
_CienaCesExtAggPeerRgNumAddedPorts_Object = MibTableColumn
cienaCesExtAggPeerRgNumAddedPorts = _CienaCesExtAggPeerRgNumAddedPorts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 22),
    _CienaCesExtAggPeerRgNumAddedPorts_Type()
)
cienaCesExtAggPeerRgNumAddedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggPeerRgNumAddedPorts.setStatus("current")
_CienaCesExtAggPeerRgNumAvailablePorts_Type = Unsigned32
_CienaCesExtAggPeerRgNumAvailablePorts_Object = MibTableColumn
cienaCesExtAggPeerRgNumAvailablePorts = _CienaCesExtAggPeerRgNumAvailablePorts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 23),
    _CienaCesExtAggPeerRgNumAvailablePorts_Type()
)
cienaCesExtAggPeerRgNumAvailablePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggPeerRgNumAvailablePorts.setStatus("current")
_CienaCesExtAggDisconnectRx_Type = Counter32
_CienaCesExtAggDisconnectRx_Object = MibTableColumn
cienaCesExtAggDisconnectRx = _CienaCesExtAggDisconnectRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 24),
    _CienaCesExtAggDisconnectRx_Type()
)
cienaCesExtAggDisconnectRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggDisconnectRx.setStatus("current")
_CienaCesExtAggDisconnectTx_Type = Counter32
_CienaCesExtAggDisconnectTx_Object = MibTableColumn
cienaCesExtAggDisconnectTx = _CienaCesExtAggDisconnectTx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 25),
    _CienaCesExtAggDisconnectTx_Type()
)
cienaCesExtAggDisconnectTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggDisconnectTx.setStatus("current")
_CienaCesExtAggConfigMismatchRx_Type = Counter32
_CienaCesExtAggConfigMismatchRx_Object = MibTableColumn
cienaCesExtAggConfigMismatchRx = _CienaCesExtAggConfigMismatchRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 26),
    _CienaCesExtAggConfigMismatchRx_Type()
)
cienaCesExtAggConfigMismatchRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggConfigMismatchRx.setStatus("current")
_CienaCesExtAggKeyMismatchCount_Type = Counter32
_CienaCesExtAggKeyMismatchCount_Object = MibTableColumn
cienaCesExtAggKeyMismatchCount = _CienaCesExtAggKeyMismatchCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 27),
    _CienaCesExtAggKeyMismatchCount_Type()
)
cienaCesExtAggKeyMismatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggKeyMismatchCount.setStatus("current")
_CienaCesExtAggOutOfSequenceRx_Type = Counter32
_CienaCesExtAggOutOfSequenceRx_Object = MibTableColumn
cienaCesExtAggOutOfSequenceRx = _CienaCesExtAggOutOfSequenceRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 28),
    _CienaCesExtAggOutOfSequenceRx_Type()
)
cienaCesExtAggOutOfSequenceRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggOutOfSequenceRx.setStatus("current")
_CienaCesExtAggPeerUnreachableCount_Type = Counter32
_CienaCesExtAggPeerUnreachableCount_Object = MibTableColumn
cienaCesExtAggPeerUnreachableCount = _CienaCesExtAggPeerUnreachableCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 29),
    _CienaCesExtAggPeerUnreachableCount_Type()
)
cienaCesExtAggPeerUnreachableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggPeerUnreachableCount.setStatus("current")
_CienaCesExtAggUnknownRx_Type = Counter32
_CienaCesExtAggUnknownRx_Object = MibTableColumn
cienaCesExtAggUnknownRx = _CienaCesExtAggUnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 30),
    _CienaCesExtAggUnknownRx_Type()
)
cienaCesExtAggUnknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggUnknownRx.setStatus("current")
_CienaCesExtAggTotalRx_Type = Counter32
_CienaCesExtAggTotalRx_Object = MibTableColumn
cienaCesExtAggTotalRx = _CienaCesExtAggTotalRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 31),
    _CienaCesExtAggTotalRx_Type()
)
cienaCesExtAggTotalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggTotalRx.setStatus("current")
_CienaCesExtAggTotalTx_Type = Counter32
_CienaCesExtAggTotalTx_Object = MibTableColumn
cienaCesExtAggTotalTx = _CienaCesExtAggTotalTx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 32),
    _CienaCesExtAggTotalTx_Type()
)
cienaCesExtAggTotalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggTotalTx.setStatus("current")
_CienaCesExtAggTotalDownTime_Type = Unsigned32
_CienaCesExtAggTotalDownTime_Object = MibTableColumn
cienaCesExtAggTotalDownTime = _CienaCesExtAggTotalDownTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 33),
    _CienaCesExtAggTotalDownTime_Type()
)
cienaCesExtAggTotalDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggTotalDownTime.setStatus("current")
_CienaCesExtAggUpTime_Type = Unsigned32
_CienaCesExtAggUpTime_Object = MibTableColumn
cienaCesExtAggUpTime = _CienaCesExtAggUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 34),
    _CienaCesExtAggUpTime_Type()
)
cienaCesExtAggUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggUpTime.setStatus("current")
_CienaCesExtAggTimeInProtectState_Type = Unsigned32
_CienaCesExtAggTimeInProtectState_Object = MibTableColumn
cienaCesExtAggTimeInProtectState = _CienaCesExtAggTimeInProtectState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 35),
    _CienaCesExtAggTimeInProtectState_Type()
)
cienaCesExtAggTimeInProtectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggTimeInProtectState.setStatus("current")
_CienaCesExtAggLastTimeProtected_Type = Unsigned32
_CienaCesExtAggLastTimeProtected_Object = MibTableColumn
cienaCesExtAggLastTimeProtected = _CienaCesExtAggLastTimeProtected_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 36),
    _CienaCesExtAggLastTimeProtected_Type()
)
cienaCesExtAggLastTimeProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggLastTimeProtected.setStatus("current")
_CienaCesExtAggNumberOfSwitchovers_Type = Counter32
_CienaCesExtAggNumberOfSwitchovers_Object = MibTableColumn
cienaCesExtAggNumberOfSwitchovers = _CienaCesExtAggNumberOfSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 37),
    _CienaCesExtAggNumberOfSwitchovers_Type()
)
cienaCesExtAggNumberOfSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggNumberOfSwitchovers.setStatus("current")


class _CienaCesExtAggMultiChassis_Type(Integer32):
    """Custom type cienaCesExtAggMultiChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_CienaCesExtAggMultiChassis_Type.__name__ = "Integer32"
_CienaCesExtAggMultiChassis_Object = MibTableColumn
cienaCesExtAggMultiChassis = _CienaCesExtAggMultiChassis_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 38),
    _CienaCesExtAggMultiChassis_Type()
)
cienaCesExtAggMultiChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggMultiChassis.setStatus("current")


class _CienaCesExtAggMinimumLinkAggregation_Type(Integer32):
    """Custom type cienaCesExtAggMinimumLinkAggregation based on Integer32"""
    defaultValue = 2

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


_CienaCesExtAggMinimumLinkAggregation_Type.__name__ = "Integer32"
_CienaCesExtAggMinimumLinkAggregation_Object = MibTableColumn
cienaCesExtAggMinimumLinkAggregation = _CienaCesExtAggMinimumLinkAggregation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 39),
    _CienaCesExtAggMinimumLinkAggregation_Type()
)
cienaCesExtAggMinimumLinkAggregation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggMinimumLinkAggregation.setStatus("current")


class _CienaCesExtAggMinimumLinkThreshold_Type(Integer32):
    """Custom type cienaCesExtAggMinimumLinkThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesExtAggMinimumLinkThreshold_Type.__name__ = "Integer32"
_CienaCesExtAggMinimumLinkThreshold_Object = MibTableColumn
cienaCesExtAggMinimumLinkThreshold = _CienaCesExtAggMinimumLinkThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 40),
    _CienaCesExtAggMinimumLinkThreshold_Type()
)
cienaCesExtAggMinimumLinkThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggMinimumLinkThreshold.setStatus("current")


class _CienaCesExtAggAdminState_Type(Integer32):
    """Custom type cienaCesExtAggAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_CienaCesExtAggAdminState_Type.__name__ = "Integer32"
_CienaCesExtAggAdminState_Object = MibTableColumn
cienaCesExtAggAdminState = _CienaCesExtAggAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 41),
    _CienaCesExtAggAdminState_Type()
)
cienaCesExtAggAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggAdminState.setStatus("current")


class _CienaCesExtAggOperState_Type(Integer32):
    """Custom type cienaCesExtAggOperState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_CienaCesExtAggOperState_Type.__name__ = "Integer32"
_CienaCesExtAggOperState_Object = MibTableColumn
cienaCesExtAggOperState = _CienaCesExtAggOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 3, 1, 42),
    _CienaCesExtAggOperState_Type()
)
cienaCesExtAggOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggOperState.setStatus("current")
_CienaCesLagProtectionTable_Object = MibTable
cienaCesLagProtectionTable = _CienaCesLagProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cienaCesLagProtectionTable.setStatus("current")
_CienaCesLagProtectionEntry_Object = MibTableRow
cienaCesLagProtectionEntry = _CienaCesLagProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 4, 1)
)
cienaCesLagProtectionEntry.setIndexNames(
    (0, "CIENA-CES-EXT-LAG-MIB", "cienaCesExtAggId"),
    (0, "CIENA-CES-EXT-LAG-MIB", "cienaCesLagProtectionPort"),
)
if mibBuilder.loadTexts:
    cienaCesLagProtectionEntry.setStatus("current")


class _CienaCesLagProtectionPort_Type(Integer32):
    """Custom type cienaCesLagProtectionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesLagProtectionPort_Type.__name__ = "Integer32"
_CienaCesLagProtectionPort_Object = MibTableColumn
cienaCesLagProtectionPort = _CienaCesLagProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 4, 1, 1),
    _CienaCesLagProtectionPort_Type()
)
cienaCesLagProtectionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLagProtectionPort.setStatus("current")


class _CienaCesExtAggMarkerTimeout_Type(Unsigned32):
    """Custom type cienaCesExtAggMarkerTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CienaCesExtAggMarkerTimeout_Type.__name__ = "Unsigned32"
_CienaCesExtAggMarkerTimeout_Object = MibScalar
cienaCesExtAggMarkerTimeout = _CienaCesExtAggMarkerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 1, 1, 5),
    _CienaCesExtAggMarkerTimeout_Type()
)
cienaCesExtAggMarkerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAggMarkerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesExtAggMarkerTimeout.setUnits("msec")
_CienaCesExtLagMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesExtLagMIBConformance = _CienaCesExtLagMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 2)
)
_CienaCesExtLagMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesExtLagMIBCompliances = _CienaCesExtLagMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 2, 1)
)
_CienaCesExtLagMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesExtLagMIBGroups = _CienaCesExtLagMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 3, 2, 2)
)
_CienaCesExtLagMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesExtLagMIBNotificationPrefix = _CienaCesExtLagMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 21)
)
_CienaCesExtLagMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesExtLagMIBNotifications = _CienaCesExtLagMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 21, 0)
)

# Managed Objects groups


# Notification objects

cienaCesExtLagMclagStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 21, 0, 1)
)
cienaCesExtLagMclagStateChange.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-EXT-LAG-MIB", "cienaCesExtAggIndex"),
        ("CIENA-CES-EXT-LAG-MIB", "cienaCesExtAggRedundancyState"))
)
if mibBuilder.loadTexts:
    cienaCesExtLagMclagStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-EXT-LAG-MIB",
    **{"cienaCesExtLagMIB": cienaCesExtLagMIB,
       "cienaCesExtLagMIBObjects": cienaCesExtLagMIBObjects,
       "cienaCesExtLag": cienaCesExtLag,
       "cienaCesMaxLags": cienaCesMaxLags,
       "cienaCesNumLags": cienaCesNumLags,
       "cienaCesExtLagTable": cienaCesExtLagTable,
       "cienaCesExtLagEntry": cienaCesExtLagEntry,
       "cienaCesExtAggId": cienaCesExtAggId,
       "cienaCesExtAggName": cienaCesExtAggName,
       "cienaCesExtAggIndex": cienaCesExtAggIndex,
       "cienaCesExtAggMode": cienaCesExtAggMode,
       "cienaCesExtLagProtectionRevertState": cienaCesExtLagProtectionRevertState,
       "cienaCesExtLagProtectionRevertTimer": cienaCesExtLagProtectionRevertTimer,
       "cienaCesExtAggTotalAddedPorts": cienaCesExtAggTotalAddedPorts,
       "cienaCesExtAggTotalProtectionPorts": cienaCesExtAggTotalProtectionPorts,
       "cienaCesExtLagProtectionMode": cienaCesExtLagProtectionMode,
       "cienaCesExtAggICL": cienaCesExtAggICL,
       "cienaCesExtAggRole": cienaCesExtAggRole,
       "cienaCesExtAggRgNodeId": cienaCesExtAggRgNodeId,
       "cienaCesExtAggRgDynamicPriority": cienaCesExtAggRgDynamicPriority,
       "cienaCesExtAggRgOperKey": cienaCesExtAggRgOperKey,
       "cienaCesExtAggRedundancyState": cienaCesExtAggRedundancyState,
       "cienaCesExtAggConnectState": cienaCesExtAggConnectState,
       "cienaCesExtAggRgMismatchStatus": cienaCesExtAggRgMismatchStatus,
       "cienaCesExtAggPeerSystemMac": cienaCesExtAggPeerSystemMac,
       "cienaCesExtAggPeerRgNodeId": cienaCesExtAggPeerRgNodeId,
       "cienaCesExtAggPeerRgDynamicPriority": cienaCesExtAggPeerRgDynamicPriority,
       "cienaCesExtAggPeerRgOperKey": cienaCesExtAggPeerRgOperKey,
       "cienaCesExtAggPeerRgNumAddedPorts": cienaCesExtAggPeerRgNumAddedPorts,
       "cienaCesExtAggPeerRgNumAvailablePorts": cienaCesExtAggPeerRgNumAvailablePorts,
       "cienaCesExtAggDisconnectRx": cienaCesExtAggDisconnectRx,
       "cienaCesExtAggDisconnectTx": cienaCesExtAggDisconnectTx,
       "cienaCesExtAggConfigMismatchRx": cienaCesExtAggConfigMismatchRx,
       "cienaCesExtAggKeyMismatchCount": cienaCesExtAggKeyMismatchCount,
       "cienaCesExtAggOutOfSequenceRx": cienaCesExtAggOutOfSequenceRx,
       "cienaCesExtAggPeerUnreachableCount": cienaCesExtAggPeerUnreachableCount,
       "cienaCesExtAggUnknownRx": cienaCesExtAggUnknownRx,
       "cienaCesExtAggTotalRx": cienaCesExtAggTotalRx,
       "cienaCesExtAggTotalTx": cienaCesExtAggTotalTx,
       "cienaCesExtAggTotalDownTime": cienaCesExtAggTotalDownTime,
       "cienaCesExtAggUpTime": cienaCesExtAggUpTime,
       "cienaCesExtAggTimeInProtectState": cienaCesExtAggTimeInProtectState,
       "cienaCesExtAggLastTimeProtected": cienaCesExtAggLastTimeProtected,
       "cienaCesExtAggNumberOfSwitchovers": cienaCesExtAggNumberOfSwitchovers,
       "cienaCesExtAggMultiChassis": cienaCesExtAggMultiChassis,
       "cienaCesExtAggMinimumLinkAggregation": cienaCesExtAggMinimumLinkAggregation,
       "cienaCesExtAggMinimumLinkThreshold": cienaCesExtAggMinimumLinkThreshold,
       "cienaCesExtAggAdminState": cienaCesExtAggAdminState,
       "cienaCesExtAggOperState": cienaCesExtAggOperState,
       "cienaCesLagProtectionTable": cienaCesLagProtectionTable,
       "cienaCesLagProtectionEntry": cienaCesLagProtectionEntry,
       "cienaCesLagProtectionPort": cienaCesLagProtectionPort,
       "cienaCesExtAggMarkerTimeout": cienaCesExtAggMarkerTimeout,
       "cienaCesExtLagMIBConformance": cienaCesExtLagMIBConformance,
       "cienaCesExtLagMIBCompliances": cienaCesExtLagMIBCompliances,
       "cienaCesExtLagMIBGroups": cienaCesExtLagMIBGroups,
       "cienaCesExtLagMIBNotificationPrefix": cienaCesExtLagMIBNotificationPrefix,
       "cienaCesExtLagMIBNotifications": cienaCesExtLagMIBNotifications,
       "cienaCesExtLagMclagStateChange": cienaCesExtLagMclagStateChange}
)
