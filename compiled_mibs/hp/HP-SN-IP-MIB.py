# SNMP MIB module (HP-SN-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\hp\HP-SN-IP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:50:45 2025
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

(snDvmrp,
 snFsrp,
 snGblRt,
 snIp,
 snLoopbackIf,
 snPim,
 snRip) = mibBuilder.importSymbols(
    "HP-SN-ROOT-MIB",
    "snDvmrp",
    "snFsrp",
    "snGblRt",
    "snIp",
    "snLoopbackIf",
    "snPim",
    "snRip")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class RtrStatus(Integer32):
    """Custom type RtrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )





class ClearStatus(Integer32):
    """Custom type ClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )





class RowSts(Integer32):
    """Custom type RowSts based on Integer32"""
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
        *(("other", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4))
    )





class PortIndex(Integer32):
    """Custom type PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3900),
    )





class Action(Integer32):
    """Custom type Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )





class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class Metric(Integer32):
    """Custom type Metric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class PortMask(Integer32):
    """Custom type PortMask based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnRtIpGeneral_ObjectIdentity = ObjectIdentity
snRtIpGeneral = _SnRtIpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1)
)
_SnRtClearArpCache_Type = ClearStatus
_SnRtClearArpCache_Object = MibScalar
snRtClearArpCache = _SnRtClearArpCache_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 1),
    _SnRtClearArpCache_Type()
)
snRtClearArpCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtClearArpCache.setStatus("mandatory")
_SnRtClearIpCache_Type = ClearStatus
_SnRtClearIpCache_Object = MibScalar
snRtClearIpCache = _SnRtClearIpCache_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 2),
    _SnRtClearIpCache_Type()
)
snRtClearIpCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtClearIpCache.setStatus("mandatory")
_SnRtClearIpRoute_Type = ClearStatus
_SnRtClearIpRoute_Object = MibScalar
snRtClearIpRoute = _SnRtClearIpRoute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 3),
    _SnRtClearIpRoute_Type()
)
snRtClearIpRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtClearIpRoute.setStatus("mandatory")
_SnRtBootpServer_Type = IpAddress
_SnRtBootpServer_Object = MibScalar
snRtBootpServer = _SnRtBootpServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 4),
    _SnRtBootpServer_Type()
)
snRtBootpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtBootpServer.setStatus("deprecated")


class _SnRtBootpRelayMax_Type(Integer32):
    """Custom type snRtBootpRelayMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SnRtBootpRelayMax_Type.__name__ = "Integer32"
_SnRtBootpRelayMax_Object = MibScalar
snRtBootpRelayMax = _SnRtBootpRelayMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 5),
    _SnRtBootpRelayMax_Type()
)
snRtBootpRelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtBootpRelayMax.setStatus("mandatory")


class _SnRtArpAge_Type(Integer32):
    """Custom type snRtArpAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_SnRtArpAge_Type.__name__ = "Integer32"
_SnRtArpAge_Object = MibScalar
snRtArpAge = _SnRtArpAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 6),
    _SnRtArpAge_Type()
)
snRtArpAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtArpAge.setStatus("mandatory")
_SnRtIpIrdpEnable_Type = RtrStatus
_SnRtIpIrdpEnable_Object = MibScalar
snRtIpIrdpEnable = _SnRtIpIrdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 7),
    _SnRtIpIrdpEnable_Type()
)
snRtIpIrdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpIrdpEnable.setStatus("mandatory")
_SnRtIpLoadShare_Type = RtrStatus
_SnRtIpLoadShare_Object = MibScalar
snRtIpLoadShare = _SnRtIpLoadShare_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 8),
    _SnRtIpLoadShare_Type()
)
snRtIpLoadShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpLoadShare.setStatus("mandatory")
_SnRtIpProxyArp_Type = RtrStatus
_SnRtIpProxyArp_Object = MibScalar
snRtIpProxyArp = _SnRtIpProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 9),
    _SnRtIpProxyArp_Type()
)
snRtIpProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpProxyArp.setStatus("mandatory")
_SnRtIpRarp_Type = RtrStatus
_SnRtIpRarp_Object = MibScalar
snRtIpRarp = _SnRtIpRarp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 10),
    _SnRtIpRarp_Type()
)
snRtIpRarp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRarp.setStatus("mandatory")


class _SnRtIpTtl_Type(Integer32):
    """Custom type snRtIpTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnRtIpTtl_Type.__name__ = "Integer32"
_SnRtIpTtl_Object = MibScalar
snRtIpTtl = _SnRtIpTtl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 11),
    _SnRtIpTtl_Type()
)
snRtIpTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpTtl.setStatus("mandatory")
_SnRtIpSetAllPortConfig_Type = Integer32
_SnRtIpSetAllPortConfig_Object = MibScalar
snRtIpSetAllPortConfig = _SnRtIpSetAllPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 12),
    _SnRtIpSetAllPortConfig_Type()
)
snRtIpSetAllPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpSetAllPortConfig.setStatus("mandatory")
_SnRtIpFwdCacheMaxEntries_Type = Integer32
_SnRtIpFwdCacheMaxEntries_Object = MibScalar
snRtIpFwdCacheMaxEntries = _SnRtIpFwdCacheMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 13),
    _SnRtIpFwdCacheMaxEntries_Type()
)
snRtIpFwdCacheMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpFwdCacheMaxEntries.setStatus("mandatory")
_SnRtIpFwdCacheCurEntries_Type = Integer32
_SnRtIpFwdCacheCurEntries_Object = MibScalar
snRtIpFwdCacheCurEntries = _SnRtIpFwdCacheCurEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 14),
    _SnRtIpFwdCacheCurEntries_Type()
)
snRtIpFwdCacheCurEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpFwdCacheCurEntries.setStatus("mandatory")
_SnRtIpMaxStaticRouteEntries_Type = Integer32
_SnRtIpMaxStaticRouteEntries_Object = MibScalar
snRtIpMaxStaticRouteEntries = _SnRtIpMaxStaticRouteEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 15),
    _SnRtIpMaxStaticRouteEntries_Type()
)
snRtIpMaxStaticRouteEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpMaxStaticRouteEntries.setStatus("mandatory")


class _SnRtIpDirBcastFwd_Type(RtrStatus):
    """Custom type snRtIpDirBcastFwd based on RtrStatus"""
    defaultValue = 1


_SnRtIpDirBcastFwd_Type.__name__ = "RtrStatus"
_SnRtIpDirBcastFwd_Object = MibScalar
snRtIpDirBcastFwd = _SnRtIpDirBcastFwd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 16),
    _SnRtIpDirBcastFwd_Type()
)
snRtIpDirBcastFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpDirBcastFwd.setStatus("mandatory")
_SnRtIpLoadShareNumOfPaths_Type = Integer32
_SnRtIpLoadShareNumOfPaths_Object = MibScalar
snRtIpLoadShareNumOfPaths = _SnRtIpLoadShareNumOfPaths_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 17),
    _SnRtIpLoadShareNumOfPaths_Type()
)
snRtIpLoadShareNumOfPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpLoadShareNumOfPaths.setStatus("mandatory")
_SnRtIpLoadShareMaxPaths_Type = Integer32
_SnRtIpLoadShareMaxPaths_Object = MibScalar
snRtIpLoadShareMaxPaths = _SnRtIpLoadShareMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 18),
    _SnRtIpLoadShareMaxPaths_Type()
)
snRtIpLoadShareMaxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpLoadShareMaxPaths.setStatus("mandatory")
_SnRtIpLoadShareMinPaths_Type = Integer32
_SnRtIpLoadShareMinPaths_Object = MibScalar
snRtIpLoadShareMinPaths = _SnRtIpLoadShareMinPaths_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 19),
    _SnRtIpLoadShareMinPaths_Type()
)
snRtIpLoadShareMinPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpLoadShareMinPaths.setStatus("mandatory")
_SnRtIpProtocolRouterId_Type = IpAddress
_SnRtIpProtocolRouterId_Object = MibScalar
snRtIpProtocolRouterId = _SnRtIpProtocolRouterId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 20),
    _SnRtIpProtocolRouterId_Type()
)
snRtIpProtocolRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpProtocolRouterId.setStatus("mandatory")


class _SnRtIpSourceRoute_Type(RtrStatus):
    """Custom type snRtIpSourceRoute based on RtrStatus"""
    defaultValue = 1


_SnRtIpSourceRoute_Type.__name__ = "RtrStatus"
_SnRtIpSourceRoute_Object = MibScalar
snRtIpSourceRoute = _SnRtIpSourceRoute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 1, 21),
    _SnRtIpSourceRoute_Type()
)
snRtIpSourceRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpSourceRoute.setStatus("mandatory")
_SnRtIpStaticRouteTable_Object = MibTable
snRtIpStaticRouteTable = _SnRtIpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 2)
)
if mibBuilder.loadTexts:
    snRtIpStaticRouteTable.setStatus("mandatory")
_SnRtIpStaticRouteEntry_Object = MibTableRow
snRtIpStaticRouteEntry = _SnRtIpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 2, 1)
)
snRtIpStaticRouteEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpStaticRouteIndex"),
)
if mibBuilder.loadTexts:
    snRtIpStaticRouteEntry.setStatus("mandatory")
_SnRtIpStaticRouteIndex_Type = Integer32
_SnRtIpStaticRouteIndex_Object = MibTableColumn
snRtIpStaticRouteIndex = _SnRtIpStaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 2, 1, 1),
    _SnRtIpStaticRouteIndex_Type()
)
snRtIpStaticRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpStaticRouteIndex.setStatus("mandatory")
_SnRtIpStaticRouteDest_Type = IpAddress
_SnRtIpStaticRouteDest_Object = MibTableColumn
snRtIpStaticRouteDest = _SnRtIpStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 2, 1, 2),
    _SnRtIpStaticRouteDest_Type()
)
snRtIpStaticRouteDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpStaticRouteDest.setStatus("mandatory")
_SnRtIpStaticRouteMask_Type = IpAddress
_SnRtIpStaticRouteMask_Object = MibTableColumn
snRtIpStaticRouteMask = _SnRtIpStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 2, 1, 3),
    _SnRtIpStaticRouteMask_Type()
)
snRtIpStaticRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpStaticRouteMask.setStatus("mandatory")
_SnRtIpStaticRouteNextHop_Type = IpAddress
_SnRtIpStaticRouteNextHop_Object = MibTableColumn
snRtIpStaticRouteNextHop = _SnRtIpStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 2, 1, 4),
    _SnRtIpStaticRouteNextHop_Type()
)
snRtIpStaticRouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpStaticRouteNextHop.setStatus("mandatory")
_SnRtIpStaticRouteMetric_Type = Integer32
_SnRtIpStaticRouteMetric_Object = MibTableColumn
snRtIpStaticRouteMetric = _SnRtIpStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 2, 1, 5),
    _SnRtIpStaticRouteMetric_Type()
)
snRtIpStaticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpStaticRouteMetric.setStatus("mandatory")
_SnRtIpStaticRouteRowStatus_Type = RowSts
_SnRtIpStaticRouteRowStatus_Object = MibTableColumn
snRtIpStaticRouteRowStatus = _SnRtIpStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 2, 1, 6),
    _SnRtIpStaticRouteRowStatus_Type()
)
snRtIpStaticRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpStaticRouteRowStatus.setStatus("mandatory")


class _SnRtIpStaticRouteDistance_Type(Integer32):
    """Custom type snRtIpStaticRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnRtIpStaticRouteDistance_Type.__name__ = "Integer32"
_SnRtIpStaticRouteDistance_Object = MibTableColumn
snRtIpStaticRouteDistance = _SnRtIpStaticRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 2, 1, 7),
    _SnRtIpStaticRouteDistance_Type()
)
snRtIpStaticRouteDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpStaticRouteDistance.setStatus("mandatory")
_SnRtIpFilterTable_Object = MibTable
snRtIpFilterTable = _SnRtIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 3)
)
if mibBuilder.loadTexts:
    snRtIpFilterTable.setStatus("mandatory")
_SnRtIpFilterEntry_Object = MibTableRow
snRtIpFilterEntry = _SnRtIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 3, 1)
)
snRtIpFilterEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpFilterIndex"),
)
if mibBuilder.loadTexts:
    snRtIpFilterEntry.setStatus("mandatory")
_SnRtIpFilterIndex_Type = Integer32
_SnRtIpFilterIndex_Object = MibTableColumn
snRtIpFilterIndex = _SnRtIpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 3, 1, 1),
    _SnRtIpFilterIndex_Type()
)
snRtIpFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpFilterIndex.setStatus("mandatory")


class _SnRtIpFilterAction_Type(Integer32):
    """Custom type snRtIpFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1),
          ("qosEnabled", 2))
    )


_SnRtIpFilterAction_Type.__name__ = "Integer32"
_SnRtIpFilterAction_Object = MibTableColumn
snRtIpFilterAction = _SnRtIpFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 3, 1, 2),
    _SnRtIpFilterAction_Type()
)
snRtIpFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterAction.setStatus("mandatory")


class _SnRtIpFilterProtocol_Type(Integer32):
    """Custom type snRtIpFilterProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnRtIpFilterProtocol_Type.__name__ = "Integer32"
_SnRtIpFilterProtocol_Object = MibTableColumn
snRtIpFilterProtocol = _SnRtIpFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 3, 1, 3),
    _SnRtIpFilterProtocol_Type()
)
snRtIpFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterProtocol.setStatus("mandatory")
_SnRtIpFilterSourceIp_Type = IpAddress
_SnRtIpFilterSourceIp_Object = MibTableColumn
snRtIpFilterSourceIp = _SnRtIpFilterSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 3, 1, 4),
    _SnRtIpFilterSourceIp_Type()
)
snRtIpFilterSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterSourceIp.setStatus("mandatory")
_SnRtIpFilterSourceMask_Type = IpAddress
_SnRtIpFilterSourceMask_Object = MibTableColumn
snRtIpFilterSourceMask = _SnRtIpFilterSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 3, 1, 5),
    _SnRtIpFilterSourceMask_Type()
)
snRtIpFilterSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterSourceMask.setStatus("mandatory")
_SnRtIpFilterDestIp_Type = IpAddress
_SnRtIpFilterDestIp_Object = MibTableColumn
snRtIpFilterDestIp = _SnRtIpFilterDestIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 3, 1, 6),
    _SnRtIpFilterDestIp_Type()
)
snRtIpFilterDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterDestIp.setStatus("mandatory")
_SnRtIpFilterDestMask_Type = IpAddress
_SnRtIpFilterDestMask_Object = MibTableColumn
snRtIpFilterDestMask = _SnRtIpFilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 3, 1, 7),
    _SnRtIpFilterDestMask_Type()
)
snRtIpFilterDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterDestMask.setStatus("mandatory")


class _SnRtIpFilterOperator_Type(Integer32):
    """Custom type snRtIpFilterOperator based on Integer32"""
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
        *(("greater", 1),
          ("equal", 2),
          ("less", 3),
          ("notEqual", 4))
    )


_SnRtIpFilterOperator_Type.__name__ = "Integer32"
_SnRtIpFilterOperator_Object = MibTableColumn
snRtIpFilterOperator = _SnRtIpFilterOperator_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 3, 1, 8),
    _SnRtIpFilterOperator_Type()
)
snRtIpFilterOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterOperator.setStatus("mandatory")


class _SnRtIpFilterOperand_Type(Integer32):
    """Custom type snRtIpFilterOperand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnRtIpFilterOperand_Type.__name__ = "Integer32"
_SnRtIpFilterOperand_Object = MibTableColumn
snRtIpFilterOperand = _SnRtIpFilterOperand_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 3, 1, 9),
    _SnRtIpFilterOperand_Type()
)
snRtIpFilterOperand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterOperand.setStatus("mandatory")
_SnRtIpFilterRowStatus_Type = RowSts
_SnRtIpFilterRowStatus_Object = MibTableColumn
snRtIpFilterRowStatus = _SnRtIpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 3, 1, 10),
    _SnRtIpFilterRowStatus_Type()
)
snRtIpFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterRowStatus.setStatus("mandatory")
_SnRtIpFilterEstablished_Type = RtrStatus
_SnRtIpFilterEstablished_Object = MibTableColumn
snRtIpFilterEstablished = _SnRtIpFilterEstablished_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 3, 1, 11),
    _SnRtIpFilterEstablished_Type()
)
snRtIpFilterEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterEstablished.setStatus("mandatory")


class _SnRtIpFilterQosPriority_Type(Integer32):
    """Custom type snRtIpFilterQosPriority based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("level0", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7))
    )


_SnRtIpFilterQosPriority_Type.__name__ = "Integer32"
_SnRtIpFilterQosPriority_Object = MibTableColumn
snRtIpFilterQosPriority = _SnRtIpFilterQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 3, 1, 12),
    _SnRtIpFilterQosPriority_Type()
)
snRtIpFilterQosPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpFilterQosPriority.setStatus("mandatory")
_SnRtIpRarpTable_Object = MibTable
snRtIpRarpTable = _SnRtIpRarpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 4)
)
if mibBuilder.loadTexts:
    snRtIpRarpTable.setStatus("mandatory")
_SnRtIpRarpEntry_Object = MibTableRow
snRtIpRarpEntry = _SnRtIpRarpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 4, 1)
)
snRtIpRarpEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpRarpIndex"),
)
if mibBuilder.loadTexts:
    snRtIpRarpEntry.setStatus("mandatory")


class _SnRtIpRarpIndex_Type(Integer32):
    """Custom type snRtIpRarpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SnRtIpRarpIndex_Type.__name__ = "Integer32"
_SnRtIpRarpIndex_Object = MibTableColumn
snRtIpRarpIndex = _SnRtIpRarpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 4, 1, 1),
    _SnRtIpRarpIndex_Type()
)
snRtIpRarpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpRarpIndex.setStatus("mandatory")


class _SnRtIpRarpMac_Type(OctetString):
    """Custom type snRtIpRarpMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SnRtIpRarpMac_Type.__name__ = "OctetString"
_SnRtIpRarpMac_Object = MibTableColumn
snRtIpRarpMac = _SnRtIpRarpMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 4, 1, 2),
    _SnRtIpRarpMac_Type()
)
snRtIpRarpMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRarpMac.setStatus("mandatory")
_SnRtIpRarpIp_Type = IpAddress
_SnRtIpRarpIp_Object = MibTableColumn
snRtIpRarpIp = _SnRtIpRarpIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 4, 1, 3),
    _SnRtIpRarpIp_Type()
)
snRtIpRarpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRarpIp.setStatus("mandatory")
_SnRtIpRarpRowStatus_Type = RowSts
_SnRtIpRarpRowStatus_Object = MibTableColumn
snRtIpRarpRowStatus = _SnRtIpRarpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 4, 1, 4),
    _SnRtIpRarpRowStatus_Type()
)
snRtIpRarpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRarpRowStatus.setStatus("mandatory")
_SnRtStaticArpTable_Object = MibTable
snRtStaticArpTable = _SnRtStaticArpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 5)
)
if mibBuilder.loadTexts:
    snRtStaticArpTable.setStatus("mandatory")
_SnRtStaticArpEntry_Object = MibTableRow
snRtStaticArpEntry = _SnRtStaticArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 5, 1)
)
snRtStaticArpEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtStaticArpIndex"),
)
if mibBuilder.loadTexts:
    snRtStaticArpEntry.setStatus("mandatory")


class _SnRtStaticArpIndex_Type(Integer32):
    """Custom type snRtStaticArpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SnRtStaticArpIndex_Type.__name__ = "Integer32"
_SnRtStaticArpIndex_Object = MibTableColumn
snRtStaticArpIndex = _SnRtStaticArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 5, 1, 1),
    _SnRtStaticArpIndex_Type()
)
snRtStaticArpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtStaticArpIndex.setStatus("mandatory")
_SnRtStaticArpIp_Type = IpAddress
_SnRtStaticArpIp_Object = MibTableColumn
snRtStaticArpIp = _SnRtStaticArpIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 5, 1, 2),
    _SnRtStaticArpIp_Type()
)
snRtStaticArpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtStaticArpIp.setStatus("mandatory")


class _SnRtStaticArpMac_Type(OctetString):
    """Custom type snRtStaticArpMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SnRtStaticArpMac_Type.__name__ = "OctetString"
_SnRtStaticArpMac_Object = MibTableColumn
snRtStaticArpMac = _SnRtStaticArpMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 5, 1, 3),
    _SnRtStaticArpMac_Type()
)
snRtStaticArpMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtStaticArpMac.setStatus("mandatory")
_SnRtStaticArpPort_Type = PortIndex
_SnRtStaticArpPort_Object = MibTableColumn
snRtStaticArpPort = _SnRtStaticArpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 5, 1, 4),
    _SnRtStaticArpPort_Type()
)
snRtStaticArpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtStaticArpPort.setStatus("mandatory")
_SnRtStaticArpRowStatus_Type = RowSts
_SnRtStaticArpRowStatus_Object = MibTableColumn
snRtStaticArpRowStatus = _SnRtStaticArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 5, 1, 5),
    _SnRtStaticArpRowStatus_Type()
)
snRtStaticArpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtStaticArpRowStatus.setStatus("mandatory")
_SnRtIpPortAddrTable_Object = MibTable
snRtIpPortAddrTable = _SnRtIpPortAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 6)
)
if mibBuilder.loadTexts:
    snRtIpPortAddrTable.setStatus("deprecated")
_SnRtIpPortAddrEntry_Object = MibTableRow
snRtIpPortAddrEntry = _SnRtIpPortAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 6, 1)
)
snRtIpPortAddrEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpPortAddrPortIndex"),
    (0, "HP-SN-IP-MIB", "snRtIpPortAddress"),
)
if mibBuilder.loadTexts:
    snRtIpPortAddrEntry.setStatus("deprecated")
_SnRtIpPortAddrPortIndex_Type = PortIndex
_SnRtIpPortAddrPortIndex_Object = MibTableColumn
snRtIpPortAddrPortIndex = _SnRtIpPortAddrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 6, 1, 1),
    _SnRtIpPortAddrPortIndex_Type()
)
snRtIpPortAddrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpPortAddrPortIndex.setStatus("deprecated")
_SnRtIpPortAddress_Type = IpAddress
_SnRtIpPortAddress_Object = MibTableColumn
snRtIpPortAddress = _SnRtIpPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 6, 1, 2),
    _SnRtIpPortAddress_Type()
)
snRtIpPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpPortAddress.setStatus("deprecated")
_SnRtIpPortSubnetMask_Type = IpAddress
_SnRtIpPortSubnetMask_Object = MibTableColumn
snRtIpPortSubnetMask = _SnRtIpPortSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 6, 1, 3),
    _SnRtIpPortSubnetMask_Type()
)
snRtIpPortSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortSubnetMask.setStatus("deprecated")


class _SnRtIpPortAddrType_Type(Integer32):
    """Custom type snRtIpPortAddrType based on Integer32"""
    defaultValue = 1

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


_SnRtIpPortAddrType_Type.__name__ = "Integer32"
_SnRtIpPortAddrType_Object = MibTableColumn
snRtIpPortAddrType = _SnRtIpPortAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 6, 1, 4),
    _SnRtIpPortAddrType_Type()
)
snRtIpPortAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortAddrType.setStatus("deprecated")
_SnRtIpPortRowStatus_Type = RowSts
_SnRtIpPortRowStatus_Object = MibTableColumn
snRtIpPortRowStatus = _SnRtIpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 6, 1, 5),
    _SnRtIpPortRowStatus_Type()
)
snRtIpPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortRowStatus.setStatus("deprecated")
_SnRtIpPortAccessTable_Object = MibTable
snRtIpPortAccessTable = _SnRtIpPortAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 7)
)
if mibBuilder.loadTexts:
    snRtIpPortAccessTable.setStatus("deprecated")
_SnRtIpPortAccessEntry_Object = MibTableRow
snRtIpPortAccessEntry = _SnRtIpPortAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 7, 1)
)
snRtIpPortAccessEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpPortAccessPortIndex"),
    (0, "HP-SN-IP-MIB", "snRtIpPortAccessDirection"),
)
if mibBuilder.loadTexts:
    snRtIpPortAccessEntry.setStatus("deprecated")
_SnRtIpPortAccessPortIndex_Type = PortIndex
_SnRtIpPortAccessPortIndex_Object = MibTableColumn
snRtIpPortAccessPortIndex = _SnRtIpPortAccessPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 7, 1, 1),
    _SnRtIpPortAccessPortIndex_Type()
)
snRtIpPortAccessPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpPortAccessPortIndex.setStatus("deprecated")


class _SnRtIpPortAccessDirection_Type(Integer32):
    """Custom type snRtIpPortAccessDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_SnRtIpPortAccessDirection_Type.__name__ = "Integer32"
_SnRtIpPortAccessDirection_Object = MibTableColumn
snRtIpPortAccessDirection = _SnRtIpPortAccessDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 7, 1, 2),
    _SnRtIpPortAccessDirection_Type()
)
snRtIpPortAccessDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpPortAccessDirection.setStatus("deprecated")
_SnRtIpPortAccessFilters_Type = OctetString
_SnRtIpPortAccessFilters_Object = MibTableColumn
snRtIpPortAccessFilters = _SnRtIpPortAccessFilters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 7, 1, 3),
    _SnRtIpPortAccessFilters_Type()
)
snRtIpPortAccessFilters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortAccessFilters.setStatus("deprecated")
_SnRtIpPortAccessRowStatus_Type = RowSts
_SnRtIpPortAccessRowStatus_Object = MibTableColumn
snRtIpPortAccessRowStatus = _SnRtIpPortAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 7, 1, 4),
    _SnRtIpPortAccessRowStatus_Type()
)
snRtIpPortAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortAccessRowStatus.setStatus("deprecated")
_SnRtIpPortConfigTable_Object = MibTable
snRtIpPortConfigTable = _SnRtIpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 8)
)
if mibBuilder.loadTexts:
    snRtIpPortConfigTable.setStatus("deprecated")
_SnRtIpPortConfigEntry_Object = MibTableRow
snRtIpPortConfigEntry = _SnRtIpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 8, 1)
)
snRtIpPortConfigEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    snRtIpPortConfigEntry.setStatus("deprecated")
_SnRtIpPortConfigPortIndex_Type = PortIndex
_SnRtIpPortConfigPortIndex_Object = MibTableColumn
snRtIpPortConfigPortIndex = _SnRtIpPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 8, 1, 1),
    _SnRtIpPortConfigPortIndex_Type()
)
snRtIpPortConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpPortConfigPortIndex.setStatus("deprecated")


class _SnRtIpPortMtu_Type(Integer32):
    """Custom type snRtIpPortMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 4470),
    )


_SnRtIpPortMtu_Type.__name__ = "Integer32"
_SnRtIpPortMtu_Object = MibTableColumn
snRtIpPortMtu = _SnRtIpPortMtu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 8, 1, 2),
    _SnRtIpPortMtu_Type()
)
snRtIpPortMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortMtu.setStatus("deprecated")


class _SnRtIpPortEncap_Type(Integer32):
    """Custom type snRtIpPortEncap based on Integer32"""
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
        *(("ethernet", 1),
          ("snap", 2),
          ("hdlc", 3),
          ("ppp", 4))
    )


_SnRtIpPortEncap_Type.__name__ = "Integer32"
_SnRtIpPortEncap_Object = MibTableColumn
snRtIpPortEncap = _SnRtIpPortEncap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 8, 1, 3),
    _SnRtIpPortEncap_Type()
)
snRtIpPortEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortEncap.setStatus("deprecated")


class _SnRtIpPortMetric_Type(Integer32):
    """Custom type snRtIpPortMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SnRtIpPortMetric_Type.__name__ = "Integer32"
_SnRtIpPortMetric_Object = MibTableColumn
snRtIpPortMetric = _SnRtIpPortMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 8, 1, 4),
    _SnRtIpPortMetric_Type()
)
snRtIpPortMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortMetric.setStatus("deprecated")


class _SnRtIpPortDirBcastFwd_Type(RtrStatus):
    """Custom type snRtIpPortDirBcastFwd based on RtrStatus"""
    defaultValue = 1


_SnRtIpPortDirBcastFwd_Type.__name__ = "RtrStatus"
_SnRtIpPortDirBcastFwd_Object = MibTableColumn
snRtIpPortDirBcastFwd = _SnRtIpPortDirBcastFwd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 8, 1, 5),
    _SnRtIpPortDirBcastFwd_Type()
)
snRtIpPortDirBcastFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortDirBcastFwd.setStatus("deprecated")
_SnRtBcastFwd_ObjectIdentity = ObjectIdentity
snRtBcastFwd = _SnRtBcastFwd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9)
)
_SnRtBcastFwdGeneral_ObjectIdentity = ObjectIdentity
snRtBcastFwdGeneral = _SnRtBcastFwdGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 1)
)


class _SnRtUdpBcastFwdEnable_Type(RtrStatus):
    """Custom type snRtUdpBcastFwdEnable based on RtrStatus"""
    defaultValue = 1


_SnRtUdpBcastFwdEnable_Type.__name__ = "RtrStatus"
_SnRtUdpBcastFwdEnable_Object = MibScalar
snRtUdpBcastFwdEnable = _SnRtUdpBcastFwdEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 1, 1),
    _SnRtUdpBcastFwdEnable_Type()
)
snRtUdpBcastFwdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtUdpBcastFwdEnable.setStatus("mandatory")
_SnRtUdpBcastFwdPort_ObjectIdentity = ObjectIdentity
snRtUdpBcastFwdPort = _SnRtUdpBcastFwdPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 2)
)
_SnRtUdpBcastFwdPortTable_Object = MibTable
snRtUdpBcastFwdPortTable = _SnRtUdpBcastFwdPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 2, 1)
)
if mibBuilder.loadTexts:
    snRtUdpBcastFwdPortTable.setStatus("mandatory")
_SnRtUdpBcastFwdPortEntry_Object = MibTableRow
snRtUdpBcastFwdPortEntry = _SnRtUdpBcastFwdPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 2, 1, 1)
)
snRtUdpBcastFwdPortEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtUdpBcastFwdPortIndex"),
)
if mibBuilder.loadTexts:
    snRtUdpBcastFwdPortEntry.setStatus("mandatory")


class _SnRtUdpBcastFwdPortIndex_Type(Integer32):
    """Custom type snRtUdpBcastFwdPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SnRtUdpBcastFwdPortIndex_Type.__name__ = "Integer32"
_SnRtUdpBcastFwdPortIndex_Object = MibTableColumn
snRtUdpBcastFwdPortIndex = _SnRtUdpBcastFwdPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 2, 1, 1, 1),
    _SnRtUdpBcastFwdPortIndex_Type()
)
snRtUdpBcastFwdPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtUdpBcastFwdPortIndex.setStatus("mandatory")


class _SnRtUdpBcastFwdPortNumber_Type(Integer32):
    """Custom type snRtUdpBcastFwdPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnRtUdpBcastFwdPortNumber_Type.__name__ = "Integer32"
_SnRtUdpBcastFwdPortNumber_Object = MibTableColumn
snRtUdpBcastFwdPortNumber = _SnRtUdpBcastFwdPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 2, 1, 1, 2),
    _SnRtUdpBcastFwdPortNumber_Type()
)
snRtUdpBcastFwdPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtUdpBcastFwdPortNumber.setStatus("mandatory")
_SnRtUdpBcastFwdPortRowStatus_Type = RowSts
_SnRtUdpBcastFwdPortRowStatus_Object = MibTableColumn
snRtUdpBcastFwdPortRowStatus = _SnRtUdpBcastFwdPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 2, 1, 1, 3),
    _SnRtUdpBcastFwdPortRowStatus_Type()
)
snRtUdpBcastFwdPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtUdpBcastFwdPortRowStatus.setStatus("mandatory")
_SnRtUdpHelper_ObjectIdentity = ObjectIdentity
snRtUdpHelper = _SnRtUdpHelper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 3)
)
_SnRtUdpHelperTable_Object = MibTable
snRtUdpHelperTable = _SnRtUdpHelperTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 3, 1)
)
if mibBuilder.loadTexts:
    snRtUdpHelperTable.setStatus("mandatory")
_SnRtUdpHelperEntry_Object = MibTableRow
snRtUdpHelperEntry = _SnRtUdpHelperEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 3, 1, 1)
)
snRtUdpHelperEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtUdpHelperPortIndex"),
    (0, "HP-SN-IP-MIB", "snRtUdpHelperIndex"),
)
if mibBuilder.loadTexts:
    snRtUdpHelperEntry.setStatus("mandatory")
_SnRtUdpHelperPortIndex_Type = PortIndex
_SnRtUdpHelperPortIndex_Object = MibTableColumn
snRtUdpHelperPortIndex = _SnRtUdpHelperPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 3, 1, 1, 1),
    _SnRtUdpHelperPortIndex_Type()
)
snRtUdpHelperPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtUdpHelperPortIndex.setStatus("mandatory")


class _SnRtUdpHelperIndex_Type(Integer32):
    """Custom type snRtUdpHelperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SnRtUdpHelperIndex_Type.__name__ = "Integer32"
_SnRtUdpHelperIndex_Object = MibTableColumn
snRtUdpHelperIndex = _SnRtUdpHelperIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 3, 1, 1, 2),
    _SnRtUdpHelperIndex_Type()
)
snRtUdpHelperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtUdpHelperIndex.setStatus("mandatory")
_SnRtUdpHelperAddr_Type = IpAddress
_SnRtUdpHelperAddr_Object = MibTableColumn
snRtUdpHelperAddr = _SnRtUdpHelperAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 3, 1, 1, 3),
    _SnRtUdpHelperAddr_Type()
)
snRtUdpHelperAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtUdpHelperAddr.setStatus("mandatory")
_SnRtUdpHelperRowStatus_Type = RowSts
_SnRtUdpHelperRowStatus_Object = MibTableColumn
snRtUdpHelperRowStatus = _SnRtUdpHelperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 9, 3, 1, 1, 4),
    _SnRtUdpHelperRowStatus_Type()
)
snRtUdpHelperRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtUdpHelperRowStatus.setStatus("mandatory")
_SnRtIpTraceRoute_ObjectIdentity = ObjectIdentity
snRtIpTraceRoute = _SnRtIpTraceRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 10)
)
_SnRtIpTraceRouteGeneral_ObjectIdentity = ObjectIdentity
snRtIpTraceRouteGeneral = _SnRtIpTraceRouteGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 10, 1)
)
_SnRtIpTraceRouteTargetAddr_Type = IpAddress
_SnRtIpTraceRouteTargetAddr_Object = MibScalar
snRtIpTraceRouteTargetAddr = _SnRtIpTraceRouteTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 10, 1, 1),
    _SnRtIpTraceRouteTargetAddr_Type()
)
snRtIpTraceRouteTargetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpTraceRouteTargetAddr.setStatus("mandatory")


class _SnRtIpTraceRouteMinTtl_Type(Integer32):
    """Custom type snRtIpTraceRouteMinTtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnRtIpTraceRouteMinTtl_Type.__name__ = "Integer32"
_SnRtIpTraceRouteMinTtl_Object = MibScalar
snRtIpTraceRouteMinTtl = _SnRtIpTraceRouteMinTtl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 10, 1, 2),
    _SnRtIpTraceRouteMinTtl_Type()
)
snRtIpTraceRouteMinTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpTraceRouteMinTtl.setStatus("mandatory")


class _SnRtIpTraceRouteMaxTtl_Type(Integer32):
    """Custom type snRtIpTraceRouteMaxTtl based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnRtIpTraceRouteMaxTtl_Type.__name__ = "Integer32"
_SnRtIpTraceRouteMaxTtl_Object = MibScalar
snRtIpTraceRouteMaxTtl = _SnRtIpTraceRouteMaxTtl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 10, 1, 3),
    _SnRtIpTraceRouteMaxTtl_Type()
)
snRtIpTraceRouteMaxTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpTraceRouteMaxTtl.setStatus("mandatory")


class _SnRtIpTraceRouteTimeOut_Type(Integer32):
    """Custom type snRtIpTraceRouteTimeOut based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SnRtIpTraceRouteTimeOut_Type.__name__ = "Integer32"
_SnRtIpTraceRouteTimeOut_Object = MibScalar
snRtIpTraceRouteTimeOut = _SnRtIpTraceRouteTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 10, 1, 4),
    _SnRtIpTraceRouteTimeOut_Type()
)
snRtIpTraceRouteTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpTraceRouteTimeOut.setStatus("mandatory")


class _SnRtIpTraceRouteControl_Type(Integer32):
    """Custom type snRtIpTraceRouteControl based on Integer32"""
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
        *(("start", 1),
          ("abort", 2),
          ("success", 3),
          ("failure", 4),
          ("inProgress", 5))
    )


_SnRtIpTraceRouteControl_Type.__name__ = "Integer32"
_SnRtIpTraceRouteControl_Object = MibScalar
snRtIpTraceRouteControl = _SnRtIpTraceRouteControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 10, 1, 5),
    _SnRtIpTraceRouteControl_Type()
)
snRtIpTraceRouteControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpTraceRouteControl.setStatus("mandatory")
_SnRtIpTraceRouteResult_ObjectIdentity = ObjectIdentity
snRtIpTraceRouteResult = _SnRtIpTraceRouteResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 10, 2)
)
_SnRtIpTraceRouteResultTable_Object = MibTable
snRtIpTraceRouteResultTable = _SnRtIpTraceRouteResultTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    snRtIpTraceRouteResultTable.setStatus("mandatory")
_SnRtIpTraceRouteResultEntry_Object = MibTableRow
snRtIpTraceRouteResultEntry = _SnRtIpTraceRouteResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 10, 2, 1, 1)
)
snRtIpTraceRouteResultEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpTraceRouteResultIndex"),
)
if mibBuilder.loadTexts:
    snRtIpTraceRouteResultEntry.setStatus("mandatory")
_SnRtIpTraceRouteResultIndex_Type = Integer32
_SnRtIpTraceRouteResultIndex_Object = MibTableColumn
snRtIpTraceRouteResultIndex = _SnRtIpTraceRouteResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 10, 2, 1, 1, 1),
    _SnRtIpTraceRouteResultIndex_Type()
)
snRtIpTraceRouteResultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpTraceRouteResultIndex.setStatus("mandatory")
_SnRtIpTraceRouteResultAddr_Type = IpAddress
_SnRtIpTraceRouteResultAddr_Object = MibTableColumn
snRtIpTraceRouteResultAddr = _SnRtIpTraceRouteResultAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 10, 2, 1, 1, 2),
    _SnRtIpTraceRouteResultAddr_Type()
)
snRtIpTraceRouteResultAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpTraceRouteResultAddr.setStatus("mandatory")
_SnRtIpTraceRouteResultRoundTripTime1_Type = TimeTicks
_SnRtIpTraceRouteResultRoundTripTime1_Object = MibTableColumn
snRtIpTraceRouteResultRoundTripTime1 = _SnRtIpTraceRouteResultRoundTripTime1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 10, 2, 1, 1, 3),
    _SnRtIpTraceRouteResultRoundTripTime1_Type()
)
snRtIpTraceRouteResultRoundTripTime1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpTraceRouteResultRoundTripTime1.setStatus("mandatory")
_SnRtIpTraceRouteResultRoundTripTime2_Type = TimeTicks
_SnRtIpTraceRouteResultRoundTripTime2_Object = MibTableColumn
snRtIpTraceRouteResultRoundTripTime2 = _SnRtIpTraceRouteResultRoundTripTime2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 10, 2, 1, 1, 4),
    _SnRtIpTraceRouteResultRoundTripTime2_Type()
)
snRtIpTraceRouteResultRoundTripTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpTraceRouteResultRoundTripTime2.setStatus("mandatory")
_SnRtIpFwdCacheTable_Object = MibTable
snRtIpFwdCacheTable = _SnRtIpFwdCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 11)
)
if mibBuilder.loadTexts:
    snRtIpFwdCacheTable.setStatus("mandatory")
_SnRtIpFwdCacheEntry_Object = MibTableRow
snRtIpFwdCacheEntry = _SnRtIpFwdCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 11, 1)
)
snRtIpFwdCacheEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpFwdCacheIndex"),
)
if mibBuilder.loadTexts:
    snRtIpFwdCacheEntry.setStatus("mandatory")
_SnRtIpFwdCacheIndex_Type = Integer32
_SnRtIpFwdCacheIndex_Object = MibTableColumn
snRtIpFwdCacheIndex = _SnRtIpFwdCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 11, 1, 1),
    _SnRtIpFwdCacheIndex_Type()
)
snRtIpFwdCacheIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpFwdCacheIndex.setStatus("mandatory")
_SnRtIpFwdCacheIp_Type = IpAddress
_SnRtIpFwdCacheIp_Object = MibTableColumn
snRtIpFwdCacheIp = _SnRtIpFwdCacheIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 11, 1, 2),
    _SnRtIpFwdCacheIp_Type()
)
snRtIpFwdCacheIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpFwdCacheIp.setStatus("mandatory")


class _SnRtIpFwdCacheMac_Type(OctetString):
    """Custom type snRtIpFwdCacheMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SnRtIpFwdCacheMac_Type.__name__ = "OctetString"
_SnRtIpFwdCacheMac_Object = MibTableColumn
snRtIpFwdCacheMac = _SnRtIpFwdCacheMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 11, 1, 3),
    _SnRtIpFwdCacheMac_Type()
)
snRtIpFwdCacheMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpFwdCacheMac.setStatus("mandatory")
_SnRtIpFwdCacheNextHopIp_Type = IpAddress
_SnRtIpFwdCacheNextHopIp_Object = MibTableColumn
snRtIpFwdCacheNextHopIp = _SnRtIpFwdCacheNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 11, 1, 4),
    _SnRtIpFwdCacheNextHopIp_Type()
)
snRtIpFwdCacheNextHopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpFwdCacheNextHopIp.setStatus("mandatory")


class _SnRtIpFwdCacheOutgoingPort_Type(Integer32):
    """Custom type snRtIpFwdCacheOutgoingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3900),
    )


_SnRtIpFwdCacheOutgoingPort_Type.__name__ = "Integer32"
_SnRtIpFwdCacheOutgoingPort_Object = MibTableColumn
snRtIpFwdCacheOutgoingPort = _SnRtIpFwdCacheOutgoingPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 11, 1, 5),
    _SnRtIpFwdCacheOutgoingPort_Type()
)
snRtIpFwdCacheOutgoingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpFwdCacheOutgoingPort.setStatus("mandatory")


class _SnRtIpFwdCacheType_Type(Integer32):
    """Custom type snRtIpFwdCacheType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("permanent", 2))
    )


_SnRtIpFwdCacheType_Type.__name__ = "Integer32"
_SnRtIpFwdCacheType_Object = MibTableColumn
snRtIpFwdCacheType = _SnRtIpFwdCacheType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 11, 1, 6),
    _SnRtIpFwdCacheType_Type()
)
snRtIpFwdCacheType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpFwdCacheType.setStatus("mandatory")


class _SnRtIpFwdCacheAction_Type(Integer32):
    """Custom type snRtIpFwdCacheAction based on Integer32"""
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
        *(("other", 1),
          ("forward", 2),
          ("forUs", 3),
          ("waitForArp", 4),
          ("complexFilter", 5),
          ("icmpDeny", 6),
          ("dropPacket", 7))
    )


_SnRtIpFwdCacheAction_Type.__name__ = "Integer32"
_SnRtIpFwdCacheAction_Object = MibTableColumn
snRtIpFwdCacheAction = _SnRtIpFwdCacheAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 11, 1, 7),
    _SnRtIpFwdCacheAction_Type()
)
snRtIpFwdCacheAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpFwdCacheAction.setStatus("mandatory")


class _SnRtIpFwdCacheFragCheck_Type(Integer32):
    """Custom type snRtIpFwdCacheFragCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnRtIpFwdCacheFragCheck_Type.__name__ = "Integer32"
_SnRtIpFwdCacheFragCheck_Object = MibTableColumn
snRtIpFwdCacheFragCheck = _SnRtIpFwdCacheFragCheck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 11, 1, 8),
    _SnRtIpFwdCacheFragCheck_Type()
)
snRtIpFwdCacheFragCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpFwdCacheFragCheck.setStatus("mandatory")


class _SnRtIpFwdCacheSnapHdr_Type(Integer32):
    """Custom type snRtIpFwdCacheSnapHdr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnRtIpFwdCacheSnapHdr_Type.__name__ = "Integer32"
_SnRtIpFwdCacheSnapHdr_Object = MibTableColumn
snRtIpFwdCacheSnapHdr = _SnRtIpFwdCacheSnapHdr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 11, 1, 9),
    _SnRtIpFwdCacheSnapHdr_Type()
)
snRtIpFwdCacheSnapHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpFwdCacheSnapHdr.setStatus("mandatory")
_SnRtIpFwdCacheVLanId_Type = Integer32
_SnRtIpFwdCacheVLanId_Object = MibTableColumn
snRtIpFwdCacheVLanId = _SnRtIpFwdCacheVLanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 11, 1, 10),
    _SnRtIpFwdCacheVLanId_Type()
)
snRtIpFwdCacheVLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpFwdCacheVLanId.setStatus("mandatory")
_SnIpAsPathAccessListTable_Object = MibTable
snIpAsPathAccessListTable = _SnIpAsPathAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 12)
)
if mibBuilder.loadTexts:
    snIpAsPathAccessListTable.setStatus("mandatory")
_SnIpAsPathAccessListEntry_Object = MibTableRow
snIpAsPathAccessListEntry = _SnIpAsPathAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 12, 1)
)
snIpAsPathAccessListEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snIpAsPathAccessListIndex"),
    (0, "HP-SN-IP-MIB", "snIpAsPathAccessListSequence"),
)
if mibBuilder.loadTexts:
    snIpAsPathAccessListEntry.setStatus("mandatory")
_SnIpAsPathAccessListIndex_Type = Integer32
_SnIpAsPathAccessListIndex_Object = MibTableColumn
snIpAsPathAccessListIndex = _SnIpAsPathAccessListIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 12, 1, 1),
    _SnIpAsPathAccessListIndex_Type()
)
snIpAsPathAccessListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpAsPathAccessListIndex.setStatus("mandatory")
_SnIpAsPathAccessListSequence_Type = Integer32
_SnIpAsPathAccessListSequence_Object = MibTableColumn
snIpAsPathAccessListSequence = _SnIpAsPathAccessListSequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 12, 1, 2),
    _SnIpAsPathAccessListSequence_Type()
)
snIpAsPathAccessListSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpAsPathAccessListSequence.setStatus("mandatory")


class _SnIpAsPathAccessListAction_Type(Integer32):
    """Custom type snIpAsPathAccessListAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SnIpAsPathAccessListAction_Type.__name__ = "Integer32"
_SnIpAsPathAccessListAction_Object = MibTableColumn
snIpAsPathAccessListAction = _SnIpAsPathAccessListAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 12, 1, 3),
    _SnIpAsPathAccessListAction_Type()
)
snIpAsPathAccessListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpAsPathAccessListAction.setStatus("mandatory")


class _SnIpAsPathAccessListRegExpression_Type(OctetString):
    """Custom type snIpAsPathAccessListRegExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SnIpAsPathAccessListRegExpression_Type.__name__ = "OctetString"
_SnIpAsPathAccessListRegExpression_Object = MibTableColumn
snIpAsPathAccessListRegExpression = _SnIpAsPathAccessListRegExpression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 12, 1, 4),
    _SnIpAsPathAccessListRegExpression_Type()
)
snIpAsPathAccessListRegExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpAsPathAccessListRegExpression.setStatus("mandatory")


class _SnIpAsPathAccessListRowStatus_Type(Integer32):
    """Custom type snIpAsPathAccessListRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4),
          ("modify", 5))
    )


_SnIpAsPathAccessListRowStatus_Type.__name__ = "Integer32"
_SnIpAsPathAccessListRowStatus_Object = MibTableColumn
snIpAsPathAccessListRowStatus = _SnIpAsPathAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 12, 1, 5),
    _SnIpAsPathAccessListRowStatus_Type()
)
snIpAsPathAccessListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpAsPathAccessListRowStatus.setStatus("mandatory")
_SnIpCommunityListTable_Object = MibTable
snIpCommunityListTable = _SnIpCommunityListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 13)
)
if mibBuilder.loadTexts:
    snIpCommunityListTable.setStatus("mandatory")
_SnIpCommunityListEntry_Object = MibTableRow
snIpCommunityListEntry = _SnIpCommunityListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 13, 1)
)
snIpCommunityListEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snIpCommunityListIndex"),
    (0, "HP-SN-IP-MIB", "snIpCommunityListSequence"),
)
if mibBuilder.loadTexts:
    snIpCommunityListEntry.setStatus("mandatory")
_SnIpCommunityListIndex_Type = Integer32
_SnIpCommunityListIndex_Object = MibTableColumn
snIpCommunityListIndex = _SnIpCommunityListIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 13, 1, 1),
    _SnIpCommunityListIndex_Type()
)
snIpCommunityListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpCommunityListIndex.setStatus("mandatory")
_SnIpCommunityListSequence_Type = Integer32
_SnIpCommunityListSequence_Object = MibTableColumn
snIpCommunityListSequence = _SnIpCommunityListSequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 13, 1, 2),
    _SnIpCommunityListSequence_Type()
)
snIpCommunityListSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpCommunityListSequence.setStatus("mandatory")


class _SnIpCommunityListAction_Type(Integer32):
    """Custom type snIpCommunityListAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SnIpCommunityListAction_Type.__name__ = "Integer32"
_SnIpCommunityListAction_Object = MibTableColumn
snIpCommunityListAction = _SnIpCommunityListAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 13, 1, 3),
    _SnIpCommunityListAction_Type()
)
snIpCommunityListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpCommunityListAction.setStatus("mandatory")


class _SnIpCommunityListCommNum_Type(OctetString):
    """Custom type snIpCommunityListCommNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SnIpCommunityListCommNum_Type.__name__ = "OctetString"
_SnIpCommunityListCommNum_Object = MibTableColumn
snIpCommunityListCommNum = _SnIpCommunityListCommNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 13, 1, 4),
    _SnIpCommunityListCommNum_Type()
)
snIpCommunityListCommNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpCommunityListCommNum.setStatus("mandatory")


class _SnIpCommunityListInternet_Type(Integer32):
    """Custom type snIpCommunityListInternet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnIpCommunityListInternet_Type.__name__ = "Integer32"
_SnIpCommunityListInternet_Object = MibTableColumn
snIpCommunityListInternet = _SnIpCommunityListInternet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 13, 1, 5),
    _SnIpCommunityListInternet_Type()
)
snIpCommunityListInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpCommunityListInternet.setStatus("mandatory")


class _SnIpCommunityListNoAdvertise_Type(Integer32):
    """Custom type snIpCommunityListNoAdvertise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnIpCommunityListNoAdvertise_Type.__name__ = "Integer32"
_SnIpCommunityListNoAdvertise_Object = MibTableColumn
snIpCommunityListNoAdvertise = _SnIpCommunityListNoAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 13, 1, 6),
    _SnIpCommunityListNoAdvertise_Type()
)
snIpCommunityListNoAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpCommunityListNoAdvertise.setStatus("mandatory")


class _SnIpCommunityListNoExport_Type(Integer32):
    """Custom type snIpCommunityListNoExport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnIpCommunityListNoExport_Type.__name__ = "Integer32"
_SnIpCommunityListNoExport_Object = MibTableColumn
snIpCommunityListNoExport = _SnIpCommunityListNoExport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 13, 1, 7),
    _SnIpCommunityListNoExport_Type()
)
snIpCommunityListNoExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpCommunityListNoExport.setStatus("mandatory")


class _SnIpCommunityListRowStatus_Type(Integer32):
    """Custom type snIpCommunityListRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4),
          ("modify", 5))
    )


_SnIpCommunityListRowStatus_Type.__name__ = "Integer32"
_SnIpCommunityListRowStatus_Object = MibTableColumn
snIpCommunityListRowStatus = _SnIpCommunityListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 13, 1, 8),
    _SnIpCommunityListRowStatus_Type()
)
snIpCommunityListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpCommunityListRowStatus.setStatus("mandatory")


class _SnIpCommunityListLocalAs_Type(Integer32):
    """Custom type snIpCommunityListLocalAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnIpCommunityListLocalAs_Type.__name__ = "Integer32"
_SnIpCommunityListLocalAs_Object = MibTableColumn
snIpCommunityListLocalAs = _SnIpCommunityListLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 13, 1, 9),
    _SnIpCommunityListLocalAs_Type()
)
snIpCommunityListLocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpCommunityListLocalAs.setStatus("mandatory")
_SnIpPrefixListTable_Object = MibTable
snIpPrefixListTable = _SnIpPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 14)
)
if mibBuilder.loadTexts:
    snIpPrefixListTable.setStatus("mandatory")
_SnIpPrefixListEntry_Object = MibTableRow
snIpPrefixListEntry = _SnIpPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 14, 1)
)
snIpPrefixListEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snIpPrefixListName"),
    (0, "HP-SN-IP-MIB", "snIpPrefixListSequence"),
)
if mibBuilder.loadTexts:
    snIpPrefixListEntry.setStatus("mandatory")


class _SnIpPrefixListName_Type(OctetString):
    """Custom type snIpPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnIpPrefixListName_Type.__name__ = "OctetString"
_SnIpPrefixListName_Object = MibTableColumn
snIpPrefixListName = _SnIpPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 14, 1, 1),
    _SnIpPrefixListName_Type()
)
snIpPrefixListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpPrefixListName.setStatus("mandatory")
_SnIpPrefixListSequence_Type = Integer32
_SnIpPrefixListSequence_Object = MibTableColumn
snIpPrefixListSequence = _SnIpPrefixListSequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 14, 1, 2),
    _SnIpPrefixListSequence_Type()
)
snIpPrefixListSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpPrefixListSequence.setStatus("mandatory")


class _SnIpPrefixListDesc_Type(OctetString):
    """Custom type snIpPrefixListDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SnIpPrefixListDesc_Type.__name__ = "OctetString"
_SnIpPrefixListDesc_Object = MibTableColumn
snIpPrefixListDesc = _SnIpPrefixListDesc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 14, 1, 3),
    _SnIpPrefixListDesc_Type()
)
snIpPrefixListDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpPrefixListDesc.setStatus("mandatory")


class _SnIpPrefixListAction_Type(Integer32):
    """Custom type snIpPrefixListAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SnIpPrefixListAction_Type.__name__ = "Integer32"
_SnIpPrefixListAction_Object = MibTableColumn
snIpPrefixListAction = _SnIpPrefixListAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 14, 1, 4),
    _SnIpPrefixListAction_Type()
)
snIpPrefixListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpPrefixListAction.setStatus("mandatory")
_SnIpPrefixListAddr_Type = IpAddress
_SnIpPrefixListAddr_Object = MibTableColumn
snIpPrefixListAddr = _SnIpPrefixListAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 14, 1, 5),
    _SnIpPrefixListAddr_Type()
)
snIpPrefixListAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpPrefixListAddr.setStatus("mandatory")
_SnIpPrefixListMask_Type = IpAddress
_SnIpPrefixListMask_Object = MibTableColumn
snIpPrefixListMask = _SnIpPrefixListMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 14, 1, 6),
    _SnIpPrefixListMask_Type()
)
snIpPrefixListMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpPrefixListMask.setStatus("mandatory")


class _SnIpPrefixListGeValue_Type(Integer32):
    """Custom type snIpPrefixListGeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SnIpPrefixListGeValue_Type.__name__ = "Integer32"
_SnIpPrefixListGeValue_Object = MibTableColumn
snIpPrefixListGeValue = _SnIpPrefixListGeValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 14, 1, 7),
    _SnIpPrefixListGeValue_Type()
)
snIpPrefixListGeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpPrefixListGeValue.setStatus("mandatory")


class _SnIpPrefixListLeValue_Type(Integer32):
    """Custom type snIpPrefixListLeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SnIpPrefixListLeValue_Type.__name__ = "Integer32"
_SnIpPrefixListLeValue_Object = MibTableColumn
snIpPrefixListLeValue = _SnIpPrefixListLeValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 14, 1, 8),
    _SnIpPrefixListLeValue_Type()
)
snIpPrefixListLeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpPrefixListLeValue.setStatus("mandatory")


class _SnIpPrefixListRowStatus_Type(Integer32):
    """Custom type snIpPrefixListRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4),
          ("modify", 5))
    )


_SnIpPrefixListRowStatus_Type.__name__ = "Integer32"
_SnIpPrefixListRowStatus_Object = MibTableColumn
snIpPrefixListRowStatus = _SnIpPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 14, 1, 9),
    _SnIpPrefixListRowStatus_Type()
)
snIpPrefixListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpPrefixListRowStatus.setStatus("mandatory")
_SnIpAsPathAccessListStringTable_Object = MibTable
snIpAsPathAccessListStringTable = _SnIpAsPathAccessListStringTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 16)
)
if mibBuilder.loadTexts:
    snIpAsPathAccessListStringTable.setStatus("mandatory")
_SnIpAsPathAccessListStringEntry_Object = MibTableRow
snIpAsPathAccessListStringEntry = _SnIpAsPathAccessListStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 16, 1)
)
snIpAsPathAccessListStringEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snIpAsPathAccessListStringName"),
    (0, "HP-SN-IP-MIB", "snIpAsPathAccessListStringSequence"),
)
if mibBuilder.loadTexts:
    snIpAsPathAccessListStringEntry.setStatus("mandatory")


class _SnIpAsPathAccessListStringName_Type(DisplayString):
    """Custom type snIpAsPathAccessListStringName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnIpAsPathAccessListStringName_Type.__name__ = "DisplayString"
_SnIpAsPathAccessListStringName_Object = MibTableColumn
snIpAsPathAccessListStringName = _SnIpAsPathAccessListStringName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 16, 1, 1),
    _SnIpAsPathAccessListStringName_Type()
)
snIpAsPathAccessListStringName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpAsPathAccessListStringName.setStatus("mandatory")
_SnIpAsPathAccessListStringSequence_Type = Integer32
_SnIpAsPathAccessListStringSequence_Object = MibTableColumn
snIpAsPathAccessListStringSequence = _SnIpAsPathAccessListStringSequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 16, 1, 2),
    _SnIpAsPathAccessListStringSequence_Type()
)
snIpAsPathAccessListStringSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpAsPathAccessListStringSequence.setStatus("mandatory")


class _SnIpAsPathAccessListStringAction_Type(Integer32):
    """Custom type snIpAsPathAccessListStringAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SnIpAsPathAccessListStringAction_Type.__name__ = "Integer32"
_SnIpAsPathAccessListStringAction_Object = MibTableColumn
snIpAsPathAccessListStringAction = _SnIpAsPathAccessListStringAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 16, 1, 3),
    _SnIpAsPathAccessListStringAction_Type()
)
snIpAsPathAccessListStringAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpAsPathAccessListStringAction.setStatus("mandatory")


class _SnIpAsPathAccessListStringRegExpression_Type(DisplayString):
    """Custom type snIpAsPathAccessListStringRegExpression based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SnIpAsPathAccessListStringRegExpression_Type.__name__ = "DisplayString"
_SnIpAsPathAccessListStringRegExpression_Object = MibTableColumn
snIpAsPathAccessListStringRegExpression = _SnIpAsPathAccessListStringRegExpression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 16, 1, 4),
    _SnIpAsPathAccessListStringRegExpression_Type()
)
snIpAsPathAccessListStringRegExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpAsPathAccessListStringRegExpression.setStatus("mandatory")


class _SnIpAsPathAccessListStringRowStatus_Type(Integer32):
    """Custom type snIpAsPathAccessListStringRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4),
          ("modify", 5))
    )


_SnIpAsPathAccessListStringRowStatus_Type.__name__ = "Integer32"
_SnIpAsPathAccessListStringRowStatus_Object = MibTableColumn
snIpAsPathAccessListStringRowStatus = _SnIpAsPathAccessListStringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 16, 1, 5),
    _SnIpAsPathAccessListStringRowStatus_Type()
)
snIpAsPathAccessListStringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpAsPathAccessListStringRowStatus.setStatus("mandatory")
_SnIpCommunityListStringTable_Object = MibTable
snIpCommunityListStringTable = _SnIpCommunityListStringTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 17)
)
if mibBuilder.loadTexts:
    snIpCommunityListStringTable.setStatus("mandatory")
_SnIpCommunityListStringEntry_Object = MibTableRow
snIpCommunityListStringEntry = _SnIpCommunityListStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 17, 1)
)
snIpCommunityListStringEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snIpCommunityListStringName"),
    (0, "HP-SN-IP-MIB", "snIpCommunityListStringSequence"),
)
if mibBuilder.loadTexts:
    snIpCommunityListStringEntry.setStatus("mandatory")


class _SnIpCommunityListStringName_Type(DisplayString):
    """Custom type snIpCommunityListStringName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnIpCommunityListStringName_Type.__name__ = "DisplayString"
_SnIpCommunityListStringName_Object = MibTableColumn
snIpCommunityListStringName = _SnIpCommunityListStringName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 17, 1, 1),
    _SnIpCommunityListStringName_Type()
)
snIpCommunityListStringName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpCommunityListStringName.setStatus("mandatory")
_SnIpCommunityListStringSequence_Type = Integer32
_SnIpCommunityListStringSequence_Object = MibTableColumn
snIpCommunityListStringSequence = _SnIpCommunityListStringSequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 17, 1, 2),
    _SnIpCommunityListStringSequence_Type()
)
snIpCommunityListStringSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIpCommunityListStringSequence.setStatus("mandatory")


class _SnIpCommunityListStringAction_Type(Integer32):
    """Custom type snIpCommunityListStringAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SnIpCommunityListStringAction_Type.__name__ = "Integer32"
_SnIpCommunityListStringAction_Object = MibTableColumn
snIpCommunityListStringAction = _SnIpCommunityListStringAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 17, 1, 3),
    _SnIpCommunityListStringAction_Type()
)
snIpCommunityListStringAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpCommunityListStringAction.setStatus("mandatory")


class _SnIpCommunityListStringCommNum_Type(OctetString):
    """Custom type snIpCommunityListStringCommNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SnIpCommunityListStringCommNum_Type.__name__ = "OctetString"
_SnIpCommunityListStringCommNum_Object = MibTableColumn
snIpCommunityListStringCommNum = _SnIpCommunityListStringCommNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 17, 1, 4),
    _SnIpCommunityListStringCommNum_Type()
)
snIpCommunityListStringCommNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpCommunityListStringCommNum.setStatus("mandatory")


class _SnIpCommunityListStringInternet_Type(Integer32):
    """Custom type snIpCommunityListStringInternet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnIpCommunityListStringInternet_Type.__name__ = "Integer32"
_SnIpCommunityListStringInternet_Object = MibTableColumn
snIpCommunityListStringInternet = _SnIpCommunityListStringInternet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 17, 1, 5),
    _SnIpCommunityListStringInternet_Type()
)
snIpCommunityListStringInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpCommunityListStringInternet.setStatus("mandatory")


class _SnIpCommunityListStringNoAdvertise_Type(Integer32):
    """Custom type snIpCommunityListStringNoAdvertise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnIpCommunityListStringNoAdvertise_Type.__name__ = "Integer32"
_SnIpCommunityListStringNoAdvertise_Object = MibTableColumn
snIpCommunityListStringNoAdvertise = _SnIpCommunityListStringNoAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 17, 1, 6),
    _SnIpCommunityListStringNoAdvertise_Type()
)
snIpCommunityListStringNoAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpCommunityListStringNoAdvertise.setStatus("mandatory")


class _SnIpCommunityListStringNoExport_Type(Integer32):
    """Custom type snIpCommunityListStringNoExport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnIpCommunityListStringNoExport_Type.__name__ = "Integer32"
_SnIpCommunityListStringNoExport_Object = MibTableColumn
snIpCommunityListStringNoExport = _SnIpCommunityListStringNoExport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 17, 1, 7),
    _SnIpCommunityListStringNoExport_Type()
)
snIpCommunityListStringNoExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpCommunityListStringNoExport.setStatus("mandatory")


class _SnIpCommunityListStringRowStatus_Type(Integer32):
    """Custom type snIpCommunityListStringRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4),
          ("modify", 5))
    )


_SnIpCommunityListStringRowStatus_Type.__name__ = "Integer32"
_SnIpCommunityListStringRowStatus_Object = MibTableColumn
snIpCommunityListStringRowStatus = _SnIpCommunityListStringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 17, 1, 8),
    _SnIpCommunityListStringRowStatus_Type()
)
snIpCommunityListStringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpCommunityListStringRowStatus.setStatus("mandatory")


class _SnIpCommunityListStringLocalAs_Type(Integer32):
    """Custom type snIpCommunityListStringLocalAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnIpCommunityListStringLocalAs_Type.__name__ = "Integer32"
_SnIpCommunityListStringLocalAs_Object = MibTableColumn
snIpCommunityListStringLocalAs = _SnIpCommunityListStringLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 17, 1, 9),
    _SnIpCommunityListStringLocalAs_Type()
)
snIpCommunityListStringLocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIpCommunityListStringLocalAs.setStatus("mandatory")
_SnRtIpPortIfAddrTable_Object = MibTable
snRtIpPortIfAddrTable = _SnRtIpPortIfAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 18)
)
if mibBuilder.loadTexts:
    snRtIpPortIfAddrTable.setStatus("mandatory")
_SnRtIpPortIfAddrEntry_Object = MibTableRow
snRtIpPortIfAddrEntry = _SnRtIpPortIfAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 18, 1)
)
snRtIpPortIfAddrEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpPortIfAddrInterfaceIndex"),
    (0, "HP-SN-IP-MIB", "snRtIpPortIfAddress"),
)
if mibBuilder.loadTexts:
    snRtIpPortIfAddrEntry.setStatus("mandatory")
_SnRtIpPortIfAddrInterfaceIndex_Type = InterfaceIndex
_SnRtIpPortIfAddrInterfaceIndex_Object = MibTableColumn
snRtIpPortIfAddrInterfaceIndex = _SnRtIpPortIfAddrInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 18, 1, 1),
    _SnRtIpPortIfAddrInterfaceIndex_Type()
)
snRtIpPortIfAddrInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpPortIfAddrInterfaceIndex.setStatus("mandatory")
_SnRtIpPortIfAddress_Type = IpAddress
_SnRtIpPortIfAddress_Object = MibTableColumn
snRtIpPortIfAddress = _SnRtIpPortIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 18, 1, 2),
    _SnRtIpPortIfAddress_Type()
)
snRtIpPortIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpPortIfAddress.setStatus("mandatory")
_SnRtIpPortIfSubnetMask_Type = IpAddress
_SnRtIpPortIfSubnetMask_Object = MibTableColumn
snRtIpPortIfSubnetMask = _SnRtIpPortIfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 18, 1, 3),
    _SnRtIpPortIfSubnetMask_Type()
)
snRtIpPortIfSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortIfSubnetMask.setStatus("mandatory")


class _SnRtIpPortIfAddrType_Type(Integer32):
    """Custom type snRtIpPortIfAddrType based on Integer32"""
    defaultValue = 1

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


_SnRtIpPortIfAddrType_Type.__name__ = "Integer32"
_SnRtIpPortIfAddrType_Object = MibTableColumn
snRtIpPortIfAddrType = _SnRtIpPortIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 18, 1, 4),
    _SnRtIpPortIfAddrType_Type()
)
snRtIpPortIfAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortIfAddrType.setStatus("mandatory")
_SnRtIpPortIfRowStatus_Type = RowSts
_SnRtIpPortIfRowStatus_Object = MibTableColumn
snRtIpPortIfRowStatus = _SnRtIpPortIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 18, 1, 5),
    _SnRtIpPortIfRowStatus_Type()
)
snRtIpPortIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortIfRowStatus.setStatus("mandatory")
_SnRtIpPortIfAccessTable_Object = MibTable
snRtIpPortIfAccessTable = _SnRtIpPortIfAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 19)
)
if mibBuilder.loadTexts:
    snRtIpPortIfAccessTable.setStatus("mandatory")
_SnRtIpPortIfAccessEntry_Object = MibTableRow
snRtIpPortIfAccessEntry = _SnRtIpPortIfAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 19, 1)
)
snRtIpPortIfAccessEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpPortIfAccessInterfaceIndex"),
    (0, "HP-SN-IP-MIB", "snRtIpPortIfAccessDirection"),
)
if mibBuilder.loadTexts:
    snRtIpPortIfAccessEntry.setStatus("mandatory")
_SnRtIpPortIfAccessInterfaceIndex_Type = InterfaceIndex
_SnRtIpPortIfAccessInterfaceIndex_Object = MibTableColumn
snRtIpPortIfAccessInterfaceIndex = _SnRtIpPortIfAccessInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 19, 1, 1),
    _SnRtIpPortIfAccessInterfaceIndex_Type()
)
snRtIpPortIfAccessInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpPortIfAccessInterfaceIndex.setStatus("mandatory")


class _SnRtIpPortIfAccessDirection_Type(Integer32):
    """Custom type snRtIpPortIfAccessDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_SnRtIpPortIfAccessDirection_Type.__name__ = "Integer32"
_SnRtIpPortIfAccessDirection_Object = MibTableColumn
snRtIpPortIfAccessDirection = _SnRtIpPortIfAccessDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 19, 1, 2),
    _SnRtIpPortIfAccessDirection_Type()
)
snRtIpPortIfAccessDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpPortIfAccessDirection.setStatus("mandatory")
_SnRtIpPortIfAccessFilters_Type = OctetString
_SnRtIpPortIfAccessFilters_Object = MibTableColumn
snRtIpPortIfAccessFilters = _SnRtIpPortIfAccessFilters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 19, 1, 3),
    _SnRtIpPortIfAccessFilters_Type()
)
snRtIpPortIfAccessFilters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortIfAccessFilters.setStatus("mandatory")
_SnRtIpPortIfAccessRowStatus_Type = RowSts
_SnRtIpPortIfAccessRowStatus_Object = MibTableColumn
snRtIpPortIfAccessRowStatus = _SnRtIpPortIfAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 19, 1, 4),
    _SnRtIpPortIfAccessRowStatus_Type()
)
snRtIpPortIfAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortIfAccessRowStatus.setStatus("mandatory")
_SnRtIpPortIfConfigTable_Object = MibTable
snRtIpPortIfConfigTable = _SnRtIpPortIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 20)
)
if mibBuilder.loadTexts:
    snRtIpPortIfConfigTable.setStatus("mandatory")
_SnRtIpPortIfConfigEntry_Object = MibTableRow
snRtIpPortIfConfigEntry = _SnRtIpPortIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 20, 1)
)
snRtIpPortIfConfigEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpPortIfConfigInterfaceIndex"),
)
if mibBuilder.loadTexts:
    snRtIpPortIfConfigEntry.setStatus("mandatory")
_SnRtIpPortIfConfigInterfaceIndex_Type = InterfaceIndex
_SnRtIpPortIfConfigInterfaceIndex_Object = MibTableColumn
snRtIpPortIfConfigInterfaceIndex = _SnRtIpPortIfConfigInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 20, 1, 1),
    _SnRtIpPortIfConfigInterfaceIndex_Type()
)
snRtIpPortIfConfigInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpPortIfConfigInterfaceIndex.setStatus("mandatory")


class _SnRtIpPortIfMtu_Type(Integer32):
    """Custom type snRtIpPortIfMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 4470),
    )


_SnRtIpPortIfMtu_Type.__name__ = "Integer32"
_SnRtIpPortIfMtu_Object = MibTableColumn
snRtIpPortIfMtu = _SnRtIpPortIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 20, 1, 2),
    _SnRtIpPortIfMtu_Type()
)
snRtIpPortIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortIfMtu.setStatus("mandatory")


class _SnRtIpPortIfEncap_Type(Integer32):
    """Custom type snRtIpPortIfEncap based on Integer32"""
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
        *(("ethernet", 1),
          ("snap", 2),
          ("hdlc", 3),
          ("ppp", 4),
          ("other", 5))
    )


_SnRtIpPortIfEncap_Type.__name__ = "Integer32"
_SnRtIpPortIfEncap_Object = MibTableColumn
snRtIpPortIfEncap = _SnRtIpPortIfEncap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 20, 1, 3),
    _SnRtIpPortIfEncap_Type()
)
snRtIpPortIfEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortIfEncap.setStatus("mandatory")


class _SnRtIpPortIfMetric_Type(Integer32):
    """Custom type snRtIpPortIfMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SnRtIpPortIfMetric_Type.__name__ = "Integer32"
_SnRtIpPortIfMetric_Object = MibTableColumn
snRtIpPortIfMetric = _SnRtIpPortIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 20, 1, 4),
    _SnRtIpPortIfMetric_Type()
)
snRtIpPortIfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortIfMetric.setStatus("mandatory")


class _SnRtIpPortIfDirBcastFwd_Type(RtrStatus):
    """Custom type snRtIpPortIfDirBcastFwd based on RtrStatus"""
    defaultValue = 1


_SnRtIpPortIfDirBcastFwd_Type.__name__ = "RtrStatus"
_SnRtIpPortIfDirBcastFwd_Object = MibTableColumn
snRtIpPortIfDirBcastFwd = _SnRtIpPortIfDirBcastFwd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2, 20, 1, 5),
    _SnRtIpPortIfDirBcastFwd_Type()
)
snRtIpPortIfDirBcastFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpPortIfDirBcastFwd.setStatus("mandatory")
_SnRtIpRipGeneral_ObjectIdentity = ObjectIdentity
snRtIpRipGeneral = _SnRtIpRipGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 1)
)
_SnRtIpRipEnable_Type = RtrStatus
_SnRtIpRipEnable_Object = MibScalar
snRtIpRipEnable = _SnRtIpRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 1, 1),
    _SnRtIpRipEnable_Type()
)
snRtIpRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipEnable.setStatus("mandatory")


class _SnRtIpRipUpdateTime_Type(Integer32):
    """Custom type snRtIpRipUpdateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SnRtIpRipUpdateTime_Type.__name__ = "Integer32"
_SnRtIpRipUpdateTime_Object = MibScalar
snRtIpRipUpdateTime = _SnRtIpRipUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 1, 2),
    _SnRtIpRipUpdateTime_Type()
)
snRtIpRipUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipUpdateTime.setStatus("mandatory")
_SnRtIpRipRedisEnable_Type = RtrStatus
_SnRtIpRipRedisEnable_Object = MibScalar
snRtIpRipRedisEnable = _SnRtIpRipRedisEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 1, 3),
    _SnRtIpRipRedisEnable_Type()
)
snRtIpRipRedisEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipRedisEnable.setStatus("mandatory")


class _SnRtIpRipRedisDefMetric_Type(Integer32):
    """Custom type snRtIpRipRedisDefMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SnRtIpRipRedisDefMetric_Type.__name__ = "Integer32"
_SnRtIpRipRedisDefMetric_Object = MibScalar
snRtIpRipRedisDefMetric = _SnRtIpRipRedisDefMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 1, 4),
    _SnRtIpRipRedisDefMetric_Type()
)
snRtIpRipRedisDefMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipRedisDefMetric.setStatus("mandatory")
_SnRtIpRipSetAllPortConfig_Type = Integer32
_SnRtIpRipSetAllPortConfig_Object = MibScalar
snRtIpRipSetAllPortConfig = _SnRtIpRipSetAllPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 1, 5),
    _SnRtIpRipSetAllPortConfig_Type()
)
snRtIpRipSetAllPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipSetAllPortConfig.setStatus("mandatory")


class _SnRtIpRipGblFiltList_Type(OctetString):
    """Custom type snRtIpRipGblFiltList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SnRtIpRipGblFiltList_Type.__name__ = "OctetString"
_SnRtIpRipGblFiltList_Object = MibScalar
snRtIpRipGblFiltList = _SnRtIpRipGblFiltList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 1, 6),
    _SnRtIpRipGblFiltList_Type()
)
snRtIpRipGblFiltList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipGblFiltList.setStatus("mandatory")


class _SnRtIpRipFiltOnAllPort_Type(Integer32):
    """Custom type snRtIpRipFiltOnAllPort based on Integer32"""
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
        *(("valid", 1),
          ("deleteAllInBound", 2),
          ("deleteAllOutBound", 3),
          ("addAllInBound", 4),
          ("addAllOutBound", 5))
    )


_SnRtIpRipFiltOnAllPort_Type.__name__ = "Integer32"
_SnRtIpRipFiltOnAllPort_Object = MibScalar
snRtIpRipFiltOnAllPort = _SnRtIpRipFiltOnAllPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 1, 7),
    _SnRtIpRipFiltOnAllPort_Type()
)
snRtIpRipFiltOnAllPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipFiltOnAllPort.setStatus("mandatory")


class _SnRtIpRipDistance_Type(Integer32):
    """Custom type snRtIpRipDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnRtIpRipDistance_Type.__name__ = "Integer32"
_SnRtIpRipDistance_Object = MibScalar
snRtIpRipDistance = _SnRtIpRipDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 1, 8),
    _SnRtIpRipDistance_Type()
)
snRtIpRipDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipDistance.setStatus("mandatory")
_SnRtIpRipPortConfigTable_Object = MibTable
snRtIpRipPortConfigTable = _SnRtIpRipPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 2)
)
if mibBuilder.loadTexts:
    snRtIpRipPortConfigTable.setStatus("deprecated")
_SnRtIpRipPortConfigEntry_Object = MibTableRow
snRtIpRipPortConfigEntry = _SnRtIpRipPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 2, 1)
)
snRtIpRipPortConfigEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpRipPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    snRtIpRipPortConfigEntry.setStatus("deprecated")
_SnRtIpRipPortConfigPortIndex_Type = PortIndex
_SnRtIpRipPortConfigPortIndex_Object = MibTableColumn
snRtIpRipPortConfigPortIndex = _SnRtIpRipPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 2, 1, 1),
    _SnRtIpRipPortConfigPortIndex_Type()
)
snRtIpRipPortConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpRipPortConfigPortIndex.setStatus("deprecated")


class _SnRtIpRipPortVersion_Type(Integer32):
    """Custom type snRtIpRipPortVersion based on Integer32"""
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
        *(("disabled", 0),
          ("v1Only", 1),
          ("v2Only", 2),
          ("v1CompatibleV2", 3))
    )


_SnRtIpRipPortVersion_Type.__name__ = "Integer32"
_SnRtIpRipPortVersion_Object = MibTableColumn
snRtIpRipPortVersion = _SnRtIpRipPortVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 2, 1, 2),
    _SnRtIpRipPortVersion_Type()
)
snRtIpRipPortVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipPortVersion.setStatus("deprecated")
_SnRtIpRipPortPoisonReverse_Type = RtrStatus
_SnRtIpRipPortPoisonReverse_Object = MibTableColumn
snRtIpRipPortPoisonReverse = _SnRtIpRipPortPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 2, 1, 3),
    _SnRtIpRipPortPoisonReverse_Type()
)
snRtIpRipPortPoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipPortPoisonReverse.setStatus("deprecated")


class _SnRtIpRipPortLearnDefault_Type(Integer32):
    """Custom type snRtIpRipPortLearnDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnRtIpRipPortLearnDefault_Type.__name__ = "Integer32"
_SnRtIpRipPortLearnDefault_Object = MibTableColumn
snRtIpRipPortLearnDefault = _SnRtIpRipPortLearnDefault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 2, 1, 4),
    _SnRtIpRipPortLearnDefault_Type()
)
snRtIpRipPortLearnDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipPortLearnDefault.setStatus("deprecated")
_SnRtIpRipRedisTable_Object = MibTable
snRtIpRipRedisTable = _SnRtIpRipRedisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 3)
)
if mibBuilder.loadTexts:
    snRtIpRipRedisTable.setStatus("mandatory")
_SnRtIpRipRedisEntry_Object = MibTableRow
snRtIpRipRedisEntry = _SnRtIpRipRedisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 3, 1)
)
snRtIpRipRedisEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpRipRedisIndex"),
)
if mibBuilder.loadTexts:
    snRtIpRipRedisEntry.setStatus("mandatory")


class _SnRtIpRipRedisIndex_Type(Integer32):
    """Custom type snRtIpRipRedisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SnRtIpRipRedisIndex_Type.__name__ = "Integer32"
_SnRtIpRipRedisIndex_Object = MibTableColumn
snRtIpRipRedisIndex = _SnRtIpRipRedisIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 3, 1, 1),
    _SnRtIpRipRedisIndex_Type()
)
snRtIpRipRedisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpRipRedisIndex.setStatus("mandatory")
_SnRtIpRipRedisAction_Type = Action
_SnRtIpRipRedisAction_Object = MibTableColumn
snRtIpRipRedisAction = _SnRtIpRipRedisAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 3, 1, 2),
    _SnRtIpRipRedisAction_Type()
)
snRtIpRipRedisAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipRedisAction.setStatus("mandatory")


class _SnRtIpRipRedisProtocol_Type(Integer32):
    """Custom type snRtIpRipRedisProtocol based on Integer32"""
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
        *(("other", 1),
          ("all", 2),
          ("static", 3),
          ("ospf", 4),
          ("bgp", 5),
          ("isis", 6))
    )


_SnRtIpRipRedisProtocol_Type.__name__ = "Integer32"
_SnRtIpRipRedisProtocol_Object = MibTableColumn
snRtIpRipRedisProtocol = _SnRtIpRipRedisProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 3, 1, 3),
    _SnRtIpRipRedisProtocol_Type()
)
snRtIpRipRedisProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipRedisProtocol.setStatus("mandatory")
_SnRtIpRipRedisIp_Type = IpAddress
_SnRtIpRipRedisIp_Object = MibTableColumn
snRtIpRipRedisIp = _SnRtIpRipRedisIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 3, 1, 4),
    _SnRtIpRipRedisIp_Type()
)
snRtIpRipRedisIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipRedisIp.setStatus("mandatory")
_SnRtIpRipRedisMask_Type = IpAddress
_SnRtIpRipRedisMask_Object = MibTableColumn
snRtIpRipRedisMask = _SnRtIpRipRedisMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 3, 1, 5),
    _SnRtIpRipRedisMask_Type()
)
snRtIpRipRedisMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipRedisMask.setStatus("mandatory")
_SnRtIpRipRedisMatchMetric_Type = Metric
_SnRtIpRipRedisMatchMetric_Object = MibTableColumn
snRtIpRipRedisMatchMetric = _SnRtIpRipRedisMatchMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 3, 1, 6),
    _SnRtIpRipRedisMatchMetric_Type()
)
snRtIpRipRedisMatchMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipRedisMatchMetric.setStatus("mandatory")


class _SnRtIpRipRedisSetMetric_Type(Integer32):
    """Custom type snRtIpRipRedisSetMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SnRtIpRipRedisSetMetric_Type.__name__ = "Integer32"
_SnRtIpRipRedisSetMetric_Object = MibTableColumn
snRtIpRipRedisSetMetric = _SnRtIpRipRedisSetMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 3, 1, 7),
    _SnRtIpRipRedisSetMetric_Type()
)
snRtIpRipRedisSetMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipRedisSetMetric.setStatus("mandatory")
_SnRtIpRipRedisRowStatus_Type = RowSts
_SnRtIpRipRedisRowStatus_Object = MibTableColumn
snRtIpRipRedisRowStatus = _SnRtIpRipRedisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 3, 1, 8),
    _SnRtIpRipRedisRowStatus_Type()
)
snRtIpRipRedisRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipRedisRowStatus.setStatus("mandatory")
_SnRtIpRipRouteFilterTable_Object = MibTable
snRtIpRipRouteFilterTable = _SnRtIpRipRouteFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 4)
)
if mibBuilder.loadTexts:
    snRtIpRipRouteFilterTable.setStatus("mandatory")
_SnRtIpRipRouteFilterEntry_Object = MibTableRow
snRtIpRipRouteFilterEntry = _SnRtIpRipRouteFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 4, 1)
)
snRtIpRipRouteFilterEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpRipRouteFilterId"),
)
if mibBuilder.loadTexts:
    snRtIpRipRouteFilterEntry.setStatus("mandatory")


class _SnRtIpRipRouteFilterId_Type(Integer32):
    """Custom type snRtIpRipRouteFilterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SnRtIpRipRouteFilterId_Type.__name__ = "Integer32"
_SnRtIpRipRouteFilterId_Object = MibTableColumn
snRtIpRipRouteFilterId = _SnRtIpRipRouteFilterId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 4, 1, 1),
    _SnRtIpRipRouteFilterId_Type()
)
snRtIpRipRouteFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpRipRouteFilterId.setStatus("mandatory")
_SnRtIpRipRouteFilterAction_Type = Action
_SnRtIpRipRouteFilterAction_Object = MibTableColumn
snRtIpRipRouteFilterAction = _SnRtIpRipRouteFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 4, 1, 2),
    _SnRtIpRipRouteFilterAction_Type()
)
snRtIpRipRouteFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipRouteFilterAction.setStatus("mandatory")
_SnRtIpRipRouteFilterIpAddr_Type = IpAddress
_SnRtIpRipRouteFilterIpAddr_Object = MibTableColumn
snRtIpRipRouteFilterIpAddr = _SnRtIpRipRouteFilterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 4, 1, 3),
    _SnRtIpRipRouteFilterIpAddr_Type()
)
snRtIpRipRouteFilterIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipRouteFilterIpAddr.setStatus("mandatory")
_SnRtIpRipRouteFilterSubnetMask_Type = IpAddress
_SnRtIpRipRouteFilterSubnetMask_Object = MibTableColumn
snRtIpRipRouteFilterSubnetMask = _SnRtIpRipRouteFilterSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 4, 1, 4),
    _SnRtIpRipRouteFilterSubnetMask_Type()
)
snRtIpRipRouteFilterSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipRouteFilterSubnetMask.setStatus("mandatory")


class _SnRtIpRipRouteFilterRowStatus_Type(Integer32):
    """Custom type snRtIpRipRouteFilterRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4),
          ("modify", 5))
    )


_SnRtIpRipRouteFilterRowStatus_Type.__name__ = "Integer32"
_SnRtIpRipRouteFilterRowStatus_Object = MibTableColumn
snRtIpRipRouteFilterRowStatus = _SnRtIpRipRouteFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 4, 1, 5),
    _SnRtIpRipRouteFilterRowStatus_Type()
)
snRtIpRipRouteFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipRouteFilterRowStatus.setStatus("mandatory")
_SnRtIpRipNbrFilterTable_Object = MibTable
snRtIpRipNbrFilterTable = _SnRtIpRipNbrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 5)
)
if mibBuilder.loadTexts:
    snRtIpRipNbrFilterTable.setStatus("mandatory")
_SnRtIpRipNbrFilterEntry_Object = MibTableRow
snRtIpRipNbrFilterEntry = _SnRtIpRipNbrFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 5, 1)
)
snRtIpRipNbrFilterEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpRipNbrFilterId"),
)
if mibBuilder.loadTexts:
    snRtIpRipNbrFilterEntry.setStatus("mandatory")


class _SnRtIpRipNbrFilterId_Type(Integer32):
    """Custom type snRtIpRipNbrFilterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SnRtIpRipNbrFilterId_Type.__name__ = "Integer32"
_SnRtIpRipNbrFilterId_Object = MibTableColumn
snRtIpRipNbrFilterId = _SnRtIpRipNbrFilterId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 5, 1, 1),
    _SnRtIpRipNbrFilterId_Type()
)
snRtIpRipNbrFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpRipNbrFilterId.setStatus("mandatory")
_SnRtIpRipNbrFilterAction_Type = Action
_SnRtIpRipNbrFilterAction_Object = MibTableColumn
snRtIpRipNbrFilterAction = _SnRtIpRipNbrFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 5, 1, 2),
    _SnRtIpRipNbrFilterAction_Type()
)
snRtIpRipNbrFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipNbrFilterAction.setStatus("mandatory")
_SnRtIpRipNbrFilterSourceIp_Type = IpAddress
_SnRtIpRipNbrFilterSourceIp_Object = MibTableColumn
snRtIpRipNbrFilterSourceIp = _SnRtIpRipNbrFilterSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 5, 1, 3),
    _SnRtIpRipNbrFilterSourceIp_Type()
)
snRtIpRipNbrFilterSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipNbrFilterSourceIp.setStatus("mandatory")


class _SnRtIpRipNbrFilterRowStatus_Type(Integer32):
    """Custom type snRtIpRipNbrFilterRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4),
          ("modify", 5))
    )


_SnRtIpRipNbrFilterRowStatus_Type.__name__ = "Integer32"
_SnRtIpRipNbrFilterRowStatus_Object = MibTableColumn
snRtIpRipNbrFilterRowStatus = _SnRtIpRipNbrFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 5, 1, 4),
    _SnRtIpRipNbrFilterRowStatus_Type()
)
snRtIpRipNbrFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipNbrFilterRowStatus.setStatus("mandatory")
_SnRtIpRipPortAccessTable_Object = MibTable
snRtIpRipPortAccessTable = _SnRtIpRipPortAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 6)
)
if mibBuilder.loadTexts:
    snRtIpRipPortAccessTable.setStatus("deprecated")
_SnRtIpRipPortAccessEntry_Object = MibTableRow
snRtIpRipPortAccessEntry = _SnRtIpRipPortAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 6, 1)
)
snRtIpRipPortAccessEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpRipPortAccessPort"),
    (0, "HP-SN-IP-MIB", "snRtIpRipPortAccessDir"),
)
if mibBuilder.loadTexts:
    snRtIpRipPortAccessEntry.setStatus("deprecated")
_SnRtIpRipPortAccessPort_Type = PortIndex
_SnRtIpRipPortAccessPort_Object = MibTableColumn
snRtIpRipPortAccessPort = _SnRtIpRipPortAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 6, 1, 1),
    _SnRtIpRipPortAccessPort_Type()
)
snRtIpRipPortAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpRipPortAccessPort.setStatus("deprecated")


class _SnRtIpRipPortAccessDir_Type(Integer32):
    """Custom type snRtIpRipPortAccessDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_SnRtIpRipPortAccessDir_Type.__name__ = "Integer32"
_SnRtIpRipPortAccessDir_Object = MibTableColumn
snRtIpRipPortAccessDir = _SnRtIpRipPortAccessDir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 6, 1, 2),
    _SnRtIpRipPortAccessDir_Type()
)
snRtIpRipPortAccessDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpRipPortAccessDir.setStatus("deprecated")


class _SnRtIpRipPortAccessFilterList_Type(OctetString):
    """Custom type snRtIpRipPortAccessFilterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SnRtIpRipPortAccessFilterList_Type.__name__ = "OctetString"
_SnRtIpRipPortAccessFilterList_Object = MibTableColumn
snRtIpRipPortAccessFilterList = _SnRtIpRipPortAccessFilterList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 6, 1, 3),
    _SnRtIpRipPortAccessFilterList_Type()
)
snRtIpRipPortAccessFilterList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipPortAccessFilterList.setStatus("deprecated")


class _SnRtIpRipPortAccessRowStatus_Type(Integer32):
    """Custom type snRtIpRipPortAccessRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4),
          ("modify", 5))
    )


_SnRtIpRipPortAccessRowStatus_Type.__name__ = "Integer32"
_SnRtIpRipPortAccessRowStatus_Object = MibTableColumn
snRtIpRipPortAccessRowStatus = _SnRtIpRipPortAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 6, 1, 4),
    _SnRtIpRipPortAccessRowStatus_Type()
)
snRtIpRipPortAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipPortAccessRowStatus.setStatus("deprecated")
_SnRtIpRipPortIfConfigTable_Object = MibTable
snRtIpRipPortIfConfigTable = _SnRtIpRipPortIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 7)
)
if mibBuilder.loadTexts:
    snRtIpRipPortIfConfigTable.setStatus("mandatory")
_SnRtIpRipPortIfConfigEntry_Object = MibTableRow
snRtIpRipPortIfConfigEntry = _SnRtIpRipPortIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 7, 1)
)
snRtIpRipPortIfConfigEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpRipPortIfConfigInterfaceIndex"),
)
if mibBuilder.loadTexts:
    snRtIpRipPortIfConfigEntry.setStatus("mandatory")
_SnRtIpRipPortIfConfigInterfaceIndex_Type = InterfaceIndex
_SnRtIpRipPortIfConfigInterfaceIndex_Object = MibTableColumn
snRtIpRipPortIfConfigInterfaceIndex = _SnRtIpRipPortIfConfigInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 7, 1, 1),
    _SnRtIpRipPortIfConfigInterfaceIndex_Type()
)
snRtIpRipPortIfConfigInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpRipPortIfConfigInterfaceIndex.setStatus("mandatory")


class _SnRtIpRipPortIfVersion_Type(Integer32):
    """Custom type snRtIpRipPortIfVersion based on Integer32"""
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
        *(("disabled", 0),
          ("v1Only", 1),
          ("v2Only", 2),
          ("v1CompatibleV2", 3))
    )


_SnRtIpRipPortIfVersion_Type.__name__ = "Integer32"
_SnRtIpRipPortIfVersion_Object = MibTableColumn
snRtIpRipPortIfVersion = _SnRtIpRipPortIfVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 7, 1, 2),
    _SnRtIpRipPortIfVersion_Type()
)
snRtIpRipPortIfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipPortIfVersion.setStatus("mandatory")
_SnRtIpRipPortIfPoisonReverse_Type = RtrStatus
_SnRtIpRipPortIfPoisonReverse_Object = MibTableColumn
snRtIpRipPortIfPoisonReverse = _SnRtIpRipPortIfPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 7, 1, 3),
    _SnRtIpRipPortIfPoisonReverse_Type()
)
snRtIpRipPortIfPoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipPortIfPoisonReverse.setStatus("mandatory")


class _SnRtIpRipPortIfLearnDefault_Type(Integer32):
    """Custom type snRtIpRipPortIfLearnDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnRtIpRipPortIfLearnDefault_Type.__name__ = "Integer32"
_SnRtIpRipPortIfLearnDefault_Object = MibTableColumn
snRtIpRipPortIfLearnDefault = _SnRtIpRipPortIfLearnDefault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 7, 1, 4),
    _SnRtIpRipPortIfLearnDefault_Type()
)
snRtIpRipPortIfLearnDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipPortIfLearnDefault.setStatus("mandatory")
_SnRtIpRipPortIfAccessTable_Object = MibTable
snRtIpRipPortIfAccessTable = _SnRtIpRipPortIfAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 8)
)
if mibBuilder.loadTexts:
    snRtIpRipPortIfAccessTable.setStatus("mandatory")
_SnRtIpRipPortIfAccessEntry_Object = MibTableRow
snRtIpRipPortIfAccessEntry = _SnRtIpRipPortIfAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 8, 1)
)
snRtIpRipPortIfAccessEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snRtIpRipPortIfAccessPort"),
    (0, "HP-SN-IP-MIB", "snRtIpRipPortIfAccessDir"),
)
if mibBuilder.loadTexts:
    snRtIpRipPortIfAccessEntry.setStatus("mandatory")
_SnRtIpRipPortIfAccessPort_Type = InterfaceIndex
_SnRtIpRipPortIfAccessPort_Object = MibTableColumn
snRtIpRipPortIfAccessPort = _SnRtIpRipPortIfAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 8, 1, 1),
    _SnRtIpRipPortIfAccessPort_Type()
)
snRtIpRipPortIfAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpRipPortIfAccessPort.setStatus("mandatory")


class _SnRtIpRipPortIfAccessDir_Type(Integer32):
    """Custom type snRtIpRipPortIfAccessDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_SnRtIpRipPortIfAccessDir_Type.__name__ = "Integer32"
_SnRtIpRipPortIfAccessDir_Object = MibTableColumn
snRtIpRipPortIfAccessDir = _SnRtIpRipPortIfAccessDir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 8, 1, 2),
    _SnRtIpRipPortIfAccessDir_Type()
)
snRtIpRipPortIfAccessDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snRtIpRipPortIfAccessDir.setStatus("mandatory")


class _SnRtIpRipPortIfAccessFilterList_Type(OctetString):
    """Custom type snRtIpRipPortIfAccessFilterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SnRtIpRipPortIfAccessFilterList_Type.__name__ = "OctetString"
_SnRtIpRipPortIfAccessFilterList_Object = MibTableColumn
snRtIpRipPortIfAccessFilterList = _SnRtIpRipPortIfAccessFilterList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 8, 1, 3),
    _SnRtIpRipPortIfAccessFilterList_Type()
)
snRtIpRipPortIfAccessFilterList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipPortIfAccessFilterList.setStatus("mandatory")


class _SnRtIpRipPortIfAccessRowStatus_Type(Integer32):
    """Custom type snRtIpRipPortIfAccessRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4),
          ("modify", 5))
    )


_SnRtIpRipPortIfAccessRowStatus_Type.__name__ = "Integer32"
_SnRtIpRipPortIfAccessRowStatus_Object = MibTableColumn
snRtIpRipPortIfAccessRowStatus = _SnRtIpRipPortIfAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3, 8, 1, 4),
    _SnRtIpRipPortIfAccessRowStatus_Type()
)
snRtIpRipPortIfAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snRtIpRipPortIfAccessRowStatus.setStatus("mandatory")
_SnDvmrpMIBObjects_ObjectIdentity = ObjectIdentity
snDvmrpMIBObjects = _SnDvmrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1)
)


class _SnDvmrpVersion_Type(DisplayString):
    """Custom type snDvmrpVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnDvmrpVersion_Type.__name__ = "DisplayString"
_SnDvmrpVersion_Object = MibScalar
snDvmrpVersion = _SnDvmrpVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 1),
    _SnDvmrpVersion_Type()
)
snDvmrpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVersion.setStatus("mandatory")


class _SnDvmrpEnable_Type(RtrStatus):
    """Custom type snDvmrpEnable based on RtrStatus"""
    defaultValue = 0


_SnDvmrpEnable_Type.__name__ = "RtrStatus"
_SnDvmrpEnable_Object = MibScalar
snDvmrpEnable = _SnDvmrpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 2),
    _SnDvmrpEnable_Type()
)
snDvmrpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpEnable.setStatus("mandatory")
_SnDvmrpGenerationId_Type = Integer32
_SnDvmrpGenerationId_Object = MibScalar
snDvmrpGenerationId = _SnDvmrpGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 3),
    _SnDvmrpGenerationId_Type()
)
snDvmrpGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpGenerationId.setStatus("mandatory")


class _SnDvmrpProbeInterval_Type(Integer32):
    """Custom type snDvmrpProbeInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_SnDvmrpProbeInterval_Type.__name__ = "Integer32"
_SnDvmrpProbeInterval_Object = MibScalar
snDvmrpProbeInterval = _SnDvmrpProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 4),
    _SnDvmrpProbeInterval_Type()
)
snDvmrpProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpProbeInterval.setStatus("mandatory")


class _SnDvmrpReportInterval_Type(Integer32):
    """Custom type snDvmrpReportInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_SnDvmrpReportInterval_Type.__name__ = "Integer32"
_SnDvmrpReportInterval_Object = MibScalar
snDvmrpReportInterval = _SnDvmrpReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 5),
    _SnDvmrpReportInterval_Type()
)
snDvmrpReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpReportInterval.setStatus("mandatory")


class _SnDvmrpTriggerInterval_Type(Integer32):
    """Custom type snDvmrpTriggerInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_SnDvmrpTriggerInterval_Type.__name__ = "Integer32"
_SnDvmrpTriggerInterval_Object = MibScalar
snDvmrpTriggerInterval = _SnDvmrpTriggerInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 6),
    _SnDvmrpTriggerInterval_Type()
)
snDvmrpTriggerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpTriggerInterval.setStatus("mandatory")


class _SnDvmrpNeighborRouterTimeout_Type(Integer32):
    """Custom type snDvmrpNeighborRouterTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 8000),
    )


_SnDvmrpNeighborRouterTimeout_Type.__name__ = "Integer32"
_SnDvmrpNeighborRouterTimeout_Object = MibScalar
snDvmrpNeighborRouterTimeout = _SnDvmrpNeighborRouterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 7),
    _SnDvmrpNeighborRouterTimeout_Type()
)
snDvmrpNeighborRouterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpNeighborRouterTimeout.setStatus("mandatory")


class _SnDvmrpRouteExpireTime_Type(Integer32):
    """Custom type snDvmrpRouteExpireTime based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 4000),
    )


_SnDvmrpRouteExpireTime_Type.__name__ = "Integer32"
_SnDvmrpRouteExpireTime_Object = MibScalar
snDvmrpRouteExpireTime = _SnDvmrpRouteExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 8),
    _SnDvmrpRouteExpireTime_Type()
)
snDvmrpRouteExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpRouteExpireTime.setStatus("mandatory")


class _SnDvmrpRouteDiscardTime_Type(Integer32):
    """Custom type snDvmrpRouteDiscardTime based on Integer32"""
    defaultValue = 340

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 8000),
    )


_SnDvmrpRouteDiscardTime_Type.__name__ = "Integer32"
_SnDvmrpRouteDiscardTime_Object = MibScalar
snDvmrpRouteDiscardTime = _SnDvmrpRouteDiscardTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 9),
    _SnDvmrpRouteDiscardTime_Type()
)
snDvmrpRouteDiscardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpRouteDiscardTime.setStatus("mandatory")


class _SnDvmrpPruneAge_Type(Integer32):
    """Custom type snDvmrpPruneAge based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 3600),
    )


_SnDvmrpPruneAge_Type.__name__ = "Integer32"
_SnDvmrpPruneAge_Object = MibScalar
snDvmrpPruneAge = _SnDvmrpPruneAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 10),
    _SnDvmrpPruneAge_Type()
)
snDvmrpPruneAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpPruneAge.setStatus("mandatory")


class _SnDvmrpGraftRetransmitTime_Type(Integer32):
    """Custom type snDvmrpGraftRetransmitTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_SnDvmrpGraftRetransmitTime_Type.__name__ = "Integer32"
_SnDvmrpGraftRetransmitTime_Object = MibScalar
snDvmrpGraftRetransmitTime = _SnDvmrpGraftRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 11),
    _SnDvmrpGraftRetransmitTime_Type()
)
snDvmrpGraftRetransmitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpGraftRetransmitTime.setStatus("mandatory")
_SnDvmrpDefaultRoute_Type = IpAddress
_SnDvmrpDefaultRoute_Object = MibScalar
snDvmrpDefaultRoute = _SnDvmrpDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 12),
    _SnDvmrpDefaultRoute_Type()
)
snDvmrpDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpDefaultRoute.setStatus("mandatory")
_SnDvmrpVInterfaceTable_Object = MibTable
snDvmrpVInterfaceTable = _SnDvmrpVInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 13)
)
if mibBuilder.loadTexts:
    snDvmrpVInterfaceTable.setStatus("mandatory")
_SnDvmrpVInterfaceEntry_Object = MibTableRow
snDvmrpVInterfaceEntry = _SnDvmrpVInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 13, 1)
)
snDvmrpVInterfaceEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snDvmrpVInterfaceVifIndex"),
)
if mibBuilder.loadTexts:
    snDvmrpVInterfaceEntry.setStatus("mandatory")


class _SnDvmrpVInterfaceVifIndex_Type(Integer32):
    """Custom type snDvmrpVInterfaceVifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SnDvmrpVInterfaceVifIndex_Type.__name__ = "Integer32"
_SnDvmrpVInterfaceVifIndex_Object = MibTableColumn
snDvmrpVInterfaceVifIndex = _SnDvmrpVInterfaceVifIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 13, 1, 1),
    _SnDvmrpVInterfaceVifIndex_Type()
)
snDvmrpVInterfaceVifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVInterfaceVifIndex.setStatus("mandatory")


class _SnDvmrpVInterfaceType_Type(Integer32):
    """Custom type snDvmrpVInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 1),
          ("querier", 2),
          ("subnet", 3))
    )


_SnDvmrpVInterfaceType_Type.__name__ = "Integer32"
_SnDvmrpVInterfaceType_Object = MibTableColumn
snDvmrpVInterfaceType = _SnDvmrpVInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 13, 1, 2),
    _SnDvmrpVInterfaceType_Type()
)
snDvmrpVInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpVInterfaceType.setStatus("mandatory")


class _SnDvmrpVInterfaceOperState_Type(Integer32):
    """Custom type snDvmrpVInterfaceOperState based on Integer32"""
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


_SnDvmrpVInterfaceOperState_Type.__name__ = "Integer32"
_SnDvmrpVInterfaceOperState_Object = MibTableColumn
snDvmrpVInterfaceOperState = _SnDvmrpVInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 13, 1, 3),
    _SnDvmrpVInterfaceOperState_Type()
)
snDvmrpVInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVInterfaceOperState.setStatus("mandatory")
_SnDvmrpVInterfaceLocalAddress_Type = IpAddress
_SnDvmrpVInterfaceLocalAddress_Object = MibTableColumn
snDvmrpVInterfaceLocalAddress = _SnDvmrpVInterfaceLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 13, 1, 4),
    _SnDvmrpVInterfaceLocalAddress_Type()
)
snDvmrpVInterfaceLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpVInterfaceLocalAddress.setStatus("mandatory")
_SnDvmrpVInterfaceRemoteAddress_Type = IpAddress
_SnDvmrpVInterfaceRemoteAddress_Object = MibTableColumn
snDvmrpVInterfaceRemoteAddress = _SnDvmrpVInterfaceRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 13, 1, 5),
    _SnDvmrpVInterfaceRemoteAddress_Type()
)
snDvmrpVInterfaceRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpVInterfaceRemoteAddress.setStatus("mandatory")
_SnDvmrpVInterfaceRemoteSubnetMask_Type = IpAddress
_SnDvmrpVInterfaceRemoteSubnetMask_Object = MibTableColumn
snDvmrpVInterfaceRemoteSubnetMask = _SnDvmrpVInterfaceRemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 13, 1, 6),
    _SnDvmrpVInterfaceRemoteSubnetMask_Type()
)
snDvmrpVInterfaceRemoteSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVInterfaceRemoteSubnetMask.setStatus("mandatory")


class _SnDvmrpVInterfaceMetric_Type(Integer32):
    """Custom type snDvmrpVInterfaceMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SnDvmrpVInterfaceMetric_Type.__name__ = "Integer32"
_SnDvmrpVInterfaceMetric_Object = MibTableColumn
snDvmrpVInterfaceMetric = _SnDvmrpVInterfaceMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 13, 1, 7),
    _SnDvmrpVInterfaceMetric_Type()
)
snDvmrpVInterfaceMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpVInterfaceMetric.setStatus("mandatory")


class _SnDvmrpVInterfaceTtlThreshold_Type(Integer32):
    """Custom type snDvmrpVInterfaceTtlThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_SnDvmrpVInterfaceTtlThreshold_Type.__name__ = "Integer32"
_SnDvmrpVInterfaceTtlThreshold_Object = MibTableColumn
snDvmrpVInterfaceTtlThreshold = _SnDvmrpVInterfaceTtlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 13, 1, 8),
    _SnDvmrpVInterfaceTtlThreshold_Type()
)
snDvmrpVInterfaceTtlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpVInterfaceTtlThreshold.setStatus("mandatory")


class _SnDvmrpVInterfaceAdvertiseLocal_Type(RtrStatus):
    """Custom type snDvmrpVInterfaceAdvertiseLocal based on RtrStatus"""
    defaultValue = 1


_SnDvmrpVInterfaceAdvertiseLocal_Type.__name__ = "RtrStatus"
_SnDvmrpVInterfaceAdvertiseLocal_Object = MibTableColumn
snDvmrpVInterfaceAdvertiseLocal = _SnDvmrpVInterfaceAdvertiseLocal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 13, 1, 9),
    _SnDvmrpVInterfaceAdvertiseLocal_Type()
)
snDvmrpVInterfaceAdvertiseLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpVInterfaceAdvertiseLocal.setStatus("mandatory")


class _SnDvmrpVInterfaceEncapsulation_Type(RtrStatus):
    """Custom type snDvmrpVInterfaceEncapsulation based on RtrStatus"""
    defaultValue = 0


_SnDvmrpVInterfaceEncapsulation_Type.__name__ = "RtrStatus"
_SnDvmrpVInterfaceEncapsulation_Object = MibTableColumn
snDvmrpVInterfaceEncapsulation = _SnDvmrpVInterfaceEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 13, 1, 10),
    _SnDvmrpVInterfaceEncapsulation_Type()
)
snDvmrpVInterfaceEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpVInterfaceEncapsulation.setStatus("mandatory")


class _SnDvmrpVInterfaceStatus_Type(Integer32):
    """Custom type snDvmrpVInterfaceStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4),
          ("modify", 5))
    )


_SnDvmrpVInterfaceStatus_Type.__name__ = "Integer32"
_SnDvmrpVInterfaceStatus_Object = MibTableColumn
snDvmrpVInterfaceStatus = _SnDvmrpVInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 13, 1, 11),
    _SnDvmrpVInterfaceStatus_Type()
)
snDvmrpVInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDvmrpVInterfaceStatus.setStatus("mandatory")
_SnDvmrpNeighborTable_Object = MibTable
snDvmrpNeighborTable = _SnDvmrpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 14)
)
if mibBuilder.loadTexts:
    snDvmrpNeighborTable.setStatus("mandatory")
_SnDvmrpNeighborEntry_Object = MibTableRow
snDvmrpNeighborEntry = _SnDvmrpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 14, 1)
)
snDvmrpNeighborEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snDvmrpNeighborEntryIndex"),
)
if mibBuilder.loadTexts:
    snDvmrpNeighborEntry.setStatus("mandatory")
_SnDvmrpNeighborEntryIndex_Type = Integer32
_SnDvmrpNeighborEntryIndex_Object = MibTableColumn
snDvmrpNeighborEntryIndex = _SnDvmrpNeighborEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 14, 1, 1),
    _SnDvmrpNeighborEntryIndex_Type()
)
snDvmrpNeighborEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpNeighborEntryIndex.setStatus("mandatory")
_SnDvmrpNeighborVifIndex_Type = Integer32
_SnDvmrpNeighborVifIndex_Object = MibTableColumn
snDvmrpNeighborVifIndex = _SnDvmrpNeighborVifIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 14, 1, 2),
    _SnDvmrpNeighborVifIndex_Type()
)
snDvmrpNeighborVifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpNeighborVifIndex.setStatus("mandatory")
_SnDvmrpNeighborAddress_Type = IpAddress
_SnDvmrpNeighborAddress_Object = MibTableColumn
snDvmrpNeighborAddress = _SnDvmrpNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 14, 1, 3),
    _SnDvmrpNeighborAddress_Type()
)
snDvmrpNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpNeighborAddress.setStatus("mandatory")
_SnDvmrpNeighborUpTime_Type = TimeTicks
_SnDvmrpNeighborUpTime_Object = MibTableColumn
snDvmrpNeighborUpTime = _SnDvmrpNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 14, 1, 4),
    _SnDvmrpNeighborUpTime_Type()
)
snDvmrpNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpNeighborUpTime.setStatus("mandatory")
_SnDvmrpNeighborExpiryTime_Type = TimeTicks
_SnDvmrpNeighborExpiryTime_Object = MibTableColumn
snDvmrpNeighborExpiryTime = _SnDvmrpNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 14, 1, 5),
    _SnDvmrpNeighborExpiryTime_Type()
)
snDvmrpNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpNeighborExpiryTime.setStatus("mandatory")
_SnDvmrpNeighborGenerationId_Type = Integer32
_SnDvmrpNeighborGenerationId_Object = MibTableColumn
snDvmrpNeighborGenerationId = _SnDvmrpNeighborGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 14, 1, 6),
    _SnDvmrpNeighborGenerationId_Type()
)
snDvmrpNeighborGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpNeighborGenerationId.setStatus("mandatory")


class _SnDvmrpNeighborMajorVersion_Type(Integer32):
    """Custom type snDvmrpNeighborMajorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnDvmrpNeighborMajorVersion_Type.__name__ = "Integer32"
_SnDvmrpNeighborMajorVersion_Object = MibTableColumn
snDvmrpNeighborMajorVersion = _SnDvmrpNeighborMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 14, 1, 7),
    _SnDvmrpNeighborMajorVersion_Type()
)
snDvmrpNeighborMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpNeighborMajorVersion.setStatus("mandatory")


class _SnDvmrpNeighborMinorVersion_Type(Integer32):
    """Custom type snDvmrpNeighborMinorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnDvmrpNeighborMinorVersion_Type.__name__ = "Integer32"
_SnDvmrpNeighborMinorVersion_Object = MibTableColumn
snDvmrpNeighborMinorVersion = _SnDvmrpNeighborMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 14, 1, 8),
    _SnDvmrpNeighborMinorVersion_Type()
)
snDvmrpNeighborMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpNeighborMinorVersion.setStatus("mandatory")
_SnDvmrpNeighborCapabilities_Type = Integer32
_SnDvmrpNeighborCapabilities_Object = MibTableColumn
snDvmrpNeighborCapabilities = _SnDvmrpNeighborCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 14, 1, 9),
    _SnDvmrpNeighborCapabilities_Type()
)
snDvmrpNeighborCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpNeighborCapabilities.setStatus("mandatory")
_SnDvmrpRouteTable_Object = MibTable
snDvmrpRouteTable = _SnDvmrpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 15)
)
if mibBuilder.loadTexts:
    snDvmrpRouteTable.setStatus("mandatory")
_SnDvmrpRouteEntry_Object = MibTableRow
snDvmrpRouteEntry = _SnDvmrpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 15, 1)
)
snDvmrpRouteEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snDvmrpRouteEntryIndex"),
)
if mibBuilder.loadTexts:
    snDvmrpRouteEntry.setStatus("mandatory")
_SnDvmrpRouteEntryIndex_Type = Integer32
_SnDvmrpRouteEntryIndex_Object = MibTableColumn
snDvmrpRouteEntryIndex = _SnDvmrpRouteEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 15, 1, 1),
    _SnDvmrpRouteEntryIndex_Type()
)
snDvmrpRouteEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpRouteEntryIndex.setStatus("mandatory")
_SnDvmrpRouteSource_Type = IpAddress
_SnDvmrpRouteSource_Object = MibTableColumn
snDvmrpRouteSource = _SnDvmrpRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 15, 1, 2),
    _SnDvmrpRouteSource_Type()
)
snDvmrpRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpRouteSource.setStatus("mandatory")
_SnDvmrpRouteSourceMask_Type = IpAddress
_SnDvmrpRouteSourceMask_Object = MibTableColumn
snDvmrpRouteSourceMask = _SnDvmrpRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 15, 1, 3),
    _SnDvmrpRouteSourceMask_Type()
)
snDvmrpRouteSourceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpRouteSourceMask.setStatus("mandatory")
_SnDvmrpRouteUpstreamNeighbor_Type = IpAddress
_SnDvmrpRouteUpstreamNeighbor_Object = MibTableColumn
snDvmrpRouteUpstreamNeighbor = _SnDvmrpRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 15, 1, 4),
    _SnDvmrpRouteUpstreamNeighbor_Type()
)
snDvmrpRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpRouteUpstreamNeighbor.setStatus("mandatory")
_SnDvmrpRouteVifIndex_Type = Integer32
_SnDvmrpRouteVifIndex_Object = MibTableColumn
snDvmrpRouteVifIndex = _SnDvmrpRouteVifIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 15, 1, 5),
    _SnDvmrpRouteVifIndex_Type()
)
snDvmrpRouteVifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpRouteVifIndex.setStatus("mandatory")
_SnDvmrpRouteMetric_Type = Integer32
_SnDvmrpRouteMetric_Object = MibTableColumn
snDvmrpRouteMetric = _SnDvmrpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 15, 1, 6),
    _SnDvmrpRouteMetric_Type()
)
snDvmrpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpRouteMetric.setStatus("mandatory")
_SnDvmrpRouteExpiryTime_Type = TimeTicks
_SnDvmrpRouteExpiryTime_Object = MibTableColumn
snDvmrpRouteExpiryTime = _SnDvmrpRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 15, 1, 7),
    _SnDvmrpRouteExpiryTime_Type()
)
snDvmrpRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpRouteExpiryTime.setStatus("mandatory")
_SnDvmrpRouteNextHopTable_Object = MibTable
snDvmrpRouteNextHopTable = _SnDvmrpRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 16)
)
if mibBuilder.loadTexts:
    snDvmrpRouteNextHopTable.setStatus("mandatory")
_SnDvmrpRouteNextHopEntry_Object = MibTableRow
snDvmrpRouteNextHopEntry = _SnDvmrpRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 16, 1)
)
snDvmrpRouteNextHopEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snDvmrpRouteNextHopSource"),
    (0, "HP-SN-IP-MIB", "snDvmrpRouteNextHopSourceMask"),
    (0, "HP-SN-IP-MIB", "snDvmrpRouteNextHopVifIndex"),
)
if mibBuilder.loadTexts:
    snDvmrpRouteNextHopEntry.setStatus("mandatory")
_SnDvmrpRouteNextHopSource_Type = IpAddress
_SnDvmrpRouteNextHopSource_Object = MibTableColumn
snDvmrpRouteNextHopSource = _SnDvmrpRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 16, 1, 1),
    _SnDvmrpRouteNextHopSource_Type()
)
snDvmrpRouteNextHopSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpRouteNextHopSource.setStatus("mandatory")
_SnDvmrpRouteNextHopSourceMask_Type = IpAddress
_SnDvmrpRouteNextHopSourceMask_Object = MibTableColumn
snDvmrpRouteNextHopSourceMask = _SnDvmrpRouteNextHopSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 16, 1, 2),
    _SnDvmrpRouteNextHopSourceMask_Type()
)
snDvmrpRouteNextHopSourceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpRouteNextHopSourceMask.setStatus("mandatory")
_SnDvmrpRouteNextHopVifIndex_Type = Integer32
_SnDvmrpRouteNextHopVifIndex_Object = MibTableColumn
snDvmrpRouteNextHopVifIndex = _SnDvmrpRouteNextHopVifIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 16, 1, 3),
    _SnDvmrpRouteNextHopVifIndex_Type()
)
snDvmrpRouteNextHopVifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpRouteNextHopVifIndex.setStatus("mandatory")


class _SnDvmrpRouteNextHopType_Type(Integer32):
    """Custom type snDvmrpRouteNextHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leaf", 1),
          ("branch", 2))
    )


_SnDvmrpRouteNextHopType_Type.__name__ = "Integer32"
_SnDvmrpRouteNextHopType_Object = MibTableColumn
snDvmrpRouteNextHopType = _SnDvmrpRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 16, 1, 4),
    _SnDvmrpRouteNextHopType_Type()
)
snDvmrpRouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpRouteNextHopType.setStatus("mandatory")
_SnDvmrpVIfStatTable_Object = MibTable
snDvmrpVIfStatTable = _SnDvmrpVIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17)
)
if mibBuilder.loadTexts:
    snDvmrpVIfStatTable.setStatus("mandatory")
_SnDvmrpVIfStatEntry_Object = MibTableRow
snDvmrpVIfStatEntry = _SnDvmrpVIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1)
)
snDvmrpVIfStatEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snDvmrpVIfStatVifIndex"),
)
if mibBuilder.loadTexts:
    snDvmrpVIfStatEntry.setStatus("mandatory")


class _SnDvmrpVIfStatVifIndex_Type(Integer32):
    """Custom type snDvmrpVIfStatVifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnDvmrpVIfStatVifIndex_Type.__name__ = "Integer32"
_SnDvmrpVIfStatVifIndex_Object = MibTableColumn
snDvmrpVIfStatVifIndex = _SnDvmrpVIfStatVifIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 1),
    _SnDvmrpVIfStatVifIndex_Type()
)
snDvmrpVIfStatVifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatVifIndex.setStatus("mandatory")
_SnDvmrpVIfStatInPkts_Type = Counter32
_SnDvmrpVIfStatInPkts_Object = MibTableColumn
snDvmrpVIfStatInPkts = _SnDvmrpVIfStatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 2),
    _SnDvmrpVIfStatInPkts_Type()
)
snDvmrpVIfStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatInPkts.setStatus("mandatory")
_SnDvmrpVIfStatOutPkts_Type = Counter32
_SnDvmrpVIfStatOutPkts_Object = MibTableColumn
snDvmrpVIfStatOutPkts = _SnDvmrpVIfStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 3),
    _SnDvmrpVIfStatOutPkts_Type()
)
snDvmrpVIfStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatOutPkts.setStatus("mandatory")
_SnDvmrpVIfStatInOctets_Type = Counter32
_SnDvmrpVIfStatInOctets_Object = MibTableColumn
snDvmrpVIfStatInOctets = _SnDvmrpVIfStatInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 4),
    _SnDvmrpVIfStatInOctets_Type()
)
snDvmrpVIfStatInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatInOctets.setStatus("mandatory")
_SnDvmrpVIfStatOutOctets_Type = Counter32
_SnDvmrpVIfStatOutOctets_Object = MibTableColumn
snDvmrpVIfStatOutOctets = _SnDvmrpVIfStatOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 5),
    _SnDvmrpVIfStatOutOctets_Type()
)
snDvmrpVIfStatOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatOutOctets.setStatus("mandatory")
_SnDvmrpVIfStatInProbePkts_Type = Counter32
_SnDvmrpVIfStatInProbePkts_Object = MibTableColumn
snDvmrpVIfStatInProbePkts = _SnDvmrpVIfStatInProbePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 6),
    _SnDvmrpVIfStatInProbePkts_Type()
)
snDvmrpVIfStatInProbePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatInProbePkts.setStatus("mandatory")
_SnDvmrpVIfStatOutProbePkts_Type = Counter32
_SnDvmrpVIfStatOutProbePkts_Object = MibTableColumn
snDvmrpVIfStatOutProbePkts = _SnDvmrpVIfStatOutProbePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 7),
    _SnDvmrpVIfStatOutProbePkts_Type()
)
snDvmrpVIfStatOutProbePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatOutProbePkts.setStatus("mandatory")
_SnDvmrpVIfStatDiscardProbePkts_Type = Counter32
_SnDvmrpVIfStatDiscardProbePkts_Object = MibTableColumn
snDvmrpVIfStatDiscardProbePkts = _SnDvmrpVIfStatDiscardProbePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 8),
    _SnDvmrpVIfStatDiscardProbePkts_Type()
)
snDvmrpVIfStatDiscardProbePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatDiscardProbePkts.setStatus("mandatory")
_SnDvmrpVIfStatInRtUpdatePkts_Type = Counter32
_SnDvmrpVIfStatInRtUpdatePkts_Object = MibTableColumn
snDvmrpVIfStatInRtUpdatePkts = _SnDvmrpVIfStatInRtUpdatePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 9),
    _SnDvmrpVIfStatInRtUpdatePkts_Type()
)
snDvmrpVIfStatInRtUpdatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatInRtUpdatePkts.setStatus("mandatory")
_SnDvmrpVIfStatOutRtUpdatePkts_Type = Counter32
_SnDvmrpVIfStatOutRtUpdatePkts_Object = MibTableColumn
snDvmrpVIfStatOutRtUpdatePkts = _SnDvmrpVIfStatOutRtUpdatePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 10),
    _SnDvmrpVIfStatOutRtUpdatePkts_Type()
)
snDvmrpVIfStatOutRtUpdatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatOutRtUpdatePkts.setStatus("mandatory")
_SnDvmrpVIfStatDiscardRtUpdatePkts_Type = Counter32
_SnDvmrpVIfStatDiscardRtUpdatePkts_Object = MibTableColumn
snDvmrpVIfStatDiscardRtUpdatePkts = _SnDvmrpVIfStatDiscardRtUpdatePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 11),
    _SnDvmrpVIfStatDiscardRtUpdatePkts_Type()
)
snDvmrpVIfStatDiscardRtUpdatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatDiscardRtUpdatePkts.setStatus("mandatory")
_SnDvmrpVIfStatInGraftPkts_Type = Counter32
_SnDvmrpVIfStatInGraftPkts_Object = MibTableColumn
snDvmrpVIfStatInGraftPkts = _SnDvmrpVIfStatInGraftPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 12),
    _SnDvmrpVIfStatInGraftPkts_Type()
)
snDvmrpVIfStatInGraftPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatInGraftPkts.setStatus("mandatory")
_SnDvmrpVIfStatOutGraftPkts_Type = Counter32
_SnDvmrpVIfStatOutGraftPkts_Object = MibTableColumn
snDvmrpVIfStatOutGraftPkts = _SnDvmrpVIfStatOutGraftPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 13),
    _SnDvmrpVIfStatOutGraftPkts_Type()
)
snDvmrpVIfStatOutGraftPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatOutGraftPkts.setStatus("mandatory")
_SnDvmrpVIfStatDiscardGraftPkts_Type = Counter32
_SnDvmrpVIfStatDiscardGraftPkts_Object = MibTableColumn
snDvmrpVIfStatDiscardGraftPkts = _SnDvmrpVIfStatDiscardGraftPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 14),
    _SnDvmrpVIfStatDiscardGraftPkts_Type()
)
snDvmrpVIfStatDiscardGraftPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatDiscardGraftPkts.setStatus("mandatory")
_SnDvmrpVIfStatInGraftAckPkts_Type = Counter32
_SnDvmrpVIfStatInGraftAckPkts_Object = MibTableColumn
snDvmrpVIfStatInGraftAckPkts = _SnDvmrpVIfStatInGraftAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 15),
    _SnDvmrpVIfStatInGraftAckPkts_Type()
)
snDvmrpVIfStatInGraftAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatInGraftAckPkts.setStatus("mandatory")
_SnDvmrpVIfStatOutGraftAckPkts_Type = Counter32
_SnDvmrpVIfStatOutGraftAckPkts_Object = MibTableColumn
snDvmrpVIfStatOutGraftAckPkts = _SnDvmrpVIfStatOutGraftAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 16),
    _SnDvmrpVIfStatOutGraftAckPkts_Type()
)
snDvmrpVIfStatOutGraftAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatOutGraftAckPkts.setStatus("mandatory")
_SnDvmrpVIfStatDiscardGraftAckPkts_Type = Counter32
_SnDvmrpVIfStatDiscardGraftAckPkts_Object = MibTableColumn
snDvmrpVIfStatDiscardGraftAckPkts = _SnDvmrpVIfStatDiscardGraftAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 17),
    _SnDvmrpVIfStatDiscardGraftAckPkts_Type()
)
snDvmrpVIfStatDiscardGraftAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatDiscardGraftAckPkts.setStatus("mandatory")
_SnDvmrpVIfStatInPrunePkts_Type = Counter32
_SnDvmrpVIfStatInPrunePkts_Object = MibTableColumn
snDvmrpVIfStatInPrunePkts = _SnDvmrpVIfStatInPrunePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 18),
    _SnDvmrpVIfStatInPrunePkts_Type()
)
snDvmrpVIfStatInPrunePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatInPrunePkts.setStatus("mandatory")
_SnDvmrpVIfStatOutPrunePkts_Type = Counter32
_SnDvmrpVIfStatOutPrunePkts_Object = MibTableColumn
snDvmrpVIfStatOutPrunePkts = _SnDvmrpVIfStatOutPrunePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 19),
    _SnDvmrpVIfStatOutPrunePkts_Type()
)
snDvmrpVIfStatOutPrunePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatOutPrunePkts.setStatus("mandatory")
_SnDvmrpVIfStatDiscardPrunePkts_Type = Counter32
_SnDvmrpVIfStatDiscardPrunePkts_Object = MibTableColumn
snDvmrpVIfStatDiscardPrunePkts = _SnDvmrpVIfStatDiscardPrunePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5, 1, 17, 1, 20),
    _SnDvmrpVIfStatDiscardPrunePkts_Type()
)
snDvmrpVIfStatDiscardPrunePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDvmrpVIfStatDiscardPrunePkts.setStatus("mandatory")
_SnFsrpGlobal_ObjectIdentity = ObjectIdentity
snFsrpGlobal = _SnFsrpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 1)
)


class _SnFsrpGroupOperMode_Type(Integer32):
    """Custom type snFsrpGroupOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnFsrpGroupOperMode_Type.__name__ = "Integer32"
_SnFsrpGroupOperMode_Object = MibScalar
snFsrpGroupOperMode = _SnFsrpGroupOperMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 1, 1),
    _SnFsrpGroupOperMode_Type()
)
snFsrpGroupOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFsrpGroupOperMode.setStatus("mandatory")


class _SnFsrpIfStateChangeTrap_Type(Integer32):
    """Custom type snFsrpIfStateChangeTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnFsrpIfStateChangeTrap_Type.__name__ = "Integer32"
_SnFsrpIfStateChangeTrap_Object = MibScalar
snFsrpIfStateChangeTrap = _SnFsrpIfStateChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 1, 2),
    _SnFsrpIfStateChangeTrap_Type()
)
snFsrpIfStateChangeTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFsrpIfStateChangeTrap.setStatus("mandatory")
_SnFsrpIntf_ObjectIdentity = ObjectIdentity
snFsrpIntf = _SnFsrpIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2)
)
_SnFsrpIfTable_Object = MibTable
snFsrpIfTable = _SnFsrpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    snFsrpIfTable.setStatus("mandatory")
_SnFsrpIfEntry_Object = MibTableRow
snFsrpIfEntry = _SnFsrpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2, 1, 1)
)
snFsrpIfEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snFsrpIfPort"),
    (0, "HP-SN-IP-MIB", "snFsrpIfIpAddress"),
)
if mibBuilder.loadTexts:
    snFsrpIfEntry.setStatus("mandatory")
_SnFsrpIfPort_Type = Integer32
_SnFsrpIfPort_Object = MibTableColumn
snFsrpIfPort = _SnFsrpIfPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2, 1, 1, 1),
    _SnFsrpIfPort_Type()
)
snFsrpIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFsrpIfPort.setStatus("mandatory")
_SnFsrpIfIpAddress_Type = IpAddress
_SnFsrpIfIpAddress_Object = MibTableColumn
snFsrpIfIpAddress = _SnFsrpIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2, 1, 1, 2),
    _SnFsrpIfIpAddress_Type()
)
snFsrpIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFsrpIfIpAddress.setStatus("mandatory")
_SnFsrpIfVirRtrIpAddr_Type = IpAddress
_SnFsrpIfVirRtrIpAddr_Object = MibTableColumn
snFsrpIfVirRtrIpAddr = _SnFsrpIfVirRtrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2, 1, 1, 3),
    _SnFsrpIfVirRtrIpAddr_Type()
)
snFsrpIfVirRtrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFsrpIfVirRtrIpAddr.setStatus("mandatory")
_SnFsrpIfOtherRtrIpAddr_Type = IpAddress
_SnFsrpIfOtherRtrIpAddr_Object = MibTableColumn
snFsrpIfOtherRtrIpAddr = _SnFsrpIfOtherRtrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2, 1, 1, 4),
    _SnFsrpIfOtherRtrIpAddr_Type()
)
snFsrpIfOtherRtrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFsrpIfOtherRtrIpAddr.setStatus("mandatory")


class _SnFsrpIfPreferLevel_Type(Integer32):
    """Custom type snFsrpIfPreferLevel based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnFsrpIfPreferLevel_Type.__name__ = "Integer32"
_SnFsrpIfPreferLevel_Object = MibTableColumn
snFsrpIfPreferLevel = _SnFsrpIfPreferLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2, 1, 1, 5),
    _SnFsrpIfPreferLevel_Type()
)
snFsrpIfPreferLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFsrpIfPreferLevel.setStatus("mandatory")


class _SnFsrpIfTrackPortMask_Type(PortMask):
    """Custom type snFsrpIfTrackPortMask based on PortMask"""
    defaultValue = 0


_SnFsrpIfTrackPortMask_Type.__name__ = "PortMask"
_SnFsrpIfTrackPortMask_Object = MibTableColumn
snFsrpIfTrackPortMask = _SnFsrpIfTrackPortMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2, 1, 1, 6),
    _SnFsrpIfTrackPortMask_Type()
)
snFsrpIfTrackPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFsrpIfTrackPortMask.setStatus("deprecated")


class _SnFsrpIfRowStatus_Type(Integer32):
    """Custom type snFsrpIfRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4),
          ("modify", 5))
    )


_SnFsrpIfRowStatus_Type.__name__ = "Integer32"
_SnFsrpIfRowStatus_Object = MibTableColumn
snFsrpIfRowStatus = _SnFsrpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2, 1, 1, 7),
    _SnFsrpIfRowStatus_Type()
)
snFsrpIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFsrpIfRowStatus.setStatus("mandatory")


class _SnFsrpIfState_Type(Integer32):
    """Custom type snFsrpIfState based on Integer32"""
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
        *(("init", 0),
          ("negotiating", 1),
          ("standby", 2),
          ("active", 3))
    )


_SnFsrpIfState_Type.__name__ = "Integer32"
_SnFsrpIfState_Object = MibTableColumn
snFsrpIfState = _SnFsrpIfState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2, 1, 1, 8),
    _SnFsrpIfState_Type()
)
snFsrpIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snFsrpIfState.setStatus("mandatory")


class _SnFsrpIfKeepAliveTime_Type(Integer32):
    """Custom type snFsrpIfKeepAliveTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SnFsrpIfKeepAliveTime_Type.__name__ = "Integer32"
_SnFsrpIfKeepAliveTime_Object = MibTableColumn
snFsrpIfKeepAliveTime = _SnFsrpIfKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2, 1, 1, 9),
    _SnFsrpIfKeepAliveTime_Type()
)
snFsrpIfKeepAliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFsrpIfKeepAliveTime.setStatus("mandatory")


class _SnFsrpIfRouterDeadTime_Type(Integer32):
    """Custom type snFsrpIfRouterDeadTime based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
    )


_SnFsrpIfRouterDeadTime_Type.__name__ = "Integer32"
_SnFsrpIfRouterDeadTime_Object = MibTableColumn
snFsrpIfRouterDeadTime = _SnFsrpIfRouterDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2, 1, 1, 10),
    _SnFsrpIfRouterDeadTime_Type()
)
snFsrpIfRouterDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFsrpIfRouterDeadTime.setStatus("mandatory")


class _SnFsrpIfChassisTrackPortMask_Type(OctetString):
    """Custom type snFsrpIfChassisTrackPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_SnFsrpIfChassisTrackPortMask_Type.__name__ = "OctetString"
_SnFsrpIfChassisTrackPortMask_Object = MibTableColumn
snFsrpIfChassisTrackPortMask = _SnFsrpIfChassisTrackPortMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2, 1, 1, 11),
    _SnFsrpIfChassisTrackPortMask_Type()
)
snFsrpIfChassisTrackPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFsrpIfChassisTrackPortMask.setStatus("deprecated")
_SnFsrpIfTrackPortList_Type = OctetString
_SnFsrpIfTrackPortList_Object = MibTableColumn
snFsrpIfTrackPortList = _SnFsrpIfTrackPortList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7, 2, 1, 1, 12),
    _SnFsrpIfTrackPortList_Type()
)
snFsrpIfTrackPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snFsrpIfTrackPortList.setStatus("mandatory")
_SnGblRtGeneral_ObjectIdentity = ObjectIdentity
snGblRtGeneral = _SnGblRtGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 8, 1)
)
_SnGblRtRouteOnly_Type = RtrStatus
_SnGblRtRouteOnly_Object = MibScalar
snGblRtRouteOnly = _SnGblRtRouteOnly_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 8, 1, 1),
    _SnGblRtRouteOnly_Type()
)
snGblRtRouteOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snGblRtRouteOnly.setStatus("mandatory")
_SnPimMIBObjects_ObjectIdentity = ObjectIdentity
snPimMIBObjects = _SnPimMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1)
)


class _SnPimEnable_Type(RtrStatus):
    """Custom type snPimEnable based on RtrStatus"""
    defaultValue = 0


_SnPimEnable_Type.__name__ = "RtrStatus"
_SnPimEnable_Object = MibScalar
snPimEnable = _SnPimEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 1),
    _SnPimEnable_Type()
)
snPimEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimEnable.setStatus("mandatory")


class _SnPimNeighborRouterTimeout_Type(Integer32):
    """Custom type snPimNeighborRouterTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 8000),
    )


_SnPimNeighborRouterTimeout_Type.__name__ = "Integer32"
_SnPimNeighborRouterTimeout_Object = MibScalar
snPimNeighborRouterTimeout = _SnPimNeighborRouterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 2),
    _SnPimNeighborRouterTimeout_Type()
)
snPimNeighborRouterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimNeighborRouterTimeout.setStatus("mandatory")


class _SnPimHelloTime_Type(Integer32):
    """Custom type snPimHelloTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_SnPimHelloTime_Type.__name__ = "Integer32"
_SnPimHelloTime_Object = MibScalar
snPimHelloTime = _SnPimHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 3),
    _SnPimHelloTime_Type()
)
snPimHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimHelloTime.setStatus("mandatory")


class _SnPimPruneTime_Type(Integer32):
    """Custom type snPimPruneTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_SnPimPruneTime_Type.__name__ = "Integer32"
_SnPimPruneTime_Object = MibScalar
snPimPruneTime = _SnPimPruneTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 4),
    _SnPimPruneTime_Type()
)
snPimPruneTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimPruneTime.setStatus("mandatory")


class _SnPimGraftRetransmitTime_Type(Integer32):
    """Custom type snPimGraftRetransmitTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_SnPimGraftRetransmitTime_Type.__name__ = "Integer32"
_SnPimGraftRetransmitTime_Object = MibScalar
snPimGraftRetransmitTime = _SnPimGraftRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 5),
    _SnPimGraftRetransmitTime_Type()
)
snPimGraftRetransmitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimGraftRetransmitTime.setStatus("mandatory")


class _SnPimInactivityTime_Type(Integer32):
    """Custom type snPimInactivityTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_SnPimInactivityTime_Type.__name__ = "Integer32"
_SnPimInactivityTime_Object = MibScalar
snPimInactivityTime = _SnPimInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 6),
    _SnPimInactivityTime_Type()
)
snPimInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimInactivityTime.setStatus("mandatory")
_SnPimVInterfaceTable_Object = MibTable
snPimVInterfaceTable = _SnPimVInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 7)
)
if mibBuilder.loadTexts:
    snPimVInterfaceTable.setStatus("mandatory")
_SnPimVInterfaceEntry_Object = MibTableRow
snPimVInterfaceEntry = _SnPimVInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 7, 1)
)
snPimVInterfaceEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snPimVInterfaceVifIndex"),
)
if mibBuilder.loadTexts:
    snPimVInterfaceEntry.setStatus("mandatory")


class _SnPimVInterfaceVifIndex_Type(Integer32):
    """Custom type snPimVInterfaceVifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SnPimVInterfaceVifIndex_Type.__name__ = "Integer32"
_SnPimVInterfaceVifIndex_Object = MibTableColumn
snPimVInterfaceVifIndex = _SnPimVInterfaceVifIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 7, 1, 1),
    _SnPimVInterfaceVifIndex_Type()
)
snPimVInterfaceVifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVInterfaceVifIndex.setStatus("mandatory")


class _SnPimVInterfaceType_Type(Integer32):
    """Custom type snPimVInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 1),
          ("subnet", 2))
    )


_SnPimVInterfaceType_Type.__name__ = "Integer32"
_SnPimVInterfaceType_Object = MibTableColumn
snPimVInterfaceType = _SnPimVInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 7, 1, 2),
    _SnPimVInterfaceType_Type()
)
snPimVInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimVInterfaceType.setStatus("mandatory")
_SnPimVInterfaceLocalAddress_Type = IpAddress
_SnPimVInterfaceLocalAddress_Object = MibTableColumn
snPimVInterfaceLocalAddress = _SnPimVInterfaceLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 7, 1, 3),
    _SnPimVInterfaceLocalAddress_Type()
)
snPimVInterfaceLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimVInterfaceLocalAddress.setStatus("mandatory")
_SnPimVInterfaceLocalSubnetMask_Type = IpAddress
_SnPimVInterfaceLocalSubnetMask_Object = MibTableColumn
snPimVInterfaceLocalSubnetMask = _SnPimVInterfaceLocalSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 7, 1, 4),
    _SnPimVInterfaceLocalSubnetMask_Type()
)
snPimVInterfaceLocalSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVInterfaceLocalSubnetMask.setStatus("mandatory")
_SnPimVInterfaceRemoteAddress_Type = IpAddress
_SnPimVInterfaceRemoteAddress_Object = MibTableColumn
snPimVInterfaceRemoteAddress = _SnPimVInterfaceRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 7, 1, 5),
    _SnPimVInterfaceRemoteAddress_Type()
)
snPimVInterfaceRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimVInterfaceRemoteAddress.setStatus("mandatory")
_SnPimVInterfaceDR_Type = IpAddress
_SnPimVInterfaceDR_Object = MibTableColumn
snPimVInterfaceDR = _SnPimVInterfaceDR_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 7, 1, 6),
    _SnPimVInterfaceDR_Type()
)
snPimVInterfaceDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVInterfaceDR.setStatus("mandatory")


class _SnPimVInterfaceTtlThreshold_Type(Integer32):
    """Custom type snPimVInterfaceTtlThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SnPimVInterfaceTtlThreshold_Type.__name__ = "Integer32"
_SnPimVInterfaceTtlThreshold_Object = MibTableColumn
snPimVInterfaceTtlThreshold = _SnPimVInterfaceTtlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 7, 1, 7),
    _SnPimVInterfaceTtlThreshold_Type()
)
snPimVInterfaceTtlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimVInterfaceTtlThreshold.setStatus("mandatory")


class _SnPimVInterfaceStatus_Type(Integer32):
    """Custom type snPimVInterfaceStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4),
          ("modify", 5))
    )


_SnPimVInterfaceStatus_Type.__name__ = "Integer32"
_SnPimVInterfaceStatus_Object = MibTableColumn
snPimVInterfaceStatus = _SnPimVInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 7, 1, 8),
    _SnPimVInterfaceStatus_Type()
)
snPimVInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimVInterfaceStatus.setStatus("mandatory")


class _SnPimVInterfaceMode_Type(Integer32):
    """Custom type snPimVInterfaceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("sparse", 2))
    )


_SnPimVInterfaceMode_Type.__name__ = "Integer32"
_SnPimVInterfaceMode_Object = MibTableColumn
snPimVInterfaceMode = _SnPimVInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 7, 1, 9),
    _SnPimVInterfaceMode_Type()
)
snPimVInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimVInterfaceMode.setStatus("mandatory")
_SnPimNeighborTable_Object = MibTable
snPimNeighborTable = _SnPimNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 8)
)
if mibBuilder.loadTexts:
    snPimNeighborTable.setStatus("mandatory")
_SnPimNeighborEntry_Object = MibTableRow
snPimNeighborEntry = _SnPimNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 8, 1)
)
snPimNeighborEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snPimNeighborEntryIndex"),
)
if mibBuilder.loadTexts:
    snPimNeighborEntry.setStatus("mandatory")
_SnPimNeighborEntryIndex_Type = Integer32
_SnPimNeighborEntryIndex_Object = MibTableColumn
snPimNeighborEntryIndex = _SnPimNeighborEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 8, 1, 1),
    _SnPimNeighborEntryIndex_Type()
)
snPimNeighborEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimNeighborEntryIndex.setStatus("mandatory")
_SnPimNeighborVifIndex_Type = Integer32
_SnPimNeighborVifIndex_Object = MibTableColumn
snPimNeighborVifIndex = _SnPimNeighborVifIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 8, 1, 2),
    _SnPimNeighborVifIndex_Type()
)
snPimNeighborVifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimNeighborVifIndex.setStatus("mandatory")
_SnPimNeighborAddress_Type = IpAddress
_SnPimNeighborAddress_Object = MibTableColumn
snPimNeighborAddress = _SnPimNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 8, 1, 3),
    _SnPimNeighborAddress_Type()
)
snPimNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimNeighborAddress.setStatus("mandatory")
_SnPimNeighborUpTime_Type = TimeTicks
_SnPimNeighborUpTime_Object = MibTableColumn
snPimNeighborUpTime = _SnPimNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 8, 1, 4),
    _SnPimNeighborUpTime_Type()
)
snPimNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimNeighborUpTime.setStatus("mandatory")
_SnPimNeighborExpiryTime_Type = TimeTicks
_SnPimNeighborExpiryTime_Object = MibTableColumn
snPimNeighborExpiryTime = _SnPimNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 8, 1, 5),
    _SnPimNeighborExpiryTime_Type()
)
snPimNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimNeighborExpiryTime.setStatus("mandatory")
_SnPimVIfStatTable_Object = MibTable
snPimVIfStatTable = _SnPimVIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9)
)
if mibBuilder.loadTexts:
    snPimVIfStatTable.setStatus("mandatory")
_SnPimVIfStatEntry_Object = MibTableRow
snPimVIfStatEntry = _SnPimVIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1)
)
snPimVIfStatEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snPimVIfStatVifIndex"),
)
if mibBuilder.loadTexts:
    snPimVIfStatEntry.setStatus("mandatory")


class _SnPimVIfStatVifIndex_Type(Integer32):
    """Custom type snPimVIfStatVifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SnPimVIfStatVifIndex_Type.__name__ = "Integer32"
_SnPimVIfStatVifIndex_Object = MibTableColumn
snPimVIfStatVifIndex = _SnPimVIfStatVifIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 1),
    _SnPimVIfStatVifIndex_Type()
)
snPimVIfStatVifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatVifIndex.setStatus("mandatory")
_SnPimVIfStatInJoinPkts_Type = Counter32
_SnPimVIfStatInJoinPkts_Object = MibTableColumn
snPimVIfStatInJoinPkts = _SnPimVIfStatInJoinPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 2),
    _SnPimVIfStatInJoinPkts_Type()
)
snPimVIfStatInJoinPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatInJoinPkts.setStatus("mandatory")
_SnPimVIfStatOutJoinPkts_Type = Counter32
_SnPimVIfStatOutJoinPkts_Object = MibTableColumn
snPimVIfStatOutJoinPkts = _SnPimVIfStatOutJoinPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 3),
    _SnPimVIfStatOutJoinPkts_Type()
)
snPimVIfStatOutJoinPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatOutJoinPkts.setStatus("mandatory")
_SnPimVIfStatDiscardJoinPkts_Type = Counter32
_SnPimVIfStatDiscardJoinPkts_Object = MibTableColumn
snPimVIfStatDiscardJoinPkts = _SnPimVIfStatDiscardJoinPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 4),
    _SnPimVIfStatDiscardJoinPkts_Type()
)
snPimVIfStatDiscardJoinPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatDiscardJoinPkts.setStatus("mandatory")
_SnPimVIfStatInPrunePkts_Type = Counter32
_SnPimVIfStatInPrunePkts_Object = MibTableColumn
snPimVIfStatInPrunePkts = _SnPimVIfStatInPrunePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 5),
    _SnPimVIfStatInPrunePkts_Type()
)
snPimVIfStatInPrunePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatInPrunePkts.setStatus("mandatory")
_SnPimVIfStatOutPrunePkts_Type = Counter32
_SnPimVIfStatOutPrunePkts_Object = MibTableColumn
snPimVIfStatOutPrunePkts = _SnPimVIfStatOutPrunePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 6),
    _SnPimVIfStatOutPrunePkts_Type()
)
snPimVIfStatOutPrunePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatOutPrunePkts.setStatus("mandatory")
_SnPimVIfStatDiscardPrunePkts_Type = Counter32
_SnPimVIfStatDiscardPrunePkts_Object = MibTableColumn
snPimVIfStatDiscardPrunePkts = _SnPimVIfStatDiscardPrunePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 7),
    _SnPimVIfStatDiscardPrunePkts_Type()
)
snPimVIfStatDiscardPrunePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatDiscardPrunePkts.setStatus("mandatory")
_SnPimVIfStatInAssertPkts_Type = Counter32
_SnPimVIfStatInAssertPkts_Object = MibTableColumn
snPimVIfStatInAssertPkts = _SnPimVIfStatInAssertPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 8),
    _SnPimVIfStatInAssertPkts_Type()
)
snPimVIfStatInAssertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatInAssertPkts.setStatus("mandatory")
_SnPimVIfStatOutAssertPkts_Type = Counter32
_SnPimVIfStatOutAssertPkts_Object = MibTableColumn
snPimVIfStatOutAssertPkts = _SnPimVIfStatOutAssertPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 9),
    _SnPimVIfStatOutAssertPkts_Type()
)
snPimVIfStatOutAssertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatOutAssertPkts.setStatus("mandatory")
_SnPimVIfStatDiscardAssertPkts_Type = Counter32
_SnPimVIfStatDiscardAssertPkts_Object = MibTableColumn
snPimVIfStatDiscardAssertPkts = _SnPimVIfStatDiscardAssertPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 10),
    _SnPimVIfStatDiscardAssertPkts_Type()
)
snPimVIfStatDiscardAssertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatDiscardAssertPkts.setStatus("mandatory")
_SnPimVIfStatInHelloPkts_Type = Counter32
_SnPimVIfStatInHelloPkts_Object = MibTableColumn
snPimVIfStatInHelloPkts = _SnPimVIfStatInHelloPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 11),
    _SnPimVIfStatInHelloPkts_Type()
)
snPimVIfStatInHelloPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatInHelloPkts.setStatus("mandatory")
_SnPimVIfStatOutHelloPkts_Type = Counter32
_SnPimVIfStatOutHelloPkts_Object = MibTableColumn
snPimVIfStatOutHelloPkts = _SnPimVIfStatOutHelloPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 12),
    _SnPimVIfStatOutHelloPkts_Type()
)
snPimVIfStatOutHelloPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatOutHelloPkts.setStatus("mandatory")
_SnPimVIfStatDiscardHelloPkts_Type = Counter32
_SnPimVIfStatDiscardHelloPkts_Object = MibTableColumn
snPimVIfStatDiscardHelloPkts = _SnPimVIfStatDiscardHelloPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 13),
    _SnPimVIfStatDiscardHelloPkts_Type()
)
snPimVIfStatDiscardHelloPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatDiscardHelloPkts.setStatus("mandatory")
_SnPimVIfStatInGraftPkts_Type = Counter32
_SnPimVIfStatInGraftPkts_Object = MibTableColumn
snPimVIfStatInGraftPkts = _SnPimVIfStatInGraftPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 14),
    _SnPimVIfStatInGraftPkts_Type()
)
snPimVIfStatInGraftPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatInGraftPkts.setStatus("mandatory")
_SnPimVIfStatOutGraftPkts_Type = Counter32
_SnPimVIfStatOutGraftPkts_Object = MibTableColumn
snPimVIfStatOutGraftPkts = _SnPimVIfStatOutGraftPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 15),
    _SnPimVIfStatOutGraftPkts_Type()
)
snPimVIfStatOutGraftPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatOutGraftPkts.setStatus("mandatory")
_SnPimVIfStatDiscardGraftPkts_Type = Counter32
_SnPimVIfStatDiscardGraftPkts_Object = MibTableColumn
snPimVIfStatDiscardGraftPkts = _SnPimVIfStatDiscardGraftPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 16),
    _SnPimVIfStatDiscardGraftPkts_Type()
)
snPimVIfStatDiscardGraftPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatDiscardGraftPkts.setStatus("mandatory")
_SnPimVIfStatInGraftAckPkts_Type = Counter32
_SnPimVIfStatInGraftAckPkts_Object = MibTableColumn
snPimVIfStatInGraftAckPkts = _SnPimVIfStatInGraftAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 17),
    _SnPimVIfStatInGraftAckPkts_Type()
)
snPimVIfStatInGraftAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatInGraftAckPkts.setStatus("mandatory")
_SnPimVIfStatOutGraftAckPkts_Type = Counter32
_SnPimVIfStatOutGraftAckPkts_Object = MibTableColumn
snPimVIfStatOutGraftAckPkts = _SnPimVIfStatOutGraftAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 18),
    _SnPimVIfStatOutGraftAckPkts_Type()
)
snPimVIfStatOutGraftAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatOutGraftAckPkts.setStatus("mandatory")
_SnPimVIfStatDiscardGraftAckPkts_Type = Counter32
_SnPimVIfStatDiscardGraftAckPkts_Object = MibTableColumn
snPimVIfStatDiscardGraftAckPkts = _SnPimVIfStatDiscardGraftAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 1, 9, 1, 19),
    _SnPimVIfStatDiscardGraftAckPkts_Type()
)
snPimVIfStatDiscardGraftAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimVIfStatDiscardGraftAckPkts.setStatus("mandatory")
_SnPimSMMIBObjects_ObjectIdentity = ObjectIdentity
snPimSMMIBObjects = _SnPimSMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2)
)


class _SnPimJoinPruneInterval_Type(Integer32):
    """Custom type snPimJoinPruneInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_SnPimJoinPruneInterval_Type.__name__ = "Integer32"
_SnPimJoinPruneInterval_Object = MibScalar
snPimJoinPruneInterval = _SnPimJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 1),
    _SnPimJoinPruneInterval_Type()
)
snPimJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimJoinPruneInterval.setStatus("mandatory")
_SnPimCandidateBSRTable_Object = MibTable
snPimCandidateBSRTable = _SnPimCandidateBSRTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 2)
)
if mibBuilder.loadTexts:
    snPimCandidateBSRTable.setStatus("mandatory")
_SnPimCandidateBSREntry_Object = MibTableRow
snPimCandidateBSREntry = _SnPimCandidateBSREntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 2, 1)
)
snPimCandidateBSREntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snPimCandidateBSRPortID"),
)
if mibBuilder.loadTexts:
    snPimCandidateBSREntry.setStatus("mandatory")
_SnPimCandidateBSRPortID_Type = Integer32
_SnPimCandidateBSRPortID_Object = MibTableColumn
snPimCandidateBSRPortID = _SnPimCandidateBSRPortID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 2, 1, 1),
    _SnPimCandidateBSRPortID_Type()
)
snPimCandidateBSRPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimCandidateBSRPortID.setStatus("mandatory")
_SnPimCandidateBSRIPAddress_Type = IpAddress
_SnPimCandidateBSRIPAddress_Object = MibTableColumn
snPimCandidateBSRIPAddress = _SnPimCandidateBSRIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 2, 1, 2),
    _SnPimCandidateBSRIPAddress_Type()
)
snPimCandidateBSRIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimCandidateBSRIPAddress.setStatus("mandatory")


class _SnPimCandidateBSRHashMaskLen_Type(Integer32):
    """Custom type snPimCandidateBSRHashMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SnPimCandidateBSRHashMaskLen_Type.__name__ = "Integer32"
_SnPimCandidateBSRHashMaskLen_Object = MibTableColumn
snPimCandidateBSRHashMaskLen = _SnPimCandidateBSRHashMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 2, 1, 3),
    _SnPimCandidateBSRHashMaskLen_Type()
)
snPimCandidateBSRHashMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimCandidateBSRHashMaskLen.setStatus("mandatory")


class _SnPimCandidateBSRPreference_Type(Integer32):
    """Custom type snPimCandidateBSRPreference based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnPimCandidateBSRPreference_Type.__name__ = "Integer32"
_SnPimCandidateBSRPreference_Object = MibTableColumn
snPimCandidateBSRPreference = _SnPimCandidateBSRPreference_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 2, 1, 4),
    _SnPimCandidateBSRPreference_Type()
)
snPimCandidateBSRPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimCandidateBSRPreference.setStatus("mandatory")
_SnPimRPSetTable_Object = MibTable
snPimRPSetTable = _SnPimRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 3)
)
if mibBuilder.loadTexts:
    snPimRPSetTable.setStatus("mandatory")
_SnPimRPSetEntry_Object = MibTableRow
snPimRPSetEntry = _SnPimRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 3, 1)
)
snPimRPSetEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snPimRPSetGroupAddress"),
    (0, "HP-SN-IP-MIB", "snPimRPSetMask"),
    (0, "HP-SN-IP-MIB", "snPimRPSetIPAddress"),
)
if mibBuilder.loadTexts:
    snPimRPSetEntry.setStatus("mandatory")
_SnPimRPSetGroupAddress_Type = IpAddress
_SnPimRPSetGroupAddress_Object = MibTableColumn
snPimRPSetGroupAddress = _SnPimRPSetGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 3, 1, 1),
    _SnPimRPSetGroupAddress_Type()
)
snPimRPSetGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimRPSetGroupAddress.setStatus("mandatory")
_SnPimRPSetMask_Type = IpAddress
_SnPimRPSetMask_Object = MibTableColumn
snPimRPSetMask = _SnPimRPSetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 3, 1, 2),
    _SnPimRPSetMask_Type()
)
snPimRPSetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimRPSetMask.setStatus("mandatory")
_SnPimRPSetIPAddress_Type = IpAddress
_SnPimRPSetIPAddress_Object = MibTableColumn
snPimRPSetIPAddress = _SnPimRPSetIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 3, 1, 3),
    _SnPimRPSetIPAddress_Type()
)
snPimRPSetIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimRPSetIPAddress.setStatus("mandatory")


class _SnPimRPSetHoldTime_Type(Integer32):
    """Custom type snPimRPSetHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnPimRPSetHoldTime_Type.__name__ = "Integer32"
_SnPimRPSetHoldTime_Object = MibTableColumn
snPimRPSetHoldTime = _SnPimRPSetHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 3, 1, 4),
    _SnPimRPSetHoldTime_Type()
)
snPimRPSetHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimRPSetHoldTime.setStatus("mandatory")
_SnPimCandidateRPTable_Object = MibTable
snPimCandidateRPTable = _SnPimCandidateRPTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 4)
)
if mibBuilder.loadTexts:
    snPimCandidateRPTable.setStatus("mandatory")
_SnPimCandidateRPEntry_Object = MibTableRow
snPimCandidateRPEntry = _SnPimCandidateRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 4, 1)
)
snPimCandidateRPEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snPimCandidateRPGroupAddress"),
    (0, "HP-SN-IP-MIB", "snPimCandidateRPMask"),
)
if mibBuilder.loadTexts:
    snPimCandidateRPEntry.setStatus("mandatory")
_SnPimCandidateRPGroupAddress_Type = IpAddress
_SnPimCandidateRPGroupAddress_Object = MibTableColumn
snPimCandidateRPGroupAddress = _SnPimCandidateRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 4, 1, 1),
    _SnPimCandidateRPGroupAddress_Type()
)
snPimCandidateRPGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimCandidateRPGroupAddress.setStatus("mandatory")
_SnPimCandidateRPMask_Type = IpAddress
_SnPimCandidateRPMask_Object = MibTableColumn
snPimCandidateRPMask = _SnPimCandidateRPMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 4, 1, 2),
    _SnPimCandidateRPMask_Type()
)
snPimCandidateRPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPimCandidateRPMask.setStatus("mandatory")
_SnPimCandidateRPIPAddress_Type = IpAddress
_SnPimCandidateRPIPAddress_Object = MibTableColumn
snPimCandidateRPIPAddress = _SnPimCandidateRPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 4, 1, 3),
    _SnPimCandidateRPIPAddress_Type()
)
snPimCandidateRPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimCandidateRPIPAddress.setStatus("mandatory")


class _SnPimCandidateRPRowStatus_Type(Integer32):
    """Custom type snPimCandidateRPRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noSuch", 0),
          ("other", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4),
          ("modify", 5))
    )


_SnPimCandidateRPRowStatus_Type.__name__ = "Integer32"
_SnPimCandidateRPRowStatus_Object = MibTableColumn
snPimCandidateRPRowStatus = _SnPimCandidateRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9, 2, 4, 1, 4),
    _SnPimCandidateRPRowStatus_Type()
)
snPimCandidateRPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPimCandidateRPRowStatus.setStatus("mandatory")
_SnLoopbackIntfConfigTable_Object = MibTable
snLoopbackIntfConfigTable = _SnLoopbackIntfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 13, 1)
)
if mibBuilder.loadTexts:
    snLoopbackIntfConfigTable.setStatus("mandatory")
_SnLoopbackIntfConfigEntry_Object = MibTableRow
snLoopbackIntfConfigEntry = _SnLoopbackIntfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 13, 1, 1)
)
snLoopbackIntfConfigEntry.setIndexNames(
    (0, "HP-SN-IP-MIB", "snLoopbackIntfConfigPortIndex"),
)
if mibBuilder.loadTexts:
    snLoopbackIntfConfigEntry.setStatus("mandatory")


class _SnLoopbackIntfConfigPortIndex_Type(Integer32):
    """Custom type snLoopbackIntfConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SnLoopbackIntfConfigPortIndex_Type.__name__ = "Integer32"
_SnLoopbackIntfConfigPortIndex_Object = MibTableColumn
snLoopbackIntfConfigPortIndex = _SnLoopbackIntfConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 13, 1, 1, 1),
    _SnLoopbackIntfConfigPortIndex_Type()
)
snLoopbackIntfConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snLoopbackIntfConfigPortIndex.setStatus("mandatory")


class _SnLoopbackIntfMode_Type(Integer32):
    """Custom type snLoopbackIntfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnLoopbackIntfMode_Type.__name__ = "Integer32"
_SnLoopbackIntfMode_Object = MibTableColumn
snLoopbackIntfMode = _SnLoopbackIntfMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 13, 1, 1, 2),
    _SnLoopbackIntfMode_Type()
)
snLoopbackIntfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snLoopbackIntfMode.setStatus("mandatory")


class _SnLoopbackIntfRowStatus_Type(Integer32):
    """Custom type snLoopbackIntfRowStatus based on Integer32"""
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
        *(("invalid", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4),
          ("modify", 5))
    )


_SnLoopbackIntfRowStatus_Type.__name__ = "Integer32"
_SnLoopbackIntfRowStatus_Object = MibTableColumn
snLoopbackIntfRowStatus = _SnLoopbackIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 13, 1, 1, 3),
    _SnLoopbackIntfRowStatus_Type()
)
snLoopbackIntfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snLoopbackIntfRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SN-IP-MIB",
    **{"DisplayString": DisplayString,
       "RtrStatus": RtrStatus,
       "ClearStatus": ClearStatus,
       "RowSts": RowSts,
       "PortIndex": PortIndex,
       "Action": Action,
       "PhysAddress": PhysAddress,
       "Metric": Metric,
       "PortMask": PortMask,
       "snRtIpGeneral": snRtIpGeneral,
       "snRtClearArpCache": snRtClearArpCache,
       "snRtClearIpCache": snRtClearIpCache,
       "snRtClearIpRoute": snRtClearIpRoute,
       "snRtBootpServer": snRtBootpServer,
       "snRtBootpRelayMax": snRtBootpRelayMax,
       "snRtArpAge": snRtArpAge,
       "snRtIpIrdpEnable": snRtIpIrdpEnable,
       "snRtIpLoadShare": snRtIpLoadShare,
       "snRtIpProxyArp": snRtIpProxyArp,
       "snRtIpRarp": snRtIpRarp,
       "snRtIpTtl": snRtIpTtl,
       "snRtIpSetAllPortConfig": snRtIpSetAllPortConfig,
       "snRtIpFwdCacheMaxEntries": snRtIpFwdCacheMaxEntries,
       "snRtIpFwdCacheCurEntries": snRtIpFwdCacheCurEntries,
       "snRtIpMaxStaticRouteEntries": snRtIpMaxStaticRouteEntries,
       "snRtIpDirBcastFwd": snRtIpDirBcastFwd,
       "snRtIpLoadShareNumOfPaths": snRtIpLoadShareNumOfPaths,
       "snRtIpLoadShareMaxPaths": snRtIpLoadShareMaxPaths,
       "snRtIpLoadShareMinPaths": snRtIpLoadShareMinPaths,
       "snRtIpProtocolRouterId": snRtIpProtocolRouterId,
       "snRtIpSourceRoute": snRtIpSourceRoute,
       "snRtIpStaticRouteTable": snRtIpStaticRouteTable,
       "snRtIpStaticRouteEntry": snRtIpStaticRouteEntry,
       "snRtIpStaticRouteIndex": snRtIpStaticRouteIndex,
       "snRtIpStaticRouteDest": snRtIpStaticRouteDest,
       "snRtIpStaticRouteMask": snRtIpStaticRouteMask,
       "snRtIpStaticRouteNextHop": snRtIpStaticRouteNextHop,
       "snRtIpStaticRouteMetric": snRtIpStaticRouteMetric,
       "snRtIpStaticRouteRowStatus": snRtIpStaticRouteRowStatus,
       "snRtIpStaticRouteDistance": snRtIpStaticRouteDistance,
       "snRtIpFilterTable": snRtIpFilterTable,
       "snRtIpFilterEntry": snRtIpFilterEntry,
       "snRtIpFilterIndex": snRtIpFilterIndex,
       "snRtIpFilterAction": snRtIpFilterAction,
       "snRtIpFilterProtocol": snRtIpFilterProtocol,
       "snRtIpFilterSourceIp": snRtIpFilterSourceIp,
       "snRtIpFilterSourceMask": snRtIpFilterSourceMask,
       "snRtIpFilterDestIp": snRtIpFilterDestIp,
       "snRtIpFilterDestMask": snRtIpFilterDestMask,
       "snRtIpFilterOperator": snRtIpFilterOperator,
       "snRtIpFilterOperand": snRtIpFilterOperand,
       "snRtIpFilterRowStatus": snRtIpFilterRowStatus,
       "snRtIpFilterEstablished": snRtIpFilterEstablished,
       "snRtIpFilterQosPriority": snRtIpFilterQosPriority,
       "snRtIpRarpTable": snRtIpRarpTable,
       "snRtIpRarpEntry": snRtIpRarpEntry,
       "snRtIpRarpIndex": snRtIpRarpIndex,
       "snRtIpRarpMac": snRtIpRarpMac,
       "snRtIpRarpIp": snRtIpRarpIp,
       "snRtIpRarpRowStatus": snRtIpRarpRowStatus,
       "snRtStaticArpTable": snRtStaticArpTable,
       "snRtStaticArpEntry": snRtStaticArpEntry,
       "snRtStaticArpIndex": snRtStaticArpIndex,
       "snRtStaticArpIp": snRtStaticArpIp,
       "snRtStaticArpMac": snRtStaticArpMac,
       "snRtStaticArpPort": snRtStaticArpPort,
       "snRtStaticArpRowStatus": snRtStaticArpRowStatus,
       "snRtIpPortAddrTable": snRtIpPortAddrTable,
       "snRtIpPortAddrEntry": snRtIpPortAddrEntry,
       "snRtIpPortAddrPortIndex": snRtIpPortAddrPortIndex,
       "snRtIpPortAddress": snRtIpPortAddress,
       "snRtIpPortSubnetMask": snRtIpPortSubnetMask,
       "snRtIpPortAddrType": snRtIpPortAddrType,
       "snRtIpPortRowStatus": snRtIpPortRowStatus,
       "snRtIpPortAccessTable": snRtIpPortAccessTable,
       "snRtIpPortAccessEntry": snRtIpPortAccessEntry,
       "snRtIpPortAccessPortIndex": snRtIpPortAccessPortIndex,
       "snRtIpPortAccessDirection": snRtIpPortAccessDirection,
       "snRtIpPortAccessFilters": snRtIpPortAccessFilters,
       "snRtIpPortAccessRowStatus": snRtIpPortAccessRowStatus,
       "snRtIpPortConfigTable": snRtIpPortConfigTable,
       "snRtIpPortConfigEntry": snRtIpPortConfigEntry,
       "snRtIpPortConfigPortIndex": snRtIpPortConfigPortIndex,
       "snRtIpPortMtu": snRtIpPortMtu,
       "snRtIpPortEncap": snRtIpPortEncap,
       "snRtIpPortMetric": snRtIpPortMetric,
       "snRtIpPortDirBcastFwd": snRtIpPortDirBcastFwd,
       "snRtBcastFwd": snRtBcastFwd,
       "snRtBcastFwdGeneral": snRtBcastFwdGeneral,
       "snRtUdpBcastFwdEnable": snRtUdpBcastFwdEnable,
       "snRtUdpBcastFwdPort": snRtUdpBcastFwdPort,
       "snRtUdpBcastFwdPortTable": snRtUdpBcastFwdPortTable,
       "snRtUdpBcastFwdPortEntry": snRtUdpBcastFwdPortEntry,
       "snRtUdpBcastFwdPortIndex": snRtUdpBcastFwdPortIndex,
       "snRtUdpBcastFwdPortNumber": snRtUdpBcastFwdPortNumber,
       "snRtUdpBcastFwdPortRowStatus": snRtUdpBcastFwdPortRowStatus,
       "snRtUdpHelper": snRtUdpHelper,
       "snRtUdpHelperTable": snRtUdpHelperTable,
       "snRtUdpHelperEntry": snRtUdpHelperEntry,
       "snRtUdpHelperPortIndex": snRtUdpHelperPortIndex,
       "snRtUdpHelperIndex": snRtUdpHelperIndex,
       "snRtUdpHelperAddr": snRtUdpHelperAddr,
       "snRtUdpHelperRowStatus": snRtUdpHelperRowStatus,
       "snRtIpTraceRoute": snRtIpTraceRoute,
       "snRtIpTraceRouteGeneral": snRtIpTraceRouteGeneral,
       "snRtIpTraceRouteTargetAddr": snRtIpTraceRouteTargetAddr,
       "snRtIpTraceRouteMinTtl": snRtIpTraceRouteMinTtl,
       "snRtIpTraceRouteMaxTtl": snRtIpTraceRouteMaxTtl,
       "snRtIpTraceRouteTimeOut": snRtIpTraceRouteTimeOut,
       "snRtIpTraceRouteControl": snRtIpTraceRouteControl,
       "snRtIpTraceRouteResult": snRtIpTraceRouteResult,
       "snRtIpTraceRouteResultTable": snRtIpTraceRouteResultTable,
       "snRtIpTraceRouteResultEntry": snRtIpTraceRouteResultEntry,
       "snRtIpTraceRouteResultIndex": snRtIpTraceRouteResultIndex,
       "snRtIpTraceRouteResultAddr": snRtIpTraceRouteResultAddr,
       "snRtIpTraceRouteResultRoundTripTime1": snRtIpTraceRouteResultRoundTripTime1,
       "snRtIpTraceRouteResultRoundTripTime2": snRtIpTraceRouteResultRoundTripTime2,
       "snRtIpFwdCacheTable": snRtIpFwdCacheTable,
       "snRtIpFwdCacheEntry": snRtIpFwdCacheEntry,
       "snRtIpFwdCacheIndex": snRtIpFwdCacheIndex,
       "snRtIpFwdCacheIp": snRtIpFwdCacheIp,
       "snRtIpFwdCacheMac": snRtIpFwdCacheMac,
       "snRtIpFwdCacheNextHopIp": snRtIpFwdCacheNextHopIp,
       "snRtIpFwdCacheOutgoingPort": snRtIpFwdCacheOutgoingPort,
       "snRtIpFwdCacheType": snRtIpFwdCacheType,
       "snRtIpFwdCacheAction": snRtIpFwdCacheAction,
       "snRtIpFwdCacheFragCheck": snRtIpFwdCacheFragCheck,
       "snRtIpFwdCacheSnapHdr": snRtIpFwdCacheSnapHdr,
       "snRtIpFwdCacheVLanId": snRtIpFwdCacheVLanId,
       "snIpAsPathAccessListTable": snIpAsPathAccessListTable,
       "snIpAsPathAccessListEntry": snIpAsPathAccessListEntry,
       "snIpAsPathAccessListIndex": snIpAsPathAccessListIndex,
       "snIpAsPathAccessListSequence": snIpAsPathAccessListSequence,
       "snIpAsPathAccessListAction": snIpAsPathAccessListAction,
       "snIpAsPathAccessListRegExpression": snIpAsPathAccessListRegExpression,
       "snIpAsPathAccessListRowStatus": snIpAsPathAccessListRowStatus,
       "snIpCommunityListTable": snIpCommunityListTable,
       "snIpCommunityListEntry": snIpCommunityListEntry,
       "snIpCommunityListIndex": snIpCommunityListIndex,
       "snIpCommunityListSequence": snIpCommunityListSequence,
       "snIpCommunityListAction": snIpCommunityListAction,
       "snIpCommunityListCommNum": snIpCommunityListCommNum,
       "snIpCommunityListInternet": snIpCommunityListInternet,
       "snIpCommunityListNoAdvertise": snIpCommunityListNoAdvertise,
       "snIpCommunityListNoExport": snIpCommunityListNoExport,
       "snIpCommunityListRowStatus": snIpCommunityListRowStatus,
       "snIpCommunityListLocalAs": snIpCommunityListLocalAs,
       "snIpPrefixListTable": snIpPrefixListTable,
       "snIpPrefixListEntry": snIpPrefixListEntry,
       "snIpPrefixListName": snIpPrefixListName,
       "snIpPrefixListSequence": snIpPrefixListSequence,
       "snIpPrefixListDesc": snIpPrefixListDesc,
       "snIpPrefixListAction": snIpPrefixListAction,
       "snIpPrefixListAddr": snIpPrefixListAddr,
       "snIpPrefixListMask": snIpPrefixListMask,
       "snIpPrefixListGeValue": snIpPrefixListGeValue,
       "snIpPrefixListLeValue": snIpPrefixListLeValue,
       "snIpPrefixListRowStatus": snIpPrefixListRowStatus,
       "snIpAsPathAccessListStringTable": snIpAsPathAccessListStringTable,
       "snIpAsPathAccessListStringEntry": snIpAsPathAccessListStringEntry,
       "snIpAsPathAccessListStringName": snIpAsPathAccessListStringName,
       "snIpAsPathAccessListStringSequence": snIpAsPathAccessListStringSequence,
       "snIpAsPathAccessListStringAction": snIpAsPathAccessListStringAction,
       "snIpAsPathAccessListStringRegExpression": snIpAsPathAccessListStringRegExpression,
       "snIpAsPathAccessListStringRowStatus": snIpAsPathAccessListStringRowStatus,
       "snIpCommunityListStringTable": snIpCommunityListStringTable,
       "snIpCommunityListStringEntry": snIpCommunityListStringEntry,
       "snIpCommunityListStringName": snIpCommunityListStringName,
       "snIpCommunityListStringSequence": snIpCommunityListStringSequence,
       "snIpCommunityListStringAction": snIpCommunityListStringAction,
       "snIpCommunityListStringCommNum": snIpCommunityListStringCommNum,
       "snIpCommunityListStringInternet": snIpCommunityListStringInternet,
       "snIpCommunityListStringNoAdvertise": snIpCommunityListStringNoAdvertise,
       "snIpCommunityListStringNoExport": snIpCommunityListStringNoExport,
       "snIpCommunityListStringRowStatus": snIpCommunityListStringRowStatus,
       "snIpCommunityListStringLocalAs": snIpCommunityListStringLocalAs,
       "snRtIpPortIfAddrTable": snRtIpPortIfAddrTable,
       "snRtIpPortIfAddrEntry": snRtIpPortIfAddrEntry,
       "snRtIpPortIfAddrInterfaceIndex": snRtIpPortIfAddrInterfaceIndex,
       "snRtIpPortIfAddress": snRtIpPortIfAddress,
       "snRtIpPortIfSubnetMask": snRtIpPortIfSubnetMask,
       "snRtIpPortIfAddrType": snRtIpPortIfAddrType,
       "snRtIpPortIfRowStatus": snRtIpPortIfRowStatus,
       "snRtIpPortIfAccessTable": snRtIpPortIfAccessTable,
       "snRtIpPortIfAccessEntry": snRtIpPortIfAccessEntry,
       "snRtIpPortIfAccessInterfaceIndex": snRtIpPortIfAccessInterfaceIndex,
       "snRtIpPortIfAccessDirection": snRtIpPortIfAccessDirection,
       "snRtIpPortIfAccessFilters": snRtIpPortIfAccessFilters,
       "snRtIpPortIfAccessRowStatus": snRtIpPortIfAccessRowStatus,
       "snRtIpPortIfConfigTable": snRtIpPortIfConfigTable,
       "snRtIpPortIfConfigEntry": snRtIpPortIfConfigEntry,
       "snRtIpPortIfConfigInterfaceIndex": snRtIpPortIfConfigInterfaceIndex,
       "snRtIpPortIfMtu": snRtIpPortIfMtu,
       "snRtIpPortIfEncap": snRtIpPortIfEncap,
       "snRtIpPortIfMetric": snRtIpPortIfMetric,
       "snRtIpPortIfDirBcastFwd": snRtIpPortIfDirBcastFwd,
       "snRtIpRipGeneral": snRtIpRipGeneral,
       "snRtIpRipEnable": snRtIpRipEnable,
       "snRtIpRipUpdateTime": snRtIpRipUpdateTime,
       "snRtIpRipRedisEnable": snRtIpRipRedisEnable,
       "snRtIpRipRedisDefMetric": snRtIpRipRedisDefMetric,
       "snRtIpRipSetAllPortConfig": snRtIpRipSetAllPortConfig,
       "snRtIpRipGblFiltList": snRtIpRipGblFiltList,
       "snRtIpRipFiltOnAllPort": snRtIpRipFiltOnAllPort,
       "snRtIpRipDistance": snRtIpRipDistance,
       "snRtIpRipPortConfigTable": snRtIpRipPortConfigTable,
       "snRtIpRipPortConfigEntry": snRtIpRipPortConfigEntry,
       "snRtIpRipPortConfigPortIndex": snRtIpRipPortConfigPortIndex,
       "snRtIpRipPortVersion": snRtIpRipPortVersion,
       "snRtIpRipPortPoisonReverse": snRtIpRipPortPoisonReverse,
       "snRtIpRipPortLearnDefault": snRtIpRipPortLearnDefault,
       "snRtIpRipRedisTable": snRtIpRipRedisTable,
       "snRtIpRipRedisEntry": snRtIpRipRedisEntry,
       "snRtIpRipRedisIndex": snRtIpRipRedisIndex,
       "snRtIpRipRedisAction": snRtIpRipRedisAction,
       "snRtIpRipRedisProtocol": snRtIpRipRedisProtocol,
       "snRtIpRipRedisIp": snRtIpRipRedisIp,
       "snRtIpRipRedisMask": snRtIpRipRedisMask,
       "snRtIpRipRedisMatchMetric": snRtIpRipRedisMatchMetric,
       "snRtIpRipRedisSetMetric": snRtIpRipRedisSetMetric,
       "snRtIpRipRedisRowStatus": snRtIpRipRedisRowStatus,
       "snRtIpRipRouteFilterTable": snRtIpRipRouteFilterTable,
       "snRtIpRipRouteFilterEntry": snRtIpRipRouteFilterEntry,
       "snRtIpRipRouteFilterId": snRtIpRipRouteFilterId,
       "snRtIpRipRouteFilterAction": snRtIpRipRouteFilterAction,
       "snRtIpRipRouteFilterIpAddr": snRtIpRipRouteFilterIpAddr,
       "snRtIpRipRouteFilterSubnetMask": snRtIpRipRouteFilterSubnetMask,
       "snRtIpRipRouteFilterRowStatus": snRtIpRipRouteFilterRowStatus,
       "snRtIpRipNbrFilterTable": snRtIpRipNbrFilterTable,
       "snRtIpRipNbrFilterEntry": snRtIpRipNbrFilterEntry,
       "snRtIpRipNbrFilterId": snRtIpRipNbrFilterId,
       "snRtIpRipNbrFilterAction": snRtIpRipNbrFilterAction,
       "snRtIpRipNbrFilterSourceIp": snRtIpRipNbrFilterSourceIp,
       "snRtIpRipNbrFilterRowStatus": snRtIpRipNbrFilterRowStatus,
       "snRtIpRipPortAccessTable": snRtIpRipPortAccessTable,
       "snRtIpRipPortAccessEntry": snRtIpRipPortAccessEntry,
       "snRtIpRipPortAccessPort": snRtIpRipPortAccessPort,
       "snRtIpRipPortAccessDir": snRtIpRipPortAccessDir,
       "snRtIpRipPortAccessFilterList": snRtIpRipPortAccessFilterList,
       "snRtIpRipPortAccessRowStatus": snRtIpRipPortAccessRowStatus,
       "snRtIpRipPortIfConfigTable": snRtIpRipPortIfConfigTable,
       "snRtIpRipPortIfConfigEntry": snRtIpRipPortIfConfigEntry,
       "snRtIpRipPortIfConfigInterfaceIndex": snRtIpRipPortIfConfigInterfaceIndex,
       "snRtIpRipPortIfVersion": snRtIpRipPortIfVersion,
       "snRtIpRipPortIfPoisonReverse": snRtIpRipPortIfPoisonReverse,
       "snRtIpRipPortIfLearnDefault": snRtIpRipPortIfLearnDefault,
       "snRtIpRipPortIfAccessTable": snRtIpRipPortIfAccessTable,
       "snRtIpRipPortIfAccessEntry": snRtIpRipPortIfAccessEntry,
       "snRtIpRipPortIfAccessPort": snRtIpRipPortIfAccessPort,
       "snRtIpRipPortIfAccessDir": snRtIpRipPortIfAccessDir,
       "snRtIpRipPortIfAccessFilterList": snRtIpRipPortIfAccessFilterList,
       "snRtIpRipPortIfAccessRowStatus": snRtIpRipPortIfAccessRowStatus,
       "snDvmrpMIBObjects": snDvmrpMIBObjects,
       "snDvmrpVersion": snDvmrpVersion,
       "snDvmrpEnable": snDvmrpEnable,
       "snDvmrpGenerationId": snDvmrpGenerationId,
       "snDvmrpProbeInterval": snDvmrpProbeInterval,
       "snDvmrpReportInterval": snDvmrpReportInterval,
       "snDvmrpTriggerInterval": snDvmrpTriggerInterval,
       "snDvmrpNeighborRouterTimeout": snDvmrpNeighborRouterTimeout,
       "snDvmrpRouteExpireTime": snDvmrpRouteExpireTime,
       "snDvmrpRouteDiscardTime": snDvmrpRouteDiscardTime,
       "snDvmrpPruneAge": snDvmrpPruneAge,
       "snDvmrpGraftRetransmitTime": snDvmrpGraftRetransmitTime,
       "snDvmrpDefaultRoute": snDvmrpDefaultRoute,
       "snDvmrpVInterfaceTable": snDvmrpVInterfaceTable,
       "snDvmrpVInterfaceEntry": snDvmrpVInterfaceEntry,
       "snDvmrpVInterfaceVifIndex": snDvmrpVInterfaceVifIndex,
       "snDvmrpVInterfaceType": snDvmrpVInterfaceType,
       "snDvmrpVInterfaceOperState": snDvmrpVInterfaceOperState,
       "snDvmrpVInterfaceLocalAddress": snDvmrpVInterfaceLocalAddress,
       "snDvmrpVInterfaceRemoteAddress": snDvmrpVInterfaceRemoteAddress,
       "snDvmrpVInterfaceRemoteSubnetMask": snDvmrpVInterfaceRemoteSubnetMask,
       "snDvmrpVInterfaceMetric": snDvmrpVInterfaceMetric,
       "snDvmrpVInterfaceTtlThreshold": snDvmrpVInterfaceTtlThreshold,
       "snDvmrpVInterfaceAdvertiseLocal": snDvmrpVInterfaceAdvertiseLocal,
       "snDvmrpVInterfaceEncapsulation": snDvmrpVInterfaceEncapsulation,
       "snDvmrpVInterfaceStatus": snDvmrpVInterfaceStatus,
       "snDvmrpNeighborTable": snDvmrpNeighborTable,
       "snDvmrpNeighborEntry": snDvmrpNeighborEntry,
       "snDvmrpNeighborEntryIndex": snDvmrpNeighborEntryIndex,
       "snDvmrpNeighborVifIndex": snDvmrpNeighborVifIndex,
       "snDvmrpNeighborAddress": snDvmrpNeighborAddress,
       "snDvmrpNeighborUpTime": snDvmrpNeighborUpTime,
       "snDvmrpNeighborExpiryTime": snDvmrpNeighborExpiryTime,
       "snDvmrpNeighborGenerationId": snDvmrpNeighborGenerationId,
       "snDvmrpNeighborMajorVersion": snDvmrpNeighborMajorVersion,
       "snDvmrpNeighborMinorVersion": snDvmrpNeighborMinorVersion,
       "snDvmrpNeighborCapabilities": snDvmrpNeighborCapabilities,
       "snDvmrpRouteTable": snDvmrpRouteTable,
       "snDvmrpRouteEntry": snDvmrpRouteEntry,
       "snDvmrpRouteEntryIndex": snDvmrpRouteEntryIndex,
       "snDvmrpRouteSource": snDvmrpRouteSource,
       "snDvmrpRouteSourceMask": snDvmrpRouteSourceMask,
       "snDvmrpRouteUpstreamNeighbor": snDvmrpRouteUpstreamNeighbor,
       "snDvmrpRouteVifIndex": snDvmrpRouteVifIndex,
       "snDvmrpRouteMetric": snDvmrpRouteMetric,
       "snDvmrpRouteExpiryTime": snDvmrpRouteExpiryTime,
       "snDvmrpRouteNextHopTable": snDvmrpRouteNextHopTable,
       "snDvmrpRouteNextHopEntry": snDvmrpRouteNextHopEntry,
       "snDvmrpRouteNextHopSource": snDvmrpRouteNextHopSource,
       "snDvmrpRouteNextHopSourceMask": snDvmrpRouteNextHopSourceMask,
       "snDvmrpRouteNextHopVifIndex": snDvmrpRouteNextHopVifIndex,
       "snDvmrpRouteNextHopType": snDvmrpRouteNextHopType,
       "snDvmrpVIfStatTable": snDvmrpVIfStatTable,
       "snDvmrpVIfStatEntry": snDvmrpVIfStatEntry,
       "snDvmrpVIfStatVifIndex": snDvmrpVIfStatVifIndex,
       "snDvmrpVIfStatInPkts": snDvmrpVIfStatInPkts,
       "snDvmrpVIfStatOutPkts": snDvmrpVIfStatOutPkts,
       "snDvmrpVIfStatInOctets": snDvmrpVIfStatInOctets,
       "snDvmrpVIfStatOutOctets": snDvmrpVIfStatOutOctets,
       "snDvmrpVIfStatInProbePkts": snDvmrpVIfStatInProbePkts,
       "snDvmrpVIfStatOutProbePkts": snDvmrpVIfStatOutProbePkts,
       "snDvmrpVIfStatDiscardProbePkts": snDvmrpVIfStatDiscardProbePkts,
       "snDvmrpVIfStatInRtUpdatePkts": snDvmrpVIfStatInRtUpdatePkts,
       "snDvmrpVIfStatOutRtUpdatePkts": snDvmrpVIfStatOutRtUpdatePkts,
       "snDvmrpVIfStatDiscardRtUpdatePkts": snDvmrpVIfStatDiscardRtUpdatePkts,
       "snDvmrpVIfStatInGraftPkts": snDvmrpVIfStatInGraftPkts,
       "snDvmrpVIfStatOutGraftPkts": snDvmrpVIfStatOutGraftPkts,
       "snDvmrpVIfStatDiscardGraftPkts": snDvmrpVIfStatDiscardGraftPkts,
       "snDvmrpVIfStatInGraftAckPkts": snDvmrpVIfStatInGraftAckPkts,
       "snDvmrpVIfStatOutGraftAckPkts": snDvmrpVIfStatOutGraftAckPkts,
       "snDvmrpVIfStatDiscardGraftAckPkts": snDvmrpVIfStatDiscardGraftAckPkts,
       "snDvmrpVIfStatInPrunePkts": snDvmrpVIfStatInPrunePkts,
       "snDvmrpVIfStatOutPrunePkts": snDvmrpVIfStatOutPrunePkts,
       "snDvmrpVIfStatDiscardPrunePkts": snDvmrpVIfStatDiscardPrunePkts,
       "snFsrpGlobal": snFsrpGlobal,
       "snFsrpGroupOperMode": snFsrpGroupOperMode,
       "snFsrpIfStateChangeTrap": snFsrpIfStateChangeTrap,
       "snFsrpIntf": snFsrpIntf,
       "snFsrpIfTable": snFsrpIfTable,
       "snFsrpIfEntry": snFsrpIfEntry,
       "snFsrpIfPort": snFsrpIfPort,
       "snFsrpIfIpAddress": snFsrpIfIpAddress,
       "snFsrpIfVirRtrIpAddr": snFsrpIfVirRtrIpAddr,
       "snFsrpIfOtherRtrIpAddr": snFsrpIfOtherRtrIpAddr,
       "snFsrpIfPreferLevel": snFsrpIfPreferLevel,
       "snFsrpIfTrackPortMask": snFsrpIfTrackPortMask,
       "snFsrpIfRowStatus": snFsrpIfRowStatus,
       "snFsrpIfState": snFsrpIfState,
       "snFsrpIfKeepAliveTime": snFsrpIfKeepAliveTime,
       "snFsrpIfRouterDeadTime": snFsrpIfRouterDeadTime,
       "snFsrpIfChassisTrackPortMask": snFsrpIfChassisTrackPortMask,
       "snFsrpIfTrackPortList": snFsrpIfTrackPortList,
       "snGblRtGeneral": snGblRtGeneral,
       "snGblRtRouteOnly": snGblRtRouteOnly,
       "snPimMIBObjects": snPimMIBObjects,
       "snPimEnable": snPimEnable,
       "snPimNeighborRouterTimeout": snPimNeighborRouterTimeout,
       "snPimHelloTime": snPimHelloTime,
       "snPimPruneTime": snPimPruneTime,
       "snPimGraftRetransmitTime": snPimGraftRetransmitTime,
       "snPimInactivityTime": snPimInactivityTime,
       "snPimVInterfaceTable": snPimVInterfaceTable,
       "snPimVInterfaceEntry": snPimVInterfaceEntry,
       "snPimVInterfaceVifIndex": snPimVInterfaceVifIndex,
       "snPimVInterfaceType": snPimVInterfaceType,
       "snPimVInterfaceLocalAddress": snPimVInterfaceLocalAddress,
       "snPimVInterfaceLocalSubnetMask": snPimVInterfaceLocalSubnetMask,
       "snPimVInterfaceRemoteAddress": snPimVInterfaceRemoteAddress,
       "snPimVInterfaceDR": snPimVInterfaceDR,
       "snPimVInterfaceTtlThreshold": snPimVInterfaceTtlThreshold,
       "snPimVInterfaceStatus": snPimVInterfaceStatus,
       "snPimVInterfaceMode": snPimVInterfaceMode,
       "snPimNeighborTable": snPimNeighborTable,
       "snPimNeighborEntry": snPimNeighborEntry,
       "snPimNeighborEntryIndex": snPimNeighborEntryIndex,
       "snPimNeighborVifIndex": snPimNeighborVifIndex,
       "snPimNeighborAddress": snPimNeighborAddress,
       "snPimNeighborUpTime": snPimNeighborUpTime,
       "snPimNeighborExpiryTime": snPimNeighborExpiryTime,
       "snPimVIfStatTable": snPimVIfStatTable,
       "snPimVIfStatEntry": snPimVIfStatEntry,
       "snPimVIfStatVifIndex": snPimVIfStatVifIndex,
       "snPimVIfStatInJoinPkts": snPimVIfStatInJoinPkts,
       "snPimVIfStatOutJoinPkts": snPimVIfStatOutJoinPkts,
       "snPimVIfStatDiscardJoinPkts": snPimVIfStatDiscardJoinPkts,
       "snPimVIfStatInPrunePkts": snPimVIfStatInPrunePkts,
       "snPimVIfStatOutPrunePkts": snPimVIfStatOutPrunePkts,
       "snPimVIfStatDiscardPrunePkts": snPimVIfStatDiscardPrunePkts,
       "snPimVIfStatInAssertPkts": snPimVIfStatInAssertPkts,
       "snPimVIfStatOutAssertPkts": snPimVIfStatOutAssertPkts,
       "snPimVIfStatDiscardAssertPkts": snPimVIfStatDiscardAssertPkts,
       "snPimVIfStatInHelloPkts": snPimVIfStatInHelloPkts,
       "snPimVIfStatOutHelloPkts": snPimVIfStatOutHelloPkts,
       "snPimVIfStatDiscardHelloPkts": snPimVIfStatDiscardHelloPkts,
       "snPimVIfStatInGraftPkts": snPimVIfStatInGraftPkts,
       "snPimVIfStatOutGraftPkts": snPimVIfStatOutGraftPkts,
       "snPimVIfStatDiscardGraftPkts": snPimVIfStatDiscardGraftPkts,
       "snPimVIfStatInGraftAckPkts": snPimVIfStatInGraftAckPkts,
       "snPimVIfStatOutGraftAckPkts": snPimVIfStatOutGraftAckPkts,
       "snPimVIfStatDiscardGraftAckPkts": snPimVIfStatDiscardGraftAckPkts,
       "snPimSMMIBObjects": snPimSMMIBObjects,
       "snPimJoinPruneInterval": snPimJoinPruneInterval,
       "snPimCandidateBSRTable": snPimCandidateBSRTable,
       "snPimCandidateBSREntry": snPimCandidateBSREntry,
       "snPimCandidateBSRPortID": snPimCandidateBSRPortID,
       "snPimCandidateBSRIPAddress": snPimCandidateBSRIPAddress,
       "snPimCandidateBSRHashMaskLen": snPimCandidateBSRHashMaskLen,
       "snPimCandidateBSRPreference": snPimCandidateBSRPreference,
       "snPimRPSetTable": snPimRPSetTable,
       "snPimRPSetEntry": snPimRPSetEntry,
       "snPimRPSetGroupAddress": snPimRPSetGroupAddress,
       "snPimRPSetMask": snPimRPSetMask,
       "snPimRPSetIPAddress": snPimRPSetIPAddress,
       "snPimRPSetHoldTime": snPimRPSetHoldTime,
       "snPimCandidateRPTable": snPimCandidateRPTable,
       "snPimCandidateRPEntry": snPimCandidateRPEntry,
       "snPimCandidateRPGroupAddress": snPimCandidateRPGroupAddress,
       "snPimCandidateRPMask": snPimCandidateRPMask,
       "snPimCandidateRPIPAddress": snPimCandidateRPIPAddress,
       "snPimCandidateRPRowStatus": snPimCandidateRPRowStatus,
       "snLoopbackIntfConfigTable": snLoopbackIntfConfigTable,
       "snLoopbackIntfConfigEntry": snLoopbackIntfConfigEntry,
       "snLoopbackIntfConfigPortIndex": snLoopbackIntfConfigPortIndex,
       "snLoopbackIntfMode": snLoopbackIntfMode,
       "snLoopbackIntfRowStatus": snLoopbackIntfRowStatus}
)
