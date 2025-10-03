# SNMP MIB module (ALCATEL-IND1-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-AAA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:06 2025
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

(alaAaaTraps,
 softentIND1AAA) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "alaAaaTraps",
    "softentIND1AAA")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1AAAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1AAAMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBObjects = _AlcatelIND1AAAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBObjects.setStatus("current")
_AaaServerMIB_ObjectIdentity = ObjectIdentity
aaaServerMIB = _AaaServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1)
)
_AaaServerTable_Object = MibTable
aaaServerTable = _AaaServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aaaServerTable.setStatus("current")
_AaaServerEntry_Object = MibTableRow
aaaServerEntry = _AaaServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1)
)
aaaServerEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaasName"),
)
if mibBuilder.loadTexts:
    aaaServerEntry.setStatus("current")


class _AaasName_Type(DisplayString):
    """Custom type aaasName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaasName_Type.__name__ = "DisplayString"
_AaasName_Object = MibTableColumn
aaasName = _AaasName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 1),
    _AaasName_Type()
)
aaasName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasName.setStatus("current")


class _AaasProtocol_Type(Integer32):
    """Custom type aaasProtocol based on Integer32"""
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
        *(("radius", 1),
          ("ldap", 2),
          ("ace", 3),
          ("tacacs", 4))
    )


_AaasProtocol_Type.__name__ = "Integer32"
_AaasProtocol_Object = MibTableColumn
aaasProtocol = _AaasProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 2),
    _AaasProtocol_Type()
)
aaasProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasProtocol.setStatus("current")


class _AaasHostName_Type(DisplayString):
    """Custom type aaasHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasHostName_Type.__name__ = "DisplayString"
_AaasHostName_Object = MibTableColumn
aaasHostName = _AaasHostName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 3),
    _AaasHostName_Type()
)
aaasHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHostName.setStatus("current")
_AaasIpAddress_Type = IpAddress
_AaasIpAddress_Object = MibTableColumn
aaasIpAddress = _AaasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 4),
    _AaasIpAddress_Type()
)
aaasIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasIpAddress.setStatus("current")


class _AaasHostName2_Type(DisplayString):
    """Custom type aaasHostName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasHostName2_Type.__name__ = "DisplayString"
_AaasHostName2_Object = MibTableColumn
aaasHostName2 = _AaasHostName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 5),
    _AaasHostName2_Type()
)
aaasHostName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHostName2.setStatus("current")
_AaasIpAddress2_Type = IpAddress
_AaasIpAddress2_Object = MibTableColumn
aaasIpAddress2 = _AaasIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 6),
    _AaasIpAddress2_Type()
)
aaasIpAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasIpAddress2.setStatus("current")


class _AaasRetries_Type(Integer32):
    """Custom type aaasRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AaasRetries_Type.__name__ = "Integer32"
_AaasRetries_Object = MibTableColumn
aaasRetries = _AaasRetries_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 7),
    _AaasRetries_Type()
)
aaasRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRetries.setStatus("current")


class _AaasTimout_Type(Integer32):
    """Custom type aaasTimout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_AaasTimout_Type.__name__ = "Integer32"
_AaasTimout_Object = MibTableColumn
aaasTimout = _AaasTimout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 8),
    _AaasTimout_Type()
)
aaasTimout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTimout.setStatus("current")


class _AaasRadKey_Type(DisplayString):
    """Custom type aaasRadKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasRadKey_Type.__name__ = "DisplayString"
_AaasRadKey_Object = MibTableColumn
aaasRadKey = _AaasRadKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 9),
    _AaasRadKey_Type()
)
aaasRadKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadKey.setStatus("current")


class _AaasRadAuthPort_Type(Integer32):
    """Custom type aaasRadAuthPort based on Integer32"""
    defaultValue = 1645

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasRadAuthPort_Type.__name__ = "Integer32"
_AaasRadAuthPort_Object = MibTableColumn
aaasRadAuthPort = _AaasRadAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 10),
    _AaasRadAuthPort_Type()
)
aaasRadAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadAuthPort.setStatus("current")


class _AaasRadAcctPort_Type(Integer32):
    """Custom type aaasRadAcctPort based on Integer32"""
    defaultValue = 1646

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasRadAcctPort_Type.__name__ = "Integer32"
_AaasRadAcctPort_Object = MibTableColumn
aaasRadAcctPort = _AaasRadAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 11),
    _AaasRadAcctPort_Type()
)
aaasRadAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadAcctPort.setStatus("current")


class _AaasLdapPort_Type(Integer32):
    """Custom type aaasLdapPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasLdapPort_Type.__name__ = "Integer32"
_AaasLdapPort_Object = MibTableColumn
aaasLdapPort = _AaasLdapPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 12),
    _AaasLdapPort_Type()
)
aaasLdapPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapPort.setStatus("current")


class _AaasLdapDn_Type(DisplayString):
    """Custom type aaasLdapDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AaasLdapDn_Type.__name__ = "DisplayString"
_AaasLdapDn_Object = MibTableColumn
aaasLdapDn = _AaasLdapDn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 13),
    _AaasLdapDn_Type()
)
aaasLdapDn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapDn.setStatus("current")


class _AaasLdapPasswd_Type(DisplayString):
    """Custom type aaasLdapPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaasLdapPasswd_Type.__name__ = "DisplayString"
_AaasLdapPasswd_Object = MibTableColumn
aaasLdapPasswd = _AaasLdapPasswd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 14),
    _AaasLdapPasswd_Type()
)
aaasLdapPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapPasswd.setStatus("current")


class _AaasLdapSearchBase_Type(DisplayString):
    """Custom type aaasLdapSearchBase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasLdapSearchBase_Type.__name__ = "DisplayString"
_AaasLdapSearchBase_Object = MibTableColumn
aaasLdapSearchBase = _AaasLdapSearchBase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 15),
    _AaasLdapSearchBase_Type()
)
aaasLdapSearchBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapSearchBase.setStatus("current")


class _AaasLdapServType_Type(Integer32):
    """Custom type aaasLdapServType based on Integer32"""
    defaultValue = 2

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
        *(("ns", 0),
          ("generic", 1),
          ("netscape", 2),
          ("novell", 3),
          ("sun", 4),
          ("microsoft", 5))
    )


_AaasLdapServType_Type.__name__ = "Integer32"
_AaasLdapServType_Object = MibTableColumn
aaasLdapServType = _AaasLdapServType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 16),
    _AaasLdapServType_Type()
)
aaasLdapServType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapServType.setStatus("current")


class _AaasLdapEnableSsl_Type(Integer32):
    """Custom type aaasLdapEnableSsl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ns", 0),
          ("true", 1),
          ("false", 2))
    )


_AaasLdapEnableSsl_Type.__name__ = "Integer32"
_AaasLdapEnableSsl_Object = MibTableColumn
aaasLdapEnableSsl = _AaasLdapEnableSsl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 17),
    _AaasLdapEnableSsl_Type()
)
aaasLdapEnableSsl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapEnableSsl.setStatus("current")


class _AaasAceClear_Type(Integer32):
    """Custom type aaasAceClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ns", 0),
          ("true", 1),
          ("false", 2))
    )


_AaasAceClear_Type.__name__ = "Integer32"
_AaasAceClear_Object = MibTableColumn
aaasAceClear = _AaasAceClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 18),
    _AaasAceClear_Type()
)
aaasAceClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasAceClear.setStatus("current")


class _AaasRowStatus_Type(RowStatus):
    """Custom type aaasRowStatus based on RowStatus"""
    defaultValue = 2


_AaasRowStatus_Type.__name__ = "RowStatus"
_AaasRowStatus_Object = MibTableColumn
aaasRowStatus = _AaasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 19),
    _AaasRowStatus_Type()
)
aaasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRowStatus.setStatus("current")


class _AaasTacacsKey_Type(DisplayString):
    """Custom type aaasTacacsKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasTacacsKey_Type.__name__ = "DisplayString"
_AaasTacacsKey_Object = MibTableColumn
aaasTacacsKey = _AaasTacacsKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 20),
    _AaasTacacsKey_Type()
)
aaasTacacsKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTacacsKey.setStatus("current")


class _AaasTacacsPort_Type(Integer32):
    """Custom type aaasTacacsPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasTacacsPort_Type.__name__ = "Integer32"
_AaasTacacsPort_Object = MibTableColumn
aaasTacacsPort = _AaasTacacsPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 21),
    _AaasTacacsPort_Type()
)
aaasTacacsPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTacacsPort.setStatus("current")


class _AaasHttpPort_Type(Integer32):
    """Custom type aaasHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasHttpPort_Type.__name__ = "Integer32"
_AaasHttpPort_Object = MibTableColumn
aaasHttpPort = _AaasHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 22),
    _AaasHttpPort_Type()
)
aaasHttpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHttpPort.setStatus("current")


class _AaasHttpDirectory_Type(DisplayString):
    """Custom type aaasHttpDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasHttpDirectory_Type.__name__ = "DisplayString"
_AaasHttpDirectory_Object = MibTableColumn
aaasHttpDirectory = _AaasHttpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 23),
    _AaasHttpDirectory_Type()
)
aaasHttpDirectory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHttpDirectory.setStatus("current")


class _AaasHttpProxyHostName_Type(DisplayString):
    """Custom type aaasHttpProxyHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasHttpProxyHostName_Type.__name__ = "DisplayString"
_AaasHttpProxyHostName_Object = MibTableColumn
aaasHttpProxyHostName = _AaasHttpProxyHostName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 24),
    _AaasHttpProxyHostName_Type()
)
aaasHttpProxyHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHttpProxyHostName.setStatus("current")
_AaasHttpProxyIpAddress_Type = IpAddress
_AaasHttpProxyIpAddress_Object = MibTableColumn
aaasHttpProxyIpAddress = _AaasHttpProxyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 25),
    _AaasHttpProxyIpAddress_Type()
)
aaasHttpProxyIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHttpProxyIpAddress.setStatus("current")


class _AaasHttpProxyPort_Type(Integer32):
    """Custom type aaasHttpProxyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasHttpProxyPort_Type.__name__ = "Integer32"
_AaasHttpProxyPort_Object = MibTableColumn
aaasHttpProxyPort = _AaasHttpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 26),
    _AaasHttpProxyPort_Type()
)
aaasHttpProxyPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHttpProxyPort.setStatus("current")


class _AaasVrfName_Type(DisplayString):
    """Custom type aaasVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaasVrfName_Type.__name__ = "DisplayString"
_AaasVrfName_Object = MibTableColumn
aaasVrfName = _AaasVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 27),
    _AaasVrfName_Type()
)
aaasVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasVrfName.setStatus("current")
_AaaAuthAcctMIB_ObjectIdentity = ObjectIdentity
aaaAuthAcctMIB = _AaaAuthAcctMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2)
)
_AaaAuthVlanTable_Object = MibTable
aaaAuthVlanTable = _AaaAuthVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aaaAuthVlanTable.setStatus("current")
_AaaAuthVlanEntry_Object = MibTableRow
aaaAuthVlanEntry = _AaaAuthVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1)
)
aaaAuthVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaatvVlan"),
)
if mibBuilder.loadTexts:
    aaaAuthVlanEntry.setStatus("current")


class _AaatvVlan_Type(Integer32):
    """Custom type aaatvVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaatvVlan_Type.__name__ = "Integer32"
_AaatvVlan_Object = MibTableColumn
aaatvVlan = _AaatvVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1, 1),
    _AaatvVlan_Type()
)
aaatvVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatvVlan.setStatus("current")


class _AaatvName1_Type(DisplayString):
    """Custom type aaatvName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatvName1_Type.__name__ = "DisplayString"
_AaatvName1_Object = MibTableColumn
aaatvName1 = _AaatvName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1, 2),
    _AaatvName1_Type()
)
aaatvName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatvName1.setStatus("current")


class _AaatvName2_Type(DisplayString):
    """Custom type aaatvName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatvName2_Type.__name__ = "DisplayString"
_AaatvName2_Object = MibTableColumn
aaatvName2 = _AaatvName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1, 3),
    _AaatvName2_Type()
)
aaatvName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatvName2.setStatus("current")


class _AaatvName3_Type(DisplayString):
    """Custom type aaatvName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatvName3_Type.__name__ = "DisplayString"
_AaatvName3_Object = MibTableColumn
aaatvName3 = _AaatvName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1, 4),
    _AaatvName3_Type()
)
aaatvName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatvName3.setStatus("current")


class _AaatvName4_Type(DisplayString):
    """Custom type aaatvName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatvName4_Type.__name__ = "DisplayString"
_AaatvName4_Object = MibTableColumn
aaatvName4 = _AaatvName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1, 5),
    _AaatvName4_Type()
)
aaatvName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatvName4.setStatus("current")


class _AaatvRowStatus_Type(RowStatus):
    """Custom type aaatvRowStatus based on RowStatus"""
    defaultValue = 2


_AaatvRowStatus_Type.__name__ = "RowStatus"
_AaatvRowStatus_Object = MibTableColumn
aaatvRowStatus = _AaatvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1, 6),
    _AaatvRowStatus_Type()
)
aaatvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatvRowStatus.setStatus("current")


class _AaatvCertificate_Type(Integer32):
    """Custom type aaatvCertificate based on Integer32"""
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
        *(("noCertificate", 0),
          ("certificateOnly", 1),
          ("certificateWithPassword", 2))
    )


_AaatvCertificate_Type.__name__ = "Integer32"
_AaatvCertificate_Object = MibTableColumn
aaatvCertificate = _AaatvCertificate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1, 7),
    _AaatvCertificate_Type()
)
aaatvCertificate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatvCertificate.setStatus("current")
_AaaAuthSATable_Object = MibTable
aaaAuthSATable = _AaaAuthSATable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    aaaAuthSATable.setStatus("current")
_AaaAuthSAEntry_Object = MibTableRow
aaaAuthSAEntry = _AaaAuthSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1)
)
aaaAuthSAEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaatsInterface"),
)
if mibBuilder.loadTexts:
    aaaAuthSAEntry.setStatus("current")


class _AaatsInterface_Type(Integer32):
    """Custom type aaatsInterface based on Integer32"""
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
        *(("default", 1),
          ("console", 2),
          ("telnet", 3),
          ("ftp", 4),
          ("http", 5),
          ("snmp", 6),
          ("ssh", 7))
    )


_AaatsInterface_Type.__name__ = "Integer32"
_AaatsInterface_Object = MibTableColumn
aaatsInterface = _AaatsInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 1),
    _AaatsInterface_Type()
)
aaatsInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsInterface.setStatus("current")


class _AaatsName1_Type(DisplayString):
    """Custom type aaatsName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName1_Type.__name__ = "DisplayString"
_AaatsName1_Object = MibTableColumn
aaatsName1 = _AaatsName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 2),
    _AaatsName1_Type()
)
aaatsName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName1.setStatus("current")


class _AaatsName2_Type(DisplayString):
    """Custom type aaatsName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName2_Type.__name__ = "DisplayString"
_AaatsName2_Object = MibTableColumn
aaatsName2 = _AaatsName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 3),
    _AaatsName2_Type()
)
aaatsName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName2.setStatus("current")


class _AaatsName3_Type(DisplayString):
    """Custom type aaatsName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName3_Type.__name__ = "DisplayString"
_AaatsName3_Object = MibTableColumn
aaatsName3 = _AaatsName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 4),
    _AaatsName3_Type()
)
aaatsName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName3.setStatus("current")


class _AaatsName4_Type(DisplayString):
    """Custom type aaatsName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName4_Type.__name__ = "DisplayString"
_AaatsName4_Object = MibTableColumn
aaatsName4 = _AaatsName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 5),
    _AaatsName4_Type()
)
aaatsName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName4.setStatus("current")


class _AaatsRowStatus_Type(RowStatus):
    """Custom type aaatsRowStatus based on RowStatus"""
    defaultValue = 2


_AaatsRowStatus_Type.__name__ = "RowStatus"
_AaatsRowStatus_Object = MibTableColumn
aaatsRowStatus = _AaatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 7),
    _AaatsRowStatus_Type()
)
aaatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsRowStatus.setStatus("current")


class _AaatsCertificate_Type(Integer32):
    """Custom type aaatsCertificate based on Integer32"""
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
        *(("noCertificate", 0),
          ("certificateOnly", 1),
          ("certificateWithPassword", 2))
    )


_AaatsCertificate_Type.__name__ = "Integer32"
_AaatsCertificate_Object = MibTableColumn
aaatsCertificate = _AaatsCertificate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 8),
    _AaatsCertificate_Type()
)
aaatsCertificate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsCertificate.setStatus("current")
_AaaAcctVlanTable_Object = MibTable
aaaAcctVlanTable = _AaaAcctVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    aaaAcctVlanTable.setStatus("current")
_AaaAcctVlanEntry_Object = MibTableRow
aaaAcctVlanEntry = _AaaAcctVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3, 1)
)
aaaAcctVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaacvVlan"),
)
if mibBuilder.loadTexts:
    aaaAcctVlanEntry.setStatus("current")


class _AaacvVlan_Type(Integer32):
    """Custom type aaacvVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaacvVlan_Type.__name__ = "Integer32"
_AaacvVlan_Object = MibTableColumn
aaacvVlan = _AaacvVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3, 1, 1),
    _AaacvVlan_Type()
)
aaacvVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacvVlan.setStatus("current")


class _AaacvName1_Type(DisplayString):
    """Custom type aaacvName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacvName1_Type.__name__ = "DisplayString"
_AaacvName1_Object = MibTableColumn
aaacvName1 = _AaacvName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3, 1, 2),
    _AaacvName1_Type()
)
aaacvName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacvName1.setStatus("current")


class _AaacvName2_Type(DisplayString):
    """Custom type aaacvName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacvName2_Type.__name__ = "DisplayString"
_AaacvName2_Object = MibTableColumn
aaacvName2 = _AaacvName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3, 1, 3),
    _AaacvName2_Type()
)
aaacvName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacvName2.setStatus("current")


class _AaacvName3_Type(DisplayString):
    """Custom type aaacvName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacvName3_Type.__name__ = "DisplayString"
_AaacvName3_Object = MibTableColumn
aaacvName3 = _AaacvName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3, 1, 4),
    _AaacvName3_Type()
)
aaacvName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacvName3.setStatus("current")


class _AaacvName4_Type(DisplayString):
    """Custom type aaacvName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacvName4_Type.__name__ = "DisplayString"
_AaacvName4_Object = MibTableColumn
aaacvName4 = _AaacvName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3, 1, 5),
    _AaacvName4_Type()
)
aaacvName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacvName4.setStatus("current")


class _AaacvRowStatus_Type(RowStatus):
    """Custom type aaacvRowStatus based on RowStatus"""
    defaultValue = 2


_AaacvRowStatus_Type.__name__ = "RowStatus"
_AaacvRowStatus_Object = MibTableColumn
aaacvRowStatus = _AaacvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3, 1, 6),
    _AaacvRowStatus_Type()
)
aaacvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacvRowStatus.setStatus("current")
_AaaAcctSATable_Object = MibTable
aaaAcctSATable = _AaaAcctSATable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    aaaAcctSATable.setStatus("current")
_AaaAcctSAEntry_Object = MibTableRow
aaaAcctSAEntry = _AaaAcctSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1)
)
aaaAcctSAEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaacsInterface"),
)
if mibBuilder.loadTexts:
    aaaAcctSAEntry.setStatus("current")


class _AaacsInterface_Type(Integer32):
    """Custom type aaacsInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaacsInterface_Type.__name__ = "Integer32"
_AaacsInterface_Object = MibTableColumn
aaacsInterface = _AaacsInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1, 1),
    _AaacsInterface_Type()
)
aaacsInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsInterface.setStatus("current")


class _AaacsName1_Type(DisplayString):
    """Custom type aaacsName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName1_Type.__name__ = "DisplayString"
_AaacsName1_Object = MibTableColumn
aaacsName1 = _AaacsName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1, 2),
    _AaacsName1_Type()
)
aaacsName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName1.setStatus("current")


class _AaacsName2_Type(DisplayString):
    """Custom type aaacsName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName2_Type.__name__ = "DisplayString"
_AaacsName2_Object = MibTableColumn
aaacsName2 = _AaacsName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1, 3),
    _AaacsName2_Type()
)
aaacsName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName2.setStatus("current")


class _AaacsName3_Type(DisplayString):
    """Custom type aaacsName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName3_Type.__name__ = "DisplayString"
_AaacsName3_Object = MibTableColumn
aaacsName3 = _AaacsName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1, 4),
    _AaacsName3_Type()
)
aaacsName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName3.setStatus("current")


class _AaacsName4_Type(DisplayString):
    """Custom type aaacsName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName4_Type.__name__ = "DisplayString"
_AaacsName4_Object = MibTableColumn
aaacsName4 = _AaacsName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1, 5),
    _AaacsName4_Type()
)
aaacsName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName4.setStatus("current")


class _AaacsRowStatus_Type(RowStatus):
    """Custom type aaacsRowStatus based on RowStatus"""
    defaultValue = 2


_AaacsRowStatus_Type.__name__ = "RowStatus"
_AaacsRowStatus_Object = MibTableColumn
aaacsRowStatus = _AaacsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1, 6),
    _AaacsRowStatus_Type()
)
aaacsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsRowStatus.setStatus("current")
_AaaAuth8021xTable_Object = MibTable
aaaAuth8021xTable = _AaaAuth8021xTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    aaaAuth8021xTable.setStatus("current")
_AaaAuth8021xEntry_Object = MibTableRow
aaaAuth8021xEntry = _AaaAuth8021xEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1)
)
aaaAuth8021xEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaatxInterface"),
)
if mibBuilder.loadTexts:
    aaaAuth8021xEntry.setStatus("current")


class _AaatxInterface_Type(Integer32):
    """Custom type aaatxInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaatxInterface_Type.__name__ = "Integer32"
_AaatxInterface_Object = MibTableColumn
aaatxInterface = _AaatxInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 1),
    _AaatxInterface_Type()
)
aaatxInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxInterface.setStatus("current")


class _AaatxName1_Type(DisplayString):
    """Custom type aaatxName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatxName1_Type.__name__ = "DisplayString"
_AaatxName1_Object = MibTableColumn
aaatxName1 = _AaatxName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 2),
    _AaatxName1_Type()
)
aaatxName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxName1.setStatus("current")


class _AaatxName2_Type(DisplayString):
    """Custom type aaatxName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatxName2_Type.__name__ = "DisplayString"
_AaatxName2_Object = MibTableColumn
aaatxName2 = _AaatxName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 3),
    _AaatxName2_Type()
)
aaatxName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxName2.setStatus("current")


class _AaatxName3_Type(DisplayString):
    """Custom type aaatxName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatxName3_Type.__name__ = "DisplayString"
_AaatxName3_Object = MibTableColumn
aaatxName3 = _AaatxName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 4),
    _AaatxName3_Type()
)
aaatxName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxName3.setStatus("current")


class _AaatxName4_Type(DisplayString):
    """Custom type aaatxName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatxName4_Type.__name__ = "DisplayString"
_AaatxName4_Object = MibTableColumn
aaatxName4 = _AaatxName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 5),
    _AaatxName4_Type()
)
aaatxName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxName4.setStatus("current")


class _AaatxOpen_Type(Integer32):
    """Custom type aaatxOpen based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("unique", 2))
    )


_AaatxOpen_Type.__name__ = "Integer32"
_AaatxOpen_Object = MibTableColumn
aaatxOpen = _AaatxOpen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 6),
    _AaatxOpen_Type()
)
aaatxOpen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxOpen.setStatus("current")


class _AaatxRowStatus_Type(RowStatus):
    """Custom type aaatxRowStatus based on RowStatus"""
    defaultValue = 2


_AaatxRowStatus_Type.__name__ = "RowStatus"
_AaatxRowStatus_Object = MibTableColumn
aaatxRowStatus = _AaatxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 7),
    _AaatxRowStatus_Type()
)
aaatxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxRowStatus.setStatus("current")
_AaaAcct8021xTable_Object = MibTable
aaaAcct8021xTable = _AaaAcct8021xTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    aaaAcct8021xTable.setStatus("current")
_AaaAcct8021xEntry_Object = MibTableRow
aaaAcct8021xEntry = _AaaAcct8021xEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1)
)
aaaAcct8021xEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaacxInterface"),
)
if mibBuilder.loadTexts:
    aaaAcct8021xEntry.setStatus("current")


class _AaacxInterface_Type(Integer32):
    """Custom type aaacxInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaacxInterface_Type.__name__ = "Integer32"
_AaacxInterface_Object = MibTableColumn
aaacxInterface = _AaacxInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1, 1),
    _AaacxInterface_Type()
)
aaacxInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacxInterface.setStatus("current")


class _AaacxName1_Type(DisplayString):
    """Custom type aaacxName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacxName1_Type.__name__ = "DisplayString"
_AaacxName1_Object = MibTableColumn
aaacxName1 = _AaacxName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1, 2),
    _AaacxName1_Type()
)
aaacxName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacxName1.setStatus("current")


class _AaacxName2_Type(DisplayString):
    """Custom type aaacxName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacxName2_Type.__name__ = "DisplayString"
_AaacxName2_Object = MibTableColumn
aaacxName2 = _AaacxName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1, 3),
    _AaacxName2_Type()
)
aaacxName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacxName2.setStatus("current")


class _AaacxName3_Type(DisplayString):
    """Custom type aaacxName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacxName3_Type.__name__ = "DisplayString"
_AaacxName3_Object = MibTableColumn
aaacxName3 = _AaacxName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1, 4),
    _AaacxName3_Type()
)
aaacxName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacxName3.setStatus("current")


class _AaacxName4_Type(DisplayString):
    """Custom type aaacxName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacxName4_Type.__name__ = "DisplayString"
_AaacxName4_Object = MibTableColumn
aaacxName4 = _AaacxName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1, 5),
    _AaacxName4_Type()
)
aaacxName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacxName4.setStatus("current")


class _AaacxRowStatus_Type(RowStatus):
    """Custom type aaacxRowStatus based on RowStatus"""
    defaultValue = 2


_AaacxRowStatus_Type.__name__ = "RowStatus"
_AaacxRowStatus_Object = MibTableColumn
aaacxRowStatus = _AaacxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1, 6),
    _AaacxRowStatus_Type()
)
aaacxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacxRowStatus.setStatus("current")
_AaaPkiTable_Object = MibTable
aaaPkiTable = _AaaPkiTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    aaaPkiTable.setStatus("current")
_AaaPkiEntry_Object = MibTableRow
aaaPkiEntry = _AaaPkiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1)
)
aaaPkiEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaatpInterface"),
)
if mibBuilder.loadTexts:
    aaaPkiEntry.setStatus("current")


class _AaatpInterface_Type(Integer32):
    """Custom type aaatpInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaatpInterface_Type.__name__ = "Integer32"
_AaatpInterface_Object = MibTableColumn
aaatpInterface = _AaatpInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1, 1),
    _AaatpInterface_Type()
)
aaatpInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatpInterface.setStatus("current")


class _AaatpName1_Type(DisplayString):
    """Custom type aaatpName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatpName1_Type.__name__ = "DisplayString"
_AaatpName1_Object = MibTableColumn
aaatpName1 = _AaatpName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1, 2),
    _AaatpName1_Type()
)
aaatpName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatpName1.setStatus("current")


class _AaatpName2_Type(DisplayString):
    """Custom type aaatpName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatpName2_Type.__name__ = "DisplayString"
_AaatpName2_Object = MibTableColumn
aaatpName2 = _AaatpName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1, 3),
    _AaatpName2_Type()
)
aaatpName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatpName2.setStatus("current")


class _AaatpName3_Type(DisplayString):
    """Custom type aaatpName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatpName3_Type.__name__ = "DisplayString"
_AaatpName3_Object = MibTableColumn
aaatpName3 = _AaatpName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1, 4),
    _AaatpName3_Type()
)
aaatpName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatpName3.setStatus("current")


class _AaatpName4_Type(DisplayString):
    """Custom type aaatpName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatpName4_Type.__name__ = "DisplayString"
_AaatpName4_Object = MibTableColumn
aaatpName4 = _AaatpName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1, 5),
    _AaatpName4_Type()
)
aaatpName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatpName4.setStatus("current")


class _AaatpLevel_Type(Integer32):
    """Custom type aaatpLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("certificate", 1),
          ("notRevoked", 2),
          ("repository", 3))
    )


_AaatpLevel_Type.__name__ = "Integer32"
_AaatpLevel_Object = MibTableColumn
aaatpLevel = _AaatpLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1, 6),
    _AaatpLevel_Type()
)
aaatpLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatpLevel.setStatus("current")


class _AaatpRowStatus_Type(RowStatus):
    """Custom type aaatpRowStatus based on RowStatus"""
    defaultValue = 2


_AaatpRowStatus_Type.__name__ = "RowStatus"
_AaatpRowStatus_Object = MibTableColumn
aaatpRowStatus = _AaatpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1, 7),
    _AaatpRowStatus_Type()
)
aaatpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatpRowStatus.setStatus("current")
_AaaAuthMACTable_Object = MibTable
aaaAuthMACTable = _AaaAuthMACTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    aaaAuthMACTable.setStatus("current")
_AaaAuthMACEntry_Object = MibTableRow
aaaAuthMACEntry = _AaaAuthMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1)
)
aaaAuthMACEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaatxInterface"),
)
if mibBuilder.loadTexts:
    aaaAuthMACEntry.setStatus("current")


class _AaaMacInterface_Type(Integer32):
    """Custom type aaaMacInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaaMacInterface_Type.__name__ = "Integer32"
_AaaMacInterface_Object = MibTableColumn
aaaMacInterface = _AaaMacInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1, 1),
    _AaaMacInterface_Type()
)
aaaMacInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMacInterface.setStatus("current")


class _AaaMacSrvrName1_Type(DisplayString):
    """Custom type aaaMacSrvrName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaMacSrvrName1_Type.__name__ = "DisplayString"
_AaaMacSrvrName1_Object = MibTableColumn
aaaMacSrvrName1 = _AaaMacSrvrName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1, 2),
    _AaaMacSrvrName1_Type()
)
aaaMacSrvrName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMacSrvrName1.setStatus("current")


class _AaaMacSrvrName2_Type(DisplayString):
    """Custom type aaaMacSrvrName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaMacSrvrName2_Type.__name__ = "DisplayString"
_AaaMacSrvrName2_Object = MibTableColumn
aaaMacSrvrName2 = _AaaMacSrvrName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1, 3),
    _AaaMacSrvrName2_Type()
)
aaaMacSrvrName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMacSrvrName2.setStatus("current")


class _AaaMacSrvrName3_Type(DisplayString):
    """Custom type aaaMacSrvrName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaMacSrvrName3_Type.__name__ = "DisplayString"
_AaaMacSrvrName3_Object = MibTableColumn
aaaMacSrvrName3 = _AaaMacSrvrName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1, 4),
    _AaaMacSrvrName3_Type()
)
aaaMacSrvrName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMacSrvrName3.setStatus("current")


class _AaaMacSrvrName4_Type(DisplayString):
    """Custom type aaaMacSrvrName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaMacSrvrName4_Type.__name__ = "DisplayString"
_AaaMacSrvrName4_Object = MibTableColumn
aaaMacSrvrName4 = _AaaMacSrvrName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1, 5),
    _AaaMacSrvrName4_Type()
)
aaaMacSrvrName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMacSrvrName4.setStatus("current")


class _AaaMacSrvrRowStatus_Type(RowStatus):
    """Custom type aaaMacSrvrRowStatus based on RowStatus"""
    defaultValue = 2


_AaaMacSrvrRowStatus_Type.__name__ = "RowStatus"
_AaaMacSrvrRowStatus_Object = MibTableColumn
aaaMacSrvrRowStatus = _AaaMacSrvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1, 6),
    _AaaMacSrvrRowStatus_Type()
)
aaaMacSrvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMacSrvrRowStatus.setStatus("current")
_AaaAcctCmdTable_Object = MibTable
aaaAcctCmdTable = _AaaAcctCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    aaaAcctCmdTable.setStatus("current")
_AaaAcctCmdEntry_Object = MibTableRow
aaaAcctCmdEntry = _AaaAcctCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1)
)
aaaAcctCmdEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaacmdInterface"),
)
if mibBuilder.loadTexts:
    aaaAcctCmdEntry.setStatus("current")


class _AaacmdInterface_Type(Integer32):
    """Custom type aaacmdInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaacmdInterface_Type.__name__ = "Integer32"
_AaacmdInterface_Object = MibTableColumn
aaacmdInterface = _AaacmdInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1, 1),
    _AaacmdInterface_Type()
)
aaacmdInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdInterface.setStatus("current")


class _AaacmdSrvName1_Type(DisplayString):
    """Custom type aaacmdSrvName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName1_Type.__name__ = "DisplayString"
_AaacmdSrvName1_Object = MibTableColumn
aaacmdSrvName1 = _AaacmdSrvName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1, 2),
    _AaacmdSrvName1_Type()
)
aaacmdSrvName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName1.setStatus("current")


class _AaacmdSrvName2_Type(DisplayString):
    """Custom type aaacmdSrvName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName2_Type.__name__ = "DisplayString"
_AaacmdSrvName2_Object = MibTableColumn
aaacmdSrvName2 = _AaacmdSrvName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1, 3),
    _AaacmdSrvName2_Type()
)
aaacmdSrvName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName2.setStatus("current")


class _AaacmdSrvName3_Type(DisplayString):
    """Custom type aaacmdSrvName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName3_Type.__name__ = "DisplayString"
_AaacmdSrvName3_Object = MibTableColumn
aaacmdSrvName3 = _AaacmdSrvName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1, 4),
    _AaacmdSrvName3_Type()
)
aaacmdSrvName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName3.setStatus("current")


class _AaacmdSrvName4_Type(DisplayString):
    """Custom type aaacmdSrvName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName4_Type.__name__ = "DisplayString"
_AaacmdSrvName4_Object = MibTableColumn
aaacmdSrvName4 = _AaacmdSrvName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1, 5),
    _AaacmdSrvName4_Type()
)
aaacmdSrvName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName4.setStatus("current")


class _AaacmdRowStatus_Type(RowStatus):
    """Custom type aaacmdRowStatus based on RowStatus"""
    defaultValue = 2


_AaacmdRowStatus_Type.__name__ = "RowStatus"
_AaacmdRowStatus_Object = MibTableColumn
aaacmdRowStatus = _AaacmdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1, 6),
    _AaacmdRowStatus_Type()
)
aaacmdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdRowStatus.setStatus("current")
_AaaUserMIB_ObjectIdentity = ObjectIdentity
aaaUserMIB = _AaaUserMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3)
)
_AaaUserTable_Object = MibTable
aaaUserTable = _AaaUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aaaUserTable.setStatus("current")
_AaaUserEntry_Object = MibTableRow
aaaUserEntry = _AaaUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1)
)
aaaUserEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaauUserName"),
)
if mibBuilder.loadTexts:
    aaaUserEntry.setStatus("current")


class _AaauUserName_Type(DisplayString):
    """Custom type aaauUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AaauUserName_Type.__name__ = "DisplayString"
_AaauUserName_Object = MibTableColumn
aaauUserName = _AaauUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 1),
    _AaauUserName_Type()
)
aaauUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauUserName.setStatus("current")


class _AaauPassword_Type(DisplayString):
    """Custom type aaauPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AaauPassword_Type.__name__ = "DisplayString"
_AaauPassword_Object = MibTableColumn
aaauPassword = _AaauPassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 2),
    _AaauPassword_Type()
)
aaauPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPassword.setStatus("current")


class _AaauReadRight1_Type(Unsigned32):
    """Custom type aaauReadRight1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauReadRight1_Type.__name__ = "Unsigned32"
_AaauReadRight1_Object = MibTableColumn
aaauReadRight1 = _AaauReadRight1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 3),
    _AaauReadRight1_Type()
)
aaauReadRight1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauReadRight1.setStatus("current")


class _AaauReadRight2_Type(Unsigned32):
    """Custom type aaauReadRight2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauReadRight2_Type.__name__ = "Unsigned32"
_AaauReadRight2_Object = MibTableColumn
aaauReadRight2 = _AaauReadRight2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 4),
    _AaauReadRight2_Type()
)
aaauReadRight2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauReadRight2.setStatus("current")


class _AaauWriteRight1_Type(Unsigned32):
    """Custom type aaauWriteRight1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauWriteRight1_Type.__name__ = "Unsigned32"
_AaauWriteRight1_Object = MibTableColumn
aaauWriteRight1 = _AaauWriteRight1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 5),
    _AaauWriteRight1_Type()
)
aaauWriteRight1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauWriteRight1.setStatus("current")


class _AaauWriteRight2_Type(Unsigned32):
    """Custom type aaauWriteRight2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauWriteRight2_Type.__name__ = "Unsigned32"
_AaauWriteRight2_Object = MibTableColumn
aaauWriteRight2 = _AaauWriteRight2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 6),
    _AaauWriteRight2_Type()
)
aaauWriteRight2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauWriteRight2.setStatus("current")


class _AaauProfile_Type(Integer32):
    """Custom type aaauProfile based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AaauProfile_Type.__name__ = "Integer32"
_AaauProfile_Object = MibTableColumn
aaauProfile = _AaauProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 7),
    _AaauProfile_Type()
)
aaauProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauProfile.setStatus("obsolete")


class _AaauSnmpLevel_Type(Integer32):
    """Custom type aaauSnmpLevel based on Integer32"""
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
        *(("no", 1),
          ("noauth", 2),
          ("sha", 3),
          ("md5", 4),
          ("shaDes", 5),
          ("md5Des", 6))
    )


_AaauSnmpLevel_Type.__name__ = "Integer32"
_AaauSnmpLevel_Object = MibTableColumn
aaauSnmpLevel = _AaauSnmpLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 8),
    _AaauSnmpLevel_Type()
)
aaauSnmpLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauSnmpLevel.setStatus("current")


class _AaauSnmpAuthKey_Type(OctetString):
    """Custom type aaauSnmpAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AaauSnmpAuthKey_Type.__name__ = "OctetString"
_AaauSnmpAuthKey_Object = MibTableColumn
aaauSnmpAuthKey = _AaauSnmpAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 9),
    _AaauSnmpAuthKey_Type()
)
aaauSnmpAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaauSnmpAuthKey.setStatus("current")


class _AaauRowStatus_Type(RowStatus):
    """Custom type aaauRowStatus based on RowStatus"""
    defaultValue = 2


_AaauRowStatus_Type.__name__ = "RowStatus"
_AaauRowStatus_Object = MibTableColumn
aaauRowStatus = _AaauRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 10),
    _AaauRowStatus_Type()
)
aaauRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauRowStatus.setStatus("current")


class _AaauOldPassword_Type(DisplayString):
    """Custom type aaauOldPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AaauOldPassword_Type.__name__ = "DisplayString"
_AaauOldPassword_Object = MibTableColumn
aaauOldPassword = _AaauOldPassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 11),
    _AaauOldPassword_Type()
)
aaauOldPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauOldPassword.setStatus("current")


class _AaauEndUserProfile_Type(DisplayString):
    """Custom type aaauEndUserProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaauEndUserProfile_Type.__name__ = "DisplayString"
_AaauEndUserProfile_Object = MibTableColumn
aaauEndUserProfile = _AaauEndUserProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 12),
    _AaauEndUserProfile_Type()
)
aaauEndUserProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauEndUserProfile.setStatus("current")


class _AaauPasswordExpirationDate_Type(DisplayString):
    """Custom type aaauPasswordExpirationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AaauPasswordExpirationDate_Type.__name__ = "DisplayString"
_AaauPasswordExpirationDate_Object = MibTableColumn
aaauPasswordExpirationDate = _AaauPasswordExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 13),
    _AaauPasswordExpirationDate_Type()
)
aaauPasswordExpirationDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPasswordExpirationDate.setStatus("current")


class _AaauPasswordExpirationInMinute_Type(Integer32):
    """Custom type aaauPasswordExpirationInMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 216000),
    )


_AaauPasswordExpirationInMinute_Type.__name__ = "Integer32"
_AaauPasswordExpirationInMinute_Object = MibTableColumn
aaauPasswordExpirationInMinute = _AaauPasswordExpirationInMinute_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 14),
    _AaauPasswordExpirationInMinute_Type()
)
aaauPasswordExpirationInMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPasswordExpirationInMinute.setStatus("current")


class _AaauPasswordAllowModifyDate_Type(DisplayString):
    """Custom type aaauPasswordAllowModifyDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AaauPasswordAllowModifyDate_Type.__name__ = "DisplayString"
_AaauPasswordAllowModifyDate_Object = MibTableColumn
aaauPasswordAllowModifyDate = _AaauPasswordAllowModifyDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 15),
    _AaauPasswordAllowModifyDate_Type()
)
aaauPasswordAllowModifyDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaauPasswordAllowModifyDate.setStatus("current")


class _AaauPasswordLockoutEnable_Type(Integer32):
    """Custom type aaauPasswordLockoutEnable based on Integer32"""
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
        *(("lockout", 1),
          ("unlock", 2),
          ("expired", 3))
    )


_AaauPasswordLockoutEnable_Type.__name__ = "Integer32"
_AaauPasswordLockoutEnable_Object = MibTableColumn
aaauPasswordLockoutEnable = _AaauPasswordLockoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 16),
    _AaauPasswordLockoutEnable_Type()
)
aaauPasswordLockoutEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPasswordLockoutEnable.setStatus("current")


class _AaauBadAtempts_Type(Integer32):
    """Custom type aaauBadAtempts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AaauBadAtempts_Type.__name__ = "Integer32"
_AaauBadAtempts_Object = MibTableColumn
aaauBadAtempts = _AaauBadAtempts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 17),
    _AaauBadAtempts_Type()
)
aaauBadAtempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaauBadAtempts.setStatus("current")
_AaaAuthenticatedUserTable_Object = MibTable
aaaAuthenticatedUserTable = _AaaAuthenticatedUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4)
)
if mibBuilder.loadTexts:
    aaaAuthenticatedUserTable.setStatus("current")
_AaaAuthenticatedUserEntry_Object = MibTableRow
aaaAuthenticatedUserEntry = _AaaAuthenticatedUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4, 1)
)
aaaAuthenticatedUserEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaaMacAddress"),
)
if mibBuilder.loadTexts:
    aaaAuthenticatedUserEntry.setStatus("current")
_AaaaMacAddress_Type = MacAddress
_AaaaMacAddress_Object = MibTableColumn
aaaaMacAddress = _AaaaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4, 1, 1),
    _AaaaMacAddress_Type()
)
aaaaMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaaMacAddress.setStatus("current")


class _AaaaUserName_Type(DisplayString):
    """Custom type aaaaUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaaUserName_Type.__name__ = "DisplayString"
_AaaaUserName_Object = MibTableColumn
aaaaUserName = _AaaaUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4, 1, 2),
    _AaaaUserName_Type()
)
aaaaUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaaUserName.setStatus("current")


class _AaaaSlot_Type(Integer32):
    """Custom type aaaaSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AaaaSlot_Type.__name__ = "Integer32"
_AaaaSlot_Object = MibTableColumn
aaaaSlot = _AaaaSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4, 1, 3),
    _AaaaSlot_Type()
)
aaaaSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaaSlot.setStatus("current")


class _AaaaPort_Type(Integer32):
    """Custom type aaaaPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AaaaPort_Type.__name__ = "Integer32"
_AaaaPort_Object = MibTableColumn
aaaaPort = _AaaaPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4, 1, 4),
    _AaaaPort_Type()
)
aaaaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaaPort.setStatus("current")


class _AaaaVlan_Type(Integer32):
    """Custom type aaaaVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaaaVlan_Type.__name__ = "Integer32"
_AaaaVlan_Object = MibTableColumn
aaaaVlan = _AaaaVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4, 1, 5),
    _AaaaVlan_Type()
)
aaaaVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaaVlan.setStatus("current")


class _AaaaDrop_Type(Integer32):
    """Custom type aaaaDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AaaaDrop_Type.__name__ = "Integer32"
_AaaaDrop_Object = MibTableColumn
aaaaDrop = _AaaaDrop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4, 1, 6),
    _AaaaDrop_Type()
)
aaaaDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaaDrop.setStatus("current")
_AaaAvlanConfig_ObjectIdentity = ObjectIdentity
aaaAvlanConfig = _AaaAvlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 5)
)


class _AaaAvlanDnsName_Type(DisplayString):
    """Custom type aaaAvlanDnsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AaaAvlanDnsName_Type.__name__ = "DisplayString"
_AaaAvlanDnsName_Object = MibScalar
aaaAvlanDnsName = _AaaAvlanDnsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 5, 1),
    _AaaAvlanDnsName_Type()
)
aaaAvlanDnsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAvlanDnsName.setStatus("current")
_AaaAvlanDhcpDefGateway_Type = IpAddress
_AaaAvlanDhcpDefGateway_Object = MibScalar
aaaAvlanDhcpDefGateway = _AaaAvlanDhcpDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 5, 2),
    _AaaAvlanDhcpDefGateway_Type()
)
aaaAvlanDhcpDefGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAvlanDhcpDefGateway.setStatus("current")


class _AaaAvlanDefaultTraffic_Type(Integer32):
    """Custom type aaaAvlanDefaultTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ns", 0),
          ("true", 1),
          ("false", 2))
    )


_AaaAvlanDefaultTraffic_Type.__name__ = "Integer32"
_AaaAvlanDefaultTraffic_Object = MibScalar
aaaAvlanDefaultTraffic = _AaaAvlanDefaultTraffic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 5, 3),
    _AaaAvlanDefaultTraffic_Type()
)
aaaAvlanDefaultTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAvlanDefaultTraffic.setStatus("current")


class _AaaAvlanPortBound_Type(Integer32):
    """Custom type aaaAvlanPortBound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ns", 0),
          ("true", 1),
          ("false", 2))
    )


_AaaAvlanPortBound_Type.__name__ = "Integer32"
_AaaAvlanPortBound_Object = MibScalar
aaaAvlanPortBound = _AaaAvlanPortBound_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 5, 4),
    _AaaAvlanPortBound_Type()
)
aaaAvlanPortBound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAvlanPortBound.setStatus("current")


class _AaaAvlanLanguage_Type(Integer32):
    """Custom type aaaAvlanLanguage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ns", 0),
          ("true", 1),
          ("false", 2))
    )


_AaaAvlanLanguage_Type.__name__ = "Integer32"
_AaaAvlanLanguage_Object = MibScalar
aaaAvlanLanguage = _AaaAvlanLanguage_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 5, 5),
    _AaaAvlanLanguage_Type()
)
aaaAvlanLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAvlanLanguage.setStatus("current")
_AaaAsaConfig_ObjectIdentity = ObjectIdentity
aaaAsaConfig = _AaaAsaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6)
)


class _AaaAsaPasswordSizeMin_Type(Integer32):
    """Custom type aaaAsaPasswordSizeMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_AaaAsaPasswordSizeMin_Type.__name__ = "Integer32"
_AaaAsaPasswordSizeMin_Object = MibScalar
aaaAsaPasswordSizeMin = _AaaAsaPasswordSizeMin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 1),
    _AaaAsaPasswordSizeMin_Type()
)
aaaAsaPasswordSizeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordSizeMin.setStatus("current")


class _AaaAsaDefaultPasswordExpirationInDays_Type(Integer32):
    """Custom type aaaAsaDefaultPasswordExpirationInDays based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_AaaAsaDefaultPasswordExpirationInDays_Type.__name__ = "Integer32"
_AaaAsaDefaultPasswordExpirationInDays_Object = MibScalar
aaaAsaDefaultPasswordExpirationInDays = _AaaAsaDefaultPasswordExpirationInDays_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 2),
    _AaaAsaDefaultPasswordExpirationInDays_Type()
)
aaaAsaDefaultPasswordExpirationInDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaDefaultPasswordExpirationInDays.setStatus("current")


class _AaaAsaPasswordContainUserName_Type(Integer32):
    """Custom type aaaAsaPasswordContainUserName based on Integer32"""
    defaultValue = 2

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


_AaaAsaPasswordContainUserName_Type.__name__ = "Integer32"
_AaaAsaPasswordContainUserName_Object = MibScalar
aaaAsaPasswordContainUserName = _AaaAsaPasswordContainUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 3),
    _AaaAsaPasswordContainUserName_Type()
)
aaaAsaPasswordContainUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordContainUserName.setStatus("current")


class _AaaAsaPasswordMinUpperCase_Type(Integer32):
    """Custom type aaaAsaPasswordMinUpperCase based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinUpperCase_Type.__name__ = "Integer32"
_AaaAsaPasswordMinUpperCase_Object = MibScalar
aaaAsaPasswordMinUpperCase = _AaaAsaPasswordMinUpperCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 4),
    _AaaAsaPasswordMinUpperCase_Type()
)
aaaAsaPasswordMinUpperCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinUpperCase.setStatus("current")


class _AaaAsaPasswordMinLowerCase_Type(Integer32):
    """Custom type aaaAsaPasswordMinLowerCase based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinLowerCase_Type.__name__ = "Integer32"
_AaaAsaPasswordMinLowerCase_Object = MibScalar
aaaAsaPasswordMinLowerCase = _AaaAsaPasswordMinLowerCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 5),
    _AaaAsaPasswordMinLowerCase_Type()
)
aaaAsaPasswordMinLowerCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinLowerCase.setStatus("current")


class _AaaAsaPasswordMinDigit_Type(Integer32):
    """Custom type aaaAsaPasswordMinDigit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinDigit_Type.__name__ = "Integer32"
_AaaAsaPasswordMinDigit_Object = MibScalar
aaaAsaPasswordMinDigit = _AaaAsaPasswordMinDigit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 6),
    _AaaAsaPasswordMinDigit_Type()
)
aaaAsaPasswordMinDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinDigit.setStatus("current")


class _AaaAsaPasswordMinNonAlphan_Type(Integer32):
    """Custom type aaaAsaPasswordMinNonAlphan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinNonAlphan_Type.__name__ = "Integer32"
_AaaAsaPasswordMinNonAlphan_Object = MibScalar
aaaAsaPasswordMinNonAlphan = _AaaAsaPasswordMinNonAlphan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 7),
    _AaaAsaPasswordMinNonAlphan_Type()
)
aaaAsaPasswordMinNonAlphan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinNonAlphan.setStatus("current")


class _AaaAsaPasswordHistory_Type(Integer32):
    """Custom type aaaAsaPasswordHistory based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AaaAsaPasswordHistory_Type.__name__ = "Integer32"
_AaaAsaPasswordHistory_Object = MibScalar
aaaAsaPasswordHistory = _AaaAsaPasswordHistory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 8),
    _AaaAsaPasswordHistory_Type()
)
aaaAsaPasswordHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordHistory.setStatus("current")


class _AaaAsaPasswordMinAge_Type(Integer32):
    """Custom type aaaAsaPasswordMinAge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_AaaAsaPasswordMinAge_Type.__name__ = "Integer32"
_AaaAsaPasswordMinAge_Object = MibScalar
aaaAsaPasswordMinAge = _AaaAsaPasswordMinAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 9),
    _AaaAsaPasswordMinAge_Type()
)
aaaAsaPasswordMinAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinAge.setStatus("current")


class _AaaAsaLockoutWindow_Type(Integer32):
    """Custom type aaaAsaLockoutWindow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AaaAsaLockoutWindow_Type.__name__ = "Integer32"
_AaaAsaLockoutWindow_Object = MibScalar
aaaAsaLockoutWindow = _AaaAsaLockoutWindow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 10),
    _AaaAsaLockoutWindow_Type()
)
aaaAsaLockoutWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaLockoutWindow.setStatus("current")


class _AaaAsaLockoutDuration_Type(Integer32):
    """Custom type aaaAsaLockoutDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AaaAsaLockoutDuration_Type.__name__ = "Integer32"
_AaaAsaLockoutDuration_Object = MibScalar
aaaAsaLockoutDuration = _AaaAsaLockoutDuration_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 11),
    _AaaAsaLockoutDuration_Type()
)
aaaAsaLockoutDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaLockoutDuration.setStatus("current")


class _AaaAsaLockoutThreshold_Type(Integer32):
    """Custom type aaaAsaLockoutThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AaaAsaLockoutThreshold_Type.__name__ = "Integer32"
_AaaAsaLockoutThreshold_Object = MibScalar
aaaAsaLockoutThreshold = _AaaAsaLockoutThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 12),
    _AaaAsaLockoutThreshold_Type()
)
aaaAsaLockoutThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaLockoutThreshold.setStatus("current")


class _AaaAsaROUserPingTrtEnable_Type(Integer32):
    """Custom type aaaAsaROUserPingTrtEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AaaAsaROUserPingTrtEnable_Type.__name__ = "Integer32"
_AaaAsaROUserPingTrtEnable_Object = MibScalar
aaaAsaROUserPingTrtEnable = _AaaAsaROUserPingTrtEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 13),
    _AaaAsaROUserPingTrtEnable_Type()
)
aaaAsaROUserPingTrtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaROUserPingTrtEnable.setStatus("obsolete")


class _AaaAsaAccessPolicyAdminConsoleOnly_Type(Integer32):
    """Custom type aaaAsaAccessPolicyAdminConsoleOnly based on Integer32"""
    defaultValue = 2

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


_AaaAsaAccessPolicyAdminConsoleOnly_Type.__name__ = "Integer32"
_AaaAsaAccessPolicyAdminConsoleOnly_Object = MibScalar
aaaAsaAccessPolicyAdminConsoleOnly = _AaaAsaAccessPolicyAdminConsoleOnly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 14),
    _AaaAsaAccessPolicyAdminConsoleOnly_Type()
)
aaaAsaAccessPolicyAdminConsoleOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaAccessPolicyAdminConsoleOnly.setStatus("current")
_AaaAvlanAddressTable_Object = MibTable
aaaAvlanAddressTable = _AaaAvlanAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 7)
)
if mibBuilder.loadTexts:
    aaaAvlanAddressTable.setStatus("current")
_AaaAvlanAddressEntry_Object = MibTableRow
aaaAvlanAddressEntry = _AaaAvlanAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 7, 1)
)
aaaAvlanAddressEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaAvlanId"),
)
if mibBuilder.loadTexts:
    aaaAvlanAddressEntry.setStatus("current")


class _AaaAvlanId_Type(Integer32):
    """Custom type aaaAvlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AaaAvlanId_Type.__name__ = "Integer32"
_AaaAvlanId_Object = MibTableColumn
aaaAvlanId = _AaaAvlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 7, 1, 1),
    _AaaAvlanId_Type()
)
aaaAvlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaAvlanId.setStatus("current")
_AaaAvlanIpAddress_Type = IpAddress
_AaaAvlanIpAddress_Object = MibTableColumn
aaaAvlanIpAddress = _AaaAvlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 7, 1, 2),
    _AaaAvlanIpAddress_Type()
)
aaaAvlanIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAvlanIpAddress.setStatus("current")
_AaaUserNetProfileTable_Object = MibTable
aaaUserNetProfileTable = _AaaUserNetProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8)
)
if mibBuilder.loadTexts:
    aaaUserNetProfileTable.setStatus("current")
_AaaUserNetProfileEntry_Object = MibTableRow
aaaUserNetProfileEntry = _AaaUserNetProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1)
)
aaaUserNetProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaUserNetProfileName"),
)
if mibBuilder.loadTexts:
    aaaUserNetProfileEntry.setStatus("current")


class _AaaUserNetProfileName_Type(DisplayString):
    """Custom type aaaUserNetProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaUserNetProfileName_Type.__name__ = "DisplayString"
_AaaUserNetProfileName_Object = MibTableColumn
aaaUserNetProfileName = _AaaUserNetProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1, 1),
    _AaaUserNetProfileName_Type()
)
aaaUserNetProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaUserNetProfileName.setStatus("current")


class _AaaUserNetProfileVlanID_Type(Integer32):
    """Custom type aaaUserNetProfileVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AaaUserNetProfileVlanID_Type.__name__ = "Integer32"
_AaaUserNetProfileVlanID_Object = MibTableColumn
aaaUserNetProfileVlanID = _AaaUserNetProfileVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1, 2),
    _AaaUserNetProfileVlanID_Type()
)
aaaUserNetProfileVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUserNetProfileVlanID.setStatus("current")
_AaaUserNetProfileRowStatus_Type = RowStatus
_AaaUserNetProfileRowStatus_Object = MibTableColumn
aaaUserNetProfileRowStatus = _AaaUserNetProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1, 3),
    _AaaUserNetProfileRowStatus_Type()
)
aaaUserNetProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUserNetProfileRowStatus.setStatus("current")


class _AaaUserNetProfileHICflag_Type(Integer32):
    """Custom type aaaUserNetProfileHICflag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AaaUserNetProfileHICflag_Type.__name__ = "Integer32"
_AaaUserNetProfileHICflag_Object = MibTableColumn
aaaUserNetProfileHICflag = _AaaUserNetProfileHICflag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1, 4),
    _AaaUserNetProfileHICflag_Type()
)
aaaUserNetProfileHICflag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUserNetProfileHICflag.setStatus("current")


class _AaaUserNetProfileQosPolicyListName_Type(DisplayString):
    """Custom type aaaUserNetProfileQosPolicyListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaUserNetProfileQosPolicyListName_Type.__name__ = "DisplayString"
_AaaUserNetProfileQosPolicyListName_Object = MibTableColumn
aaaUserNetProfileQosPolicyListName = _AaaUserNetProfileQosPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1, 5),
    _AaaUserNetProfileQosPolicyListName_Type()
)
aaaUserNetProfileQosPolicyListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUserNetProfileQosPolicyListName.setStatus("current")


class _AaaRadAgentConfig_Type(Integer32):
    """Custom type aaaRadAgentConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AaaRadAgentConfig_Type.__name__ = "Integer32"
_AaaRadAgentConfig_Object = MibScalar
aaaRadAgentConfig = _AaaRadAgentConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 9),
    _AaaRadAgentConfig_Type()
)
aaaRadAgentConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadAgentConfig.setStatus("obsolete")
_AaaRadAgentIP_Type = IpAddress
_AaaRadAgentIP_Object = MibScalar
aaaRadAgentIP = _AaaRadAgentIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 10),
    _AaaRadAgentIP_Type()
)
aaaRadAgentIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadAgentIP.setStatus("obsolete")
_AaaHicConfig_ObjectIdentity = ObjectIdentity
aaaHicConfig = _AaaHicConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11)
)
_AaaHicSvrTable_Object = MibTable
aaaHicSvrTable = _AaaHicSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    aaaHicSvrTable.setStatus("current")
_AaaHicSvrEntry_Object = MibTableRow
aaaHicSvrEntry = _AaaHicSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1)
)
aaaHicSvrEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaHicSvrName"),
)
if mibBuilder.loadTexts:
    aaaHicSvrEntry.setStatus("current")


class _AaaHicSvrName_Type(SnmpAdminString):
    """Custom type aaaHicSvrName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AaaHicSvrName_Type.__name__ = "SnmpAdminString"
_AaaHicSvrName_Object = MibTableColumn
aaaHicSvrName = _AaaHicSvrName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1, 1),
    _AaaHicSvrName_Type()
)
aaaHicSvrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaHicSvrName.setStatus("current")
_AaaHicSvrIpAddr_Type = IpAddress
_AaaHicSvrIpAddr_Object = MibTableColumn
aaaHicSvrIpAddr = _AaaHicSvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1, 2),
    _AaaHicSvrIpAddr_Type()
)
aaaHicSvrIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicSvrIpAddr.setStatus("current")


class _AaaHicSvrPort_Type(Integer32):
    """Custom type aaaHicSvrPort based on Integer32"""
    defaultValue = 11707

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_AaaHicSvrPort_Type.__name__ = "Integer32"
_AaaHicSvrPort_Object = MibTableColumn
aaaHicSvrPort = _AaaHicSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1, 3),
    _AaaHicSvrPort_Type()
)
aaaHicSvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicSvrPort.setStatus("current")


class _AaaHicSvrKey_Type(SnmpAdminString):
    """Custom type aaaHicSvrKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AaaHicSvrKey_Type.__name__ = "SnmpAdminString"
_AaaHicSvrKey_Object = MibTableColumn
aaaHicSvrKey = _AaaHicSvrKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1, 4),
    _AaaHicSvrKey_Type()
)
aaaHicSvrKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicSvrKey.setStatus("current")
_AaaHicSvrRowStatus_Type = RowStatus
_AaaHicSvrRowStatus_Object = MibTableColumn
aaaHicSvrRowStatus = _AaaHicSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1, 5),
    _AaaHicSvrRowStatus_Type()
)
aaaHicSvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicSvrRowStatus.setStatus("current")


class _AaaHicSvrStatus_Type(Integer32):
    """Custom type aaaHicSvrStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_AaaHicSvrStatus_Type.__name__ = "Integer32"
_AaaHicSvrStatus_Object = MibTableColumn
aaaHicSvrStatus = _AaaHicSvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1, 6),
    _AaaHicSvrStatus_Type()
)
aaaHicSvrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaHicSvrStatus.setStatus("current")
_AaaHicAllowedTable_Object = MibTable
aaaHicAllowedTable = _AaaHicAllowedTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    aaaHicAllowedTable.setStatus("current")
_AaaHicAllowedEntry_Object = MibTableRow
aaaHicAllowedEntry = _AaaHicAllowedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 2, 1)
)
aaaHicAllowedEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaHicAllowedName"),
)
if mibBuilder.loadTexts:
    aaaHicAllowedEntry.setStatus("current")


class _AaaHicAllowedName_Type(SnmpAdminString):
    """Custom type aaaHicAllowedName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AaaHicAllowedName_Type.__name__ = "SnmpAdminString"
_AaaHicAllowedName_Object = MibTableColumn
aaaHicAllowedName = _AaaHicAllowedName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 2, 1, 1),
    _AaaHicAllowedName_Type()
)
aaaHicAllowedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaHicAllowedName.setStatus("current")
_AaaHicAllowedIpAddr_Type = IpAddress
_AaaHicAllowedIpAddr_Object = MibTableColumn
aaaHicAllowedIpAddr = _AaaHicAllowedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 2, 1, 2),
    _AaaHicAllowedIpAddr_Type()
)
aaaHicAllowedIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicAllowedIpAddr.setStatus("current")


class _AaaHicAllowedIpMask_Type(IpAddress):
    """Custom type aaaHicAllowedIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AaaHicAllowedIpMask_Type.__name__ = "IpAddress"
_AaaHicAllowedIpMask_Object = MibTableColumn
aaaHicAllowedIpMask = _AaaHicAllowedIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 2, 1, 3),
    _AaaHicAllowedIpMask_Type()
)
aaaHicAllowedIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicAllowedIpMask.setStatus("current")
_AaaHicAllowedRowStatus_Type = RowStatus
_AaaHicAllowedRowStatus_Object = MibTableColumn
aaaHicAllowedRowStatus = _AaaHicAllowedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 2, 1, 4),
    _AaaHicAllowedRowStatus_Type()
)
aaaHicAllowedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicAllowedRowStatus.setStatus("current")
_AaaHicOverrideTable_Object = MibTable
aaaHicOverrideTable = _AaaHicOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 3)
)
if mibBuilder.loadTexts:
    aaaHicOverrideTable.setStatus("current")
_AaaHicOverrideEntry_Object = MibTableRow
aaaHicOverrideEntry = _AaaHicOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 3, 1)
)
aaaHicOverrideEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaHicOverrideMac"),
)
if mibBuilder.loadTexts:
    aaaHicOverrideEntry.setStatus("current")
_AaaHicOverrideMac_Type = MacAddress
_AaaHicOverrideMac_Object = MibTableColumn
aaaHicOverrideMac = _AaaHicOverrideMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 3, 1, 1),
    _AaaHicOverrideMac_Type()
)
aaaHicOverrideMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaHicOverrideMac.setStatus("current")


class _AaaHicOverrideStatus_Type(Integer32):
    """Custom type aaaHicOverrideStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enforce", 1),
          ("bypass", 2))
    )


_AaaHicOverrideStatus_Type.__name__ = "Integer32"
_AaaHicOverrideStatus_Object = MibTableColumn
aaaHicOverrideStatus = _AaaHicOverrideStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 3, 1, 2),
    _AaaHicOverrideStatus_Type()
)
aaaHicOverrideStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicOverrideStatus.setStatus("current")
_AaaHicOverrideRowStatus_Type = RowStatus
_AaaHicOverrideRowStatus_Object = MibTableColumn
aaaHicOverrideRowStatus = _AaaHicOverrideRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 3, 1, 3),
    _AaaHicOverrideRowStatus_Type()
)
aaaHicOverrideRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicOverrideRowStatus.setStatus("current")
_AaaHicHostTable_Object = MibTable
aaaHicHostTable = _AaaHicHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 4)
)
if mibBuilder.loadTexts:
    aaaHicHostTable.setStatus("current")
_AaaHicHostEntry_Object = MibTableRow
aaaHicHostEntry = _AaaHicHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 4, 1)
)
aaaHicHostEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaHicHostMac"),
)
if mibBuilder.loadTexts:
    aaaHicHostEntry.setStatus("current")
_AaaHicHostMac_Type = MacAddress
_AaaHicHostMac_Object = MibTableColumn
aaaHicHostMac = _AaaHicHostMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 4, 1, 1),
    _AaaHicHostMac_Type()
)
aaaHicHostMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaHicHostMac.setStatus("current")


class _AaaHicHostStatus_Type(Integer32):
    """Custom type aaaHicHostStatus based on Integer32"""
    defaultValue = 3

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
        *(("inprogress", 1),
          ("success", 2),
          ("fail", 3),
          ("timeout", 4))
    )


_AaaHicHostStatus_Type.__name__ = "Integer32"
_AaaHicHostStatus_Object = MibTableColumn
aaaHicHostStatus = _AaaHicHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 4, 1, 2),
    _AaaHicHostStatus_Type()
)
aaaHicHostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaHicHostStatus.setStatus("current")
_AaaHicConfigInfo_ObjectIdentity = ObjectIdentity
aaaHicConfigInfo = _AaaHicConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5)
)


class _AaaHicStatus_Type(Integer32):
    """Custom type aaaHicStatus based on Integer32"""
    defaultValue = 2

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


_AaaHicStatus_Type.__name__ = "Integer32"
_AaaHicStatus_Object = MibScalar
aaaHicStatus = _AaaHicStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 1),
    _AaaHicStatus_Type()
)
aaaHicStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicStatus.setStatus("current")


class _AaaHicAllowed1Name_Type(SnmpAdminString):
    """Custom type aaaHicAllowed1Name based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AaaHicAllowed1Name_Type.__name__ = "SnmpAdminString"
_AaaHicAllowed1Name_Object = MibScalar
aaaHicAllowed1Name = _AaaHicAllowed1Name_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 2),
    _AaaHicAllowed1Name_Type()
)
aaaHicAllowed1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaHicAllowed1Name.setStatus("current")


class _AaaHicAllowed2Name_Type(SnmpAdminString):
    """Custom type aaaHicAllowed2Name based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AaaHicAllowed2Name_Type.__name__ = "SnmpAdminString"
_AaaHicAllowed2Name_Object = MibScalar
aaaHicAllowed2Name = _AaaHicAllowed2Name_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 3),
    _AaaHicAllowed2Name_Type()
)
aaaHicAllowed2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaHicAllowed2Name.setStatus("current")


class _AaaHicAllowed3Name_Type(SnmpAdminString):
    """Custom type aaaHicAllowed3Name based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AaaHicAllowed3Name_Type.__name__ = "SnmpAdminString"
_AaaHicAllowed3Name_Object = MibScalar
aaaHicAllowed3Name = _AaaHicAllowed3Name_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 4),
    _AaaHicAllowed3Name_Type()
)
aaaHicAllowed3Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaHicAllowed3Name.setStatus("current")


class _AaaHicAllowed4Name_Type(SnmpAdminString):
    """Custom type aaaHicAllowed4Name based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AaaHicAllowed4Name_Type.__name__ = "SnmpAdminString"
_AaaHicAllowed4Name_Object = MibScalar
aaaHicAllowed4Name = _AaaHicAllowed4Name_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 5),
    _AaaHicAllowed4Name_Type()
)
aaaHicAllowed4Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaHicAllowed4Name.setStatus("current")


class _AaaHicWebAgentDownloadUrl_Type(SnmpAdminString):
    """Custom type aaaHicWebAgentDownloadUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AaaHicWebAgentDownloadUrl_Type.__name__ = "SnmpAdminString"
_AaaHicWebAgentDownloadUrl_Object = MibScalar
aaaHicWebAgentDownloadUrl = _AaaHicWebAgentDownloadUrl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 6),
    _AaaHicWebAgentDownloadUrl_Type()
)
aaaHicWebAgentDownloadUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaHicWebAgentDownloadUrl.setStatus("current")


class _AaaHicCustomHttpProxyPort_Type(Integer32):
    """Custom type aaaHicCustomHttpProxyPort based on Integer32"""
    defaultValue = 8080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_AaaHicCustomHttpProxyPort_Type.__name__ = "Integer32"
_AaaHicCustomHttpProxyPort_Object = MibScalar
aaaHicCustomHttpProxyPort = _AaaHicCustomHttpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 7),
    _AaaHicCustomHttpProxyPort_Type()
)
aaaHicCustomHttpProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaHicCustomHttpProxyPort.setStatus("current")
_AaaUNPIpNetRuleTable_Object = MibTable
aaaUNPIpNetRuleTable = _AaaUNPIpNetRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 12)
)
if mibBuilder.loadTexts:
    aaaUNPIpNetRuleTable.setStatus("current")
_AaaUNPIpNetRuleEntry_Object = MibTableRow
aaaUNPIpNetRuleEntry = _AaaUNPIpNetRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 12, 1)
)
aaaUNPIpNetRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaUNPIpNetRuleAddrType"),
    (0, "ALCATEL-IND1-AAA-MIB", "aaaUNPIpNetRuleAddr"),
    (0, "ALCATEL-IND1-AAA-MIB", "aaaUNPIpNetRuleMask"),
)
if mibBuilder.loadTexts:
    aaaUNPIpNetRuleEntry.setStatus("current")
_AaaUNPIpNetRuleAddrType_Type = InetAddressType
_AaaUNPIpNetRuleAddrType_Object = MibTableColumn
aaaUNPIpNetRuleAddrType = _AaaUNPIpNetRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 12, 1, 1),
    _AaaUNPIpNetRuleAddrType_Type()
)
aaaUNPIpNetRuleAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaUNPIpNetRuleAddrType.setStatus("current")
_AaaUNPIpNetRuleAddr_Type = InetAddress
_AaaUNPIpNetRuleAddr_Object = MibTableColumn
aaaUNPIpNetRuleAddr = _AaaUNPIpNetRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 12, 1, 2),
    _AaaUNPIpNetRuleAddr_Type()
)
aaaUNPIpNetRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaUNPIpNetRuleAddr.setStatus("current")
_AaaUNPIpNetRuleMask_Type = InetAddress
_AaaUNPIpNetRuleMask_Object = MibTableColumn
aaaUNPIpNetRuleMask = _AaaUNPIpNetRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 12, 1, 3),
    _AaaUNPIpNetRuleMask_Type()
)
aaaUNPIpNetRuleMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaUNPIpNetRuleMask.setStatus("current")


class _AaaUNPIpNetRuleProfileName_Type(SnmpAdminString):
    """Custom type aaaUNPIpNetRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaUNPIpNetRuleProfileName_Type.__name__ = "SnmpAdminString"
_AaaUNPIpNetRuleProfileName_Object = MibTableColumn
aaaUNPIpNetRuleProfileName = _AaaUNPIpNetRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 12, 1, 4),
    _AaaUNPIpNetRuleProfileName_Type()
)
aaaUNPIpNetRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPIpNetRuleProfileName.setStatus("current")
_AaaUNPIpNetRuleRowStatus_Type = RowStatus
_AaaUNPIpNetRuleRowStatus_Object = MibTableColumn
aaaUNPIpNetRuleRowStatus = _AaaUNPIpNetRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 12, 1, 5),
    _AaaUNPIpNetRuleRowStatus_Type()
)
aaaUNPIpNetRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPIpNetRuleRowStatus.setStatus("current")
_AaaUNPMacRuleTable_Object = MibTable
aaaUNPMacRuleTable = _AaaUNPMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 13)
)
if mibBuilder.loadTexts:
    aaaUNPMacRuleTable.setStatus("current")
_AaaUNPMacRuleEntry_Object = MibTableRow
aaaUNPMacRuleEntry = _AaaUNPMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 13, 1)
)
aaaUNPMacRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaUNPMacRuleAddr"),
)
if mibBuilder.loadTexts:
    aaaUNPMacRuleEntry.setStatus("current")
_AaaUNPMacRuleAddr_Type = MacAddress
_AaaUNPMacRuleAddr_Object = MibTableColumn
aaaUNPMacRuleAddr = _AaaUNPMacRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 13, 1, 1),
    _AaaUNPMacRuleAddr_Type()
)
aaaUNPMacRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaUNPMacRuleAddr.setStatus("current")


class _AaaUNPMacRuleProfileName_Type(SnmpAdminString):
    """Custom type aaaUNPMacRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaUNPMacRuleProfileName_Type.__name__ = "SnmpAdminString"
_AaaUNPMacRuleProfileName_Object = MibTableColumn
aaaUNPMacRuleProfileName = _AaaUNPMacRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 13, 1, 2),
    _AaaUNPMacRuleProfileName_Type()
)
aaaUNPMacRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPMacRuleProfileName.setStatus("current")
_AaaUNPMacRuleRowStatus_Type = RowStatus
_AaaUNPMacRuleRowStatus_Object = MibTableColumn
aaaUNPMacRuleRowStatus = _AaaUNPMacRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 13, 1, 3),
    _AaaUNPMacRuleRowStatus_Type()
)
aaaUNPMacRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPMacRuleRowStatus.setStatus("current")
_AaaUNPMacRangeRuleTable_Object = MibTable
aaaUNPMacRangeRuleTable = _AaaUNPMacRangeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 14)
)
if mibBuilder.loadTexts:
    aaaUNPMacRangeRuleTable.setStatus("current")
_AaaUNPMacRangeRuleEntry_Object = MibTableRow
aaaUNPMacRangeRuleEntry = _AaaUNPMacRangeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 14, 1)
)
aaaUNPMacRangeRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaUNPMacRangeRuleLoAddr"),
)
if mibBuilder.loadTexts:
    aaaUNPMacRangeRuleEntry.setStatus("current")
_AaaUNPMacRangeRuleLoAddr_Type = MacAddress
_AaaUNPMacRangeRuleLoAddr_Object = MibTableColumn
aaaUNPMacRangeRuleLoAddr = _AaaUNPMacRangeRuleLoAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 14, 1, 1),
    _AaaUNPMacRangeRuleLoAddr_Type()
)
aaaUNPMacRangeRuleLoAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaUNPMacRangeRuleLoAddr.setStatus("current")
_AaaUNPMacRangeRuleHiAddr_Type = MacAddress
_AaaUNPMacRangeRuleHiAddr_Object = MibTableColumn
aaaUNPMacRangeRuleHiAddr = _AaaUNPMacRangeRuleHiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 14, 1, 2),
    _AaaUNPMacRangeRuleHiAddr_Type()
)
aaaUNPMacRangeRuleHiAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPMacRangeRuleHiAddr.setStatus("current")


class _AaaUNPMacRangeRuleProfileName_Type(SnmpAdminString):
    """Custom type aaaUNPMacRangeRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaUNPMacRangeRuleProfileName_Type.__name__ = "SnmpAdminString"
_AaaUNPMacRangeRuleProfileName_Object = MibTableColumn
aaaUNPMacRangeRuleProfileName = _AaaUNPMacRangeRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 14, 1, 3),
    _AaaUNPMacRangeRuleProfileName_Type()
)
aaaUNPMacRangeRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPMacRangeRuleProfileName.setStatus("current")
_AaaUNPMacRangeRuleRowStatus_Type = RowStatus
_AaaUNPMacRangeRuleRowStatus_Object = MibTableColumn
aaaUNPMacRangeRuleRowStatus = _AaaUNPMacRangeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 14, 1, 4),
    _AaaUNPMacRangeRuleRowStatus_Type()
)
aaaUNPMacRangeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPMacRangeRuleRowStatus.setStatus("current")
_AlcatelIND1AAAMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBConformance = _AlcatelIND1AAAMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBConformance.setStatus("current")
_AlcatelIND1AAAMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBGroups = _AlcatelIND1AAAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBGroups.setStatus("current")
_AlcatelIND1AAAMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBCompliances = _AlcatelIND1AAAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBCompliances.setStatus("current")
_AlaAaaTrapsDesc_ObjectIdentity = ObjectIdentity
alaAaaTrapsDesc = _AlaAaaTrapsDesc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 1)
)
_AlaAaaTrapsDescRoot_ObjectIdentity = ObjectIdentity
alaAaaTrapsDescRoot = _AlaAaaTrapsDescRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 1, 0)
)
_AlaAaaTrapsObj_ObjectIdentity = ObjectIdentity
alaAaaTrapsObj = _AlaAaaTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 2)
)
_AaaHSvrIpAddress_Type = IpAddress
_AaaHSvrIpAddress_Object = MibScalar
aaaHSvrIpAddress = _AaaHSvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 2, 1),
    _AaaHSvrIpAddress_Type()
)
aaaHSvrIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aaaHSvrIpAddress.setStatus("current")

# Managed Objects groups

aaaServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 1)
)
aaaServerMIBGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaasName"),
        ("ALCATEL-IND1-AAA-MIB", "aaasProtocol"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHostName"),
        ("ALCATEL-IND1-AAA-MIB", "aaasIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHostName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaasIpAddress2"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRetries"),
        ("ALCATEL-IND1-AAA-MIB", "aaasTimout"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadKey"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadAuthPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadAcctPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapDn"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapPasswd"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapSearchBase"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapServType"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapEnableSsl"),
        ("ALCATEL-IND1-AAA-MIB", "aaasAceClear"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaasTacacsKey"),
        ("ALCATEL-IND1-AAA-MIB", "aaasTacacsPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHttpPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHttpDirectory"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHttpProxyHostName"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHttpProxyIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHttpProxyPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasVrfName"))
)
if mibBuilder.loadTexts:
    aaaServerMIBGroup.setStatus("current")

aaaAuthAcctGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 2)
)
aaaAuthAcctGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaatvVlan"),
        ("ALCATEL-IND1-AAA-MIB", "aaatvName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaatvName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaatvName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaatvName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaatvRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaatvCertificate"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsCertificate"),
        ("ALCATEL-IND1-AAA-MIB", "aaacvVlan"),
        ("ALCATEL-IND1-AAA-MIB", "aaacvName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaacvName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaacvName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaacvName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaacvRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxOpen"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaacxInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaacxName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaacxName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaacxName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaacxName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaacxRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaatpInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaatpName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaatpName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaatpName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaatpName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaatpLevel"),
        ("ALCATEL-IND1-AAA-MIB", "aaatpRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdSrvName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdSrvName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdSrvName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdSrvName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdRowStatus"))
)
if mibBuilder.loadTexts:
    aaaAuthAcctGroup.setStatus("current")

aaaUserMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 3)
)
aaaUserMIBGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaauUserName"),
        ("ALCATEL-IND1-AAA-MIB", "aaauPassword"),
        ("ALCATEL-IND1-AAA-MIB", "aaauReadRight1"),
        ("ALCATEL-IND1-AAA-MIB", "aaauReadRight2"),
        ("ALCATEL-IND1-AAA-MIB", "aaauWriteRight1"),
        ("ALCATEL-IND1-AAA-MIB", "aaauWriteRight2"),
        ("ALCATEL-IND1-AAA-MIB", "aaauProfile"),
        ("ALCATEL-IND1-AAA-MIB", "aaauSnmpLevel"),
        ("ALCATEL-IND1-AAA-MIB", "aaauSnmpAuthKey"),
        ("ALCATEL-IND1-AAA-MIB", "aaauRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaauOldPassword"),
        ("ALCATEL-IND1-AAA-MIB", "aaauEndUserProfile"),
        ("ALCATEL-IND1-AAA-MIB", "aaauPasswordExpirationDate"),
        ("ALCATEL-IND1-AAA-MIB", "aaauPasswordExpirationInMinute"),
        ("ALCATEL-IND1-AAA-MIB", "aaauPasswordAllowModifyDate"),
        ("ALCATEL-IND1-AAA-MIB", "aaauPasswordLockoutEnable"),
        ("ALCATEL-IND1-AAA-MIB", "aaauBadAtempts"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordSizeMin"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaDefaultPasswordExpirationInDays"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordContainUserName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinUpperCase"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinLowerCase"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinDigit"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinNonAlphan"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordHistory"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinAge"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaLockoutWindow"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaLockoutDuration"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaLockoutThreshold"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaROUserPingTrtEnable"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaAccessPolicyAdminConsoleOnly"))
)
if mibBuilder.loadTexts:
    aaaUserMIBGroup.setStatus("current")

aaaHicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 4)
)
aaaHicGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaHicSvrIpAddr"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicSvrPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicSvrKey"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicSvrRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicSvrStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicAllowedIpAddr"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicAllowedRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicOverrideStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicOverrideRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicHostStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicAllowed1Name"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicAllowed2Name"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicAllowed3Name"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicAllowed4Name"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicWebAgentDownloadUrl"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicCustomHttpProxyPort"))
)
if mibBuilder.loadTexts:
    aaaHicGroup.setStatus("current")


# Notification objects

aaaHicServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 1, 0, 1)
)
aaaHicServerTrap.setObjects(
    ("ALCATEL-IND1-AAA-MIB", "aaaHSvrIpAddress")
)
if mibBuilder.loadTexts:
    aaaHicServerTrap.setStatus(
        "current"
    )


# Notifications groups

aaaTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 5)
)
aaaTrapsGroup.setObjects(
    ("ALCATEL-IND1-AAA-MIB", "aaaHicServerTrap")
)
if mibBuilder.loadTexts:
    aaaTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1AAAMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 2, 1)
)
alcatelIND1AAAMIBCompliance.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaServerMIBGroup"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthAcctGroup"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUserMIBGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-AAA-MIB",
    **{"alcatelIND1AAAMIB": alcatelIND1AAAMIB,
       "alcatelIND1AAAMIBObjects": alcatelIND1AAAMIBObjects,
       "aaaServerMIB": aaaServerMIB,
       "aaaServerTable": aaaServerTable,
       "aaaServerEntry": aaaServerEntry,
       "aaasName": aaasName,
       "aaasProtocol": aaasProtocol,
       "aaasHostName": aaasHostName,
       "aaasIpAddress": aaasIpAddress,
       "aaasHostName2": aaasHostName2,
       "aaasIpAddress2": aaasIpAddress2,
       "aaasRetries": aaasRetries,
       "aaasTimout": aaasTimout,
       "aaasRadKey": aaasRadKey,
       "aaasRadAuthPort": aaasRadAuthPort,
       "aaasRadAcctPort": aaasRadAcctPort,
       "aaasLdapPort": aaasLdapPort,
       "aaasLdapDn": aaasLdapDn,
       "aaasLdapPasswd": aaasLdapPasswd,
       "aaasLdapSearchBase": aaasLdapSearchBase,
       "aaasLdapServType": aaasLdapServType,
       "aaasLdapEnableSsl": aaasLdapEnableSsl,
       "aaasAceClear": aaasAceClear,
       "aaasRowStatus": aaasRowStatus,
       "aaasTacacsKey": aaasTacacsKey,
       "aaasTacacsPort": aaasTacacsPort,
       "aaasHttpPort": aaasHttpPort,
       "aaasHttpDirectory": aaasHttpDirectory,
       "aaasHttpProxyHostName": aaasHttpProxyHostName,
       "aaasHttpProxyIpAddress": aaasHttpProxyIpAddress,
       "aaasHttpProxyPort": aaasHttpProxyPort,
       "aaasVrfName": aaasVrfName,
       "aaaAuthAcctMIB": aaaAuthAcctMIB,
       "aaaAuthVlanTable": aaaAuthVlanTable,
       "aaaAuthVlanEntry": aaaAuthVlanEntry,
       "aaatvVlan": aaatvVlan,
       "aaatvName1": aaatvName1,
       "aaatvName2": aaatvName2,
       "aaatvName3": aaatvName3,
       "aaatvName4": aaatvName4,
       "aaatvRowStatus": aaatvRowStatus,
       "aaatvCertificate": aaatvCertificate,
       "aaaAuthSATable": aaaAuthSATable,
       "aaaAuthSAEntry": aaaAuthSAEntry,
       "aaatsInterface": aaatsInterface,
       "aaatsName1": aaatsName1,
       "aaatsName2": aaatsName2,
       "aaatsName3": aaatsName3,
       "aaatsName4": aaatsName4,
       "aaatsRowStatus": aaatsRowStatus,
       "aaatsCertificate": aaatsCertificate,
       "aaaAcctVlanTable": aaaAcctVlanTable,
       "aaaAcctVlanEntry": aaaAcctVlanEntry,
       "aaacvVlan": aaacvVlan,
       "aaacvName1": aaacvName1,
       "aaacvName2": aaacvName2,
       "aaacvName3": aaacvName3,
       "aaacvName4": aaacvName4,
       "aaacvRowStatus": aaacvRowStatus,
       "aaaAcctSATable": aaaAcctSATable,
       "aaaAcctSAEntry": aaaAcctSAEntry,
       "aaacsInterface": aaacsInterface,
       "aaacsName1": aaacsName1,
       "aaacsName2": aaacsName2,
       "aaacsName3": aaacsName3,
       "aaacsName4": aaacsName4,
       "aaacsRowStatus": aaacsRowStatus,
       "aaaAuth8021xTable": aaaAuth8021xTable,
       "aaaAuth8021xEntry": aaaAuth8021xEntry,
       "aaatxInterface": aaatxInterface,
       "aaatxName1": aaatxName1,
       "aaatxName2": aaatxName2,
       "aaatxName3": aaatxName3,
       "aaatxName4": aaatxName4,
       "aaatxOpen": aaatxOpen,
       "aaatxRowStatus": aaatxRowStatus,
       "aaaAcct8021xTable": aaaAcct8021xTable,
       "aaaAcct8021xEntry": aaaAcct8021xEntry,
       "aaacxInterface": aaacxInterface,
       "aaacxName1": aaacxName1,
       "aaacxName2": aaacxName2,
       "aaacxName3": aaacxName3,
       "aaacxName4": aaacxName4,
       "aaacxRowStatus": aaacxRowStatus,
       "aaaPkiTable": aaaPkiTable,
       "aaaPkiEntry": aaaPkiEntry,
       "aaatpInterface": aaatpInterface,
       "aaatpName1": aaatpName1,
       "aaatpName2": aaatpName2,
       "aaatpName3": aaatpName3,
       "aaatpName4": aaatpName4,
       "aaatpLevel": aaatpLevel,
       "aaatpRowStatus": aaatpRowStatus,
       "aaaAuthMACTable": aaaAuthMACTable,
       "aaaAuthMACEntry": aaaAuthMACEntry,
       "aaaMacInterface": aaaMacInterface,
       "aaaMacSrvrName1": aaaMacSrvrName1,
       "aaaMacSrvrName2": aaaMacSrvrName2,
       "aaaMacSrvrName3": aaaMacSrvrName3,
       "aaaMacSrvrName4": aaaMacSrvrName4,
       "aaaMacSrvrRowStatus": aaaMacSrvrRowStatus,
       "aaaAcctCmdTable": aaaAcctCmdTable,
       "aaaAcctCmdEntry": aaaAcctCmdEntry,
       "aaacmdInterface": aaacmdInterface,
       "aaacmdSrvName1": aaacmdSrvName1,
       "aaacmdSrvName2": aaacmdSrvName2,
       "aaacmdSrvName3": aaacmdSrvName3,
       "aaacmdSrvName4": aaacmdSrvName4,
       "aaacmdRowStatus": aaacmdRowStatus,
       "aaaUserMIB": aaaUserMIB,
       "aaaUserTable": aaaUserTable,
       "aaaUserEntry": aaaUserEntry,
       "aaauUserName": aaauUserName,
       "aaauPassword": aaauPassword,
       "aaauReadRight1": aaauReadRight1,
       "aaauReadRight2": aaauReadRight2,
       "aaauWriteRight1": aaauWriteRight1,
       "aaauWriteRight2": aaauWriteRight2,
       "aaauProfile": aaauProfile,
       "aaauSnmpLevel": aaauSnmpLevel,
       "aaauSnmpAuthKey": aaauSnmpAuthKey,
       "aaauRowStatus": aaauRowStatus,
       "aaauOldPassword": aaauOldPassword,
       "aaauEndUserProfile": aaauEndUserProfile,
       "aaauPasswordExpirationDate": aaauPasswordExpirationDate,
       "aaauPasswordExpirationInMinute": aaauPasswordExpirationInMinute,
       "aaauPasswordAllowModifyDate": aaauPasswordAllowModifyDate,
       "aaauPasswordLockoutEnable": aaauPasswordLockoutEnable,
       "aaauBadAtempts": aaauBadAtempts,
       "aaaAuthenticatedUserTable": aaaAuthenticatedUserTable,
       "aaaAuthenticatedUserEntry": aaaAuthenticatedUserEntry,
       "aaaaMacAddress": aaaaMacAddress,
       "aaaaUserName": aaaaUserName,
       "aaaaSlot": aaaaSlot,
       "aaaaPort": aaaaPort,
       "aaaaVlan": aaaaVlan,
       "aaaaDrop": aaaaDrop,
       "aaaAvlanConfig": aaaAvlanConfig,
       "aaaAvlanDnsName": aaaAvlanDnsName,
       "aaaAvlanDhcpDefGateway": aaaAvlanDhcpDefGateway,
       "aaaAvlanDefaultTraffic": aaaAvlanDefaultTraffic,
       "aaaAvlanPortBound": aaaAvlanPortBound,
       "aaaAvlanLanguage": aaaAvlanLanguage,
       "aaaAsaConfig": aaaAsaConfig,
       "aaaAsaPasswordSizeMin": aaaAsaPasswordSizeMin,
       "aaaAsaDefaultPasswordExpirationInDays": aaaAsaDefaultPasswordExpirationInDays,
       "aaaAsaPasswordContainUserName": aaaAsaPasswordContainUserName,
       "aaaAsaPasswordMinUpperCase": aaaAsaPasswordMinUpperCase,
       "aaaAsaPasswordMinLowerCase": aaaAsaPasswordMinLowerCase,
       "aaaAsaPasswordMinDigit": aaaAsaPasswordMinDigit,
       "aaaAsaPasswordMinNonAlphan": aaaAsaPasswordMinNonAlphan,
       "aaaAsaPasswordHistory": aaaAsaPasswordHistory,
       "aaaAsaPasswordMinAge": aaaAsaPasswordMinAge,
       "aaaAsaLockoutWindow": aaaAsaLockoutWindow,
       "aaaAsaLockoutDuration": aaaAsaLockoutDuration,
       "aaaAsaLockoutThreshold": aaaAsaLockoutThreshold,
       "aaaAsaROUserPingTrtEnable": aaaAsaROUserPingTrtEnable,
       "aaaAsaAccessPolicyAdminConsoleOnly": aaaAsaAccessPolicyAdminConsoleOnly,
       "aaaAvlanAddressTable": aaaAvlanAddressTable,
       "aaaAvlanAddressEntry": aaaAvlanAddressEntry,
       "aaaAvlanId": aaaAvlanId,
       "aaaAvlanIpAddress": aaaAvlanIpAddress,
       "aaaUserNetProfileTable": aaaUserNetProfileTable,
       "aaaUserNetProfileEntry": aaaUserNetProfileEntry,
       "aaaUserNetProfileName": aaaUserNetProfileName,
       "aaaUserNetProfileVlanID": aaaUserNetProfileVlanID,
       "aaaUserNetProfileRowStatus": aaaUserNetProfileRowStatus,
       "aaaUserNetProfileHICflag": aaaUserNetProfileHICflag,
       "aaaUserNetProfileQosPolicyListName": aaaUserNetProfileQosPolicyListName,
       "aaaRadAgentConfig": aaaRadAgentConfig,
       "aaaRadAgentIP": aaaRadAgentIP,
       "aaaHicConfig": aaaHicConfig,
       "aaaHicSvrTable": aaaHicSvrTable,
       "aaaHicSvrEntry": aaaHicSvrEntry,
       "aaaHicSvrName": aaaHicSvrName,
       "aaaHicSvrIpAddr": aaaHicSvrIpAddr,
       "aaaHicSvrPort": aaaHicSvrPort,
       "aaaHicSvrKey": aaaHicSvrKey,
       "aaaHicSvrRowStatus": aaaHicSvrRowStatus,
       "aaaHicSvrStatus": aaaHicSvrStatus,
       "aaaHicAllowedTable": aaaHicAllowedTable,
       "aaaHicAllowedEntry": aaaHicAllowedEntry,
       "aaaHicAllowedName": aaaHicAllowedName,
       "aaaHicAllowedIpAddr": aaaHicAllowedIpAddr,
       "aaaHicAllowedIpMask": aaaHicAllowedIpMask,
       "aaaHicAllowedRowStatus": aaaHicAllowedRowStatus,
       "aaaHicOverrideTable": aaaHicOverrideTable,
       "aaaHicOverrideEntry": aaaHicOverrideEntry,
       "aaaHicOverrideMac": aaaHicOverrideMac,
       "aaaHicOverrideStatus": aaaHicOverrideStatus,
       "aaaHicOverrideRowStatus": aaaHicOverrideRowStatus,
       "aaaHicHostTable": aaaHicHostTable,
       "aaaHicHostEntry": aaaHicHostEntry,
       "aaaHicHostMac": aaaHicHostMac,
       "aaaHicHostStatus": aaaHicHostStatus,
       "aaaHicConfigInfo": aaaHicConfigInfo,
       "aaaHicStatus": aaaHicStatus,
       "aaaHicAllowed1Name": aaaHicAllowed1Name,
       "aaaHicAllowed2Name": aaaHicAllowed2Name,
       "aaaHicAllowed3Name": aaaHicAllowed3Name,
       "aaaHicAllowed4Name": aaaHicAllowed4Name,
       "aaaHicWebAgentDownloadUrl": aaaHicWebAgentDownloadUrl,
       "aaaHicCustomHttpProxyPort": aaaHicCustomHttpProxyPort,
       "aaaUNPIpNetRuleTable": aaaUNPIpNetRuleTable,
       "aaaUNPIpNetRuleEntry": aaaUNPIpNetRuleEntry,
       "aaaUNPIpNetRuleAddrType": aaaUNPIpNetRuleAddrType,
       "aaaUNPIpNetRuleAddr": aaaUNPIpNetRuleAddr,
       "aaaUNPIpNetRuleMask": aaaUNPIpNetRuleMask,
       "aaaUNPIpNetRuleProfileName": aaaUNPIpNetRuleProfileName,
       "aaaUNPIpNetRuleRowStatus": aaaUNPIpNetRuleRowStatus,
       "aaaUNPMacRuleTable": aaaUNPMacRuleTable,
       "aaaUNPMacRuleEntry": aaaUNPMacRuleEntry,
       "aaaUNPMacRuleAddr": aaaUNPMacRuleAddr,
       "aaaUNPMacRuleProfileName": aaaUNPMacRuleProfileName,
       "aaaUNPMacRuleRowStatus": aaaUNPMacRuleRowStatus,
       "aaaUNPMacRangeRuleTable": aaaUNPMacRangeRuleTable,
       "aaaUNPMacRangeRuleEntry": aaaUNPMacRangeRuleEntry,
       "aaaUNPMacRangeRuleLoAddr": aaaUNPMacRangeRuleLoAddr,
       "aaaUNPMacRangeRuleHiAddr": aaaUNPMacRangeRuleHiAddr,
       "aaaUNPMacRangeRuleProfileName": aaaUNPMacRangeRuleProfileName,
       "aaaUNPMacRangeRuleRowStatus": aaaUNPMacRangeRuleRowStatus,
       "alcatelIND1AAAMIBConformance": alcatelIND1AAAMIBConformance,
       "alcatelIND1AAAMIBGroups": alcatelIND1AAAMIBGroups,
       "aaaServerMIBGroup": aaaServerMIBGroup,
       "aaaAuthAcctGroup": aaaAuthAcctGroup,
       "aaaUserMIBGroup": aaaUserMIBGroup,
       "aaaHicGroup": aaaHicGroup,
       "aaaTrapsGroup": aaaTrapsGroup,
       "alcatelIND1AAAMIBCompliances": alcatelIND1AAAMIBCompliances,
       "alcatelIND1AAAMIBCompliance": alcatelIND1AAAMIBCompliance,
       "alaAaaTrapsDesc": alaAaaTrapsDesc,
       "alaAaaTrapsDescRoot": alaAaaTrapsDescRoot,
       "aaaHicServerTrap": aaaHicServerTrap,
       "alaAaaTrapsObj": alaAaaTrapsObj,
       "aaaHSvrIpAddress": aaaHSvrIpAddress}
)
