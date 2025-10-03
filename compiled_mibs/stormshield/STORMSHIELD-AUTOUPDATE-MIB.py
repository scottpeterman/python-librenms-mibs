# SNMP MIB module (STORMSHIELD-AUTOUPDATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-AUTOUPDATE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:03 2025
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

snsAutoupdate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 9)
)
if mibBuilder.loadTexts:
    snsAutoupdate.setRevisions(
        ("2017-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsAutoupdateTable_Object = MibTable
snsAutoupdateTable = _SnsAutoupdateTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 9, 1)
)
if mibBuilder.loadTexts:
    snsAutoupdateTable.setStatus("current")
_SnsAutoupdateEntry_Object = MibTableRow
snsAutoupdateEntry = _SnsAutoupdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1)
)
snsAutoupdateEntry.setIndexNames(
    (0, "STORMSHIELD-AUTOUPDATE-MIB", "snsAutoupdateIndex"),
)
if mibBuilder.loadTexts:
    snsAutoupdateEntry.setStatus("current")


class _SnsAutoupdateIndex_Type(Integer32):
    """Custom type snsAutoupdateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnsAutoupdateIndex_Type.__name__ = "Integer32"
_SnsAutoupdateIndex_Object = MibTableColumn
snsAutoupdateIndex = _SnsAutoupdateIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1, 1),
    _SnsAutoupdateIndex_Type()
)
snsAutoupdateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAutoupdateIndex.setStatus("current")
_SnsAutoupdateSubsys_Type = SnmpAdminString
_SnsAutoupdateSubsys_Object = MibTableColumn
snsAutoupdateSubsys = _SnsAutoupdateSubsys_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1, 2),
    _SnsAutoupdateSubsys_Type()
)
snsAutoupdateSubsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAutoupdateSubsys.setStatus("current")
_SnsAutoupdateState_Type = DisplayString
_SnsAutoupdateState_Object = MibTableColumn
snsAutoupdateState = _SnsAutoupdateState_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1, 3),
    _SnsAutoupdateState_Type()
)
snsAutoupdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAutoupdateState.setStatus("current")
_SnsAutoupdateLast_Type = DisplayString
_SnsAutoupdateLast_Object = MibTableColumn
snsAutoupdateLast = _SnsAutoupdateLast_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1, 4),
    _SnsAutoupdateLast_Type()
)
snsAutoupdateLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsAutoupdateLast.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-AUTOUPDATE-MIB",
    **{"snsAutoupdate": snsAutoupdate,
       "snsAutoupdateTable": snsAutoupdateTable,
       "snsAutoupdateEntry": snsAutoupdateEntry,
       "snsAutoupdateIndex": snsAutoupdateIndex,
       "snsAutoupdateSubsys": snsAutoupdateSubsys,
       "snsAutoupdateState": snsAutoupdateState,
       "snsAutoupdateLast": snsAutoupdateLast}
)
