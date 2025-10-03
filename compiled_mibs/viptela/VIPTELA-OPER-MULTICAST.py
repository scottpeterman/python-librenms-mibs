# SNMP MIB module (VIPTELA-OPER-MULTICAST) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-OPER-MULTICAST
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:04 2025
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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_oper_multicast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 15)
)
if mibBuilder.loadTexts:
    viptela_oper_multicast.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-10-24 00:00",
         "2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00",
         "2016-04-22 00:00",
         "2016-03-15 00:00",
         "2016-01-30 00:00",
         "2015-12-28 00:00",
         "2015-12-01 00:00",
         "2015-10-31 00:00",
         "2015-09-27 00:00",
         "2015-09-01 00:00",
         "2015-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class IpPrefix(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(17, 17),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class IgmpIfStateEnum(TextualConvention, Integer32):
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
        *(("init", 0),
          ("querier", 1),
          ("non-querier", 2))
    )



class ReplicatorStatusEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("yes", 0),
          ("no", 1))
    )



class IgmpIfEventEnum(TextualConvention, Integer32):
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
        *(("init-event", 0),
          ("query-timer-expiry", 1),
          ("query-from-lower-ip", 2),
          ("other-querier-present", 3))
    )



class RpfStatusEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("resolved", 0),
          ("not-resolved", 1))
    )



class MulticastFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("s", 0)
    )


class JoinTypeEnum(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("starStarRp", 1),
          ("starGroup", 2),
          ("sourceGroup", 3),
          ("sourceGroupRpt", 4),
          ("autoRp", 5),
          ("sourceActive", 6))
    )



class IgmpGroupStateEnum(TextualConvention, Integer32):
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
        *(("no-members-present", 0),
          ("members-present", 1),
          ("v1-members-present", 2),
          ("checking-membership", 3))
    )



class MulticastOifFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("a", 0)
    )


class UpstreamStateEnum(TextualConvention, Integer32):
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
        *(("invalid", 0),
          ("not-joined", 1),
          ("joined", 2),
          ("not-pruned", 3),
          ("pruned", 4))
    )



class IgmpGroupEventEnum(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("init-event", 0),
          ("membership-report", 1),
          ("v1-membership-report", 2),
          ("leave", 3),
          ("query-timer-expired", 4),
          ("retransmit-timer-expired", 5),
          ("v1-host-timer-expired", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Multicast_ObjectIdentity = ObjectIdentity
multicast = _Multicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1)
)
_MulticastRpfTable_Object = MibTable
multicastRpfTable = _MulticastRpfTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 1)
)
if mibBuilder.loadTexts:
    multicastRpfTable.setStatus("current")
_MulticastRpfEntry_Object = MibTableRow
multicastRpfEntry = _MulticastRpfEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 1, 1)
)
multicastRpfEntry.setIndexNames(
    (0, "VIPTELA-OPER-MULTICAST", "multicastRpfVpnId"),
    (0, "VIPTELA-OPER-MULTICAST", "multicastRpfRpfAddress"),
)
if mibBuilder.loadTexts:
    multicastRpfEntry.setStatus("current")


class _MulticastRpfVpnId_Type(Unsigned32):
    """Custom type multicastRpfVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_MulticastRpfVpnId_Type.__name__ = "Unsigned32"
_MulticastRpfVpnId_Object = MibTableColumn
multicastRpfVpnId = _MulticastRpfVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 1, 1, 1),
    _MulticastRpfVpnId_Type()
)
multicastRpfVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastRpfVpnId.setStatus("current")
_MulticastRpfRpfAddress_Type = InetAddressIP
_MulticastRpfRpfAddress_Object = MibTableColumn
multicastRpfRpfAddress = _MulticastRpfRpfAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 1, 1, 2),
    _MulticastRpfRpfAddress_Type()
)
multicastRpfRpfAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastRpfRpfAddress.setStatus("current")
_MulticastRpfRpfStatus_Type = RpfStatusEnum
_MulticastRpfRpfStatus_Object = MibTableColumn
multicastRpfRpfStatus = _MulticastRpfRpfStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 1, 1, 3),
    _MulticastRpfRpfStatus_Type()
)
multicastRpfRpfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastRpfRpfStatus.setStatus("current")
_MulticastRpfNexthopCount_Type = Unsigned32
_MulticastRpfNexthopCount_Object = MibTableColumn
multicastRpfNexthopCount = _MulticastRpfNexthopCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 1, 1, 4),
    _MulticastRpfNexthopCount_Type()
)
multicastRpfNexthopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastRpfNexthopCount.setStatus("current")
_MulticastRpfRpfNexthopsTable_Object = MibTable
multicastRpfRpfNexthopsTable = _MulticastRpfRpfNexthopsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 2)
)
if mibBuilder.loadTexts:
    multicastRpfRpfNexthopsTable.setStatus("current")
_MulticastRpfRpfNexthopsEntry_Object = MibTableRow
multicastRpfRpfNexthopsEntry = _MulticastRpfRpfNexthopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 2, 1)
)
multicastRpfRpfNexthopsEntry.setIndexNames(
    (0, "VIPTELA-OPER-MULTICAST", "multicastRpfVpnId"),
    (0, "VIPTELA-OPER-MULTICAST", "multicastRpfRpfAddress"),
    (0, "VIPTELA-OPER-MULTICAST", "multicastRpfRpfNexthopsIndex"),
)
if mibBuilder.loadTexts:
    multicastRpfRpfNexthopsEntry.setStatus("current")
_MulticastRpfRpfNexthopsIndex_Type = Unsigned32
_MulticastRpfRpfNexthopsIndex_Object = MibTableColumn
multicastRpfRpfNexthopsIndex = _MulticastRpfRpfNexthopsIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 2, 1, 1),
    _MulticastRpfRpfNexthopsIndex_Type()
)
multicastRpfRpfNexthopsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastRpfRpfNexthopsIndex.setStatus("current")
_MulticastRpfRpfNexthopsRpfNbrAddr_Type = InetAddressIP
_MulticastRpfRpfNexthopsRpfNbrAddr_Object = MibTableColumn
multicastRpfRpfNexthopsRpfNbrAddr = _MulticastRpfRpfNexthopsRpfNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 2, 1, 2),
    _MulticastRpfRpfNexthopsRpfNbrAddr_Type()
)
multicastRpfRpfNexthopsRpfNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastRpfRpfNexthopsRpfNbrAddr.setStatus("current")


class _MulticastRpfRpfNexthopsRpfIfName_Type(String):
    """Custom type multicastRpfRpfNexthopsRpfIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MulticastRpfRpfNexthopsRpfIfName_Type.__name__ = "String"
_MulticastRpfRpfNexthopsRpfIfName_Object = MibTableColumn
multicastRpfRpfNexthopsRpfIfName = _MulticastRpfRpfNexthopsRpfIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 2, 1, 3),
    _MulticastRpfRpfNexthopsRpfIfName_Type()
)
multicastRpfRpfNexthopsRpfIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastRpfRpfNexthopsRpfIfName.setStatus("current")
_MulticastRpfRpfNexthopsRpfTunnel_Type = InetAddressIP
_MulticastRpfRpfNexthopsRpfTunnel_Object = MibTableColumn
multicastRpfRpfNexthopsRpfTunnel = _MulticastRpfRpfNexthopsRpfTunnel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 2, 1, 4),
    _MulticastRpfRpfNexthopsRpfTunnel_Type()
)
multicastRpfRpfNexthopsRpfTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastRpfRpfNexthopsRpfTunnel.setStatus("current")


class _MulticastRpfRpfNhopsRpfTunColor_Type(Integer32):
    """Custom type multicastRpfRpfNhopsRpfTunColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_MulticastRpfRpfNhopsRpfTunColor_Type.__name__ = "Integer32"
_MulticastRpfRpfNhopsRpfTunColor_Object = MibTableColumn
multicastRpfRpfNhopsRpfTunColor = _MulticastRpfRpfNhopsRpfTunColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 2, 1, 5),
    _MulticastRpfRpfNhopsRpfTunColor_Type()
)
multicastRpfRpfNhopsRpfTunColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastRpfRpfNhopsRpfTunColor.setStatus("current")


class _MulticastRpfRpfNhopsRpfTunEncap_Type(Integer32):
    """Custom type multicastRpfRpfNhopsRpfTunEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_MulticastRpfRpfNhopsRpfTunEncap_Type.__name__ = "Integer32"
_MulticastRpfRpfNhopsRpfTunEncap_Object = MibTableColumn
multicastRpfRpfNhopsRpfTunEncap = _MulticastRpfRpfNhopsRpfTunEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 2, 1, 6),
    _MulticastRpfRpfNhopsRpfTunEncap_Type()
)
multicastRpfRpfNhopsRpfTunEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastRpfRpfNhopsRpfTunEncap.setStatus("current")
_MulticastTopologyTable_Object = MibTable
multicastTopologyTable = _MulticastTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 3)
)
if mibBuilder.loadTexts:
    multicastTopologyTable.setStatus("current")
_MulticastTopologyEntry_Object = MibTableRow
multicastTopologyEntry = _MulticastTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 3, 1)
)
multicastTopologyEntry.setIndexNames(
    (0, "VIPTELA-OPER-MULTICAST", "multicastTopologyVpnId"),
    (0, "VIPTELA-OPER-MULTICAST", "multicastTopologyGroup"),
    (0, "VIPTELA-OPER-MULTICAST", "multicastTopologySource"),
    (0, "VIPTELA-OPER-MULTICAST", "multicastTopologyJoinType"),
)
if mibBuilder.loadTexts:
    multicastTopologyEntry.setStatus("current")


class _MulticastTopologyVpnId_Type(Unsigned32):
    """Custom type multicastTopologyVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_MulticastTopologyVpnId_Type.__name__ = "Unsigned32"
_MulticastTopologyVpnId_Object = MibTableColumn
multicastTopologyVpnId = _MulticastTopologyVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 3, 1, 1),
    _MulticastTopologyVpnId_Type()
)
multicastTopologyVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastTopologyVpnId.setStatus("current")
_MulticastTopologyGroup_Type = InetAddressIP
_MulticastTopologyGroup_Object = MibTableColumn
multicastTopologyGroup = _MulticastTopologyGroup_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 3, 1, 2),
    _MulticastTopologyGroup_Type()
)
multicastTopologyGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastTopologyGroup.setStatus("current")
_MulticastTopologySource_Type = InetAddressIP
_MulticastTopologySource_Object = MibTableColumn
multicastTopologySource = _MulticastTopologySource_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 3, 1, 3),
    _MulticastTopologySource_Type()
)
multicastTopologySource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastTopologySource.setStatus("current")
_MulticastTopologyJoinType_Type = JoinTypeEnum
_MulticastTopologyJoinType_Object = MibTableColumn
multicastTopologyJoinType = _MulticastTopologyJoinType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 3, 1, 4),
    _MulticastTopologyJoinType_Type()
)
multicastTopologyJoinType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastTopologyJoinType.setStatus("current")
_MulticastTopologyFlags_Type = MulticastFlags
_MulticastTopologyFlags_Object = MibTableColumn
multicastTopologyFlags = _MulticastTopologyFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 3, 1, 5),
    _MulticastTopologyFlags_Type()
)
multicastTopologyFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastTopologyFlags.setStatus("current")
_MulticastTopologyRpAddress_Type = InetAddressIP
_MulticastTopologyRpAddress_Object = MibTableColumn
multicastTopologyRpAddress = _MulticastTopologyRpAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 3, 1, 6),
    _MulticastTopologyRpAddress_Type()
)
multicastTopologyRpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastTopologyRpAddress.setStatus("current")
_MulticastTopologyReplicator_Type = InetAddressIP
_MulticastTopologyReplicator_Object = MibTableColumn
multicastTopologyReplicator = _MulticastTopologyReplicator_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 3, 1, 7),
    _MulticastTopologyReplicator_Type()
)
multicastTopologyReplicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastTopologyReplicator.setStatus("current")
_MulticastTopologyUpstreamNeighbor_Type = InetAddressIP
_MulticastTopologyUpstreamNeighbor_Object = MibTableColumn
multicastTopologyUpstreamNeighbor = _MulticastTopologyUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 3, 1, 8),
    _MulticastTopologyUpstreamNeighbor_Type()
)
multicastTopologyUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastTopologyUpstreamNeighbor.setStatus("current")
_MulticastTopologyUpstreamState_Type = UpstreamStateEnum
_MulticastTopologyUpstreamState_Object = MibTableColumn
multicastTopologyUpstreamState = _MulticastTopologyUpstreamState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 3, 1, 9),
    _MulticastTopologyUpstreamState_Type()
)
multicastTopologyUpstreamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastTopologyUpstreamState.setStatus("current")


class _MulticastTopologyUpstreamInterface_Type(String):
    """Custom type multicastTopologyUpstreamInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MulticastTopologyUpstreamInterface_Type.__name__ = "String"
_MulticastTopologyUpstreamInterface_Object = MibTableColumn
multicastTopologyUpstreamInterface = _MulticastTopologyUpstreamInterface_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 3, 1, 10),
    _MulticastTopologyUpstreamInterface_Type()
)
multicastTopologyUpstreamInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastTopologyUpstreamInterface.setStatus("current")
_MulticastTopologyUpTime_Type = String
_MulticastTopologyUpTime_Object = MibTableColumn
multicastTopologyUpTime = _MulticastTopologyUpTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 3, 1, 11),
    _MulticastTopologyUpTime_Type()
)
multicastTopologyUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastTopologyUpTime.setStatus("current")
_MulticastTopologyExpires_Type = String
_MulticastTopologyExpires_Object = MibTableColumn
multicastTopologyExpires = _MulticastTopologyExpires_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 3, 1, 12),
    _MulticastTopologyExpires_Type()
)
multicastTopologyExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastTopologyExpires.setStatus("current")
_MulticastTopologyTopologyOilTable_Object = MibTable
multicastTopologyTopologyOilTable = _MulticastTopologyTopologyOilTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 4)
)
if mibBuilder.loadTexts:
    multicastTopologyTopologyOilTable.setStatus("current")
_MulticastTopologyTopologyOilEntry_Object = MibTableRow
multicastTopologyTopologyOilEntry = _MulticastTopologyTopologyOilEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 4, 1)
)
multicastTopologyTopologyOilEntry.setIndexNames(
    (0, "VIPTELA-OPER-MULTICAST", "multicastTopologyVpnId"),
    (0, "VIPTELA-OPER-MULTICAST", "multicastTopologyGroup"),
    (0, "VIPTELA-OPER-MULTICAST", "multicastTopologySource"),
    (0, "VIPTELA-OPER-MULTICAST", "multicastTopologyJoinType"),
    (0, "VIPTELA-OPER-MULTICAST", "multicastTopologyTopologyOilIndex"),
)
if mibBuilder.loadTexts:
    multicastTopologyTopologyOilEntry.setStatus("current")
_MulticastTopologyTopologyOilIndex_Type = Unsigned32
_MulticastTopologyTopologyOilIndex_Object = MibTableColumn
multicastTopologyTopologyOilIndex = _MulticastTopologyTopologyOilIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 4, 1, 1),
    _MulticastTopologyTopologyOilIndex_Type()
)
multicastTopologyTopologyOilIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastTopologyTopologyOilIndex.setStatus("current")


class _MulticastTopologyTopologyOilOifName_Type(String):
    """Custom type multicastTopologyTopologyOilOifName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MulticastTopologyTopologyOilOifName_Type.__name__ = "String"
_MulticastTopologyTopologyOilOifName_Object = MibTableColumn
multicastTopologyTopologyOilOifName = _MulticastTopologyTopologyOilOifName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 4, 1, 2),
    _MulticastTopologyTopologyOilOifName_Type()
)
multicastTopologyTopologyOilOifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastTopologyTopologyOilOifName.setStatus("current")
_MulticastTopologyTopologyOilOifFlags_Type = MulticastOifFlags
_MulticastTopologyTopologyOilOifFlags_Object = MibTableColumn
multicastTopologyTopologyOilOifFlags = _MulticastTopologyTopologyOilOifFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 4, 1, 3),
    _MulticastTopologyTopologyOilOifFlags_Type()
)
multicastTopologyTopologyOilOifFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastTopologyTopologyOilOifFlags.setStatus("current")
_MulticastTopologyTopologyOilOifTunnel_Type = InetAddressIP
_MulticastTopologyTopologyOilOifTunnel_Object = MibTableColumn
multicastTopologyTopologyOilOifTunnel = _MulticastTopologyTopologyOilOifTunnel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 4, 1, 4),
    _MulticastTopologyTopologyOilOifTunnel_Type()
)
multicastTopologyTopologyOilOifTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastTopologyTopologyOilOifTunnel.setStatus("current")
_MulticastReplicatorTable_Object = MibTable
multicastReplicatorTable = _MulticastReplicatorTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 5)
)
if mibBuilder.loadTexts:
    multicastReplicatorTable.setStatus("current")
_MulticastReplicatorEntry_Object = MibTableRow
multicastReplicatorEntry = _MulticastReplicatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 5, 1)
)
multicastReplicatorEntry.setIndexNames(
    (0, "VIPTELA-OPER-MULTICAST", "multicastReplicatorVpnId"),
    (0, "VIPTELA-OPER-MULTICAST", "multicastReplicatorReplicatorAddress"),
)
if mibBuilder.loadTexts:
    multicastReplicatorEntry.setStatus("current")


class _MulticastReplicatorVpnId_Type(Unsigned32):
    """Custom type multicastReplicatorVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_MulticastReplicatorVpnId_Type.__name__ = "Unsigned32"
_MulticastReplicatorVpnId_Object = MibTableColumn
multicastReplicatorVpnId = _MulticastReplicatorVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 5, 1, 1),
    _MulticastReplicatorVpnId_Type()
)
multicastReplicatorVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastReplicatorVpnId.setStatus("current")
_MulticastReplicatorReplicatorAddress_Type = InetAddressIP
_MulticastReplicatorReplicatorAddress_Object = MibTableColumn
multicastReplicatorReplicatorAddress = _MulticastReplicatorReplicatorAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 5, 1, 2),
    _MulticastReplicatorReplicatorAddress_Type()
)
multicastReplicatorReplicatorAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastReplicatorReplicatorAddress.setStatus("current")


class _MulticastReplicatorReplicatorStatus_Type(Integer32):
    """Custom type multicastReplicatorReplicatorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dOWN", 1),
          ("uP", 2))
    )


_MulticastReplicatorReplicatorStatus_Type.__name__ = "Integer32"
_MulticastReplicatorReplicatorStatus_Object = MibTableColumn
multicastReplicatorReplicatorStatus = _MulticastReplicatorReplicatorStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 5, 1, 3),
    _MulticastReplicatorReplicatorStatus_Type()
)
multicastReplicatorReplicatorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastReplicatorReplicatorStatus.setStatus("current")
_MulticastReplicatorLoadPercent_Type = Unsigned32
_MulticastReplicatorLoadPercent_Object = MibTableColumn
multicastReplicatorLoadPercent = _MulticastReplicatorLoadPercent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 5, 1, 4),
    _MulticastReplicatorLoadPercent_Type()
)
multicastReplicatorLoadPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastReplicatorLoadPercent.setStatus("current")
_MulticastTunnelTable_Object = MibTable
multicastTunnelTable = _MulticastTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 6)
)
if mibBuilder.loadTexts:
    multicastTunnelTable.setStatus("current")
_MulticastTunnelEntry_Object = MibTableRow
multicastTunnelEntry = _MulticastTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 6, 1)
)
multicastTunnelEntry.setIndexNames(
    (0, "VIPTELA-OPER-MULTICAST", "multicastTunnelVpnId"),
    (0, "VIPTELA-OPER-MULTICAST", "multicastTunnelTunnelAddress"),
)
if mibBuilder.loadTexts:
    multicastTunnelEntry.setStatus("current")


class _MulticastTunnelVpnId_Type(Unsigned32):
    """Custom type multicastTunnelVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_MulticastTunnelVpnId_Type.__name__ = "Unsigned32"
_MulticastTunnelVpnId_Object = MibTableColumn
multicastTunnelVpnId = _MulticastTunnelVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 6, 1, 1),
    _MulticastTunnelVpnId_Type()
)
multicastTunnelVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastTunnelVpnId.setStatus("current")
_MulticastTunnelTunnelAddress_Type = InetAddressIP
_MulticastTunnelTunnelAddress_Object = MibTableColumn
multicastTunnelTunnelAddress = _MulticastTunnelTunnelAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 6, 1, 2),
    _MulticastTunnelTunnelAddress_Type()
)
multicastTunnelTunnelAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastTunnelTunnelAddress.setStatus("current")


class _MulticastTunnelTunnelStatus_Type(Integer32):
    """Custom type multicastTunnelTunnelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dOWN", 1),
          ("uP", 2))
    )


_MulticastTunnelTunnelStatus_Type.__name__ = "Integer32"
_MulticastTunnelTunnelStatus_Object = MibTableColumn
multicastTunnelTunnelStatus = _MulticastTunnelTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 6, 1, 3),
    _MulticastTunnelTunnelStatus_Type()
)
multicastTunnelTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastTunnelTunnelStatus.setStatus("current")
_MulticastTunnelReplicator_Type = ReplicatorStatusEnum
_MulticastTunnelReplicator_Object = MibTableColumn
multicastTunnelReplicator = _MulticastTunnelReplicator_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 1, 6, 1, 4),
    _MulticastTunnelReplicator_Type()
)
multicastTunnelReplicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastTunnelReplicator.setStatus("current")
_Pim_ObjectIdentity = ObjectIdentity
pim = _Pim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2)
)
_PimInterfaceTable_Object = MibTable
pimInterfaceTable = _PimInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 1)
)
if mibBuilder.loadTexts:
    pimInterfaceTable.setStatus("current")
_PimInterfaceEntry_Object = MibTableRow
pimInterfaceEntry = _PimInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 1, 1)
)
pimInterfaceEntry.setIndexNames(
    (0, "VIPTELA-OPER-MULTICAST", "pimInterfaceVpnId"),
    (1, "VIPTELA-OPER-MULTICAST", "pimInterfaceIfName"),
)
if mibBuilder.loadTexts:
    pimInterfaceEntry.setStatus("current")


class _PimInterfaceVpnId_Type(Unsigned32):
    """Custom type pimInterfaceVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_PimInterfaceVpnId_Type.__name__ = "Unsigned32"
_PimInterfaceVpnId_Object = MibTableColumn
pimInterfaceVpnId = _PimInterfaceVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 1, 1, 1),
    _PimInterfaceVpnId_Type()
)
pimInterfaceVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimInterfaceVpnId.setStatus("current")


class _PimInterfaceIfName_Type(String):
    """Custom type pimInterfaceIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PimInterfaceIfName_Type.__name__ = "String"
_PimInterfaceIfName_Object = MibTableColumn
pimInterfaceIfName = _PimInterfaceIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 1, 1, 2),
    _PimInterfaceIfName_Type()
)
pimInterfaceIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimInterfaceIfName.setStatus("current")
_PimInterfaceIfAddr_Type = IpPrefix
_PimInterfaceIfAddr_Object = MibTableColumn
pimInterfaceIfAddr = _PimInterfaceIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 1, 1, 3),
    _PimInterfaceIfAddr_Type()
)
pimInterfaceIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceIfAddr.setStatus("current")
_PimInterfaceNeighborCount_Type = Unsigned32
_PimInterfaceNeighborCount_Object = MibTableColumn
pimInterfaceNeighborCount = _PimInterfaceNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 1, 1, 4),
    _PimInterfaceNeighborCount_Type()
)
pimInterfaceNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceNeighborCount.setStatus("current")
_PimInterfaceHelloInterval_Type = Unsigned32
_PimInterfaceHelloInterval_Object = MibTableColumn
pimInterfaceHelloInterval = _PimInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 1, 1, 5),
    _PimInterfaceHelloInterval_Type()
)
pimInterfaceHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceHelloInterval.setStatus("current")
_PimInterfacePriority_Type = Unsigned32
_PimInterfacePriority_Object = MibTableColumn
pimInterfacePriority = _PimInterfacePriority_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 1, 1, 6),
    _PimInterfacePriority_Type()
)
pimInterfacePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfacePriority.setStatus("current")
_PimInterfaceDrAddress_Type = InetAddressIP
_PimInterfaceDrAddress_Object = MibTableColumn
pimInterfaceDrAddress = _PimInterfaceDrAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 1, 1, 7),
    _PimInterfaceDrAddress_Type()
)
pimInterfaceDrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceDrAddress.setStatus("current")
_PimInterfaceJoinPruneInterval_Type = Unsigned32
_PimInterfaceJoinPruneInterval_Object = MibTableColumn
pimInterfaceJoinPruneInterval = _PimInterfaceJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 1, 1, 8),
    _PimInterfaceJoinPruneInterval_Type()
)
pimInterfaceJoinPruneInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceJoinPruneInterval.setStatus("current")
_PimRpMappingTable_Object = MibTable
pimRpMappingTable = _PimRpMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 2)
)
if mibBuilder.loadTexts:
    pimRpMappingTable.setStatus("current")
_PimRpMappingEntry_Object = MibTableRow
pimRpMappingEntry = _PimRpMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 2, 1)
)
pimRpMappingEntry.setIndexNames(
    (0, "VIPTELA-OPER-MULTICAST", "pimRpMappingVpnId"),
    (0, "VIPTELA-OPER-MULTICAST", "pimRpMappingType"),
    (0, "VIPTELA-OPER-MULTICAST", "pimRpMappingGroup"),
)
if mibBuilder.loadTexts:
    pimRpMappingEntry.setStatus("current")


class _PimRpMappingVpnId_Type(Unsigned32):
    """Custom type pimRpMappingVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_PimRpMappingVpnId_Type.__name__ = "Unsigned32"
_PimRpMappingVpnId_Object = MibTableColumn
pimRpMappingVpnId = _PimRpMappingVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 2, 1, 1),
    _PimRpMappingVpnId_Type()
)
pimRpMappingVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimRpMappingVpnId.setStatus("current")


class _PimRpMappingType_Type(Integer32):
    """Custom type pimRpMappingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("auto-RP", 0)
    )


_PimRpMappingType_Type.__name__ = "Integer32"
_PimRpMappingType_Object = MibTableColumn
pimRpMappingType = _PimRpMappingType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 2, 1, 2),
    _PimRpMappingType_Type()
)
pimRpMappingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimRpMappingType.setStatus("current")
_PimRpMappingGroup_Type = IpPrefix
_PimRpMappingGroup_Object = MibTableColumn
pimRpMappingGroup = _PimRpMappingGroup_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 2, 1, 3),
    _PimRpMappingGroup_Type()
)
pimRpMappingGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimRpMappingGroup.setStatus("current")
_PimRpMappingRpAddress_Type = InetAddressIP
_PimRpMappingRpAddress_Object = MibTableColumn
pimRpMappingRpAddress = _PimRpMappingRpAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 2, 1, 4),
    _PimRpMappingRpAddress_Type()
)
pimRpMappingRpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimRpMappingRpAddress.setStatus("current")
_PimNeighborTable_Object = MibTable
pimNeighborTable = _PimNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 3)
)
if mibBuilder.loadTexts:
    pimNeighborTable.setStatus("current")
_PimNeighborEntry_Object = MibTableRow
pimNeighborEntry = _PimNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 3, 1)
)
pimNeighborEntry.setIndexNames(
    (0, "VIPTELA-OPER-MULTICAST", "pimNeighborVpnId"),
    (0, "VIPTELA-OPER-MULTICAST", "pimNeighborIfName"),
    (0, "VIPTELA-OPER-MULTICAST", "pimNeighborNbrAddr"),
)
if mibBuilder.loadTexts:
    pimNeighborEntry.setStatus("current")


class _PimNeighborVpnId_Type(Unsigned32):
    """Custom type pimNeighborVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_PimNeighborVpnId_Type.__name__ = "Unsigned32"
_PimNeighborVpnId_Object = MibTableColumn
pimNeighborVpnId = _PimNeighborVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 3, 1, 1),
    _PimNeighborVpnId_Type()
)
pimNeighborVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimNeighborVpnId.setStatus("current")


class _PimNeighborIfName_Type(String):
    """Custom type pimNeighborIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PimNeighborIfName_Type.__name__ = "String"
_PimNeighborIfName_Object = MibTableColumn
pimNeighborIfName = _PimNeighborIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 3, 1, 2),
    _PimNeighborIfName_Type()
)
pimNeighborIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimNeighborIfName.setStatus("current")
_PimNeighborNbrAddr_Type = InetAddressIP
_PimNeighborNbrAddr_Object = MibTableColumn
pimNeighborNbrAddr = _PimNeighborNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 3, 1, 3),
    _PimNeighborNbrAddr_Type()
)
pimNeighborNbrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimNeighborNbrAddr.setStatus("current")
_PimNeighborUpTime_Type = String
_PimNeighborUpTime_Object = MibTableColumn
pimNeighborUpTime = _PimNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 3, 1, 4),
    _PimNeighborUpTime_Type()
)
pimNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborUpTime.setStatus("current")
_PimNeighborExpires_Type = String
_PimNeighborExpires_Object = MibTableColumn
pimNeighborExpires = _PimNeighborExpires_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 3, 1, 5),
    _PimNeighborExpires_Type()
)
pimNeighborExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborExpires.setStatus("current")
_PimNeighborPriority_Type = Unsigned32
_PimNeighborPriority_Object = MibTableColumn
pimNeighborPriority = _PimNeighborPriority_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 3, 1, 6),
    _PimNeighborPriority_Type()
)
pimNeighborPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborPriority.setStatus("current")
_PimNeighborHoldTime_Type = Unsigned32
_PimNeighborHoldTime_Object = MibTableColumn
pimNeighborHoldTime = _PimNeighborHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 3, 1, 7),
    _PimNeighborHoldTime_Type()
)
pimNeighborHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborHoldTime.setStatus("current")
_PimNeighborDrAddress_Type = InetAddressIP
_PimNeighborDrAddress_Object = MibTableColumn
pimNeighborDrAddress = _PimNeighborDrAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 3, 1, 8),
    _PimNeighborDrAddress_Type()
)
pimNeighborDrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborDrAddress.setStatus("current")
_PimStatisticsTable_Object = MibTable
pimStatisticsTable = _PimStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 4)
)
if mibBuilder.loadTexts:
    pimStatisticsTable.setStatus("current")
_PimStatisticsEntry_Object = MibTableRow
pimStatisticsEntry = _PimStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 4, 1)
)
pimStatisticsEntry.setIndexNames(
    (0, "VIPTELA-OPER-MULTICAST", "pimStatisticsVpnId"),
)
if mibBuilder.loadTexts:
    pimStatisticsEntry.setStatus("current")


class _PimStatisticsVpnId_Type(Unsigned32):
    """Custom type pimStatisticsVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_PimStatisticsVpnId_Type.__name__ = "Unsigned32"
_PimStatisticsVpnId_Object = MibTableColumn
pimStatisticsVpnId = _PimStatisticsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 4, 1, 1),
    _PimStatisticsVpnId_Type()
)
pimStatisticsVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimStatisticsVpnId.setStatus("current")
_PimStatisticsHelloRx_Type = Unsigned32
_PimStatisticsHelloRx_Object = MibTableColumn
pimStatisticsHelloRx = _PimStatisticsHelloRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 4, 1, 2),
    _PimStatisticsHelloRx_Type()
)
pimStatisticsHelloRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStatisticsHelloRx.setStatus("current")
_PimStatisticsJoinPruneRx_Type = Unsigned32
_PimStatisticsJoinPruneRx_Object = MibTableColumn
pimStatisticsJoinPruneRx = _PimStatisticsJoinPruneRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 4, 1, 3),
    _PimStatisticsJoinPruneRx_Type()
)
pimStatisticsJoinPruneRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStatisticsJoinPruneRx.setStatus("current")
_PimStatisticsAssertRx_Type = Unsigned32
_PimStatisticsAssertRx_Object = MibTableColumn
pimStatisticsAssertRx = _PimStatisticsAssertRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 4, 1, 4),
    _PimStatisticsAssertRx_Type()
)
pimStatisticsAssertRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStatisticsAssertRx.setStatus("current")
_PimStatisticsAutoRpAnnounceRx_Type = Unsigned32
_PimStatisticsAutoRpAnnounceRx_Object = MibTableColumn
pimStatisticsAutoRpAnnounceRx = _PimStatisticsAutoRpAnnounceRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 4, 1, 5),
    _PimStatisticsAutoRpAnnounceRx_Type()
)
pimStatisticsAutoRpAnnounceRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStatisticsAutoRpAnnounceRx.setStatus("current")
_PimStatisticsAutoRpMappingRx_Type = Unsigned32
_PimStatisticsAutoRpMappingRx_Object = MibTableColumn
pimStatisticsAutoRpMappingRx = _PimStatisticsAutoRpMappingRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 4, 1, 6),
    _PimStatisticsAutoRpMappingRx_Type()
)
pimStatisticsAutoRpMappingRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStatisticsAutoRpMappingRx.setStatus("current")
_PimStatisticsUnsupportedRx_Type = Unsigned32
_PimStatisticsUnsupportedRx_Object = MibTableColumn
pimStatisticsUnsupportedRx = _PimStatisticsUnsupportedRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 4, 1, 7),
    _PimStatisticsUnsupportedRx_Type()
)
pimStatisticsUnsupportedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStatisticsUnsupportedRx.setStatus("current")
_PimStatisticsUnknownRx_Type = Unsigned32
_PimStatisticsUnknownRx_Object = MibTableColumn
pimStatisticsUnknownRx = _PimStatisticsUnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 4, 1, 8),
    _PimStatisticsUnknownRx_Type()
)
pimStatisticsUnknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStatisticsUnknownRx.setStatus("current")
_PimStatisticsBadRx_Type = Unsigned32
_PimStatisticsBadRx_Object = MibTableColumn
pimStatisticsBadRx = _PimStatisticsBadRx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 4, 1, 9),
    _PimStatisticsBadRx_Type()
)
pimStatisticsBadRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStatisticsBadRx.setStatus("current")
_PimStatisticsHelloTx_Type = Unsigned32
_PimStatisticsHelloTx_Object = MibTableColumn
pimStatisticsHelloTx = _PimStatisticsHelloTx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 4, 1, 10),
    _PimStatisticsHelloTx_Type()
)
pimStatisticsHelloTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStatisticsHelloTx.setStatus("current")
_PimStatisticsJoinPruneTx_Type = Unsigned32
_PimStatisticsJoinPruneTx_Object = MibTableColumn
pimStatisticsJoinPruneTx = _PimStatisticsJoinPruneTx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 4, 1, 11),
    _PimStatisticsJoinPruneTx_Type()
)
pimStatisticsJoinPruneTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStatisticsJoinPruneTx.setStatus("current")
_PimStatisticsAssertTx_Type = Unsigned32
_PimStatisticsAssertTx_Object = MibTableColumn
pimStatisticsAssertTx = _PimStatisticsAssertTx_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 2, 4, 1, 12),
    _PimStatisticsAssertTx_Type()
)
pimStatisticsAssertTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStatisticsAssertTx.setStatus("current")
_Igmp_ObjectIdentity = ObjectIdentity
igmp = _Igmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3)
)
_IgmpSummary_ObjectIdentity = ObjectIdentity
igmpSummary = _IgmpSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 1)
)
_IgmpSummaryVersion_Type = Unsigned32
_IgmpSummaryVersion_Object = MibScalar
igmpSummaryVersion = _IgmpSummaryVersion_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 1, 1),
    _IgmpSummaryVersion_Type()
)
igmpSummaryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSummaryVersion.setStatus("current")
_IgmpSummaryQueryInterval_Type = Unsigned32
_IgmpSummaryQueryInterval_Object = MibScalar
igmpSummaryQueryInterval = _IgmpSummaryQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 1, 2),
    _IgmpSummaryQueryInterval_Type()
)
igmpSummaryQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSummaryQueryInterval.setStatus("current")
_IgmpSummaryQueryResponseTime_Type = Unsigned32
_IgmpSummaryQueryResponseTime_Object = MibScalar
igmpSummaryQueryResponseTime = _IgmpSummaryQueryResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 1, 3),
    _IgmpSummaryQueryResponseTime_Type()
)
igmpSummaryQueryResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSummaryQueryResponseTime.setStatus("current")
_IgmpSummaryLastMemberQueryResponseTime_Type = Unsigned32
_IgmpSummaryLastMemberQueryResponseTime_Object = MibScalar
igmpSummaryLastMemberQueryResponseTime = _IgmpSummaryLastMemberQueryResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 1, 4),
    _IgmpSummaryLastMemberQueryResponseTime_Type()
)
igmpSummaryLastMemberQueryResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSummaryLastMemberQueryResponseTime.setStatus("current")
_IgmpSummaryLastMemberQueryCount_Type = Unsigned32
_IgmpSummaryLastMemberQueryCount_Object = MibScalar
igmpSummaryLastMemberQueryCount = _IgmpSummaryLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 1, 5),
    _IgmpSummaryLastMemberQueryCount_Type()
)
igmpSummaryLastMemberQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSummaryLastMemberQueryCount.setStatus("current")
_IgmpSummaryQuerierTimeout_Type = Unsigned32
_IgmpSummaryQuerierTimeout_Object = MibScalar
igmpSummaryQuerierTimeout = _IgmpSummaryQuerierTimeout_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 1, 6),
    _IgmpSummaryQuerierTimeout_Type()
)
igmpSummaryQuerierTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSummaryQuerierTimeout.setStatus("current")
_IgmpInterfaceTable_Object = MibTable
igmpInterfaceTable = _IgmpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 2)
)
if mibBuilder.loadTexts:
    igmpInterfaceTable.setStatus("current")
_IgmpInterfaceEntry_Object = MibTableRow
igmpInterfaceEntry = _IgmpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 2, 1)
)
igmpInterfaceEntry.setIndexNames(
    (0, "VIPTELA-OPER-MULTICAST", "igmpInterfaceVpnId"),
    (1, "VIPTELA-OPER-MULTICAST", "igmpInterfaceIfName"),
)
if mibBuilder.loadTexts:
    igmpInterfaceEntry.setStatus("current")


class _IgmpInterfaceVpnId_Type(Unsigned32):
    """Custom type igmpInterfaceVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IgmpInterfaceVpnId_Type.__name__ = "Unsigned32"
_IgmpInterfaceVpnId_Object = MibTableColumn
igmpInterfaceVpnId = _IgmpInterfaceVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 2, 1, 1),
    _IgmpInterfaceVpnId_Type()
)
igmpInterfaceVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpInterfaceVpnId.setStatus("current")


class _IgmpInterfaceIfName_Type(String):
    """Custom type igmpInterfaceIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IgmpInterfaceIfName_Type.__name__ = "String"
_IgmpInterfaceIfName_Object = MibTableColumn
igmpInterfaceIfName = _IgmpInterfaceIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 2, 1, 2),
    _IgmpInterfaceIfName_Type()
)
igmpInterfaceIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpInterfaceIfName.setStatus("current")
_IgmpInterfaceIfAddr_Type = IpPrefix
_IgmpInterfaceIfAddr_Object = MibTableColumn
igmpInterfaceIfAddr = _IgmpInterfaceIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 2, 1, 3),
    _IgmpInterfaceIfAddr_Type()
)
igmpInterfaceIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceIfAddr.setStatus("current")
_IgmpInterfaceGroupCount_Type = Unsigned32
_IgmpInterfaceGroupCount_Object = MibTableColumn
igmpInterfaceGroupCount = _IgmpInterfaceGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 2, 1, 4),
    _IgmpInterfaceGroupCount_Type()
)
igmpInterfaceGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceGroupCount.setStatus("current")
_IgmpInterfaceQuerier_Type = TruthValue
_IgmpInterfaceQuerier_Object = MibTableColumn
igmpInterfaceQuerier = _IgmpInterfaceQuerier_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 2, 1, 5),
    _IgmpInterfaceQuerier_Type()
)
igmpInterfaceQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceQuerier.setStatus("current")
_IgmpInterfaceQuerierIp_Type = InetAddressIP
_IgmpInterfaceQuerierIp_Object = MibTableColumn
igmpInterfaceQuerierIp = _IgmpInterfaceQuerierIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 2, 1, 6),
    _IgmpInterfaceQuerierIp_Type()
)
igmpInterfaceQuerierIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceQuerierIp.setStatus("current")
_IgmpInterfaceQueryInterval_Type = String
_IgmpInterfaceQueryInterval_Object = MibTableColumn
igmpInterfaceQueryInterval = _IgmpInterfaceQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 2, 1, 7),
    _IgmpInterfaceQueryInterval_Type()
)
igmpInterfaceQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceQueryInterval.setStatus("current")
_IgmpInterfaceState_Type = IgmpIfStateEnum
_IgmpInterfaceState_Object = MibTableColumn
igmpInterfaceState = _IgmpInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 2, 1, 8),
    _IgmpInterfaceState_Type()
)
igmpInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceState.setStatus("current")
_IgmpInterfaceOtherQuerierExpiry_Type = String
_IgmpInterfaceOtherQuerierExpiry_Object = MibTableColumn
igmpInterfaceOtherQuerierExpiry = _IgmpInterfaceOtherQuerierExpiry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 2, 1, 9),
    _IgmpInterfaceOtherQuerierExpiry_Type()
)
igmpInterfaceOtherQuerierExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceOtherQuerierExpiry.setStatus("current")
_IgmpInterfaceEvent_Type = IgmpIfEventEnum
_IgmpInterfaceEvent_Object = MibTableColumn
igmpInterfaceEvent = _IgmpInterfaceEvent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 2, 1, 10),
    _IgmpInterfaceEvent_Type()
)
igmpInterfaceEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceEvent.setStatus("current")
_IgmpGroupsTable_Object = MibTable
igmpGroupsTable = _IgmpGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 3)
)
if mibBuilder.loadTexts:
    igmpGroupsTable.setStatus("current")
_IgmpGroupsEntry_Object = MibTableRow
igmpGroupsEntry = _IgmpGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 3, 1)
)
igmpGroupsEntry.setIndexNames(
    (0, "VIPTELA-OPER-MULTICAST", "igmpGroupsVpnId"),
    (0, "VIPTELA-OPER-MULTICAST", "igmpGroupsIfName"),
    (0, "VIPTELA-OPER-MULTICAST", "igmpGroupsGroup"),
)
if mibBuilder.loadTexts:
    igmpGroupsEntry.setStatus("current")


class _IgmpGroupsVpnId_Type(Unsigned32):
    """Custom type igmpGroupsVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IgmpGroupsVpnId_Type.__name__ = "Unsigned32"
_IgmpGroupsVpnId_Object = MibTableColumn
igmpGroupsVpnId = _IgmpGroupsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 3, 1, 1),
    _IgmpGroupsVpnId_Type()
)
igmpGroupsVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpGroupsVpnId.setStatus("current")


class _IgmpGroupsIfName_Type(String):
    """Custom type igmpGroupsIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IgmpGroupsIfName_Type.__name__ = "String"
_IgmpGroupsIfName_Object = MibTableColumn
igmpGroupsIfName = _IgmpGroupsIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 3, 1, 2),
    _IgmpGroupsIfName_Type()
)
igmpGroupsIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpGroupsIfName.setStatus("current")
_IgmpGroupsGroup_Type = InetAddressIP
_IgmpGroupsGroup_Object = MibTableColumn
igmpGroupsGroup = _IgmpGroupsGroup_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 3, 1, 3),
    _IgmpGroupsGroup_Type()
)
igmpGroupsGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpGroupsGroup.setStatus("current")
_IgmpGroupsV1MembersPresent_Type = TruthValue
_IgmpGroupsV1MembersPresent_Object = MibTableColumn
igmpGroupsV1MembersPresent = _IgmpGroupsV1MembersPresent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 3, 1, 4),
    _IgmpGroupsV1MembersPresent_Type()
)
igmpGroupsV1MembersPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupsV1MembersPresent.setStatus("current")
_IgmpGroupsState_Type = IgmpGroupStateEnum
_IgmpGroupsState_Object = MibTableColumn
igmpGroupsState = _IgmpGroupsState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 3, 1, 5),
    _IgmpGroupsState_Type()
)
igmpGroupsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupsState.setStatus("current")
_IgmpGroupsUptime_Type = String
_IgmpGroupsUptime_Object = MibTableColumn
igmpGroupsUptime = _IgmpGroupsUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 3, 1, 6),
    _IgmpGroupsUptime_Type()
)
igmpGroupsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupsUptime.setStatus("current")
_IgmpGroupsExpires_Type = String
_IgmpGroupsExpires_Object = MibTableColumn
igmpGroupsExpires = _IgmpGroupsExpires_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 3, 1, 7),
    _IgmpGroupsExpires_Type()
)
igmpGroupsExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupsExpires.setStatus("current")
_IgmpGroupsV1Expires_Type = String
_IgmpGroupsV1Expires_Object = MibTableColumn
igmpGroupsV1Expires = _IgmpGroupsV1Expires_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 3, 1, 8),
    _IgmpGroupsV1Expires_Type()
)
igmpGroupsV1Expires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupsV1Expires.setStatus("current")
_IgmpGroupsEvent_Type = IgmpGroupEventEnum
_IgmpGroupsEvent_Object = MibTableColumn
igmpGroupsEvent = _IgmpGroupsEvent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 3, 1, 9),
    _IgmpGroupsEvent_Type()
)
igmpGroupsEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupsEvent.setStatus("current")
_IgmpStatisticsTable_Object = MibTable
igmpStatisticsTable = _IgmpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 4)
)
if mibBuilder.loadTexts:
    igmpStatisticsTable.setStatus("current")
_IgmpStatisticsEntry_Object = MibTableRow
igmpStatisticsEntry = _IgmpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 4, 1)
)
igmpStatisticsEntry.setIndexNames(
    (0, "VIPTELA-OPER-MULTICAST", "igmpStatisticsVpnId"),
)
if mibBuilder.loadTexts:
    igmpStatisticsEntry.setStatus("current")


class _IgmpStatisticsVpnId_Type(Unsigned32):
    """Custom type igmpStatisticsVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IgmpStatisticsVpnId_Type.__name__ = "Unsigned32"
_IgmpStatisticsVpnId_Object = MibTableColumn
igmpStatisticsVpnId = _IgmpStatisticsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 4, 1, 1),
    _IgmpStatisticsVpnId_Type()
)
igmpStatisticsVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpStatisticsVpnId.setStatus("current")
_IgmpStatisticsRxGeneralQuery_Type = Counter64
_IgmpStatisticsRxGeneralQuery_Object = MibTableColumn
igmpStatisticsRxGeneralQuery = _IgmpStatisticsRxGeneralQuery_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 4, 1, 2),
    _IgmpStatisticsRxGeneralQuery_Type()
)
igmpStatisticsRxGeneralQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStatisticsRxGeneralQuery.setStatus("current")
_IgmpStatisticsRxGroupQuery_Type = Counter64
_IgmpStatisticsRxGroupQuery_Object = MibTableColumn
igmpStatisticsRxGroupQuery = _IgmpStatisticsRxGroupQuery_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 4, 1, 3),
    _IgmpStatisticsRxGroupQuery_Type()
)
igmpStatisticsRxGroupQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStatisticsRxGroupQuery.setStatus("current")
_IgmpStatisticsRxV1Report_Type = Counter64
_IgmpStatisticsRxV1Report_Object = MibTableColumn
igmpStatisticsRxV1Report = _IgmpStatisticsRxV1Report_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 4, 1, 4),
    _IgmpStatisticsRxV1Report_Type()
)
igmpStatisticsRxV1Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStatisticsRxV1Report.setStatus("current")
_IgmpStatisticsRxV2Report_Type = Counter64
_IgmpStatisticsRxV2Report_Object = MibTableColumn
igmpStatisticsRxV2Report = _IgmpStatisticsRxV2Report_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 4, 1, 5),
    _IgmpStatisticsRxV2Report_Type()
)
igmpStatisticsRxV2Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStatisticsRxV2Report.setStatus("current")
_IgmpStatisticsRxLeave_Type = Counter64
_IgmpStatisticsRxLeave_Object = MibTableColumn
igmpStatisticsRxLeave = _IgmpStatisticsRxLeave_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 4, 1, 6),
    _IgmpStatisticsRxLeave_Type()
)
igmpStatisticsRxLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStatisticsRxLeave.setStatus("current")
_IgmpStatisticsRxUnknown_Type = Counter64
_IgmpStatisticsRxUnknown_Object = MibTableColumn
igmpStatisticsRxUnknown = _IgmpStatisticsRxUnknown_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 4, 1, 7),
    _IgmpStatisticsRxUnknown_Type()
)
igmpStatisticsRxUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStatisticsRxUnknown.setStatus("current")
_IgmpStatisticsRxError_Type = Counter64
_IgmpStatisticsRxError_Object = MibTableColumn
igmpStatisticsRxError = _IgmpStatisticsRxError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 4, 1, 8),
    _IgmpStatisticsRxError_Type()
)
igmpStatisticsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStatisticsRxError.setStatus("current")
_IgmpStatisticsTxGeneralQuery_Type = Counter64
_IgmpStatisticsTxGeneralQuery_Object = MibTableColumn
igmpStatisticsTxGeneralQuery = _IgmpStatisticsTxGeneralQuery_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 4, 1, 9),
    _IgmpStatisticsTxGeneralQuery_Type()
)
igmpStatisticsTxGeneralQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStatisticsTxGeneralQuery.setStatus("current")
_IgmpStatisticsTxGroupQuery_Type = Counter64
_IgmpStatisticsTxGroupQuery_Object = MibTableColumn
igmpStatisticsTxGroupQuery = _IgmpStatisticsTxGroupQuery_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 4, 1, 10),
    _IgmpStatisticsTxGroupQuery_Type()
)
igmpStatisticsTxGroupQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStatisticsTxGroupQuery.setStatus("current")
_IgmpStatisticsTxError_Type = Counter64
_IgmpStatisticsTxError_Object = MibTableColumn
igmpStatisticsTxError = _IgmpStatisticsTxError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 15, 3, 4, 1, 11),
    _IgmpStatisticsTxError_Type()
)
igmpStatisticsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStatisticsTxError.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-OPER-MULTICAST",
    **{"ConfdString": ConfdString,
       "InetAddressIP": InetAddressIP,
       "IpPrefix": IpPrefix,
       "String": String,
       "IgmpIfStateEnum": IgmpIfStateEnum,
       "ReplicatorStatusEnum": ReplicatorStatusEnum,
       "IgmpIfEventEnum": IgmpIfEventEnum,
       "RpfStatusEnum": RpfStatusEnum,
       "MulticastFlags": MulticastFlags,
       "JoinTypeEnum": JoinTypeEnum,
       "IgmpGroupStateEnum": IgmpGroupStateEnum,
       "MulticastOifFlags": MulticastOifFlags,
       "UpstreamStateEnum": UpstreamStateEnum,
       "IgmpGroupEventEnum": IgmpGroupEventEnum,
       "viptela-oper-multicast": viptela_oper_multicast,
       "multicast": multicast,
       "multicastRpfTable": multicastRpfTable,
       "multicastRpfEntry": multicastRpfEntry,
       "multicastRpfVpnId": multicastRpfVpnId,
       "multicastRpfRpfAddress": multicastRpfRpfAddress,
       "multicastRpfRpfStatus": multicastRpfRpfStatus,
       "multicastRpfNexthopCount": multicastRpfNexthopCount,
       "multicastRpfRpfNexthopsTable": multicastRpfRpfNexthopsTable,
       "multicastRpfRpfNexthopsEntry": multicastRpfRpfNexthopsEntry,
       "multicastRpfRpfNexthopsIndex": multicastRpfRpfNexthopsIndex,
       "multicastRpfRpfNexthopsRpfNbrAddr": multicastRpfRpfNexthopsRpfNbrAddr,
       "multicastRpfRpfNexthopsRpfIfName": multicastRpfRpfNexthopsRpfIfName,
       "multicastRpfRpfNexthopsRpfTunnel": multicastRpfRpfNexthopsRpfTunnel,
       "multicastRpfRpfNhopsRpfTunColor": multicastRpfRpfNhopsRpfTunColor,
       "multicastRpfRpfNhopsRpfTunEncap": multicastRpfRpfNhopsRpfTunEncap,
       "multicastTopologyTable": multicastTopologyTable,
       "multicastTopologyEntry": multicastTopologyEntry,
       "multicastTopologyVpnId": multicastTopologyVpnId,
       "multicastTopologyGroup": multicastTopologyGroup,
       "multicastTopologySource": multicastTopologySource,
       "multicastTopologyJoinType": multicastTopologyJoinType,
       "multicastTopologyFlags": multicastTopologyFlags,
       "multicastTopologyRpAddress": multicastTopologyRpAddress,
       "multicastTopologyReplicator": multicastTopologyReplicator,
       "multicastTopologyUpstreamNeighbor": multicastTopologyUpstreamNeighbor,
       "multicastTopologyUpstreamState": multicastTopologyUpstreamState,
       "multicastTopologyUpstreamInterface": multicastTopologyUpstreamInterface,
       "multicastTopologyUpTime": multicastTopologyUpTime,
       "multicastTopologyExpires": multicastTopologyExpires,
       "multicastTopologyTopologyOilTable": multicastTopologyTopologyOilTable,
       "multicastTopologyTopologyOilEntry": multicastTopologyTopologyOilEntry,
       "multicastTopologyTopologyOilIndex": multicastTopologyTopologyOilIndex,
       "multicastTopologyTopologyOilOifName": multicastTopologyTopologyOilOifName,
       "multicastTopologyTopologyOilOifFlags": multicastTopologyTopologyOilOifFlags,
       "multicastTopologyTopologyOilOifTunnel": multicastTopologyTopologyOilOifTunnel,
       "multicastReplicatorTable": multicastReplicatorTable,
       "multicastReplicatorEntry": multicastReplicatorEntry,
       "multicastReplicatorVpnId": multicastReplicatorVpnId,
       "multicastReplicatorReplicatorAddress": multicastReplicatorReplicatorAddress,
       "multicastReplicatorReplicatorStatus": multicastReplicatorReplicatorStatus,
       "multicastReplicatorLoadPercent": multicastReplicatorLoadPercent,
       "multicastTunnelTable": multicastTunnelTable,
       "multicastTunnelEntry": multicastTunnelEntry,
       "multicastTunnelVpnId": multicastTunnelVpnId,
       "multicastTunnelTunnelAddress": multicastTunnelTunnelAddress,
       "multicastTunnelTunnelStatus": multicastTunnelTunnelStatus,
       "multicastTunnelReplicator": multicastTunnelReplicator,
       "pim": pim,
       "pimInterfaceTable": pimInterfaceTable,
       "pimInterfaceEntry": pimInterfaceEntry,
       "pimInterfaceVpnId": pimInterfaceVpnId,
       "pimInterfaceIfName": pimInterfaceIfName,
       "pimInterfaceIfAddr": pimInterfaceIfAddr,
       "pimInterfaceNeighborCount": pimInterfaceNeighborCount,
       "pimInterfaceHelloInterval": pimInterfaceHelloInterval,
       "pimInterfacePriority": pimInterfacePriority,
       "pimInterfaceDrAddress": pimInterfaceDrAddress,
       "pimInterfaceJoinPruneInterval": pimInterfaceJoinPruneInterval,
       "pimRpMappingTable": pimRpMappingTable,
       "pimRpMappingEntry": pimRpMappingEntry,
       "pimRpMappingVpnId": pimRpMappingVpnId,
       "pimRpMappingType": pimRpMappingType,
       "pimRpMappingGroup": pimRpMappingGroup,
       "pimRpMappingRpAddress": pimRpMappingRpAddress,
       "pimNeighborTable": pimNeighborTable,
       "pimNeighborEntry": pimNeighborEntry,
       "pimNeighborVpnId": pimNeighborVpnId,
       "pimNeighborIfName": pimNeighborIfName,
       "pimNeighborNbrAddr": pimNeighborNbrAddr,
       "pimNeighborUpTime": pimNeighborUpTime,
       "pimNeighborExpires": pimNeighborExpires,
       "pimNeighborPriority": pimNeighborPriority,
       "pimNeighborHoldTime": pimNeighborHoldTime,
       "pimNeighborDrAddress": pimNeighborDrAddress,
       "pimStatisticsTable": pimStatisticsTable,
       "pimStatisticsEntry": pimStatisticsEntry,
       "pimStatisticsVpnId": pimStatisticsVpnId,
       "pimStatisticsHelloRx": pimStatisticsHelloRx,
       "pimStatisticsJoinPruneRx": pimStatisticsJoinPruneRx,
       "pimStatisticsAssertRx": pimStatisticsAssertRx,
       "pimStatisticsAutoRpAnnounceRx": pimStatisticsAutoRpAnnounceRx,
       "pimStatisticsAutoRpMappingRx": pimStatisticsAutoRpMappingRx,
       "pimStatisticsUnsupportedRx": pimStatisticsUnsupportedRx,
       "pimStatisticsUnknownRx": pimStatisticsUnknownRx,
       "pimStatisticsBadRx": pimStatisticsBadRx,
       "pimStatisticsHelloTx": pimStatisticsHelloTx,
       "pimStatisticsJoinPruneTx": pimStatisticsJoinPruneTx,
       "pimStatisticsAssertTx": pimStatisticsAssertTx,
       "igmp": igmp,
       "igmpSummary": igmpSummary,
       "igmpSummaryVersion": igmpSummaryVersion,
       "igmpSummaryQueryInterval": igmpSummaryQueryInterval,
       "igmpSummaryQueryResponseTime": igmpSummaryQueryResponseTime,
       "igmpSummaryLastMemberQueryResponseTime": igmpSummaryLastMemberQueryResponseTime,
       "igmpSummaryLastMemberQueryCount": igmpSummaryLastMemberQueryCount,
       "igmpSummaryQuerierTimeout": igmpSummaryQuerierTimeout,
       "igmpInterfaceTable": igmpInterfaceTable,
       "igmpInterfaceEntry": igmpInterfaceEntry,
       "igmpInterfaceVpnId": igmpInterfaceVpnId,
       "igmpInterfaceIfName": igmpInterfaceIfName,
       "igmpInterfaceIfAddr": igmpInterfaceIfAddr,
       "igmpInterfaceGroupCount": igmpInterfaceGroupCount,
       "igmpInterfaceQuerier": igmpInterfaceQuerier,
       "igmpInterfaceQuerierIp": igmpInterfaceQuerierIp,
       "igmpInterfaceQueryInterval": igmpInterfaceQueryInterval,
       "igmpInterfaceState": igmpInterfaceState,
       "igmpInterfaceOtherQuerierExpiry": igmpInterfaceOtherQuerierExpiry,
       "igmpInterfaceEvent": igmpInterfaceEvent,
       "igmpGroupsTable": igmpGroupsTable,
       "igmpGroupsEntry": igmpGroupsEntry,
       "igmpGroupsVpnId": igmpGroupsVpnId,
       "igmpGroupsIfName": igmpGroupsIfName,
       "igmpGroupsGroup": igmpGroupsGroup,
       "igmpGroupsV1MembersPresent": igmpGroupsV1MembersPresent,
       "igmpGroupsState": igmpGroupsState,
       "igmpGroupsUptime": igmpGroupsUptime,
       "igmpGroupsExpires": igmpGroupsExpires,
       "igmpGroupsV1Expires": igmpGroupsV1Expires,
       "igmpGroupsEvent": igmpGroupsEvent,
       "igmpStatisticsTable": igmpStatisticsTable,
       "igmpStatisticsEntry": igmpStatisticsEntry,
       "igmpStatisticsVpnId": igmpStatisticsVpnId,
       "igmpStatisticsRxGeneralQuery": igmpStatisticsRxGeneralQuery,
       "igmpStatisticsRxGroupQuery": igmpStatisticsRxGroupQuery,
       "igmpStatisticsRxV1Report": igmpStatisticsRxV1Report,
       "igmpStatisticsRxV2Report": igmpStatisticsRxV2Report,
       "igmpStatisticsRxLeave": igmpStatisticsRxLeave,
       "igmpStatisticsRxUnknown": igmpStatisticsRxUnknown,
       "igmpStatisticsRxError": igmpStatisticsRxError,
       "igmpStatisticsTxGeneralQuery": igmpStatisticsTxGeneralQuery,
       "igmpStatisticsTxGroupQuery": igmpStatisticsTxGroupQuery,
       "igmpStatisticsTxError": igmpStatisticsTxError}
)
