# SNMP MIB module (MERU-CONFIG-ICR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\MERU-CONFIG-ICR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:02 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigIcr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwIcrTable_Object = MibTable
mwIcrTable = _MwIcrTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1)
)
if mibBuilder.loadTexts:
    mwIcrTable.setStatus("current")
_MwIcrEntry_Object = MibTableRow
mwIcrEntry = _MwIcrEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1)
)
mwIcrEntry.setIndexNames(
    (0, "MERU-CONFIG-ICR-MIB", "mwIcrTableIndex"),
)
if mibBuilder.loadTexts:
    mwIcrEntry.setStatus("current")
_MwIcrTableIndex_Type = Integer32
_MwIcrTableIndex_Object = MibTableColumn
mwIcrTableIndex = _MwIcrTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1, 1),
    _MwIcrTableIndex_Type()
)
mwIcrTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwIcrTableIndex.setStatus("current")


class _MwIcrEssId_Type(DisplayString):
    """Custom type mwIcrEssId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MwIcrEssId_Type.__name__ = "DisplayString"
_MwIcrEssId_Object = MibTableColumn
mwIcrEssId = _MwIcrEssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1, 2),
    _MwIcrEssId_Type()
)
mwIcrEssId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwIcrEssId.setStatus("current")
_MwIcrControllerIp_Type = IpAddress
_MwIcrControllerIp_Object = MibTableColumn
mwIcrControllerIp = _MwIcrControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1, 3),
    _MwIcrControllerIp_Type()
)
mwIcrControllerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwIcrControllerIp.setStatus("current")
_MwIcrHomeDhcpIp_Type = IpAddress
_MwIcrHomeDhcpIp_Object = MibTableColumn
mwIcrHomeDhcpIp = _MwIcrHomeDhcpIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1, 4),
    _MwIcrHomeDhcpIp_Type()
)
mwIcrHomeDhcpIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwIcrHomeDhcpIp.setStatus("current")
_MwIcrRowStatus_Type = RowStatus
_MwIcrRowStatus_Object = MibTableColumn
mwIcrRowStatus = _MwIcrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1, 5),
    _MwIcrRowStatus_Type()
)
mwIcrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwIcrRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-ICR-MIB",
    **{"mwConfigIcr": mwConfigIcr,
       "mwIcrTable": mwIcrTable,
       "mwIcrEntry": mwIcrEntry,
       "mwIcrTableIndex": mwIcrTableIndex,
       "mwIcrEssId": mwIcrEssId,
       "mwIcrControllerIp": mwIcrControllerIp,
       "mwIcrHomeDhcpIp": mwIcrHomeDhcpIp,
       "mwIcrRowStatus": mwIcrRowStatus}
)
