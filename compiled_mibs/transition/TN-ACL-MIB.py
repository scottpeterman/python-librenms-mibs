# SNMP MIB module (TN-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-ACL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:42 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(PortList,
 VlanIdOrAny,
 VlanIdOrAnyOrNone,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIdOrAny",
    "VlanIdOrAnyOrNone",
    "VlanIdOrNone")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(tnDevMgmt,) = mibBuilder.importSymbols(
    "TN-MGMT-MIB",
    "tnDevMgmt")


# MODULE-IDENTITY

tnAclMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tnAclMgmt.setRevisions(
        ("2013-05-16 00:00",
         "2014-05-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RateLimiterValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16),
    )



class TruthValueOrAny(TextualConvention, Integer32):
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
        *(("any", 1),
          ("val0", 2),
          ("val1", 3))
    )



class HostOrNetworkOrAny(TextualConvention, Integer32):
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
        *(("any", 1),
          ("host", 2),
          ("network", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TnAclPortTable_Object = MibTable
tnAclPortTable = _TnAclPortTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tnAclPortTable.setStatus("current")
_TnAclPortEntry_Object = MibTableRow
tnAclPortEntry = _TnAclPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 1, 1)
)
tnAclPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnAclPortEntry.setStatus("current")


class _TnAclPortPolicyId_Type(Integer32):
    """Custom type tnAclPortPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnAclPortPolicyId_Type.__name__ = "Integer32"
_TnAclPortPolicyId_Object = MibTableColumn
tnAclPortPolicyId = _TnAclPortPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 1, 1, 1),
    _TnAclPortPolicyId_Type()
)
tnAclPortPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAclPortPolicyId.setStatus("current")


class _TnAclPortAction_Type(Integer32):
    """Custom type tnAclPortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_TnAclPortAction_Type.__name__ = "Integer32"
_TnAclPortAction_Object = MibTableColumn
tnAclPortAction = _TnAclPortAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 1, 1, 2),
    _TnAclPortAction_Type()
)
tnAclPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAclPortAction.setStatus("current")
_TnAclPortRateLimiterId_Type = RateLimiterValue
_TnAclPortRateLimiterId_Object = MibTableColumn
tnAclPortRateLimiterId = _TnAclPortRateLimiterId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 1, 1, 3),
    _TnAclPortRateLimiterId_Type()
)
tnAclPortRateLimiterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAclPortRateLimiterId.setStatus("current")


class _TnAclPortEvcPolicerState_Type(Integer32):
    """Custom type tnAclPortEvcPolicerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnAclPortEvcPolicerState_Type.__name__ = "Integer32"
_TnAclPortEvcPolicerState_Object = MibTableColumn
tnAclPortEvcPolicerState = _TnAclPortEvcPolicerState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 1, 1, 4),
    _TnAclPortEvcPolicerState_Type()
)
tnAclPortEvcPolicerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAclPortEvcPolicerState.setStatus("current")


class _TnAclPortEvcPolicerId_Type(Integer32):
    """Custom type tnAclPortEvcPolicerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnAclPortEvcPolicerId_Type.__name__ = "Integer32"
_TnAclPortEvcPolicerId_Object = MibTableColumn
tnAclPortEvcPolicerId = _TnAclPortEvcPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 1, 1, 5),
    _TnAclPortEvcPolicerId_Type()
)
tnAclPortEvcPolicerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAclPortEvcPolicerId.setStatus("current")
_TnAclPortRedirect_Type = PortList
_TnAclPortRedirect_Object = MibTableColumn
tnAclPortRedirect = _TnAclPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 1, 1, 6),
    _TnAclPortRedirect_Type()
)
tnAclPortRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAclPortRedirect.setStatus("current")


class _TnAclPortMirrorState_Type(Integer32):
    """Custom type tnAclPortMirrorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnAclPortMirrorState_Type.__name__ = "Integer32"
_TnAclPortMirrorState_Object = MibTableColumn
tnAclPortMirrorState = _TnAclPortMirrorState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 1, 1, 7),
    _TnAclPortMirrorState_Type()
)
tnAclPortMirrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAclPortMirrorState.setStatus("current")


class _TnAclPortLoggingState_Type(Integer32):
    """Custom type tnAclPortLoggingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnAclPortLoggingState_Type.__name__ = "Integer32"
_TnAclPortLoggingState_Object = MibTableColumn
tnAclPortLoggingState = _TnAclPortLoggingState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 1, 1, 8),
    _TnAclPortLoggingState_Type()
)
tnAclPortLoggingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAclPortLoggingState.setStatus("current")


class _TnAclPortShutdownState_Type(Integer32):
    """Custom type tnAclPortShutdownState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnAclPortShutdownState_Type.__name__ = "Integer32"
_TnAclPortShutdownState_Object = MibTableColumn
tnAclPortShutdownState = _TnAclPortShutdownState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 1, 1, 9),
    _TnAclPortShutdownState_Type()
)
tnAclPortShutdownState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAclPortShutdownState.setStatus("current")


class _TnAclPortAclState_Type(Integer32):
    """Custom type tnAclPortAclState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnAclPortAclState_Type.__name__ = "Integer32"
_TnAclPortAclState_Object = MibTableColumn
tnAclPortAclState = _TnAclPortAclState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 1, 1, 10),
    _TnAclPortAclState_Type()
)
tnAclPortAclState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAclPortAclState.setStatus("current")
_TnAclPortCounter_Type = Counter32
_TnAclPortCounter_Object = MibTableColumn
tnAclPortCounter = _TnAclPortCounter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 1, 1, 11),
    _TnAclPortCounter_Type()
)
tnAclPortCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAclPortCounter.setStatus("current")
_TnAclRateLimiterTable_Object = MibTable
tnAclRateLimiterTable = _TnAclRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tnAclRateLimiterTable.setStatus("current")
_TnAclRateLimiterEntry_Object = MibTableRow
tnAclRateLimiterEntry = _TnAclRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 2, 1)
)
tnAclRateLimiterEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-ACL-MIB", "tnAclRateLimitId"),
)
if mibBuilder.loadTexts:
    tnAclRateLimiterEntry.setStatus("current")


class _TnAclRateLimitId_Type(Integer32):
    """Custom type tnAclRateLimitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TnAclRateLimitId_Type.__name__ = "Integer32"
_TnAclRateLimitId_Object = MibTableColumn
tnAclRateLimitId = _TnAclRateLimitId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 2, 1, 1),
    _TnAclRateLimitId_Type()
)
tnAclRateLimitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAclRateLimitId.setStatus("current")
_TnAclRateLimitRate_Type = Integer32
_TnAclRateLimitRate_Object = MibTableColumn
tnAclRateLimitRate = _TnAclRateLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 2, 1, 2),
    _TnAclRateLimitRate_Type()
)
tnAclRateLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAclRateLimitRate.setStatus("current")


class _TnAclRateLimitUnit_Type(Integer32):
    """Custom type tnAclRateLimitUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pps", 1),
          ("kbps", 2))
    )


_TnAclRateLimitUnit_Type.__name__ = "Integer32"
_TnAclRateLimitUnit_Object = MibTableColumn
tnAclRateLimitUnit = _TnAclRateLimitUnit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 2, 1, 3),
    _TnAclRateLimitUnit_Type()
)
tnAclRateLimitUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAclRateLimitUnit.setStatus("current")
_TnAclOperTable_Object = MibTable
tnAclOperTable = _TnAclOperTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    tnAclOperTable.setStatus("current")
_TnAclOperEntry_Object = MibTableRow
tnAclOperEntry = _TnAclOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 3, 1)
)
tnAclOperEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnAclOperEntry.setStatus("current")


class _TnAclClearCounter_Type(Integer32):
    """Custom type tnAclClearCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nooper", 1),
          ("clear", 2))
    )


_TnAclClearCounter_Type.__name__ = "Integer32"
_TnAclClearCounter_Object = MibTableColumn
tnAclClearCounter = _TnAclClearCounter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 3, 1, 1),
    _TnAclClearCounter_Type()
)
tnAclClearCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAclClearCounter.setStatus("current")
_TnAceTable_Object = MibTable
tnAceTable = _TnAceTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    tnAceTable.setStatus("current")
_TnAceEntry_Object = MibTableRow
tnAceEntry = _TnAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1)
)
tnAceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-ACL-MIB", "tnAceIndex"),
)
if mibBuilder.loadTexts:
    tnAceEntry.setStatus("current")


class _TnAceIndex_Type(Integer32):
    """Custom type tnAceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TnAceIndex_Type.__name__ = "Integer32"
_TnAceIndex_Object = MibTableColumn
tnAceIndex = _TnAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 1),
    _TnAceIndex_Type()
)
tnAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAceIndex.setStatus("current")


class _TnAceNextIndex_Type(Integer32):
    """Custom type tnAceNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TnAceNextIndex_Type.__name__ = "Integer32"
_TnAceNextIndex_Object = MibTableColumn
tnAceNextIndex = _TnAceNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 2),
    _TnAceNextIndex_Type()
)
tnAceNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceNextIndex.setStatus("current")
_TnAceIngressPort_Type = PortList
_TnAceIngressPort_Object = MibTableColumn
tnAceIngressPort = _TnAceIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 3),
    _TnAceIngressPort_Type()
)
tnAceIngressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceIngressPort.setStatus("current")


class _TnAcePolicyFilterType_Type(Integer32):
    """Custom type tnAcePolicyFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnAcePolicyFilterType_Type.__name__ = "Integer32"
_TnAcePolicyFilterType_Object = MibTableColumn
tnAcePolicyFilterType = _TnAcePolicyFilterType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 4),
    _TnAcePolicyFilterType_Type()
)
tnAcePolicyFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAcePolicyFilterType.setStatus("current")


class _TnAcePolicyValue_Type(Integer32):
    """Custom type tnAcePolicyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnAcePolicyValue_Type.__name__ = "Integer32"
_TnAcePolicyValue_Object = MibTableColumn
tnAcePolicyValue = _TnAcePolicyValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 5),
    _TnAcePolicyValue_Type()
)
tnAcePolicyValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAcePolicyValue.setStatus("current")


class _TnAcePolicyBitMask_Type(Integer32):
    """Custom type tnAcePolicyBitMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnAcePolicyBitMask_Type.__name__ = "Integer32"
_TnAcePolicyBitMask_Object = MibTableColumn
tnAcePolicyBitMask = _TnAcePolicyBitMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 6),
    _TnAcePolicyBitMask_Type()
)
tnAcePolicyBitMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAcePolicyBitMask.setStatus("current")


class _TnAcePolicyFrameType_Type(Integer32):
    """Custom type tnAcePolicyFrameType based on Integer32"""
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
        *(("any", 1),
          ("etherType", 2),
          ("arp", 3),
          ("ipv4", 4))
    )


_TnAcePolicyFrameType_Type.__name__ = "Integer32"
_TnAcePolicyFrameType_Object = MibTableColumn
tnAcePolicyFrameType = _TnAcePolicyFrameType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 7),
    _TnAcePolicyFrameType_Type()
)
tnAcePolicyFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAcePolicyFrameType.setStatus("current")


class _TnAceAction_Type(Integer32):
    """Custom type tnAceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_TnAceAction_Type.__name__ = "Integer32"
_TnAceAction_Object = MibTableColumn
tnAceAction = _TnAceAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 8),
    _TnAceAction_Type()
)
tnAceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceAction.setStatus("current")
_TnAceRateLimiter_Type = RateLimiterValue
_TnAceRateLimiter_Object = MibTableColumn
tnAceRateLimiter = _TnAceRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 9),
    _TnAceRateLimiter_Type()
)
tnAceRateLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceRateLimiter.setStatus("current")


class _TnAceEvcPolicerState_Type(Integer32):
    """Custom type tnAceEvcPolicerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnAceEvcPolicerState_Type.__name__ = "Integer32"
_TnAceEvcPolicerState_Object = MibTableColumn
tnAceEvcPolicerState = _TnAceEvcPolicerState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 10),
    _TnAceEvcPolicerState_Type()
)
tnAceEvcPolicerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceEvcPolicerState.setStatus("current")


class _TnAceEvcPolicerId_Type(Integer32):
    """Custom type tnAceEvcPolicerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnAceEvcPolicerId_Type.__name__ = "Integer32"
_TnAceEvcPolicerId_Object = MibTableColumn
tnAceEvcPolicerId = _TnAceEvcPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 11),
    _TnAceEvcPolicerId_Type()
)
tnAceEvcPolicerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceEvcPolicerId.setStatus("current")
_TnAcePortRedirect_Type = PortList
_TnAcePortRedirect_Object = MibTableColumn
tnAcePortRedirect = _TnAcePortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 12),
    _TnAcePortRedirect_Type()
)
tnAcePortRedirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAcePortRedirect.setStatus("current")


class _TnAceMirrorState_Type(Integer32):
    """Custom type tnAceMirrorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnAceMirrorState_Type.__name__ = "Integer32"
_TnAceMirrorState_Object = MibTableColumn
tnAceMirrorState = _TnAceMirrorState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 13),
    _TnAceMirrorState_Type()
)
tnAceMirrorState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceMirrorState.setStatus("current")


class _TnAceLoggingState_Type(Integer32):
    """Custom type tnAceLoggingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnAceLoggingState_Type.__name__ = "Integer32"
_TnAceLoggingState_Object = MibTableColumn
tnAceLoggingState = _TnAceLoggingState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 14),
    _TnAceLoggingState_Type()
)
tnAceLoggingState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceLoggingState.setStatus("current")


class _TnAceShutdownState_Type(Integer32):
    """Custom type tnAceShutdownState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnAceShutdownState_Type.__name__ = "Integer32"
_TnAceShutdownState_Object = MibTableColumn
tnAceShutdownState = _TnAceShutdownState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 15),
    _TnAceShutdownState_Type()
)
tnAceShutdownState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceShutdownState.setStatus("current")
_TnAceCounter_Type = Counter32
_TnAceCounter_Object = MibTableColumn
tnAceCounter = _TnAceCounter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 16),
    _TnAceCounter_Type()
)
tnAceCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAceCounter.setStatus("current")


class _TnAceVlan8021qTagged_Type(Integer32):
    """Custom type tnAceVlan8021qTagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_TnAceVlan8021qTagged_Type.__name__ = "Integer32"
_TnAceVlan8021qTagged_Object = MibTableColumn
tnAceVlan8021qTagged = _TnAceVlan8021qTagged_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 17),
    _TnAceVlan8021qTagged_Type()
)
tnAceVlan8021qTagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceVlan8021qTagged.setStatus("current")


class _TnAceVlanIdFilter_Type(Integer32):
    """Custom type tnAceVlanIdFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnAceVlanIdFilter_Type.__name__ = "Integer32"
_TnAceVlanIdFilter_Object = MibTableColumn
tnAceVlanIdFilter = _TnAceVlanIdFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 18),
    _TnAceVlanIdFilter_Type()
)
tnAceVlanIdFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceVlanIdFilter.setStatus("current")


class _TnAceVlanId_Type(Integer32):
    """Custom type tnAceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TnAceVlanId_Type.__name__ = "Integer32"
_TnAceVlanId_Object = MibTableColumn
tnAceVlanId = _TnAceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 19),
    _TnAceVlanId_Type()
)
tnAceVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceVlanId.setStatus("current")


class _TnAceTagPriority_Type(Integer32):
    """Custom type tnAceTagPriority based on Integer32"""
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
        *(("tp0", 1),
          ("tp1", 2),
          ("tp2", 3),
          ("tp3", 4),
          ("tp4", 5),
          ("tp5", 6),
          ("tp6", 7),
          ("tp7", 8),
          ("any", 9))
    )


_TnAceTagPriority_Type.__name__ = "Integer32"
_TnAceTagPriority_Object = MibTableColumn
tnAceTagPriority = _TnAceTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 20),
    _TnAceTagPriority_Type()
)
tnAceTagPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceTagPriority.setStatus("current")
_TnAceRowStatus_Type = RowStatus
_TnAceRowStatus_Object = MibTableColumn
tnAceRowStatus = _TnAceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 21),
    _TnAceRowStatus_Type()
)
tnAceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceRowStatus.setStatus("current")
_TnAceLookup_Type = TruthValue
_TnAceLookup_Object = MibTableColumn
tnAceLookup = _TnAceLookup_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 4, 1, 22),
    _TnAceLookup_Type()
)
tnAceLookup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceLookup.setStatus("current")
_TnAceEtherTable_Object = MibTable
tnAceEtherTable = _TnAceEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 5)
)
if mibBuilder.loadTexts:
    tnAceEtherTable.setStatus("current")
_TnAceEtherEntry_Object = MibTableRow
tnAceEtherEntry = _TnAceEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 5, 1)
)
tnAceEtherEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-ACL-MIB", "tnAceIndex"),
)
if mibBuilder.loadTexts:
    tnAceEtherEntry.setStatus("current")


class _TnAceEtherSmacFilter_Type(Integer32):
    """Custom type tnAceEtherSmacFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnAceEtherSmacFilter_Type.__name__ = "Integer32"
_TnAceEtherSmacFilter_Object = MibTableColumn
tnAceEtherSmacFilter = _TnAceEtherSmacFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 5, 1, 1),
    _TnAceEtherSmacFilter_Type()
)
tnAceEtherSmacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceEtherSmacFilter.setStatus("current")
_TnAceEtherSmacVal_Type = MacAddress
_TnAceEtherSmacVal_Object = MibTableColumn
tnAceEtherSmacVal = _TnAceEtherSmacVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 5, 1, 2),
    _TnAceEtherSmacVal_Type()
)
tnAceEtherSmacVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceEtherSmacVal.setStatus("current")


class _TnAceEtherDmacFilter_Type(Integer32):
    """Custom type tnAceEtherDmacFilter based on Integer32"""
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
        *(("any", 1),
          ("unicast", 2),
          ("multicast", 3),
          ("broadcast", 4),
          ("specific", 5))
    )


_TnAceEtherDmacFilter_Type.__name__ = "Integer32"
_TnAceEtherDmacFilter_Object = MibTableColumn
tnAceEtherDmacFilter = _TnAceEtherDmacFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 5, 1, 3),
    _TnAceEtherDmacFilter_Type()
)
tnAceEtherDmacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceEtherDmacFilter.setStatus("current")
_TnAceEtherDmacVal_Type = MacAddress
_TnAceEtherDmacVal_Object = MibTableColumn
tnAceEtherDmacVal = _TnAceEtherDmacVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 5, 1, 4),
    _TnAceEtherDmacVal_Type()
)
tnAceEtherDmacVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceEtherDmacVal.setStatus("current")


class _TnAceEtherTypeFilter_Type(Integer32):
    """Custom type tnAceEtherTypeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnAceEtherTypeFilter_Type.__name__ = "Integer32"
_TnAceEtherTypeFilter_Object = MibTableColumn
tnAceEtherTypeFilter = _TnAceEtherTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 5, 1, 5),
    _TnAceEtherTypeFilter_Type()
)
tnAceEtherTypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceEtherTypeFilter.setStatus("current")


class _TnAceEtherTypeVal_Type(Integer32):
    """Custom type tnAceEtherTypeVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TnAceEtherTypeVal_Type.__name__ = "Integer32"
_TnAceEtherTypeVal_Object = MibTableColumn
tnAceEtherTypeVal = _TnAceEtherTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 5, 1, 6),
    _TnAceEtherTypeVal_Type()
)
tnAceEtherTypeVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAceEtherTypeVal.setStatus("current")
_TnAceArpTable_Object = MibTable
tnAceArpTable = _TnAceArpTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6)
)
if mibBuilder.loadTexts:
    tnAceArpTable.setStatus("current")
_TnAceArpEntry_Object = MibTableRow
tnAceArpEntry = _TnAceArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1)
)
tnAceArpEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-ACL-MIB", "tnAceIndex"),
)
if mibBuilder.loadTexts:
    tnAceArpEntry.setStatus("current")


class _TnAceArpSmacFilter_Type(Integer32):
    """Custom type tnAceArpSmacFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnAceArpSmacFilter_Type.__name__ = "Integer32"
_TnAceArpSmacFilter_Object = MibTableColumn
tnAceArpSmacFilter = _TnAceArpSmacFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 1),
    _TnAceArpSmacFilter_Type()
)
tnAceArpSmacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpSmacFilter.setStatus("current")
_TnAceArpSmacVal_Type = MacAddress
_TnAceArpSmacVal_Object = MibTableColumn
tnAceArpSmacVal = _TnAceArpSmacVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 2),
    _TnAceArpSmacVal_Type()
)
tnAceArpSmacVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpSmacVal.setStatus("current")


class _TnAceArpDmacFilter_Type(Integer32):
    """Custom type tnAceArpDmacFilter based on Integer32"""
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
        *(("any", 1),
          ("unicast", 2),
          ("multicast", 3),
          ("broadcast", 4))
    )


_TnAceArpDmacFilter_Type.__name__ = "Integer32"
_TnAceArpDmacFilter_Object = MibTableColumn
tnAceArpDmacFilter = _TnAceArpDmacFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 3),
    _TnAceArpDmacFilter_Type()
)
tnAceArpDmacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpDmacFilter.setStatus("current")


class _TnAceArpParmArpRarp_Type(Integer32):
    """Custom type tnAceArpParmArpRarp based on Integer32"""
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
        *(("any", 1),
          ("arp", 2),
          ("rarp", 3),
          ("other", 4))
    )


_TnAceArpParmArpRarp_Type.__name__ = "Integer32"
_TnAceArpParmArpRarp_Object = MibTableColumn
tnAceArpParmArpRarp = _TnAceArpParmArpRarp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 4),
    _TnAceArpParmArpRarp_Type()
)
tnAceArpParmArpRarp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpParmArpRarp.setStatus("current")


class _TnAceArpParmRequestReply_Type(Integer32):
    """Custom type tnAceArpParmRequestReply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("request", 2),
          ("reply", 3))
    )


_TnAceArpParmRequestReply_Type.__name__ = "Integer32"
_TnAceArpParmRequestReply_Object = MibTableColumn
tnAceArpParmRequestReply = _TnAceArpParmRequestReply_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 5),
    _TnAceArpParmRequestReply_Type()
)
tnAceArpParmRequestReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpParmRequestReply.setStatus("current")
_TnAceArpParmSenderIpFilter_Type = HostOrNetworkOrAny
_TnAceArpParmSenderIpFilter_Object = MibTableColumn
tnAceArpParmSenderIpFilter = _TnAceArpParmSenderIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 6),
    _TnAceArpParmSenderIpFilter_Type()
)
tnAceArpParmSenderIpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpParmSenderIpFilter.setStatus("current")
_TnAceArpParmSenderIpAddress_Type = InetAddress
_TnAceArpParmSenderIpAddress_Object = MibTableColumn
tnAceArpParmSenderIpAddress = _TnAceArpParmSenderIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 7),
    _TnAceArpParmSenderIpAddress_Type()
)
tnAceArpParmSenderIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpParmSenderIpAddress.setStatus("current")
_TnAceArpParmSenderIpMask_Type = InetAddress
_TnAceArpParmSenderIpMask_Object = MibTableColumn
tnAceArpParmSenderIpMask = _TnAceArpParmSenderIpMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 8),
    _TnAceArpParmSenderIpMask_Type()
)
tnAceArpParmSenderIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpParmSenderIpMask.setStatus("current")
_TnAceArpParmTargetIpFilter_Type = HostOrNetworkOrAny
_TnAceArpParmTargetIpFilter_Object = MibTableColumn
tnAceArpParmTargetIpFilter = _TnAceArpParmTargetIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 9),
    _TnAceArpParmTargetIpFilter_Type()
)
tnAceArpParmTargetIpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpParmTargetIpFilter.setStatus("current")
_TnAceArpParmTargetIpAddress_Type = InetAddress
_TnAceArpParmTargetIpAddress_Object = MibTableColumn
tnAceArpParmTargetIpAddress = _TnAceArpParmTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 10),
    _TnAceArpParmTargetIpAddress_Type()
)
tnAceArpParmTargetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpParmTargetIpAddress.setStatus("current")
_TnAceArpParmTargetIpMask_Type = InetAddress
_TnAceArpParmTargetIpMask_Object = MibTableColumn
tnAceArpParmTargetIpMask = _TnAceArpParmTargetIpMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 11),
    _TnAceArpParmTargetIpMask_Type()
)
tnAceArpParmTargetIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpParmTargetIpMask.setStatus("current")
_TnAceArpSenderMacMatch_Type = TruthValueOrAny
_TnAceArpSenderMacMatch_Object = MibTableColumn
tnAceArpSenderMacMatch = _TnAceArpSenderMacMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 12),
    _TnAceArpSenderMacMatch_Type()
)
tnAceArpSenderMacMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpSenderMacMatch.setStatus("current")
_TnAceArpRarpTargetMacMatch_Type = TruthValueOrAny
_TnAceArpRarpTargetMacMatch_Object = MibTableColumn
tnAceArpRarpTargetMacMatch = _TnAceArpRarpTargetMacMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 13),
    _TnAceArpRarpTargetMacMatch_Type()
)
tnAceArpRarpTargetMacMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpRarpTargetMacMatch.setStatus("current")
_TnAceArpIpEthernetLength_Type = TruthValueOrAny
_TnAceArpIpEthernetLength_Object = MibTableColumn
tnAceArpIpEthernetLength = _TnAceArpIpEthernetLength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 14),
    _TnAceArpIpEthernetLength_Type()
)
tnAceArpIpEthernetLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpIpEthernetLength.setStatus("current")
_TnAceArpIp_Type = TruthValueOrAny
_TnAceArpIp_Object = MibTableColumn
tnAceArpIp = _TnAceArpIp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 15),
    _TnAceArpIp_Type()
)
tnAceArpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpIp.setStatus("current")
_TnAceArpEthernet_Type = TruthValueOrAny
_TnAceArpEthernet_Object = MibTableColumn
tnAceArpEthernet = _TnAceArpEthernet_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 6, 1, 16),
    _TnAceArpEthernet_Type()
)
tnAceArpEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceArpEthernet.setStatus("current")
_TnAceIpv4Table_Object = MibTable
tnAceIpv4Table = _TnAceIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7)
)
if mibBuilder.loadTexts:
    tnAceIpv4Table.setStatus("current")
_TnAceIpv4Entry_Object = MibTableRow
tnAceIpv4Entry = _TnAceIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1)
)
tnAceIpv4Entry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-ACL-MIB", "tnAceIndex"),
)
if mibBuilder.loadTexts:
    tnAceIpv4Entry.setStatus("current")


class _TnAceIpv4ProtoFilter_Type(Integer32):
    """Custom type tnAceIpv4ProtoFilter based on Integer32"""
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
        *(("any", 1),
          ("other", 2),
          ("icmp", 3),
          ("udp", 4),
          ("tcp", 5))
    )


_TnAceIpv4ProtoFilter_Type.__name__ = "Integer32"
_TnAceIpv4ProtoFilter_Object = MibTableColumn
tnAceIpv4ProtoFilter = _TnAceIpv4ProtoFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 1),
    _TnAceIpv4ProtoFilter_Type()
)
tnAceIpv4ProtoFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4ProtoFilter.setStatus("current")


class _TnAceIpv4ProtoValue_Type(Integer32):
    """Custom type tnAceIpv4ProtoValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnAceIpv4ProtoValue_Type.__name__ = "Integer32"
_TnAceIpv4ProtoValue_Object = MibTableColumn
tnAceIpv4ProtoValue = _TnAceIpv4ProtoValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 2),
    _TnAceIpv4ProtoValue_Type()
)
tnAceIpv4ProtoValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4ProtoValue.setStatus("current")


class _TnAceIpv4Ttl_Type(Integer32):
    """Custom type tnAceIpv4Ttl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("zero", 2),
          ("nonZero", 3))
    )


_TnAceIpv4Ttl_Type.__name__ = "Integer32"
_TnAceIpv4Ttl_Object = MibTableColumn
tnAceIpv4Ttl = _TnAceIpv4Ttl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 3),
    _TnAceIpv4Ttl_Type()
)
tnAceIpv4Ttl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4Ttl.setStatus("current")


class _TnAceIpv4Fragment_Type(Integer32):
    """Custom type tnAceIpv4Fragment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("yes", 2),
          ("no", 3))
    )


_TnAceIpv4Fragment_Type.__name__ = "Integer32"
_TnAceIpv4Fragment_Object = MibTableColumn
tnAceIpv4Fragment = _TnAceIpv4Fragment_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 4),
    _TnAceIpv4Fragment_Type()
)
tnAceIpv4Fragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4Fragment.setStatus("current")


class _TnAceIpv4Option_Type(Integer32):
    """Custom type tnAceIpv4Option based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("yes", 2),
          ("no", 3))
    )


_TnAceIpv4Option_Type.__name__ = "Integer32"
_TnAceIpv4Option_Object = MibTableColumn
tnAceIpv4Option = _TnAceIpv4Option_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 5),
    _TnAceIpv4Option_Type()
)
tnAceIpv4Option.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4Option.setStatus("current")
_TnAceIpv4SipFilter_Type = HostOrNetworkOrAny
_TnAceIpv4SipFilter_Object = MibTableColumn
tnAceIpv4SipFilter = _TnAceIpv4SipFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 6),
    _TnAceIpv4SipFilter_Type()
)
tnAceIpv4SipFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4SipFilter.setStatus("current")
_TnAceIpv4SipAddress_Type = InetAddress
_TnAceIpv4SipAddress_Object = MibTableColumn
tnAceIpv4SipAddress = _TnAceIpv4SipAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 7),
    _TnAceIpv4SipAddress_Type()
)
tnAceIpv4SipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4SipAddress.setStatus("current")
_TnAceIpv4SipMask_Type = InetAddress
_TnAceIpv4SipMask_Object = MibTableColumn
tnAceIpv4SipMask = _TnAceIpv4SipMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 8),
    _TnAceIpv4SipMask_Type()
)
tnAceIpv4SipMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4SipMask.setStatus("current")
_TnAceIpv4DipFilter_Type = HostOrNetworkOrAny
_TnAceIpv4DipFilter_Object = MibTableColumn
tnAceIpv4DipFilter = _TnAceIpv4DipFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 9),
    _TnAceIpv4DipFilter_Type()
)
tnAceIpv4DipFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4DipFilter.setStatus("current")
_TnAceIpv4DipAddress_Type = InetAddress
_TnAceIpv4DipAddress_Object = MibTableColumn
tnAceIpv4DipAddress = _TnAceIpv4DipAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 10),
    _TnAceIpv4DipAddress_Type()
)
tnAceIpv4DipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4DipAddress.setStatus("current")
_TnAceIpv4DipMask_Type = InetAddress
_TnAceIpv4DipMask_Object = MibTableColumn
tnAceIpv4DipMask = _TnAceIpv4DipMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 11),
    _TnAceIpv4DipMask_Type()
)
tnAceIpv4DipMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4DipMask.setStatus("current")


class _TnAceIpv4IcmpTypeFilter_Type(Integer32):
    """Custom type tnAceIpv4IcmpTypeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnAceIpv4IcmpTypeFilter_Type.__name__ = "Integer32"
_TnAceIpv4IcmpTypeFilter_Object = MibTableColumn
tnAceIpv4IcmpTypeFilter = _TnAceIpv4IcmpTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 12),
    _TnAceIpv4IcmpTypeFilter_Type()
)
tnAceIpv4IcmpTypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4IcmpTypeFilter.setStatus("current")


class _TnAceIpv4IcmpTypeValue_Type(Integer32):
    """Custom type tnAceIpv4IcmpTypeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnAceIpv4IcmpTypeValue_Type.__name__ = "Integer32"
_TnAceIpv4IcmpTypeValue_Object = MibTableColumn
tnAceIpv4IcmpTypeValue = _TnAceIpv4IcmpTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 13),
    _TnAceIpv4IcmpTypeValue_Type()
)
tnAceIpv4IcmpTypeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4IcmpTypeValue.setStatus("current")


class _TnAceIpv4IcmpCodeFilter_Type(Integer32):
    """Custom type tnAceIpv4IcmpCodeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_TnAceIpv4IcmpCodeFilter_Type.__name__ = "Integer32"
_TnAceIpv4IcmpCodeFilter_Object = MibTableColumn
tnAceIpv4IcmpCodeFilter = _TnAceIpv4IcmpCodeFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 14),
    _TnAceIpv4IcmpCodeFilter_Type()
)
tnAceIpv4IcmpCodeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4IcmpCodeFilter.setStatus("current")


class _TnAceIpv4IcmpCodeValue_Type(Integer32):
    """Custom type tnAceIpv4IcmpCodeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnAceIpv4IcmpCodeValue_Type.__name__ = "Integer32"
_TnAceIpv4IcmpCodeValue_Object = MibTableColumn
tnAceIpv4IcmpCodeValue = _TnAceIpv4IcmpCodeValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 15),
    _TnAceIpv4IcmpCodeValue_Type()
)
tnAceIpv4IcmpCodeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIpv4IcmpCodeValue.setStatus("current")


class _TnAceIPv4SrcPortFilterType_Type(Integer32):
    """Custom type tnAceIPv4SrcPortFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2),
          ("range", 3))
    )


_TnAceIPv4SrcPortFilterType_Type.__name__ = "Integer32"
_TnAceIPv4SrcPortFilterType_Object = MibTableColumn
tnAceIPv4SrcPortFilterType = _TnAceIPv4SrcPortFilterType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 16),
    _TnAceIPv4SrcPortFilterType_Type()
)
tnAceIPv4SrcPortFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIPv4SrcPortFilterType.setStatus("current")


class _TnAceIPv4SrcPortFilterNo_Type(Integer32):
    """Custom type tnAceIPv4SrcPortFilterNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnAceIPv4SrcPortFilterNo_Type.__name__ = "Integer32"
_TnAceIPv4SrcPortFilterNo_Object = MibTableColumn
tnAceIPv4SrcPortFilterNo = _TnAceIPv4SrcPortFilterNo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 17),
    _TnAceIPv4SrcPortFilterNo_Type()
)
tnAceIPv4SrcPortFilterNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIPv4SrcPortFilterNo.setStatus("current")


class _TnAceIPv4SrcPortRangeStart_Type(Integer32):
    """Custom type tnAceIPv4SrcPortRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnAceIPv4SrcPortRangeStart_Type.__name__ = "Integer32"
_TnAceIPv4SrcPortRangeStart_Object = MibTableColumn
tnAceIPv4SrcPortRangeStart = _TnAceIPv4SrcPortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 18),
    _TnAceIPv4SrcPortRangeStart_Type()
)
tnAceIPv4SrcPortRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIPv4SrcPortRangeStart.setStatus("current")


class _TnAceIPv4SrcPortRangeEnd_Type(Integer32):
    """Custom type tnAceIPv4SrcPortRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnAceIPv4SrcPortRangeEnd_Type.__name__ = "Integer32"
_TnAceIPv4SrcPortRangeEnd_Object = MibTableColumn
tnAceIPv4SrcPortRangeEnd = _TnAceIPv4SrcPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 19),
    _TnAceIPv4SrcPortRangeEnd_Type()
)
tnAceIPv4SrcPortRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIPv4SrcPortRangeEnd.setStatus("current")


class _TnAceIPv4DstPortFilterType_Type(Integer32):
    """Custom type tnAceIPv4DstPortFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2),
          ("range", 3))
    )


_TnAceIPv4DstPortFilterType_Type.__name__ = "Integer32"
_TnAceIPv4DstPortFilterType_Object = MibTableColumn
tnAceIPv4DstPortFilterType = _TnAceIPv4DstPortFilterType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 20),
    _TnAceIPv4DstPortFilterType_Type()
)
tnAceIPv4DstPortFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIPv4DstPortFilterType.setStatus("current")


class _TnAceIPv4DstPortFilterNo_Type(Integer32):
    """Custom type tnAceIPv4DstPortFilterNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnAceIPv4DstPortFilterNo_Type.__name__ = "Integer32"
_TnAceIPv4DstPortFilterNo_Object = MibTableColumn
tnAceIPv4DstPortFilterNo = _TnAceIPv4DstPortFilterNo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 21),
    _TnAceIPv4DstPortFilterNo_Type()
)
tnAceIPv4DstPortFilterNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIPv4DstPortFilterNo.setStatus("current")


class _TnAceIPv4DstPortRangeStart_Type(Integer32):
    """Custom type tnAceIPv4DstPortRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnAceIPv4DstPortRangeStart_Type.__name__ = "Integer32"
_TnAceIPv4DstPortRangeStart_Object = MibTableColumn
tnAceIPv4DstPortRangeStart = _TnAceIPv4DstPortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 22),
    _TnAceIPv4DstPortRangeStart_Type()
)
tnAceIPv4DstPortRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIPv4DstPortRangeStart.setStatus("current")


class _TnAceIPv4DstPortRangeEnd_Type(Integer32):
    """Custom type tnAceIPv4DstPortRangeEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnAceIPv4DstPortRangeEnd_Type.__name__ = "Integer32"
_TnAceIPv4DstPortRangeEnd_Object = MibTableColumn
tnAceIPv4DstPortRangeEnd = _TnAceIPv4DstPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 23),
    _TnAceIPv4DstPortRangeEnd_Type()
)
tnAceIPv4DstPortRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIPv4DstPortRangeEnd.setStatus("current")
_TnAceIPv4TcpFin_Type = TruthValueOrAny
_TnAceIPv4TcpFin_Object = MibTableColumn
tnAceIPv4TcpFin = _TnAceIPv4TcpFin_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 24),
    _TnAceIPv4TcpFin_Type()
)
tnAceIPv4TcpFin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIPv4TcpFin.setStatus("current")
_TnAceIPv4TcpSyn_Type = TruthValueOrAny
_TnAceIPv4TcpSyn_Object = MibTableColumn
tnAceIPv4TcpSyn = _TnAceIPv4TcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 25),
    _TnAceIPv4TcpSyn_Type()
)
tnAceIPv4TcpSyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIPv4TcpSyn.setStatus("current")
_TnAceIPv4TcpRst_Type = TruthValueOrAny
_TnAceIPv4TcpRst_Object = MibTableColumn
tnAceIPv4TcpRst = _TnAceIPv4TcpRst_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 26),
    _TnAceIPv4TcpRst_Type()
)
tnAceIPv4TcpRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIPv4TcpRst.setStatus("current")
_TnAceIPv4TcpPsh_Type = TruthValueOrAny
_TnAceIPv4TcpPsh_Object = MibTableColumn
tnAceIPv4TcpPsh = _TnAceIPv4TcpPsh_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 27),
    _TnAceIPv4TcpPsh_Type()
)
tnAceIPv4TcpPsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIPv4TcpPsh.setStatus("current")
_TnAceIPv4TcpAck_Type = TruthValueOrAny
_TnAceIPv4TcpAck_Object = MibTableColumn
tnAceIPv4TcpAck = _TnAceIPv4TcpAck_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 28),
    _TnAceIPv4TcpAck_Type()
)
tnAceIPv4TcpAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIPv4TcpAck.setStatus("current")
_TnAceIPv4TcpUrg_Type = TruthValueOrAny
_TnAceIPv4TcpUrg_Object = MibTableColumn
tnAceIPv4TcpUrg = _TnAceIPv4TcpUrg_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 7, 1, 29),
    _TnAceIPv4TcpUrg_Type()
)
tnAceIPv4TcpUrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAceIPv4TcpUrg.setStatus("current")
_TnAclStatusTable_Object = MibTable
tnAclStatusTable = _TnAclStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 8)
)
if mibBuilder.loadTexts:
    tnAclStatusTable.setStatus("current")
_TnAclStatusEntry_Object = MibTableRow
tnAclStatusEntry = _TnAclStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 8, 1)
)
tnAclStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-ACL-MIB", "tnAclStatusUser"),
    (0, "TN-ACL-MIB", "tnAceIndex"),
)
if mibBuilder.loadTexts:
    tnAclStatusEntry.setStatus("current")


class _TnAclStatusUser_Type(Integer32):
    """Custom type tnAclStatusUser based on Integer32"""
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
        *(("static", 1),
          ("ipsourceguard", 2),
          ("ipmc", 3),
          ("mep", 4),
          ("arpinspection", 5),
          ("ptp", 6),
          ("dhcp", 7),
          ("loopprotect", 8),
          ("ethersat", 9),
          ("linkoam", 10))
    )


_TnAclStatusUser_Type.__name__ = "Integer32"
_TnAclStatusUser_Object = MibTableColumn
tnAclStatusUser = _TnAclStatusUser_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 8, 1, 1),
    _TnAclStatusUser_Type()
)
tnAclStatusUser.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAclStatusUser.setStatus("current")
_TnAclStatusIngressPort_Type = PortList
_TnAclStatusIngressPort_Object = MibTableColumn
tnAclStatusIngressPort = _TnAclStatusIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 8, 1, 2),
    _TnAclStatusIngressPort_Type()
)
tnAclStatusIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAclStatusIngressPort.setStatus("current")


class _TnAclStatusFrameType_Type(Integer32):
    """Custom type tnAclStatusFrameType based on Integer32"""
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
        *(("any", 1),
          ("eType", 2),
          ("arp", 3),
          ("ipv4", 4),
          ("ipv4icmp", 5),
          ("ipv4udp", 6),
          ("ipv4tcp", 7),
          ("ipv4other", 8),
          ("ipv6", 9))
    )


_TnAclStatusFrameType_Type.__name__ = "Integer32"
_TnAclStatusFrameType_Object = MibTableColumn
tnAclStatusFrameType = _TnAclStatusFrameType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 8, 1, 3),
    _TnAclStatusFrameType_Type()
)
tnAclStatusFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAclStatusFrameType.setStatus("current")
_TnAclStatusEtypeVal_Type = Integer32
_TnAclStatusEtypeVal_Object = MibTableColumn
tnAclStatusEtypeVal = _TnAclStatusEtypeVal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 8, 1, 4),
    _TnAclStatusEtypeVal_Type()
)
tnAclStatusEtypeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAclStatusEtypeVal.setStatus("current")


class _TnAclStatusAction_Type(Integer32):
    """Custom type tnAclStatusAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_TnAclStatusAction_Type.__name__ = "Integer32"
_TnAclStatusAction_Object = MibTableColumn
tnAclStatusAction = _TnAclStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 8, 1, 5),
    _TnAclStatusAction_Type()
)
tnAclStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAclStatusAction.setStatus("current")
_TnAclStatusRateLimiter_Type = RateLimiterValue
_TnAclStatusRateLimiter_Object = MibTableColumn
tnAclStatusRateLimiter = _TnAclStatusRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 8, 1, 6),
    _TnAclStatusRateLimiter_Type()
)
tnAclStatusRateLimiter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAclStatusRateLimiter.setStatus("current")
_TnAclStatusPortRedirect_Type = PortList
_TnAclStatusPortRedirect_Object = MibTableColumn
tnAclStatusPortRedirect = _TnAclStatusPortRedirect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 8, 1, 7),
    _TnAclStatusPortRedirect_Type()
)
tnAclStatusPortRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAclStatusPortRedirect.setStatus("current")


class _TnAclStatusMirror_Type(Integer32):
    """Custom type tnAclStatusMirror based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnAclStatusMirror_Type.__name__ = "Integer32"
_TnAclStatusMirror_Object = MibTableColumn
tnAclStatusMirror = _TnAclStatusMirror_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 8, 1, 8),
    _TnAclStatusMirror_Type()
)
tnAclStatusMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAclStatusMirror.setStatus("current")


class _TnAclStatusCpu_Type(Integer32):
    """Custom type tnAclStatusCpu based on Integer32"""
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


_TnAclStatusCpu_Type.__name__ = "Integer32"
_TnAclStatusCpu_Object = MibTableColumn
tnAclStatusCpu = _TnAclStatusCpu_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 8, 1, 9),
    _TnAclStatusCpu_Type()
)
tnAclStatusCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAclStatusCpu.setStatus("current")


class _TnAclStatusCpuOnce_Type(Integer32):
    """Custom type tnAclStatusCpuOnce based on Integer32"""
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


_TnAclStatusCpuOnce_Type.__name__ = "Integer32"
_TnAclStatusCpuOnce_Object = MibTableColumn
tnAclStatusCpuOnce = _TnAclStatusCpuOnce_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 8, 1, 10),
    _TnAclStatusCpuOnce_Type()
)
tnAclStatusCpuOnce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAclStatusCpuOnce.setStatus("current")
_TnAclStatusCounter_Type = Counter32
_TnAclStatusCounter_Object = MibTableColumn
tnAclStatusCounter = _TnAclStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 8, 1, 11),
    _TnAclStatusCounter_Type()
)
tnAclStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAclStatusCounter.setStatus("current")


class _TnAclStatusConflict_Type(Integer32):
    """Custom type tnAclStatusConflict based on Integer32"""
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


_TnAclStatusConflict_Type.__name__ = "Integer32"
_TnAclStatusConflict_Object = MibTableColumn
tnAclStatusConflict = _TnAclStatusConflict_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 5, 8, 1, 12),
    _TnAclStatusConflict_Type()
)
tnAclStatusConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAclStatusConflict.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-ACL-MIB",
    **{"RateLimiterValue": RateLimiterValue,
       "TruthValueOrAny": TruthValueOrAny,
       "HostOrNetworkOrAny": HostOrNetworkOrAny,
       "tnAclMgmt": tnAclMgmt,
       "tnAclPortTable": tnAclPortTable,
       "tnAclPortEntry": tnAclPortEntry,
       "tnAclPortPolicyId": tnAclPortPolicyId,
       "tnAclPortAction": tnAclPortAction,
       "tnAclPortRateLimiterId": tnAclPortRateLimiterId,
       "tnAclPortEvcPolicerState": tnAclPortEvcPolicerState,
       "tnAclPortEvcPolicerId": tnAclPortEvcPolicerId,
       "tnAclPortRedirect": tnAclPortRedirect,
       "tnAclPortMirrorState": tnAclPortMirrorState,
       "tnAclPortLoggingState": tnAclPortLoggingState,
       "tnAclPortShutdownState": tnAclPortShutdownState,
       "tnAclPortAclState": tnAclPortAclState,
       "tnAclPortCounter": tnAclPortCounter,
       "tnAclRateLimiterTable": tnAclRateLimiterTable,
       "tnAclRateLimiterEntry": tnAclRateLimiterEntry,
       "tnAclRateLimitId": tnAclRateLimitId,
       "tnAclRateLimitRate": tnAclRateLimitRate,
       "tnAclRateLimitUnit": tnAclRateLimitUnit,
       "tnAclOperTable": tnAclOperTable,
       "tnAclOperEntry": tnAclOperEntry,
       "tnAclClearCounter": tnAclClearCounter,
       "tnAceTable": tnAceTable,
       "tnAceEntry": tnAceEntry,
       "tnAceIndex": tnAceIndex,
       "tnAceNextIndex": tnAceNextIndex,
       "tnAceIngressPort": tnAceIngressPort,
       "tnAcePolicyFilterType": tnAcePolicyFilterType,
       "tnAcePolicyValue": tnAcePolicyValue,
       "tnAcePolicyBitMask": tnAcePolicyBitMask,
       "tnAcePolicyFrameType": tnAcePolicyFrameType,
       "tnAceAction": tnAceAction,
       "tnAceRateLimiter": tnAceRateLimiter,
       "tnAceEvcPolicerState": tnAceEvcPolicerState,
       "tnAceEvcPolicerId": tnAceEvcPolicerId,
       "tnAcePortRedirect": tnAcePortRedirect,
       "tnAceMirrorState": tnAceMirrorState,
       "tnAceLoggingState": tnAceLoggingState,
       "tnAceShutdownState": tnAceShutdownState,
       "tnAceCounter": tnAceCounter,
       "tnAceVlan8021qTagged": tnAceVlan8021qTagged,
       "tnAceVlanIdFilter": tnAceVlanIdFilter,
       "tnAceVlanId": tnAceVlanId,
       "tnAceTagPriority": tnAceTagPriority,
       "tnAceRowStatus": tnAceRowStatus,
       "tnAceLookup": tnAceLookup,
       "tnAceEtherTable": tnAceEtherTable,
       "tnAceEtherEntry": tnAceEtherEntry,
       "tnAceEtherSmacFilter": tnAceEtherSmacFilter,
       "tnAceEtherSmacVal": tnAceEtherSmacVal,
       "tnAceEtherDmacFilter": tnAceEtherDmacFilter,
       "tnAceEtherDmacVal": tnAceEtherDmacVal,
       "tnAceEtherTypeFilter": tnAceEtherTypeFilter,
       "tnAceEtherTypeVal": tnAceEtherTypeVal,
       "tnAceArpTable": tnAceArpTable,
       "tnAceArpEntry": tnAceArpEntry,
       "tnAceArpSmacFilter": tnAceArpSmacFilter,
       "tnAceArpSmacVal": tnAceArpSmacVal,
       "tnAceArpDmacFilter": tnAceArpDmacFilter,
       "tnAceArpParmArpRarp": tnAceArpParmArpRarp,
       "tnAceArpParmRequestReply": tnAceArpParmRequestReply,
       "tnAceArpParmSenderIpFilter": tnAceArpParmSenderIpFilter,
       "tnAceArpParmSenderIpAddress": tnAceArpParmSenderIpAddress,
       "tnAceArpParmSenderIpMask": tnAceArpParmSenderIpMask,
       "tnAceArpParmTargetIpFilter": tnAceArpParmTargetIpFilter,
       "tnAceArpParmTargetIpAddress": tnAceArpParmTargetIpAddress,
       "tnAceArpParmTargetIpMask": tnAceArpParmTargetIpMask,
       "tnAceArpSenderMacMatch": tnAceArpSenderMacMatch,
       "tnAceArpRarpTargetMacMatch": tnAceArpRarpTargetMacMatch,
       "tnAceArpIpEthernetLength": tnAceArpIpEthernetLength,
       "tnAceArpIp": tnAceArpIp,
       "tnAceArpEthernet": tnAceArpEthernet,
       "tnAceIpv4Table": tnAceIpv4Table,
       "tnAceIpv4Entry": tnAceIpv4Entry,
       "tnAceIpv4ProtoFilter": tnAceIpv4ProtoFilter,
       "tnAceIpv4ProtoValue": tnAceIpv4ProtoValue,
       "tnAceIpv4Ttl": tnAceIpv4Ttl,
       "tnAceIpv4Fragment": tnAceIpv4Fragment,
       "tnAceIpv4Option": tnAceIpv4Option,
       "tnAceIpv4SipFilter": tnAceIpv4SipFilter,
       "tnAceIpv4SipAddress": tnAceIpv4SipAddress,
       "tnAceIpv4SipMask": tnAceIpv4SipMask,
       "tnAceIpv4DipFilter": tnAceIpv4DipFilter,
       "tnAceIpv4DipAddress": tnAceIpv4DipAddress,
       "tnAceIpv4DipMask": tnAceIpv4DipMask,
       "tnAceIpv4IcmpTypeFilter": tnAceIpv4IcmpTypeFilter,
       "tnAceIpv4IcmpTypeValue": tnAceIpv4IcmpTypeValue,
       "tnAceIpv4IcmpCodeFilter": tnAceIpv4IcmpCodeFilter,
       "tnAceIpv4IcmpCodeValue": tnAceIpv4IcmpCodeValue,
       "tnAceIPv4SrcPortFilterType": tnAceIPv4SrcPortFilterType,
       "tnAceIPv4SrcPortFilterNo": tnAceIPv4SrcPortFilterNo,
       "tnAceIPv4SrcPortRangeStart": tnAceIPv4SrcPortRangeStart,
       "tnAceIPv4SrcPortRangeEnd": tnAceIPv4SrcPortRangeEnd,
       "tnAceIPv4DstPortFilterType": tnAceIPv4DstPortFilterType,
       "tnAceIPv4DstPortFilterNo": tnAceIPv4DstPortFilterNo,
       "tnAceIPv4DstPortRangeStart": tnAceIPv4DstPortRangeStart,
       "tnAceIPv4DstPortRangeEnd": tnAceIPv4DstPortRangeEnd,
       "tnAceIPv4TcpFin": tnAceIPv4TcpFin,
       "tnAceIPv4TcpSyn": tnAceIPv4TcpSyn,
       "tnAceIPv4TcpRst": tnAceIPv4TcpRst,
       "tnAceIPv4TcpPsh": tnAceIPv4TcpPsh,
       "tnAceIPv4TcpAck": tnAceIPv4TcpAck,
       "tnAceIPv4TcpUrg": tnAceIPv4TcpUrg,
       "tnAclStatusTable": tnAclStatusTable,
       "tnAclStatusEntry": tnAclStatusEntry,
       "tnAclStatusUser": tnAclStatusUser,
       "tnAclStatusIngressPort": tnAclStatusIngressPort,
       "tnAclStatusFrameType": tnAclStatusFrameType,
       "tnAclStatusEtypeVal": tnAclStatusEtypeVal,
       "tnAclStatusAction": tnAclStatusAction,
       "tnAclStatusRateLimiter": tnAclStatusRateLimiter,
       "tnAclStatusPortRedirect": tnAclStatusPortRedirect,
       "tnAclStatusMirror": tnAclStatusMirror,
       "tnAclStatusCpu": tnAclStatusCpu,
       "tnAclStatusCpuOnce": tnAclStatusCpuOnce,
       "tnAclStatusCounter": tnAclStatusCounter,
       "tnAclStatusConflict": tnAclStatusConflict}
)
