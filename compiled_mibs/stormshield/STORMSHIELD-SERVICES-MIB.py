# SNMP MIB module (STORMSHIELD-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-SERVICES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:14 2025
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

snsServices = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 7)
)
if mibBuilder.loadTexts:
    snsServices.setRevisions(
        ("2017-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsServicesTable_Object = MibTable
snsServicesTable = _SnsServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 7, 1)
)
if mibBuilder.loadTexts:
    snsServicesTable.setStatus("current")
_SnsServicesEntry_Object = MibTableRow
snsServicesEntry = _SnsServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 7, 1, 1)
)
snsServicesEntry.setIndexNames(
    (0, "STORMSHIELD-SERVICES-MIB", "snsServicesIndex"),
)
if mibBuilder.loadTexts:
    snsServicesEntry.setStatus("current")


class _SnsServicesIndex_Type(Integer32):
    """Custom type snsServicesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnsServicesIndex_Type.__name__ = "Integer32"
_SnsServicesIndex_Object = MibTableColumn
snsServicesIndex = _SnsServicesIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 7, 1, 1, 1),
    _SnsServicesIndex_Type()
)
snsServicesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsServicesIndex.setStatus("current")
_SnsServicesName_Type = SnmpAdminString
_SnsServicesName_Object = MibTableColumn
snsServicesName = _SnsServicesName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 7, 1, 1, 2),
    _SnsServicesName_Type()
)
snsServicesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsServicesName.setStatus("current")
_SnsServicesState_Type = Integer32
_SnsServicesState_Object = MibTableColumn
snsServicesState = _SnsServicesState_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 7, 1, 1, 3),
    _SnsServicesState_Type()
)
snsServicesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsServicesState.setStatus("current")
_SnsServicesUptime_Type = Integer32
_SnsServicesUptime_Object = MibTableColumn
snsServicesUptime = _SnsServicesUptime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 7, 1, 1, 4),
    _SnsServicesUptime_Type()
)
snsServicesUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsServicesUptime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-SERVICES-MIB",
    **{"snsServices": snsServices,
       "snsServicesTable": snsServicesTable,
       "snsServicesEntry": snsServicesEntry,
       "snsServicesIndex": snsServicesIndex,
       "snsServicesName": snsServicesName,
       "snsServicesState": snsServicesState,
       "snsServicesUptime": snsServicesUptime}
)
