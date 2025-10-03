# SNMP MIB module (CISCOSB-DHCPv6) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-DHCPv6
# Produced by pysmi-1.6.2 at Thu Oct  2 11:28:30 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType")

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

rlDhcpv6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlDhcpv6Common_ObjectIdentity = ObjectIdentity
rlDhcpv6Common = _RlDhcpv6Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 1)
)


class _RlDhcpv6DuidEn_Type(OctetString):
    """Custom type rlDhcpv6DuidEn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 38),
    )


_RlDhcpv6DuidEn_Type.__name__ = "OctetString"
_RlDhcpv6DuidEn_Object = MibScalar
rlDhcpv6DuidEn = _RlDhcpv6DuidEn_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 1, 1),
    _RlDhcpv6DuidEn_Type()
)
rlDhcpv6DuidEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDhcpv6DuidEn.setStatus("current")
_RlDhcpv6Client_ObjectIdentity = ObjectIdentity
rlDhcpv6Client = _RlDhcpv6Client_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 2)
)
_RlDhcpv6Relay_ObjectIdentity = ObjectIdentity
rlDhcpv6Relay = _RlDhcpv6Relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-DHCPv6",
    **{"rlDhcpv6": rlDhcpv6,
       "rlDhcpv6Common": rlDhcpv6Common,
       "rlDhcpv6DuidEn": rlDhcpv6DuidEn,
       "rlDhcpv6Client": rlDhcpv6Client,
       "rlDhcpv6Relay": rlDhcpv6Relay}
)
