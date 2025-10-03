# SNMP MIB module (TN-LLDP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-LLDP-EXT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:47 2025
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

(lldpPortConfigEntry,) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "lldpPortConfigEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnExtLldpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 137)
)
if mibBuilder.loadTexts:
    tnExtLldpMIB.setRevisions(
        ("2012-03-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnExtLldpMIBNotifications_ObjectIdentity = ObjectIdentity
tnExtLldpMIBNotifications = _TnExtLldpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 137, 1)
)
_TnExtLldpMgmtObjects_ObjectIdentity = ObjectIdentity
tnExtLldpMgmtObjects = _TnExtLldpMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 137, 2)
)
_TnLldpExtPortConfigTable_Object = MibTable
tnLldpExtPortConfigTable = _TnLldpExtPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 137, 2, 1)
)
if mibBuilder.loadTexts:
    tnLldpExtPortConfigTable.setStatus("current")
_TnLldpExtPortConfigEntry_Object = MibTableRow
tnLldpExtPortConfigEntry = _TnLldpExtPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 137, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnLldpExtPortConfigEntry.setStatus("current")


class _LldpPortConfigCdpAwareEnabled_Type(TruthValue):
    """Custom type lldpPortConfigCdpAwareEnabled based on TruthValue"""
    defaultValue = 2


_LldpPortConfigCdpAwareEnabled_Type.__name__ = "TruthValue"
_LldpPortConfigCdpAwareEnabled_Object = MibTableColumn
lldpPortConfigCdpAwareEnabled = _LldpPortConfigCdpAwareEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 137, 2, 1, 1, 1),
    _LldpPortConfigCdpAwareEnabled_Type()
)
lldpPortConfigCdpAwareEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpPortConfigCdpAwareEnabled.setStatus("current")
_TnExtLldpMIBConformance_ObjectIdentity = ObjectIdentity
tnExtLldpMIBConformance = _TnExtLldpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 137, 3)
)
lldpPortConfigEntry.registerAugmentions(
    ("TN-LLDP-EXT-MIB",
     "tnLldpExtPortConfigEntry")
)
tnLldpExtPortConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-LLDP-EXT-MIB",
    **{"tnExtLldpMIB": tnExtLldpMIB,
       "tnExtLldpMIBNotifications": tnExtLldpMIBNotifications,
       "tnExtLldpMgmtObjects": tnExtLldpMgmtObjects,
       "tnLldpExtPortConfigTable": tnLldpExtPortConfigTable,
       "tnLldpExtPortConfigEntry": tnLldpExtPortConfigEntry,
       "lldpPortConfigCdpAwareEnabled": lldpPortConfigCdpAwareEnabled,
       "tnExtLldpMIBConformance": tnExtLldpMIBConformance}
)
