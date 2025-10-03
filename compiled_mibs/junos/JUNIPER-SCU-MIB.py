# SNMP MIB module (JUNIPER-SCU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-SCU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:04:41 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

jnxScu = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 16)
)
if mibBuilder.loadTexts:
    jnxScu.setRevisions(
        ("2002-02-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxScuStats_ObjectIdentity = ObjectIdentity
jnxScuStats = _JnxScuStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 16, 1)
)
_JnxScuStatsTable_Object = MibTable
jnxScuStatsTable = _JnxScuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1)
)
if mibBuilder.loadTexts:
    jnxScuStatsTable.setStatus("current")
_JnxScuStatsEntry_Object = MibTableRow
jnxScuStatsEntry = _JnxScuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1)
)
jnxScuStatsEntry.setIndexNames(
    (0, "JUNIPER-SCU-MIB", "jnxScuStatsDstIfIndex"),
    (0, "JUNIPER-SCU-MIB", "jnxScuStatsAddrFamily"),
    (0, "JUNIPER-SCU-MIB", "jnxScuStatsClassName"),
)
if mibBuilder.loadTexts:
    jnxScuStatsEntry.setStatus("current")
_JnxScuStatsDstIfIndex_Type = InterfaceIndex
_JnxScuStatsDstIfIndex_Object = MibTableColumn
jnxScuStatsDstIfIndex = _JnxScuStatsDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 1),
    _JnxScuStatsDstIfIndex_Type()
)
jnxScuStatsDstIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxScuStatsDstIfIndex.setStatus("current")


class _JnxScuStatsAddrFamily_Type(Integer32):
    """Custom type jnxScuStatsAddrFamily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_JnxScuStatsAddrFamily_Type.__name__ = "Integer32"
_JnxScuStatsAddrFamily_Object = MibTableColumn
jnxScuStatsAddrFamily = _JnxScuStatsAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 2),
    _JnxScuStatsAddrFamily_Type()
)
jnxScuStatsAddrFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxScuStatsAddrFamily.setStatus("current")


class _JnxScuStatsClassName_Type(SnmpAdminString):
    """Custom type jnxScuStatsClassName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 112),
    )


_JnxScuStatsClassName_Type.__name__ = "SnmpAdminString"
_JnxScuStatsClassName_Object = MibTableColumn
jnxScuStatsClassName = _JnxScuStatsClassName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 3),
    _JnxScuStatsClassName_Type()
)
jnxScuStatsClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxScuStatsClassName.setStatus("current")
_JnxScuStatsPackets_Type = Counter64
_JnxScuStatsPackets_Object = MibTableColumn
jnxScuStatsPackets = _JnxScuStatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 4),
    _JnxScuStatsPackets_Type()
)
jnxScuStatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxScuStatsPackets.setStatus("current")
_JnxScuStatsBytes_Type = Counter64
_JnxScuStatsBytes_Object = MibTableColumn
jnxScuStatsBytes = _JnxScuStatsBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 5),
    _JnxScuStatsBytes_Type()
)
jnxScuStatsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxScuStatsBytes.setStatus("current")


class _JnxScuStatsClName_Type(SnmpAdminString):
    """Custom type jnxScuStatsClName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 112),
    )


_JnxScuStatsClName_Type.__name__ = "SnmpAdminString"
_JnxScuStatsClName_Object = MibTableColumn
jnxScuStatsClName = _JnxScuStatsClName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 6),
    _JnxScuStatsClName_Type()
)
jnxScuStatsClName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxScuStatsClName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SCU-MIB",
    **{"jnxScu": jnxScu,
       "jnxScuStats": jnxScuStats,
       "jnxScuStatsTable": jnxScuStatsTable,
       "jnxScuStatsEntry": jnxScuStatsEntry,
       "jnxScuStatsDstIfIndex": jnxScuStatsDstIfIndex,
       "jnxScuStatsAddrFamily": jnxScuStatsAddrFamily,
       "jnxScuStatsClassName": jnxScuStatsClassName,
       "jnxScuStatsPackets": jnxScuStatsPackets,
       "jnxScuStatsBytes": jnxScuStatsBytes,
       "jnxScuStatsClName": jnxScuStatsClName}
)
