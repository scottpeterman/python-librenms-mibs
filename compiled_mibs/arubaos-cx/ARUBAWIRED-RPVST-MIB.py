# SNMP MIB module (ARUBAWIRED-RPVST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-RPVST-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:27 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arubaWiredRpvstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    arubaWiredRpvstMIB.setRevisions(
        ("2020-11-25 00:00",
         "2020-10-22 00:00",
         "2020-06-12 00:00",
         "2018-05-29 00:00",
         "2018-01-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PointToPoint(TextualConvention, Integer32):
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
        *(("forceTrue", 1),
          ("forceFalse", 2),
          ("auto", 3))
    )



# MIB Managed Objects in the order of their OIDs

_ArubaWiredRpvstNotifications_ObjectIdentity = ObjectIdentity
arubaWiredRpvstNotifications = _ArubaWiredRpvstNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 0)
)
_ArubaWiredRpvstObjects_ObjectIdentity = ObjectIdentity
arubaWiredRpvstObjects = _ArubaWiredRpvstObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1)
)
_ArubaWiredRpvstGeneralGroup_ObjectIdentity = ObjectIdentity
arubaWiredRpvstGeneralGroup = _ArubaWiredRpvstGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 1)
)


class _ArubaWiredRpvstResetCounters_Type(TruthValue):
    """Custom type arubaWiredRpvstResetCounters based on TruthValue"""
    defaultValue = 2


_ArubaWiredRpvstResetCounters_Type.__name__ = "TruthValue"
_ArubaWiredRpvstResetCounters_Object = MibScalar
arubaWiredRpvstResetCounters = _ArubaWiredRpvstResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 1, 1),
    _ArubaWiredRpvstResetCounters_Type()
)
arubaWiredRpvstResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstResetCounters.setStatus("current")


class _ArubaWiredRpvstExtendedSystemID_Type(TruthValue):
    """Custom type arubaWiredRpvstExtendedSystemID based on TruthValue"""
    defaultValue = 1


_ArubaWiredRpvstExtendedSystemID_Type.__name__ = "TruthValue"
_ArubaWiredRpvstExtendedSystemID_Object = MibScalar
arubaWiredRpvstExtendedSystemID = _ArubaWiredRpvstExtendedSystemID_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 1, 2),
    _ArubaWiredRpvstExtendedSystemID_Type()
)
arubaWiredRpvstExtendedSystemID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstExtendedSystemID.setStatus("current")


class _ArubaWiredRpvstIgnorePVIDInconsistency_Type(TruthValue):
    """Custom type arubaWiredRpvstIgnorePVIDInconsistency based on TruthValue"""
    defaultValue = 2


_ArubaWiredRpvstIgnorePVIDInconsistency_Type.__name__ = "TruthValue"
_ArubaWiredRpvstIgnorePVIDInconsistency_Object = MibScalar
arubaWiredRpvstIgnorePVIDInconsistency = _ArubaWiredRpvstIgnorePVIDInconsistency_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 1, 3),
    _ArubaWiredRpvstIgnorePVIDInconsistency_Type()
)
arubaWiredRpvstIgnorePVIDInconsistency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstIgnorePVIDInconsistency.setStatus("current")


class _ArubaWiredRpvstPathCostMode_Type(Integer32):
    """Custom type arubaWiredRpvstPathCostMode based on Integer32"""
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
        *(("pathCost8021d", 1),
          ("pathCost8021t", 2),
          ("proprietary", 3))
    )


_ArubaWiredRpvstPathCostMode_Type.__name__ = "Integer32"
_ArubaWiredRpvstPathCostMode_Object = MibScalar
arubaWiredRpvstPathCostMode = _ArubaWiredRpvstPathCostMode_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 1, 4),
    _ArubaWiredRpvstPathCostMode_Type()
)
arubaWiredRpvstPathCostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstPathCostMode.setStatus("current")
_ArubaWiredRpvstBpduGuardTimeout_Type = Integer32
_ArubaWiredRpvstBpduGuardTimeout_Object = MibScalar
arubaWiredRpvstBpduGuardTimeout = _ArubaWiredRpvstBpduGuardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 1, 5),
    _ArubaWiredRpvstBpduGuardTimeout_Type()
)
arubaWiredRpvstBpduGuardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstBpduGuardTimeout.setStatus("current")
_ArubaWiredRpvstMstpInterconnectVlan_Type = Integer32
_ArubaWiredRpvstMstpInterconnectVlan_Object = MibScalar
arubaWiredRpvstMstpInterconnectVlan = _ArubaWiredRpvstMstpInterconnectVlan_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 1, 6),
    _ArubaWiredRpvstMstpInterconnectVlan_Type()
)
arubaWiredRpvstMstpInterconnectVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstMstpInterconnectVlan.setStatus("current")
_ArubaWiredRpvstCurrentVportCount_Type = Integer32
_ArubaWiredRpvstCurrentVportCount_Object = MibScalar
arubaWiredRpvstCurrentVportCount = _ArubaWiredRpvstCurrentVportCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 1, 7),
    _ArubaWiredRpvstCurrentVportCount_Type()
)
arubaWiredRpvstCurrentVportCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstCurrentVportCount.setStatus("current")
_ArubaWiredRpvstVlanTable_Object = MibTable
arubaWiredRpvstVlanTable = _ArubaWiredRpvstVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanTable.setStatus("current")
_ArubaWiredRpvstVlanEntry_Object = MibTableRow
arubaWiredRpvstVlanEntry = _ArubaWiredRpvstVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1)
)
arubaWiredRpvstVlanEntry.setIndexNames(
    (0, "ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanId"),
)
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanEntry.setStatus("current")
_ArubaWiredRpvstVlanId_Type = VlanIndex
_ArubaWiredRpvstVlanId_Object = MibTableColumn
arubaWiredRpvstVlanId = _ArubaWiredRpvstVlanId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 1),
    _ArubaWiredRpvstVlanId_Type()
)
arubaWiredRpvstVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanId.setStatus("current")


class _ArubaWiredRpvstVlanHelloTime_Type(Integer32):
    """Custom type arubaWiredRpvstVlanHelloTime based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_ArubaWiredRpvstVlanHelloTime_Type.__name__ = "Integer32"
_ArubaWiredRpvstVlanHelloTime_Object = MibTableColumn
arubaWiredRpvstVlanHelloTime = _ArubaWiredRpvstVlanHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 2),
    _ArubaWiredRpvstVlanHelloTime_Type()
)
arubaWiredRpvstVlanHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanHelloTime.setUnits("seconds")


class _ArubaWiredRpvstVlanForwardDelay_Type(Integer32):
    """Custom type arubaWiredRpvstVlanForwardDelay based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_ArubaWiredRpvstVlanForwardDelay_Type.__name__ = "Integer32"
_ArubaWiredRpvstVlanForwardDelay_Object = MibTableColumn
arubaWiredRpvstVlanForwardDelay = _ArubaWiredRpvstVlanForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 3),
    _ArubaWiredRpvstVlanForwardDelay_Type()
)
arubaWiredRpvstVlanForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanForwardDelay.setUnits("seconds")


class _ArubaWiredRpvstVlanMaxAge_Type(Integer32):
    """Custom type arubaWiredRpvstVlanMaxAge based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_ArubaWiredRpvstVlanMaxAge_Type.__name__ = "Integer32"
_ArubaWiredRpvstVlanMaxAge_Object = MibTableColumn
arubaWiredRpvstVlanMaxAge = _ArubaWiredRpvstVlanMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 4),
    _ArubaWiredRpvstVlanMaxAge_Type()
)
arubaWiredRpvstVlanMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanMaxAge.setUnits("seconds")


class _ArubaWiredRpvstVlanPriority_Type(Integer32):
    """Custom type arubaWiredRpvstVlanPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArubaWiredRpvstVlanPriority_Type.__name__ = "Integer32"
_ArubaWiredRpvstVlanPriority_Object = MibTableColumn
arubaWiredRpvstVlanPriority = _ArubaWiredRpvstVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 5),
    _ArubaWiredRpvstVlanPriority_Type()
)
arubaWiredRpvstVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanPriority.setStatus("current")


class _ArubaWiredRpvstVlanRoot_Type(Integer32):
    """Custom type arubaWiredRpvstVlanRoot based on Integer32"""
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
          ("primary", 1),
          ("secondary", 2))
    )


_ArubaWiredRpvstVlanRoot_Type.__name__ = "Integer32"
_ArubaWiredRpvstVlanRoot_Object = MibTableColumn
arubaWiredRpvstVlanRoot = _ArubaWiredRpvstVlanRoot_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 6),
    _ArubaWiredRpvstVlanRoot_Type()
)
arubaWiredRpvstVlanRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanRoot.setStatus("current")


class _ArubaWiredRpvstVlanRpvstAdminStatus_Type(Integer32):
    """Custom type arubaWiredRpvstVlanRpvstAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ArubaWiredRpvstVlanRpvstAdminStatus_Type.__name__ = "Integer32"
_ArubaWiredRpvstVlanRpvstAdminStatus_Object = MibTableColumn
arubaWiredRpvstVlanRpvstAdminStatus = _ArubaWiredRpvstVlanRpvstAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 7),
    _ArubaWiredRpvstVlanRpvstAdminStatus_Type()
)
arubaWiredRpvstVlanRpvstAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanRpvstAdminStatus.setStatus("current")


class _ArubaWiredRpvstVlanResetCounters_Type(TruthValue):
    """Custom type arubaWiredRpvstVlanResetCounters based on TruthValue"""
    defaultValue = 2


_ArubaWiredRpvstVlanResetCounters_Type.__name__ = "TruthValue"
_ArubaWiredRpvstVlanResetCounters_Object = MibTableColumn
arubaWiredRpvstVlanResetCounters = _ArubaWiredRpvstVlanResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 8),
    _ArubaWiredRpvstVlanResetCounters_Type()
)
arubaWiredRpvstVlanResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanResetCounters.setStatus("current")


class _ArubaWiredRpvstVlanOperHelloTime_Type(Integer32):
    """Custom type arubaWiredRpvstVlanOperHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ArubaWiredRpvstVlanOperHelloTime_Type.__name__ = "Integer32"
_ArubaWiredRpvstVlanOperHelloTime_Object = MibTableColumn
arubaWiredRpvstVlanOperHelloTime = _ArubaWiredRpvstVlanOperHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 9),
    _ArubaWiredRpvstVlanOperHelloTime_Type()
)
arubaWiredRpvstVlanOperHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanOperHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanOperHelloTime.setUnits("seconds")


class _ArubaWiredRpvstVlanRootPriority_Type(Integer32):
    """Custom type arubaWiredRpvstVlanRootPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArubaWiredRpvstVlanRootPriority_Type.__name__ = "Integer32"
_ArubaWiredRpvstVlanRootPriority_Object = MibTableColumn
arubaWiredRpvstVlanRootPriority = _ArubaWiredRpvstVlanRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 10),
    _ArubaWiredRpvstVlanRootPriority_Type()
)
arubaWiredRpvstVlanRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanRootPriority.setStatus("current")
_ArubaWiredRpvstVlanRootPort_Type = InterfaceIndex
_ArubaWiredRpvstVlanRootPort_Object = MibTableColumn
arubaWiredRpvstVlanRootPort = _ArubaWiredRpvstVlanRootPort_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 11),
    _ArubaWiredRpvstVlanRootPort_Type()
)
arubaWiredRpvstVlanRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanRootPort.setStatus("current")


class _ArubaWiredRpvstVlanRootPathCost_Type(Integer32):
    """Custom type arubaWiredRpvstVlanRootPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_ArubaWiredRpvstVlanRootPathCost_Type.__name__ = "Integer32"
_ArubaWiredRpvstVlanRootPathCost_Object = MibTableColumn
arubaWiredRpvstVlanRootPathCost = _ArubaWiredRpvstVlanRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 12),
    _ArubaWiredRpvstVlanRootPathCost_Type()
)
arubaWiredRpvstVlanRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanRootPathCost.setStatus("current")
_ArubaWiredRpvstVlanRootMacAddress_Type = MacAddress
_ArubaWiredRpvstVlanRootMacAddress_Object = MibTableColumn
arubaWiredRpvstVlanRootMacAddress = _ArubaWiredRpvstVlanRootMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 13),
    _ArubaWiredRpvstVlanRootMacAddress_Type()
)
arubaWiredRpvstVlanRootMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanRootMacAddress.setStatus("current")
_ArubaWiredRpvstVlanRootChangeCounter_Type = Counter32
_ArubaWiredRpvstVlanRootChangeCounter_Object = MibTableColumn
arubaWiredRpvstVlanRootChangeCounter = _ArubaWiredRpvstVlanRootChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 14),
    _ArubaWiredRpvstVlanRootChangeCounter_Type()
)
arubaWiredRpvstVlanRootChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanRootChangeCounter.setStatus("current")
_ArubaWiredRpvstVlanTimeSinceLastTopoChange_Type = TimeTicks
_ArubaWiredRpvstVlanTimeSinceLastTopoChange_Object = MibTableColumn
arubaWiredRpvstVlanTimeSinceLastTopoChange = _ArubaWiredRpvstVlanTimeSinceLastTopoChange_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 15),
    _ArubaWiredRpvstVlanTimeSinceLastTopoChange_Type()
)
arubaWiredRpvstVlanTimeSinceLastTopoChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanTimeSinceLastTopoChange.setStatus("current")
_ArubaWiredRpvstVlanTopoChangeCount_Type = Counter32
_ArubaWiredRpvstVlanTopoChangeCount_Object = MibTableColumn
arubaWiredRpvstVlanTopoChangeCount = _ArubaWiredRpvstVlanTopoChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 16),
    _ArubaWiredRpvstVlanTopoChangeCount_Type()
)
arubaWiredRpvstVlanTopoChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanTopoChangeCount.setStatus("current")


class _ArubaWiredRpvstVlanSendTopoChangeCtrl_Type(TruthValue):
    """Custom type arubaWiredRpvstVlanSendTopoChangeCtrl based on TruthValue"""
    defaultValue = 2


_ArubaWiredRpvstVlanSendTopoChangeCtrl_Type.__name__ = "TruthValue"
_ArubaWiredRpvstVlanSendTopoChangeCtrl_Object = MibTableColumn
arubaWiredRpvstVlanSendTopoChangeCtrl = _ArubaWiredRpvstVlanSendTopoChangeCtrl_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 17),
    _ArubaWiredRpvstVlanSendTopoChangeCtrl_Type()
)
arubaWiredRpvstVlanSendTopoChangeCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanSendTopoChangeCtrl.setStatus("current")


class _ArubaWiredRpvstVlanLogPortStateTransitions_Type(TruthValue):
    """Custom type arubaWiredRpvstVlanLogPortStateTransitions based on TruthValue"""
    defaultValue = 2


_ArubaWiredRpvstVlanLogPortStateTransitions_Type.__name__ = "TruthValue"
_ArubaWiredRpvstVlanLogPortStateTransitions_Object = MibTableColumn
arubaWiredRpvstVlanLogPortStateTransitions = _ArubaWiredRpvstVlanLogPortStateTransitions_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 2, 1, 18),
    _ArubaWiredRpvstVlanLogPortStateTransitions_Type()
)
arubaWiredRpvstVlanLogPortStateTransitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanLogPortStateTransitions.setStatus("current")
_ArubaWiredRpvstPortTable_Object = MibTable
arubaWiredRpvstPortTable = _ArubaWiredRpvstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 3)
)
if mibBuilder.loadTexts:
    arubaWiredRpvstPortTable.setStatus("current")
_ArubaWiredRpvstPortEntry_Object = MibTableRow
arubaWiredRpvstPortEntry = _ArubaWiredRpvstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 3, 1)
)
arubaWiredRpvstPortEntry.setIndexNames(
    (0, "ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredRpvstPortEntry.setStatus("current")
_ArubaWiredRpvstPortIndex_Type = InterfaceIndex
_ArubaWiredRpvstPortIndex_Object = MibTableColumn
arubaWiredRpvstPortIndex = _ArubaWiredRpvstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 3, 1, 1),
    _ArubaWiredRpvstPortIndex_Type()
)
arubaWiredRpvstPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortIndex.setStatus("current")


class _ArubaWiredRpvstPortAdminEdge_Type(TruthValue):
    """Custom type arubaWiredRpvstPortAdminEdge based on TruthValue"""
    defaultValue = 2


_ArubaWiredRpvstPortAdminEdge_Type.__name__ = "TruthValue"
_ArubaWiredRpvstPortAdminEdge_Object = MibTableColumn
arubaWiredRpvstPortAdminEdge = _ArubaWiredRpvstPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 3, 1, 2),
    _ArubaWiredRpvstPortAdminEdge_Type()
)
arubaWiredRpvstPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortAdminEdge.setStatus("current")


class _ArubaWiredRpvstPortAdminPointToPoint_Type(PointToPoint):
    """Custom type arubaWiredRpvstPortAdminPointToPoint based on PointToPoint"""
    defaultValue = 3


_ArubaWiredRpvstPortAdminPointToPoint_Type.__name__ = "PointToPoint"
_ArubaWiredRpvstPortAdminPointToPoint_Object = MibTableColumn
arubaWiredRpvstPortAdminPointToPoint = _ArubaWiredRpvstPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 3, 1, 3),
    _ArubaWiredRpvstPortAdminPointToPoint_Type()
)
arubaWiredRpvstPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortAdminPointToPoint.setStatus("current")


class _ArubaWiredRpvstPortAutoEdge_Type(TruthValue):
    """Custom type arubaWiredRpvstPortAutoEdge based on TruthValue"""
    defaultValue = 1


_ArubaWiredRpvstPortAutoEdge_Type.__name__ = "TruthValue"
_ArubaWiredRpvstPortAutoEdge_Object = MibTableColumn
arubaWiredRpvstPortAutoEdge = _ArubaWiredRpvstPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 3, 1, 4),
    _ArubaWiredRpvstPortAutoEdge_Type()
)
arubaWiredRpvstPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortAutoEdge.setStatus("current")


class _ArubaWiredRpvstPortBpduFiltering_Type(TruthValue):
    """Custom type arubaWiredRpvstPortBpduFiltering based on TruthValue"""
    defaultValue = 2


_ArubaWiredRpvstPortBpduFiltering_Type.__name__ = "TruthValue"
_ArubaWiredRpvstPortBpduFiltering_Object = MibTableColumn
arubaWiredRpvstPortBpduFiltering = _ArubaWiredRpvstPortBpduFiltering_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 3, 1, 5),
    _ArubaWiredRpvstPortBpduFiltering_Type()
)
arubaWiredRpvstPortBpduFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortBpduFiltering.setStatus("current")


class _ArubaWiredRpvstPortRestrictedTcn_Type(TruthValue):
    """Custom type arubaWiredRpvstPortRestrictedTcn based on TruthValue"""
    defaultValue = 2


_ArubaWiredRpvstPortRestrictedTcn_Type.__name__ = "TruthValue"
_ArubaWiredRpvstPortRestrictedTcn_Object = MibTableColumn
arubaWiredRpvstPortRestrictedTcn = _ArubaWiredRpvstPortRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 3, 1, 6),
    _ArubaWiredRpvstPortRestrictedTcn_Type()
)
arubaWiredRpvstPortRestrictedTcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortRestrictedTcn.setStatus("current")


class _ArubaWiredRpvstPortRootGuard_Type(TruthValue):
    """Custom type arubaWiredRpvstPortRootGuard based on TruthValue"""
    defaultValue = 2


_ArubaWiredRpvstPortRootGuard_Type.__name__ = "TruthValue"
_ArubaWiredRpvstPortRootGuard_Object = MibTableColumn
arubaWiredRpvstPortRootGuard = _ArubaWiredRpvstPortRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 3, 1, 7),
    _ArubaWiredRpvstPortRootGuard_Type()
)
arubaWiredRpvstPortRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortRootGuard.setStatus("current")


class _ArubaWiredRpvstPortLoopGuard_Type(TruthValue):
    """Custom type arubaWiredRpvstPortLoopGuard based on TruthValue"""
    defaultValue = 2


_ArubaWiredRpvstPortLoopGuard_Type.__name__ = "TruthValue"
_ArubaWiredRpvstPortLoopGuard_Object = MibTableColumn
arubaWiredRpvstPortLoopGuard = _ArubaWiredRpvstPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 3, 1, 8),
    _ArubaWiredRpvstPortLoopGuard_Type()
)
arubaWiredRpvstPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortLoopGuard.setStatus("current")


class _ArubaWiredRpvstPortBpduProtection_Type(TruthValue):
    """Custom type arubaWiredRpvstPortBpduProtection based on TruthValue"""
    defaultValue = 2


_ArubaWiredRpvstPortBpduProtection_Type.__name__ = "TruthValue"
_ArubaWiredRpvstPortBpduProtection_Object = MibTableColumn
arubaWiredRpvstPortBpduProtection = _ArubaWiredRpvstPortBpduProtection_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 3, 1, 9),
    _ArubaWiredRpvstPortBpduProtection_Type()
)
arubaWiredRpvstPortBpduProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortBpduProtection.setStatus("current")
_ArubaWiredRpvstPortVlanTable_Object = MibTable
arubaWiredRpvstPortVlanTable = _ArubaWiredRpvstPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 4)
)
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanTable.setStatus("current")
_ArubaWiredRpvstPortVlanEntry_Object = MibTableRow
arubaWiredRpvstPortVlanEntry = _ArubaWiredRpvstPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 4, 1)
)
arubaWiredRpvstPortVlanEntry.setIndexNames(
    (0, "ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanId"),
    (0, "ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanEntry.setStatus("current")
_ArubaWiredRpvstPortVlanId_Type = VlanIndex
_ArubaWiredRpvstPortVlanId_Object = MibTableColumn
arubaWiredRpvstPortVlanId = _ArubaWiredRpvstPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 4, 1, 1),
    _ArubaWiredRpvstPortVlanId_Type()
)
arubaWiredRpvstPortVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanId.setStatus("current")
_ArubaWiredRpvstPortVlanIndex_Type = InterfaceIndex
_ArubaWiredRpvstPortVlanIndex_Object = MibTableColumn
arubaWiredRpvstPortVlanIndex = _ArubaWiredRpvstPortVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 4, 1, 2),
    _ArubaWiredRpvstPortVlanIndex_Type()
)
arubaWiredRpvstPortVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanIndex.setStatus("current")


class _ArubaWiredRpvstPortVlanPathCost_Type(Integer32):
    """Custom type arubaWiredRpvstPortVlanPathCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_ArubaWiredRpvstPortVlanPathCost_Type.__name__ = "Integer32"
_ArubaWiredRpvstPortVlanPathCost_Object = MibTableColumn
arubaWiredRpvstPortVlanPathCost = _ArubaWiredRpvstPortVlanPathCost_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 4, 1, 3),
    _ArubaWiredRpvstPortVlanPathCost_Type()
)
arubaWiredRpvstPortVlanPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanPathCost.setStatus("current")


class _ArubaWiredRpvstPortVlanPriority_Type(Integer32):
    """Custom type arubaWiredRpvstPortVlanPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ArubaWiredRpvstPortVlanPriority_Type.__name__ = "Integer32"
_ArubaWiredRpvstPortVlanPriority_Object = MibTableColumn
arubaWiredRpvstPortVlanPriority = _ArubaWiredRpvstPortVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 4, 1, 4),
    _ArubaWiredRpvstPortVlanPriority_Type()
)
arubaWiredRpvstPortVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanPriority.setStatus("current")


class _ArubaWiredRpvstPortVlanResetCounters_Type(TruthValue):
    """Custom type arubaWiredRpvstPortVlanResetCounters based on TruthValue"""
    defaultValue = 2


_ArubaWiredRpvstPortVlanResetCounters_Type.__name__ = "TruthValue"
_ArubaWiredRpvstPortVlanResetCounters_Object = MibTableColumn
arubaWiredRpvstPortVlanResetCounters = _ArubaWiredRpvstPortVlanResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 4, 1, 5),
    _ArubaWiredRpvstPortVlanResetCounters_Type()
)
arubaWiredRpvstPortVlanResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanResetCounters.setStatus("current")


class _ArubaWiredRpvstPortVlanRole_Type(Integer32):
    """Custom type arubaWiredRpvstPortVlanRole based on Integer32"""
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
        *(("root", 1),
          ("alternate", 2),
          ("designated", 3),
          ("backup", 4),
          ("master", 5),
          ("disabled", 6))
    )


_ArubaWiredRpvstPortVlanRole_Type.__name__ = "Integer32"
_ArubaWiredRpvstPortVlanRole_Object = MibTableColumn
arubaWiredRpvstPortVlanRole = _ArubaWiredRpvstPortVlanRole_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 4, 1, 6),
    _ArubaWiredRpvstPortVlanRole_Type()
)
arubaWiredRpvstPortVlanRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanRole.setStatus("current")


class _ArubaWiredRpvstPortVlanState_Type(Integer32):
    """Custom type arubaWiredRpvstPortVlanState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6),
          ("bpduError", 7),
          ("loopInconsistent", 8),
          ("pvidInconsistent", 9),
          ("rootGuard", 10))
    )


_ArubaWiredRpvstPortVlanState_Type.__name__ = "Integer32"
_ArubaWiredRpvstPortVlanState_Object = MibTableColumn
arubaWiredRpvstPortVlanState = _ArubaWiredRpvstPortVlanState_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 4, 1, 7),
    _ArubaWiredRpvstPortVlanState_Type()
)
arubaWiredRpvstPortVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanState.setStatus("current")
_ArubaWiredRpvstPortVlanDesigBridge_Type = MacAddress
_ArubaWiredRpvstPortVlanDesigBridge_Object = MibTableColumn
arubaWiredRpvstPortVlanDesigBridge = _ArubaWiredRpvstPortVlanDesigBridge_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 4, 1, 8),
    _ArubaWiredRpvstPortVlanDesigBridge_Type()
)
arubaWiredRpvstPortVlanDesigBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanDesigBridge.setStatus("current")
_ArubaWiredRpvstPortVlanOperPointToPoint_Type = TruthValue
_ArubaWiredRpvstPortVlanOperPointToPoint_Object = MibTableColumn
arubaWiredRpvstPortVlanOperPointToPoint = _ArubaWiredRpvstPortVlanOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 4, 1, 9),
    _ArubaWiredRpvstPortVlanOperPointToPoint_Type()
)
arubaWiredRpvstPortVlanOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanOperPointToPoint.setStatus("current")
_ArubaWiredRpvstPortVlanOperEdge_Type = TruthValue
_ArubaWiredRpvstPortVlanOperEdge_Object = MibTableColumn
arubaWiredRpvstPortVlanOperEdge = _ArubaWiredRpvstPortVlanOperEdge_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 4, 1, 10),
    _ArubaWiredRpvstPortVlanOperEdge_Type()
)
arubaWiredRpvstPortVlanOperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanOperEdge.setStatus("current")


class _ArubaWiredRpvstPortVlanInconsistencyReason_Type(Integer32):
    """Custom type arubaWiredRpvstPortVlanInconsistencyReason based on Integer32"""
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
        *(("invalid", 0),
          ("rootProtected", 1),
          ("loopProtected", 2),
          ("inconsistentPvidProtected", 3))
    )


_ArubaWiredRpvstPortVlanInconsistencyReason_Type.__name__ = "Integer32"
_ArubaWiredRpvstPortVlanInconsistencyReason_Object = MibTableColumn
arubaWiredRpvstPortVlanInconsistencyReason = _ArubaWiredRpvstPortVlanInconsistencyReason_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 4, 1, 11),
    _ArubaWiredRpvstPortVlanInconsistencyReason_Type()
)
arubaWiredRpvstPortVlanInconsistencyReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanInconsistencyReason.setStatus("current")
_ArubaWiredRpvstNotificationTable_Object = MibTable
arubaWiredRpvstNotificationTable = _ArubaWiredRpvstNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5)
)
if mibBuilder.loadTexts:
    arubaWiredRpvstNotificationTable.setStatus("current")
_ArubaWiredRpvstNotificationEntry_Object = MibTableRow
arubaWiredRpvstNotificationEntry = _ArubaWiredRpvstNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1)
)
arubaWiredRpvstNotificationEntry.setIndexNames(
    (0, "ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstId"),
)
if mibBuilder.loadTexts:
    arubaWiredRpvstNotificationEntry.setStatus("current")


class _ArubaWiredRpvstPortName_Type(DisplayString):
    """Custom type arubaWiredRpvstPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredRpvstPortName_Type.__name__ = "DisplayString"
_ArubaWiredRpvstPortName_Object = MibTableColumn
arubaWiredRpvstPortName = _ArubaWiredRpvstPortName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 1),
    _ArubaWiredRpvstPortName_Type()
)
arubaWiredRpvstPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortName.setStatus("current")


class _ArubaWiredRpvstVlanIndex_Type(Integer32):
    """Custom type arubaWiredRpvstVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_ArubaWiredRpvstVlanIndex_Type.__name__ = "Integer32"
_ArubaWiredRpvstVlanIndex_Object = MibTableColumn
arubaWiredRpvstVlanIndex = _ArubaWiredRpvstVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 2),
    _ArubaWiredRpvstVlanIndex_Type()
)
arubaWiredRpvstVlanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanIndex.setStatus("current")


class _ArubaWiredRpvstPortVlanErrantBpduRxCount_Type(Integer32):
    """Custom type arubaWiredRpvstPortVlanErrantBpduRxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ArubaWiredRpvstPortVlanErrantBpduRxCount_Type.__name__ = "Integer32"
_ArubaWiredRpvstPortVlanErrantBpduRxCount_Object = MibTableColumn
arubaWiredRpvstPortVlanErrantBpduRxCount = _ArubaWiredRpvstPortVlanErrantBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 3),
    _ArubaWiredRpvstPortVlanErrantBpduRxCount_Type()
)
arubaWiredRpvstPortVlanErrantBpduRxCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanErrantBpduRxCount.setStatus("current")
_ArubaWiredRpvstErrantBpduSrcMac_Type = MacAddress
_ArubaWiredRpvstErrantBpduSrcMac_Object = MibTableColumn
arubaWiredRpvstErrantBpduSrcMac = _ArubaWiredRpvstErrantBpduSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 4),
    _ArubaWiredRpvstErrantBpduSrcMac_Type()
)
arubaWiredRpvstErrantBpduSrcMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredRpvstErrantBpduSrcMac.setStatus("current")


class _ArubaWiredRpvstSuperiorBpduSrcPort_Type(DisplayString):
    """Custom type arubaWiredRpvstSuperiorBpduSrcPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredRpvstSuperiorBpduSrcPort_Type.__name__ = "DisplayString"
_ArubaWiredRpvstSuperiorBpduSrcPort_Object = MibTableColumn
arubaWiredRpvstSuperiorBpduSrcPort = _ArubaWiredRpvstSuperiorBpduSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 5),
    _ArubaWiredRpvstSuperiorBpduSrcPort_Type()
)
arubaWiredRpvstSuperiorBpduSrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredRpvstSuperiorBpduSrcPort.setStatus("current")
_ArubaWiredRpvstSuperiorBpduSrcMac_Type = MacAddress
_ArubaWiredRpvstSuperiorBpduSrcMac_Object = MibTableColumn
arubaWiredRpvstSuperiorBpduSrcMac = _ArubaWiredRpvstSuperiorBpduSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 6),
    _ArubaWiredRpvstSuperiorBpduSrcMac_Type()
)
arubaWiredRpvstSuperiorBpduSrcMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredRpvstSuperiorBpduSrcMac.setStatus("current")


class _ArubaWiredRpvstErrantBpduDetector_Type(Integer32):
    """Custom type arubaWiredRpvstErrantBpduDetector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bpduFilter", 1),
          ("bpduProtection", 2))
    )


_ArubaWiredRpvstErrantBpduDetector_Type.__name__ = "Integer32"
_ArubaWiredRpvstErrantBpduDetector_Object = MibTableColumn
arubaWiredRpvstErrantBpduDetector = _ArubaWiredRpvstErrantBpduDetector_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 7),
    _ArubaWiredRpvstErrantBpduDetector_Type()
)
arubaWiredRpvstErrantBpduDetector.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredRpvstErrantBpduDetector.setStatus("current")


class _ArubaWiredRpvstDesignatedPort_Type(DisplayString):
    """Custom type arubaWiredRpvstDesignatedPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredRpvstDesignatedPort_Type.__name__ = "DisplayString"
_ArubaWiredRpvstDesignatedPort_Object = MibTableColumn
arubaWiredRpvstDesignatedPort = _ArubaWiredRpvstDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 8),
    _ArubaWiredRpvstDesignatedPort_Type()
)
arubaWiredRpvstDesignatedPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredRpvstDesignatedPort.setStatus("current")


class _ArubaWiredRpvstOldPortRole_Type(DisplayString):
    """Custom type arubaWiredRpvstOldPortRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredRpvstOldPortRole_Type.__name__ = "DisplayString"
_ArubaWiredRpvstOldPortRole_Object = MibTableColumn
arubaWiredRpvstOldPortRole = _ArubaWiredRpvstOldPortRole_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 9),
    _ArubaWiredRpvstOldPortRole_Type()
)
arubaWiredRpvstOldPortRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredRpvstOldPortRole.setStatus("current")


class _ArubaWiredRpvstNewPortRole_Type(DisplayString):
    """Custom type arubaWiredRpvstNewPortRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredRpvstNewPortRole_Type.__name__ = "DisplayString"
_ArubaWiredRpvstNewPortRole_Object = MibTableColumn
arubaWiredRpvstNewPortRole = _ArubaWiredRpvstNewPortRole_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 10),
    _ArubaWiredRpvstNewPortRole_Type()
)
arubaWiredRpvstNewPortRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredRpvstNewPortRole.setStatus("current")
_ArubaWiredRpvstTopoChangeTime_Type = DateAndTime
_ArubaWiredRpvstTopoChangeTime_Object = MibTableColumn
arubaWiredRpvstTopoChangeTime = _ArubaWiredRpvstTopoChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 11),
    _ArubaWiredRpvstTopoChangeTime_Type()
)
arubaWiredRpvstTopoChangeTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredRpvstTopoChangeTime.setStatus("current")


class _ArubaWiredRpvstPreviousRootBridgeID_Type(DisplayString):
    """Custom type arubaWiredRpvstPreviousRootBridgeID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredRpvstPreviousRootBridgeID_Type.__name__ = "DisplayString"
_ArubaWiredRpvstPreviousRootBridgeID_Object = MibTableColumn
arubaWiredRpvstPreviousRootBridgeID = _ArubaWiredRpvstPreviousRootBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 12),
    _ArubaWiredRpvstPreviousRootBridgeID_Type()
)
arubaWiredRpvstPreviousRootBridgeID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredRpvstPreviousRootBridgeID.setStatus("current")


class _ArubaWiredRpvstNewRootBridgeID_Type(DisplayString):
    """Custom type arubaWiredRpvstNewRootBridgeID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredRpvstNewRootBridgeID_Type.__name__ = "DisplayString"
_ArubaWiredRpvstNewRootBridgeID_Object = MibTableColumn
arubaWiredRpvstNewRootBridgeID = _ArubaWiredRpvstNewRootBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 13),
    _ArubaWiredRpvstNewRootBridgeID_Type()
)
arubaWiredRpvstNewRootBridgeID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredRpvstNewRootBridgeID.setStatus("current")
_ArubaWiredRpvstRootBridgeChangeTimeStamp_Type = DateAndTime
_ArubaWiredRpvstRootBridgeChangeTimeStamp_Object = MibTableColumn
arubaWiredRpvstRootBridgeChangeTimeStamp = _ArubaWiredRpvstRootBridgeChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 14),
    _ArubaWiredRpvstRootBridgeChangeTimeStamp_Type()
)
arubaWiredRpvstRootBridgeChangeTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    arubaWiredRpvstRootBridgeChangeTimeStamp.setStatus("current")


class _ArubaWiredRpvstId_Type(Integer32):
    """Custom type arubaWiredRpvstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_ArubaWiredRpvstId_Type.__name__ = "Integer32"
_ArubaWiredRpvstId_Object = MibTableColumn
arubaWiredRpvstId = _ArubaWiredRpvstId_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 1, 5, 1, 15),
    _ArubaWiredRpvstId_Type()
)
arubaWiredRpvstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredRpvstId.setStatus("current")
_ArubaWiredRpvstConformance_ObjectIdentity = ObjectIdentity
arubaWiredRpvstConformance = _ArubaWiredRpvstConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 2)
)
_ArubaWiredRpvstGroups_ObjectIdentity = ObjectIdentity
arubaWiredRpvstGroups = _ArubaWiredRpvstGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 2, 1)
)
_ArubaWiredRpvstCompliances_ObjectIdentity = ObjectIdentity
arubaWiredRpvstCompliances = _ArubaWiredRpvstCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 2, 2)
)

# Managed Objects groups

arubaWiredRpvstGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 2, 1, 1)
)
arubaWiredRpvstGroup.setObjects(
      *(("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstResetCounters"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstExtendedSystemID"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstIgnorePVIDInconsistency"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstBpduGuardTimeout"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstMstpInterconnectVlan"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstCurrentVportCount"))
)
if mibBuilder.loadTexts:
    arubaWiredRpvstGroup.setStatus("current")

arubaWiredRpvstVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 2, 1, 2)
)
arubaWiredRpvstVlanGroup.setObjects(
      *(("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanHelloTime"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanForwardDelay"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanMaxAge"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanPriority"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanRoot"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanRpvstAdminStatus"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanResetCounters"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanOperHelloTime"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanRootPriority"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanRootPort"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanRootPathCost"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanRootMacAddress"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanRootChangeCounter"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanTimeSinceLastTopoChange"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanTopoChangeCount"))
)
if mibBuilder.loadTexts:
    arubaWiredRpvstVlanGroup.setStatus("current")

arubaWiredRpvstPortVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 2, 1, 3)
)
arubaWiredRpvstPortVlanGroup.setObjects(
      *(("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanPathCost"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanPriority"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanResetCounters"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanRole"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanState"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanDesigBridge"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanOperPointToPoint"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanOperEdge"))
)
if mibBuilder.loadTexts:
    arubaWiredRpvstPortVlanGroup.setStatus("current")

arubaWiredRpvstPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 2, 1, 4)
)
arubaWiredRpvstPortGroup.setObjects(
      *(("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortAdminEdge"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortAdminPointToPoint"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortAutoEdge"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortBpduFiltering"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortRestrictedTcn"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortRootGuard"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortLoopGuard"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortBpduProtection"))
)
if mibBuilder.loadTexts:
    arubaWiredRpvstPortGroup.setStatus("current")

arubaWiredRpvstPvst1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 2, 1, 5)
)
arubaWiredRpvstPvst1.setObjects(
      *(("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPathCostMode"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanSendTopoChangeCtrl"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanLogPortStateTransitions"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanInconsistencyReason"))
)
if mibBuilder.loadTexts:
    arubaWiredRpvstPvst1.setStatus("current")

arubaWiredRpvstNotificationObjectGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 2, 1, 6)
)
arubaWiredRpvstNotificationObjectGrp.setObjects(
      *(("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortName"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanIndex"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanErrantBpduRxCount"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstErrantBpduSrcMac"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstSuperiorBpduSrcPort"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstSuperiorBpduSrcMac"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstErrantBpduDetector"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstDesignatedPort"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstOldPortRole"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstNewPortRole"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstTopoChangeTime"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPreviousRootBridgeID"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstNewRootBridgeID"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstRootBridgeChangeTimeStamp"))
)
if mibBuilder.loadTexts:
    arubaWiredRpvstNotificationObjectGrp.setStatus("current")


# Notification objects

arubaWiredRpvstErrantBpduReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 0, 1)
)
arubaWiredRpvstErrantBpduReceived.setObjects(
      *(("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanIndex"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortName"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanErrantBpduRxCount"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanState"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanDesigBridge"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstDesignatedPort"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstErrantBpduSrcMac"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstErrantBpduDetector"))
)
if mibBuilder.loadTexts:
    arubaWiredRpvstErrantBpduReceived.setStatus(
        "current"
    )

arubaWiredRpvstNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 0, 2)
)
arubaWiredRpvstNewRoot.setObjects(
      *(("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanIndex"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstNewRootBridgeID"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPreviousRootBridgeID"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstRootBridgeChangeTimeStamp"))
)
if mibBuilder.loadTexts:
    arubaWiredRpvstNewRoot.setStatus(
        "current"
    )

arubaWiredRpvstRootGuardInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 0, 3)
)
arubaWiredRpvstRootGuardInconsistency.setObjects(
      *(("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanIndex"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortName"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstSuperiorBpduSrcMac"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstSuperiorBpduSrcPort"))
)
if mibBuilder.loadTexts:
    arubaWiredRpvstRootGuardInconsistency.setStatus(
        "current"
    )

arubaWiredRpvstLoopGuardInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 0, 4)
)
arubaWiredRpvstLoopGuardInconsistency.setObjects(
      *(("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanIndex"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortName"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanDesigBridge"))
)
if mibBuilder.loadTexts:
    arubaWiredRpvstLoopGuardInconsistency.setStatus(
        "current"
    )

arubaWiredRpvstTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 0, 5)
)
arubaWiredRpvstTopologyChange.setObjects(
      *(("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanIndex"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortName"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstOldPortRole"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstNewPortRole"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstTopoChangeTime"))
)
if mibBuilder.loadTexts:
    arubaWiredRpvstTopologyChange.setStatus(
        "current"
    )


# Notifications groups

arubaWiredRpvstNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 2, 1, 7)
)
arubaWiredRpvstNotificationGroup.setObjects(
      *(("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstErrantBpduReceived"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstNewRoot"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstRootGuardInconsistency"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstLoopGuardInconsistency"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstTopologyChange"))
)
if mibBuilder.loadTexts:
    arubaWiredRpvstNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

arubaWiredRpvstCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 2, 2, 1)
)
arubaWiredRpvstCompliance1.setObjects(
      *(("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstGroup"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstVlanGroup"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortVlanGroup"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPortGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredRpvstCompliance1.setStatus(
        "current"
    )

arubaWiredRpvstCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 2, 2, 2)
)
arubaWiredRpvstCompliance2.setObjects(
    ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstPvst1")
)
if mibBuilder.loadTexts:
    arubaWiredRpvstCompliance2.setStatus(
        "current"
    )

arubaWiredRpvstNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5, 2, 2, 3)
)
arubaWiredRpvstNotificationCompliance.setObjects(
      *(("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstNotificationObjectGrp"),
        ("ARUBAWIRED-RPVST-MIB", "arubaWiredRpvstNotificationGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredRpvstNotificationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-RPVST-MIB",
    **{"PointToPoint": PointToPoint,
       "arubaWiredRpvstMIB": arubaWiredRpvstMIB,
       "arubaWiredRpvstNotifications": arubaWiredRpvstNotifications,
       "arubaWiredRpvstErrantBpduReceived": arubaWiredRpvstErrantBpduReceived,
       "arubaWiredRpvstNewRoot": arubaWiredRpvstNewRoot,
       "arubaWiredRpvstRootGuardInconsistency": arubaWiredRpvstRootGuardInconsistency,
       "arubaWiredRpvstLoopGuardInconsistency": arubaWiredRpvstLoopGuardInconsistency,
       "arubaWiredRpvstTopologyChange": arubaWiredRpvstTopologyChange,
       "arubaWiredRpvstObjects": arubaWiredRpvstObjects,
       "arubaWiredRpvstGeneralGroup": arubaWiredRpvstGeneralGroup,
       "arubaWiredRpvstResetCounters": arubaWiredRpvstResetCounters,
       "arubaWiredRpvstExtendedSystemID": arubaWiredRpvstExtendedSystemID,
       "arubaWiredRpvstIgnorePVIDInconsistency": arubaWiredRpvstIgnorePVIDInconsistency,
       "arubaWiredRpvstPathCostMode": arubaWiredRpvstPathCostMode,
       "arubaWiredRpvstBpduGuardTimeout": arubaWiredRpvstBpduGuardTimeout,
       "arubaWiredRpvstMstpInterconnectVlan": arubaWiredRpvstMstpInterconnectVlan,
       "arubaWiredRpvstCurrentVportCount": arubaWiredRpvstCurrentVportCount,
       "arubaWiredRpvstVlanTable": arubaWiredRpvstVlanTable,
       "arubaWiredRpvstVlanEntry": arubaWiredRpvstVlanEntry,
       "arubaWiredRpvstVlanId": arubaWiredRpvstVlanId,
       "arubaWiredRpvstVlanHelloTime": arubaWiredRpvstVlanHelloTime,
       "arubaWiredRpvstVlanForwardDelay": arubaWiredRpvstVlanForwardDelay,
       "arubaWiredRpvstVlanMaxAge": arubaWiredRpvstVlanMaxAge,
       "arubaWiredRpvstVlanPriority": arubaWiredRpvstVlanPriority,
       "arubaWiredRpvstVlanRoot": arubaWiredRpvstVlanRoot,
       "arubaWiredRpvstVlanRpvstAdminStatus": arubaWiredRpvstVlanRpvstAdminStatus,
       "arubaWiredRpvstVlanResetCounters": arubaWiredRpvstVlanResetCounters,
       "arubaWiredRpvstVlanOperHelloTime": arubaWiredRpvstVlanOperHelloTime,
       "arubaWiredRpvstVlanRootPriority": arubaWiredRpvstVlanRootPriority,
       "arubaWiredRpvstVlanRootPort": arubaWiredRpvstVlanRootPort,
       "arubaWiredRpvstVlanRootPathCost": arubaWiredRpvstVlanRootPathCost,
       "arubaWiredRpvstVlanRootMacAddress": arubaWiredRpvstVlanRootMacAddress,
       "arubaWiredRpvstVlanRootChangeCounter": arubaWiredRpvstVlanRootChangeCounter,
       "arubaWiredRpvstVlanTimeSinceLastTopoChange": arubaWiredRpvstVlanTimeSinceLastTopoChange,
       "arubaWiredRpvstVlanTopoChangeCount": arubaWiredRpvstVlanTopoChangeCount,
       "arubaWiredRpvstVlanSendTopoChangeCtrl": arubaWiredRpvstVlanSendTopoChangeCtrl,
       "arubaWiredRpvstVlanLogPortStateTransitions": arubaWiredRpvstVlanLogPortStateTransitions,
       "arubaWiredRpvstPortTable": arubaWiredRpvstPortTable,
       "arubaWiredRpvstPortEntry": arubaWiredRpvstPortEntry,
       "arubaWiredRpvstPortIndex": arubaWiredRpvstPortIndex,
       "arubaWiredRpvstPortAdminEdge": arubaWiredRpvstPortAdminEdge,
       "arubaWiredRpvstPortAdminPointToPoint": arubaWiredRpvstPortAdminPointToPoint,
       "arubaWiredRpvstPortAutoEdge": arubaWiredRpvstPortAutoEdge,
       "arubaWiredRpvstPortBpduFiltering": arubaWiredRpvstPortBpduFiltering,
       "arubaWiredRpvstPortRestrictedTcn": arubaWiredRpvstPortRestrictedTcn,
       "arubaWiredRpvstPortRootGuard": arubaWiredRpvstPortRootGuard,
       "arubaWiredRpvstPortLoopGuard": arubaWiredRpvstPortLoopGuard,
       "arubaWiredRpvstPortBpduProtection": arubaWiredRpvstPortBpduProtection,
       "arubaWiredRpvstPortVlanTable": arubaWiredRpvstPortVlanTable,
       "arubaWiredRpvstPortVlanEntry": arubaWiredRpvstPortVlanEntry,
       "arubaWiredRpvstPortVlanId": arubaWiredRpvstPortVlanId,
       "arubaWiredRpvstPortVlanIndex": arubaWiredRpvstPortVlanIndex,
       "arubaWiredRpvstPortVlanPathCost": arubaWiredRpvstPortVlanPathCost,
       "arubaWiredRpvstPortVlanPriority": arubaWiredRpvstPortVlanPriority,
       "arubaWiredRpvstPortVlanResetCounters": arubaWiredRpvstPortVlanResetCounters,
       "arubaWiredRpvstPortVlanRole": arubaWiredRpvstPortVlanRole,
       "arubaWiredRpvstPortVlanState": arubaWiredRpvstPortVlanState,
       "arubaWiredRpvstPortVlanDesigBridge": arubaWiredRpvstPortVlanDesigBridge,
       "arubaWiredRpvstPortVlanOperPointToPoint": arubaWiredRpvstPortVlanOperPointToPoint,
       "arubaWiredRpvstPortVlanOperEdge": arubaWiredRpvstPortVlanOperEdge,
       "arubaWiredRpvstPortVlanInconsistencyReason": arubaWiredRpvstPortVlanInconsistencyReason,
       "arubaWiredRpvstNotificationTable": arubaWiredRpvstNotificationTable,
       "arubaWiredRpvstNotificationEntry": arubaWiredRpvstNotificationEntry,
       "arubaWiredRpvstPortName": arubaWiredRpvstPortName,
       "arubaWiredRpvstVlanIndex": arubaWiredRpvstVlanIndex,
       "arubaWiredRpvstPortVlanErrantBpduRxCount": arubaWiredRpvstPortVlanErrantBpduRxCount,
       "arubaWiredRpvstErrantBpduSrcMac": arubaWiredRpvstErrantBpduSrcMac,
       "arubaWiredRpvstSuperiorBpduSrcPort": arubaWiredRpvstSuperiorBpduSrcPort,
       "arubaWiredRpvstSuperiorBpduSrcMac": arubaWiredRpvstSuperiorBpduSrcMac,
       "arubaWiredRpvstErrantBpduDetector": arubaWiredRpvstErrantBpduDetector,
       "arubaWiredRpvstDesignatedPort": arubaWiredRpvstDesignatedPort,
       "arubaWiredRpvstOldPortRole": arubaWiredRpvstOldPortRole,
       "arubaWiredRpvstNewPortRole": arubaWiredRpvstNewPortRole,
       "arubaWiredRpvstTopoChangeTime": arubaWiredRpvstTopoChangeTime,
       "arubaWiredRpvstPreviousRootBridgeID": arubaWiredRpvstPreviousRootBridgeID,
       "arubaWiredRpvstNewRootBridgeID": arubaWiredRpvstNewRootBridgeID,
       "arubaWiredRpvstRootBridgeChangeTimeStamp": arubaWiredRpvstRootBridgeChangeTimeStamp,
       "arubaWiredRpvstId": arubaWiredRpvstId,
       "arubaWiredRpvstConformance": arubaWiredRpvstConformance,
       "arubaWiredRpvstGroups": arubaWiredRpvstGroups,
       "arubaWiredRpvstGroup": arubaWiredRpvstGroup,
       "arubaWiredRpvstVlanGroup": arubaWiredRpvstVlanGroup,
       "arubaWiredRpvstPortVlanGroup": arubaWiredRpvstPortVlanGroup,
       "arubaWiredRpvstPortGroup": arubaWiredRpvstPortGroup,
       "arubaWiredRpvstPvst1": arubaWiredRpvstPvst1,
       "arubaWiredRpvstNotificationObjectGrp": arubaWiredRpvstNotificationObjectGrp,
       "arubaWiredRpvstNotificationGroup": arubaWiredRpvstNotificationGroup,
       "arubaWiredRpvstCompliances": arubaWiredRpvstCompliances,
       "arubaWiredRpvstCompliance1": arubaWiredRpvstCompliance1,
       "arubaWiredRpvstCompliance2": arubaWiredRpvstCompliance2,
       "arubaWiredRpvstNotificationCompliance": arubaWiredRpvstNotificationCompliance}
)
