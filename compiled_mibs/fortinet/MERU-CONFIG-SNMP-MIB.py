# SNMP MIB module (MERU-CONFIG-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\MERU-CONFIG-SNMP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:10 2025
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

mwConfigSnmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwWncTrapCommunityTable_Object = MibTable
mwWncTrapCommunityTable = _MwWncTrapCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2)
)
if mibBuilder.loadTexts:
    mwWncTrapCommunityTable.setStatus("current")
_MwWncTrapCommunityEntry_Object = MibTableRow
mwWncTrapCommunityEntry = _MwWncTrapCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1)
)
mwWncTrapCommunityEntry.setIndexNames(
    (0, "MERU-CONFIG-SNMP-MIB", "mwWncTrapCommunityTableIndex"),
)
if mibBuilder.loadTexts:
    mwWncTrapCommunityEntry.setStatus("current")
_MwWncTrapCommunityTableIndex_Type = Integer32
_MwWncTrapCommunityTableIndex_Object = MibTableColumn
mwWncTrapCommunityTableIndex = _MwWncTrapCommunityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 1),
    _MwWncTrapCommunityTableIndex_Type()
)
mwWncTrapCommunityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwWncTrapCommunityTableIndex.setStatus("current")


class _MwWncTrapCommunitypCommunityStr_Type(DisplayString):
    """Custom type mwWncTrapCommunitypCommunityStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwWncTrapCommunitypCommunityStr_Type.__name__ = "DisplayString"
_MwWncTrapCommunitypCommunityStr_Object = MibTableColumn
mwWncTrapCommunitypCommunityStr = _MwWncTrapCommunitypCommunityStr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 2),
    _MwWncTrapCommunitypCommunityStr_Type()
)
mwWncTrapCommunitypCommunityStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwWncTrapCommunitypCommunityStr.setStatus("current")
_MwWncTrapCommunityClientIpAddress_Type = IpAddress
_MwWncTrapCommunityClientIpAddress_Object = MibTableColumn
mwWncTrapCommunityClientIpAddress = _MwWncTrapCommunityClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 3),
    _MwWncTrapCommunityClientIpAddress_Type()
)
mwWncTrapCommunityClientIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwWncTrapCommunityClientIpAddress.setStatus("current")
_MwWncTrapCommunityRowStatus_Type = RowStatus
_MwWncTrapCommunityRowStatus_Object = MibTableColumn
mwWncTrapCommunityRowStatus = _MwWncTrapCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 4),
    _MwWncTrapCommunityRowStatus_Type()
)
mwWncTrapCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwWncTrapCommunityRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-SNMP-MIB",
    **{"mwConfigSnmp": mwConfigSnmp,
       "mwWncTrapCommunityTable": mwWncTrapCommunityTable,
       "mwWncTrapCommunityEntry": mwWncTrapCommunityEntry,
       "mwWncTrapCommunityTableIndex": mwWncTrapCommunityTableIndex,
       "mwWncTrapCommunitypCommunityStr": mwWncTrapCommunitypCommunityStr,
       "mwWncTrapCommunityClientIpAddress": mwWncTrapCommunityClientIpAddress,
       "mwWncTrapCommunityRowStatus": mwWncTrapCommunityRowStatus}
)
