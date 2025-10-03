# SNMP MIB module (NBS-JUMPER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mrv\NBS-JUMPER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:18 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(nbs,) = mibBuilder.importSymbols(
    "NBS-MIB",
    "nbs")

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

nbsJumperMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 210)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsJumperGrp_ObjectIdentity = ObjectIdentity
nbsJumperGrp = _NbsJumperGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 210, 1)
)
if mibBuilder.loadTexts:
    nbsJumperGrp.setStatus("current")
_NbsJumperTableSize_Type = Unsigned32
_NbsJumperTableSize_Object = MibScalar
nbsJumperTableSize = _NbsJumperTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 210, 1, 1),
    _NbsJumperTableSize_Type()
)
nbsJumperTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsJumperTableSize.setStatus("current")
_NbsJumperTable_Object = MibTable
nbsJumperTable = _NbsJumperTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 210, 1, 2)
)
if mibBuilder.loadTexts:
    nbsJumperTable.setStatus("current")
_NbsJumperEntry_Object = MibTableRow
nbsJumperEntry = _NbsJumperEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1)
)
nbsJumperEntry.setIndexNames(
    (0, "NBS-JUMPER-MIB", "nbsJumperIfIndex"),
    (0, "NBS-JUMPER-MIB", "nbsJumperIndex"),
)
if mibBuilder.loadTexts:
    nbsJumperEntry.setStatus("current")
_NbsJumperIfIndex_Type = InterfaceIndex
_NbsJumperIfIndex_Object = MibTableColumn
nbsJumperIfIndex = _NbsJumperIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 1),
    _NbsJumperIfIndex_Type()
)
nbsJumperIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsJumperIfIndex.setStatus("current")
_NbsJumperIndex_Type = Integer32
_NbsJumperIndex_Object = MibTableColumn
nbsJumperIndex = _NbsJumperIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 2),
    _NbsJumperIndex_Type()
)
nbsJumperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsJumperIndex.setStatus("current")


class _NbsJumperPosition_Type(Integer32):
    """Custom type nbsJumperPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsJumperPosition_Type.__name__ = "Integer32"
_NbsJumperPosition_Object = MibTableColumn
nbsJumperPosition = _NbsJumperPosition_Object(
    (1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 3),
    _NbsJumperPosition_Type()
)
nbsJumperPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsJumperPosition.setStatus("current")


class _NbsJumperInterpret_Type(DisplayString):
    """Custom type nbsJumperInterpret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsJumperInterpret_Type.__name__ = "DisplayString"
_NbsJumperInterpret_Object = MibTableColumn
nbsJumperInterpret = _NbsJumperInterpret_Object(
    (1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 4),
    _NbsJumperInterpret_Type()
)
nbsJumperInterpret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsJumperInterpret.setStatus("current")


class _NbsJumperSilkScreen_Type(DisplayString):
    """Custom type nbsJumperSilkScreen based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NbsJumperSilkScreen_Type.__name__ = "DisplayString"
_NbsJumperSilkScreen_Object = MibTableColumn
nbsJumperSilkScreen = _NbsJumperSilkScreen_Object(
    (1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 5),
    _NbsJumperSilkScreen_Type()
)
nbsJumperSilkScreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsJumperSilkScreen.setStatus("current")


class _NbsJumperDescription_Type(DisplayString):
    """Custom type nbsJumperDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsJumperDescription_Type.__name__ = "DisplayString"
_NbsJumperDescription_Object = MibTableColumn
nbsJumperDescription = _NbsJumperDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 6),
    _NbsJumperDescription_Type()
)
nbsJumperDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsJumperDescription.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-JUMPER-MIB",
    **{"nbsJumperMib": nbsJumperMib,
       "nbsJumperGrp": nbsJumperGrp,
       "nbsJumperTableSize": nbsJumperTableSize,
       "nbsJumperTable": nbsJumperTable,
       "nbsJumperEntry": nbsJumperEntry,
       "nbsJumperIfIndex": nbsJumperIfIndex,
       "nbsJumperIndex": nbsJumperIndex,
       "nbsJumperPosition": nbsJumperPosition,
       "nbsJumperInterpret": nbsJumperInterpret,
       "nbsJumperSilkScreen": nbsJumperSilkScreen,
       "nbsJumperDescription": nbsJumperDescription}
)
