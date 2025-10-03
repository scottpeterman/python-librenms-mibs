# SNMP MIB module (TN-PROV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-PROV-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:14 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnProvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 110)
)
if mibBuilder.loadTexts:
    tnProvMIB.setRevisions(
        ("2012-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnProvObjects_ObjectIdentity = ObjectIdentity
tnProvObjects = _TnProvObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 110, 1)
)
_TnProvGroup_ObjectIdentity = ObjectIdentity
tnProvGroup = _TnProvGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 110, 1, 1)
)
_TnProvTable_Object = MibTable
tnProvTable = _TnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 110, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnProvTable.setStatus("current")
_TnProvEntry_Object = MibTableRow
tnProvEntry = _TnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 110, 1, 1, 1, 1)
)
tnProvEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnProvEntry.setStatus("current")


class _TnProvType_Type(Integer32):
    """Custom type tnProvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("restore", 2),
          ("saveStartupConfig", 3),
          ("activate", 4),
          ("delete", 5))
    )


_TnProvType_Type.__name__ = "Integer32"
_TnProvType_Object = MibTableColumn
tnProvType = _TnProvType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 110, 1, 1, 1, 1, 1),
    _TnProvType_Type()
)
tnProvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnProvType.setStatus("current")
_TnProvAddrType_Type = InetAddressType
_TnProvAddrType_Object = MibTableColumn
tnProvAddrType = _TnProvAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 110, 1, 1, 1, 1, 2),
    _TnProvAddrType_Type()
)
tnProvAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnProvAddrType.setStatus("current")
_TnProvAddr_Type = InetAddress
_TnProvAddr_Object = MibTableColumn
tnProvAddr = _TnProvAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 110, 1, 1, 1, 1, 3),
    _TnProvAddr_Type()
)
tnProvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnProvAddr.setStatus("current")
_TnProvFile_Type = DisplayString
_TnProvFile_Object = MibTableColumn
tnProvFile = _TnProvFile_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 110, 1, 1, 1, 1, 4),
    _TnProvFile_Type()
)
tnProvFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnProvFile.setStatus("current")


class _TnProvOper_Type(Integer32):
    """Custom type tnProvOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("doNothing", 2))
    )


_TnProvOper_Type.__name__ = "Integer32"
_TnProvOper_Object = MibTableColumn
tnProvOper = _TnProvOper_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 110, 1, 1, 1, 1, 5),
    _TnProvOper_Type()
)
tnProvOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnProvOper.setStatus("current")


class _TnProvResult_Type(Integer32):
    """Custom type tnProvResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("fail", 2),
          ("inProgress", 3))
    )


_TnProvResult_Type.__name__ = "Integer32"
_TnProvResult_Object = MibTableColumn
tnProvResult = _TnProvResult_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 110, 1, 1, 1, 1, 6),
    _TnProvResult_Type()
)
tnProvResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnProvResult.setStatus("current")
_TnProvDstFile_Type = DisplayString
_TnProvDstFile_Object = MibTableColumn
tnProvDstFile = _TnProvDstFile_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 110, 1, 1, 1, 1, 7),
    _TnProvDstFile_Type()
)
tnProvDstFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnProvDstFile.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-PROV-MIB",
    **{"tnProvMIB": tnProvMIB,
       "tnProvObjects": tnProvObjects,
       "tnProvGroup": tnProvGroup,
       "tnProvTable": tnProvTable,
       "tnProvEntry": tnProvEntry,
       "tnProvType": tnProvType,
       "tnProvAddrType": tnProvAddrType,
       "tnProvAddr": tnProvAddr,
       "tnProvFile": tnProvFile,
       "tnProvOper": tnProvOper,
       "tnProvResult": tnProvResult,
       "tnProvDstFile": tnProvDstFile}
)
