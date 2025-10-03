# SNMP MIB module (PPP-IP-NCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\PPP-IP-NCP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:08:05 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ppp,) = mibBuilder.importSymbols(
    "PPP-LCP-MIB",
    "ppp")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PppIp_ObjectIdentity = ObjectIdentity
pppIp = _PppIp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23, 3)
)
_PppIpTable_Object = MibTable
pppIpTable = _PppIpTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 3, 1)
)
if mibBuilder.loadTexts:
    pppIpTable.setStatus("mandatory")
_PppIpEntry_Object = MibTableRow
pppIpEntry = _PppIpEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1)
)
pppIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppIpEntry.setStatus("mandatory")


class _PppIpOperStatus_Type(Integer32):
    """Custom type pppIpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opened", 1),
          ("not-opened", 2))
    )


_PppIpOperStatus_Type.__name__ = "Integer32"
_PppIpOperStatus_Object = MibTableColumn
pppIpOperStatus = _PppIpOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 1),
    _PppIpOperStatus_Type()
)
pppIpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpOperStatus.setStatus("mandatory")


class _PppIpLocalToRemoteCompressionProtocol_Type(Integer32):
    """Custom type pppIpLocalToRemoteCompressionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vj-tcp", 2))
    )


_PppIpLocalToRemoteCompressionProtocol_Type.__name__ = "Integer32"
_PppIpLocalToRemoteCompressionProtocol_Object = MibTableColumn
pppIpLocalToRemoteCompressionProtocol = _PppIpLocalToRemoteCompressionProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 2),
    _PppIpLocalToRemoteCompressionProtocol_Type()
)
pppIpLocalToRemoteCompressionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpLocalToRemoteCompressionProtocol.setStatus("mandatory")


class _PppIpRemoteToLocalCompressionProtocol_Type(Integer32):
    """Custom type pppIpRemoteToLocalCompressionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vj-tcp", 2))
    )


_PppIpRemoteToLocalCompressionProtocol_Type.__name__ = "Integer32"
_PppIpRemoteToLocalCompressionProtocol_Object = MibTableColumn
pppIpRemoteToLocalCompressionProtocol = _PppIpRemoteToLocalCompressionProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 3),
    _PppIpRemoteToLocalCompressionProtocol_Type()
)
pppIpRemoteToLocalCompressionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpRemoteToLocalCompressionProtocol.setStatus("mandatory")


class _PppIpRemoteMaxSlotId_Type(Integer32):
    """Custom type pppIpRemoteMaxSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PppIpRemoteMaxSlotId_Type.__name__ = "Integer32"
_PppIpRemoteMaxSlotId_Object = MibTableColumn
pppIpRemoteMaxSlotId = _PppIpRemoteMaxSlotId_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 4),
    _PppIpRemoteMaxSlotId_Type()
)
pppIpRemoteMaxSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpRemoteMaxSlotId.setStatus("mandatory")


class _PppIpLocalMaxSlotId_Type(Integer32):
    """Custom type pppIpLocalMaxSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PppIpLocalMaxSlotId_Type.__name__ = "Integer32"
_PppIpLocalMaxSlotId_Object = MibTableColumn
pppIpLocalMaxSlotId = _PppIpLocalMaxSlotId_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 3, 1, 1, 5),
    _PppIpLocalMaxSlotId_Type()
)
pppIpLocalMaxSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIpLocalMaxSlotId.setStatus("mandatory")
_PppIpConfigTable_Object = MibTable
pppIpConfigTable = _PppIpConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 3, 2)
)
if mibBuilder.loadTexts:
    pppIpConfigTable.setStatus("mandatory")
_PppIpConfigEntry_Object = MibTableRow
pppIpConfigEntry = _PppIpConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 3, 2, 1)
)
pppIpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppIpConfigEntry.setStatus("mandatory")


class _PppIpConfigAdminStatus_Type(Integer32):
    """Custom type pppIpConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_PppIpConfigAdminStatus_Type.__name__ = "Integer32"
_PppIpConfigAdminStatus_Object = MibTableColumn
pppIpConfigAdminStatus = _PppIpConfigAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 3, 2, 1, 1),
    _PppIpConfigAdminStatus_Type()
)
pppIpConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppIpConfigAdminStatus.setStatus("mandatory")


class _PppIpConfigCompression_Type(Integer32):
    """Custom type pppIpConfigCompression based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vj-tcp", 2))
    )


_PppIpConfigCompression_Type.__name__ = "Integer32"
_PppIpConfigCompression_Object = MibTableColumn
pppIpConfigCompression = _PppIpConfigCompression_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 3, 2, 1, 2),
    _PppIpConfigCompression_Type()
)
pppIpConfigCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppIpConfigCompression.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PPP-IP-NCP-MIB",
    **{"pppIp": pppIp,
       "pppIpTable": pppIpTable,
       "pppIpEntry": pppIpEntry,
       "pppIpOperStatus": pppIpOperStatus,
       "pppIpLocalToRemoteCompressionProtocol": pppIpLocalToRemoteCompressionProtocol,
       "pppIpRemoteToLocalCompressionProtocol": pppIpRemoteToLocalCompressionProtocol,
       "pppIpRemoteMaxSlotId": pppIpRemoteMaxSlotId,
       "pppIpLocalMaxSlotId": pppIpLocalMaxSlotId,
       "pppIpConfigTable": pppIpConfigTable,
       "pppIpConfigEntry": pppIpConfigEntry,
       "pppIpConfigAdminStatus": pppIpConfigAdminStatus,
       "pppIpConfigCompression": pppIpConfigCompression}
)
