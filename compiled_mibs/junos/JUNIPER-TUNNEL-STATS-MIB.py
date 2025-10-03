# SNMP MIB module (JUNIPER-TUNNEL-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-TUNNEL-STATS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:04:57 2025
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

(jnxTunnelStatsMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxTunnelStatsMibRoot")

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

jnxTunnelStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 84, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxTunnelStatsObjects_ObjectIdentity = ObjectIdentity
jnxTunnelStatsObjects = _JnxTunnelStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 84, 1, 1)
)
_JnxTunnelStatsTable_Object = MibTable
jnxTunnelStatsTable = _JnxTunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 84, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxTunnelStatsTable.setStatus("current")
_JnxTunnelStatsEntry_Object = MibTableRow
jnxTunnelStatsEntry = _JnxTunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 84, 1, 1, 1, 1)
)
jnxTunnelStatsEntry.setIndexNames(
    (0, "JUNIPER-TUNNEL-STATS-MIB", "jnxTunnelType"),
)
if mibBuilder.loadTexts:
    jnxTunnelStatsEntry.setStatus("current")


class _JnxTunnelType_Type(Integer32):
    """Custom type jnxTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("v4ov6", 1)
    )


_JnxTunnelType_Type.__name__ = "Integer32"
_JnxTunnelType_Object = MibTableColumn
jnxTunnelType = _JnxTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 84, 1, 1, 1, 1, 1),
    _JnxTunnelType_Type()
)
jnxTunnelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTunnelType.setStatus("current")
_JnxTunnelCount_Type = Integer32
_JnxTunnelCount_Object = MibTableColumn
jnxTunnelCount = _JnxTunnelCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 84, 1, 1, 1, 1, 2),
    _JnxTunnelCount_Type()
)
jnxTunnelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTunnelCount.setStatus("current")
_JnxTunnelCountInKernel_Type = Integer32
_JnxTunnelCountInKernel_Object = MibTableColumn
jnxTunnelCountInKernel = _JnxTunnelCountInKernel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 84, 1, 1, 1, 1, 3),
    _JnxTunnelCountInKernel_Type()
)
jnxTunnelCountInKernel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTunnelCountInKernel.setStatus("current")
_JnxTunnelCountInPfe_Type = Integer32
_JnxTunnelCountInPfe_Object = MibTableColumn
jnxTunnelCountInPfe = _JnxTunnelCountInPfe_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 84, 1, 1, 1, 1, 4),
    _JnxTunnelCountInPfe_Type()
)
jnxTunnelCountInPfe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTunnelCountInPfe.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-TUNNEL-STATS-MIB",
    **{"jnxTunnelStatsMIB": jnxTunnelStatsMIB,
       "jnxTunnelStatsObjects": jnxTunnelStatsObjects,
       "jnxTunnelStatsTable": jnxTunnelStatsTable,
       "jnxTunnelStatsEntry": jnxTunnelStatsEntry,
       "jnxTunnelType": jnxTunnelType,
       "jnxTunnelCount": jnxTunnelCount,
       "jnxTunnelCountInKernel": jnxTunnelCountInKernel,
       "jnxTunnelCountInPfe": jnxTunnelCountInPfe}
)
