# SNMP MIB module (VPLS-LDP-DRAFT-01-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\VPLS-LDP-DRAFT-01-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:05:27 2025
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

(jnxExperiment,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxExperiment")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(jnxVplsConfigIndex,
 jnxVplsPwBindIndex) = mibBuilder.importSymbols(
    "VPLS-GENERIC-DRAFT-01-MIB",
    "jnxVplsConfigIndex",
    "jnxVplsPwBindIndex")


# MODULE-IDENTITY

jnxVplsLdpDraft01MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 9)
)
if mibBuilder.loadTexts:
    jnxVplsLdpDraft01MIB.setRevisions(
        ("2006-08-30 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxVplsLdpNotifications_ObjectIdentity = ObjectIdentity
jnxVplsLdpNotifications = _JnxVplsLdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 9, 0)
)
_JnxVplsLdpObjects_ObjectIdentity = ObjectIdentity
jnxVplsLdpObjects = _JnxVplsLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 9, 1)
)
_JnxVplsLdpConfigTable_Object = MibTable
jnxVplsLdpConfigTable = _JnxVplsLdpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 9, 1, 1)
)
if mibBuilder.loadTexts:
    jnxVplsLdpConfigTable.setStatus("current")
_JnxVplsLdpConfigEntry_Object = MibTableRow
jnxVplsLdpConfigEntry = _JnxVplsLdpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 9, 1, 1, 1)
)
jnxVplsLdpConfigEntry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"),
)
if mibBuilder.loadTexts:
    jnxVplsLdpConfigEntry.setStatus("current")


class _JnxVplsLdpConfigMacAddrWithdraw_Type(TruthValue):
    """Custom type jnxVplsLdpConfigMacAddrWithdraw based on TruthValue"""
    defaultValue = 1


_JnxVplsLdpConfigMacAddrWithdraw_Type.__name__ = "TruthValue"
_JnxVplsLdpConfigMacAddrWithdraw_Object = MibTableColumn
jnxVplsLdpConfigMacAddrWithdraw = _JnxVplsLdpConfigMacAddrWithdraw_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 9, 1, 1, 1, 1),
    _JnxVplsLdpConfigMacAddrWithdraw_Type()
)
jnxVplsLdpConfigMacAddrWithdraw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsLdpConfigMacAddrWithdraw.setStatus("current")
_JnxVplsLdpPwBindTable_Object = MibTable
jnxVplsLdpPwBindTable = _JnxVplsLdpPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 9, 1, 2)
)
if mibBuilder.loadTexts:
    jnxVplsLdpPwBindTable.setStatus("current")
_JnxVplsLdpPwBindEntry_Object = MibTableRow
jnxVplsLdpPwBindEntry = _JnxVplsLdpPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 9, 1, 2, 1)
)
jnxVplsLdpPwBindEntry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"),
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsPwBindIndex"),
)
if mibBuilder.loadTexts:
    jnxVplsLdpPwBindEntry.setStatus("current")


class _JnxVplsLdpPwBindMacAddressLimit_Type(Unsigned32):
    """Custom type jnxVplsLdpPwBindMacAddressLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxVplsLdpPwBindMacAddressLimit_Type.__name__ = "Unsigned32"
_JnxVplsLdpPwBindMacAddressLimit_Object = MibTableColumn
jnxVplsLdpPwBindMacAddressLimit = _JnxVplsLdpPwBindMacAddressLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 9, 1, 2, 1, 1),
    _JnxVplsLdpPwBindMacAddressLimit_Type()
)
jnxVplsLdpPwBindMacAddressLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsLdpPwBindMacAddressLimit.setStatus("current")
_JnxVplsLdpConformance_ObjectIdentity = ObjectIdentity
jnxVplsLdpConformance = _JnxVplsLdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 9, 2)
)

# Managed Objects groups


# Notification objects

jnxVplsLdpPwBindMacTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 9, 0, 1)
)
jnxVplsLdpPwBindMacTableFull.setObjects(
      *(("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsPwBindIndex"))
)
if mibBuilder.loadTexts:
    jnxVplsLdpPwBindMacTableFull.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VPLS-LDP-DRAFT-01-MIB",
    **{"jnxVplsLdpDraft01MIB": jnxVplsLdpDraft01MIB,
       "jnxVplsLdpNotifications": jnxVplsLdpNotifications,
       "jnxVplsLdpPwBindMacTableFull": jnxVplsLdpPwBindMacTableFull,
       "jnxVplsLdpObjects": jnxVplsLdpObjects,
       "jnxVplsLdpConfigTable": jnxVplsLdpConfigTable,
       "jnxVplsLdpConfigEntry": jnxVplsLdpConfigEntry,
       "jnxVplsLdpConfigMacAddrWithdraw": jnxVplsLdpConfigMacAddrWithdraw,
       "jnxVplsLdpPwBindTable": jnxVplsLdpPwBindTable,
       "jnxVplsLdpPwBindEntry": jnxVplsLdpPwBindEntry,
       "jnxVplsLdpPwBindMacAddressLimit": jnxVplsLdpPwBindMacAddressLimit,
       "jnxVplsLdpConformance": jnxVplsLdpConformance}
)
