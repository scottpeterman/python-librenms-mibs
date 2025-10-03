# SNMP MIB module (ALCATEL-IND1-OSPF3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-OSPF3-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:53 2025
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

(routingIND1Ospf3,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Ospf3")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1OSPF3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1OSPF3MIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1OSPF3MIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1OSPF3MIBObjects = _AlcatelIND1OSPF3MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1)
)
_AlaProtocolOspf3_ObjectIdentity = ObjectIdentity
alaProtocolOspf3 = _AlaProtocolOspf3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1)
)


class _AlaOspf3OrigRouteTag_Type(Unsigned32):
    """Custom type alaOspf3OrigRouteTag based on Unsigned32"""
    defaultValue = 0


_AlaOspf3OrigRouteTag_Type.__name__ = "Unsigned32"
_AlaOspf3OrigRouteTag_Object = MibScalar
alaOspf3OrigRouteTag = _AlaOspf3OrigRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 1),
    _AlaOspf3OrigRouteTag_Type()
)
alaOspf3OrigRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3OrigRouteTag.setStatus("current")


class _AlaOspf3TimerSpfDelay_Type(Integer32):
    """Custom type alaOspf3TimerSpfDelay based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspf3TimerSpfDelay_Type.__name__ = "Integer32"
_AlaOspf3TimerSpfDelay_Object = MibScalar
alaOspf3TimerSpfDelay = _AlaOspf3TimerSpfDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 2),
    _AlaOspf3TimerSpfDelay_Type()
)
alaOspf3TimerSpfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3TimerSpfDelay.setStatus("current")


class _AlaOspf3TimerSpfHold_Type(Integer32):
    """Custom type alaOspf3TimerSpfHold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaOspf3TimerSpfHold_Type.__name__ = "Integer32"
_AlaOspf3TimerSpfHold_Object = MibScalar
alaOspf3TimerSpfHold = _AlaOspf3TimerSpfHold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 3),
    _AlaOspf3TimerSpfHold_Type()
)
alaOspf3TimerSpfHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3TimerSpfHold.setStatus("current")


class _AlaOspf3RestartHelperSupport_Type(Integer32):
    """Custom type alaOspf3RestartHelperSupport based on Integer32"""
    defaultValue = 1

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


_AlaOspf3RestartHelperSupport_Type.__name__ = "Integer32"
_AlaOspf3RestartHelperSupport_Object = MibScalar
alaOspf3RestartHelperSupport = _AlaOspf3RestartHelperSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 4),
    _AlaOspf3RestartHelperSupport_Type()
)
alaOspf3RestartHelperSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3RestartHelperSupport.setStatus("current")


class _AlaOspf3RestartStrictLsaChecking_Type(Integer32):
    """Custom type alaOspf3RestartStrictLsaChecking based on Integer32"""
    defaultValue = 1

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


_AlaOspf3RestartStrictLsaChecking_Type.__name__ = "Integer32"
_AlaOspf3RestartStrictLsaChecking_Object = MibScalar
alaOspf3RestartStrictLsaChecking = _AlaOspf3RestartStrictLsaChecking_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 5),
    _AlaOspf3RestartStrictLsaChecking_Type()
)
alaOspf3RestartStrictLsaChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3RestartStrictLsaChecking.setStatus("current")


class _AlaOspf3RestartInitiate_Type(Integer32):
    """Custom type alaOspf3RestartInitiate based on Integer32"""
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


_AlaOspf3RestartInitiate_Type.__name__ = "Integer32"
_AlaOspf3RestartInitiate_Object = MibScalar
alaOspf3RestartInitiate = _AlaOspf3RestartInitiate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 6),
    _AlaOspf3RestartInitiate_Type()
)
alaOspf3RestartInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3RestartInitiate.setStatus("current")


class _AlaOspf3MTUCheck_Type(Integer32):
    """Custom type alaOspf3MTUCheck based on Integer32"""
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


_AlaOspf3MTUCheck_Type.__name__ = "Integer32"
_AlaOspf3MTUCheck_Object = MibScalar
alaOspf3MTUCheck = _AlaOspf3MTUCheck_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 7),
    _AlaOspf3MTUCheck_Type()
)
alaOspf3MTUCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOspf3MTUCheck.setStatus("current")
_AlcatelIND1OSPF3MIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1OSPF3MIBConformance = _AlcatelIND1OSPF3MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2)
)
_AlcatelIND1OSPF3MIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1OSPF3MIBCompliances = _AlcatelIND1OSPF3MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2, 1)
)
_AlcatelIND1OSPF3MIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1OSPF3MIBGroups = _AlcatelIND1OSPF3MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2, 2)
)

# Managed Objects groups

alaOSPF3ConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2, 2, 1)
)
alaOSPF3ConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-OSPF3-MIB", "alaOspf3OrigRouteTag"),
        ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3TimerSpfDelay"),
        ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3TimerSpfHold"),
        ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RestartHelperSupport"),
        ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RestartStrictLsaChecking"),
        ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RestartInitiate"),
        ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3MTUCheck"))
)
if mibBuilder.loadTexts:
    alaOSPF3ConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1OSPF3MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2, 1, 1)
)
alcatelIND1OSPF3MIBCompliance.setObjects(
    ("ALCATEL-IND1-OSPF3-MIB", "alaOSPF3ConfigMIBGroup")
)
if mibBuilder.loadTexts:
    alcatelIND1OSPF3MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-OSPF3-MIB",
    **{"alcatelIND1OSPF3MIB": alcatelIND1OSPF3MIB,
       "alcatelIND1OSPF3MIBObjects": alcatelIND1OSPF3MIBObjects,
       "alaProtocolOspf3": alaProtocolOspf3,
       "alaOspf3OrigRouteTag": alaOspf3OrigRouteTag,
       "alaOspf3TimerSpfDelay": alaOspf3TimerSpfDelay,
       "alaOspf3TimerSpfHold": alaOspf3TimerSpfHold,
       "alaOspf3RestartHelperSupport": alaOspf3RestartHelperSupport,
       "alaOspf3RestartStrictLsaChecking": alaOspf3RestartStrictLsaChecking,
       "alaOspf3RestartInitiate": alaOspf3RestartInitiate,
       "alaOspf3MTUCheck": alaOspf3MTUCheck,
       "alcatelIND1OSPF3MIBConformance": alcatelIND1OSPF3MIBConformance,
       "alcatelIND1OSPF3MIBCompliances": alcatelIND1OSPF3MIBCompliances,
       "alcatelIND1OSPF3MIBCompliance": alcatelIND1OSPF3MIBCompliance,
       "alcatelIND1OSPF3MIBGroups": alcatelIND1OSPF3MIBGroups,
       "alaOSPF3ConfigMIBGroup": alaOSPF3ConfigMIBGroup}
)
