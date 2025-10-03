# SNMP MIB module (AT-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\awplus\AT-IP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:29 2025
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

atIpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602)
)
if mibBuilder.loadTexts:
    atIpMib.setRevisions(
        ("2010-06-14 05:09",
         "2008-11-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AtIpAddressAssignmentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSet", 0),
          ("primary", 1),
          ("secondary", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AtIpAddressTable_Object = MibTable
atIpAddressTable = _AtIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1)
)
if mibBuilder.loadTexts:
    atIpAddressTable.setStatus("current")
_AtIpAddressEntry_Object = MibTableRow
atIpAddressEntry = _AtIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1)
)
atIpAddressEntry.setIndexNames(
    (0, "AT-IP-MIB", "atIpAddressAddrType"),
    (0, "AT-IP-MIB", "atIpAddressAddr"),
)
if mibBuilder.loadTexts:
    atIpAddressEntry.setStatus("current")
_AtIpAddressAddrType_Type = InetAddressType
_AtIpAddressAddrType_Object = MibTableColumn
atIpAddressAddrType = _AtIpAddressAddrType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 1),
    _AtIpAddressAddrType_Type()
)
atIpAddressAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atIpAddressAddrType.setStatus("current")
_AtIpAddressAddr_Type = InetAddress
_AtIpAddressAddr_Object = MibTableColumn
atIpAddressAddr = _AtIpAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 2),
    _AtIpAddressAddr_Type()
)
atIpAddressAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atIpAddressAddr.setStatus("current")
_AtIpAddressPrefixLen_Type = Integer32
_AtIpAddressPrefixLen_Object = MibTableColumn
atIpAddressPrefixLen = _AtIpAddressPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 3),
    _AtIpAddressPrefixLen_Type()
)
atIpAddressPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atIpAddressPrefixLen.setStatus("current")
_AtIpAddressLabel_Type = DisplayString
_AtIpAddressLabel_Object = MibTableColumn
atIpAddressLabel = _AtIpAddressLabel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 4),
    _AtIpAddressLabel_Type()
)
atIpAddressLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atIpAddressLabel.setStatus("current")
_AtIpAddressIfIndex_Type = InterfaceIndex
_AtIpAddressIfIndex_Object = MibTableColumn
atIpAddressIfIndex = _AtIpAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 5),
    _AtIpAddressIfIndex_Type()
)
atIpAddressIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atIpAddressIfIndex.setStatus("current")
_AtIpAddressAssignmentType_Type = AtIpAddressAssignmentType
_AtIpAddressAssignmentType_Object = MibTableColumn
atIpAddressAssignmentType = _AtIpAddressAssignmentType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 6),
    _AtIpAddressAssignmentType_Type()
)
atIpAddressAssignmentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atIpAddressAssignmentType.setStatus("current")
_AtIpAddressRowStatus_Type = RowStatus
_AtIpAddressRowStatus_Object = MibTableColumn
atIpAddressRowStatus = _AtIpAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 7),
    _AtIpAddressRowStatus_Type()
)
atIpAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atIpAddressRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-IP-MIB",
    **{"AtIpAddressAssignmentType": AtIpAddressAssignmentType,
       "atIpMib": atIpMib,
       "atIpAddressTable": atIpAddressTable,
       "atIpAddressEntry": atIpAddressEntry,
       "atIpAddressAddrType": atIpAddressAddrType,
       "atIpAddressAddr": atIpAddressAddr,
       "atIpAddressPrefixLen": atIpAddressPrefixLen,
       "atIpAddressLabel": atIpAddressLabel,
       "atIpAddressIfIndex": atIpAddressIfIndex,
       "atIpAddressAssignmentType": atIpAddressAssignmentType,
       "atIpAddressRowStatus": atIpAddressRowStatus}
)
