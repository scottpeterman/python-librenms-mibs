# SNMP MIB module (EXTREME-EAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\EXTREME-EAPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:22 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

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

extremeEaps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EapsDomainMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("master", 1),
          ("transit", 2))
    )



class EapsMbrVlanType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unassigned", 0),
          ("control", 1),
          ("protected", 2))
    )



class EapsRingPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class EapsPortType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )



class EapsDomainState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("complete", 1),
          ("failed", 2),
          ("linksup", 3),
          ("linkdown", 4),
          ("preforwarding", 5),
          ("init", 6),
          ("precomplete", 7),
          ("preinit", 8))
    )



class EapsDomainPortStatus(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("up", 1),
          ("down", 2),
          ("blocked", 3))
    )



class EapsFailTimerExpiryAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sendAlert", 0),
          ("openSecondaryPort", 1))
    )



class EapsSharedPortState(TextualConvention, Integer32):
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
        *(("idle", 0),
          ("ready", 1),
          ("blocking", 2),
          ("preforwarding", 3))
    )



class EapsSharedPortMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unconfigured", 0),
          ("controller", 1),
          ("partner", 2))
    )



class EapsSharedPortSegmentTimerExpiryAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sendAlert", 0),
          ("segmentDown", 1))
    )



class EapsSharedPortNeighborStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("neighborDown", 0),
          ("neighborUp", 1),
          ("neighborError", 2))
    )



class EapsSharedPortRootBlockerStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("active", 1),
          ("inactive", 2))
    )



class EapsSharedPortSegmentStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("segUp", 1),
          ("segDown", 2),
          ("segBlockingUp", 3),
          ("segBlockingDown", 4))
    )



class EapsSharedPortVlanPortStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("activeOpen", 1),
          ("blocked", 2),
          ("open", 3),
          ("down", 4))
    )



class EapsDomainPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("high", 1))
    )



# MIB Managed Objects in the order of their OIDs

_ExtremeEapsTable_Object = MibTable
extremeEapsTable = _ExtremeEapsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1)
)
if mibBuilder.loadTexts:
    extremeEapsTable.setStatus("current")
_ExtremeEapsEntry_Object = MibTableRow
extremeEapsEntry = _ExtremeEapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1)
)
extremeEapsEntry.setIndexNames(
    (0, "EXTREME-EAPS-MIB", "extremeEapsName"),
)
if mibBuilder.loadTexts:
    extremeEapsEntry.setStatus("current")


class _ExtremeEapsName_Type(DisplayString):
    """Custom type extremeEapsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeEapsName_Type.__name__ = "DisplayString"
_ExtremeEapsName_Object = MibTableColumn
extremeEapsName = _ExtremeEapsName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 1),
    _ExtremeEapsName_Type()
)
extremeEapsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsName.setStatus("current")
_ExtremeEapsMode_Type = EapsDomainMode
_ExtremeEapsMode_Object = MibTableColumn
extremeEapsMode = _ExtremeEapsMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 2),
    _ExtremeEapsMode_Type()
)
extremeEapsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEapsMode.setStatus("current")
_ExtremeEapsState_Type = EapsDomainState
_ExtremeEapsState_Object = MibTableColumn
extremeEapsState = _ExtremeEapsState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 3),
    _ExtremeEapsState_Type()
)
extremeEapsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsState.setStatus("current")
_ExtremeEapsFailedFlag_Type = TruthValue
_ExtremeEapsFailedFlag_Object = MibTableColumn
extremeEapsFailedFlag = _ExtremeEapsFailedFlag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 4),
    _ExtremeEapsFailedFlag_Type()
)
extremeEapsFailedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsFailedFlag.setStatus("current")
_ExtremeEapsEnabled_Type = TruthValue
_ExtremeEapsEnabled_Object = MibTableColumn
extremeEapsEnabled = _ExtremeEapsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 5),
    _ExtremeEapsEnabled_Type()
)
extremeEapsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEapsEnabled.setStatus("current")
_ExtremeEapsPrimaryPort_Type = EapsRingPort
_ExtremeEapsPrimaryPort_Object = MibTableColumn
extremeEapsPrimaryPort = _ExtremeEapsPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 6),
    _ExtremeEapsPrimaryPort_Type()
)
extremeEapsPrimaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEapsPrimaryPort.setStatus("current")
_ExtremeEapsSecondaryPort_Type = EapsRingPort
_ExtremeEapsSecondaryPort_Object = MibTableColumn
extremeEapsSecondaryPort = _ExtremeEapsSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 7),
    _ExtremeEapsSecondaryPort_Type()
)
extremeEapsSecondaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEapsSecondaryPort.setStatus("current")


class _ExtremeEapsHelloTimer_Type(Integer32):
    """Custom type extremeEapsHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ExtremeEapsHelloTimer_Type.__name__ = "Integer32"
_ExtremeEapsHelloTimer_Object = MibTableColumn
extremeEapsHelloTimer = _ExtremeEapsHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 8),
    _ExtremeEapsHelloTimer_Type()
)
extremeEapsHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEapsHelloTimer.setStatus("current")


class _ExtremeEapsFailedTimer_Type(Integer32):
    """Custom type extremeEapsFailedTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 300),
    )


_ExtremeEapsFailedTimer_Type.__name__ = "Integer32"
_ExtremeEapsFailedTimer_Object = MibTableColumn
extremeEapsFailedTimer = _ExtremeEapsFailedTimer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 9),
    _ExtremeEapsFailedTimer_Type()
)
extremeEapsFailedTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEapsFailedTimer.setStatus("current")
_ExtremeEapsFailedTimerExpiryAction_Type = EapsFailTimerExpiryAction
_ExtremeEapsFailedTimerExpiryAction_Object = MibTableColumn
extremeEapsFailedTimerExpiryAction = _ExtremeEapsFailedTimerExpiryAction_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 10),
    _ExtremeEapsFailedTimerExpiryAction_Type()
)
extremeEapsFailedTimerExpiryAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEapsFailedTimerExpiryAction.setStatus("current")
_ExtremeEapsUnconfigRingPort_Type = EapsPortType
_ExtremeEapsUnconfigRingPort_Object = MibTableColumn
extremeEapsUnconfigRingPort = _ExtremeEapsUnconfigRingPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 11),
    _ExtremeEapsUnconfigRingPort_Type()
)
extremeEapsUnconfigRingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEapsUnconfigRingPort.setStatus("current")
_ExtremeEapsPrimaryStatus_Type = EapsDomainPortStatus
_ExtremeEapsPrimaryStatus_Object = MibTableColumn
extremeEapsPrimaryStatus = _ExtremeEapsPrimaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 12),
    _ExtremeEapsPrimaryStatus_Type()
)
extremeEapsPrimaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsPrimaryStatus.setStatus("current")
_ExtremeEapsSecondaryStatus_Type = EapsDomainPortStatus
_ExtremeEapsSecondaryStatus_Object = MibTableColumn
extremeEapsSecondaryStatus = _ExtremeEapsSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 13),
    _ExtremeEapsSecondaryStatus_Type()
)
extremeEapsSecondaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSecondaryStatus.setStatus("current")


class _ExtremeEapsProtectedVlansCount_Type(Integer32):
    """Custom type extremeEapsProtectedVlansCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEapsProtectedVlansCount_Type.__name__ = "Integer32"
_ExtremeEapsProtectedVlansCount_Object = MibTableColumn
extremeEapsProtectedVlansCount = _ExtremeEapsProtectedVlansCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 14),
    _ExtremeEapsProtectedVlansCount_Type()
)
extremeEapsProtectedVlansCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsProtectedVlansCount.setStatus("current")
_ExtremeEapsRowStatus_Type = RowStatus
_ExtremeEapsRowStatus_Object = MibTableColumn
extremeEapsRowStatus = _ExtremeEapsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 15),
    _ExtremeEapsRowStatus_Type()
)
extremeEapsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEapsRowStatus.setStatus("current")


class _ExtremeEapsHelloTimerMs_Type(Integer32):
    """Custom type extremeEapsHelloTimerMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 900),
    )


_ExtremeEapsHelloTimerMs_Type.__name__ = "Integer32"
_ExtremeEapsHelloTimerMs_Object = MibTableColumn
extremeEapsHelloTimerMs = _ExtremeEapsHelloTimerMs_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 16),
    _ExtremeEapsHelloTimerMs_Type()
)
extremeEapsHelloTimerMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsHelloTimerMs.setStatus("current")
_ExtremeEapsPriority_Type = EapsDomainPriority
_ExtremeEapsPriority_Object = MibTableColumn
extremeEapsPriority = _ExtremeEapsPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 17),
    _ExtremeEapsPriority_Type()
)
extremeEapsPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEapsPriority.setStatus("current")
_ExtremeEapsPrevState_Type = EapsDomainState
_ExtremeEapsPrevState_Object = MibScalar
extremeEapsPrevState = _ExtremeEapsPrevState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 2),
    _ExtremeEapsPrevState_Type()
)
extremeEapsPrevState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeEapsPrevState.setStatus("current")
_ExtremeEapsGlobalInfo_ObjectIdentity = ObjectIdentity
extremeEapsGlobalInfo = _ExtremeEapsGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 3)
)
_ExtremeEapsGlobalEnabled_Type = TruthValue
_ExtremeEapsGlobalEnabled_Object = MibScalar
extremeEapsGlobalEnabled = _ExtremeEapsGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 1),
    _ExtremeEapsGlobalEnabled_Type()
)
extremeEapsGlobalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEapsGlobalEnabled.setStatus("current")
_ExtremeEapsGlobalFastConvergence_Type = TruthValue
_ExtremeEapsGlobalFastConvergence_Object = MibScalar
extremeEapsGlobalFastConvergence = _ExtremeEapsGlobalFastConvergence_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 2),
    _ExtremeEapsGlobalFastConvergence_Type()
)
extremeEapsGlobalFastConvergence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEapsGlobalFastConvergence.setStatus("current")
_ExtremeEapsLastConfigurationChange_Type = Unsigned32
_ExtremeEapsLastConfigurationChange_Object = MibScalar
extremeEapsLastConfigurationChange = _ExtremeEapsLastConfigurationChange_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 3),
    _ExtremeEapsLastConfigurationChange_Type()
)
extremeEapsLastConfigurationChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsLastConfigurationChange.setStatus("current")
_ExtremeEapsLastStatusChange_Type = Unsigned32
_ExtremeEapsLastStatusChange_Object = MibScalar
extremeEapsLastStatusChange = _ExtremeEapsLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 4),
    _ExtremeEapsLastStatusChange_Type()
)
extremeEapsLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsLastStatusChange.setStatus("current")
_ExtremeEapsStatusTrapCount_Type = Counter32
_ExtremeEapsStatusTrapCount_Object = MibScalar
extremeEapsStatusTrapCount = _ExtremeEapsStatusTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 5),
    _ExtremeEapsStatusTrapCount_Type()
)
extremeEapsStatusTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsStatusTrapCount.setStatus("current")
_ExtremeEapsGlobalMulticastAddRingPorts_Type = TruthValue
_ExtremeEapsGlobalMulticastAddRingPorts_Object = MibScalar
extremeEapsGlobalMulticastAddRingPorts = _ExtremeEapsGlobalMulticastAddRingPorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 6),
    _ExtremeEapsGlobalMulticastAddRingPorts_Type()
)
extremeEapsGlobalMulticastAddRingPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEapsGlobalMulticastAddRingPorts.setStatus("current")
_ExtremeEapsGlobalMulticastSendIGMPQuery_Type = TruthValue
_ExtremeEapsGlobalMulticastSendIGMPQuery_Object = MibScalar
extremeEapsGlobalMulticastSendIGMPQuery = _ExtremeEapsGlobalMulticastSendIGMPQuery_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 7),
    _ExtremeEapsGlobalMulticastSendIGMPQuery_Type()
)
extremeEapsGlobalMulticastSendIGMPQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEapsGlobalMulticastSendIGMPQuery.setStatus("current")
_ExtremeEapsGlobalMulticastTempFlooding_Type = TruthValue
_ExtremeEapsGlobalMulticastTempFlooding_Object = MibScalar
extremeEapsGlobalMulticastTempFlooding = _ExtremeEapsGlobalMulticastTempFlooding_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 8),
    _ExtremeEapsGlobalMulticastTempFlooding_Type()
)
extremeEapsGlobalMulticastTempFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEapsGlobalMulticastTempFlooding.setStatus("current")
_ExtremeEapsGlobalMulticastTempFloodingDuration_Type = Unsigned32
_ExtremeEapsGlobalMulticastTempFloodingDuration_Object = MibScalar
extremeEapsGlobalMulticastTempFloodingDuration = _ExtremeEapsGlobalMulticastTempFloodingDuration_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 3, 9),
    _ExtremeEapsGlobalMulticastTempFloodingDuration_Type()
)
extremeEapsGlobalMulticastTempFloodingDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEapsGlobalMulticastTempFloodingDuration.setStatus("current")
_ExtremeEapsMbrVlanTable_Object = MibTable
extremeEapsMbrVlanTable = _ExtremeEapsMbrVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 4)
)
if mibBuilder.loadTexts:
    extremeEapsMbrVlanTable.setStatus("current")
_ExtremeEapsMbrVlanEntry_Object = MibTableRow
extremeEapsMbrVlanEntry = _ExtremeEapsMbrVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 4, 1)
)
extremeEapsMbrVlanEntry.setIndexNames(
    (0, "EXTREME-EAPS-MIB", "extremeEapsName"),
    (0, "EXTREME-EAPS-MIB", "extremeEapsMbrVlanName"),
    (0, "EXTREME-EAPS-MIB", "extremeEapsMbrVlanType"),
)
if mibBuilder.loadTexts:
    extremeEapsMbrVlanEntry.setStatus("current")


class _ExtremeEapsMbrVlanName_Type(DisplayString):
    """Custom type extremeEapsMbrVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeEapsMbrVlanName_Type.__name__ = "DisplayString"
_ExtremeEapsMbrVlanName_Object = MibTableColumn
extremeEapsMbrVlanName = _ExtremeEapsMbrVlanName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 4, 1, 1),
    _ExtremeEapsMbrVlanName_Type()
)
extremeEapsMbrVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsMbrVlanName.setStatus("current")
_ExtremeEapsMbrVlanType_Type = EapsMbrVlanType
_ExtremeEapsMbrVlanType_Object = MibTableColumn
extremeEapsMbrVlanType = _ExtremeEapsMbrVlanType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 4, 1, 2),
    _ExtremeEapsMbrVlanType_Type()
)
extremeEapsMbrVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsMbrVlanType.setStatus("current")


class _ExtremeEapsMbrVlanTag_Type(Integer32):
    """Custom type extremeEapsMbrVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_ExtremeEapsMbrVlanTag_Type.__name__ = "Integer32"
_ExtremeEapsMbrVlanTag_Object = MibTableColumn
extremeEapsMbrVlanTag = _ExtremeEapsMbrVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 4, 1, 3),
    _ExtremeEapsMbrVlanTag_Type()
)
extremeEapsMbrVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsMbrVlanTag.setStatus("current")
_ExtremeEapsMbrVlanRowStatus_Type = RowStatus
_ExtremeEapsMbrVlanRowStatus_Object = MibTableColumn
extremeEapsMbrVlanRowStatus = _ExtremeEapsMbrVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 4, 1, 4),
    _ExtremeEapsMbrVlanRowStatus_Type()
)
extremeEapsMbrVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEapsMbrVlanRowStatus.setStatus("current")
_ExtremeEapsSharedPortTable_Object = MibTable
extremeEapsSharedPortTable = _ExtremeEapsSharedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5)
)
if mibBuilder.loadTexts:
    extremeEapsSharedPortTable.setStatus("current")
_ExtremeEapsSharedPortEntry_Object = MibTableRow
extremeEapsSharedPortEntry = _ExtremeEapsSharedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1)
)
extremeEapsSharedPortEntry.setIndexNames(
    (0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortIfIndex"),
)
if mibBuilder.loadTexts:
    extremeEapsSharedPortEntry.setStatus("current")
_ExtremeEapsSharedPortIfIndex_Type = EapsRingPort
_ExtremeEapsSharedPortIfIndex_Object = MibTableColumn
extremeEapsSharedPortIfIndex = _ExtremeEapsSharedPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 1),
    _ExtremeEapsSharedPortIfIndex_Type()
)
extremeEapsSharedPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortIfIndex.setStatus("current")
_ExtremeEapsSharedPortMode_Type = EapsSharedPortMode
_ExtremeEapsSharedPortMode_Object = MibTableColumn
extremeEapsSharedPortMode = _ExtremeEapsSharedPortMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 2),
    _ExtremeEapsSharedPortMode_Type()
)
extremeEapsSharedPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEapsSharedPortMode.setStatus("current")


class _ExtremeEapsSharedPortLinkId_Type(Integer32):
    """Custom type extremeEapsSharedPortLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_ExtremeEapsSharedPortLinkId_Type.__name__ = "Integer32"
_ExtremeEapsSharedPortLinkId_Object = MibTableColumn
extremeEapsSharedPortLinkId = _ExtremeEapsSharedPortLinkId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 3),
    _ExtremeEapsSharedPortLinkId_Type()
)
extremeEapsSharedPortLinkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEapsSharedPortLinkId.setStatus("current")
_ExtremeEapsSharedPortSegmentTimerExpiryAction_Type = EapsSharedPortSegmentTimerExpiryAction
_ExtremeEapsSharedPortSegmentTimerExpiryAction_Object = MibTableColumn
extremeEapsSharedPortSegmentTimerExpiryAction = _ExtremeEapsSharedPortSegmentTimerExpiryAction_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 4),
    _ExtremeEapsSharedPortSegmentTimerExpiryAction_Type()
)
extremeEapsSharedPortSegmentTimerExpiryAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEapsSharedPortSegmentTimerExpiryAction.setStatus("current")
_ExtremeEapsSharedPortState_Type = EapsSharedPortState
_ExtremeEapsSharedPortState_Object = MibTableColumn
extremeEapsSharedPortState = _ExtremeEapsSharedPortState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 5),
    _ExtremeEapsSharedPortState_Type()
)
extremeEapsSharedPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortState.setStatus("current")
_ExtremeEapsSharedPortNbrStatus_Type = EapsSharedPortNeighborStatus
_ExtremeEapsSharedPortNbrStatus_Object = MibTableColumn
extremeEapsSharedPortNbrStatus = _ExtremeEapsSharedPortNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 6),
    _ExtremeEapsSharedPortNbrStatus_Type()
)
extremeEapsSharedPortNbrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortNbrStatus.setStatus("current")


class _ExtremeEapsSharedPortDomainsCount_Type(Integer32):
    """Custom type extremeEapsSharedPortDomainsCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEapsSharedPortDomainsCount_Type.__name__ = "Integer32"
_ExtremeEapsSharedPortDomainsCount_Object = MibTableColumn
extremeEapsSharedPortDomainsCount = _ExtremeEapsSharedPortDomainsCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 7),
    _ExtremeEapsSharedPortDomainsCount_Type()
)
extremeEapsSharedPortDomainsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortDomainsCount.setStatus("current")


class _ExtremeEapsSharedPortProtectedVlansCount_Type(Integer32):
    """Custom type extremeEapsSharedPortProtectedVlansCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEapsSharedPortProtectedVlansCount_Type.__name__ = "Integer32"
_ExtremeEapsSharedPortProtectedVlansCount_Object = MibTableColumn
extremeEapsSharedPortProtectedVlansCount = _ExtremeEapsSharedPortProtectedVlansCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 8),
    _ExtremeEapsSharedPortProtectedVlansCount_Type()
)
extremeEapsSharedPortProtectedVlansCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortProtectedVlansCount.setStatus("current")
_ExtremeEapsSharedPortRootBlockerStatus_Type = EapsSharedPortRootBlockerStatus
_ExtremeEapsSharedPortRootBlockerStatus_Object = MibTableColumn
extremeEapsSharedPortRootBlockerStatus = _ExtremeEapsSharedPortRootBlockerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 9),
    _ExtremeEapsSharedPortRootBlockerStatus_Type()
)
extremeEapsSharedPortRootBlockerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortRootBlockerStatus.setStatus("current")


class _ExtremeEapsSharedPortRootBlockerId_Type(Integer32):
    """Custom type extremeEapsSharedPortRootBlockerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEapsSharedPortRootBlockerId_Type.__name__ = "Integer32"
_ExtremeEapsSharedPortRootBlockerId_Object = MibTableColumn
extremeEapsSharedPortRootBlockerId = _ExtremeEapsSharedPortRootBlockerId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 10),
    _ExtremeEapsSharedPortRootBlockerId_Type()
)
extremeEapsSharedPortRootBlockerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortRootBlockerId.setStatus("current")
_ExtremeEapsSharedPortRowStatus_Type = RowStatus
_ExtremeEapsSharedPortRowStatus_Object = MibTableColumn
extremeEapsSharedPortRowStatus = _ExtremeEapsSharedPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 11),
    _ExtremeEapsSharedPortRowStatus_Type()
)
extremeEapsSharedPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEapsSharedPortRowStatus.setStatus("current")


class _ExtremeEapsSharedPortSegmentHealthInterval_Type(Integer32):
    """Custom type extremeEapsSharedPortSegmentHealthInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ExtremeEapsSharedPortSegmentHealthInterval_Type.__name__ = "Integer32"
_ExtremeEapsSharedPortSegmentHealthInterval_Object = MibTableColumn
extremeEapsSharedPortSegmentHealthInterval = _ExtremeEapsSharedPortSegmentHealthInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 12),
    _ExtremeEapsSharedPortSegmentHealthInterval_Type()
)
extremeEapsSharedPortSegmentHealthInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortSegmentHealthInterval.setStatus("current")


class _ExtremeEapsSharedPortSegmentTimeout_Type(Integer32):
    """Custom type extremeEapsSharedPortSegmentTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_ExtremeEapsSharedPortSegmentTimeout_Type.__name__ = "Integer32"
_ExtremeEapsSharedPortSegmentTimeout_Object = MibTableColumn
extremeEapsSharedPortSegmentTimeout = _ExtremeEapsSharedPortSegmentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 13),
    _ExtremeEapsSharedPortSegmentTimeout_Type()
)
extremeEapsSharedPortSegmentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortSegmentTimeout.setStatus("current")
_ExtremeEapsSharedPortCommonPathFailedFlag_Type = TruthValue
_ExtremeEapsSharedPortCommonPathFailedFlag_Object = MibTableColumn
extremeEapsSharedPortCommonPathFailedFlag = _ExtremeEapsSharedPortCommonPathFailedFlag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 14),
    _ExtremeEapsSharedPortCommonPathFailedFlag_Type()
)
extremeEapsSharedPortCommonPathFailedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortCommonPathFailedFlag.setStatus("current")


class _ExtremeEapsSharedPortCommonPathHealthInterval_Type(Integer32):
    """Custom type extremeEapsSharedPortCommonPathHealthInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ExtremeEapsSharedPortCommonPathHealthInterval_Type.__name__ = "Integer32"
_ExtremeEapsSharedPortCommonPathHealthInterval_Object = MibTableColumn
extremeEapsSharedPortCommonPathHealthInterval = _ExtremeEapsSharedPortCommonPathHealthInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 15),
    _ExtremeEapsSharedPortCommonPathHealthInterval_Type()
)
extremeEapsSharedPortCommonPathHealthInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortCommonPathHealthInterval.setStatus("current")


class _ExtremeEapsSharedPortCommonPathTimeout_Type(Integer32):
    """Custom type extremeEapsSharedPortCommonPathTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_ExtremeEapsSharedPortCommonPathTimeout_Type.__name__ = "Integer32"
_ExtremeEapsSharedPortCommonPathTimeout_Object = MibTableColumn
extremeEapsSharedPortCommonPathTimeout = _ExtremeEapsSharedPortCommonPathTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 5, 1, 16),
    _ExtremeEapsSharedPortCommonPathTimeout_Type()
)
extremeEapsSharedPortCommonPathTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortCommonPathTimeout.setStatus("current")
_ExtremeEapsSharedPortSegmentTable_Object = MibTable
extremeEapsSharedPortSegmentTable = _ExtremeEapsSharedPortSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 6)
)
if mibBuilder.loadTexts:
    extremeEapsSharedPortSegmentTable.setStatus("current")
_ExtremeEapsSharedPortSegmentEntry_Object = MibTableRow
extremeEapsSharedPortSegmentEntry = _ExtremeEapsSharedPortSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 6, 1)
)
extremeEapsSharedPortSegmentEntry.setIndexNames(
    (0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortIfIndex"),
    (0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortSegmentPort"),
    (0, "EXTREME-EAPS-MIB", "extremeEapsName"),
)
if mibBuilder.loadTexts:
    extremeEapsSharedPortSegmentEntry.setStatus("current")
_ExtremeEapsSharedPortSegmentPort_Type = EapsRingPort
_ExtremeEapsSharedPortSegmentPort_Object = MibTableColumn
extremeEapsSharedPortSegmentPort = _ExtremeEapsSharedPortSegmentPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 6, 1, 1),
    _ExtremeEapsSharedPortSegmentPort_Type()
)
extremeEapsSharedPortSegmentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortSegmentPort.setStatus("current")
_ExtremeEapsSharedPortSegmentStatus_Type = EapsSharedPortSegmentStatus
_ExtremeEapsSharedPortSegmentStatus_Object = MibTableColumn
extremeEapsSharedPortSegmentStatus = _ExtremeEapsSharedPortSegmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 6, 1, 2),
    _ExtremeEapsSharedPortSegmentStatus_Type()
)
extremeEapsSharedPortSegmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortSegmentStatus.setStatus("current")
_ExtremeEapsSharedPortSegmentFailedFlag_Type = TruthValue
_ExtremeEapsSharedPortSegmentFailedFlag_Object = MibTableColumn
extremeEapsSharedPortSegmentFailedFlag = _ExtremeEapsSharedPortSegmentFailedFlag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 6, 1, 3),
    _ExtremeEapsSharedPortSegmentFailedFlag_Type()
)
extremeEapsSharedPortSegmentFailedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortSegmentFailedFlag.setStatus("current")


class _ExtremeEapsSharedPortSegmentVlanPortCount_Type(Integer32):
    """Custom type extremeEapsSharedPortSegmentVlanPortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEapsSharedPortSegmentVlanPortCount_Type.__name__ = "Integer32"
_ExtremeEapsSharedPortSegmentVlanPortCount_Object = MibTableColumn
extremeEapsSharedPortSegmentVlanPortCount = _ExtremeEapsSharedPortSegmentVlanPortCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 6, 1, 4),
    _ExtremeEapsSharedPortSegmentVlanPortCount_Type()
)
extremeEapsSharedPortSegmentVlanPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortSegmentVlanPortCount.setStatus("current")


class _ExtremeEapsSharedPortSegmentAdjId_Type(Integer32):
    """Custom type extremeEapsSharedPortSegmentAdjId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEapsSharedPortSegmentAdjId_Type.__name__ = "Integer32"
_ExtremeEapsSharedPortSegmentAdjId_Object = MibTableColumn
extremeEapsSharedPortSegmentAdjId = _ExtremeEapsSharedPortSegmentAdjId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 6, 1, 5),
    _ExtremeEapsSharedPortSegmentAdjId_Type()
)
extremeEapsSharedPortSegmentAdjId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortSegmentAdjId.setStatus("current")


class _ExtremeEapsSharedPortSegmentRBD_Type(Integer32):
    """Custom type extremeEapsSharedPortSegmentRBD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEapsSharedPortSegmentRBD_Type.__name__ = "Integer32"
_ExtremeEapsSharedPortSegmentRBD_Object = MibTableColumn
extremeEapsSharedPortSegmentRBD = _ExtremeEapsSharedPortSegmentRBD_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 6, 1, 6),
    _ExtremeEapsSharedPortSegmentRBD_Type()
)
extremeEapsSharedPortSegmentRBD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortSegmentRBD.setStatus("current")
_ExtremeEapsSharedPortVlanTable_Object = MibTable
extremeEapsSharedPortVlanTable = _ExtremeEapsSharedPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 7)
)
if mibBuilder.loadTexts:
    extremeEapsSharedPortVlanTable.setStatus("current")
_ExtremeEapsSharedPortVlanEntry_Object = MibTableRow
extremeEapsSharedPortVlanEntry = _ExtremeEapsSharedPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 7, 1)
)
extremeEapsSharedPortVlanEntry.setIndexNames(
    (0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortIfIndex"),
    (0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortVlanName"),
)
if mibBuilder.loadTexts:
    extremeEapsSharedPortVlanEntry.setStatus("current")


class _ExtremeEapsSharedPortVlanName_Type(DisplayString):
    """Custom type extremeEapsSharedPortVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeEapsSharedPortVlanName_Type.__name__ = "DisplayString"
_ExtremeEapsSharedPortVlanName_Object = MibTableColumn
extremeEapsSharedPortVlanName = _ExtremeEapsSharedPortVlanName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 7, 1, 1),
    _ExtremeEapsSharedPortVlanName_Type()
)
extremeEapsSharedPortVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortVlanName.setStatus("current")


class _ExtremeEapsSharedPortVlanPortCount_Type(Integer32):
    """Custom type extremeEapsSharedPortVlanPortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeEapsSharedPortVlanPortCount_Type.__name__ = "Integer32"
_ExtremeEapsSharedPortVlanPortCount_Object = MibTableColumn
extremeEapsSharedPortVlanPortCount = _ExtremeEapsSharedPortVlanPortCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 7, 1, 2),
    _ExtremeEapsSharedPortVlanPortCount_Type()
)
extremeEapsSharedPortVlanPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortVlanPortCount.setStatus("current")
_ExtremeEapsSharedPortVlanActiveOpenPort_Type = EapsRingPort
_ExtremeEapsSharedPortVlanActiveOpenPort_Object = MibTableColumn
extremeEapsSharedPortVlanActiveOpenPort = _ExtremeEapsSharedPortVlanActiveOpenPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 7, 1, 3),
    _ExtremeEapsSharedPortVlanActiveOpenPort_Type()
)
extremeEapsSharedPortVlanActiveOpenPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortVlanActiveOpenPort.setStatus("current")
_ExtremeEapsSharedPortVlanPortTable_Object = MibTable
extremeEapsSharedPortVlanPortTable = _ExtremeEapsSharedPortVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 8)
)
if mibBuilder.loadTexts:
    extremeEapsSharedPortVlanPortTable.setStatus("current")
_ExtremeEapsSharedPortVlanPortEntry_Object = MibTableRow
extremeEapsSharedPortVlanPortEntry = _ExtremeEapsSharedPortVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 8, 1)
)
extremeEapsSharedPortVlanPortEntry.setIndexNames(
    (0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortIfIndex"),
    (0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortVlanName"),
    (0, "EXTREME-EAPS-MIB", "extremeEapsSharedPortSegmentPort"),
    (0, "EXTREME-EAPS-MIB", "extremeEapsName"),
)
if mibBuilder.loadTexts:
    extremeEapsSharedPortVlanPortEntry.setStatus("current")
_ExtremeEapsSharedPortVlanPortStatus_Type = EapsSharedPortVlanPortStatus
_ExtremeEapsSharedPortVlanPortStatus_Object = MibTableColumn
extremeEapsSharedPortVlanPortStatus = _ExtremeEapsSharedPortVlanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 8, 1, 1),
    _ExtremeEapsSharedPortVlanPortStatus_Type()
)
extremeEapsSharedPortVlanPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsSharedPortVlanPortStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-EAPS-MIB",
    **{"EapsDomainMode": EapsDomainMode,
       "EapsMbrVlanType": EapsMbrVlanType,
       "EapsRingPort": EapsRingPort,
       "EapsPortType": EapsPortType,
       "EapsDomainState": EapsDomainState,
       "EapsDomainPortStatus": EapsDomainPortStatus,
       "EapsFailTimerExpiryAction": EapsFailTimerExpiryAction,
       "EapsSharedPortState": EapsSharedPortState,
       "EapsSharedPortMode": EapsSharedPortMode,
       "EapsSharedPortSegmentTimerExpiryAction": EapsSharedPortSegmentTimerExpiryAction,
       "EapsSharedPortNeighborStatus": EapsSharedPortNeighborStatus,
       "EapsSharedPortRootBlockerStatus": EapsSharedPortRootBlockerStatus,
       "EapsSharedPortSegmentStatus": EapsSharedPortSegmentStatus,
       "EapsSharedPortVlanPortStatus": EapsSharedPortVlanPortStatus,
       "EapsDomainPriority": EapsDomainPriority,
       "extremeEaps": extremeEaps,
       "extremeEapsTable": extremeEapsTable,
       "extremeEapsEntry": extremeEapsEntry,
       "extremeEapsName": extremeEapsName,
       "extremeEapsMode": extremeEapsMode,
       "extremeEapsState": extremeEapsState,
       "extremeEapsFailedFlag": extremeEapsFailedFlag,
       "extremeEapsEnabled": extremeEapsEnabled,
       "extremeEapsPrimaryPort": extremeEapsPrimaryPort,
       "extremeEapsSecondaryPort": extremeEapsSecondaryPort,
       "extremeEapsHelloTimer": extremeEapsHelloTimer,
       "extremeEapsFailedTimer": extremeEapsFailedTimer,
       "extremeEapsFailedTimerExpiryAction": extremeEapsFailedTimerExpiryAction,
       "extremeEapsUnconfigRingPort": extremeEapsUnconfigRingPort,
       "extremeEapsPrimaryStatus": extremeEapsPrimaryStatus,
       "extremeEapsSecondaryStatus": extremeEapsSecondaryStatus,
       "extremeEapsProtectedVlansCount": extremeEapsProtectedVlansCount,
       "extremeEapsRowStatus": extremeEapsRowStatus,
       "extremeEapsHelloTimerMs": extremeEapsHelloTimerMs,
       "extremeEapsPriority": extremeEapsPriority,
       "extremeEapsPrevState": extremeEapsPrevState,
       "extremeEapsGlobalInfo": extremeEapsGlobalInfo,
       "extremeEapsGlobalEnabled": extremeEapsGlobalEnabled,
       "extremeEapsGlobalFastConvergence": extremeEapsGlobalFastConvergence,
       "extremeEapsLastConfigurationChange": extremeEapsLastConfigurationChange,
       "extremeEapsLastStatusChange": extremeEapsLastStatusChange,
       "extremeEapsStatusTrapCount": extremeEapsStatusTrapCount,
       "extremeEapsGlobalMulticastAddRingPorts": extremeEapsGlobalMulticastAddRingPorts,
       "extremeEapsGlobalMulticastSendIGMPQuery": extremeEapsGlobalMulticastSendIGMPQuery,
       "extremeEapsGlobalMulticastTempFlooding": extremeEapsGlobalMulticastTempFlooding,
       "extremeEapsGlobalMulticastTempFloodingDuration": extremeEapsGlobalMulticastTempFloodingDuration,
       "extremeEapsMbrVlanTable": extremeEapsMbrVlanTable,
       "extremeEapsMbrVlanEntry": extremeEapsMbrVlanEntry,
       "extremeEapsMbrVlanName": extremeEapsMbrVlanName,
       "extremeEapsMbrVlanType": extremeEapsMbrVlanType,
       "extremeEapsMbrVlanTag": extremeEapsMbrVlanTag,
       "extremeEapsMbrVlanRowStatus": extremeEapsMbrVlanRowStatus,
       "extremeEapsSharedPortTable": extremeEapsSharedPortTable,
       "extremeEapsSharedPortEntry": extremeEapsSharedPortEntry,
       "extremeEapsSharedPortIfIndex": extremeEapsSharedPortIfIndex,
       "extremeEapsSharedPortMode": extremeEapsSharedPortMode,
       "extremeEapsSharedPortLinkId": extremeEapsSharedPortLinkId,
       "extremeEapsSharedPortSegmentTimerExpiryAction": extremeEapsSharedPortSegmentTimerExpiryAction,
       "extremeEapsSharedPortState": extremeEapsSharedPortState,
       "extremeEapsSharedPortNbrStatus": extremeEapsSharedPortNbrStatus,
       "extremeEapsSharedPortDomainsCount": extremeEapsSharedPortDomainsCount,
       "extremeEapsSharedPortProtectedVlansCount": extremeEapsSharedPortProtectedVlansCount,
       "extremeEapsSharedPortRootBlockerStatus": extremeEapsSharedPortRootBlockerStatus,
       "extremeEapsSharedPortRootBlockerId": extremeEapsSharedPortRootBlockerId,
       "extremeEapsSharedPortRowStatus": extremeEapsSharedPortRowStatus,
       "extremeEapsSharedPortSegmentHealthInterval": extremeEapsSharedPortSegmentHealthInterval,
       "extremeEapsSharedPortSegmentTimeout": extremeEapsSharedPortSegmentTimeout,
       "extremeEapsSharedPortCommonPathFailedFlag": extremeEapsSharedPortCommonPathFailedFlag,
       "extremeEapsSharedPortCommonPathHealthInterval": extremeEapsSharedPortCommonPathHealthInterval,
       "extremeEapsSharedPortCommonPathTimeout": extremeEapsSharedPortCommonPathTimeout,
       "extremeEapsSharedPortSegmentTable": extremeEapsSharedPortSegmentTable,
       "extremeEapsSharedPortSegmentEntry": extremeEapsSharedPortSegmentEntry,
       "extremeEapsSharedPortSegmentPort": extremeEapsSharedPortSegmentPort,
       "extremeEapsSharedPortSegmentStatus": extremeEapsSharedPortSegmentStatus,
       "extremeEapsSharedPortSegmentFailedFlag": extremeEapsSharedPortSegmentFailedFlag,
       "extremeEapsSharedPortSegmentVlanPortCount": extremeEapsSharedPortSegmentVlanPortCount,
       "extremeEapsSharedPortSegmentAdjId": extremeEapsSharedPortSegmentAdjId,
       "extremeEapsSharedPortSegmentRBD": extremeEapsSharedPortSegmentRBD,
       "extremeEapsSharedPortVlanTable": extremeEapsSharedPortVlanTable,
       "extremeEapsSharedPortVlanEntry": extremeEapsSharedPortVlanEntry,
       "extremeEapsSharedPortVlanName": extremeEapsSharedPortVlanName,
       "extremeEapsSharedPortVlanPortCount": extremeEapsSharedPortVlanPortCount,
       "extremeEapsSharedPortVlanActiveOpenPort": extremeEapsSharedPortVlanActiveOpenPort,
       "extremeEapsSharedPortVlanPortTable": extremeEapsSharedPortVlanPortTable,
       "extremeEapsSharedPortVlanPortEntry": extremeEapsSharedPortVlanPortEntry,
       "extremeEapsSharedPortVlanPortStatus": extremeEapsSharedPortVlanPortStatus}
)
