# SNMP MIB module (NETSCREEN-SET-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\screenos\NETSCREEN-SET-DNS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:25:43 2025
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

(netscreenSetting,
 netscreenSettingMibModule) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenSetting",
    "netscreenSettingMibModule")

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

netscreenSetDnsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 0, 3)
)
if mibBuilder.loadTexts:
    netscreenSetDnsMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-10 00:00",
         "2001-09-28 00:00",
         "2001-05-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsSetDNS_ObjectIdentity = ObjectIdentity
nsSetDNS = _NsSetDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 3)
)
_NsConfigDnsPriSer_Type = IpAddress
_NsConfigDnsPriSer_Object = MibScalar
nsConfigDnsPriSer = _NsConfigDnsPriSer_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 3, 1),
    _NsConfigDnsPriSer_Type()
)
nsConfigDnsPriSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsConfigDnsPriSer.setStatus("current")
_NsConfigDnsSecSer_Type = IpAddress
_NsConfigDnsSecSer_Object = MibScalar
nsConfigDnsSecSer = _NsConfigDnsSecSer_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 3, 2),
    _NsConfigDnsSecSer_Type()
)
nsConfigDnsSecSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsConfigDnsSecSer.setStatus("current")


class _NsConfigDnsRefEnable_Type(Integer32):
    """Custom type nsConfigDnsRefEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsConfigDnsRefEnable_Type.__name__ = "Integer32"
_NsConfigDnsRefEnable_Object = MibScalar
nsConfigDnsRefEnable = _NsConfigDnsRefEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 3, 3),
    _NsConfigDnsRefEnable_Type()
)
nsConfigDnsRefEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsConfigDnsRefEnable.setStatus("current")


class _NsConfigDnsRefTime_Type(DisplayString):
    """Custom type nsConfigDnsRefTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_NsConfigDnsRefTime_Type.__name__ = "DisplayString"
_NsConfigDnsRefTime_Object = MibScalar
nsConfigDnsRefTime = _NsConfigDnsRefTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 3, 4),
    _NsConfigDnsRefTime_Type()
)
nsConfigDnsRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsConfigDnsRefTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SET-DNS-MIB",
    **{"netscreenSetDnsMibModule": netscreenSetDnsMibModule,
       "nsSetDNS": nsSetDNS,
       "nsConfigDnsPriSer": nsConfigDnsPriSer,
       "nsConfigDnsSecSer": nsConfigDnsSecSer,
       "nsConfigDnsRefEnable": nsConfigDnsRefEnable,
       "nsConfigDnsRefTime": nsConfigDnsRefTime}
)
