# SNMP MIB module (HH3C-IP-BROADCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-IP-BROADCAST-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:49 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cIpBroadcast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 33)
)
if mibBuilder.loadTexts:
    hh3cIpBroadcast.setRevisions(
        ("2004-12-13 19:36",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cIpBdstScalarGroup_ObjectIdentity = ObjectIdentity
hh3cIpBdstScalarGroup = _Hh3cIpBdstScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 33, 1)
)


class _Hh3cIpBdstForwardBroadcast_Type(Integer32):
    """Custom type hh3cIpBdstForwardBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notForwarding", 2))
    )


_Hh3cIpBdstForwardBroadcast_Type.__name__ = "Integer32"
_Hh3cIpBdstForwardBroadcast_Object = MibScalar
hh3cIpBdstForwardBroadcast = _Hh3cIpBdstForwardBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 33, 1, 1),
    _Hh3cIpBdstForwardBroadcast_Type()
)
hh3cIpBdstForwardBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpBdstForwardBroadcast.setStatus("current")


class _Hh3cIpReceiveBroadcast_Type(Integer32):
    """Custom type hh3cIpReceiveBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receive", 1),
          ("notReceive", 2))
    )


_Hh3cIpReceiveBroadcast_Type.__name__ = "Integer32"
_Hh3cIpReceiveBroadcast_Object = MibScalar
hh3cIpReceiveBroadcast = _Hh3cIpReceiveBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 33, 1, 2),
    _Hh3cIpReceiveBroadcast_Type()
)
hh3cIpReceiveBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpReceiveBroadcast.setStatus("current")
_Hh3cIpBdstGroup_ObjectIdentity = ObjectIdentity
hh3cIpBdstGroup = _Hh3cIpBdstGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 33, 2)
)
_Hh3cIpBdstTrap_ObjectIdentity = ObjectIdentity
hh3cIpBdstTrap = _Hh3cIpBdstTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 33, 3)
)
_Hh3cIpBdstTrapPrex_ObjectIdentity = ObjectIdentity
hh3cIpBdstTrapPrex = _Hh3cIpBdstTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 33, 3, 0)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-IP-BROADCAST-MIB",
    **{"hh3cIpBroadcast": hh3cIpBroadcast,
       "hh3cIpBdstScalarGroup": hh3cIpBdstScalarGroup,
       "hh3cIpBdstForwardBroadcast": hh3cIpBdstForwardBroadcast,
       "hh3cIpReceiveBroadcast": hh3cIpReceiveBroadcast,
       "hh3cIpBdstGroup": hh3cIpBdstGroup,
       "hh3cIpBdstTrap": hh3cIpBdstTrap,
       "hh3cIpBdstTrapPrex": hh3cIpBdstTrapPrex}
)
