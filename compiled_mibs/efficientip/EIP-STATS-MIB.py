# SNMP MIB module (EIP-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\efficientip\EIP-STATS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:11 2025
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

_Eip_ObjectIdentity = ObjectIdentity
eip = _Eip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1)
)
_EipDhcp_ObjectIdentity = ObjectIdentity
eipDhcp = _EipDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 3)
)
_EipDhcpStat_ObjectIdentity = ObjectIdentity
eipDhcpStat = _EipDhcpStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 3, 2)
)
_EipDhcpStatTable_Object = MibTable
eipDhcpStatTable = _EipDhcpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22)
)
if mibBuilder.loadTexts:
    eipDhcpStatTable.setStatus("mandatory")
_EipDhcpStatEntry_Object = MibTableRow
eipDhcpStatEntry = _EipDhcpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22, 1)
)
eipDhcpStatEntry.setIndexNames(
    (0, "EIP-STATS-MIB", "eipDhcpStatName"),
)
if mibBuilder.loadTexts:
    eipDhcpStatEntry.setStatus("mandatory")


class _EipDhcpStatIndex_Type(DisplayString):
    """Custom type eipDhcpStatIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EipDhcpStatIndex_Type.__name__ = "DisplayString"
_EipDhcpStatIndex_Object = MibTableColumn
eipDhcpStatIndex = _EipDhcpStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22, 1, 1),
    _EipDhcpStatIndex_Type()
)
eipDhcpStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDhcpStatIndex.setStatus("mandatory")


class _EipDhcpStatName_Type(DisplayString):
    """Custom type eipDhcpStatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EipDhcpStatName_Type.__name__ = "DisplayString"
_EipDhcpStatName_Object = MibTableColumn
eipDhcpStatName = _EipDhcpStatName_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22, 1, 2),
    _EipDhcpStatName_Type()
)
eipDhcpStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDhcpStatName.setStatus("mandatory")
_EipDhcpStatValue_Type = Integer32
_EipDhcpStatValue_Object = MibTableColumn
eipDhcpStatValue = _EipDhcpStatValue_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22, 1, 3),
    _EipDhcpStatValue_Type()
)
eipDhcpStatValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDhcpStatValue.setStatus("mandatory")
_EipDns_ObjectIdentity = ObjectIdentity
eipDns = _EipDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 4)
)
_EipDnsStat_ObjectIdentity = ObjectIdentity
eipDnsStat = _EipDnsStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 4, 2)
)
_EipDnsStatTable_Object = MibTable
eipDnsStatTable = _EipDnsStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    eipDnsStatTable.setStatus("mandatory")
_EipDnsStatEntry_Object = MibTableRow
eipDnsStatEntry = _EipDnsStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3, 1)
)
eipDnsStatEntry.setIndexNames(
    (0, "EIP-STATS-MIB", "eipDnsStatName"),
)
if mibBuilder.loadTexts:
    eipDnsStatEntry.setStatus("mandatory")


class _EipDnsStatIndex_Type(DisplayString):
    """Custom type eipDnsStatIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EipDnsStatIndex_Type.__name__ = "DisplayString"
_EipDnsStatIndex_Object = MibTableColumn
eipDnsStatIndex = _EipDnsStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3, 1, 1),
    _EipDnsStatIndex_Type()
)
eipDnsStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDnsStatIndex.setStatus("mandatory")


class _EipDnsStatName_Type(DisplayString):
    """Custom type eipDnsStatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EipDnsStatName_Type.__name__ = "DisplayString"
_EipDnsStatName_Object = MibTableColumn
eipDnsStatName = _EipDnsStatName_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3, 1, 2),
    _EipDnsStatName_Type()
)
eipDnsStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDnsStatName.setStatus("mandatory")
_EipDnsStatValue_Type = Integer32
_EipDnsStatValue_Object = MibTableColumn
eipDnsStatValue = _EipDnsStatValue_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3, 1, 3),
    _EipDnsStatValue_Type()
)
eipDnsStatValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDnsStatValue.setStatus("mandatory")
_EipDhcp6_ObjectIdentity = ObjectIdentity
eipDhcp6 = _EipDhcp6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 7)
)
_EipDhcp6Stat_ObjectIdentity = ObjectIdentity
eipDhcp6Stat = _EipDhcp6Stat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 7, 1)
)
_EipDhcp6StatTable_Object = MibTable
eipDhcp6StatTable = _EipDhcp6StatTable_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    eipDhcp6StatTable.setStatus("mandatory")
_EipDhcp6StatEntry_Object = MibTableRow
eipDhcp6StatEntry = _EipDhcp6StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1, 1)
)
eipDhcp6StatEntry.setIndexNames(
    (0, "EIP-STATS-MIB", "eipDhcp6StatName"),
)
if mibBuilder.loadTexts:
    eipDhcp6StatEntry.setStatus("mandatory")


class _EipDhcp6StatIndex_Type(DisplayString):
    """Custom type eipDhcp6StatIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EipDhcp6StatIndex_Type.__name__ = "DisplayString"
_EipDhcp6StatIndex_Object = MibTableColumn
eipDhcp6StatIndex = _EipDhcp6StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1, 1, 1),
    _EipDhcp6StatIndex_Type()
)
eipDhcp6StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDhcp6StatIndex.setStatus("mandatory")


class _EipDhcp6StatName_Type(DisplayString):
    """Custom type eipDhcp6StatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EipDhcp6StatName_Type.__name__ = "DisplayString"
_EipDhcp6StatName_Object = MibTableColumn
eipDhcp6StatName = _EipDhcp6StatName_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1, 1, 2),
    _EipDhcp6StatName_Type()
)
eipDhcp6StatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDhcp6StatName.setStatus("mandatory")
_EipDhcp6StatValue_Type = Integer32
_EipDhcp6StatValue_Object = MibTableColumn
eipDhcp6StatValue = _EipDhcp6StatValue_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1, 1, 3),
    _EipDhcp6StatValue_Type()
)
eipDhcp6StatValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDhcp6StatValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EIP-STATS-MIB",
    **{"eip": eip,
       "products": products,
       "eipDhcp": eipDhcp,
       "eipDhcpStat": eipDhcpStat,
       "eipDhcpStatTable": eipDhcpStatTable,
       "eipDhcpStatEntry": eipDhcpStatEntry,
       "eipDhcpStatIndex": eipDhcpStatIndex,
       "eipDhcpStatName": eipDhcpStatName,
       "eipDhcpStatValue": eipDhcpStatValue,
       "eipDns": eipDns,
       "eipDnsStat": eipDnsStat,
       "eipDnsStatTable": eipDnsStatTable,
       "eipDnsStatEntry": eipDnsStatEntry,
       "eipDnsStatIndex": eipDnsStatIndex,
       "eipDnsStatName": eipDnsStatName,
       "eipDnsStatValue": eipDnsStatValue,
       "eipDhcp6": eipDhcp6,
       "eipDhcp6Stat": eipDhcp6Stat,
       "eipDhcp6StatTable": eipDhcp6StatTable,
       "eipDhcp6StatEntry": eipDhcp6StatEntry,
       "eipDhcp6StatIndex": eipDhcp6StatIndex,
       "eipDhcp6StatName": eipDhcp6StatName,
       "eipDhcp6StatValue": eipDhcp6StatValue}
)
