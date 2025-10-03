# SNMP MIB module (SPSv1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bladeshelter\SPSv1-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:22 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Powertek_ObjectIdentity = ObjectIdentity
powertek = _Powertek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1)
)
_Pdu_ObjectIdentity = ObjectIdentity
pdu = _Pdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4)
)
_Sps_ObjectIdentity = ObjectIdentity
sps = _Sps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4)
)
_PduObjects_ObjectIdentity = ObjectIdentity
pduObjects = _PduObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1)
)
_PduIdent_ObjectIdentity = ObjectIdentity
pduIdent = _PduIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 1)
)


class _PduIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type pduIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_PduIdentAgentSoftwareVersion_Object = MibScalar
pduIdentAgentSoftwareVersion = _PduIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 1, 1),
    _PduIdentAgentSoftwareVersion_Type()
)
pduIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduIdentAgentSoftwareVersion.setStatus("mandatory")


class _PduIdentSerialNumber_Type(DisplayString):
    """Custom type pduIdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduIdentSerialNumber_Type.__name__ = "DisplayString"
_PduIdentSerialNumber_Object = MibScalar
pduIdentSerialNumber = _PduIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 1, 2),
    _PduIdentSerialNumber_Type()
)
pduIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduIdentSerialNumber.setStatus("mandatory")
_PduNetwork_ObjectIdentity = ObjectIdentity
pduNetwork = _PduNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2)
)
_PduNetworkTcpip_ObjectIdentity = ObjectIdentity
pduNetworkTcpip = _PduNetworkTcpip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1)
)


class _PduNetworkTcpipDhcpControl_Type(Integer32):
    """Custom type pduNetworkTcpipDhcpControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkTcpipDhcpControl_Type.__name__ = "Integer32"
_PduNetworkTcpipDhcpControl_Object = MibScalar
pduNetworkTcpipDhcpControl = _PduNetworkTcpipDhcpControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 1),
    _PduNetworkTcpipDhcpControl_Type()
)
pduNetworkTcpipDhcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipDhcpControl.setStatus("mandatory")
_PduNetworkTcpipIpv4_ObjectIdentity = ObjectIdentity
pduNetworkTcpipIpv4 = _PduNetworkTcpipIpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 2)
)
_PduNetworkTcpipIpv4Address_Type = IpAddress
_PduNetworkTcpipIpv4Address_Object = MibScalar
pduNetworkTcpipIpv4Address = _PduNetworkTcpipIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 2, 1),
    _PduNetworkTcpipIpv4Address_Type()
)
pduNetworkTcpipIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv4Address.setStatus("mandatory")
_PduNetworkTcpipIpv4Gateway_Type = IpAddress
_PduNetworkTcpipIpv4Gateway_Object = MibScalar
pduNetworkTcpipIpv4Gateway = _PduNetworkTcpipIpv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 2, 2),
    _PduNetworkTcpipIpv4Gateway_Type()
)
pduNetworkTcpipIpv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv4Gateway.setStatus("mandatory")
_PduNetworkTcpipIpv4Subnet_Type = IpAddress
_PduNetworkTcpipIpv4Subnet_Object = MibScalar
pduNetworkTcpipIpv4Subnet = _PduNetworkTcpipIpv4Subnet_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 2, 3),
    _PduNetworkTcpipIpv4Subnet_Type()
)
pduNetworkTcpipIpv4Subnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv4Subnet.setStatus("mandatory")
_PduNetworkTcpipIpv4PrimaryDNS_Type = IpAddress
_PduNetworkTcpipIpv4PrimaryDNS_Object = MibScalar
pduNetworkTcpipIpv4PrimaryDNS = _PduNetworkTcpipIpv4PrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 2, 4),
    _PduNetworkTcpipIpv4PrimaryDNS_Type()
)
pduNetworkTcpipIpv4PrimaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv4PrimaryDNS.setStatus("mandatory")
_PduNetworkTcpipIpv4SecondaryDNS_Type = IpAddress
_PduNetworkTcpipIpv4SecondaryDNS_Object = MibScalar
pduNetworkTcpipIpv4SecondaryDNS = _PduNetworkTcpipIpv4SecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 2, 5),
    _PduNetworkTcpipIpv4SecondaryDNS_Type()
)
pduNetworkTcpipIpv4SecondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv4SecondaryDNS.setStatus("mandatory")
_PduNetworkTcpipIpv6_ObjectIdentity = ObjectIdentity
pduNetworkTcpipIpv6 = _PduNetworkTcpipIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3)
)


class _PduNetworkTcpipIpv6Control_Type(Integer32):
    """Custom type pduNetworkTcpipIpv6Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkTcpipIpv6Control_Type.__name__ = "Integer32"
_PduNetworkTcpipIpv6Control_Object = MibScalar
pduNetworkTcpipIpv6Control = _PduNetworkTcpipIpv6Control_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3, 1),
    _PduNetworkTcpipIpv6Control_Type()
)
pduNetworkTcpipIpv6Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv6Control.setStatus("mandatory")


class _PduNetworkTcpipIpv6AutoConfig_Type(Integer32):
    """Custom type pduNetworkTcpipIpv6AutoConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_PduNetworkTcpipIpv6AutoConfig_Type.__name__ = "Integer32"
_PduNetworkTcpipIpv6AutoConfig_Object = MibScalar
pduNetworkTcpipIpv6AutoConfig = _PduNetworkTcpipIpv6AutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3, 2),
    _PduNetworkTcpipIpv6AutoConfig_Type()
)
pduNetworkTcpipIpv6AutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv6AutoConfig.setStatus("mandatory")


class _PduNetworkTcpipIpv6Address_Type(DisplayString):
    """Custom type pduNetworkTcpipIpv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduNetworkTcpipIpv6Address_Type.__name__ = "DisplayString"
_PduNetworkTcpipIpv6Address_Object = MibScalar
pduNetworkTcpipIpv6Address = _PduNetworkTcpipIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3, 3),
    _PduNetworkTcpipIpv6Address_Type()
)
pduNetworkTcpipIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv6Address.setStatus("mandatory")
_PduNetworkTcpipIpv6Prefix_Type = Integer32
_PduNetworkTcpipIpv6Prefix_Object = MibScalar
pduNetworkTcpipIpv6Prefix = _PduNetworkTcpipIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3, 4),
    _PduNetworkTcpipIpv6Prefix_Type()
)
pduNetworkTcpipIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv6Prefix.setStatus("mandatory")


class _PduNetworkTcpipIpv6Router_Type(DisplayString):
    """Custom type pduNetworkTcpipIpv6Router based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduNetworkTcpipIpv6Router_Type.__name__ = "DisplayString"
_PduNetworkTcpipIpv6Router_Object = MibScalar
pduNetworkTcpipIpv6Router = _PduNetworkTcpipIpv6Router_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3, 5),
    _PduNetworkTcpipIpv6Router_Type()
)
pduNetworkTcpipIpv6Router.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv6Router.setStatus("mandatory")


class _PduNetworkTcpipIpv6PrimaryDNS_Type(DisplayString):
    """Custom type pduNetworkTcpipIpv6PrimaryDNS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduNetworkTcpipIpv6PrimaryDNS_Type.__name__ = "DisplayString"
_PduNetworkTcpipIpv6PrimaryDNS_Object = MibScalar
pduNetworkTcpipIpv6PrimaryDNS = _PduNetworkTcpipIpv6PrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3, 6),
    _PduNetworkTcpipIpv6PrimaryDNS_Type()
)
pduNetworkTcpipIpv6PrimaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv6PrimaryDNS.setStatus("mandatory")


class _PduNetworkTcpipIpv6SecondaryDNS_Type(DisplayString):
    """Custom type pduNetworkTcpipIpv6SecondaryDNS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduNetworkTcpipIpv6SecondaryDNS_Type.__name__ = "DisplayString"
_PduNetworkTcpipIpv6SecondaryDNS_Object = MibScalar
pduNetworkTcpipIpv6SecondaryDNS = _PduNetworkTcpipIpv6SecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 1, 3, 7),
    _PduNetworkTcpipIpv6SecondaryDNS_Type()
)
pduNetworkTcpipIpv6SecondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkTcpipIpv6SecondaryDNS.setStatus("mandatory")
_PduNetworkSecurity_ObjectIdentity = ObjectIdentity
pduNetworkSecurity = _PduNetworkSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2)
)


class _PduNetworkSecurityControl_Type(Integer32):
    """Custom type pduNetworkSecurityControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkSecurityControl_Type.__name__ = "Integer32"
_PduNetworkSecurityControl_Object = MibScalar
pduNetworkSecurityControl = _PduNetworkSecurityControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 1),
    _PduNetworkSecurityControl_Type()
)
pduNetworkSecurityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecurityControl.setStatus("mandatory")
_PduNetworkSecuritySsh_ObjectIdentity = ObjectIdentity
pduNetworkSecuritySsh = _PduNetworkSecuritySsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 2)
)


class _PduNetworkSecuritySshControl_Type(Integer32):
    """Custom type pduNetworkSecuritySshControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkSecuritySshControl_Type.__name__ = "Integer32"
_PduNetworkSecuritySshControl_Object = MibScalar
pduNetworkSecuritySshControl = _PduNetworkSecuritySshControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 2, 1),
    _PduNetworkSecuritySshControl_Type()
)
pduNetworkSecuritySshControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySshControl.setStatus("mandatory")


class _PduNetworkSecuritySshInterval_Type(Integer32):
    """Custom type pduNetworkSecuritySshInterval based on Integer32"""
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
        *(("oneMinute", 1),
          ("fiveMinutes", 2),
          ("tenMinutes", 3),
          ("thirtyMinutes", 4))
    )


_PduNetworkSecuritySshInterval_Type.__name__ = "Integer32"
_PduNetworkSecuritySshInterval_Object = MibScalar
pduNetworkSecuritySshInterval = _PduNetworkSecuritySshInterval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 2, 2),
    _PduNetworkSecuritySshInterval_Type()
)
pduNetworkSecuritySshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySshInterval.setStatus("mandatory")


class _PduNetworkSecuritySshFailTimes_Type(Integer32):
    """Custom type pduNetworkSecuritySshFailTimes based on Integer32"""
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
        *(("five", 1),
          ("ten", 2),
          ("twenty", 3),
          ("thirty", 4),
          ("hundred", 5))
    )


_PduNetworkSecuritySshFailTimes_Type.__name__ = "Integer32"
_PduNetworkSecuritySshFailTimes_Object = MibScalar
pduNetworkSecuritySshFailTimes = _PduNetworkSecuritySshFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 2, 3),
    _PduNetworkSecuritySshFailTimes_Type()
)
pduNetworkSecuritySshFailTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySshFailTimes.setStatus("mandatory")


class _PduNetworkSecuritySshBlock_Type(Integer32):
    """Custom type pduNetworkSecuritySshBlock based on Integer32"""
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
        *(("fiveMinutes", 1),
          ("thirtyMinutes", 2),
          ("oneHour", 3),
          ("oneDay", 4))
    )


_PduNetworkSecuritySshBlock_Type.__name__ = "Integer32"
_PduNetworkSecuritySshBlock_Object = MibScalar
pduNetworkSecuritySshBlock = _PduNetworkSecuritySshBlock_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 2, 4),
    _PduNetworkSecuritySshBlock_Type()
)
pduNetworkSecuritySshBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySshBlock.setStatus("mandatory")
_PduNetworkSecuritySnmp_ObjectIdentity = ObjectIdentity
pduNetworkSecuritySnmp = _PduNetworkSecuritySnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 3)
)


class _PduNetworkSecuritySnmpControl_Type(Integer32):
    """Custom type pduNetworkSecuritySnmpControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkSecuritySnmpControl_Type.__name__ = "Integer32"
_PduNetworkSecuritySnmpControl_Object = MibScalar
pduNetworkSecuritySnmpControl = _PduNetworkSecuritySnmpControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 3, 1),
    _PduNetworkSecuritySnmpControl_Type()
)
pduNetworkSecuritySnmpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySnmpControl.setStatus("mandatory")


class _PduNetworkSecuritySnmpInterval_Type(Integer32):
    """Custom type pduNetworkSecuritySnmpInterval based on Integer32"""
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
        *(("oneMinute", 1),
          ("fiveMinutes", 2),
          ("tenMinutes", 3),
          ("thirtyMinutes", 4))
    )


_PduNetworkSecuritySnmpInterval_Type.__name__ = "Integer32"
_PduNetworkSecuritySnmpInterval_Object = MibScalar
pduNetworkSecuritySnmpInterval = _PduNetworkSecuritySnmpInterval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 3, 2),
    _PduNetworkSecuritySnmpInterval_Type()
)
pduNetworkSecuritySnmpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySnmpInterval.setStatus("mandatory")


class _PduNetworkSecuritySnmpFailTimes_Type(Integer32):
    """Custom type pduNetworkSecuritySnmpFailTimes based on Integer32"""
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
        *(("five", 1),
          ("ten", 2),
          ("twenty", 3),
          ("thirty", 4),
          ("hundred", 5))
    )


_PduNetworkSecuritySnmpFailTimes_Type.__name__ = "Integer32"
_PduNetworkSecuritySnmpFailTimes_Object = MibScalar
pduNetworkSecuritySnmpFailTimes = _PduNetworkSecuritySnmpFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 3, 3),
    _PduNetworkSecuritySnmpFailTimes_Type()
)
pduNetworkSecuritySnmpFailTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySnmpFailTimes.setStatus("mandatory")


class _PduNetworkSecuritySnmpBlock_Type(Integer32):
    """Custom type pduNetworkSecuritySnmpBlock based on Integer32"""
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
        *(("fiveMinutes", 1),
          ("thirtyMinutes", 2),
          ("oneHour", 3),
          ("oneDay", 4))
    )


_PduNetworkSecuritySnmpBlock_Type.__name__ = "Integer32"
_PduNetworkSecuritySnmpBlock_Object = MibScalar
pduNetworkSecuritySnmpBlock = _PduNetworkSecuritySnmpBlock_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 3, 4),
    _PduNetworkSecuritySnmpBlock_Type()
)
pduNetworkSecuritySnmpBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecuritySnmpBlock.setStatus("mandatory")
_PduNetworkSecurityHttp_ObjectIdentity = ObjectIdentity
pduNetworkSecurityHttp = _PduNetworkSecurityHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 4)
)


class _PduNetworkSecurityHttpControl_Type(Integer32):
    """Custom type pduNetworkSecurityHttpControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkSecurityHttpControl_Type.__name__ = "Integer32"
_PduNetworkSecurityHttpControl_Object = MibScalar
pduNetworkSecurityHttpControl = _PduNetworkSecurityHttpControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 4, 1),
    _PduNetworkSecurityHttpControl_Type()
)
pduNetworkSecurityHttpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecurityHttpControl.setStatus("mandatory")


class _PduNetworkSecurityHttpInterval_Type(Integer32):
    """Custom type pduNetworkSecurityHttpInterval based on Integer32"""
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
        *(("oneMinute", 1),
          ("fiveMinutes", 2),
          ("tenMinutes", 3),
          ("thirtyMinutes", 4))
    )


_PduNetworkSecurityHttpInterval_Type.__name__ = "Integer32"
_PduNetworkSecurityHttpInterval_Object = MibScalar
pduNetworkSecurityHttpInterval = _PduNetworkSecurityHttpInterval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 4, 2),
    _PduNetworkSecurityHttpInterval_Type()
)
pduNetworkSecurityHttpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecurityHttpInterval.setStatus("mandatory")


class _PduNetworkSecurityHttpFailTimes_Type(Integer32):
    """Custom type pduNetworkSecurityHttpFailTimes based on Integer32"""
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
        *(("five", 1),
          ("ten", 2),
          ("twenty", 3),
          ("thirty", 4),
          ("hundred", 5))
    )


_PduNetworkSecurityHttpFailTimes_Type.__name__ = "Integer32"
_PduNetworkSecurityHttpFailTimes_Object = MibScalar
pduNetworkSecurityHttpFailTimes = _PduNetworkSecurityHttpFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 4, 3),
    _PduNetworkSecurityHttpFailTimes_Type()
)
pduNetworkSecurityHttpFailTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecurityHttpFailTimes.setStatus("mandatory")


class _PduNetworkSecurityHttpBlock_Type(Integer32):
    """Custom type pduNetworkSecurityHttpBlock based on Integer32"""
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
        *(("fiveMinutes", 1),
          ("thirtyMinutes", 2),
          ("oneHour", 3),
          ("oneDay", 4))
    )


_PduNetworkSecurityHttpBlock_Type.__name__ = "Integer32"
_PduNetworkSecurityHttpBlock_Object = MibScalar
pduNetworkSecurityHttpBlock = _PduNetworkSecurityHttpBlock_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 2, 4, 4),
    _PduNetworkSecurityHttpBlock_Type()
)
pduNetworkSecurityHttpBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkSecurityHttpBlock.setStatus("mandatory")
_PduNetworkService_ObjectIdentity = ObjectIdentity
pduNetworkService = _PduNetworkService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3)
)
_PduNetworkServiceSsh_ObjectIdentity = ObjectIdentity
pduNetworkServiceSsh = _PduNetworkServiceSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 1)
)


class _PduNetworkServiceSshControl_Type(Integer32):
    """Custom type pduNetworkServiceSshControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkServiceSshControl_Type.__name__ = "Integer32"
_PduNetworkServiceSshControl_Object = MibScalar
pduNetworkServiceSshControl = _PduNetworkServiceSshControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 1, 1),
    _PduNetworkServiceSshControl_Type()
)
pduNetworkServiceSshControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceSshControl.setStatus("mandatory")
_PduNetworkServiceSshPort_Type = Integer32
_PduNetworkServiceSshPort_Object = MibScalar
pduNetworkServiceSshPort = _PduNetworkServiceSshPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 1, 2),
    _PduNetworkServiceSshPort_Type()
)
pduNetworkServiceSshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceSshPort.setStatus("mandatory")
_PduNetworkServiceSsl_ObjectIdentity = ObjectIdentity
pduNetworkServiceSsl = _PduNetworkServiceSsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 2)
)


class _PduNetworkServiceSslControl_Type(Integer32):
    """Custom type pduNetworkServiceSslControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkServiceSslControl_Type.__name__ = "Integer32"
_PduNetworkServiceSslControl_Object = MibScalar
pduNetworkServiceSslControl = _PduNetworkServiceSslControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 2, 1),
    _PduNetworkServiceSslControl_Type()
)
pduNetworkServiceSslControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceSslControl.setStatus("mandatory")
_PduNetworkServiceSslPort_Type = Integer32
_PduNetworkServiceSslPort_Object = MibScalar
pduNetworkServiceSslPort = _PduNetworkServiceSslPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 2, 2),
    _PduNetworkServiceSslPort_Type()
)
pduNetworkServiceSslPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceSslPort.setStatus("mandatory")


class _PduNetworkServiceSslForce_Type(Integer32):
    """Custom type pduNetworkServiceSslForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkServiceSslForce_Type.__name__ = "Integer32"
_PduNetworkServiceSslForce_Object = MibScalar
pduNetworkServiceSslForce = _PduNetworkServiceSslForce_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 2, 3),
    _PduNetworkServiceSslForce_Type()
)
pduNetworkServiceSslForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceSslForce.setStatus("mandatory")


class _PduNetworkServicePingControl_Type(Integer32):
    """Custom type pduNetworkServicePingControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkServicePingControl_Type.__name__ = "Integer32"
_PduNetworkServicePingControl_Object = MibScalar
pduNetworkServicePingControl = _PduNetworkServicePingControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 3),
    _PduNetworkServicePingControl_Type()
)
pduNetworkServicePingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServicePingControl.setStatus("mandatory")
_PduNetworkServiceRadius_ObjectIdentity = ObjectIdentity
pduNetworkServiceRadius = _PduNetworkServiceRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 4)
)


class _PduNetworkServiceRadiusControl_Type(Integer32):
    """Custom type pduNetworkServiceRadiusControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduNetworkServiceRadiusControl_Type.__name__ = "Integer32"
_PduNetworkServiceRadiusControl_Object = MibScalar
pduNetworkServiceRadiusControl = _PduNetworkServiceRadiusControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 4, 1),
    _PduNetworkServiceRadiusControl_Type()
)
pduNetworkServiceRadiusControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceRadiusControl.setStatus("mandatory")


class _PduNetworkServiceRadiusIp_Type(DisplayString):
    """Custom type pduNetworkServiceRadiusIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduNetworkServiceRadiusIp_Type.__name__ = "DisplayString"
_PduNetworkServiceRadiusIp_Object = MibScalar
pduNetworkServiceRadiusIp = _PduNetworkServiceRadiusIp_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 4, 2),
    _PduNetworkServiceRadiusIp_Type()
)
pduNetworkServiceRadiusIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceRadiusIp.setStatus("mandatory")
_PduNetworkServiceRadiusPort_Type = Integer32
_PduNetworkServiceRadiusPort_Object = MibScalar
pduNetworkServiceRadiusPort = _PduNetworkServiceRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 4, 3),
    _PduNetworkServiceRadiusPort_Type()
)
pduNetworkServiceRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceRadiusPort.setStatus("mandatory")


class _PduNetworkServiceRadiusSecretKey_Type(DisplayString):
    """Custom type pduNetworkServiceRadiusSecretKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduNetworkServiceRadiusSecretKey_Type.__name__ = "DisplayString"
_PduNetworkServiceRadiusSecretKey_Object = MibScalar
pduNetworkServiceRadiusSecretKey = _PduNetworkServiceRadiusSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 4, 4),
    _PduNetworkServiceRadiusSecretKey_Type()
)
pduNetworkServiceRadiusSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceRadiusSecretKey.setStatus("mandatory")
_PduNetworkServiceRadiusTimeout_Type = Integer32
_PduNetworkServiceRadiusTimeout_Object = MibScalar
pduNetworkServiceRadiusTimeout = _PduNetworkServiceRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 4, 5),
    _PduNetworkServiceRadiusTimeout_Type()
)
pduNetworkServiceRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceRadiusTimeout.setStatus("mandatory")
_PduNetworkServiceRadiusRetry_Type = Integer32
_PduNetworkServiceRadiusRetry_Object = MibScalar
pduNetworkServiceRadiusRetry = _PduNetworkServiceRadiusRetry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 2, 3, 4, 6),
    _PduNetworkServiceRadiusRetry_Type()
)
pduNetworkServiceRadiusRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetworkServiceRadiusRetry.setStatus("mandatory")
_PduSystem_ObjectIdentity = ObjectIdentity
pduSystem = _PduSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3)
)


class _PduSystemName_Type(DisplayString):
    """Custom type pduSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSystemName_Type.__name__ = "DisplayString"
_PduSystemName_Object = MibScalar
pduSystemName = _PduSystemName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 1),
    _PduSystemName_Type()
)
pduSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemName.setStatus("mandatory")


class _PduSystemContact_Type(DisplayString):
    """Custom type pduSystemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSystemContact_Type.__name__ = "DisplayString"
_PduSystemContact_Object = MibScalar
pduSystemContact = _PduSystemContact_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 2),
    _PduSystemContact_Type()
)
pduSystemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemContact.setStatus("mandatory")


class _PduSystemLocation_Type(DisplayString):
    """Custom type pduSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSystemLocation_Type.__name__ = "DisplayString"
_PduSystemLocation_Object = MibScalar
pduSystemLocation = _PduSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 3),
    _PduSystemLocation_Type()
)
pduSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemLocation.setStatus("mandatory")
_PduSystemLogInterval_Type = Integer32
_PduSystemLogInterval_Object = MibScalar
pduSystemLogInterval = _PduSystemLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 4),
    _PduSystemLogInterval_Type()
)
pduSystemLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemLogInterval.setStatus("mandatory")


class _PduSystemWebRefresh_Type(Integer32):
    """Custom type pduSystemWebRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_PduSystemWebRefresh_Type.__name__ = "Integer32"
_PduSystemWebRefresh_Object = MibScalar
pduSystemWebRefresh = _PduSystemWebRefresh_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 5),
    _PduSystemWebRefresh_Type()
)
pduSystemWebRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemWebRefresh.setStatus("mandatory")
_PduSystemTime_ObjectIdentity = ObjectIdentity
pduSystemTime = _PduSystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6)
)
_PduSystemTimeDisplay_Type = DisplayString
_PduSystemTimeDisplay_Object = MibScalar
pduSystemTimeDisplay = _PduSystemTimeDisplay_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 1),
    _PduSystemTimeDisplay_Type()
)
pduSystemTimeDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduSystemTimeDisplay.setStatus("mandatory")


class _PduSystemTimeZone_Type(Integer32):
    """Custom type pduSystemTimeZone based on Integer32"""
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
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77)
        )
    )
    namedValues = NamedValues(
        *(("gMT-1200InternationalDateLineWest", 1),
          ("gMT-1200Eniwetok-Kwajalein", 2),
          ("gMT-1100MidwayIsland-Samoa", 3),
          ("gMT-1000Hawaii", 4),
          ("gMT-0900Alaska", 5),
          ("gMT-0800PacificTime-Tijuana", 6),
          ("gMT-0700Arizona-MountainTime", 7),
          ("gMT-0700Chihuahua-LaPaz-Mazatlan", 8),
          ("gMT-0700MountainTime", 9),
          ("gMT-0600CentralAmerica", 10),
          ("gMT-0600CentralTime", 11),
          ("gMT-0600Guadalajara-MexicoCity-Monterrey", 12),
          ("gMT-0600Saskatchewan", 13),
          ("gMT-0500Bogota-Lima-Quito", 14),
          ("gMT-0500EasternTime", 15),
          ("gMT-0500Indiana", 16),
          ("gMT-0400AtlanticTime", 17),
          ("gMT-0400Caracas-LaPaz", 18),
          ("gMT-0400Santiago", 19),
          ("gMT-0330Newfoundland", 20),
          ("gMT-0300Brasilia", 21),
          ("gMT-0300BuenosAires-Georgetown", 22),
          ("gMT-0300Greenland", 23),
          ("gMT-0200Mid-Atlantic", 24),
          ("gMT-0100Azores", 25),
          ("gMT-0100CapeVerdeIs", 26),
          ("gMT-0000Casablanca-Monrovia", 27),
          ("gMT-0000GreenwichMeanTime-Dublin-Edinburgh-Lisbon-London", 28),
          ("gMT0100Amsterdam-Berlin-Bern-Rome-Stockholm-Vienna", 29),
          ("gMT0100Belgrade-Bratislava-Budapest-Ljubljana-Prague", 30),
          ("gMT0100Brussels-Copenhagen-Madrid-Paris", 31),
          ("gMT0100Sarajevo-Skopje-Warsaw-Zagreb", 32),
          ("gMT0100WestCentralAfrica", 33),
          ("gMT0200Athens-Istanbul-Minsk", 34),
          ("gMT0200Bucharest", 35),
          ("gMT0200Cairo", 36),
          ("gMT0200Harare-Pretoria", 37),
          ("gMT0200Helsinki-Kyiv-Riga-Sofia-Tallinn-Vilnius", 38),
          ("gMT0200Jerusalem", 39),
          ("gMT0300Baghdad", 40),
          ("gMT0300Kuwait-Riyadh", 41),
          ("gMT0300Moscow-StPetersburg-Volgograd", 42),
          ("gMT0300Nairobi", 43),
          ("gMT0330Tehran", 44),
          ("gMT0400AbuDhabi-Muscat", 45),
          ("gMT0400Baku-Tbilisi-Yerevan", 46),
          ("gMT0430Kabul", 47),
          ("gMT0500Ekaterinburg", 48),
          ("gMT0500Islamabad-Karachi-Tashkent", 49),
          ("gMT0530Bombay-Calcutta", 50),
          ("gMT0530Chennai-Kolkata-Mumbai-NewDelhi", 51),
          ("gMT0545Kathmandu", 52),
          ("gMT0600Almaty-Novosibirsk", 53),
          ("gMT0600Astana-Dhaka", 54),
          ("gMT0600SriJayawardenepura", 55),
          ("gMT0630Rangoon", 56),
          ("gMT0700Bangkok-Hanoi-Jakarta", 57),
          ("gMT0700Krasnoyarsk", 58),
          ("gMT0800Beijing-Chongqing-HongKong-Urumqi", 59),
          ("gMT0800Irkutsk-UlaanBataar", 60),
          ("gMT0800KualaLumpur-Singapore", 61),
          ("gMT0800Perth", 62),
          ("gMT0800Taipei", 63),
          ("gMT0900Osaka-Sapporo-Tokyo", 64),
          ("gMT0900Seoul", 65),
          ("gMT0900Yakutsk", 66),
          ("gMT0930Adelaide", 67),
          ("gMT0930Darwin", 68),
          ("gMT1000Brisbane", 69),
          ("gMT1000Canberra-Melbourne-Sydney", 70),
          ("gMT1000Guam-PortMoresby", 71),
          ("gMT1000Hobart", 72),
          ("gMT1000Vladivostok", 73),
          ("gMT1100Magadan-SolomonIs-NewCaledonia", 74),
          ("gMT1200Auckland-Wellington", 75),
          ("gMT1200Fiji-Kamchatka-MarshallIs", 76),
          ("gMT1300NukuAlofa", 77))
    )


_PduSystemTimeZone_Type.__name__ = "Integer32"
_PduSystemTimeZone_Object = MibScalar
pduSystemTimeZone = _PduSystemTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 2),
    _PduSystemTimeZone_Type()
)
pduSystemTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeZone.setStatus("mandatory")


class _PduSystemTimeFormat_Type(Integer32):
    """Custom type pduSystemTimeFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mmddyyyy", 1),
          ("ddmmyyyy", 2),
          ("yyyymmdd", 3))
    )


_PduSystemTimeFormat_Type.__name__ = "Integer32"
_PduSystemTimeFormat_Object = MibScalar
pduSystemTimeFormat = _PduSystemTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 3),
    _PduSystemTimeFormat_Type()
)
pduSystemTimeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeFormat.setStatus("mandatory")


class _PduSystemTimeSetting_Type(Integer32):
    """Custom type pduSystemTimeSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twentyFourHrFormat", 1),
          ("twelveHrFormat", 2))
    )


_PduSystemTimeSetting_Type.__name__ = "Integer32"
_PduSystemTimeSetting_Object = MibScalar
pduSystemTimeSetting = _PduSystemTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 4),
    _PduSystemTimeSetting_Type()
)
pduSystemTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeSetting.setStatus("mandatory")


class _PduSystemTimeDayLightSaving_Type(Integer32):
    """Custom type pduSystemTimeDayLightSaving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduSystemTimeDayLightSaving_Type.__name__ = "Integer32"
_PduSystemTimeDayLightSaving_Object = MibScalar
pduSystemTimeDayLightSaving = _PduSystemTimeDayLightSaving_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 5),
    _PduSystemTimeDayLightSaving_Type()
)
pduSystemTimeDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeDayLightSaving.setStatus("mandatory")
_PduSystemTimeManual_ObjectIdentity = ObjectIdentity
pduSystemTimeManual = _PduSystemTimeManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 6)
)


class _PduSystemTimeManualDate_Type(DisplayString):
    """Custom type pduSystemTimeManualDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_PduSystemTimeManualDate_Type.__name__ = "DisplayString"
_PduSystemTimeManualDate_Object = MibScalar
pduSystemTimeManualDate = _PduSystemTimeManualDate_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 6, 1),
    _PduSystemTimeManualDate_Type()
)
pduSystemTimeManualDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeManualDate.setStatus("mandatory")


class _PduSystemTimeManualTime_Type(DisplayString):
    """Custom type pduSystemTimeManualTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_PduSystemTimeManualTime_Type.__name__ = "DisplayString"
_PduSystemTimeManualTime_Object = MibScalar
pduSystemTimeManualTime = _PduSystemTimeManualTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 6, 2),
    _PduSystemTimeManualTime_Type()
)
pduSystemTimeManualTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeManualTime.setStatus("mandatory")
_PduSystemTimeNtp_ObjectIdentity = ObjectIdentity
pduSystemTimeNtp = _PduSystemTimeNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 7)
)


class _PduSystemTimeNtpControl_Type(Integer32):
    """Custom type pduSystemTimeNtpControl based on Integer32"""
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


_PduSystemTimeNtpControl_Type.__name__ = "Integer32"
_PduSystemTimeNtpControl_Object = MibScalar
pduSystemTimeNtpControl = _PduSystemTimeNtpControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 7, 1),
    _PduSystemTimeNtpControl_Type()
)
pduSystemTimeNtpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeNtpControl.setStatus("mandatory")


class _PduSystemTimeNtpServer_Type(DisplayString):
    """Custom type pduSystemTimeNtpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduSystemTimeNtpServer_Type.__name__ = "DisplayString"
_PduSystemTimeNtpServer_Object = MibScalar
pduSystemTimeNtpServer = _PduSystemTimeNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 7, 2),
    _PduSystemTimeNtpServer_Type()
)
pduSystemTimeNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeNtpServer.setStatus("mandatory")
_PduSystemTimeNtpSyncInterval_Type = Integer32
_PduSystemTimeNtpSyncInterval_Object = MibScalar
pduSystemTimeNtpSyncInterval = _PduSystemTimeNtpSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 7, 3),
    _PduSystemTimeNtpSyncInterval_Type()
)
pduSystemTimeNtpSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeNtpSyncInterval.setStatus("mandatory")


class _PduSystemTimeNtpSyncUnit_Type(Integer32):
    """Custom type pduSystemTimeNtpSyncUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("day", 1),
          ("month", 2))
    )


_PduSystemTimeNtpSyncUnit_Type.__name__ = "Integer32"
_PduSystemTimeNtpSyncUnit_Object = MibScalar
pduSystemTimeNtpSyncUnit = _PduSystemTimeNtpSyncUnit_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 6, 7, 4),
    _PduSystemTimeNtpSyncUnit_Type()
)
pduSystemTimeNtpSyncUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemTimeNtpSyncUnit.setStatus("mandatory")


class _PduSystemResetToDefault_Type(Integer32):
    """Custom type pduSystemResetToDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 1),
          ("reset", 2))
    )


_PduSystemResetToDefault_Type.__name__ = "Integer32"
_PduSystemResetToDefault_Object = MibScalar
pduSystemResetToDefault = _PduSystemResetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 7),
    _PduSystemResetToDefault_Type()
)
pduSystemResetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemResetToDefault.setStatus("mandatory")


class _PduSystemReboot_Type(Integer32):
    """Custom type pduSystemReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 1),
          ("reboot", 2))
    )


_PduSystemReboot_Type.__name__ = "Integer32"
_PduSystemReboot_Object = MibScalar
pduSystemReboot = _PduSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 3, 8),
    _PduSystemReboot_Type()
)
pduSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSystemReboot.setStatus("mandatory")
_PduSNMP_ObjectIdentity = ObjectIdentity
pduSNMP = _PduSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4)
)


class _PduSnmpControl_Type(Integer32):
    """Custom type pduSnmpControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduSnmpControl_Type.__name__ = "Integer32"
_PduSnmpControl_Object = MibScalar
pduSnmpControl = _PduSnmpControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 1),
    _PduSnmpControl_Type()
)
pduSnmpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpControl.setStatus("mandatory")
_PduSnmpPort_Type = Integer32
_PduSnmpPort_Object = MibScalar
pduSnmpPort = _PduSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 2),
    _PduSnmpPort_Type()
)
pduSnmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpPort.setStatus("mandatory")


class _PduSnmpVersion_Type(Integer32):
    """Custom type pduSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_PduSnmpVersion_Type.__name__ = "Integer32"
_PduSnmpVersion_Object = MibScalar
pduSnmpVersion = _PduSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 3),
    _PduSnmpVersion_Type()
)
pduSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpVersion.setStatus("mandatory")
_PduSnmpTrapsReceiversTable_Object = MibTable
pduSnmpTrapsReceiversTable = _PduSnmpTrapsReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 4)
)
if mibBuilder.loadTexts:
    pduSnmpTrapsReceiversTable.setStatus("mandatory")
_PduSnmpTrapsReceiversEntry_Object = MibTableRow
pduSnmpTrapsReceiversEntry = _PduSnmpTrapsReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 4, 1)
)
pduSnmpTrapsReceiversEntry.setIndexNames(
    (0, "SPSv1-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    pduSnmpTrapsReceiversEntry.setStatus("mandatory")


class _TrapsIndex_Type(Integer32):
    """Custom type trapsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TrapsIndex_Type.__name__ = "Integer32"
_TrapsIndex_Object = MibTableColumn
trapsIndex = _TrapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 4, 1, 1),
    _TrapsIndex_Type()
)
trapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsIndex.setStatus("mandatory")


class _TrapsReceiverAddr_Type(DisplayString):
    """Custom type trapsReceiverAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TrapsReceiverAddr_Type.__name__ = "DisplayString"
_TrapsReceiverAddr_Object = MibTableColumn
trapsReceiverAddr = _TrapsReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 4, 1, 2),
    _TrapsReceiverAddr_Type()
)
trapsReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsReceiverAddr.setStatus("mandatory")


class _ReceiverEventLevel_Type(Integer32):
    """Custom type receiverEventLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("informational", 3))
    )


_ReceiverEventLevel_Type.__name__ = "Integer32"
_ReceiverEventLevel_Object = MibTableColumn
receiverEventLevel = _ReceiverEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 4, 1, 3),
    _ReceiverEventLevel_Type()
)
receiverEventLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverEventLevel.setStatus("mandatory")


class _ReceiverSnmpVer_Type(Integer32):
    """Custom type receiverSnmpVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_ReceiverSnmpVer_Type.__name__ = "Integer32"
_ReceiverSnmpVer_Object = MibTableColumn
receiverSnmpVer = _ReceiverSnmpVer_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 4, 1, 4),
    _ReceiverSnmpVer_Type()
)
receiverSnmpVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverSnmpVer.setStatus("mandatory")


class _ReceiverDescription_Type(DisplayString):
    """Custom type receiverDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ReceiverDescription_Type.__name__ = "DisplayString"
_ReceiverDescription_Object = MibTableColumn
receiverDescription = _ReceiverDescription_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 4, 4, 1, 5),
    _ReceiverDescription_Type()
)
receiverDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverDescription.setStatus("mandatory")
_PduEmail_ObjectIdentity = ObjectIdentity
pduEmail = _PduEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5)
)


class _PduEmailServer_Type(DisplayString):
    """Custom type pduEmailServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduEmailServer_Type.__name__ = "DisplayString"
_PduEmailServer_Object = MibScalar
pduEmailServer = _PduEmailServer_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 1),
    _PduEmailServer_Type()
)
pduEmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailServer.setStatus("mandatory")
_PduEmailPort_Type = Integer32
_PduEmailPort_Object = MibScalar
pduEmailPort = _PduEmailPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 2),
    _PduEmailPort_Type()
)
pduEmailPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailPort.setStatus("mandatory")


class _PduEmailSenderEmail_Type(DisplayString):
    """Custom type pduEmailSenderEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduEmailSenderEmail_Type.__name__ = "DisplayString"
_PduEmailSenderEmail_Object = MibScalar
pduEmailSenderEmail = _PduEmailSenderEmail_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 3),
    _PduEmailSenderEmail_Type()
)
pduEmailSenderEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailSenderEmail.setStatus("mandatory")


class _PduEmailPrefix_Type(DisplayString):
    """Custom type pduEmailPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduEmailPrefix_Type.__name__ = "DisplayString"
_PduEmailPrefix_Object = MibScalar
pduEmailPrefix = _PduEmailPrefix_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 4),
    _PduEmailPrefix_Type()
)
pduEmailPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailPrefix.setStatus("mandatory")


class _PduEmailAuthControl_Type(Integer32):
    """Custom type pduEmailAuthControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduEmailAuthControl_Type.__name__ = "Integer32"
_PduEmailAuthControl_Object = MibScalar
pduEmailAuthControl = _PduEmailAuthControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 5),
    _PduEmailAuthControl_Type()
)
pduEmailAuthControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailAuthControl.setStatus("mandatory")


class _PduEmailAuthUsername_Type(DisplayString):
    """Custom type pduEmailAuthUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduEmailAuthUsername_Type.__name__ = "DisplayString"
_PduEmailAuthUsername_Object = MibScalar
pduEmailAuthUsername = _PduEmailAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 6),
    _PduEmailAuthUsername_Type()
)
pduEmailAuthUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailAuthUsername.setStatus("mandatory")


class _PduEmailAuthPassword_Type(DisplayString):
    """Custom type pduEmailAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduEmailAuthPassword_Type.__name__ = "DisplayString"
_PduEmailAuthPassword_Object = MibScalar
pduEmailAuthPassword = _PduEmailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 7),
    _PduEmailAuthPassword_Type()
)
pduEmailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailAuthPassword.setStatus("mandatory")
_PduEmailReceiversTable_Object = MibTable
pduEmailReceiversTable = _PduEmailReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 8)
)
if mibBuilder.loadTexts:
    pduEmailReceiversTable.setStatus("mandatory")
_PduEmailReceiversEntry_Object = MibTableRow
pduEmailReceiversEntry = _PduEmailReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 8, 1)
)
pduEmailReceiversEntry.setIndexNames(
    (0, "SPSv1-MIB", "mailRecvIndex"),
)
if mibBuilder.loadTexts:
    pduEmailReceiversEntry.setStatus("mandatory")


class _MailRecvIndex_Type(Integer32):
    """Custom type mailRecvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MailRecvIndex_Type.__name__ = "Integer32"
_MailRecvIndex_Object = MibTableColumn
mailRecvIndex = _MailRecvIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 8, 1, 1),
    _MailRecvIndex_Type()
)
mailRecvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mailRecvIndex.setStatus("mandatory")


class _MailRecvReceiverAddr_Type(DisplayString):
    """Custom type mailRecvReceiverAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MailRecvReceiverAddr_Type.__name__ = "DisplayString"
_MailRecvReceiverAddr_Object = MibTableColumn
mailRecvReceiverAddr = _MailRecvReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 8, 1, 2),
    _MailRecvReceiverAddr_Type()
)
mailRecvReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailRecvReceiverAddr.setStatus("mandatory")


class _MailRecvEmailType_Type(Integer32):
    """Custom type mailRecvEmailType based on Integer32"""
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
        *(("none", 1),
          ("events", 2),
          ("status", 3),
          ("both", 4))
    )


_MailRecvEmailType_Type.__name__ = "Integer32"
_MailRecvEmailType_Object = MibTableColumn
mailRecvEmailType = _MailRecvEmailType_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 8, 1, 3),
    _MailRecvEmailType_Type()
)
mailRecvEmailType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailRecvEmailType.setStatus("mandatory")


class _MailRecvEventLevel_Type(Integer32):
    """Custom type mailRecvEventLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("informational", 3))
    )


_MailRecvEventLevel_Type.__name__ = "Integer32"
_MailRecvEventLevel_Object = MibTableColumn
mailRecvEventLevel = _MailRecvEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 8, 1, 4),
    _MailRecvEventLevel_Type()
)
mailRecvEventLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailRecvEventLevel.setStatus("mandatory")


class _MailRecvDescription_Type(DisplayString):
    """Custom type mailRecvDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MailRecvDescription_Type.__name__ = "DisplayString"
_MailRecvDescription_Object = MibTableColumn
mailRecvDescription = _MailRecvDescription_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 5, 8, 1, 5),
    _MailRecvDescription_Type()
)
mailRecvDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailRecvDescription.setStatus("mandatory")
_PduPwrMonitoring_ObjectIdentity = ObjectIdentity
pduPwrMonitoring = _PduPwrMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6)
)
_PduPwrMonitoringInlet_ObjectIdentity = ObjectIdentity
pduPwrMonitoringInlet = _PduPwrMonitoringInlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1)
)
_PduPwrMonitoringInletNum_Type = Integer32
_PduPwrMonitoringInletNum_Object = MibScalar
pduPwrMonitoringInletNum = _PduPwrMonitoringInletNum_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 1),
    _PduPwrMonitoringInletNum_Type()
)
pduPwrMonitoringInletNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrMonitoringInletNum.setStatus("mandatory")
_PduPwrMonitoringInletStatusTable_Object = MibTable
pduPwrMonitoringInletStatusTable = _PduPwrMonitoringInletStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringInletStatusTable.setStatus("mandatory")
_PduPwrMonitoringInletStatusEntry_Object = MibTableRow
pduPwrMonitoringInletStatusEntry = _PduPwrMonitoringInletStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1)
)
pduPwrMonitoringInletStatusEntry.setIndexNames(
    (0, "SPSv1-MIB", "inletIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringInletStatusEntry.setStatus("mandatory")


class _InletIndex_Type(Integer32):
    """Custom type inletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_InletIndex_Type.__name__ = "Integer32"
_InletIndex_Object = MibTableColumn
inletIndex = _InletIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 1),
    _InletIndex_Type()
)
inletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletIndex.setStatus("mandatory")
_InletPowerAll_Type = Integer32
_InletPowerAll_Object = MibTableColumn
inletPowerAll = _InletPowerAll_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 2),
    _InletPowerAll_Type()
)
inletPowerAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerAll.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPowerAll.setUnits("0.1W")
_InletResetFrom_Type = DisplayString
_InletResetFrom_Object = MibTableColumn
inletResetFrom = _InletResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 3),
    _InletResetFrom_Type()
)
inletResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletResetFrom.setStatus("mandatory")
_InletEnergy_Type = Integer32
_InletEnergy_Object = MibTableColumn
inletEnergy = _InletEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 4),
    _InletEnergy_Type()
)
inletEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletEnergy.setUnits("KWh")


class _InletStatus_Type(Integer32):
    """Custom type inletStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_InletStatus_Type.__name__ = "Integer32"
_InletStatus_Object = MibTableColumn
inletStatus = _InletStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 5),
    _InletStatus_Type()
)
inletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletStatus.setStatus("mandatory")
_InletCurrPhase1_Type = Integer32
_InletCurrPhase1_Object = MibTableColumn
inletCurrPhase1 = _InletCurrPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 6),
    _InletCurrPhase1_Type()
)
inletCurrPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCurrPhase1.setUnits("0.01A")
_InletCurrPhase2_Type = Integer32
_InletCurrPhase2_Object = MibTableColumn
inletCurrPhase2 = _InletCurrPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 7),
    _InletCurrPhase2_Type()
)
inletCurrPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCurrPhase2.setUnits("0.01A")
_InletCurrPhase3_Type = Integer32
_InletCurrPhase3_Object = MibTableColumn
inletCurrPhase3 = _InletCurrPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 8),
    _InletCurrPhase3_Type()
)
inletCurrPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCurrPhase3.setUnits("0.01A")
_InletVoltPhase1_Type = Integer32
_InletVoltPhase1_Object = MibTableColumn
inletVoltPhase1 = _InletVoltPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 9),
    _InletVoltPhase1_Type()
)
inletVoltPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVoltPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVoltPhase1.setUnits("0.1V")
_InletVoltPhase2_Type = Integer32
_InletVoltPhase2_Object = MibTableColumn
inletVoltPhase2 = _InletVoltPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 10),
    _InletVoltPhase2_Type()
)
inletVoltPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVoltPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVoltPhase2.setUnits("0.1V")
_InletVoltPhase3_Type = Integer32
_InletVoltPhase3_Object = MibTableColumn
inletVoltPhase3 = _InletVoltPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 11),
    _InletVoltPhase3_Type()
)
inletVoltPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVoltPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletVoltPhase3.setUnits("0.1V")
_InletPwrFactorPhase1_Type = Integer32
_InletPwrFactorPhase1_Object = MibTableColumn
inletPwrFactorPhase1 = _InletPwrFactorPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 12),
    _InletPwrFactorPhase1_Type()
)
inletPwrFactorPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPwrFactorPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPwrFactorPhase1.setUnits("0.1%")
_InletPwrFactorPhase2_Type = Integer32
_InletPwrFactorPhase2_Object = MibTableColumn
inletPwrFactorPhase2 = _InletPwrFactorPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 13),
    _InletPwrFactorPhase2_Type()
)
inletPwrFactorPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPwrFactorPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPwrFactorPhase2.setUnits("0.1%")
_InletPwrFactorPhase3_Type = Integer32
_InletPwrFactorPhase3_Object = MibTableColumn
inletPwrFactorPhase3 = _InletPwrFactorPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 14),
    _InletPwrFactorPhase3_Type()
)
inletPwrFactorPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPwrFactorPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPwrFactorPhase3.setUnits("0.1%")
_InletPowerPhase1_Type = Integer32
_InletPowerPhase1_Object = MibTableColumn
inletPowerPhase1 = _InletPowerPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 15),
    _InletPowerPhase1_Type()
)
inletPowerPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPowerPhase1.setUnits("0.1W")
_InletPowerPhase2_Type = Integer32
_InletPowerPhase2_Object = MibTableColumn
inletPowerPhase2 = _InletPowerPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 16),
    _InletPowerPhase2_Type()
)
inletPowerPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPowerPhase2.setUnits("0.1W")
_InletPowerPhase3_Type = Integer32
_InletPowerPhase3_Object = MibTableColumn
inletPowerPhase3 = _InletPowerPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 17),
    _InletPowerPhase3_Type()
)
inletPowerPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletPowerPhase3.setUnits("0.1W")


class _InletStatusPhase1_Type(Integer32):
    """Custom type inletStatusPhase1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_InletStatusPhase1_Type.__name__ = "Integer32"
_InletStatusPhase1_Object = MibTableColumn
inletStatusPhase1 = _InletStatusPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 18),
    _InletStatusPhase1_Type()
)
inletStatusPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletStatusPhase1.setStatus("mandatory")


class _InletStatusPhase2_Type(Integer32):
    """Custom type inletStatusPhase2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_InletStatusPhase2_Type.__name__ = "Integer32"
_InletStatusPhase2_Object = MibTableColumn
inletStatusPhase2 = _InletStatusPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 19),
    _InletStatusPhase2_Type()
)
inletStatusPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletStatusPhase2.setStatus("mandatory")


class _InletStatusPhase3_Type(Integer32):
    """Custom type inletStatusPhase3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_InletStatusPhase3_Type.__name__ = "Integer32"
_InletStatusPhase3_Object = MibTableColumn
inletStatusPhase3 = _InletStatusPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 2, 1, 20),
    _InletStatusPhase3_Type()
)
inletStatusPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletStatusPhase3.setStatus("mandatory")
_PduPwrMonitoringInletCfgTable_Object = MibTable
pduPwrMonitoringInletCfgTable = _PduPwrMonitoringInletCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringInletCfgTable.setStatus("mandatory")
_PduPwrMonitoringInletCfgEntry_Object = MibTableRow
pduPwrMonitoringInletCfgEntry = _PduPwrMonitoringInletCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1)
)
pduPwrMonitoringInletCfgEntry.setIndexNames(
    (0, "SPSv1-MIB", "inletCfgIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringInletCfgEntry.setStatus("mandatory")


class _InletCfgIndex_Type(Integer32):
    """Custom type inletCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_InletCfgIndex_Type.__name__ = "Integer32"
_InletCfgIndex_Object = MibTableColumn
inletCfgIndex = _InletCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 1),
    _InletCfgIndex_Type()
)
inletCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCfgIndex.setStatus("mandatory")
_InletCfgLoadCritical_Type = Integer32
_InletCfgLoadCritical_Object = MibTableColumn
inletCfgLoadCritical = _InletCfgLoadCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 2),
    _InletCfgLoadCritical_Type()
)
inletCfgLoadCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgLoadCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgLoadCritical.setUnits("0.1kW")
_InletCfgLoadWarning_Type = Integer32
_InletCfgLoadWarning_Object = MibTableColumn
inletCfgLoadWarning = _InletCfgLoadWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 3),
    _InletCfgLoadWarning_Type()
)
inletCfgLoadWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgLoadWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgLoadWarning.setUnits("0.1kW")
_InletCfgCurrCritPhase1_Type = Integer32
_InletCfgCurrCritPhase1_Object = MibTableColumn
inletCfgCurrCritPhase1 = _InletCfgCurrCritPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 4),
    _InletCfgCurrCritPhase1_Type()
)
inletCfgCurrCritPhase1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase1.setUnits("0.1A")
_InletCfgCurrCritPhase2_Type = Integer32
_InletCfgCurrCritPhase2_Object = MibTableColumn
inletCfgCurrCritPhase2 = _InletCfgCurrCritPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 5),
    _InletCfgCurrCritPhase2_Type()
)
inletCfgCurrCritPhase2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase2.setUnits("0.1A")
_InletCfgCurrCritPhase3_Type = Integer32
_InletCfgCurrCritPhase3_Object = MibTableColumn
inletCfgCurrCritPhase3 = _InletCfgCurrCritPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 6),
    _InletCfgCurrCritPhase3_Type()
)
inletCfgCurrCritPhase3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrCritPhase3.setUnits("0.1A")
_InletCfgCurrWarnPhase1_Type = Integer32
_InletCfgCurrWarnPhase1_Object = MibTableColumn
inletCfgCurrWarnPhase1 = _InletCfgCurrWarnPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 7),
    _InletCfgCurrWarnPhase1_Type()
)
inletCfgCurrWarnPhase1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase1.setUnits("0.1A")
_InletCfgCurrWarnPhase2_Type = Integer32
_InletCfgCurrWarnPhase2_Object = MibTableColumn
inletCfgCurrWarnPhase2 = _InletCfgCurrWarnPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 8),
    _InletCfgCurrWarnPhase2_Type()
)
inletCfgCurrWarnPhase2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase2.setUnits("0.1A")
_InletCfgCurrWarnPhase3_Type = Integer32
_InletCfgCurrWarnPhase3_Object = MibTableColumn
inletCfgCurrWarnPhase3 = _InletCfgCurrWarnPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 9),
    _InletCfgCurrWarnPhase3_Type()
)
inletCfgCurrWarnPhase3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgCurrWarnPhase3.setUnits("0.1A")
_InletCfgVoltCritPhase1_Type = Integer32
_InletCfgVoltCritPhase1_Object = MibTableColumn
inletCfgVoltCritPhase1 = _InletCfgVoltCritPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 10),
    _InletCfgVoltCritPhase1_Type()
)
inletCfgVoltCritPhase1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgVoltCritPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgVoltCritPhase1.setUnits("0.1V")
_InletCfgVoltCritPhase2_Type = Integer32
_InletCfgVoltCritPhase2_Object = MibTableColumn
inletCfgVoltCritPhase2 = _InletCfgVoltCritPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 11),
    _InletCfgVoltCritPhase2_Type()
)
inletCfgVoltCritPhase2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgVoltCritPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgVoltCritPhase2.setUnits("0.1V")
_InletCfgVoltCritPhase3_Type = Integer32
_InletCfgVoltCritPhase3_Object = MibTableColumn
inletCfgVoltCritPhase3 = _InletCfgVoltCritPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 12),
    _InletCfgVoltCritPhase3_Type()
)
inletCfgVoltCritPhase3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgVoltCritPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgVoltCritPhase3.setUnits("0.1V")
_InletCfgVoltWarnPhase1_Type = Integer32
_InletCfgVoltWarnPhase1_Object = MibTableColumn
inletCfgVoltWarnPhase1 = _InletCfgVoltWarnPhase1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 13),
    _InletCfgVoltWarnPhase1_Type()
)
inletCfgVoltWarnPhase1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgVoltWarnPhase1.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgVoltWarnPhase1.setUnits("0.1V")
_InletCfgVoltWarnPhase2_Type = Integer32
_InletCfgVoltWarnPhase2_Object = MibTableColumn
inletCfgVoltWarnPhase2 = _InletCfgVoltWarnPhase2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 14),
    _InletCfgVoltWarnPhase2_Type()
)
inletCfgVoltWarnPhase2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgVoltWarnPhase2.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgVoltWarnPhase2.setUnits("0.1V")
_InletCfgVoltWarnPhase3_Type = Integer32
_InletCfgVoltWarnPhase3_Object = MibTableColumn
inletCfgVoltWarnPhase3 = _InletCfgVoltWarnPhase3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 1, 3, 1, 15),
    _InletCfgVoltWarnPhase3_Type()
)
inletCfgVoltWarnPhase3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCfgVoltWarnPhase3.setStatus("mandatory")
if mibBuilder.loadTexts:
    inletCfgVoltWarnPhase3.setUnits("0.1V")
_PduPwrMonitoringOutlet_ObjectIdentity = ObjectIdentity
pduPwrMonitoringOutlet = _PduPwrMonitoringOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2)
)
_PduPwrMonitoringOutletPduA_ObjectIdentity = ObjectIdentity
pduPwrMonitoringOutletPduA = _PduPwrMonitoringOutletPduA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1)
)
_PduPwrMonitoringOutletNumPduA_Type = Integer32
_PduPwrMonitoringOutletNumPduA_Object = MibScalar
pduPwrMonitoringOutletNumPduA = _PduPwrMonitoringOutletNumPduA_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 1),
    _PduPwrMonitoringOutletNumPduA_Type()
)
pduPwrMonitoringOutletNumPduA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletNumPduA.setStatus("mandatory")
_PduPwrMonitoringOutletStatusTablePduA_Object = MibTable
pduPwrMonitoringOutletStatusTablePduA = _PduPwrMonitoringOutletStatusTablePduA_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusTablePduA.setStatus("mandatory")
_PduPwrMonitoringOutletStatusPduAEntry_Object = MibTableRow
pduPwrMonitoringOutletStatusPduAEntry = _PduPwrMonitoringOutletStatusPduAEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1)
)
pduPwrMonitoringOutletStatusPduAEntry.setIndexNames(
    (0, "SPSv1-MIB", "outletPduAIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusPduAEntry.setStatus("mandatory")


class _OutletPduAIndex_Type(Integer32):
    """Custom type outletPduAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletPduAIndex_Type.__name__ = "Integer32"
_OutletPduAIndex_Object = MibTableColumn
outletPduAIndex = _OutletPduAIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 1),
    _OutletPduAIndex_Type()
)
outletPduAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAIndex.setStatus("mandatory")


class _OutletPduAState_Type(Integer32):
    """Custom type outletPduAState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_OutletPduAState_Type.__name__ = "Integer32"
_OutletPduAState_Object = MibTableColumn
outletPduAState = _OutletPduAState_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 2),
    _OutletPduAState_Type()
)
outletPduAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAState.setStatus("mandatory")
_OutletPduACurrent_Type = Integer32
_OutletPduACurrent_Object = MibTableColumn
outletPduACurrent = _OutletPduACurrent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 3),
    _OutletPduACurrent_Type()
)
outletPduACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduACurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduACurrent.setUnits("0.01A")
_OutletPduAPwrFactor_Type = Integer32
_OutletPduAPwrFactor_Object = MibTableColumn
outletPduAPwrFactor = _OutletPduAPwrFactor_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 4),
    _OutletPduAPwrFactor_Type()
)
outletPduAPwrFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAPwrFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduAPwrFactor.setUnits("0.1%")
_OutletPduAPower_Type = Integer32
_OutletPduAPower_Object = MibTableColumn
outletPduAPower = _OutletPduAPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 5),
    _OutletPduAPower_Type()
)
outletPduAPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduAPower.setUnits("0.1W")
_OutletPduAEnergy_Type = Integer32
_OutletPduAEnergy_Object = MibTableColumn
outletPduAEnergy = _OutletPduAEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 6),
    _OutletPduAEnergy_Type()
)
outletPduAEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduAEnergy.setUnits("KWh")
_OutletPduAResetFrom_Type = DisplayString
_OutletPduAResetFrom_Object = MibTableColumn
outletPduAResetFrom = _OutletPduAResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 7),
    _OutletPduAResetFrom_Type()
)
outletPduAResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAResetFrom.setStatus("mandatory")


class _OutletPduAStatus_Type(Integer32):
    """Custom type outletPduAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_OutletPduAStatus_Type.__name__ = "Integer32"
_OutletPduAStatus_Object = MibTableColumn
outletPduAStatus = _OutletPduAStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 2, 1, 8),
    _OutletPduAStatus_Type()
)
outletPduAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduAStatus.setStatus("mandatory")
_PduPwrMonitoringOutletCfgTablePduA_Object = MibTable
pduPwrMonitoringOutletCfgTablePduA = _PduPwrMonitoringOutletCfgTablePduA_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgTablePduA.setStatus("mandatory")
_PduPwrMonitoringOutletCfgPduAEntry_Object = MibTableRow
pduPwrMonitoringOutletCfgPduAEntry = _PduPwrMonitoringOutletCfgPduAEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1)
)
pduPwrMonitoringOutletCfgPduAEntry.setIndexNames(
    (0, "SPSv1-MIB", "outletCfgPduAIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgPduAEntry.setStatus("mandatory")


class _OutletCfgPduAIndex_Type(Integer32):
    """Custom type outletCfgPduAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCfgPduAIndex_Type.__name__ = "Integer32"
_OutletCfgPduAIndex_Object = MibTableColumn
outletCfgPduAIndex = _OutletCfgPduAIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 1),
    _OutletCfgPduAIndex_Type()
)
outletCfgPduAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCfgPduAIndex.setStatus("mandatory")
_OutletCfgPduAName_Type = DisplayString
_OutletCfgPduAName_Object = MibTableColumn
outletCfgPduAName = _OutletCfgPduAName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 2),
    _OutletCfgPduAName_Type()
)
outletCfgPduAName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduAName.setStatus("mandatory")


class _OutletCfgPduADelayOnStatus_Type(Integer32):
    """Custom type outletCfgPduADelayOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduADelayOnStatus_Type.__name__ = "Integer32"
_OutletCfgPduADelayOnStatus_Object = MibTableColumn
outletCfgPduADelayOnStatus = _OutletCfgPduADelayOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 3),
    _OutletCfgPduADelayOnStatus_Type()
)
outletCfgPduADelayOnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduADelayOnStatus.setStatus("mandatory")
_OutletCfgPduADelayOnTime_Type = Integer32
_OutletCfgPduADelayOnTime_Object = MibTableColumn
outletCfgPduADelayOnTime = _OutletCfgPduADelayOnTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 4),
    _OutletCfgPduADelayOnTime_Type()
)
outletCfgPduADelayOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduADelayOnTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduADelayOnTime.setUnits("seconds")


class _OutletCfgPduADelayOffStatus_Type(Integer32):
    """Custom type outletCfgPduADelayOffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduADelayOffStatus_Type.__name__ = "Integer32"
_OutletCfgPduADelayOffStatus_Object = MibTableColumn
outletCfgPduADelayOffStatus = _OutletCfgPduADelayOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 5),
    _OutletCfgPduADelayOffStatus_Type()
)
outletCfgPduADelayOffStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduADelayOffStatus.setStatus("mandatory")
_OutletCfgPduADelayOffTime_Type = Integer32
_OutletCfgPduADelayOffTime_Object = MibTableColumn
outletCfgPduADelayOffTime = _OutletCfgPduADelayOffTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 6),
    _OutletCfgPduADelayOffTime_Type()
)
outletCfgPduADelayOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduADelayOffTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduADelayOffTime.setUnits("seconds")
_OutletCfgPduAReboot_Type = Integer32
_OutletCfgPduAReboot_Object = MibTableColumn
outletCfgPduAReboot = _OutletCfgPduAReboot_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 7),
    _OutletCfgPduAReboot_Type()
)
outletCfgPduAReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduAReboot.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduAReboot.setUnits("seconds")
_OutletCfgPduAOverCurrCritical_Type = Integer32
_OutletCfgPduAOverCurrCritical_Object = MibTableColumn
outletCfgPduAOverCurrCritical = _OutletCfgPduAOverCurrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 8),
    _OutletCfgPduAOverCurrCritical_Type()
)
outletCfgPduAOverCurrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduAOverCurrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduAOverCurrCritical.setUnits("0.1A")
_OutletCfgPduAOverCurrWarning_Type = Integer32
_OutletCfgPduAOverCurrWarning_Object = MibTableColumn
outletCfgPduAOverCurrWarning = _OutletCfgPduAOverCurrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 9),
    _OutletCfgPduAOverCurrWarning_Type()
)
outletCfgPduAOverCurrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduAOverCurrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduAOverCurrWarning.setUnits("0.1A")
_OutletCfgPduAOverPwrCritical_Type = Integer32
_OutletCfgPduAOverPwrCritical_Object = MibTableColumn
outletCfgPduAOverPwrCritical = _OutletCfgPduAOverPwrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 10),
    _OutletCfgPduAOverPwrCritical_Type()
)
outletCfgPduAOverPwrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduAOverPwrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduAOverPwrCritical.setUnits("1W")
_OutletCfgPduAOverPwrWarning_Type = Integer32
_OutletCfgPduAOverPwrWarning_Object = MibTableColumn
outletCfgPduAOverPwrWarning = _OutletCfgPduAOverPwrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 3, 1, 11),
    _OutletCfgPduAOverPwrWarning_Type()
)
outletCfgPduAOverPwrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduAOverPwrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduAOverPwrWarning.setUnits("1W")
_PduPwrMonitoringOutletCtlTablePduA_Object = MibTable
pduPwrMonitoringOutletCtlTablePduA = _PduPwrMonitoringOutletCtlTablePduA_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 4)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlTablePduA.setStatus("mandatory")
_PduPwrMonitoringOutletCtlPduAEntry_Object = MibTableRow
pduPwrMonitoringOutletCtlPduAEntry = _PduPwrMonitoringOutletCtlPduAEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 4, 1)
)
pduPwrMonitoringOutletCtlPduAEntry.setIndexNames(
    (0, "SPSv1-MIB", "outletCtlPduAIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlPduAEntry.setStatus("mandatory")


class _OutletCtlPduAIndex_Type(Integer32):
    """Custom type outletCtlPduAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCtlPduAIndex_Type.__name__ = "Integer32"
_OutletCtlPduAIndex_Object = MibTableColumn
outletCtlPduAIndex = _OutletCtlPduAIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 4, 1, 1),
    _OutletCtlPduAIndex_Type()
)
outletCtlPduAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCtlPduAIndex.setStatus("mandatory")


class _OutletCtlPduAControl_Type(Integer32):
    """Custom type outletCtlPduAControl based on Integer32"""
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
        *(("immediateOn", 1),
          ("delayedOn", 2),
          ("immediateOff", 3),
          ("delayedOff", 4),
          ("immediateCycle", 5),
          ("delayedCycle", 6))
    )


_OutletCtlPduAControl_Type.__name__ = "Integer32"
_OutletCtlPduAControl_Object = MibTableColumn
outletCtlPduAControl = _OutletCtlPduAControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 1, 4, 1, 2),
    _OutletCtlPduAControl_Type()
)
outletCtlPduAControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCtlPduAControl.setStatus("mandatory")
_PduPwrMonitoringOutletPduB_ObjectIdentity = ObjectIdentity
pduPwrMonitoringOutletPduB = _PduPwrMonitoringOutletPduB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2)
)
_PduPwrMonitoringOutletNumPduB_Type = Integer32
_PduPwrMonitoringOutletNumPduB_Object = MibScalar
pduPwrMonitoringOutletNumPduB = _PduPwrMonitoringOutletNumPduB_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 1),
    _PduPwrMonitoringOutletNumPduB_Type()
)
pduPwrMonitoringOutletNumPduB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletNumPduB.setStatus("mandatory")
_PduPwrMonitoringOutletStatusTablePduB_Object = MibTable
pduPwrMonitoringOutletStatusTablePduB = _PduPwrMonitoringOutletStatusTablePduB_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusTablePduB.setStatus("mandatory")
_PduPwrMonitoringOutletStatusPduBEntry_Object = MibTableRow
pduPwrMonitoringOutletStatusPduBEntry = _PduPwrMonitoringOutletStatusPduBEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1)
)
pduPwrMonitoringOutletStatusPduBEntry.setIndexNames(
    (0, "SPSv1-MIB", "outletPduBIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusPduBEntry.setStatus("mandatory")


class _OutletPduBIndex_Type(Integer32):
    """Custom type outletPduBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletPduBIndex_Type.__name__ = "Integer32"
_OutletPduBIndex_Object = MibTableColumn
outletPduBIndex = _OutletPduBIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 1),
    _OutletPduBIndex_Type()
)
outletPduBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBIndex.setStatus("mandatory")


class _OutletPduBState_Type(Integer32):
    """Custom type outletPduBState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_OutletPduBState_Type.__name__ = "Integer32"
_OutletPduBState_Object = MibTableColumn
outletPduBState = _OutletPduBState_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 2),
    _OutletPduBState_Type()
)
outletPduBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBState.setStatus("mandatory")
_OutletPduBCurrent_Type = Integer32
_OutletPduBCurrent_Object = MibTableColumn
outletPduBCurrent = _OutletPduBCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 3),
    _OutletPduBCurrent_Type()
)
outletPduBCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduBCurrent.setUnits("0.01A")
_OutletPduBPwrFactor_Type = Integer32
_OutletPduBPwrFactor_Object = MibTableColumn
outletPduBPwrFactor = _OutletPduBPwrFactor_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 4),
    _OutletPduBPwrFactor_Type()
)
outletPduBPwrFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBPwrFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduBPwrFactor.setUnits("0.1%")
_OutletPduBPower_Type = Integer32
_OutletPduBPower_Object = MibTableColumn
outletPduBPower = _OutletPduBPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 5),
    _OutletPduBPower_Type()
)
outletPduBPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduBPower.setUnits("0.1W")
_OutletPduBEnergy_Type = Integer32
_OutletPduBEnergy_Object = MibTableColumn
outletPduBEnergy = _OutletPduBEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 6),
    _OutletPduBEnergy_Type()
)
outletPduBEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduBEnergy.setUnits("KWh")
_OutletPduBResetFrom_Type = DisplayString
_OutletPduBResetFrom_Object = MibTableColumn
outletPduBResetFrom = _OutletPduBResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 7),
    _OutletPduBResetFrom_Type()
)
outletPduBResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBResetFrom.setStatus("mandatory")


class _OutletPduBStatus_Type(Integer32):
    """Custom type outletPduBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_OutletPduBStatus_Type.__name__ = "Integer32"
_OutletPduBStatus_Object = MibTableColumn
outletPduBStatus = _OutletPduBStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 2, 1, 8),
    _OutletPduBStatus_Type()
)
outletPduBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduBStatus.setStatus("mandatory")
_PduPwrMonitoringOutletCfgTablePduB_Object = MibTable
pduPwrMonitoringOutletCfgTablePduB = _PduPwrMonitoringOutletCfgTablePduB_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgTablePduB.setStatus("mandatory")
_PduPwrMonitoringOutletCfgPduBEntry_Object = MibTableRow
pduPwrMonitoringOutletCfgPduBEntry = _PduPwrMonitoringOutletCfgPduBEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1)
)
pduPwrMonitoringOutletCfgPduBEntry.setIndexNames(
    (0, "SPSv1-MIB", "outletCfgPduBIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgPduBEntry.setStatus("mandatory")


class _OutletCfgPduBIndex_Type(Integer32):
    """Custom type outletCfgPduBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCfgPduBIndex_Type.__name__ = "Integer32"
_OutletCfgPduBIndex_Object = MibTableColumn
outletCfgPduBIndex = _OutletCfgPduBIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 1),
    _OutletCfgPduBIndex_Type()
)
outletCfgPduBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCfgPduBIndex.setStatus("mandatory")
_OutletCfgPduBName_Type = DisplayString
_OutletCfgPduBName_Object = MibTableColumn
outletCfgPduBName = _OutletCfgPduBName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 2),
    _OutletCfgPduBName_Type()
)
outletCfgPduBName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBName.setStatus("mandatory")


class _OutletCfgPduBDelayOnStatus_Type(Integer32):
    """Custom type outletCfgPduBDelayOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduBDelayOnStatus_Type.__name__ = "Integer32"
_OutletCfgPduBDelayOnStatus_Object = MibTableColumn
outletCfgPduBDelayOnStatus = _OutletCfgPduBDelayOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 3),
    _OutletCfgPduBDelayOnStatus_Type()
)
outletCfgPduBDelayOnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBDelayOnStatus.setStatus("mandatory")
_OutletCfgPduBDelayOnTime_Type = Integer32
_OutletCfgPduBDelayOnTime_Object = MibTableColumn
outletCfgPduBDelayOnTime = _OutletCfgPduBDelayOnTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 4),
    _OutletCfgPduBDelayOnTime_Type()
)
outletCfgPduBDelayOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBDelayOnTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduBDelayOnTime.setUnits("seconds")


class _OutletCfgPduBDelayOffStatus_Type(Integer32):
    """Custom type outletCfgPduBDelayOffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduBDelayOffStatus_Type.__name__ = "Integer32"
_OutletCfgPduBDelayOffStatus_Object = MibTableColumn
outletCfgPduBDelayOffStatus = _OutletCfgPduBDelayOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 5),
    _OutletCfgPduBDelayOffStatus_Type()
)
outletCfgPduBDelayOffStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBDelayOffStatus.setStatus("mandatory")
_OutletCfgPduBDelayOffTime_Type = Integer32
_OutletCfgPduBDelayOffTime_Object = MibTableColumn
outletCfgPduBDelayOffTime = _OutletCfgPduBDelayOffTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 6),
    _OutletCfgPduBDelayOffTime_Type()
)
outletCfgPduBDelayOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBDelayOffTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduBDelayOffTime.setUnits("seconds")
_OutletCfgPduBReboot_Type = Integer32
_OutletCfgPduBReboot_Object = MibTableColumn
outletCfgPduBReboot = _OutletCfgPduBReboot_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 7),
    _OutletCfgPduBReboot_Type()
)
outletCfgPduBReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBReboot.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduBReboot.setUnits("seconds")
_OutletCfgPduBOverCurrCritical_Type = Integer32
_OutletCfgPduBOverCurrCritical_Object = MibTableColumn
outletCfgPduBOverCurrCritical = _OutletCfgPduBOverCurrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 8),
    _OutletCfgPduBOverCurrCritical_Type()
)
outletCfgPduBOverCurrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBOverCurrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduBOverCurrCritical.setUnits("0.1A")
_OutletCfgPduBOverCurrWarning_Type = Integer32
_OutletCfgPduBOverCurrWarning_Object = MibTableColumn
outletCfgPduBOverCurrWarning = _OutletCfgPduBOverCurrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 9),
    _OutletCfgPduBOverCurrWarning_Type()
)
outletCfgPduBOverCurrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBOverCurrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduBOverCurrWarning.setUnits("0.1A")
_OutletCfgPduBOverPwrCritical_Type = Integer32
_OutletCfgPduBOverPwrCritical_Object = MibTableColumn
outletCfgPduBOverPwrCritical = _OutletCfgPduBOverPwrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 10),
    _OutletCfgPduBOverPwrCritical_Type()
)
outletCfgPduBOverPwrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBOverPwrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduBOverPwrCritical.setUnits("1W")
_OutletCfgPduBOverPwrWarning_Type = Integer32
_OutletCfgPduBOverPwrWarning_Object = MibTableColumn
outletCfgPduBOverPwrWarning = _OutletCfgPduBOverPwrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 3, 1, 11),
    _OutletCfgPduBOverPwrWarning_Type()
)
outletCfgPduBOverPwrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduBOverPwrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduBOverPwrWarning.setUnits("1W")
_PduPwrMonitoringOutletCtlTablePduB_Object = MibTable
pduPwrMonitoringOutletCtlTablePduB = _PduPwrMonitoringOutletCtlTablePduB_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 4)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlTablePduB.setStatus("mandatory")
_PduPwrMonitoringOutletCtlPduBEntry_Object = MibTableRow
pduPwrMonitoringOutletCtlPduBEntry = _PduPwrMonitoringOutletCtlPduBEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 4, 1)
)
pduPwrMonitoringOutletCtlPduBEntry.setIndexNames(
    (0, "SPSv1-MIB", "outletCtlPduBIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlPduBEntry.setStatus("mandatory")


class _OutletCtlPduBIndex_Type(Integer32):
    """Custom type outletCtlPduBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCtlPduBIndex_Type.__name__ = "Integer32"
_OutletCtlPduBIndex_Object = MibTableColumn
outletCtlPduBIndex = _OutletCtlPduBIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 4, 1, 1),
    _OutletCtlPduBIndex_Type()
)
outletCtlPduBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCtlPduBIndex.setStatus("mandatory")


class _OutletCtlPduBControl_Type(Integer32):
    """Custom type outletCtlPduBControl based on Integer32"""
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
        *(("immediateOn", 1),
          ("delayedOn", 2),
          ("immediateOff", 3),
          ("delayedOff", 4),
          ("immediateCycle", 5),
          ("delayedCycle", 6))
    )


_OutletCtlPduBControl_Type.__name__ = "Integer32"
_OutletCtlPduBControl_Object = MibTableColumn
outletCtlPduBControl = _OutletCtlPduBControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 2, 4, 1, 2),
    _OutletCtlPduBControl_Type()
)
outletCtlPduBControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCtlPduBControl.setStatus("mandatory")
_PduPwrMonitoringOutletPduC_ObjectIdentity = ObjectIdentity
pduPwrMonitoringOutletPduC = _PduPwrMonitoringOutletPduC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3)
)
_PduPwrMonitoringOutletNumPduC_Type = Integer32
_PduPwrMonitoringOutletNumPduC_Object = MibScalar
pduPwrMonitoringOutletNumPduC = _PduPwrMonitoringOutletNumPduC_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 1),
    _PduPwrMonitoringOutletNumPduC_Type()
)
pduPwrMonitoringOutletNumPduC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletNumPduC.setStatus("mandatory")
_PduPwrMonitoringOutletStatusTablePduC_Object = MibTable
pduPwrMonitoringOutletStatusTablePduC = _PduPwrMonitoringOutletStatusTablePduC_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusTablePduC.setStatus("mandatory")
_PduPwrMonitoringOutletStatusPduCEntry_Object = MibTableRow
pduPwrMonitoringOutletStatusPduCEntry = _PduPwrMonitoringOutletStatusPduCEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1)
)
pduPwrMonitoringOutletStatusPduCEntry.setIndexNames(
    (0, "SPSv1-MIB", "outletPduCIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusPduCEntry.setStatus("mandatory")


class _OutletPduCIndex_Type(Integer32):
    """Custom type outletPduCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletPduCIndex_Type.__name__ = "Integer32"
_OutletPduCIndex_Object = MibTableColumn
outletPduCIndex = _OutletPduCIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 1),
    _OutletPduCIndex_Type()
)
outletPduCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCIndex.setStatus("mandatory")


class _OutletPduCState_Type(Integer32):
    """Custom type outletPduCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_OutletPduCState_Type.__name__ = "Integer32"
_OutletPduCState_Object = MibTableColumn
outletPduCState = _OutletPduCState_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 2),
    _OutletPduCState_Type()
)
outletPduCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCState.setStatus("mandatory")
_OutletPduCCurrent_Type = Integer32
_OutletPduCCurrent_Object = MibTableColumn
outletPduCCurrent = _OutletPduCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 3),
    _OutletPduCCurrent_Type()
)
outletPduCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduCCurrent.setUnits("0.01A")
_OutletPduCPwrFactor_Type = Integer32
_OutletPduCPwrFactor_Object = MibTableColumn
outletPduCPwrFactor = _OutletPduCPwrFactor_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 4),
    _OutletPduCPwrFactor_Type()
)
outletPduCPwrFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCPwrFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduCPwrFactor.setUnits("0.1%")
_OutletPduCPower_Type = Integer32
_OutletPduCPower_Object = MibTableColumn
outletPduCPower = _OutletPduCPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 5),
    _OutletPduCPower_Type()
)
outletPduCPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduCPower.setUnits("0.1W")
_OutletPduCEnergy_Type = Integer32
_OutletPduCEnergy_Object = MibTableColumn
outletPduCEnergy = _OutletPduCEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 6),
    _OutletPduCEnergy_Type()
)
outletPduCEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduCEnergy.setUnits("KWh")
_OutletPduCResetFrom_Type = DisplayString
_OutletPduCResetFrom_Object = MibTableColumn
outletPduCResetFrom = _OutletPduCResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 7),
    _OutletPduCResetFrom_Type()
)
outletPduCResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCResetFrom.setStatus("mandatory")


class _OutletPduCStatus_Type(Integer32):
    """Custom type outletPduCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_OutletPduCStatus_Type.__name__ = "Integer32"
_OutletPduCStatus_Object = MibTableColumn
outletPduCStatus = _OutletPduCStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 2, 1, 8),
    _OutletPduCStatus_Type()
)
outletPduCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduCStatus.setStatus("mandatory")
_PduPwrMonitoringOutletCfgTablePduC_Object = MibTable
pduPwrMonitoringOutletCfgTablePduC = _PduPwrMonitoringOutletCfgTablePduC_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgTablePduC.setStatus("mandatory")
_PduPwrMonitoringOutletCfgPduCEntry_Object = MibTableRow
pduPwrMonitoringOutletCfgPduCEntry = _PduPwrMonitoringOutletCfgPduCEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1)
)
pduPwrMonitoringOutletCfgPduCEntry.setIndexNames(
    (0, "SPSv1-MIB", "outletCfgPduCIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgPduCEntry.setStatus("mandatory")


class _OutletCfgPduCIndex_Type(Integer32):
    """Custom type outletCfgPduCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCfgPduCIndex_Type.__name__ = "Integer32"
_OutletCfgPduCIndex_Object = MibTableColumn
outletCfgPduCIndex = _OutletCfgPduCIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 1),
    _OutletCfgPduCIndex_Type()
)
outletCfgPduCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCfgPduCIndex.setStatus("mandatory")
_OutletCfgPduCName_Type = DisplayString
_OutletCfgPduCName_Object = MibTableColumn
outletCfgPduCName = _OutletCfgPduCName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 2),
    _OutletCfgPduCName_Type()
)
outletCfgPduCName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCName.setStatus("mandatory")


class _OutletCfgPduCDelayOnStatus_Type(Integer32):
    """Custom type outletCfgPduCDelayOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduCDelayOnStatus_Type.__name__ = "Integer32"
_OutletCfgPduCDelayOnStatus_Object = MibTableColumn
outletCfgPduCDelayOnStatus = _OutletCfgPduCDelayOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 3),
    _OutletCfgPduCDelayOnStatus_Type()
)
outletCfgPduCDelayOnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCDelayOnStatus.setStatus("mandatory")
_OutletCfgPduCDelayOnTime_Type = Integer32
_OutletCfgPduCDelayOnTime_Object = MibTableColumn
outletCfgPduCDelayOnTime = _OutletCfgPduCDelayOnTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 4),
    _OutletCfgPduCDelayOnTime_Type()
)
outletCfgPduCDelayOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCDelayOnTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduCDelayOnTime.setUnits("seconds")


class _OutletCfgPduCDelayOffStatus_Type(Integer32):
    """Custom type outletCfgPduCDelayOffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduCDelayOffStatus_Type.__name__ = "Integer32"
_OutletCfgPduCDelayOffStatus_Object = MibTableColumn
outletCfgPduCDelayOffStatus = _OutletCfgPduCDelayOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 5),
    _OutletCfgPduCDelayOffStatus_Type()
)
outletCfgPduCDelayOffStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCDelayOffStatus.setStatus("mandatory")
_OutletCfgPduCDelayOffTime_Type = Integer32
_OutletCfgPduCDelayOffTime_Object = MibTableColumn
outletCfgPduCDelayOffTime = _OutletCfgPduCDelayOffTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 6),
    _OutletCfgPduCDelayOffTime_Type()
)
outletCfgPduCDelayOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCDelayOffTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduCDelayOffTime.setUnits("seconds")
_OutletCfgPduCReboot_Type = Integer32
_OutletCfgPduCReboot_Object = MibTableColumn
outletCfgPduCReboot = _OutletCfgPduCReboot_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 7),
    _OutletCfgPduCReboot_Type()
)
outletCfgPduCReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCReboot.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduCReboot.setUnits("seconds")
_OutletCfgPduCOverCurrCritical_Type = Integer32
_OutletCfgPduCOverCurrCritical_Object = MibTableColumn
outletCfgPduCOverCurrCritical = _OutletCfgPduCOverCurrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 8),
    _OutletCfgPduCOverCurrCritical_Type()
)
outletCfgPduCOverCurrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCOverCurrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduCOverCurrCritical.setUnits("0.1A")
_OutletCfgPduCOverCurrWarning_Type = Integer32
_OutletCfgPduCOverCurrWarning_Object = MibTableColumn
outletCfgPduCOverCurrWarning = _OutletCfgPduCOverCurrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 9),
    _OutletCfgPduCOverCurrWarning_Type()
)
outletCfgPduCOverCurrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCOverCurrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduCOverCurrWarning.setUnits("0.1A")
_OutletCfgPduCOverPwrCritical_Type = Integer32
_OutletCfgPduCOverPwrCritical_Object = MibTableColumn
outletCfgPduCOverPwrCritical = _OutletCfgPduCOverPwrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 10),
    _OutletCfgPduCOverPwrCritical_Type()
)
outletCfgPduCOverPwrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCOverPwrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduCOverPwrCritical.setUnits("1W")
_OutletCfgPduCOverPwrWarning_Type = Integer32
_OutletCfgPduCOverPwrWarning_Object = MibTableColumn
outletCfgPduCOverPwrWarning = _OutletCfgPduCOverPwrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 3, 1, 11),
    _OutletCfgPduCOverPwrWarning_Type()
)
outletCfgPduCOverPwrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduCOverPwrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduCOverPwrWarning.setUnits("1W")
_PduPwrMonitoringOutletCtlTablePduC_Object = MibTable
pduPwrMonitoringOutletCtlTablePduC = _PduPwrMonitoringOutletCtlTablePduC_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 4)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlTablePduC.setStatus("mandatory")
_PduPwrMonitoringOutletCtlPduCEntry_Object = MibTableRow
pduPwrMonitoringOutletCtlPduCEntry = _PduPwrMonitoringOutletCtlPduCEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 4, 1)
)
pduPwrMonitoringOutletCtlPduCEntry.setIndexNames(
    (0, "SPSv1-MIB", "outletCtlPduCIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlPduCEntry.setStatus("mandatory")


class _OutletCtlPduCIndex_Type(Integer32):
    """Custom type outletCtlPduCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCtlPduCIndex_Type.__name__ = "Integer32"
_OutletCtlPduCIndex_Object = MibTableColumn
outletCtlPduCIndex = _OutletCtlPduCIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 4, 1, 1),
    _OutletCtlPduCIndex_Type()
)
outletCtlPduCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCtlPduCIndex.setStatus("mandatory")


class _OutletCtlPduCControl_Type(Integer32):
    """Custom type outletCtlPduCControl based on Integer32"""
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
        *(("immediateOn", 1),
          ("delayedOn", 2),
          ("immediateOff", 3),
          ("delayedOff", 4),
          ("immediateCycle", 5),
          ("delayedCycle", 6))
    )


_OutletCtlPduCControl_Type.__name__ = "Integer32"
_OutletCtlPduCControl_Object = MibTableColumn
outletCtlPduCControl = _OutletCtlPduCControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 3, 4, 1, 2),
    _OutletCtlPduCControl_Type()
)
outletCtlPduCControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCtlPduCControl.setStatus("mandatory")
_PduPwrMonitoringOutletPduD_ObjectIdentity = ObjectIdentity
pduPwrMonitoringOutletPduD = _PduPwrMonitoringOutletPduD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4)
)
_PduPwrMonitoringOutletNumPduD_Type = Integer32
_PduPwrMonitoringOutletNumPduD_Object = MibScalar
pduPwrMonitoringOutletNumPduD = _PduPwrMonitoringOutletNumPduD_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 1),
    _PduPwrMonitoringOutletNumPduD_Type()
)
pduPwrMonitoringOutletNumPduD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletNumPduD.setStatus("mandatory")
_PduPwrMonitoringOutletStatusTablePduD_Object = MibTable
pduPwrMonitoringOutletStatusTablePduD = _PduPwrMonitoringOutletStatusTablePduD_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusTablePduD.setStatus("mandatory")
_PduPwrMonitoringOutletStatusPduDEntry_Object = MibTableRow
pduPwrMonitoringOutletStatusPduDEntry = _PduPwrMonitoringOutletStatusPduDEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1)
)
pduPwrMonitoringOutletStatusPduDEntry.setIndexNames(
    (0, "SPSv1-MIB", "outletPduDIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletStatusPduDEntry.setStatus("mandatory")


class _OutletPduDIndex_Type(Integer32):
    """Custom type outletPduDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletPduDIndex_Type.__name__ = "Integer32"
_OutletPduDIndex_Object = MibTableColumn
outletPduDIndex = _OutletPduDIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 1),
    _OutletPduDIndex_Type()
)
outletPduDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDIndex.setStatus("mandatory")


class _OutletPduDState_Type(Integer32):
    """Custom type outletPduDState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_OutletPduDState_Type.__name__ = "Integer32"
_OutletPduDState_Object = MibTableColumn
outletPduDState = _OutletPduDState_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 2),
    _OutletPduDState_Type()
)
outletPduDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDState.setStatus("mandatory")
_OutletPduDCurrent_Type = Integer32
_OutletPduDCurrent_Object = MibTableColumn
outletPduDCurrent = _OutletPduDCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 3),
    _OutletPduDCurrent_Type()
)
outletPduDCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduDCurrent.setUnits("0.01A")
_OutletPduDPwrFactor_Type = Integer32
_OutletPduDPwrFactor_Object = MibTableColumn
outletPduDPwrFactor = _OutletPduDPwrFactor_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 4),
    _OutletPduDPwrFactor_Type()
)
outletPduDPwrFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDPwrFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduDPwrFactor.setUnits("0.1%")
_OutletPduDPower_Type = Integer32
_OutletPduDPower_Object = MibTableColumn
outletPduDPower = _OutletPduDPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 5),
    _OutletPduDPower_Type()
)
outletPduDPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduDPower.setUnits("0.1W")
_OutletPduDEnergy_Type = Integer32
_OutletPduDEnergy_Object = MibTableColumn
outletPduDEnergy = _OutletPduDEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 6),
    _OutletPduDEnergy_Type()
)
outletPduDEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletPduDEnergy.setUnits("KWh")
_OutletPduDResetFrom_Type = DisplayString
_OutletPduDResetFrom_Object = MibTableColumn
outletPduDResetFrom = _OutletPduDResetFrom_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 7),
    _OutletPduDResetFrom_Type()
)
outletPduDResetFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDResetFrom.setStatus("mandatory")


class _OutletPduDStatus_Type(Integer32):
    """Custom type outletPduDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_OutletPduDStatus_Type.__name__ = "Integer32"
_OutletPduDStatus_Object = MibTableColumn
outletPduDStatus = _OutletPduDStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 2, 1, 8),
    _OutletPduDStatus_Type()
)
outletPduDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPduDStatus.setStatus("mandatory")
_PduPwrMonitoringOutletCfgTablePduD_Object = MibTable
pduPwrMonitoringOutletCfgTablePduD = _PduPwrMonitoringOutletCfgTablePduD_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgTablePduD.setStatus("mandatory")
_PduPwrMonitoringOutletCfgPduDEntry_Object = MibTableRow
pduPwrMonitoringOutletCfgPduDEntry = _PduPwrMonitoringOutletCfgPduDEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1)
)
pduPwrMonitoringOutletCfgPduDEntry.setIndexNames(
    (0, "SPSv1-MIB", "outletCfgPduDIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCfgPduDEntry.setStatus("mandatory")


class _OutletCfgPduDIndex_Type(Integer32):
    """Custom type outletCfgPduDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCfgPduDIndex_Type.__name__ = "Integer32"
_OutletCfgPduDIndex_Object = MibTableColumn
outletCfgPduDIndex = _OutletCfgPduDIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 1),
    _OutletCfgPduDIndex_Type()
)
outletCfgPduDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCfgPduDIndex.setStatus("mandatory")
_OutletCfgPduDName_Type = DisplayString
_OutletCfgPduDName_Object = MibTableColumn
outletCfgPduDName = _OutletCfgPduDName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 2),
    _OutletCfgPduDName_Type()
)
outletCfgPduDName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDName.setStatus("mandatory")


class _OutletCfgPduDDelayOnStatus_Type(Integer32):
    """Custom type outletCfgPduDDelayOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduDDelayOnStatus_Type.__name__ = "Integer32"
_OutletCfgPduDDelayOnStatus_Object = MibTableColumn
outletCfgPduDDelayOnStatus = _OutletCfgPduDDelayOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 3),
    _OutletCfgPduDDelayOnStatus_Type()
)
outletCfgPduDDelayOnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDDelayOnStatus.setStatus("mandatory")
_OutletCfgPduDDelayOnTime_Type = Integer32
_OutletCfgPduDDelayOnTime_Object = MibTableColumn
outletCfgPduDDelayOnTime = _OutletCfgPduDDelayOnTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 4),
    _OutletCfgPduDDelayOnTime_Type()
)
outletCfgPduDDelayOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDDelayOnTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduDDelayOnTime.setUnits("seconds")


class _OutletCfgPduDDelayOffStatus_Type(Integer32):
    """Custom type outletCfgPduDDelayOffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodelay", 1),
          ("delay", 2))
    )


_OutletCfgPduDDelayOffStatus_Type.__name__ = "Integer32"
_OutletCfgPduDDelayOffStatus_Object = MibTableColumn
outletCfgPduDDelayOffStatus = _OutletCfgPduDDelayOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 5),
    _OutletCfgPduDDelayOffStatus_Type()
)
outletCfgPduDDelayOffStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDDelayOffStatus.setStatus("mandatory")
_OutletCfgPduDDelayOffTime_Type = Integer32
_OutletCfgPduDDelayOffTime_Object = MibTableColumn
outletCfgPduDDelayOffTime = _OutletCfgPduDDelayOffTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 6),
    _OutletCfgPduDDelayOffTime_Type()
)
outletCfgPduDDelayOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDDelayOffTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduDDelayOffTime.setUnits("seconds")
_OutletCfgPduDReboot_Type = Integer32
_OutletCfgPduDReboot_Object = MibTableColumn
outletCfgPduDReboot = _OutletCfgPduDReboot_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 7),
    _OutletCfgPduDReboot_Type()
)
outletCfgPduDReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDReboot.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduDReboot.setUnits("seconds")
_OutletCfgPduDOverCurrCritical_Type = Integer32
_OutletCfgPduDOverCurrCritical_Object = MibTableColumn
outletCfgPduDOverCurrCritical = _OutletCfgPduDOverCurrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 8),
    _OutletCfgPduDOverCurrCritical_Type()
)
outletCfgPduDOverCurrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDOverCurrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduDOverCurrCritical.setUnits("0.1A")
_OutletCfgPduDOverCurrWarning_Type = Integer32
_OutletCfgPduDOverCurrWarning_Object = MibTableColumn
outletCfgPduDOverCurrWarning = _OutletCfgPduDOverCurrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 9),
    _OutletCfgPduDOverCurrWarning_Type()
)
outletCfgPduDOverCurrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDOverCurrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduDOverCurrWarning.setUnits("0.1A")
_OutletCfgPduDOverPwrCritical_Type = Integer32
_OutletCfgPduDOverPwrCritical_Object = MibTableColumn
outletCfgPduDOverPwrCritical = _OutletCfgPduDOverPwrCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 10),
    _OutletCfgPduDOverPwrCritical_Type()
)
outletCfgPduDOverPwrCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDOverPwrCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduDOverPwrCritical.setUnits("1W")
_OutletCfgPduDOverPwrWarning_Type = Integer32
_OutletCfgPduDOverPwrWarning_Object = MibTableColumn
outletCfgPduDOverPwrWarning = _OutletCfgPduDOverPwrWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 3, 1, 11),
    _OutletCfgPduDOverPwrWarning_Type()
)
outletCfgPduDOverPwrWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCfgPduDOverPwrWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    outletCfgPduDOverPwrWarning.setUnits("1W")
_PduPwrMonitoringOutletCtlTablePduD_Object = MibTable
pduPwrMonitoringOutletCtlTablePduD = _PduPwrMonitoringOutletCtlTablePduD_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 4)
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlTablePduD.setStatus("mandatory")
_PduPwrMonitoringOutletCtlPduDEntry_Object = MibTableRow
pduPwrMonitoringOutletCtlPduDEntry = _PduPwrMonitoringOutletCtlPduDEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 4, 1)
)
pduPwrMonitoringOutletCtlPduDEntry.setIndexNames(
    (0, "SPSv1-MIB", "outletCtlPduDIndex"),
)
if mibBuilder.loadTexts:
    pduPwrMonitoringOutletCtlPduDEntry.setStatus("mandatory")


class _OutletCtlPduDIndex_Type(Integer32):
    """Custom type outletCtlPduDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 41),
    )


_OutletCtlPduDIndex_Type.__name__ = "Integer32"
_OutletCtlPduDIndex_Object = MibTableColumn
outletCtlPduDIndex = _OutletCtlPduDIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 4, 1, 1),
    _OutletCtlPduDIndex_Type()
)
outletCtlPduDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCtlPduDIndex.setStatus("mandatory")


class _OutletCtlPduDControl_Type(Integer32):
    """Custom type outletCtlPduDControl based on Integer32"""
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
        *(("immediateOn", 1),
          ("delayedOn", 2),
          ("immediateOff", 3),
          ("delayedOff", 4),
          ("immediateCycle", 5),
          ("delayedCycle", 6))
    )


_OutletCtlPduDControl_Type.__name__ = "Integer32"
_OutletCtlPduDControl_Object = MibTableColumn
outletCtlPduDControl = _OutletCtlPduDControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 6, 2, 4, 4, 1, 2),
    _OutletCtlPduDControl_Type()
)
outletCtlPduDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCtlPduDControl.setStatus("mandatory")
_PduEnvMonitoring_ObjectIdentity = ObjectIdentity
pduEnvMonitoring = _PduEnvMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7)
)
_PduEnvMonitoringStatus_ObjectIdentity = ObjectIdentity
pduEnvMonitoringStatus = _PduEnvMonitoringStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 1)
)
_PduEnvMonitoringTemp_Type = Integer32
_PduEnvMonitoringTemp_Object = MibScalar
pduEnvMonitoringTemp = _PduEnvMonitoringTemp_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 1, 1),
    _PduEnvMonitoringTemp_Type()
)
pduEnvMonitoringTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEnvMonitoringTemp.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringTemp.setUnits("degC")
_PduEnvMonitoringHumi_Type = Integer32
_PduEnvMonitoringHumi_Object = MibScalar
pduEnvMonitoringHumi = _PduEnvMonitoringHumi_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 1, 2),
    _PduEnvMonitoringHumi_Type()
)
pduEnvMonitoringHumi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumi.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumi.setUnits("0.1%")


class _PduEnvMonitoringTempAlarm_Type(Integer32):
    """Custom type pduEnvMonitoringTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_PduEnvMonitoringTempAlarm_Type.__name__ = "Integer32"
_PduEnvMonitoringTempAlarm_Object = MibScalar
pduEnvMonitoringTempAlarm = _PduEnvMonitoringTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 1, 3),
    _PduEnvMonitoringTempAlarm_Type()
)
pduEnvMonitoringTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempAlarm.setStatus("mandatory")


class _PduEnvMonitoringHumiAlarm_Type(Integer32):
    """Custom type pduEnvMonitoringHumiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_PduEnvMonitoringHumiAlarm_Type.__name__ = "Integer32"
_PduEnvMonitoringHumiAlarm_Object = MibScalar
pduEnvMonitoringHumiAlarm = _PduEnvMonitoringHumiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 1, 4),
    _PduEnvMonitoringHumiAlarm_Type()
)
pduEnvMonitoringHumiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiAlarm.setStatus("mandatory")
_PduEnvMonitoringCfg_ObjectIdentity = ObjectIdentity
pduEnvMonitoringCfg = _PduEnvMonitoringCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2)
)


class _PduEnvMonitoringControl_Type(Integer32):
    """Custom type pduEnvMonitoringControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduEnvMonitoringControl_Type.__name__ = "Integer32"
_PduEnvMonitoringControl_Object = MibScalar
pduEnvMonitoringControl = _PduEnvMonitoringControl_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 1),
    _PduEnvMonitoringControl_Type()
)
pduEnvMonitoringControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringControl.setStatus("mandatory")
_PduEnvMonitoringTempHighCritical_Type = Integer32
_PduEnvMonitoringTempHighCritical_Object = MibScalar
pduEnvMonitoringTempHighCritical = _PduEnvMonitoringTempHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 2),
    _PduEnvMonitoringTempHighCritical_Type()
)
pduEnvMonitoringTempHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempHighCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempHighCritical.setUnits("degC")
_PduEnvMonitoringTempHighWarning_Type = Integer32
_PduEnvMonitoringTempHighWarning_Object = MibScalar
pduEnvMonitoringTempHighWarning = _PduEnvMonitoringTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 3),
    _PduEnvMonitoringTempHighWarning_Type()
)
pduEnvMonitoringTempHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempHighWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempHighWarning.setUnits("degC")
_PduEnvMonitoringTempLowCritical_Type = Integer32
_PduEnvMonitoringTempLowCritical_Object = MibScalar
pduEnvMonitoringTempLowCritical = _PduEnvMonitoringTempLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 4),
    _PduEnvMonitoringTempLowCritical_Type()
)
pduEnvMonitoringTempLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempLowCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempLowCritical.setUnits("degC")
_PduEnvMonitoringTempLowWarning_Type = Integer32
_PduEnvMonitoringTempLowWarning_Object = MibScalar
pduEnvMonitoringTempLowWarning = _PduEnvMonitoringTempLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 5),
    _PduEnvMonitoringTempLowWarning_Type()
)
pduEnvMonitoringTempLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempLowWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempLowWarning.setUnits("degC")
_PduEnvMonitoringTempHystersis_Type = Integer32
_PduEnvMonitoringTempHystersis_Object = MibScalar
pduEnvMonitoringTempHystersis = _PduEnvMonitoringTempHystersis_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 6),
    _PduEnvMonitoringTempHystersis_Type()
)
pduEnvMonitoringTempHystersis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempHystersis.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempHystersis.setUnits("degC")
_PduEnvMonitoringTempOffset_Type = Integer32
_PduEnvMonitoringTempOffset_Object = MibScalar
pduEnvMonitoringTempOffset = _PduEnvMonitoringTempOffset_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 7),
    _PduEnvMonitoringTempOffset_Type()
)
pduEnvMonitoringTempOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempOffset.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringTempOffset.setUnits("degC")
_PduEnvMonitoringHumiHighCritical_Type = Integer32
_PduEnvMonitoringHumiHighCritical_Object = MibScalar
pduEnvMonitoringHumiHighCritical = _PduEnvMonitoringHumiHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 8),
    _PduEnvMonitoringHumiHighCritical_Type()
)
pduEnvMonitoringHumiHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiHighCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiHighCritical.setUnits("0.1%")
_PduEnvMonitoringHumiHighWarning_Type = Integer32
_PduEnvMonitoringHumiHighWarning_Object = MibScalar
pduEnvMonitoringHumiHighWarning = _PduEnvMonitoringHumiHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 9),
    _PduEnvMonitoringHumiHighWarning_Type()
)
pduEnvMonitoringHumiHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiHighWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiHighWarning.setUnits("0.1%")
_PduEnvMonitoringHumiLowCritical_Type = Integer32
_PduEnvMonitoringHumiLowCritical_Object = MibScalar
pduEnvMonitoringHumiLowCritical = _PduEnvMonitoringHumiLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 10),
    _PduEnvMonitoringHumiLowCritical_Type()
)
pduEnvMonitoringHumiLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiLowCritical.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiLowCritical.setUnits("0.1%")
_PduEnvMonitoringHumiLowWarning_Type = Integer32
_PduEnvMonitoringHumiLowWarning_Object = MibScalar
pduEnvMonitoringHumiLowWarning = _PduEnvMonitoringHumiLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 11),
    _PduEnvMonitoringHumiLowWarning_Type()
)
pduEnvMonitoringHumiLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiLowWarning.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiLowWarning.setUnits("0.1%")
_PduEnvMonitoringHumiHystersis_Type = Integer32
_PduEnvMonitoringHumiHystersis_Object = MibScalar
pduEnvMonitoringHumiHystersis = _PduEnvMonitoringHumiHystersis_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 12),
    _PduEnvMonitoringHumiHystersis_Type()
)
pduEnvMonitoringHumiHystersis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiHystersis.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiHystersis.setUnits("0.1%")
_PduEnvMonitoringHumiOffset_Type = Integer32
_PduEnvMonitoringHumiOffset_Object = MibScalar
pduEnvMonitoringHumiOffset = _PduEnvMonitoringHumiOffset_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 1, 7, 2, 13),
    _PduEnvMonitoringHumiOffset_Type()
)
pduEnvMonitoringHumiOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiOffset.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEnvMonitoringHumiOffset.setUnits("0.1%")
_PduTraps_ObjectIdentity = ObjectIdentity
pduTraps = _PduTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2)
)

# Managed Objects groups


# Notification objects

pduSystemColdBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 1)
)
if mibBuilder.loadTexts:
    pduSystemColdBoot.setStatus(
        ""
    )

pduSystemWarmBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 2)
)
if mibBuilder.loadTexts:
    pduSystemWarmBoot.setStatus(
        ""
    )

pduSystemRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 3)
)
if mibBuilder.loadTexts:
    pduSystemRestart.setStatus(
        ""
    )

pduResetToDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 4)
)
if mibBuilder.loadTexts:
    pduResetToDefault.setStatus(
        ""
    )

pduFirmUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 5)
)
if mibBuilder.loadTexts:
    pduFirmUpgrade.setStatus(
        ""
    )

pduSystemLogClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 6)
)
if mibBuilder.loadTexts:
    pduSystemLogClear.setStatus(
        ""
    )

pduEventlogClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 7)
)
if mibBuilder.loadTexts:
    pduEventlogClear.setStatus(
        ""
    )

pduInletHistoryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 8)
)
if mibBuilder.loadTexts:
    pduInletHistoryClear.setStatus(
        ""
    )

pduOutletHistoryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 9)
)
if mibBuilder.loadTexts:
    pduOutletHistoryClear.setStatus(
        ""
    )

pduSystemTimeChangeUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 10)
)
if mibBuilder.loadTexts:
    pduSystemTimeChangeUser.setStatus(
        ""
    )

pduSystemTimeChangeNtp = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 11)
)
if mibBuilder.loadTexts:
    pduSystemTimeChangeNtp.setStatus(
        ""
    )

pduSystemTimeChangeRtc = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 12)
)
if mibBuilder.loadTexts:
    pduSystemTimeChangeRtc.setStatus(
        ""
    )

pduMailTestPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 13)
)
if mibBuilder.loadTexts:
    pduMailTestPass.setStatus(
        ""
    )

pduMailTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 14)
)
if mibBuilder.loadTexts:
    pduMailTestFail.setStatus(
        ""
    )

pduMailSentPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 15)
)
if mibBuilder.loadTexts:
    pduMailSentPass.setStatus(
        ""
    )

pduMailSentFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 16)
)
if mibBuilder.loadTexts:
    pduMailSentFail.setStatus(
        ""
    )

pduSystemCfgChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 17)
)
if mibBuilder.loadTexts:
    pduSystemCfgChange.setStatus(
        ""
    )

pduSystemParamImport = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 18)
)
if mibBuilder.loadTexts:
    pduSystemParamImport.setStatus(
        ""
    )

pduInletCommLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 19)
)
if mibBuilder.loadTexts:
    pduInletCommLost.setStatus(
        ""
    )

pduInletCommRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 20)
)
if mibBuilder.loadTexts:
    pduInletCommRestore.setStatus(
        ""
    )

pduOutletCommLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 21)
)
if mibBuilder.loadTexts:
    pduOutletCommLost.setStatus(
        ""
    )

pduOutletCommRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 22)
)
if mibBuilder.loadTexts:
    pduOutletCommRestore.setStatus(
        ""
    )

pduOutletOnUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 23)
)
if mibBuilder.loadTexts:
    pduOutletOnUser.setStatus(
        ""
    )

pduOutletOnSchedule = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 24)
)
if mibBuilder.loadTexts:
    pduOutletOnSchedule.setStatus(
        ""
    )

pduOutletOffUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 25)
)
if mibBuilder.loadTexts:
    pduOutletOffUser.setStatus(
        ""
    )

pduOutletOffSchedule = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 26)
)
if mibBuilder.loadTexts:
    pduOutletOffSchedule.setStatus(
        ""
    )

pduOutletRebootUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 27)
)
if mibBuilder.loadTexts:
    pduOutletRebootUser.setStatus(
        ""
    )

pduOutletRebootSchedule = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 28)
)
if mibBuilder.loadTexts:
    pduOutletRebootSchedule.setStatus(
        ""
    )

pduInletEnergyReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 29)
)
if mibBuilder.loadTexts:
    pduInletEnergyReset.setStatus(
        ""
    )

pduOutletEnergyReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 30)
)
if mibBuilder.loadTexts:
    pduOutletEnergyReset.setStatus(
        ""
    )

pduSetUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 31)
)
if mibBuilder.loadTexts:
    pduSetUser.setStatus(
        ""
    )

pduDeletUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 32)
)
if mibBuilder.loadTexts:
    pduDeletUser.setStatus(
        ""
    )

pduUpgradeInletSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 33)
)
if mibBuilder.loadTexts:
    pduUpgradeInletSuccess.setStatus(
        ""
    )

pduUpgradeInletFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 34)
)
if mibBuilder.loadTexts:
    pduUpgradeInletFail.setStatus(
        ""
    )

pduUpgradeOutletSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 35)
)
if mibBuilder.loadTexts:
    pduUpgradeOutletSuccess.setStatus(
        ""
    )

pduUpgradeOutletFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 36)
)
if mibBuilder.loadTexts:
    pduUpgradeOutletFail.setStatus(
        ""
    )

pduEmdTempHighWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 101)
)
if mibBuilder.loadTexts:
    pduEmdTempHighWarnToNormal.setStatus(
        ""
    )

pduEmdTempHighWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 102)
)
if mibBuilder.loadTexts:
    pduEmdTempHighWarn.setStatus(
        ""
    )

pduEmdTempLowWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 103)
)
if mibBuilder.loadTexts:
    pduEmdTempLowWarnToNormal.setStatus(
        ""
    )

pduEmdTempLowWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 104)
)
if mibBuilder.loadTexts:
    pduEmdTempLowWarn.setStatus(
        ""
    )

pduEmdTempHighCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 105)
)
if mibBuilder.loadTexts:
    pduEmdTempHighCritToWarn.setStatus(
        ""
    )

pduEmdTempHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 106)
)
if mibBuilder.loadTexts:
    pduEmdTempHighCritical.setStatus(
        ""
    )

pduEmdTempLowCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 107)
)
if mibBuilder.loadTexts:
    pduEmdTempLowCritToWarn.setStatus(
        ""
    )

pduEmdTempLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 108)
)
if mibBuilder.loadTexts:
    pduEmdTempLowCritical.setStatus(
        ""
    )

pduEmdHumiHighWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 109)
)
if mibBuilder.loadTexts:
    pduEmdHumiHighWarnToNormal.setStatus(
        ""
    )

pduEmdHumiHighWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 110)
)
if mibBuilder.loadTexts:
    pduEmdHumiHighWarn.setStatus(
        ""
    )

pduEmdHumiLowWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 111)
)
if mibBuilder.loadTexts:
    pduEmdHumiLowWarnToNormal.setStatus(
        ""
    )

pduEmdHumiLowWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 112)
)
if mibBuilder.loadTexts:
    pduEmdHumiLowWarn.setStatus(
        ""
    )

pduEmdHumiHighCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 113)
)
if mibBuilder.loadTexts:
    pduEmdHumiHighCritToWarn.setStatus(
        ""
    )

pduEmdHumiHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 114)
)
if mibBuilder.loadTexts:
    pduEmdHumiHighCritical.setStatus(
        ""
    )

pduEmdHumiLowCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 115)
)
if mibBuilder.loadTexts:
    pduEmdHumiLowCritToWarn.setStatus(
        ""
    )

pduEmdHumiLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 116)
)
if mibBuilder.loadTexts:
    pduEmdHumiLowCritical.setStatus(
        ""
    )

pduEmdAlarm1NotActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 117)
)
if mibBuilder.loadTexts:
    pduEmdAlarm1NotActive.setStatus(
        ""
    )

pduEmdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 118)
)
if mibBuilder.loadTexts:
    pduEmdAlarm1Active.setStatus(
        ""
    )

pduEmdAlarm2NotActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 119)
)
if mibBuilder.loadTexts:
    pduEmdAlarm2NotActive.setStatus(
        ""
    )

pduEmdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 120)
)
if mibBuilder.loadTexts:
    pduEmdAlarm2Active.setStatus(
        ""
    )

pduRs485Online = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 121)
)
if mibBuilder.loadTexts:
    pduRs485Online.setStatus(
        ""
    )

pduRs485Offline = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 122)
)
if mibBuilder.loadTexts:
    pduRs485Offline.setStatus(
        ""
    )

pduInletLoadCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 123)
)
if mibBuilder.loadTexts:
    pduInletLoadCritToWarn.setStatus(
        ""
    )

pduInletLoadCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 124)
)
if mibBuilder.loadTexts:
    pduInletLoadCritical.setStatus(
        ""
    )

pduInletLoadWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 125)
)
if mibBuilder.loadTexts:
    pduInletLoadWarnToNormal.setStatus(
        ""
    )

pduInletLoadWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 126)
)
if mibBuilder.loadTexts:
    pduInletLoadWarn.setStatus(
        ""
    )

pduInletCurrPhase1CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 127)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1CritToWarn.setStatus(
        ""
    )

pduInletCurrPhase1Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 128)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1Critical.setStatus(
        ""
    )

pduInletCurrPhase1WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 129)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1WarnToNormal.setStatus(
        ""
    )

pduInletCurrPhase1Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 130)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1Warn.setStatus(
        ""
    )

pduInletCurrPhase2CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 131)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2CritToWarn.setStatus(
        ""
    )

pduInletCurrPhase2Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 132)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2Critical.setStatus(
        ""
    )

pduInletCurrPhase2WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 133)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2WarnToNormal.setStatus(
        ""
    )

pduInletCurrPhase2Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 134)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2Warn.setStatus(
        ""
    )

pduInletCurrPhase3CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 135)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3CritToWarn.setStatus(
        ""
    )

pduInletCurrPhase3Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 136)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3Critical.setStatus(
        ""
    )

pduInletCurrPhase3WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 137)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3WarnToNormal.setStatus(
        ""
    )

pduInletCurrPhase3Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 138)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3Warn.setStatus(
        ""
    )

pduInletVoltPhase1CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 139)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase1CritToWarn.setStatus(
        ""
    )

pduInletVoltPhase1Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 140)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase1Critical.setStatus(
        ""
    )

pduInletVoltPhase1WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 141)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase1WarnToNormal.setStatus(
        ""
    )

pduInletVoltPhase1Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 142)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase1Warn.setStatus(
        ""
    )

pduInletVoltPhase2CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 143)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase2CritToWarn.setStatus(
        ""
    )

pduInletVoltPhase2Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 144)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase2Critical.setStatus(
        ""
    )

pduInletVoltPhase2WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 145)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase2WarnToNormal.setStatus(
        ""
    )

pduInletVoltPhase2Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 146)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase2Warn.setStatus(
        ""
    )

pduInletVoltPhase3CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 147)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase3CritToWarn.setStatus(
        ""
    )

pduInletVoltPhase3Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 148)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase3Critical.setStatus(
        ""
    )

pduInletVoltPhase3WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 149)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase3WarnToNormal.setStatus(
        ""
    )

pduInletVoltPhase3Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 150)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase3Warn.setStatus(
        ""
    )

pduOutletCurrCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 151)
)
if mibBuilder.loadTexts:
    pduOutletCurrCritToWarn.setStatus(
        ""
    )

pduOutletCurrCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 152)
)
if mibBuilder.loadTexts:
    pduOutletCurrCritical.setStatus(
        ""
    )

pduOutletCurrWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 153)
)
if mibBuilder.loadTexts:
    pduOutletCurrWarnToNormal.setStatus(
        ""
    )

pduOutletCurrWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 154)
)
if mibBuilder.loadTexts:
    pduOutletCurrWarn.setStatus(
        ""
    )

pduOutletPwrCritTOWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 155)
)
if mibBuilder.loadTexts:
    pduOutletPwrCritTOWarn.setStatus(
        ""
    )

pduOutletPwrCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 156)
)
if mibBuilder.loadTexts:
    pduOutletPwrCritical.setStatus(
        ""
    )

pduOutletPwrWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 157)
)
if mibBuilder.loadTexts:
    pduOutletPwrWarnToNormal.setStatus(
        ""
    )

pduOutletPwrWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 158)
)
if mibBuilder.loadTexts:
    pduOutletPwrWarn.setStatus(
        ""
    )

pduAlarm1Disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 159)
)
if mibBuilder.loadTexts:
    pduAlarm1Disabled.setStatus(
        ""
    )

pduAlarm2Disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 4, 2, 0, 160)
)
if mibBuilder.loadTexts:
    pduAlarm2Disabled.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPSv1-MIB",
    **{"powertek": powertek,
       "product": product,
       "pdu": pdu,
       "sps": sps,
       "pduObjects": pduObjects,
       "pduIdent": pduIdent,
       "pduIdentAgentSoftwareVersion": pduIdentAgentSoftwareVersion,
       "pduIdentSerialNumber": pduIdentSerialNumber,
       "pduNetwork": pduNetwork,
       "pduNetworkTcpip": pduNetworkTcpip,
       "pduNetworkTcpipDhcpControl": pduNetworkTcpipDhcpControl,
       "pduNetworkTcpipIpv4": pduNetworkTcpipIpv4,
       "pduNetworkTcpipIpv4Address": pduNetworkTcpipIpv4Address,
       "pduNetworkTcpipIpv4Gateway": pduNetworkTcpipIpv4Gateway,
       "pduNetworkTcpipIpv4Subnet": pduNetworkTcpipIpv4Subnet,
       "pduNetworkTcpipIpv4PrimaryDNS": pduNetworkTcpipIpv4PrimaryDNS,
       "pduNetworkTcpipIpv4SecondaryDNS": pduNetworkTcpipIpv4SecondaryDNS,
       "pduNetworkTcpipIpv6": pduNetworkTcpipIpv6,
       "pduNetworkTcpipIpv6Control": pduNetworkTcpipIpv6Control,
       "pduNetworkTcpipIpv6AutoConfig": pduNetworkTcpipIpv6AutoConfig,
       "pduNetworkTcpipIpv6Address": pduNetworkTcpipIpv6Address,
       "pduNetworkTcpipIpv6Prefix": pduNetworkTcpipIpv6Prefix,
       "pduNetworkTcpipIpv6Router": pduNetworkTcpipIpv6Router,
       "pduNetworkTcpipIpv6PrimaryDNS": pduNetworkTcpipIpv6PrimaryDNS,
       "pduNetworkTcpipIpv6SecondaryDNS": pduNetworkTcpipIpv6SecondaryDNS,
       "pduNetworkSecurity": pduNetworkSecurity,
       "pduNetworkSecurityControl": pduNetworkSecurityControl,
       "pduNetworkSecuritySsh": pduNetworkSecuritySsh,
       "pduNetworkSecuritySshControl": pduNetworkSecuritySshControl,
       "pduNetworkSecuritySshInterval": pduNetworkSecuritySshInterval,
       "pduNetworkSecuritySshFailTimes": pduNetworkSecuritySshFailTimes,
       "pduNetworkSecuritySshBlock": pduNetworkSecuritySshBlock,
       "pduNetworkSecuritySnmp": pduNetworkSecuritySnmp,
       "pduNetworkSecuritySnmpControl": pduNetworkSecuritySnmpControl,
       "pduNetworkSecuritySnmpInterval": pduNetworkSecuritySnmpInterval,
       "pduNetworkSecuritySnmpFailTimes": pduNetworkSecuritySnmpFailTimes,
       "pduNetworkSecuritySnmpBlock": pduNetworkSecuritySnmpBlock,
       "pduNetworkSecurityHttp": pduNetworkSecurityHttp,
       "pduNetworkSecurityHttpControl": pduNetworkSecurityHttpControl,
       "pduNetworkSecurityHttpInterval": pduNetworkSecurityHttpInterval,
       "pduNetworkSecurityHttpFailTimes": pduNetworkSecurityHttpFailTimes,
       "pduNetworkSecurityHttpBlock": pduNetworkSecurityHttpBlock,
       "pduNetworkService": pduNetworkService,
       "pduNetworkServiceSsh": pduNetworkServiceSsh,
       "pduNetworkServiceSshControl": pduNetworkServiceSshControl,
       "pduNetworkServiceSshPort": pduNetworkServiceSshPort,
       "pduNetworkServiceSsl": pduNetworkServiceSsl,
       "pduNetworkServiceSslControl": pduNetworkServiceSslControl,
       "pduNetworkServiceSslPort": pduNetworkServiceSslPort,
       "pduNetworkServiceSslForce": pduNetworkServiceSslForce,
       "pduNetworkServicePingControl": pduNetworkServicePingControl,
       "pduNetworkServiceRadius": pduNetworkServiceRadius,
       "pduNetworkServiceRadiusControl": pduNetworkServiceRadiusControl,
       "pduNetworkServiceRadiusIp": pduNetworkServiceRadiusIp,
       "pduNetworkServiceRadiusPort": pduNetworkServiceRadiusPort,
       "pduNetworkServiceRadiusSecretKey": pduNetworkServiceRadiusSecretKey,
       "pduNetworkServiceRadiusTimeout": pduNetworkServiceRadiusTimeout,
       "pduNetworkServiceRadiusRetry": pduNetworkServiceRadiusRetry,
       "pduSystem": pduSystem,
       "pduSystemName": pduSystemName,
       "pduSystemContact": pduSystemContact,
       "pduSystemLocation": pduSystemLocation,
       "pduSystemLogInterval": pduSystemLogInterval,
       "pduSystemWebRefresh": pduSystemWebRefresh,
       "pduSystemTime": pduSystemTime,
       "pduSystemTimeDisplay": pduSystemTimeDisplay,
       "pduSystemTimeZone": pduSystemTimeZone,
       "pduSystemTimeFormat": pduSystemTimeFormat,
       "pduSystemTimeSetting": pduSystemTimeSetting,
       "pduSystemTimeDayLightSaving": pduSystemTimeDayLightSaving,
       "pduSystemTimeManual": pduSystemTimeManual,
       "pduSystemTimeManualDate": pduSystemTimeManualDate,
       "pduSystemTimeManualTime": pduSystemTimeManualTime,
       "pduSystemTimeNtp": pduSystemTimeNtp,
       "pduSystemTimeNtpControl": pduSystemTimeNtpControl,
       "pduSystemTimeNtpServer": pduSystemTimeNtpServer,
       "pduSystemTimeNtpSyncInterval": pduSystemTimeNtpSyncInterval,
       "pduSystemTimeNtpSyncUnit": pduSystemTimeNtpSyncUnit,
       "pduSystemResetToDefault": pduSystemResetToDefault,
       "pduSystemReboot": pduSystemReboot,
       "pduSNMP": pduSNMP,
       "pduSnmpControl": pduSnmpControl,
       "pduSnmpPort": pduSnmpPort,
       "pduSnmpVersion": pduSnmpVersion,
       "pduSnmpTrapsReceiversTable": pduSnmpTrapsReceiversTable,
       "pduSnmpTrapsReceiversEntry": pduSnmpTrapsReceiversEntry,
       "trapsIndex": trapsIndex,
       "trapsReceiverAddr": trapsReceiverAddr,
       "receiverEventLevel": receiverEventLevel,
       "receiverSnmpVer": receiverSnmpVer,
       "receiverDescription": receiverDescription,
       "pduEmail": pduEmail,
       "pduEmailServer": pduEmailServer,
       "pduEmailPort": pduEmailPort,
       "pduEmailSenderEmail": pduEmailSenderEmail,
       "pduEmailPrefix": pduEmailPrefix,
       "pduEmailAuthControl": pduEmailAuthControl,
       "pduEmailAuthUsername": pduEmailAuthUsername,
       "pduEmailAuthPassword": pduEmailAuthPassword,
       "pduEmailReceiversTable": pduEmailReceiversTable,
       "pduEmailReceiversEntry": pduEmailReceiversEntry,
       "mailRecvIndex": mailRecvIndex,
       "mailRecvReceiverAddr": mailRecvReceiverAddr,
       "mailRecvEmailType": mailRecvEmailType,
       "mailRecvEventLevel": mailRecvEventLevel,
       "mailRecvDescription": mailRecvDescription,
       "pduPwrMonitoring": pduPwrMonitoring,
       "pduPwrMonitoringInlet": pduPwrMonitoringInlet,
       "pduPwrMonitoringInletNum": pduPwrMonitoringInletNum,
       "pduPwrMonitoringInletStatusTable": pduPwrMonitoringInletStatusTable,
       "pduPwrMonitoringInletStatusEntry": pduPwrMonitoringInletStatusEntry,
       "inletIndex": inletIndex,
       "inletPowerAll": inletPowerAll,
       "inletResetFrom": inletResetFrom,
       "inletEnergy": inletEnergy,
       "inletStatus": inletStatus,
       "inletCurrPhase1": inletCurrPhase1,
       "inletCurrPhase2": inletCurrPhase2,
       "inletCurrPhase3": inletCurrPhase3,
       "inletVoltPhase1": inletVoltPhase1,
       "inletVoltPhase2": inletVoltPhase2,
       "inletVoltPhase3": inletVoltPhase3,
       "inletPwrFactorPhase1": inletPwrFactorPhase1,
       "inletPwrFactorPhase2": inletPwrFactorPhase2,
       "inletPwrFactorPhase3": inletPwrFactorPhase3,
       "inletPowerPhase1": inletPowerPhase1,
       "inletPowerPhase2": inletPowerPhase2,
       "inletPowerPhase3": inletPowerPhase3,
       "inletStatusPhase1": inletStatusPhase1,
       "inletStatusPhase2": inletStatusPhase2,
       "inletStatusPhase3": inletStatusPhase3,
       "pduPwrMonitoringInletCfgTable": pduPwrMonitoringInletCfgTable,
       "pduPwrMonitoringInletCfgEntry": pduPwrMonitoringInletCfgEntry,
       "inletCfgIndex": inletCfgIndex,
       "inletCfgLoadCritical": inletCfgLoadCritical,
       "inletCfgLoadWarning": inletCfgLoadWarning,
       "inletCfgCurrCritPhase1": inletCfgCurrCritPhase1,
       "inletCfgCurrCritPhase2": inletCfgCurrCritPhase2,
       "inletCfgCurrCritPhase3": inletCfgCurrCritPhase3,
       "inletCfgCurrWarnPhase1": inletCfgCurrWarnPhase1,
       "inletCfgCurrWarnPhase2": inletCfgCurrWarnPhase2,
       "inletCfgCurrWarnPhase3": inletCfgCurrWarnPhase3,
       "inletCfgVoltCritPhase1": inletCfgVoltCritPhase1,
       "inletCfgVoltCritPhase2": inletCfgVoltCritPhase2,
       "inletCfgVoltCritPhase3": inletCfgVoltCritPhase3,
       "inletCfgVoltWarnPhase1": inletCfgVoltWarnPhase1,
       "inletCfgVoltWarnPhase2": inletCfgVoltWarnPhase2,
       "inletCfgVoltWarnPhase3": inletCfgVoltWarnPhase3,
       "pduPwrMonitoringOutlet": pduPwrMonitoringOutlet,
       "pduPwrMonitoringOutletPduA": pduPwrMonitoringOutletPduA,
       "pduPwrMonitoringOutletNumPduA": pduPwrMonitoringOutletNumPduA,
       "pduPwrMonitoringOutletStatusTablePduA": pduPwrMonitoringOutletStatusTablePduA,
       "pduPwrMonitoringOutletStatusPduAEntry": pduPwrMonitoringOutletStatusPduAEntry,
       "outletPduAIndex": outletPduAIndex,
       "outletPduAState": outletPduAState,
       "outletPduACurrent": outletPduACurrent,
       "outletPduAPwrFactor": outletPduAPwrFactor,
       "outletPduAPower": outletPduAPower,
       "outletPduAEnergy": outletPduAEnergy,
       "outletPduAResetFrom": outletPduAResetFrom,
       "outletPduAStatus": outletPduAStatus,
       "pduPwrMonitoringOutletCfgTablePduA": pduPwrMonitoringOutletCfgTablePduA,
       "pduPwrMonitoringOutletCfgPduAEntry": pduPwrMonitoringOutletCfgPduAEntry,
       "outletCfgPduAIndex": outletCfgPduAIndex,
       "outletCfgPduAName": outletCfgPduAName,
       "outletCfgPduADelayOnStatus": outletCfgPduADelayOnStatus,
       "outletCfgPduADelayOnTime": outletCfgPduADelayOnTime,
       "outletCfgPduADelayOffStatus": outletCfgPduADelayOffStatus,
       "outletCfgPduADelayOffTime": outletCfgPduADelayOffTime,
       "outletCfgPduAReboot": outletCfgPduAReboot,
       "outletCfgPduAOverCurrCritical": outletCfgPduAOverCurrCritical,
       "outletCfgPduAOverCurrWarning": outletCfgPduAOverCurrWarning,
       "outletCfgPduAOverPwrCritical": outletCfgPduAOverPwrCritical,
       "outletCfgPduAOverPwrWarning": outletCfgPduAOverPwrWarning,
       "pduPwrMonitoringOutletCtlTablePduA": pduPwrMonitoringOutletCtlTablePduA,
       "pduPwrMonitoringOutletCtlPduAEntry": pduPwrMonitoringOutletCtlPduAEntry,
       "outletCtlPduAIndex": outletCtlPduAIndex,
       "outletCtlPduAControl": outletCtlPduAControl,
       "pduPwrMonitoringOutletPduB": pduPwrMonitoringOutletPduB,
       "pduPwrMonitoringOutletNumPduB": pduPwrMonitoringOutletNumPduB,
       "pduPwrMonitoringOutletStatusTablePduB": pduPwrMonitoringOutletStatusTablePduB,
       "pduPwrMonitoringOutletStatusPduBEntry": pduPwrMonitoringOutletStatusPduBEntry,
       "outletPduBIndex": outletPduBIndex,
       "outletPduBState": outletPduBState,
       "outletPduBCurrent": outletPduBCurrent,
       "outletPduBPwrFactor": outletPduBPwrFactor,
       "outletPduBPower": outletPduBPower,
       "outletPduBEnergy": outletPduBEnergy,
       "outletPduBResetFrom": outletPduBResetFrom,
       "outletPduBStatus": outletPduBStatus,
       "pduPwrMonitoringOutletCfgTablePduB": pduPwrMonitoringOutletCfgTablePduB,
       "pduPwrMonitoringOutletCfgPduBEntry": pduPwrMonitoringOutletCfgPduBEntry,
       "outletCfgPduBIndex": outletCfgPduBIndex,
       "outletCfgPduBName": outletCfgPduBName,
       "outletCfgPduBDelayOnStatus": outletCfgPduBDelayOnStatus,
       "outletCfgPduBDelayOnTime": outletCfgPduBDelayOnTime,
       "outletCfgPduBDelayOffStatus": outletCfgPduBDelayOffStatus,
       "outletCfgPduBDelayOffTime": outletCfgPduBDelayOffTime,
       "outletCfgPduBReboot": outletCfgPduBReboot,
       "outletCfgPduBOverCurrCritical": outletCfgPduBOverCurrCritical,
       "outletCfgPduBOverCurrWarning": outletCfgPduBOverCurrWarning,
       "outletCfgPduBOverPwrCritical": outletCfgPduBOverPwrCritical,
       "outletCfgPduBOverPwrWarning": outletCfgPduBOverPwrWarning,
       "pduPwrMonitoringOutletCtlTablePduB": pduPwrMonitoringOutletCtlTablePduB,
       "pduPwrMonitoringOutletCtlPduBEntry": pduPwrMonitoringOutletCtlPduBEntry,
       "outletCtlPduBIndex": outletCtlPduBIndex,
       "outletCtlPduBControl": outletCtlPduBControl,
       "pduPwrMonitoringOutletPduC": pduPwrMonitoringOutletPduC,
       "pduPwrMonitoringOutletNumPduC": pduPwrMonitoringOutletNumPduC,
       "pduPwrMonitoringOutletStatusTablePduC": pduPwrMonitoringOutletStatusTablePduC,
       "pduPwrMonitoringOutletStatusPduCEntry": pduPwrMonitoringOutletStatusPduCEntry,
       "outletPduCIndex": outletPduCIndex,
       "outletPduCState": outletPduCState,
       "outletPduCCurrent": outletPduCCurrent,
       "outletPduCPwrFactor": outletPduCPwrFactor,
       "outletPduCPower": outletPduCPower,
       "outletPduCEnergy": outletPduCEnergy,
       "outletPduCResetFrom": outletPduCResetFrom,
       "outletPduCStatus": outletPduCStatus,
       "pduPwrMonitoringOutletCfgTablePduC": pduPwrMonitoringOutletCfgTablePduC,
       "pduPwrMonitoringOutletCfgPduCEntry": pduPwrMonitoringOutletCfgPduCEntry,
       "outletCfgPduCIndex": outletCfgPduCIndex,
       "outletCfgPduCName": outletCfgPduCName,
       "outletCfgPduCDelayOnStatus": outletCfgPduCDelayOnStatus,
       "outletCfgPduCDelayOnTime": outletCfgPduCDelayOnTime,
       "outletCfgPduCDelayOffStatus": outletCfgPduCDelayOffStatus,
       "outletCfgPduCDelayOffTime": outletCfgPduCDelayOffTime,
       "outletCfgPduCReboot": outletCfgPduCReboot,
       "outletCfgPduCOverCurrCritical": outletCfgPduCOverCurrCritical,
       "outletCfgPduCOverCurrWarning": outletCfgPduCOverCurrWarning,
       "outletCfgPduCOverPwrCritical": outletCfgPduCOverPwrCritical,
       "outletCfgPduCOverPwrWarning": outletCfgPduCOverPwrWarning,
       "pduPwrMonitoringOutletCtlTablePduC": pduPwrMonitoringOutletCtlTablePduC,
       "pduPwrMonitoringOutletCtlPduCEntry": pduPwrMonitoringOutletCtlPduCEntry,
       "outletCtlPduCIndex": outletCtlPduCIndex,
       "outletCtlPduCControl": outletCtlPduCControl,
       "pduPwrMonitoringOutletPduD": pduPwrMonitoringOutletPduD,
       "pduPwrMonitoringOutletNumPduD": pduPwrMonitoringOutletNumPduD,
       "pduPwrMonitoringOutletStatusTablePduD": pduPwrMonitoringOutletStatusTablePduD,
       "pduPwrMonitoringOutletStatusPduDEntry": pduPwrMonitoringOutletStatusPduDEntry,
       "outletPduDIndex": outletPduDIndex,
       "outletPduDState": outletPduDState,
       "outletPduDCurrent": outletPduDCurrent,
       "outletPduDPwrFactor": outletPduDPwrFactor,
       "outletPduDPower": outletPduDPower,
       "outletPduDEnergy": outletPduDEnergy,
       "outletPduDResetFrom": outletPduDResetFrom,
       "outletPduDStatus": outletPduDStatus,
       "pduPwrMonitoringOutletCfgTablePduD": pduPwrMonitoringOutletCfgTablePduD,
       "pduPwrMonitoringOutletCfgPduDEntry": pduPwrMonitoringOutletCfgPduDEntry,
       "outletCfgPduDIndex": outletCfgPduDIndex,
       "outletCfgPduDName": outletCfgPduDName,
       "outletCfgPduDDelayOnStatus": outletCfgPduDDelayOnStatus,
       "outletCfgPduDDelayOnTime": outletCfgPduDDelayOnTime,
       "outletCfgPduDDelayOffStatus": outletCfgPduDDelayOffStatus,
       "outletCfgPduDDelayOffTime": outletCfgPduDDelayOffTime,
       "outletCfgPduDReboot": outletCfgPduDReboot,
       "outletCfgPduDOverCurrCritical": outletCfgPduDOverCurrCritical,
       "outletCfgPduDOverCurrWarning": outletCfgPduDOverCurrWarning,
       "outletCfgPduDOverPwrCritical": outletCfgPduDOverPwrCritical,
       "outletCfgPduDOverPwrWarning": outletCfgPduDOverPwrWarning,
       "pduPwrMonitoringOutletCtlTablePduD": pduPwrMonitoringOutletCtlTablePduD,
       "pduPwrMonitoringOutletCtlPduDEntry": pduPwrMonitoringOutletCtlPduDEntry,
       "outletCtlPduDIndex": outletCtlPduDIndex,
       "outletCtlPduDControl": outletCtlPduDControl,
       "pduEnvMonitoring": pduEnvMonitoring,
       "pduEnvMonitoringStatus": pduEnvMonitoringStatus,
       "pduEnvMonitoringTemp": pduEnvMonitoringTemp,
       "pduEnvMonitoringHumi": pduEnvMonitoringHumi,
       "pduEnvMonitoringTempAlarm": pduEnvMonitoringTempAlarm,
       "pduEnvMonitoringHumiAlarm": pduEnvMonitoringHumiAlarm,
       "pduEnvMonitoringCfg": pduEnvMonitoringCfg,
       "pduEnvMonitoringControl": pduEnvMonitoringControl,
       "pduEnvMonitoringTempHighCritical": pduEnvMonitoringTempHighCritical,
       "pduEnvMonitoringTempHighWarning": pduEnvMonitoringTempHighWarning,
       "pduEnvMonitoringTempLowCritical": pduEnvMonitoringTempLowCritical,
       "pduEnvMonitoringTempLowWarning": pduEnvMonitoringTempLowWarning,
       "pduEnvMonitoringTempHystersis": pduEnvMonitoringTempHystersis,
       "pduEnvMonitoringTempOffset": pduEnvMonitoringTempOffset,
       "pduEnvMonitoringHumiHighCritical": pduEnvMonitoringHumiHighCritical,
       "pduEnvMonitoringHumiHighWarning": pduEnvMonitoringHumiHighWarning,
       "pduEnvMonitoringHumiLowCritical": pduEnvMonitoringHumiLowCritical,
       "pduEnvMonitoringHumiLowWarning": pduEnvMonitoringHumiLowWarning,
       "pduEnvMonitoringHumiHystersis": pduEnvMonitoringHumiHystersis,
       "pduEnvMonitoringHumiOffset": pduEnvMonitoringHumiOffset,
       "pduTraps": pduTraps,
       "pduSystemColdBoot": pduSystemColdBoot,
       "pduSystemWarmBoot": pduSystemWarmBoot,
       "pduSystemRestart": pduSystemRestart,
       "pduResetToDefault": pduResetToDefault,
       "pduFirmUpgrade": pduFirmUpgrade,
       "pduSystemLogClear": pduSystemLogClear,
       "pduEventlogClear": pduEventlogClear,
       "pduInletHistoryClear": pduInletHistoryClear,
       "pduOutletHistoryClear": pduOutletHistoryClear,
       "pduSystemTimeChangeUser": pduSystemTimeChangeUser,
       "pduSystemTimeChangeNtp": pduSystemTimeChangeNtp,
       "pduSystemTimeChangeRtc": pduSystemTimeChangeRtc,
       "pduMailTestPass": pduMailTestPass,
       "pduMailTestFail": pduMailTestFail,
       "pduMailSentPass": pduMailSentPass,
       "pduMailSentFail": pduMailSentFail,
       "pduSystemCfgChange": pduSystemCfgChange,
       "pduSystemParamImport": pduSystemParamImport,
       "pduInletCommLost": pduInletCommLost,
       "pduInletCommRestore": pduInletCommRestore,
       "pduOutletCommLost": pduOutletCommLost,
       "pduOutletCommRestore": pduOutletCommRestore,
       "pduOutletOnUser": pduOutletOnUser,
       "pduOutletOnSchedule": pduOutletOnSchedule,
       "pduOutletOffUser": pduOutletOffUser,
       "pduOutletOffSchedule": pduOutletOffSchedule,
       "pduOutletRebootUser": pduOutletRebootUser,
       "pduOutletRebootSchedule": pduOutletRebootSchedule,
       "pduInletEnergyReset": pduInletEnergyReset,
       "pduOutletEnergyReset": pduOutletEnergyReset,
       "pduSetUser": pduSetUser,
       "pduDeletUser": pduDeletUser,
       "pduUpgradeInletSuccess": pduUpgradeInletSuccess,
       "pduUpgradeInletFail": pduUpgradeInletFail,
       "pduUpgradeOutletSuccess": pduUpgradeOutletSuccess,
       "pduUpgradeOutletFail": pduUpgradeOutletFail,
       "pduEmdTempHighWarnToNormal": pduEmdTempHighWarnToNormal,
       "pduEmdTempHighWarn": pduEmdTempHighWarn,
       "pduEmdTempLowWarnToNormal": pduEmdTempLowWarnToNormal,
       "pduEmdTempLowWarn": pduEmdTempLowWarn,
       "pduEmdTempHighCritToWarn": pduEmdTempHighCritToWarn,
       "pduEmdTempHighCritical": pduEmdTempHighCritical,
       "pduEmdTempLowCritToWarn": pduEmdTempLowCritToWarn,
       "pduEmdTempLowCritical": pduEmdTempLowCritical,
       "pduEmdHumiHighWarnToNormal": pduEmdHumiHighWarnToNormal,
       "pduEmdHumiHighWarn": pduEmdHumiHighWarn,
       "pduEmdHumiLowWarnToNormal": pduEmdHumiLowWarnToNormal,
       "pduEmdHumiLowWarn": pduEmdHumiLowWarn,
       "pduEmdHumiHighCritToWarn": pduEmdHumiHighCritToWarn,
       "pduEmdHumiHighCritical": pduEmdHumiHighCritical,
       "pduEmdHumiLowCritToWarn": pduEmdHumiLowCritToWarn,
       "pduEmdHumiLowCritical": pduEmdHumiLowCritical,
       "pduEmdAlarm1NotActive": pduEmdAlarm1NotActive,
       "pduEmdAlarm1Active": pduEmdAlarm1Active,
       "pduEmdAlarm2NotActive": pduEmdAlarm2NotActive,
       "pduEmdAlarm2Active": pduEmdAlarm2Active,
       "pduRs485Online": pduRs485Online,
       "pduRs485Offline": pduRs485Offline,
       "pduInletLoadCritToWarn": pduInletLoadCritToWarn,
       "pduInletLoadCritical": pduInletLoadCritical,
       "pduInletLoadWarnToNormal": pduInletLoadWarnToNormal,
       "pduInletLoadWarn": pduInletLoadWarn,
       "pduInletCurrPhase1CritToWarn": pduInletCurrPhase1CritToWarn,
       "pduInletCurrPhase1Critical": pduInletCurrPhase1Critical,
       "pduInletCurrPhase1WarnToNormal": pduInletCurrPhase1WarnToNormal,
       "pduInletCurrPhase1Warn": pduInletCurrPhase1Warn,
       "pduInletCurrPhase2CritToWarn": pduInletCurrPhase2CritToWarn,
       "pduInletCurrPhase2Critical": pduInletCurrPhase2Critical,
       "pduInletCurrPhase2WarnToNormal": pduInletCurrPhase2WarnToNormal,
       "pduInletCurrPhase2Warn": pduInletCurrPhase2Warn,
       "pduInletCurrPhase3CritToWarn": pduInletCurrPhase3CritToWarn,
       "pduInletCurrPhase3Critical": pduInletCurrPhase3Critical,
       "pduInletCurrPhase3WarnToNormal": pduInletCurrPhase3WarnToNormal,
       "pduInletCurrPhase3Warn": pduInletCurrPhase3Warn,
       "pduInletVoltPhase1CritToWarn": pduInletVoltPhase1CritToWarn,
       "pduInletVoltPhase1Critical": pduInletVoltPhase1Critical,
       "pduInletVoltPhase1WarnToNormal": pduInletVoltPhase1WarnToNormal,
       "pduInletVoltPhase1Warn": pduInletVoltPhase1Warn,
       "pduInletVoltPhase2CritToWarn": pduInletVoltPhase2CritToWarn,
       "pduInletVoltPhase2Critical": pduInletVoltPhase2Critical,
       "pduInletVoltPhase2WarnToNormal": pduInletVoltPhase2WarnToNormal,
       "pduInletVoltPhase2Warn": pduInletVoltPhase2Warn,
       "pduInletVoltPhase3CritToWarn": pduInletVoltPhase3CritToWarn,
       "pduInletVoltPhase3Critical": pduInletVoltPhase3Critical,
       "pduInletVoltPhase3WarnToNormal": pduInletVoltPhase3WarnToNormal,
       "pduInletVoltPhase3Warn": pduInletVoltPhase3Warn,
       "pduOutletCurrCritToWarn": pduOutletCurrCritToWarn,
       "pduOutletCurrCritical": pduOutletCurrCritical,
       "pduOutletCurrWarnToNormal": pduOutletCurrWarnToNormal,
       "pduOutletCurrWarn": pduOutletCurrWarn,
       "pduOutletPwrCritTOWarn": pduOutletPwrCritTOWarn,
       "pduOutletPwrCritical": pduOutletPwrCritical,
       "pduOutletPwrWarnToNormal": pduOutletPwrWarnToNormal,
       "pduOutletPwrWarn": pduOutletPwrWarn,
       "pduAlarm1Disabled": pduAlarm1Disabled,
       "pduAlarm2Disabled": pduAlarm2Disabled}
)
