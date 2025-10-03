# SNMP MIB module (ALCATEL-IND1-IPRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-IPRM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:32 2025
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

(routingIND1Iprm,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Iprm")

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1IPRMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1IPRMMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdminStatus(TextualConvention, Integer32):
    status = "current"
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



class StaticRouteType(TextualConvention, Integer32):
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
        *(("regular", 1),
          ("recursive", 2),
          ("bfd-enabled", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IPRMMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IPRMMIBObjects = _AlcatelIND1IPRMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1)
)
_AlaIprmConfig_ObjectIdentity = ObjectIdentity
alaIprmConfig = _AlaIprmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1)
)
_AlaIprmRouteTable_Object = MibTable
alaIprmRouteTable = _AlaIprmRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaIprmRouteTable.setStatus("current")
_AlaIprmRouteEntry_Object = MibTableRow
alaIprmRouteEntry = _AlaIprmRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1)
)
alaIprmRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRouteDest"),
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRouteMask"),
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRouteTos"),
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRouteNextHop"),
)
if mibBuilder.loadTexts:
    alaIprmRouteEntry.setStatus("current")
_AlaIprmRouteDest_Type = IpAddress
_AlaIprmRouteDest_Object = MibTableColumn
alaIprmRouteDest = _AlaIprmRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 1),
    _AlaIprmRouteDest_Type()
)
alaIprmRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmRouteDest.setStatus("current")
_AlaIprmRouteMask_Type = IpAddress
_AlaIprmRouteMask_Object = MibTableColumn
alaIprmRouteMask = _AlaIprmRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 2),
    _AlaIprmRouteMask_Type()
)
alaIprmRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmRouteMask.setStatus("current")


class _AlaIprmRouteTos_Type(Integer32):
    """Custom type alaIprmRouteTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaIprmRouteTos_Type.__name__ = "Integer32"
_AlaIprmRouteTos_Object = MibTableColumn
alaIprmRouteTos = _AlaIprmRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 3),
    _AlaIprmRouteTos_Type()
)
alaIprmRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmRouteTos.setStatus("current")
_AlaIprmRouteNextHop_Type = IpAddress
_AlaIprmRouteNextHop_Object = MibTableColumn
alaIprmRouteNextHop = _AlaIprmRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 4),
    _AlaIprmRouteNextHop_Type()
)
alaIprmRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmRouteNextHop.setStatus("current")
_AlaIprmRouteProto_Type = IANAipRouteProtocol
_AlaIprmRouteProto_Object = MibTableColumn
alaIprmRouteProto = _AlaIprmRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 5),
    _AlaIprmRouteProto_Type()
)
alaIprmRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIprmRouteProto.setStatus("current")
_AlaIprmRouteMetric_Type = Integer32
_AlaIprmRouteMetric_Object = MibTableColumn
alaIprmRouteMetric = _AlaIprmRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 6),
    _AlaIprmRouteMetric_Type()
)
alaIprmRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIprmRouteMetric.setStatus("current")
_AlaIprmRoutePriority_Type = Integer32
_AlaIprmRoutePriority_Object = MibTableColumn
alaIprmRoutePriority = _AlaIprmRoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 7),
    _AlaIprmRoutePriority_Type()
)
alaIprmRoutePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIprmRoutePriority.setStatus("current")
_AlaIprmStaticRouteTable_Object = MibTable
alaIprmStaticRouteTable = _AlaIprmStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaIprmStaticRouteTable.setStatus("current")
_AlaIprmStaticRouteEntry_Object = MibTableRow
alaIprmStaticRouteEntry = _AlaIprmStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1)
)
alaIprmStaticRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteDest"),
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteMask"),
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    alaIprmStaticRouteEntry.setStatus("current")
_AlaIprmStaticRouteDest_Type = IpAddress
_AlaIprmStaticRouteDest_Object = MibTableColumn
alaIprmStaticRouteDest = _AlaIprmStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 1),
    _AlaIprmStaticRouteDest_Type()
)
alaIprmStaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmStaticRouteDest.setStatus("current")
_AlaIprmStaticRouteMask_Type = IpAddress
_AlaIprmStaticRouteMask_Object = MibTableColumn
alaIprmStaticRouteMask = _AlaIprmStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 2),
    _AlaIprmStaticRouteMask_Type()
)
alaIprmStaticRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmStaticRouteMask.setStatus("current")
_AlaIprmStaticRouteNextHop_Type = IpAddress
_AlaIprmStaticRouteNextHop_Object = MibTableColumn
alaIprmStaticRouteNextHop = _AlaIprmStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 3),
    _AlaIprmStaticRouteNextHop_Type()
)
alaIprmStaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmStaticRouteNextHop.setStatus("current")
_AlaIprmStaticRouteMetric_Type = Integer32
_AlaIprmStaticRouteMetric_Object = MibTableColumn
alaIprmStaticRouteMetric = _AlaIprmStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 4),
    _AlaIprmStaticRouteMetric_Type()
)
alaIprmStaticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmStaticRouteMetric.setStatus("current")
_AlaIprmStaticRouteStatus_Type = RowStatus
_AlaIprmStaticRouteStatus_Object = MibTableColumn
alaIprmStaticRouteStatus = _AlaIprmStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 5),
    _AlaIprmStaticRouteStatus_Type()
)
alaIprmStaticRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmStaticRouteStatus.setStatus("current")
_AlaIprmStaticRouteBfdStatus_Type = AdminStatus
_AlaIprmStaticRouteBfdStatus_Object = MibTableColumn
alaIprmStaticRouteBfdStatus = _AlaIprmStaticRouteBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 6),
    _AlaIprmStaticRouteBfdStatus_Type()
)
alaIprmStaticRouteBfdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmStaticRouteBfdStatus.setStatus("current")
_AlaIprmStaticRouteType_Type = StaticRouteType
_AlaIprmStaticRouteType_Object = MibTableColumn
alaIprmStaticRouteType = _AlaIprmStaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 7),
    _AlaIprmStaticRouteType_Type()
)
alaIprmStaticRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmStaticRouteType.setStatus("current")


class _AlaIprmRtPrefLocal_Type(Integer32):
    """Custom type alaIprmRtPrefLocal based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaIprmRtPrefLocal_Type.__name__ = "Integer32"
_AlaIprmRtPrefLocal_Object = MibScalar
alaIprmRtPrefLocal = _AlaIprmRtPrefLocal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 3),
    _AlaIprmRtPrefLocal_Type()
)
alaIprmRtPrefLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIprmRtPrefLocal.setStatus("current")


class _AlaIprmRtPrefStatic_Type(Integer32):
    """Custom type alaIprmRtPrefStatic based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaIprmRtPrefStatic_Type.__name__ = "Integer32"
_AlaIprmRtPrefStatic_Object = MibScalar
alaIprmRtPrefStatic = _AlaIprmRtPrefStatic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 4),
    _AlaIprmRtPrefStatic_Type()
)
alaIprmRtPrefStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmRtPrefStatic.setStatus("current")


class _AlaIprmRtPrefOspf_Type(Integer32):
    """Custom type alaIprmRtPrefOspf based on Integer32"""
    defaultValue = 110

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaIprmRtPrefOspf_Type.__name__ = "Integer32"
_AlaIprmRtPrefOspf_Object = MibScalar
alaIprmRtPrefOspf = _AlaIprmRtPrefOspf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 5),
    _AlaIprmRtPrefOspf_Type()
)
alaIprmRtPrefOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmRtPrefOspf.setStatus("current")


class _AlaIprmRtPrefRip_Type(Integer32):
    """Custom type alaIprmRtPrefRip based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaIprmRtPrefRip_Type.__name__ = "Integer32"
_AlaIprmRtPrefRip_Object = MibScalar
alaIprmRtPrefRip = _AlaIprmRtPrefRip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 6),
    _AlaIprmRtPrefRip_Type()
)
alaIprmRtPrefRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmRtPrefRip.setStatus("current")


class _AlaIprmRtPrefBgp_Type(Integer32):
    """Custom type alaIprmRtPrefBgp based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaIprmRtPrefBgp_Type.__name__ = "Integer32"
_AlaIprmRtPrefBgp_Object = MibScalar
alaIprmRtPrefBgp = _AlaIprmRtPrefBgp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 7),
    _AlaIprmRtPrefBgp_Type()
)
alaIprmRtPrefBgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmRtPrefBgp.setStatus("deprecated")


class _AlaIprmRtPrefEbgp_Type(Integer32):
    """Custom type alaIprmRtPrefEbgp based on Integer32"""
    defaultValue = 190

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaIprmRtPrefEbgp_Type.__name__ = "Integer32"
_AlaIprmRtPrefEbgp_Object = MibScalar
alaIprmRtPrefEbgp = _AlaIprmRtPrefEbgp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 8),
    _AlaIprmRtPrefEbgp_Type()
)
alaIprmRtPrefEbgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmRtPrefEbgp.setStatus("current")


class _AlaIprmRtPrefIbgp_Type(Integer32):
    """Custom type alaIprmRtPrefIbgp based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaIprmRtPrefIbgp_Type.__name__ = "Integer32"
_AlaIprmRtPrefIbgp_Object = MibScalar
alaIprmRtPrefIbgp = _AlaIprmRtPrefIbgp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 9),
    _AlaIprmRtPrefIbgp_Type()
)
alaIprmRtPrefIbgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmRtPrefIbgp.setStatus("current")


class _AlaIprmRtPrefIsisL1_Type(Integer32):
    """Custom type alaIprmRtPrefIsisL1 based on Integer32"""
    defaultValue = 115

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaIprmRtPrefIsisL1_Type.__name__ = "Integer32"
_AlaIprmRtPrefIsisL1_Object = MibScalar
alaIprmRtPrefIsisL1 = _AlaIprmRtPrefIsisL1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 10),
    _AlaIprmRtPrefIsisL1_Type()
)
alaIprmRtPrefIsisL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmRtPrefIsisL1.setStatus("current")


class _AlaIprmRtPrefIsisL2_Type(Integer32):
    """Custom type alaIprmRtPrefIsisL2 based on Integer32"""
    defaultValue = 118

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaIprmRtPrefIsisL2_Type.__name__ = "Integer32"
_AlaIprmRtPrefIsisL2_Object = MibScalar
alaIprmRtPrefIsisL2 = _AlaIprmRtPrefIsisL2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 11),
    _AlaIprmRtPrefIsisL2_Type()
)
alaIprmRtPrefIsisL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmRtPrefIsisL2.setStatus("current")


class _AlaIprmStaticAllBfd_Type(AdminStatus):
    """Custom type alaIprmStaticAllBfd based on AdminStatus"""
    defaultValue = 2


_AlaIprmStaticAllBfd_Type.__name__ = "AdminStatus"
_AlaIprmStaticAllBfd_Object = MibScalar
alaIprmStaticAllBfd = _AlaIprmStaticAllBfd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 1, 1, 12),
    _AlaIprmStaticAllBfd_Type()
)
alaIprmStaticAllBfd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmStaticAllBfd.setStatus("current")
_AlcatelIND1IPRMMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IPRMMIBConformance = _AlcatelIND1IPRMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 2)
)
_AlcatelIND1IPRMMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IPRMMIBCompliances = _AlcatelIND1IPRMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 2, 1)
)
_AlcatelIND1IPRMMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IPRMMIBGroups = _AlcatelIND1IPRMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 2, 2)
)

# Managed Objects groups

alaIprmConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 2, 2, 1)
)
alaIprmConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-IPRM-MIB", "alaIprmRouteProto"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRouteMetric"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRoutePriority"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteMetric"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteStatus"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRtPrefLocal"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRtPrefStatic"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRtPrefOspf"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRtPrefRip"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRtPrefBgp"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRtPrefEbgp"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRtPrefIbgp"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRtPrefIsisL1"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRtPrefIsisL2"))
)
if mibBuilder.loadTexts:
    alaIprmConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaIprmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 2, 1, 2, 1, 1)
)
alaIprmCompliance.setObjects(
    ("ALCATEL-IND1-IPRM-MIB", "alaIprmConfigMIBGroup")
)
if mibBuilder.loadTexts:
    alaIprmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-IPRM-MIB",
    **{"AdminStatus": AdminStatus,
       "StaticRouteType": StaticRouteType,
       "alcatelIND1IPRMMIB": alcatelIND1IPRMMIB,
       "alcatelIND1IPRMMIBObjects": alcatelIND1IPRMMIBObjects,
       "alaIprmConfig": alaIprmConfig,
       "alaIprmRouteTable": alaIprmRouteTable,
       "alaIprmRouteEntry": alaIprmRouteEntry,
       "alaIprmRouteDest": alaIprmRouteDest,
       "alaIprmRouteMask": alaIprmRouteMask,
       "alaIprmRouteTos": alaIprmRouteTos,
       "alaIprmRouteNextHop": alaIprmRouteNextHop,
       "alaIprmRouteProto": alaIprmRouteProto,
       "alaIprmRouteMetric": alaIprmRouteMetric,
       "alaIprmRoutePriority": alaIprmRoutePriority,
       "alaIprmStaticRouteTable": alaIprmStaticRouteTable,
       "alaIprmStaticRouteEntry": alaIprmStaticRouteEntry,
       "alaIprmStaticRouteDest": alaIprmStaticRouteDest,
       "alaIprmStaticRouteMask": alaIprmStaticRouteMask,
       "alaIprmStaticRouteNextHop": alaIprmStaticRouteNextHop,
       "alaIprmStaticRouteMetric": alaIprmStaticRouteMetric,
       "alaIprmStaticRouteStatus": alaIprmStaticRouteStatus,
       "alaIprmStaticRouteBfdStatus": alaIprmStaticRouteBfdStatus,
       "alaIprmStaticRouteType": alaIprmStaticRouteType,
       "alaIprmRtPrefLocal": alaIprmRtPrefLocal,
       "alaIprmRtPrefStatic": alaIprmRtPrefStatic,
       "alaIprmRtPrefOspf": alaIprmRtPrefOspf,
       "alaIprmRtPrefRip": alaIprmRtPrefRip,
       "alaIprmRtPrefBgp": alaIprmRtPrefBgp,
       "alaIprmRtPrefEbgp": alaIprmRtPrefEbgp,
       "alaIprmRtPrefIbgp": alaIprmRtPrefIbgp,
       "alaIprmRtPrefIsisL1": alaIprmRtPrefIsisL1,
       "alaIprmRtPrefIsisL2": alaIprmRtPrefIsisL2,
       "alaIprmStaticAllBfd": alaIprmStaticAllBfd,
       "alcatelIND1IPRMMIBConformance": alcatelIND1IPRMMIBConformance,
       "alcatelIND1IPRMMIBCompliances": alcatelIND1IPRMMIBCompliances,
       "alaIprmCompliance": alaIprmCompliance,
       "alcatelIND1IPRMMIBGroups": alcatelIND1IPRMMIBGroups,
       "alaIprmConfigMIBGroup": alaIprmConfigMIBGroup}
)
