# SNMP MIB module (JUNIPER-DCU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-DCU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:04 2025
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

jnxDCUs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6)
)
if mibBuilder.loadTexts:
    jnxDCUs.setRevisions(
        ("2002-12-17 00:00",
         "2002-02-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxDCUsTable_Object = MibTable
jnxDCUsTable = _JnxDCUsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6, 1)
)
if mibBuilder.loadTexts:
    jnxDCUsTable.setStatus("deprecated")
_JnxDCUsEntry_Object = MibTableRow
jnxDCUsEntry = _JnxDCUsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6, 1, 1)
)
jnxDCUsEntry.setIndexNames(
    (0, "JUNIPER-DCU-MIB", "jnxDCUSrcIfIndex"),
    (0, "JUNIPER-DCU-MIB", "jnxDCUDstClassName"),
)
if mibBuilder.loadTexts:
    jnxDCUsEntry.setStatus("deprecated")
_JnxDCUSrcIfIndex_Type = InterfaceIndex
_JnxDCUSrcIfIndex_Object = MibTableColumn
jnxDCUSrcIfIndex = _JnxDCUSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6, 1, 1, 1),
    _JnxDCUSrcIfIndex_Type()
)
jnxDCUSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDCUSrcIfIndex.setStatus("deprecated")


class _JnxDCUDstClassName_Type(DisplayString):
    """Custom type jnxDCUDstClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_JnxDCUDstClassName_Type.__name__ = "DisplayString"
_JnxDCUDstClassName_Object = MibTableColumn
jnxDCUDstClassName = _JnxDCUDstClassName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6, 1, 1, 2),
    _JnxDCUDstClassName_Type()
)
jnxDCUDstClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDCUDstClassName.setStatus("deprecated")
_JnxDCUPackets_Type = Counter64
_JnxDCUPackets_Object = MibTableColumn
jnxDCUPackets = _JnxDCUPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6, 1, 1, 3),
    _JnxDCUPackets_Type()
)
jnxDCUPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDCUPackets.setStatus("deprecated")
_JnxDCUBytes_Type = Counter64
_JnxDCUBytes_Object = MibTableColumn
jnxDCUBytes = _JnxDCUBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6, 1, 1, 4),
    _JnxDCUBytes_Type()
)
jnxDCUBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDCUBytes.setStatus("deprecated")
_JnxDcuStatsTable_Object = MibTable
jnxDcuStatsTable = _JnxDcuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6, 2)
)
if mibBuilder.loadTexts:
    jnxDcuStatsTable.setStatus("current")
_JnxDcuStatsEntry_Object = MibTableRow
jnxDcuStatsEntry = _JnxDcuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6, 2, 1)
)
jnxDcuStatsEntry.setIndexNames(
    (0, "JUNIPER-DCU-MIB", "jnxDcuStatsSrcIfIndex"),
    (0, "JUNIPER-DCU-MIB", "jnxDcuStatsAddrFamily"),
    (0, "JUNIPER-DCU-MIB", "jnxDcuStatsClassName"),
)
if mibBuilder.loadTexts:
    jnxDcuStatsEntry.setStatus("current")
_JnxDcuStatsSrcIfIndex_Type = InterfaceIndex
_JnxDcuStatsSrcIfIndex_Object = MibTableColumn
jnxDcuStatsSrcIfIndex = _JnxDcuStatsSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6, 2, 1, 1),
    _JnxDcuStatsSrcIfIndex_Type()
)
jnxDcuStatsSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxDcuStatsSrcIfIndex.setStatus("current")


class _JnxDcuStatsAddrFamily_Type(Integer32):
    """Custom type jnxDcuStatsAddrFamily based on Integer32"""
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


_JnxDcuStatsAddrFamily_Type.__name__ = "Integer32"
_JnxDcuStatsAddrFamily_Object = MibTableColumn
jnxDcuStatsAddrFamily = _JnxDcuStatsAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6, 2, 1, 2),
    _JnxDcuStatsAddrFamily_Type()
)
jnxDcuStatsAddrFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxDcuStatsAddrFamily.setStatus("current")


class _JnxDcuStatsClassName_Type(SnmpAdminString):
    """Custom type jnxDcuStatsClassName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 112),
    )


_JnxDcuStatsClassName_Type.__name__ = "SnmpAdminString"
_JnxDcuStatsClassName_Object = MibTableColumn
jnxDcuStatsClassName = _JnxDcuStatsClassName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6, 2, 1, 3),
    _JnxDcuStatsClassName_Type()
)
jnxDcuStatsClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxDcuStatsClassName.setStatus("current")
_JnxDcuStatsPackets_Type = Counter64
_JnxDcuStatsPackets_Object = MibTableColumn
jnxDcuStatsPackets = _JnxDcuStatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6, 2, 1, 4),
    _JnxDcuStatsPackets_Type()
)
jnxDcuStatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDcuStatsPackets.setStatus("current")
_JnxDcuStatsBytes_Type = Counter64
_JnxDcuStatsBytes_Object = MibTableColumn
jnxDcuStatsBytes = _JnxDcuStatsBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6, 2, 1, 5),
    _JnxDcuStatsBytes_Type()
)
jnxDcuStatsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDcuStatsBytes.setStatus("current")


class _JnxDcuStatsClName_Type(SnmpAdminString):
    """Custom type jnxDcuStatsClName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 112),
    )


_JnxDcuStatsClName_Type.__name__ = "SnmpAdminString"
_JnxDcuStatsClName_Object = MibTableColumn
jnxDcuStatsClName = _JnxDcuStatsClName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 6, 2, 1, 6),
    _JnxDcuStatsClName_Type()
)
jnxDcuStatsClName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDcuStatsClName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-DCU-MIB",
    **{"jnxDCUs": jnxDCUs,
       "jnxDCUsTable": jnxDCUsTable,
       "jnxDCUsEntry": jnxDCUsEntry,
       "jnxDCUSrcIfIndex": jnxDCUSrcIfIndex,
       "jnxDCUDstClassName": jnxDCUDstClassName,
       "jnxDCUPackets": jnxDCUPackets,
       "jnxDCUBytes": jnxDCUBytes,
       "jnxDcuStatsTable": jnxDcuStatsTable,
       "jnxDcuStatsEntry": jnxDcuStatsEntry,
       "jnxDcuStatsSrcIfIndex": jnxDcuStatsSrcIfIndex,
       "jnxDcuStatsAddrFamily": jnxDcuStatsAddrFamily,
       "jnxDcuStatsClassName": jnxDcuStatsClassName,
       "jnxDcuStatsPackets": jnxDcuStatsPackets,
       "jnxDcuStatsBytes": jnxDcuStatsBytes,
       "jnxDcuStatsClName": jnxDcuStatsClName}
)
