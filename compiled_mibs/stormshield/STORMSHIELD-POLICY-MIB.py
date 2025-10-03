# SNMP MIB module (STORMSHIELD-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-POLICY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:11 2025
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

(stormshieldMIB,) = mibBuilder.importSymbols(
    "STORMSHIELD-SMI-MIB",
    "stormshieldMIB")


# MODULE-IDENTITY

snsPolicy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 8)
)
if mibBuilder.loadTexts:
    snsPolicy.setRevisions(
        ("2017-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsPolicyTable_Object = MibTable
snsPolicyTable = _SnsPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 8, 1)
)
if mibBuilder.loadTexts:
    snsPolicyTable.setStatus("current")
_SnsPolicyEntry_Object = MibTableRow
snsPolicyEntry = _SnsPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 8, 1, 1)
)
snsPolicyEntry.setIndexNames(
    (0, "STORMSHIELD-POLICY-MIB", "snsPolicyIndex"),
)
if mibBuilder.loadTexts:
    snsPolicyEntry.setStatus("current")


class _SnsPolicyIndex_Type(Integer32):
    """Custom type snsPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnsPolicyIndex_Type.__name__ = "Integer32"
_SnsPolicyIndex_Object = MibTableColumn
snsPolicyIndex = _SnsPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 8, 1, 1, 1),
    _SnsPolicyIndex_Type()
)
snsPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsPolicyIndex.setStatus("current")
_SnsPolicyName_Type = SnmpAdminString
_SnsPolicyName_Object = MibTableColumn
snsPolicyName = _SnsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 8, 1, 1, 2),
    _SnsPolicyName_Type()
)
snsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsPolicyName.setStatus("current")
_SnsPolicySlotName_Type = SnmpAdminString
_SnsPolicySlotName_Object = MibTableColumn
snsPolicySlotName = _SnsPolicySlotName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 8, 1, 1, 3),
    _SnsPolicySlotName_Type()
)
snsPolicySlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsPolicySlotName.setStatus("current")
_SnsPolicyActive_Type = DisplayString
_SnsPolicyActive_Object = MibTableColumn
snsPolicyActive = _SnsPolicyActive_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 8, 1, 1, 4),
    _SnsPolicyActive_Type()
)
snsPolicyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsPolicyActive.setStatus("current")
_SnsPolicySync_Type = Integer32
_SnsPolicySync_Object = MibTableColumn
snsPolicySync = _SnsPolicySync_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 8, 1, 1, 5),
    _SnsPolicySync_Type()
)
snsPolicySync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsPolicySync.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-POLICY-MIB",
    **{"snsPolicy": snsPolicy,
       "snsPolicyTable": snsPolicyTable,
       "snsPolicyEntry": snsPolicyEntry,
       "snsPolicyIndex": snsPolicyIndex,
       "snsPolicyName": snsPolicyName,
       "snsPolicySlotName": snsPolicySlotName,
       "snsPolicyActive": snsPolicyActive,
       "snsPolicySync": snsPolicySync}
)
