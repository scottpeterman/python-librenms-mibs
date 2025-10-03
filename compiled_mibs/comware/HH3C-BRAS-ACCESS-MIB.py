# SNMP MIB module (HH3C-BRAS-ACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-BRAS-ACCESS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:51 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cBrasAcc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200)
)
if mibBuilder.loadTexts:
    hh3cBrasAcc.setRevisions(
        ("2020-11-10 09:27",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cBrasAccTotalStat_ObjectIdentity = ObjectIdentity
hh3cBrasAccTotalStat = _Hh3cBrasAccTotalStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 1)
)
_Hh3cBrasAccTotalUserNum_Type = Integer32
_Hh3cBrasAccTotalUserNum_Object = MibScalar
hh3cBrasAccTotalUserNum = _Hh3cBrasAccTotalUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 1, 1),
    _Hh3cBrasAccTotalUserNum_Type()
)
hh3cBrasAccTotalUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccTotalUserNum.setStatus("current")
_Hh3cBrasAccTotalPPPoEUserNum_Type = Integer32
_Hh3cBrasAccTotalPPPoEUserNum_Object = MibScalar
hh3cBrasAccTotalPPPoEUserNum = _Hh3cBrasAccTotalPPPoEUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 1, 2),
    _Hh3cBrasAccTotalPPPoEUserNum_Type()
)
hh3cBrasAccTotalPPPoEUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccTotalPPPoEUserNum.setStatus("current")
_Hh3cBrasAccTotalIPoEUserNum_Type = Integer32
_Hh3cBrasAccTotalIPoEUserNum_Object = MibScalar
hh3cBrasAccTotalIPoEUserNum = _Hh3cBrasAccTotalIPoEUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 1, 3),
    _Hh3cBrasAccTotalIPoEUserNum_Type()
)
hh3cBrasAccTotalIPoEUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccTotalIPoEUserNum.setStatus("current")
_Hh3cBrasAccTotalLNSUserNum_Type = Integer32
_Hh3cBrasAccTotalLNSUserNum_Object = MibScalar
hh3cBrasAccTotalLNSUserNum = _Hh3cBrasAccTotalLNSUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 1, 4),
    _Hh3cBrasAccTotalLNSUserNum_Type()
)
hh3cBrasAccTotalLNSUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccTotalLNSUserNum.setStatus("current")
_Hh3cBrasAccTotalLACUserNum_Type = Integer32
_Hh3cBrasAccTotalLACUserNum_Object = MibScalar
hh3cBrasAccTotalLACUserNum = _Hh3cBrasAccTotalLACUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 1, 5),
    _Hh3cBrasAccTotalLACUserNum_Type()
)
hh3cBrasAccTotalLACUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccTotalLACUserNum.setStatus("current")
_Hh3cBrasAccTotalIPv4UserNum_Type = Integer32
_Hh3cBrasAccTotalIPv4UserNum_Object = MibScalar
hh3cBrasAccTotalIPv4UserNum = _Hh3cBrasAccTotalIPv4UserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 1, 6),
    _Hh3cBrasAccTotalIPv4UserNum_Type()
)
hh3cBrasAccTotalIPv4UserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccTotalIPv4UserNum.setStatus("current")
_Hh3cBrasAccTotalIPv6UserNum_Type = Integer32
_Hh3cBrasAccTotalIPv6UserNum_Object = MibScalar
hh3cBrasAccTotalIPv6UserNum = _Hh3cBrasAccTotalIPv6UserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 1, 7),
    _Hh3cBrasAccTotalIPv6UserNum_Type()
)
hh3cBrasAccTotalIPv6UserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccTotalIPv6UserNum.setStatus("current")
_Hh3cBrasAccTotalDSUserNum_Type = Integer32
_Hh3cBrasAccTotalDSUserNum_Object = MibScalar
hh3cBrasAccTotalDSUserNum = _Hh3cBrasAccTotalDSUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 1, 8),
    _Hh3cBrasAccTotalDSUserNum_Type()
)
hh3cBrasAccTotalDSUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccTotalDSUserNum.setStatus("current")
_Hh3cBrasAccUPStatTable_Object = MibTable
hh3cBrasAccUPStatTable = _Hh3cBrasAccUPStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 2)
)
if mibBuilder.loadTexts:
    hh3cBrasAccUPStatTable.setStatus("current")
_Hh3cBrasAccUPStatEntry_Object = MibTableRow
hh3cBrasAccUPStatEntry = _Hh3cBrasAccUPStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 2, 1)
)
hh3cBrasAccUPStatEntry.setIndexNames(
    (0, "HH3C-BRAS-ACCESS-MIB", "hh3cBrasAccUPID"),
)
if mibBuilder.loadTexts:
    hh3cBrasAccUPStatEntry.setStatus("current")


class _Hh3cBrasAccUPID_Type(Integer32):
    """Custom type hh3cBrasAccUPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 2047),
    )


_Hh3cBrasAccUPID_Type.__name__ = "Integer32"
_Hh3cBrasAccUPID_Object = MibTableColumn
hh3cBrasAccUPID = _Hh3cBrasAccUPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 2, 1, 1),
    _Hh3cBrasAccUPID_Type()
)
hh3cBrasAccUPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBrasAccUPID.setStatus("current")
_Hh3cBrasAccUPUserNum_Type = Integer32
_Hh3cBrasAccUPUserNum_Object = MibTableColumn
hh3cBrasAccUPUserNum = _Hh3cBrasAccUPUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 2, 1, 2),
    _Hh3cBrasAccUPUserNum_Type()
)
hh3cBrasAccUPUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPUserNum.setStatus("current")
_Hh3cBrasAccUPPPPoEUserNum_Type = Integer32
_Hh3cBrasAccUPPPPoEUserNum_Object = MibTableColumn
hh3cBrasAccUPPPPoEUserNum = _Hh3cBrasAccUPPPPoEUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 2, 1, 3),
    _Hh3cBrasAccUPPPPoEUserNum_Type()
)
hh3cBrasAccUPPPPoEUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPPPPoEUserNum.setStatus("current")
_Hh3cBrasAccUPIPoEUserNum_Type = Integer32
_Hh3cBrasAccUPIPoEUserNum_Object = MibTableColumn
hh3cBrasAccUPIPoEUserNum = _Hh3cBrasAccUPIPoEUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 2, 1, 4),
    _Hh3cBrasAccUPIPoEUserNum_Type()
)
hh3cBrasAccUPIPoEUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPIPoEUserNum.setStatus("current")
_Hh3cBrasAccUPLNSUserNum_Type = Integer32
_Hh3cBrasAccUPLNSUserNum_Object = MibTableColumn
hh3cBrasAccUPLNSUserNum = _Hh3cBrasAccUPLNSUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 2, 1, 5),
    _Hh3cBrasAccUPLNSUserNum_Type()
)
hh3cBrasAccUPLNSUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPLNSUserNum.setStatus("current")
_Hh3cBrasAccUPLACUserNum_Type = Integer32
_Hh3cBrasAccUPLACUserNum_Object = MibTableColumn
hh3cBrasAccUPLACUserNum = _Hh3cBrasAccUPLACUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 2, 1, 6),
    _Hh3cBrasAccUPLACUserNum_Type()
)
hh3cBrasAccUPLACUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPLACUserNum.setStatus("current")
_Hh3cBrasAccUPIPv4UserNum_Type = Integer32
_Hh3cBrasAccUPIPv4UserNum_Object = MibTableColumn
hh3cBrasAccUPIPv4UserNum = _Hh3cBrasAccUPIPv4UserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 2, 1, 7),
    _Hh3cBrasAccUPIPv4UserNum_Type()
)
hh3cBrasAccUPIPv4UserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPIPv4UserNum.setStatus("current")
_Hh3cBrasAccUPIPv6UserNum_Type = Integer32
_Hh3cBrasAccUPIPv6UserNum_Object = MibTableColumn
hh3cBrasAccUPIPv6UserNum = _Hh3cBrasAccUPIPv6UserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 2, 1, 8),
    _Hh3cBrasAccUPIPv6UserNum_Type()
)
hh3cBrasAccUPIPv6UserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPIPv6UserNum.setStatus("current")
_Hh3cBrasAccUPDSUserNum_Type = Integer32
_Hh3cBrasAccUPDSUserNum_Object = MibTableColumn
hh3cBrasAccUPDSUserNum = _Hh3cBrasAccUPDSUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 2, 1, 9),
    _Hh3cBrasAccUPDSUserNum_Type()
)
hh3cBrasAccUPDSUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPDSUserNum.setStatus("current")
_Hh3cBrasAccUPSlotStatTable_Object = MibTable
hh3cBrasAccUPSlotStatTable = _Hh3cBrasAccUPSlotStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 3)
)
if mibBuilder.loadTexts:
    hh3cBrasAccUPSlotStatTable.setStatus("current")
_Hh3cBrasAccUPSlotStatEntry_Object = MibTableRow
hh3cBrasAccUPSlotStatEntry = _Hh3cBrasAccUPSlotStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 3, 1)
)
hh3cBrasAccUPSlotStatEntry.setIndexNames(
    (0, "HH3C-BRAS-ACCESS-MIB", "hh3cBrasAccUPSlotUPID"),
    (0, "HH3C-BRAS-ACCESS-MIB", "hh3cBrasAccUPSlotID"),
)
if mibBuilder.loadTexts:
    hh3cBrasAccUPSlotStatEntry.setStatus("current")


class _Hh3cBrasAccUPSlotUPID_Type(Integer32):
    """Custom type hh3cBrasAccUPSlotUPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 2047),
    )


_Hh3cBrasAccUPSlotUPID_Type.__name__ = "Integer32"
_Hh3cBrasAccUPSlotUPID_Object = MibTableColumn
hh3cBrasAccUPSlotUPID = _Hh3cBrasAccUPSlotUPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 3, 1, 1),
    _Hh3cBrasAccUPSlotUPID_Type()
)
hh3cBrasAccUPSlotUPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBrasAccUPSlotUPID.setStatus("current")


class _Hh3cBrasAccUPSlotID_Type(Integer32):
    """Custom type hh3cBrasAccUPSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cBrasAccUPSlotID_Type.__name__ = "Integer32"
_Hh3cBrasAccUPSlotID_Object = MibTableColumn
hh3cBrasAccUPSlotID = _Hh3cBrasAccUPSlotID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 3, 1, 2),
    _Hh3cBrasAccUPSlotID_Type()
)
hh3cBrasAccUPSlotID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBrasAccUPSlotID.setStatus("current")
_Hh3cBrasAccUPSlotUserNum_Type = Integer32
_Hh3cBrasAccUPSlotUserNum_Object = MibTableColumn
hh3cBrasAccUPSlotUserNum = _Hh3cBrasAccUPSlotUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 3, 1, 3),
    _Hh3cBrasAccUPSlotUserNum_Type()
)
hh3cBrasAccUPSlotUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPSlotUserNum.setStatus("current")
_Hh3cBrasAccUPSlotPPPoEUserNum_Type = Integer32
_Hh3cBrasAccUPSlotPPPoEUserNum_Object = MibTableColumn
hh3cBrasAccUPSlotPPPoEUserNum = _Hh3cBrasAccUPSlotPPPoEUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 3, 1, 4),
    _Hh3cBrasAccUPSlotPPPoEUserNum_Type()
)
hh3cBrasAccUPSlotPPPoEUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPSlotPPPoEUserNum.setStatus("current")
_Hh3cBrasAccUPSlotIPoEUserNum_Type = Integer32
_Hh3cBrasAccUPSlotIPoEUserNum_Object = MibTableColumn
hh3cBrasAccUPSlotIPoEUserNum = _Hh3cBrasAccUPSlotIPoEUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 3, 1, 5),
    _Hh3cBrasAccUPSlotIPoEUserNum_Type()
)
hh3cBrasAccUPSlotIPoEUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPSlotIPoEUserNum.setStatus("current")
_Hh3cBrasAccUPSlotLNSUserNum_Type = Integer32
_Hh3cBrasAccUPSlotLNSUserNum_Object = MibTableColumn
hh3cBrasAccUPSlotLNSUserNum = _Hh3cBrasAccUPSlotLNSUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 3, 1, 6),
    _Hh3cBrasAccUPSlotLNSUserNum_Type()
)
hh3cBrasAccUPSlotLNSUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPSlotLNSUserNum.setStatus("current")
_Hh3cBrasAccUPSlotLACUserNum_Type = Integer32
_Hh3cBrasAccUPSlotLACUserNum_Object = MibTableColumn
hh3cBrasAccUPSlotLACUserNum = _Hh3cBrasAccUPSlotLACUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 3, 1, 7),
    _Hh3cBrasAccUPSlotLACUserNum_Type()
)
hh3cBrasAccUPSlotLACUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPSlotLACUserNum.setStatus("current")
_Hh3cBrasAccUPSlotIPv4UserNum_Type = Integer32
_Hh3cBrasAccUPSlotIPv4UserNum_Object = MibTableColumn
hh3cBrasAccUPSlotIPv4UserNum = _Hh3cBrasAccUPSlotIPv4UserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 3, 1, 8),
    _Hh3cBrasAccUPSlotIPv4UserNum_Type()
)
hh3cBrasAccUPSlotIPv4UserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPSlotIPv4UserNum.setStatus("current")
_Hh3cBrasAccUPSlotIPv6UserNum_Type = Integer32
_Hh3cBrasAccUPSlotIPv6UserNum_Object = MibTableColumn
hh3cBrasAccUPSlotIPv6UserNum = _Hh3cBrasAccUPSlotIPv6UserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 3, 1, 9),
    _Hh3cBrasAccUPSlotIPv6UserNum_Type()
)
hh3cBrasAccUPSlotIPv6UserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPSlotIPv6UserNum.setStatus("current")
_Hh3cBrasAccUPSlotDSUserNum_Type = Integer32
_Hh3cBrasAccUPSlotDSUserNum_Object = MibTableColumn
hh3cBrasAccUPSlotDSUserNum = _Hh3cBrasAccUPSlotDSUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 3, 1, 10),
    _Hh3cBrasAccUPSlotDSUserNum_Type()
)
hh3cBrasAccUPSlotDSUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccUPSlotDSUserNum.setStatus("current")
_Hh3cBrasAccIfStatTable_Object = MibTable
hh3cBrasAccIfStatTable = _Hh3cBrasAccIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 4)
)
if mibBuilder.loadTexts:
    hh3cBrasAccIfStatTable.setStatus("current")
_Hh3cBrasAccIfStatEntry_Object = MibTableRow
hh3cBrasAccIfStatEntry = _Hh3cBrasAccIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 4, 1)
)
hh3cBrasAccIfStatEntry.setIndexNames(
    (0, "HH3C-BRAS-ACCESS-MIB", "hh3cBrasAccIfName"),
)
if mibBuilder.loadTexts:
    hh3cBrasAccIfStatEntry.setStatus("current")


class _Hh3cBrasAccIfName_Type(DisplayString):
    """Custom type hh3cBrasAccIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cBrasAccIfName_Type.__name__ = "DisplayString"
_Hh3cBrasAccIfName_Object = MibTableColumn
hh3cBrasAccIfName = _Hh3cBrasAccIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 4, 1, 1),
    _Hh3cBrasAccIfName_Type()
)
hh3cBrasAccIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccIfName.setStatus("current")
_Hh3cBrasAccIfUserNum_Type = Integer32
_Hh3cBrasAccIfUserNum_Object = MibTableColumn
hh3cBrasAccIfUserNum = _Hh3cBrasAccIfUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 4, 1, 2),
    _Hh3cBrasAccIfUserNum_Type()
)
hh3cBrasAccIfUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccIfUserNum.setStatus("current")
_Hh3cBrasAccIfPPPoEUserNum_Type = Integer32
_Hh3cBrasAccIfPPPoEUserNum_Object = MibTableColumn
hh3cBrasAccIfPPPoEUserNum = _Hh3cBrasAccIfPPPoEUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 4, 1, 3),
    _Hh3cBrasAccIfPPPoEUserNum_Type()
)
hh3cBrasAccIfPPPoEUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccIfPPPoEUserNum.setStatus("current")
_Hh3cBrasAccIfIPoEUserNum_Type = Integer32
_Hh3cBrasAccIfIPoEUserNum_Object = MibTableColumn
hh3cBrasAccIfIPoEUserNum = _Hh3cBrasAccIfIPoEUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 4, 1, 4),
    _Hh3cBrasAccIfIPoEUserNum_Type()
)
hh3cBrasAccIfIPoEUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccIfIPoEUserNum.setStatus("current")
_Hh3cBrasAccIfLNSUserNum_Type = Integer32
_Hh3cBrasAccIfLNSUserNum_Object = MibTableColumn
hh3cBrasAccIfLNSUserNum = _Hh3cBrasAccIfLNSUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 4, 1, 5),
    _Hh3cBrasAccIfLNSUserNum_Type()
)
hh3cBrasAccIfLNSUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccIfLNSUserNum.setStatus("current")
_Hh3cBrasAccIfLACUserNum_Type = Integer32
_Hh3cBrasAccIfLACUserNum_Object = MibTableColumn
hh3cBrasAccIfLACUserNum = _Hh3cBrasAccIfLACUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 4, 1, 6),
    _Hh3cBrasAccIfLACUserNum_Type()
)
hh3cBrasAccIfLACUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccIfLACUserNum.setStatus("current")
_Hh3cBrasAccIfIPv4UserNum_Type = Integer32
_Hh3cBrasAccIfIPv4UserNum_Object = MibTableColumn
hh3cBrasAccIfIPv4UserNum = _Hh3cBrasAccIfIPv4UserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 4, 1, 7),
    _Hh3cBrasAccIfIPv4UserNum_Type()
)
hh3cBrasAccIfIPv4UserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccIfIPv4UserNum.setStatus("current")
_Hh3cBrasAccIfIPv6UserNum_Type = Integer32
_Hh3cBrasAccIfIPv6UserNum_Object = MibTableColumn
hh3cBrasAccIfIPv6UserNum = _Hh3cBrasAccIfIPv6UserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 4, 1, 8),
    _Hh3cBrasAccIfIPv6UserNum_Type()
)
hh3cBrasAccIfIPv6UserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccIfIPv6UserNum.setStatus("current")
_Hh3cBrasAccIfDSUserNum_Type = Integer32
_Hh3cBrasAccIfDSUserNum_Object = MibTableColumn
hh3cBrasAccIfDSUserNum = _Hh3cBrasAccIfDSUserNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 4, 1, 9),
    _Hh3cBrasAccIfDSUserNum_Type()
)
hh3cBrasAccIfDSUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBrasAccIfDSUserNum.setStatus("current")
_Hh3cBrasAccCUMibTrapOid_ObjectIdentity = ObjectIdentity
hh3cBrasAccCUMibTrapOid = _Hh3cBrasAccCUMibTrapOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 5)
)
_Hh3cBrasAccCUTrapUPID_Type = Integer32
_Hh3cBrasAccCUTrapUPID_Object = MibScalar
hh3cBrasAccCUTrapUPID = _Hh3cBrasAccCUTrapUPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 5, 1),
    _Hh3cBrasAccCUTrapUPID_Type()
)
hh3cBrasAccCUTrapUPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cBrasAccCUTrapUPID.setStatus("current")
_Hh3cBrasAccCUTrapSlotID_Type = Integer32
_Hh3cBrasAccCUTrapSlotID_Object = MibScalar
hh3cBrasAccCUTrapSlotID = _Hh3cBrasAccCUTrapSlotID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 5, 2),
    _Hh3cBrasAccCUTrapSlotID_Type()
)
hh3cBrasAccCUTrapSlotID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cBrasAccCUTrapSlotID.setStatus("current")
_Hh3cBrasAccCUTrapThreshold_Type = Integer32
_Hh3cBrasAccCUTrapThreshold_Object = MibScalar
hh3cBrasAccCUTrapThreshold = _Hh3cBrasAccCUTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 5, 3),
    _Hh3cBrasAccCUTrapThreshold_Type()
)
hh3cBrasAccCUTrapThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cBrasAccCUTrapThreshold.setStatus("current")
_Hh3cBrasAccCUTrap_ObjectIdentity = ObjectIdentity
hh3cBrasAccCUTrap = _Hh3cBrasAccCUTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 6)
)
_Hh3cBrasAccCUTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cBrasAccCUTrapPrefix = _Hh3cBrasAccCUTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 6, 0)
)

# Managed Objects groups


# Notification objects

hh3cBrasAccCUUPWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 6, 0, 1)
)
hh3cBrasAccCUUPWarning.setObjects(
      *(("HH3C-BRAS-ACCESS-MIB", "hh3cBrasAccCUTrapUPID"),
        ("HH3C-BRAS-ACCESS-MIB", "hh3cBrasAccCUTrapThreshold"))
)
if mibBuilder.loadTexts:
    hh3cBrasAccCUUPWarning.setStatus(
        "current"
    )

hh3cBrasAccCUUPWarningResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 6, 0, 2)
)
hh3cBrasAccCUUPWarningResume.setObjects(
      *(("HH3C-BRAS-ACCESS-MIB", "hh3cBrasAccCUTrapUPID"),
        ("HH3C-BRAS-ACCESS-MIB", "hh3cBrasAccCUTrapThreshold"))
)
if mibBuilder.loadTexts:
    hh3cBrasAccCUUPWarningResume.setStatus(
        "current"
    )

hh3cBrasAccCUSlotWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 6, 0, 3)
)
hh3cBrasAccCUSlotWarning.setObjects(
      *(("HH3C-BRAS-ACCESS-MIB", "hh3cBrasAccCUTrapUPID"),
        ("HH3C-BRAS-ACCESS-MIB", "hh3cBrasAccCUTrapSlotID"),
        ("HH3C-BRAS-ACCESS-MIB", "hh3cBrasAccCUTrapThreshold"))
)
if mibBuilder.loadTexts:
    hh3cBrasAccCUSlotWarning.setStatus(
        "current"
    )

hh3cBrasAccCUSlotWarningResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 200, 6, 0, 4)
)
hh3cBrasAccCUSlotWarningResume.setObjects(
      *(("HH3C-BRAS-ACCESS-MIB", "hh3cBrasAccCUTrapUPID"),
        ("HH3C-BRAS-ACCESS-MIB", "hh3cBrasAccCUTrapSlotID"),
        ("HH3C-BRAS-ACCESS-MIB", "hh3cBrasAccCUTrapThreshold"))
)
if mibBuilder.loadTexts:
    hh3cBrasAccCUSlotWarningResume.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-BRAS-ACCESS-MIB",
    **{"hh3cBrasAcc": hh3cBrasAcc,
       "hh3cBrasAccTotalStat": hh3cBrasAccTotalStat,
       "hh3cBrasAccTotalUserNum": hh3cBrasAccTotalUserNum,
       "hh3cBrasAccTotalPPPoEUserNum": hh3cBrasAccTotalPPPoEUserNum,
       "hh3cBrasAccTotalIPoEUserNum": hh3cBrasAccTotalIPoEUserNum,
       "hh3cBrasAccTotalLNSUserNum": hh3cBrasAccTotalLNSUserNum,
       "hh3cBrasAccTotalLACUserNum": hh3cBrasAccTotalLACUserNum,
       "hh3cBrasAccTotalIPv4UserNum": hh3cBrasAccTotalIPv4UserNum,
       "hh3cBrasAccTotalIPv6UserNum": hh3cBrasAccTotalIPv6UserNum,
       "hh3cBrasAccTotalDSUserNum": hh3cBrasAccTotalDSUserNum,
       "hh3cBrasAccUPStatTable": hh3cBrasAccUPStatTable,
       "hh3cBrasAccUPStatEntry": hh3cBrasAccUPStatEntry,
       "hh3cBrasAccUPID": hh3cBrasAccUPID,
       "hh3cBrasAccUPUserNum": hh3cBrasAccUPUserNum,
       "hh3cBrasAccUPPPPoEUserNum": hh3cBrasAccUPPPPoEUserNum,
       "hh3cBrasAccUPIPoEUserNum": hh3cBrasAccUPIPoEUserNum,
       "hh3cBrasAccUPLNSUserNum": hh3cBrasAccUPLNSUserNum,
       "hh3cBrasAccUPLACUserNum": hh3cBrasAccUPLACUserNum,
       "hh3cBrasAccUPIPv4UserNum": hh3cBrasAccUPIPv4UserNum,
       "hh3cBrasAccUPIPv6UserNum": hh3cBrasAccUPIPv6UserNum,
       "hh3cBrasAccUPDSUserNum": hh3cBrasAccUPDSUserNum,
       "hh3cBrasAccUPSlotStatTable": hh3cBrasAccUPSlotStatTable,
       "hh3cBrasAccUPSlotStatEntry": hh3cBrasAccUPSlotStatEntry,
       "hh3cBrasAccUPSlotUPID": hh3cBrasAccUPSlotUPID,
       "hh3cBrasAccUPSlotID": hh3cBrasAccUPSlotID,
       "hh3cBrasAccUPSlotUserNum": hh3cBrasAccUPSlotUserNum,
       "hh3cBrasAccUPSlotPPPoEUserNum": hh3cBrasAccUPSlotPPPoEUserNum,
       "hh3cBrasAccUPSlotIPoEUserNum": hh3cBrasAccUPSlotIPoEUserNum,
       "hh3cBrasAccUPSlotLNSUserNum": hh3cBrasAccUPSlotLNSUserNum,
       "hh3cBrasAccUPSlotLACUserNum": hh3cBrasAccUPSlotLACUserNum,
       "hh3cBrasAccUPSlotIPv4UserNum": hh3cBrasAccUPSlotIPv4UserNum,
       "hh3cBrasAccUPSlotIPv6UserNum": hh3cBrasAccUPSlotIPv6UserNum,
       "hh3cBrasAccUPSlotDSUserNum": hh3cBrasAccUPSlotDSUserNum,
       "hh3cBrasAccIfStatTable": hh3cBrasAccIfStatTable,
       "hh3cBrasAccIfStatEntry": hh3cBrasAccIfStatEntry,
       "hh3cBrasAccIfName": hh3cBrasAccIfName,
       "hh3cBrasAccIfUserNum": hh3cBrasAccIfUserNum,
       "hh3cBrasAccIfPPPoEUserNum": hh3cBrasAccIfPPPoEUserNum,
       "hh3cBrasAccIfIPoEUserNum": hh3cBrasAccIfIPoEUserNum,
       "hh3cBrasAccIfLNSUserNum": hh3cBrasAccIfLNSUserNum,
       "hh3cBrasAccIfLACUserNum": hh3cBrasAccIfLACUserNum,
       "hh3cBrasAccIfIPv4UserNum": hh3cBrasAccIfIPv4UserNum,
       "hh3cBrasAccIfIPv6UserNum": hh3cBrasAccIfIPv6UserNum,
       "hh3cBrasAccIfDSUserNum": hh3cBrasAccIfDSUserNum,
       "hh3cBrasAccCUMibTrapOid": hh3cBrasAccCUMibTrapOid,
       "hh3cBrasAccCUTrapUPID": hh3cBrasAccCUTrapUPID,
       "hh3cBrasAccCUTrapSlotID": hh3cBrasAccCUTrapSlotID,
       "hh3cBrasAccCUTrapThreshold": hh3cBrasAccCUTrapThreshold,
       "hh3cBrasAccCUTrap": hh3cBrasAccCUTrap,
       "hh3cBrasAccCUTrapPrefix": hh3cBrasAccCUTrapPrefix,
       "hh3cBrasAccCUUPWarning": hh3cBrasAccCUUPWarning,
       "hh3cBrasAccCUUPWarningResume": hh3cBrasAccCUUPWarningResume,
       "hh3cBrasAccCUSlotWarning": hh3cBrasAccCUSlotWarning,
       "hh3cBrasAccCUSlotWarningResume": hh3cBrasAccCUSlotWarningResume}
)
