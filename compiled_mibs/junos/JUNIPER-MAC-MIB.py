# SNMP MIB module (JUNIPER-MAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-MAC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:58 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxMac = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23)
)
if mibBuilder.loadTexts:
    jnxMac.setRevisions(
        ("2002-10-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxVlanIndex(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_JnxMacStats_ObjectIdentity = ObjectIdentity
jnxMacStats = _JnxMacStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1)
)
_JnxMacStatsTable_Object = MibTable
jnxMacStatsTable = _JnxMacStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1)
)
if mibBuilder.loadTexts:
    jnxMacStatsTable.setStatus("current")
_JnxMacStatsEntry_Object = MibTableRow
jnxMacStatsEntry = _JnxMacStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1)
)
jnxMacStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-MAC-MIB", "jnxVlanIndex"),
    (0, "JUNIPER-MAC-MIB", "jnxSourceMacAddress"),
)
if mibBuilder.loadTexts:
    jnxMacStatsEntry.setStatus("current")
_JnxVlanIndex_Type = JnxVlanIndex
_JnxVlanIndex_Object = MibTableColumn
jnxVlanIndex = _JnxVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 1),
    _JnxVlanIndex_Type()
)
jnxVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVlanIndex.setStatus("current")
_JnxSourceMacAddress_Type = MacAddress
_JnxSourceMacAddress_Object = MibTableColumn
jnxSourceMacAddress = _JnxSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 2),
    _JnxSourceMacAddress_Type()
)
jnxSourceMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSourceMacAddress.setStatus("current")
_JnxMacHCInOctets_Type = Counter64
_JnxMacHCInOctets_Object = MibTableColumn
jnxMacHCInOctets = _JnxMacHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 3),
    _JnxMacHCInOctets_Type()
)
jnxMacHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacHCInOctets.setStatus("current")
_JnxMacHCInFrames_Type = Counter64
_JnxMacHCInFrames_Object = MibTableColumn
jnxMacHCInFrames = _JnxMacHCInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 4),
    _JnxMacHCInFrames_Type()
)
jnxMacHCInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacHCInFrames.setStatus("current")
_JnxMacHCOutOctets_Type = Counter64
_JnxMacHCOutOctets_Object = MibTableColumn
jnxMacHCOutOctets = _JnxMacHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 5),
    _JnxMacHCOutOctets_Type()
)
jnxMacHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacHCOutOctets.setStatus("current")
_JnxMacHCOutFrames_Type = Counter64
_JnxMacHCOutFrames_Object = MibTableColumn
jnxMacHCOutFrames = _JnxMacHCOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 6),
    _JnxMacHCOutFrames_Type()
)
jnxMacHCOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMacHCOutFrames.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MAC-MIB",
    **{"JnxVlanIndex": JnxVlanIndex,
       "jnxMac": jnxMac,
       "jnxMacStats": jnxMacStats,
       "jnxMacStatsTable": jnxMacStatsTable,
       "jnxMacStatsEntry": jnxMacStatsEntry,
       "jnxVlanIndex": jnxVlanIndex,
       "jnxSourceMacAddress": jnxSourceMacAddress,
       "jnxMacHCInOctets": jnxMacHCInOctets,
       "jnxMacHCInFrames": jnxMacHCInFrames,
       "jnxMacHCOutOctets": jnxMacHCOutOctets,
       "jnxMacHCOutFrames": jnxMacHCOutFrames}
)
