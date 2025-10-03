# SNMP MIB module (ARUBAWIRED-PORTSECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-PORTSECURITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:21 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arubaWiredPortSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21)
)
if mibBuilder.loadTexts:
    arubaWiredPortSecurityMIB.setRevisions(
        ("2021-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VidList(TextualConvention, OctetString):
    status = "current"
    displayHint = "512x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512



class ArubaWiredPortSecurityMacAddrType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1),
          ("stickyDynamic", 2),
          ("stickyStatic", 3))
    )



# MIB Managed Objects in the order of their OIDs

_ArubaWiredPortSecurityNotifications_ObjectIdentity = ObjectIdentity
arubaWiredPortSecurityNotifications = _ArubaWiredPortSecurityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 0)
)
_ArubaWiredPortSecurityObjects_ObjectIdentity = ObjectIdentity
arubaWiredPortSecurityObjects = _ArubaWiredPortSecurityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1)
)
_ArubaWiredPortSecurityGlobalObjects_ObjectIdentity = ObjectIdentity
arubaWiredPortSecurityGlobalObjects = _ArubaWiredPortSecurityGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 1)
)


class _ArubaWiredPortSecurityGlobalEnable_Type(TruthValue):
    """Custom type arubaWiredPortSecurityGlobalEnable based on TruthValue"""
    defaultValue = 2


_ArubaWiredPortSecurityGlobalEnable_Type.__name__ = "TruthValue"
_ArubaWiredPortSecurityGlobalEnable_Object = MibScalar
arubaWiredPortSecurityGlobalEnable = _ArubaWiredPortSecurityGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 1, 1),
    _ArubaWiredPortSecurityGlobalEnable_Type()
)
arubaWiredPortSecurityGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredPortSecurityGlobalEnable.setStatus("current")
_ArubaWiredPortSecurityPortObjects_ObjectIdentity = ObjectIdentity
arubaWiredPortSecurityPortObjects = _ArubaWiredPortSecurityPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2)
)
_ArubaWiredPortSecurityPortTable_Object = MibTable
arubaWiredPortSecurityPortTable = _ArubaWiredPortSecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 1)
)
if mibBuilder.loadTexts:
    arubaWiredPortSecurityPortTable.setStatus("current")
_ArubaWiredPortSecurityPortEntry_Object = MibTableRow
arubaWiredPortSecurityPortEntry = _ArubaWiredPortSecurityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 1, 1)
)
arubaWiredPortSecurityPortEntry.setIndexNames(
    (0, "ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredifIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredPortSecurityPortEntry.setStatus("current")


class _ArubaWiredifIndex_Type(Unsigned32):
    """Custom type arubaWiredifIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ArubaWiredifIndex_Type.__name__ = "Unsigned32"
_ArubaWiredifIndex_Object = MibTableColumn
arubaWiredifIndex = _ArubaWiredifIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 1, 1, 1),
    _ArubaWiredifIndex_Type()
)
arubaWiredifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredifIndex.setStatus("current")


class _ArubaWiredPortSecurityEnable_Type(TruthValue):
    """Custom type arubaWiredPortSecurityEnable based on TruthValue"""
    defaultValue = 2


_ArubaWiredPortSecurityEnable_Type.__name__ = "TruthValue"
_ArubaWiredPortSecurityEnable_Object = MibTableColumn
arubaWiredPortSecurityEnable = _ArubaWiredPortSecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 1, 1, 2),
    _ArubaWiredPortSecurityEnable_Type()
)
arubaWiredPortSecurityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredPortSecurityEnable.setStatus("current")


class _ArubaWiredClientLimit_Type(Unsigned32):
    """Custom type arubaWiredClientLimit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ArubaWiredClientLimit_Type.__name__ = "Unsigned32"
_ArubaWiredClientLimit_Object = MibTableColumn
arubaWiredClientLimit = _ArubaWiredClientLimit_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 1, 1, 3),
    _ArubaWiredClientLimit_Type()
)
arubaWiredClientLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredClientLimit.setStatus("current")


class _ArubaWiredCurrentSecureMacAddrCount_Type(Unsigned32):
    """Custom type arubaWiredCurrentSecureMacAddrCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ArubaWiredCurrentSecureMacAddrCount_Type.__name__ = "Unsigned32"
_ArubaWiredCurrentSecureMacAddrCount_Object = MibTableColumn
arubaWiredCurrentSecureMacAddrCount = _ArubaWiredCurrentSecureMacAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 1, 1, 4),
    _ArubaWiredCurrentSecureMacAddrCount_Type()
)
arubaWiredCurrentSecureMacAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredCurrentSecureMacAddrCount.setStatus("current")


class _ArubaWiredViolationAction_Type(Integer32):
    """Custom type arubaWiredViolationAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notify", 1),
          ("shutdown", 2))
    )


_ArubaWiredViolationAction_Type.__name__ = "Integer32"
_ArubaWiredViolationAction_Object = MibTableColumn
arubaWiredViolationAction = _ArubaWiredViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 1, 1, 5),
    _ArubaWiredViolationAction_Type()
)
arubaWiredViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredViolationAction.setStatus("current")
_ArubaWiredClientViolationStatus_Type = TruthValue
_ArubaWiredClientViolationStatus_Object = MibTableColumn
arubaWiredClientViolationStatus = _ArubaWiredClientViolationStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 1, 1, 6),
    _ArubaWiredClientViolationStatus_Type()
)
arubaWiredClientViolationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredClientViolationStatus.setStatus("current")


class _ArubaWiredClientViolationReason_Type(Integer32):
    """Custom type arubaWiredClientViolationReason based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clientLimitExceeded", 1),
          ("stickyClientMove", 2))
    )


_ArubaWiredClientViolationReason_Type.__name__ = "Integer32"
_ArubaWiredClientViolationReason_Object = MibTableColumn
arubaWiredClientViolationReason = _ArubaWiredClientViolationReason_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 1, 1, 7),
    _ArubaWiredClientViolationReason_Type()
)
arubaWiredClientViolationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredClientViolationReason.setStatus("current")
_ArubaWiredClientLimitViolationCount_Type = Counter32
_ArubaWiredClientLimitViolationCount_Object = MibTableColumn
arubaWiredClientLimitViolationCount = _ArubaWiredClientLimitViolationCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 1, 1, 8),
    _ArubaWiredClientLimitViolationCount_Type()
)
arubaWiredClientLimitViolationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredClientLimitViolationCount.setStatus("current")
_ArubaWiredStickyClientMoveViolationCount_Type = Counter32
_ArubaWiredStickyClientMoveViolationCount_Object = MibTableColumn
arubaWiredStickyClientMoveViolationCount = _ArubaWiredStickyClientMoveViolationCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 1, 1, 9),
    _ArubaWiredStickyClientMoveViolationCount_Type()
)
arubaWiredStickyClientMoveViolationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredStickyClientMoveViolationCount.setStatus("current")


class _ArubaWiredRecoveryTimer_Type(Unsigned32):
    """Custom type arubaWiredRecoveryTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_ArubaWiredRecoveryTimer_Type.__name__ = "Unsigned32"
_ArubaWiredRecoveryTimer_Object = MibTableColumn
arubaWiredRecoveryTimer = _ArubaWiredRecoveryTimer_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 1, 1, 10),
    _ArubaWiredRecoveryTimer_Type()
)
arubaWiredRecoveryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRecoveryTimer.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredRecoveryTimer.setUnits("seconds")


class _ArubaWiredShutdownRecovery_Type(TruthValue):
    """Custom type arubaWiredShutdownRecovery based on TruthValue"""
    defaultValue = 2


_ArubaWiredShutdownRecovery_Type.__name__ = "TruthValue"
_ArubaWiredShutdownRecovery_Object = MibTableColumn
arubaWiredShutdownRecovery = _ArubaWiredShutdownRecovery_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 1, 1, 11),
    _ArubaWiredShutdownRecovery_Type()
)
arubaWiredShutdownRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredShutdownRecovery.setStatus("current")


class _ArubaWiredStickyEnable_Type(TruthValue):
    """Custom type arubaWiredStickyEnable based on TruthValue"""
    defaultValue = 2


_ArubaWiredStickyEnable_Type.__name__ = "TruthValue"
_ArubaWiredStickyEnable_Object = MibTableColumn
arubaWiredStickyEnable = _ArubaWiredStickyEnable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 1, 1, 12),
    _ArubaWiredStickyEnable_Type()
)
arubaWiredStickyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredStickyEnable.setStatus("current")
_ArubaWiredPortSecurityClientTable_Object = MibTable
arubaWiredPortSecurityClientTable = _ArubaWiredPortSecurityClientTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 2)
)
if mibBuilder.loadTexts:
    arubaWiredPortSecurityClientTable.setStatus("current")
_ArubaWiredPortSecurityClientEntry_Object = MibTableRow
arubaWiredPortSecurityClientEntry = _ArubaWiredPortSecurityClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 2, 1)
)
arubaWiredPortSecurityClientEntry.setIndexNames(
    (0, "ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredClientPortName"),
    (0, "ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredClientMac"),
)
if mibBuilder.loadTexts:
    arubaWiredPortSecurityClientEntry.setStatus("current")


class _ArubaWiredClientPortName_Type(DisplayString):
    """Custom type arubaWiredClientPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ArubaWiredClientPortName_Type.__name__ = "DisplayString"
_ArubaWiredClientPortName_Object = MibTableColumn
arubaWiredClientPortName = _ArubaWiredClientPortName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 2, 1, 1),
    _ArubaWiredClientPortName_Type()
)
arubaWiredClientPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredClientPortName.setStatus("current")
_ArubaWiredClientMac_Type = MacAddress
_ArubaWiredClientMac_Object = MibTableColumn
arubaWiredClientMac = _ArubaWiredClientMac_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 2, 1, 2),
    _ArubaWiredClientMac_Type()
)
arubaWiredClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredClientMac.setStatus("current")


class _ArubaWiredClientAuthorizationState_Type(DisplayString):
    """Custom type arubaWiredClientAuthorizationState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArubaWiredClientAuthorizationState_Type.__name__ = "DisplayString"
_ArubaWiredClientAuthorizationState_Object = MibTableColumn
arubaWiredClientAuthorizationState = _ArubaWiredClientAuthorizationState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 2, 1, 3),
    _ArubaWiredClientAuthorizationState_Type()
)
arubaWiredClientAuthorizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredClientAuthorizationState.setStatus("current")
_ArubaWiredClientMacType_Type = ArubaWiredPortSecurityMacAddrType
_ArubaWiredClientMacType_Object = MibTableColumn
arubaWiredClientMacType = _ArubaWiredClientMacType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 2, 1, 4),
    _ArubaWiredClientMacType_Type()
)
arubaWiredClientMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredClientMacType.setStatus("current")
_ArubaWiredPortSecurityMacCfgTable_Object = MibTable
arubaWiredPortSecurityMacCfgTable = _ArubaWiredPortSecurityMacCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 3)
)
if mibBuilder.loadTexts:
    arubaWiredPortSecurityMacCfgTable.setStatus("current")
_ArubaWiredPortSecurityMacCfgEntry_Object = MibTableRow
arubaWiredPortSecurityMacCfgEntry = _ArubaWiredPortSecurityMacCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 3, 1)
)
arubaWiredPortSecurityMacCfgEntry.setIndexNames(
    (0, "ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredPortifIndex"),
    (0, "ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredStaticMacType"),
    (0, "ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredStaticClientMac"),
)
if mibBuilder.loadTexts:
    arubaWiredPortSecurityMacCfgEntry.setStatus("current")


class _ArubaWiredPortifIndex_Type(Unsigned32):
    """Custom type arubaWiredPortifIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ArubaWiredPortifIndex_Type.__name__ = "Unsigned32"
_ArubaWiredPortifIndex_Object = MibTableColumn
arubaWiredPortifIndex = _ArubaWiredPortifIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 3, 1, 1),
    _ArubaWiredPortifIndex_Type()
)
arubaWiredPortifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredPortifIndex.setStatus("current")
_ArubaWiredStaticMacType_Type = TruthValue
_ArubaWiredStaticMacType_Object = MibTableColumn
arubaWiredStaticMacType = _ArubaWiredStaticMacType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 3, 1, 2),
    _ArubaWiredStaticMacType_Type()
)
arubaWiredStaticMacType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredStaticMacType.setStatus("current")
_ArubaWiredStaticClientMac_Type = MacAddress
_ArubaWiredStaticClientMac_Object = MibTableColumn
arubaWiredStaticClientMac = _ArubaWiredStaticClientMac_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 3, 1, 3),
    _ArubaWiredStaticClientMac_Type()
)
arubaWiredStaticClientMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredStaticClientMac.setStatus("current")
_ArubaWiredClientMacVidList_Type = VidList
_ArubaWiredClientMacVidList_Object = MibTableColumn
arubaWiredClientMacVidList = _ArubaWiredClientMacVidList_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 3, 1, 4),
    _ArubaWiredClientMacVidList_Type()
)
arubaWiredClientMacVidList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredClientMacVidList.setStatus("current")
_ArubaWiredMacAddrRowStatus_Type = RowStatus
_ArubaWiredMacAddrRowStatus_Object = MibTableColumn
arubaWiredMacAddrRowStatus = _ArubaWiredMacAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 1, 2, 3, 1, 5),
    _ArubaWiredMacAddrRowStatus_Type()
)
arubaWiredMacAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredMacAddrRowStatus.setStatus("current")
_ArubaWiredPortSecurityConformance_ObjectIdentity = ObjectIdentity
arubaWiredPortSecurityConformance = _ArubaWiredPortSecurityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 2)
)
_ArubaWiredPortSecurityGroups_ObjectIdentity = ObjectIdentity
arubaWiredPortSecurityGroups = _ArubaWiredPortSecurityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 2, 1)
)
_ArubaWiredPortSecurityCompliances_ObjectIdentity = ObjectIdentity
arubaWiredPortSecurityCompliances = _ArubaWiredPortSecurityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 2, 2)
)

# Managed Objects groups

arubaWiredPortSecurityPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 2, 1, 1)
)
arubaWiredPortSecurityPortGroup.setObjects(
      *(("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredifIndex"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredPortSecurityEnable"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredClientLimit"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredCurrentSecureMacAddrCount"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredViolationAction"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredClientViolationStatus"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredClientViolationReason"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredClientLimitViolationCount"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredStickyClientMoveViolationCount"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredRecoveryTimer"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredShutdownRecovery"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredStickyEnable"))
)
if mibBuilder.loadTexts:
    arubaWiredPortSecurityPortGroup.setStatus("current")

arubaWiredPortSecurityClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 2, 1, 2)
)
arubaWiredPortSecurityClientGroup.setObjects(
      *(("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredClientMac"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredClientAuthorizationState"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredClientMacType"))
)
if mibBuilder.loadTexts:
    arubaWiredPortSecurityClientGroup.setStatus("current")

arubaWiredPortSecurityMacCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 2, 1, 3)
)
arubaWiredPortSecurityMacCfgGroup.setObjects(
      *(("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredClientMacVidList"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredMacAddrRowStatus"))
)
if mibBuilder.loadTexts:
    arubaWiredPortSecurityMacCfgGroup.setStatus("current")

arubaWiredPortSecurityGlobalCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 2, 1, 4)
)
arubaWiredPortSecurityGlobalCfgGroup.setObjects(
    ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredPortSecurityGlobalEnable")
)
if mibBuilder.loadTexts:
    arubaWiredPortSecurityGlobalCfgGroup.setStatus("current")


# Notification objects

arubaWiredPortSecurityViolationStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 0, 1)
)
arubaWiredPortSecurityViolationStatusChange.setObjects(
      *(("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredifIndex"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredClientMac"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredClientViolationStatus"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredClientViolationReason"))
)
if mibBuilder.loadTexts:
    arubaWiredPortSecurityViolationStatusChange.setStatus(
        "current"
    )


# Notifications groups

arubaWiredPortSecurityNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 2, 1, 5)
)
arubaWiredPortSecurityNotificationsGroup.setObjects(
    ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredPortSecurityViolationStatusChange")
)
if mibBuilder.loadTexts:
    arubaWiredPortSecurityNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

arubaWiredPortSecurityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21, 2, 2, 1)
)
arubaWiredPortSecurityCompliance.setObjects(
      *(("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredPortSecurityPortGroup"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredPortSecurityClientGroup"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredPortSecurityMacCfgGroup"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredPortSecurityGlobalCfgGroup"),
        ("ARUBAWIRED-PORTSECURITY-MIB", "arubaWiredPortSecurityNotificationsGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredPortSecurityCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-PORTSECURITY-MIB",
    **{"VidList": VidList,
       "ArubaWiredPortSecurityMacAddrType": ArubaWiredPortSecurityMacAddrType,
       "arubaWiredPortSecurityMIB": arubaWiredPortSecurityMIB,
       "arubaWiredPortSecurityNotifications": arubaWiredPortSecurityNotifications,
       "arubaWiredPortSecurityViolationStatusChange": arubaWiredPortSecurityViolationStatusChange,
       "arubaWiredPortSecurityObjects": arubaWiredPortSecurityObjects,
       "arubaWiredPortSecurityGlobalObjects": arubaWiredPortSecurityGlobalObjects,
       "arubaWiredPortSecurityGlobalEnable": arubaWiredPortSecurityGlobalEnable,
       "arubaWiredPortSecurityPortObjects": arubaWiredPortSecurityPortObjects,
       "arubaWiredPortSecurityPortTable": arubaWiredPortSecurityPortTable,
       "arubaWiredPortSecurityPortEntry": arubaWiredPortSecurityPortEntry,
       "arubaWiredifIndex": arubaWiredifIndex,
       "arubaWiredPortSecurityEnable": arubaWiredPortSecurityEnable,
       "arubaWiredClientLimit": arubaWiredClientLimit,
       "arubaWiredCurrentSecureMacAddrCount": arubaWiredCurrentSecureMacAddrCount,
       "arubaWiredViolationAction": arubaWiredViolationAction,
       "arubaWiredClientViolationStatus": arubaWiredClientViolationStatus,
       "arubaWiredClientViolationReason": arubaWiredClientViolationReason,
       "arubaWiredClientLimitViolationCount": arubaWiredClientLimitViolationCount,
       "arubaWiredStickyClientMoveViolationCount": arubaWiredStickyClientMoveViolationCount,
       "arubaWiredRecoveryTimer": arubaWiredRecoveryTimer,
       "arubaWiredShutdownRecovery": arubaWiredShutdownRecovery,
       "arubaWiredStickyEnable": arubaWiredStickyEnable,
       "arubaWiredPortSecurityClientTable": arubaWiredPortSecurityClientTable,
       "arubaWiredPortSecurityClientEntry": arubaWiredPortSecurityClientEntry,
       "arubaWiredClientPortName": arubaWiredClientPortName,
       "arubaWiredClientMac": arubaWiredClientMac,
       "arubaWiredClientAuthorizationState": arubaWiredClientAuthorizationState,
       "arubaWiredClientMacType": arubaWiredClientMacType,
       "arubaWiredPortSecurityMacCfgTable": arubaWiredPortSecurityMacCfgTable,
       "arubaWiredPortSecurityMacCfgEntry": arubaWiredPortSecurityMacCfgEntry,
       "arubaWiredPortifIndex": arubaWiredPortifIndex,
       "arubaWiredStaticMacType": arubaWiredStaticMacType,
       "arubaWiredStaticClientMac": arubaWiredStaticClientMac,
       "arubaWiredClientMacVidList": arubaWiredClientMacVidList,
       "arubaWiredMacAddrRowStatus": arubaWiredMacAddrRowStatus,
       "arubaWiredPortSecurityConformance": arubaWiredPortSecurityConformance,
       "arubaWiredPortSecurityGroups": arubaWiredPortSecurityGroups,
       "arubaWiredPortSecurityPortGroup": arubaWiredPortSecurityPortGroup,
       "arubaWiredPortSecurityClientGroup": arubaWiredPortSecurityClientGroup,
       "arubaWiredPortSecurityMacCfgGroup": arubaWiredPortSecurityMacCfgGroup,
       "arubaWiredPortSecurityGlobalCfgGroup": arubaWiredPortSecurityGlobalCfgGroup,
       "arubaWiredPortSecurityNotificationsGroup": arubaWiredPortSecurityNotificationsGroup,
       "arubaWiredPortSecurityCompliances": arubaWiredPortSecurityCompliances,
       "arubaWiredPortSecurityCompliance": arubaWiredPortSecurityCompliance}
)
