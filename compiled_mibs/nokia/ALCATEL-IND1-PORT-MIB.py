# SNMP MIB module (ALCATEL-IND1-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-PORT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:58 2025
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

(cmmEsmDrvTraps,
 softentIND1Port) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "cmmEsmDrvTraps",
    "softentIND1Port")

(ifInErrors,
 ifIndex,
 ifOutErrors) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifInErrors",
    "ifIndex",
    "ifOutErrors")

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


# MODULE-IDENTITY

alcatelIND1PortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PortMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1PortNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1PortNotifications = _AlcatelIND1PortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 0)
)
_DdmNotifications_ObjectIdentity = ObjectIdentity
ddmNotifications = _DdmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 0, 1)
)
_EsmViolationNotifications_ObjectIdentity = ObjectIdentity
esmViolationNotifications = _EsmViolationNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 0, 2)
)
_AlcatelIND1PortMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1PortMIBObjects = _AlcatelIND1PortMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1)
)
_EsmConfTrap_ObjectIdentity = ObjectIdentity
esmConfTrap = _EsmConfTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 1)
)
_EsmDrvTrapDrops_Type = Integer32
_EsmDrvTrapDrops_Object = MibScalar
esmDrvTrapDrops = _EsmDrvTrapDrops_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 1, 1),
    _EsmDrvTrapDrops_Type()
)
esmDrvTrapDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmDrvTrapDrops.setStatus("current")
_PhysicalPort_ObjectIdentity = ObjectIdentity
physicalPort = _PhysicalPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2)
)
_EsmConfTable_Object = MibTable
esmConfTable = _EsmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    esmConfTable.setStatus("current")
_EsmConfEntry_Object = MibTableRow
esmConfEntry = _EsmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1)
)
esmConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    esmConfEntry.setStatus("current")
_EsmPortSlot_Type = Integer32
_EsmPortSlot_Object = MibTableColumn
esmPortSlot = _EsmPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 1),
    _EsmPortSlot_Type()
)
esmPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortSlot.setStatus("current")
_EsmPortIF_Type = Integer32
_EsmPortIF_Object = MibTableColumn
esmPortIF = _EsmPortIF_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 2),
    _EsmPortIF_Type()
)
esmPortIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortIF.setStatus("current")


class _EsmPortAutoSpeed_Type(Integer32):
    """Custom type esmPortAutoSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("speed100", 1),
          ("speed10", 2),
          ("speedAuto", 3),
          ("unknown", 4),
          ("speed1000", 5),
          ("speed10000", 6))
    )


_EsmPortAutoSpeed_Type.__name__ = "Integer32"
_EsmPortAutoSpeed_Object = MibTableColumn
esmPortAutoSpeed = _EsmPortAutoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 3),
    _EsmPortAutoSpeed_Type()
)
esmPortAutoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortAutoSpeed.setStatus("current")


class _EsmPortAutoDuplexMode_Type(Integer32):
    """Custom type esmPortAutoDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("autoDuplex", 3),
          ("unknown", 4))
    )


_EsmPortAutoDuplexMode_Type.__name__ = "Integer32"
_EsmPortAutoDuplexMode_Object = MibTableColumn
esmPortAutoDuplexMode = _EsmPortAutoDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 4),
    _EsmPortAutoDuplexMode_Type()
)
esmPortAutoDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortAutoDuplexMode.setStatus("current")


class _EsmPortCfgSpeed_Type(Integer32):
    """Custom type esmPortCfgSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("speed100", 1),
          ("speed10", 2),
          ("speedAuto", 3),
          ("speed1000", 5),
          ("speed10000", 6),
          ("speedMax100", 8),
          ("speedMax1000", 9))
    )


_EsmPortCfgSpeed_Type.__name__ = "Integer32"
_EsmPortCfgSpeed_Object = MibTableColumn
esmPortCfgSpeed = _EsmPortCfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 5),
    _EsmPortCfgSpeed_Type()
)
esmPortCfgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgSpeed.setStatus("current")


class _EsmPortCfgDuplexMode_Type(Integer32):
    """Custom type esmPortCfgDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("autoDuplex", 3))
    )


_EsmPortCfgDuplexMode_Type.__name__ = "Integer32"
_EsmPortCfgDuplexMode_Object = MibTableColumn
esmPortCfgDuplexMode = _EsmPortCfgDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 6),
    _EsmPortCfgDuplexMode_Type()
)
esmPortCfgDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgDuplexMode.setStatus("current")


class _EsmPortCfgIFG_Type(Integer32):
    """Custom type esmPortCfgIFG based on Integer32"""
    defaultValue = 12


_EsmPortCfgIFG_Type.__name__ = "Integer32"
_EsmPortCfgIFG_Object = MibTableColumn
esmPortCfgIFG = _EsmPortCfgIFG_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 7),
    _EsmPortCfgIFG_Type()
)
esmPortCfgIFG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgIFG.setStatus("current")
_EsmPortPauseSlotTime_Type = Integer32
_EsmPortPauseSlotTime_Object = MibTableColumn
esmPortPauseSlotTime = _EsmPortPauseSlotTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 8),
    _EsmPortPauseSlotTime_Type()
)
esmPortPauseSlotTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortPauseSlotTime.setStatus("current")


class _EsmPortMaxFloodRate_Type(Integer32):
    """Custom type esmPortMaxFloodRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mbps", 1),
          ("percentage", 2),
          ("pps", 3))
    )


_EsmPortMaxFloodRate_Type.__name__ = "Integer32"
_EsmPortMaxFloodRate_Object = MibTableColumn
esmPortMaxFloodRate = _EsmPortMaxFloodRate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 9),
    _EsmPortMaxFloodRate_Type()
)
esmPortMaxFloodRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortMaxFloodRate.setStatus("current")


class _EsmPortFloodMcastEnable_Type(Integer32):
    """Custom type esmPortFloodMcastEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableMulticastFlood", 1),
          ("disableMulticastFlood", 2))
    )


_EsmPortFloodMcastEnable_Type.__name__ = "Integer32"
_EsmPortFloodMcastEnable_Object = MibTableColumn
esmPortFloodMcastEnable = _EsmPortFloodMcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 10),
    _EsmPortFloodMcastEnable_Type()
)
esmPortFloodMcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortFloodMcastEnable.setStatus("current")
_EsmPortCfgMaxFrameSize_Type = Integer32
_EsmPortCfgMaxFrameSize_Object = MibTableColumn
esmPortCfgMaxFrameSize = _EsmPortCfgMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 11),
    _EsmPortCfgMaxFrameSize_Type()
)
esmPortCfgMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgMaxFrameSize.setStatus("current")


class _EsmPortCfgLongEnable_Type(Integer32):
    """Custom type esmPortCfgLongEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EsmPortCfgLongEnable_Type.__name__ = "Integer32"
_EsmPortCfgLongEnable_Object = MibTableColumn
esmPortCfgLongEnable = _EsmPortCfgLongEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 12),
    _EsmPortCfgLongEnable_Type()
)
esmPortCfgLongEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgLongEnable.setStatus("current")


class _EsmPortCfgRuntEnable_Type(Integer32):
    """Custom type esmPortCfgRuntEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_EsmPortCfgRuntEnable_Type.__name__ = "Integer32"
_EsmPortCfgRuntEnable_Object = MibTableColumn
esmPortCfgRuntEnable = _EsmPortCfgRuntEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 13),
    _EsmPortCfgRuntEnable_Type()
)
esmPortCfgRuntEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgRuntEnable.setStatus("current")


class _EsmPortCfgRuntSize_Type(Integer32):
    """Custom type esmPortCfgRuntSize based on Integer32"""
    defaultValue = 64


_EsmPortCfgRuntSize_Type.__name__ = "Integer32"
_EsmPortCfgRuntSize_Object = MibTableColumn
esmPortCfgRuntSize = _EsmPortCfgRuntSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 14),
    _EsmPortCfgRuntSize_Type()
)
esmPortCfgRuntSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgRuntSize.setStatus("current")


class _EsmPortCfgAutoNegotiation_Type(Integer32):
    """Custom type esmPortCfgAutoNegotiation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EsmPortCfgAutoNegotiation_Type.__name__ = "Integer32"
_EsmPortCfgAutoNegotiation_Object = MibTableColumn
esmPortCfgAutoNegotiation = _EsmPortCfgAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 15),
    _EsmPortCfgAutoNegotiation_Type()
)
esmPortCfgAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgAutoNegotiation.setStatus("current")


class _EsmPortCfgCrossover_Type(Integer32):
    """Custom type esmPortCfgCrossover based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 1),
          ("mdix", 2),
          ("auto", 3))
    )


_EsmPortCfgCrossover_Type.__name__ = "Integer32"
_EsmPortCfgCrossover_Object = MibTableColumn
esmPortCfgCrossover = _EsmPortCfgCrossover_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 16),
    _EsmPortCfgCrossover_Type()
)
esmPortCfgCrossover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgCrossover.setStatus("current")


class _EsmPortCfgFlow_Type(Integer32):
    """Custom type esmPortCfgFlow based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EsmPortCfgFlow_Type.__name__ = "Integer32"
_EsmPortCfgFlow_Object = MibTableColumn
esmPortCfgFlow = _EsmPortCfgFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 17),
    _EsmPortCfgFlow_Type()
)
esmPortCfgFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgFlow.setStatus("current")


class _EsmPortCfgHybridActiveType_Type(Integer32):
    """Custom type esmPortCfgHybridActiveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notapplicable", 0),
          ("fiber", 1),
          ("copper", 2))
    )


_EsmPortCfgHybridActiveType_Type.__name__ = "Integer32"
_EsmPortCfgHybridActiveType_Object = MibTableColumn
esmPortCfgHybridActiveType = _EsmPortCfgHybridActiveType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 18),
    _EsmPortCfgHybridActiveType_Type()
)
esmPortCfgHybridActiveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortCfgHybridActiveType.setStatus("current")


class _EsmPortCfgHybridMode_Type(Integer32):
    """Custom type esmPortCfgHybridMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notapplicable", 0),
          ("preferredCopper", 1),
          ("forcedCopper", 2),
          ("preferredFiber", 3),
          ("forcedFiber", 4))
    )


_EsmPortCfgHybridMode_Type.__name__ = "Integer32"
_EsmPortCfgHybridMode_Object = MibTableColumn
esmPortCfgHybridMode = _EsmPortCfgHybridMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 19),
    _EsmPortCfgHybridMode_Type()
)
esmPortCfgHybridMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgHybridMode.setStatus("current")


class _EsmPortOperationalHybridType_Type(Integer32):
    """Custom type esmPortOperationalHybridType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("fiber", 1),
          ("copper", 2))
    )


_EsmPortOperationalHybridType_Type.__name__ = "Integer32"
_EsmPortOperationalHybridType_Object = MibTableColumn
esmPortOperationalHybridType = _EsmPortOperationalHybridType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 20),
    _EsmPortOperationalHybridType_Type()
)
esmPortOperationalHybridType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortOperationalHybridType.setStatus("current")


class _EsmPortCfgMMULowWaterMarkCellSetLimit_Type(Integer32):
    """Custom type esmPortCfgMMULowWaterMarkCellSetLimit based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_EsmPortCfgMMULowWaterMarkCellSetLimit_Type.__name__ = "Integer32"
_EsmPortCfgMMULowWaterMarkCellSetLimit_Object = MibTableColumn
esmPortCfgMMULowWaterMarkCellSetLimit = _EsmPortCfgMMULowWaterMarkCellSetLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 21),
    _EsmPortCfgMMULowWaterMarkCellSetLimit_Type()
)
esmPortCfgMMULowWaterMarkCellSetLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgMMULowWaterMarkCellSetLimit.setStatus("current")


class _EsmPortCfgMMUDynamicCellSetLimit_Type(Integer32):
    """Custom type esmPortCfgMMUDynamicCellSetLimit based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_EsmPortCfgMMUDynamicCellSetLimit_Type.__name__ = "Integer32"
_EsmPortCfgMMUDynamicCellSetLimit_Object = MibTableColumn
esmPortCfgMMUDynamicCellSetLimit = _EsmPortCfgMMUDynamicCellSetLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 22),
    _EsmPortCfgMMUDynamicCellSetLimit_Type()
)
esmPortCfgMMUDynamicCellSetLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortCfgMMUDynamicCellSetLimit.setStatus("current")


class _EsmPortViolationBitMap_Type(Bits):
    """Custom type esmPortViolationBitMap based on Bits"""
    namedValues = NamedValues(
        *(("bEniSecurityBlockPortENI", 0),
          ("bEniSecurityBlockPortSTP", 1),
          ("bEniSecurityBlockPortSL", 2),
          ("bEniSecurityBlockPortQoS", 3),
          ("bEniSecurityBlockPortUDLD", 4),
          ("bEniSecurityBlockPortETHBLK", 5))
    )

_EsmPortViolationBitMap_Type.__name__ = "Bits"
_EsmPortViolationBitMap_Object = MibTableColumn
esmPortViolationBitMap = _EsmPortViolationBitMap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 23),
    _EsmPortViolationBitMap_Type()
)
esmPortViolationBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortViolationBitMap.setStatus("current")


class _EsmPortViolationClearAll_Type(Integer32):
    """Custom type esmPortViolationClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_EsmPortViolationClearAll_Type.__name__ = "Integer32"
_EsmPortViolationClearAll_Object = MibTableColumn
esmPortViolationClearAll = _EsmPortViolationClearAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 24),
    _EsmPortViolationClearAll_Type()
)
esmPortViolationClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortViolationClearAll.setStatus("current")


class _EsmPortFloodBcastEnable_Type(Integer32):
    """Custom type esmPortFloodBcastEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableBcastFlood", 1),
          ("disableBcastFlood", 2))
    )


_EsmPortFloodBcastEnable_Type.__name__ = "Integer32"
_EsmPortFloodBcastEnable_Object = MibTableColumn
esmPortFloodBcastEnable = _EsmPortFloodBcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 25),
    _EsmPortFloodBcastEnable_Type()
)
esmPortFloodBcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortFloodBcastEnable.setStatus("current")


class _EsmPortFloodUnknownUcastEnable_Type(Integer32):
    """Custom type esmPortFloodUnknownUcastEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableUnknownUcastFlood", 1),
          ("disableUnknownUcastFlood", 2))
    )


_EsmPortFloodUnknownUcastEnable_Type.__name__ = "Integer32"
_EsmPortFloodUnknownUcastEnable_Object = MibTableColumn
esmPortFloodUnknownUcastEnable = _EsmPortFloodUnknownUcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 26),
    _EsmPortFloodUnknownUcastEnable_Type()
)
esmPortFloodUnknownUcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortFloodUnknownUcastEnable.setStatus("current")


class _EsmPortMaxUnknownUcastFloodRate_Type(Integer32):
    """Custom type esmPortMaxUnknownUcastFloodRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mbps", 1),
          ("percentage", 2),
          ("pps", 3))
    )


_EsmPortMaxUnknownUcastFloodRate_Type.__name__ = "Integer32"
_EsmPortMaxUnknownUcastFloodRate_Object = MibTableColumn
esmPortMaxUnknownUcastFloodRate = _EsmPortMaxUnknownUcastFloodRate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 27),
    _EsmPortMaxUnknownUcastFloodRate_Type()
)
esmPortMaxUnknownUcastFloodRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortMaxUnknownUcastFloodRate.setStatus("current")


class _EsmPortMaxMcastFloodRate_Type(Integer32):
    """Custom type esmPortMaxMcastFloodRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mbps", 1),
          ("percentage", 2),
          ("pps", 3))
    )


_EsmPortMaxMcastFloodRate_Type.__name__ = "Integer32"
_EsmPortMaxMcastFloodRate_Object = MibTableColumn
esmPortMaxMcastFloodRate = _EsmPortMaxMcastFloodRate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 28),
    _EsmPortMaxMcastFloodRate_Type()
)
esmPortMaxMcastFloodRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortMaxMcastFloodRate.setStatus("current")
_EsmPortMaxFloodRateLimit_Type = Integer32
_EsmPortMaxFloodRateLimit_Object = MibTableColumn
esmPortMaxFloodRateLimit = _EsmPortMaxFloodRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 29),
    _EsmPortMaxFloodRateLimit_Type()
)
esmPortMaxFloodRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortMaxFloodRateLimit.setStatus("current")
_EsmPortMaxUnknownUcastFloodRateLimit_Type = Integer32
_EsmPortMaxUnknownUcastFloodRateLimit_Object = MibTableColumn
esmPortMaxUnknownUcastFloodRateLimit = _EsmPortMaxUnknownUcastFloodRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 30),
    _EsmPortMaxUnknownUcastFloodRateLimit_Type()
)
esmPortMaxUnknownUcastFloodRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortMaxUnknownUcastFloodRateLimit.setStatus("current")
_EsmPortMaxMcastFloodRateLimit_Type = Integer32
_EsmPortMaxMcastFloodRateLimit_Object = MibTableColumn
esmPortMaxMcastFloodRateLimit = _EsmPortMaxMcastFloodRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 31),
    _EsmPortMaxMcastFloodRateLimit_Type()
)
esmPortMaxMcastFloodRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortMaxMcastFloodRateLimit.setStatus("current")


class _EsmPortCfgSFPType_Type(DisplayString):
    """Custom type esmPortCfgSFPType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EsmPortCfgSFPType_Type.__name__ = "DisplayString"
_EsmPortCfgSFPType_Object = MibTableColumn
esmPortCfgSFPType = _EsmPortCfgSFPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 1, 1, 32),
    _EsmPortCfgSFPType_Type()
)
esmPortCfgSFPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortCfgSFPType.setStatus("current")
_AlcetherStatsTable_Object = MibTable
alcetherStatsTable = _AlcetherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcetherStatsTable.setStatus("current")
_AlcetherStatsEntry_Object = MibTableRow
alcetherStatsEntry = _AlcetherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1)
)
alcetherStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alcetherStatsEntry.setStatus("current")


class _AlcetherClearStats_Type(Integer32):
    """Custom type alcetherClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlcetherClearStats_Type.__name__ = "Integer32"
_AlcetherClearStats_Object = MibTableColumn
alcetherClearStats = _AlcetherClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 1),
    _AlcetherClearStats_Type()
)
alcetherClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcetherClearStats.setStatus("current")
_AlcetherLastClearStats_Type = TimeTicks
_AlcetherLastClearStats_Object = MibTableColumn
alcetherLastClearStats = _AlcetherLastClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 2),
    _AlcetherLastClearStats_Type()
)
alcetherLastClearStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherLastClearStats.setStatus("current")
_AlcetherStatsCRCAlignErrors_Type = Counter64
_AlcetherStatsCRCAlignErrors_Object = MibTableColumn
alcetherStatsCRCAlignErrors = _AlcetherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 3),
    _AlcetherStatsCRCAlignErrors_Type()
)
alcetherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsCRCAlignErrors.setStatus("current")
_AlcetherStatsRxUndersizePkts_Type = Counter64
_AlcetherStatsRxUndersizePkts_Object = MibTableColumn
alcetherStatsRxUndersizePkts = _AlcetherStatsRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 4),
    _AlcetherStatsRxUndersizePkts_Type()
)
alcetherStatsRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxUndersizePkts.setStatus("current")
_AlcetherStatsTxUndersizePkts_Type = Counter64
_AlcetherStatsTxUndersizePkts_Object = MibTableColumn
alcetherStatsTxUndersizePkts = _AlcetherStatsTxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 5),
    _AlcetherStatsTxUndersizePkts_Type()
)
alcetherStatsTxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxUndersizePkts.setStatus("current")
_AlcetherStatsTxOversizePkts_Type = Counter64
_AlcetherStatsTxOversizePkts_Object = MibTableColumn
alcetherStatsTxOversizePkts = _AlcetherStatsTxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 6),
    _AlcetherStatsTxOversizePkts_Type()
)
alcetherStatsTxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxOversizePkts.setStatus("current")
_AlcetherStatsRxJabbers_Type = Counter64
_AlcetherStatsRxJabbers_Object = MibTableColumn
alcetherStatsRxJabbers = _AlcetherStatsRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 7),
    _AlcetherStatsRxJabbers_Type()
)
alcetherStatsRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxJabbers.setStatus("current")
_AlcetherStatsRxCollisions_Type = Counter64
_AlcetherStatsRxCollisions_Object = MibTableColumn
alcetherStatsRxCollisions = _AlcetherStatsRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 8),
    _AlcetherStatsRxCollisions_Type()
)
alcetherStatsRxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxCollisions.setStatus("current")
_AlcetherStatsTxCollisions_Type = Counter64
_AlcetherStatsTxCollisions_Object = MibTableColumn
alcetherStatsTxCollisions = _AlcetherStatsTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 9),
    _AlcetherStatsTxCollisions_Type()
)
alcetherStatsTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxCollisions.setStatus("current")
_AlcetherStatsPkts64Octets_Type = Counter64
_AlcetherStatsPkts64Octets_Object = MibTableColumn
alcetherStatsPkts64Octets = _AlcetherStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 10),
    _AlcetherStatsPkts64Octets_Type()
)
alcetherStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts64Octets.setStatus("current")
_AlcetherStatsPkts65to127Octets_Type = Counter64
_AlcetherStatsPkts65to127Octets_Object = MibTableColumn
alcetherStatsPkts65to127Octets = _AlcetherStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 11),
    _AlcetherStatsPkts65to127Octets_Type()
)
alcetherStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts65to127Octets.setStatus("current")
_AlcetherStatsPkts128to255Octets_Type = Counter64
_AlcetherStatsPkts128to255Octets_Object = MibTableColumn
alcetherStatsPkts128to255Octets = _AlcetherStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 12),
    _AlcetherStatsPkts128to255Octets_Type()
)
alcetherStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts128to255Octets.setStatus("current")
_AlcetherStatsPkts256to511Octets_Type = Counter64
_AlcetherStatsPkts256to511Octets_Object = MibTableColumn
alcetherStatsPkts256to511Octets = _AlcetherStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 13),
    _AlcetherStatsPkts256to511Octets_Type()
)
alcetherStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts256to511Octets.setStatus("current")
_AlcetherStatsPkts512to1023Octets_Type = Counter64
_AlcetherStatsPkts512to1023Octets_Object = MibTableColumn
alcetherStatsPkts512to1023Octets = _AlcetherStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 14),
    _AlcetherStatsPkts512to1023Octets_Type()
)
alcetherStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts512to1023Octets.setStatus("current")
_AlcetherStatsPkts1024to1518Octets_Type = Counter64
_AlcetherStatsPkts1024to1518Octets_Object = MibTableColumn
alcetherStatsPkts1024to1518Octets = _AlcetherStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 15),
    _AlcetherStatsPkts1024to1518Octets_Type()
)
alcetherStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts1024to1518Octets.setStatus("current")
_GigaEtherStatsPkts1519to4095Octets_Type = Counter64
_GigaEtherStatsPkts1519to4095Octets_Object = MibTableColumn
gigaEtherStatsPkts1519to4095Octets = _GigaEtherStatsPkts1519to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 16),
    _GigaEtherStatsPkts1519to4095Octets_Type()
)
gigaEtherStatsPkts1519to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigaEtherStatsPkts1519to4095Octets.setStatus("current")
_GigaEtherStatsPkts4096to9215Octets_Type = Counter64
_GigaEtherStatsPkts4096to9215Octets_Object = MibTableColumn
gigaEtherStatsPkts4096to9215Octets = _GigaEtherStatsPkts4096to9215Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 17),
    _GigaEtherStatsPkts4096to9215Octets_Type()
)
gigaEtherStatsPkts4096to9215Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigaEtherStatsPkts4096to9215Octets.setStatus("current")
_AlcetherStatsPkts1519to2047Octets_Type = Counter64
_AlcetherStatsPkts1519to2047Octets_Object = MibTableColumn
alcetherStatsPkts1519to2047Octets = _AlcetherStatsPkts1519to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 18),
    _AlcetherStatsPkts1519to2047Octets_Type()
)
alcetherStatsPkts1519to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts1519to2047Octets.setStatus("current")
_AlcetherStatsPkts2048to4095Octets_Type = Counter64
_AlcetherStatsPkts2048to4095Octets_Object = MibTableColumn
alcetherStatsPkts2048to4095Octets = _AlcetherStatsPkts2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 19),
    _AlcetherStatsPkts2048to4095Octets_Type()
)
alcetherStatsPkts2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts2048to4095Octets.setStatus("current")
_AlcetherStatsPkts4096Octets_Type = Counter64
_AlcetherStatsPkts4096Octets_Object = MibTableColumn
alcetherStatsPkts4096Octets = _AlcetherStatsPkts4096Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 20),
    _AlcetherStatsPkts4096Octets_Type()
)
alcetherStatsPkts4096Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsPkts4096Octets.setStatus("current")
_AlcetherStatsRxGiantPkts_Type = Counter64
_AlcetherStatsRxGiantPkts_Object = MibTableColumn
alcetherStatsRxGiantPkts = _AlcetherStatsRxGiantPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 21),
    _AlcetherStatsRxGiantPkts_Type()
)
alcetherStatsRxGiantPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxGiantPkts.setStatus("current")
_AlcetherStatsRxDribbleNibblePkts_Type = Counter64
_AlcetherStatsRxDribbleNibblePkts_Object = MibTableColumn
alcetherStatsRxDribbleNibblePkts = _AlcetherStatsRxDribbleNibblePkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 22),
    _AlcetherStatsRxDribbleNibblePkts_Type()
)
alcetherStatsRxDribbleNibblePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxDribbleNibblePkts.setStatus("current")
_AlcetherStatsRxLongEventPkts_Type = Counter64
_AlcetherStatsRxLongEventPkts_Object = MibTableColumn
alcetherStatsRxLongEventPkts = _AlcetherStatsRxLongEventPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 23),
    _AlcetherStatsRxLongEventPkts_Type()
)
alcetherStatsRxLongEventPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxLongEventPkts.setStatus("current")
_AlcetherStatsRxVlanTagPkts_Type = Counter64
_AlcetherStatsRxVlanTagPkts_Object = MibTableColumn
alcetherStatsRxVlanTagPkts = _AlcetherStatsRxVlanTagPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 24),
    _AlcetherStatsRxVlanTagPkts_Type()
)
alcetherStatsRxVlanTagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxVlanTagPkts.setStatus("current")
_AlcetherStatsRxControlPkts_Type = Counter64
_AlcetherStatsRxControlPkts_Object = MibTableColumn
alcetherStatsRxControlPkts = _AlcetherStatsRxControlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 25),
    _AlcetherStatsRxControlPkts_Type()
)
alcetherStatsRxControlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxControlPkts.setStatus("current")
_AlcetherStatsRxLenChkErrPkts_Type = Counter64
_AlcetherStatsRxLenChkErrPkts_Object = MibTableColumn
alcetherStatsRxLenChkErrPkts = _AlcetherStatsRxLenChkErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 26),
    _AlcetherStatsRxLenChkErrPkts_Type()
)
alcetherStatsRxLenChkErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxLenChkErrPkts.setStatus("current")
_AlcetherStatsRxCodeErrPkts_Type = Counter64
_AlcetherStatsRxCodeErrPkts_Object = MibTableColumn
alcetherStatsRxCodeErrPkts = _AlcetherStatsRxCodeErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 27),
    _AlcetherStatsRxCodeErrPkts_Type()
)
alcetherStatsRxCodeErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxCodeErrPkts.setStatus("current")
_AlcetherStatsRxDvEventPkts_Type = Counter64
_AlcetherStatsRxDvEventPkts_Object = MibTableColumn
alcetherStatsRxDvEventPkts = _AlcetherStatsRxDvEventPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 28),
    _AlcetherStatsRxDvEventPkts_Type()
)
alcetherStatsRxDvEventPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxDvEventPkts.setStatus("current")
_AlcetherStatsRxPrevPktDropped_Type = Counter64
_AlcetherStatsRxPrevPktDropped_Object = MibTableColumn
alcetherStatsRxPrevPktDropped = _AlcetherStatsRxPrevPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 29),
    _AlcetherStatsRxPrevPktDropped_Type()
)
alcetherStatsRxPrevPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsRxPrevPktDropped.setStatus("current")
_AlcetherStatsTx64Octets_Type = Counter64
_AlcetherStatsTx64Octets_Object = MibTableColumn
alcetherStatsTx64Octets = _AlcetherStatsTx64Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 30),
    _AlcetherStatsTx64Octets_Type()
)
alcetherStatsTx64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx64Octets.setStatus("current")
_AlcetherStatsTx65to127Octets_Type = Counter64
_AlcetherStatsTx65to127Octets_Object = MibTableColumn
alcetherStatsTx65to127Octets = _AlcetherStatsTx65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 31),
    _AlcetherStatsTx65to127Octets_Type()
)
alcetherStatsTx65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx65to127Octets.setStatus("current")
_AlcetherStatsTx128to255Octets_Type = Counter64
_AlcetherStatsTx128to255Octets_Object = MibTableColumn
alcetherStatsTx128to255Octets = _AlcetherStatsTx128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 32),
    _AlcetherStatsTx128to255Octets_Type()
)
alcetherStatsTx128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx128to255Octets.setStatus("current")
_AlcetherStatsTx256to511Octets_Type = Counter64
_AlcetherStatsTx256to511Octets_Object = MibTableColumn
alcetherStatsTx256to511Octets = _AlcetherStatsTx256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 33),
    _AlcetherStatsTx256to511Octets_Type()
)
alcetherStatsTx256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx256to511Octets.setStatus("current")
_AlcetherStatsTx512to1023Octets_Type = Counter64
_AlcetherStatsTx512to1023Octets_Object = MibTableColumn
alcetherStatsTx512to1023Octets = _AlcetherStatsTx512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 34),
    _AlcetherStatsTx512to1023Octets_Type()
)
alcetherStatsTx512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx512to1023Octets.setStatus("current")
_AlcetherStatsTx1024to1518Octets_Type = Counter64
_AlcetherStatsTx1024to1518Octets_Object = MibTableColumn
alcetherStatsTx1024to1518Octets = _AlcetherStatsTx1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 35),
    _AlcetherStatsTx1024to1518Octets_Type()
)
alcetherStatsTx1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx1024to1518Octets.setStatus("current")
_AlcetherStatsTx1519to2047Octets_Type = Counter64
_AlcetherStatsTx1519to2047Octets_Object = MibTableColumn
alcetherStatsTx1519to2047Octets = _AlcetherStatsTx1519to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 36),
    _AlcetherStatsTx1519to2047Octets_Type()
)
alcetherStatsTx1519to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx1519to2047Octets.setStatus("current")
_AlcetherStatsTx2048to4095Octets_Type = Counter64
_AlcetherStatsTx2048to4095Octets_Object = MibTableColumn
alcetherStatsTx2048to4095Octets = _AlcetherStatsTx2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 37),
    _AlcetherStatsTx2048to4095Octets_Type()
)
alcetherStatsTx2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx2048to4095Octets.setStatus("current")
_AlcetherStatsTx4096Octets_Type = Counter64
_AlcetherStatsTx4096Octets_Object = MibTableColumn
alcetherStatsTx4096Octets = _AlcetherStatsTx4096Octets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 38),
    _AlcetherStatsTx4096Octets_Type()
)
alcetherStatsTx4096Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTx4096Octets.setStatus("current")
_AlcetherStatsTxRetryCount_Type = Counter64
_AlcetherStatsTxRetryCount_Object = MibTableColumn
alcetherStatsTxRetryCount = _AlcetherStatsTxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 39),
    _AlcetherStatsTxRetryCount_Type()
)
alcetherStatsTxRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxRetryCount.setStatus("current")
_AlcetherStatsTxVlanTagPkts_Type = Counter64
_AlcetherStatsTxVlanTagPkts_Object = MibTableColumn
alcetherStatsTxVlanTagPkts = _AlcetherStatsTxVlanTagPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 40),
    _AlcetherStatsTxVlanTagPkts_Type()
)
alcetherStatsTxVlanTagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxVlanTagPkts.setStatus("current")
_AlcetherStatsTxControlPkts_Type = Counter64
_AlcetherStatsTxControlPkts_Object = MibTableColumn
alcetherStatsTxControlPkts = _AlcetherStatsTxControlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 41),
    _AlcetherStatsTxControlPkts_Type()
)
alcetherStatsTxControlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxControlPkts.setStatus("current")
_AlcetherStatsTxLatePkts_Type = Counter64
_AlcetherStatsTxLatePkts_Object = MibTableColumn
alcetherStatsTxLatePkts = _AlcetherStatsTxLatePkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 42),
    _AlcetherStatsTxLatePkts_Type()
)
alcetherStatsTxLatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxLatePkts.setStatus("current")
_AlcetherStatsTxTotalBytesOnWire_Type = Counter64
_AlcetherStatsTxTotalBytesOnWire_Object = MibTableColumn
alcetherStatsTxTotalBytesOnWire = _AlcetherStatsTxTotalBytesOnWire_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 43),
    _AlcetherStatsTxTotalBytesOnWire_Type()
)
alcetherStatsTxTotalBytesOnWire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxTotalBytesOnWire.setStatus("current")
_AlcetherStatsTxLenChkErrPkts_Type = Counter64
_AlcetherStatsTxLenChkErrPkts_Object = MibTableColumn
alcetherStatsTxLenChkErrPkts = _AlcetherStatsTxLenChkErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 44),
    _AlcetherStatsTxLenChkErrPkts_Type()
)
alcetherStatsTxLenChkErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxLenChkErrPkts.setStatus("current")
_AlcetherStatsTxExcDeferPkts_Type = Counter64
_AlcetherStatsTxExcDeferPkts_Object = MibTableColumn
alcetherStatsTxExcDeferPkts = _AlcetherStatsTxExcDeferPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 2, 1, 45),
    _AlcetherStatsTxExcDeferPkts_Type()
)
alcetherStatsTxExcDeferPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcetherStatsTxExcDeferPkts.setStatus("current")
_EsmHybridConfTable_Object = MibTable
esmHybridConfTable = _EsmHybridConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    esmHybridConfTable.setStatus("current")
_EsmHybridConfEntry_Object = MibTableRow
esmHybridConfEntry = _EsmHybridConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 3, 1)
)
esmHybridConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    esmHybridConfEntry.setStatus("current")


class _EsmHybridPortCfgSpeed_Type(Integer32):
    """Custom type esmHybridPortCfgSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("speed100", 1),
          ("speed10", 2),
          ("speedAuto", 3),
          ("speed1000", 5),
          ("speed10000", 6),
          ("speedMax100", 8),
          ("speedMax1000", 9))
    )


_EsmHybridPortCfgSpeed_Type.__name__ = "Integer32"
_EsmHybridPortCfgSpeed_Object = MibTableColumn
esmHybridPortCfgSpeed = _EsmHybridPortCfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 3, 1, 1),
    _EsmHybridPortCfgSpeed_Type()
)
esmHybridPortCfgSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmHybridPortCfgSpeed.setStatus("current")


class _EsmHybridPortCfgDuplexMode_Type(Integer32):
    """Custom type esmHybridPortCfgDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("autoDuplex", 3))
    )


_EsmHybridPortCfgDuplexMode_Type.__name__ = "Integer32"
_EsmHybridPortCfgDuplexMode_Object = MibTableColumn
esmHybridPortCfgDuplexMode = _EsmHybridPortCfgDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 3, 1, 2),
    _EsmHybridPortCfgDuplexMode_Type()
)
esmHybridPortCfgDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmHybridPortCfgDuplexMode.setStatus("current")


class _EsmHybridPortCfgAutoNegotiation_Type(Integer32):
    """Custom type esmHybridPortCfgAutoNegotiation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EsmHybridPortCfgAutoNegotiation_Type.__name__ = "Integer32"
_EsmHybridPortCfgAutoNegotiation_Object = MibTableColumn
esmHybridPortCfgAutoNegotiation = _EsmHybridPortCfgAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 3, 1, 3),
    _EsmHybridPortCfgAutoNegotiation_Type()
)
esmHybridPortCfgAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmHybridPortCfgAutoNegotiation.setStatus("current")


class _EsmHybridPortCfgCrossover_Type(Integer32):
    """Custom type esmHybridPortCfgCrossover based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 1),
          ("mdix", 2),
          ("auto", 3))
    )


_EsmHybridPortCfgCrossover_Type.__name__ = "Integer32"
_EsmHybridPortCfgCrossover_Object = MibTableColumn
esmHybridPortCfgCrossover = _EsmHybridPortCfgCrossover_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 3, 1, 4),
    _EsmHybridPortCfgCrossover_Type()
)
esmHybridPortCfgCrossover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmHybridPortCfgCrossover.setStatus("current")


class _EsmHybridPortCfgFlow_Type(Integer32):
    """Custom type esmHybridPortCfgFlow based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enabledXmit", 2),
          ("enabledRcv", 3),
          ("enabledXmitAndRcv", 4))
    )


_EsmHybridPortCfgFlow_Type.__name__ = "Integer32"
_EsmHybridPortCfgFlow_Object = MibTableColumn
esmHybridPortCfgFlow = _EsmHybridPortCfgFlow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 3, 1, 5),
    _EsmHybridPortCfgFlow_Type()
)
esmHybridPortCfgFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmHybridPortCfgFlow.setStatus("current")


class _EsmHybridPortCfgInactiveType_Type(Integer32):
    """Custom type esmHybridPortCfgInactiveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 1),
          ("copper", 2))
    )


_EsmHybridPortCfgInactiveType_Type.__name__ = "Integer32"
_EsmHybridPortCfgInactiveType_Object = MibTableColumn
esmHybridPortCfgInactiveType = _EsmHybridPortCfgInactiveType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 3, 1, 6),
    _EsmHybridPortCfgInactiveType_Type()
)
esmHybridPortCfgInactiveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmHybridPortCfgInactiveType.setStatus("current")


class _EsmHybridPortCfgSFPType_Type(DisplayString):
    """Custom type esmHybridPortCfgSFPType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EsmHybridPortCfgSFPType_Type.__name__ = "DisplayString"
_EsmHybridPortCfgSFPType_Object = MibTableColumn
esmHybridPortCfgSFPType = _EsmHybridPortCfgSFPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 3, 1, 7),
    _EsmHybridPortCfgSFPType_Type()
)
esmHybridPortCfgSFPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmHybridPortCfgSFPType.setStatus("current")
_Alcether10GigTable_Object = MibTable
alcether10GigTable = _Alcether10GigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    alcether10GigTable.setStatus("current")
_Alcether10GigEntry_Object = MibTableRow
alcether10GigEntry = _Alcether10GigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 4, 1)
)
alcether10GigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alcether10GigEntry.setStatus("current")


class _Alcether10GigPrimary_Type(Integer32):
    """Custom type alcether10GigPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phyAprimary", 1),
          ("phyBprimary", 2),
          ("notApplicable", 3))
    )


_Alcether10GigPrimary_Type.__name__ = "Integer32"
_Alcether10GigPrimary_Object = MibTableColumn
alcether10GigPrimary = _Alcether10GigPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 4, 1, 1),
    _Alcether10GigPrimary_Type()
)
alcether10GigPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcether10GigPrimary.setStatus("current")
_DdmInfoTable_Object = MibTable
ddmInfoTable = _DdmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ddmInfoTable.setStatus("current")
_DdmInfoEntry_Object = MibTableRow
ddmInfoEntry = _DdmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1)
)
ddmInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ddmInfoEntry.setStatus("current")


class _DdmTemperature_Type(Integer32):
    """Custom type ddmTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmTemperature_Type.__name__ = "Integer32"
_DdmTemperature_Object = MibTableColumn
ddmTemperature = _DdmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 1),
    _DdmTemperature_Type()
)
ddmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTemperature.setStatus("current")
if mibBuilder.loadTexts:
    ddmTemperature.setUnits("thousandth of a degree celcius")


class _DdmTempLowWarning_Type(Integer32):
    """Custom type ddmTempLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmTempLowWarning_Type.__name__ = "Integer32"
_DdmTempLowWarning_Object = MibTableColumn
ddmTempLowWarning = _DdmTempLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 2),
    _DdmTempLowWarning_Type()
)
ddmTempLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTempLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmTempLowWarning.setUnits("thousandth of a degree celcius")


class _DdmTempLowAlarm_Type(Integer32):
    """Custom type ddmTempLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmTempLowAlarm_Type.__name__ = "Integer32"
_DdmTempLowAlarm_Object = MibTableColumn
ddmTempLowAlarm = _DdmTempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 3),
    _DdmTempLowAlarm_Type()
)
ddmTempLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTempLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmTempLowAlarm.setUnits("thousandth of a degree celcius")


class _DdmTempHiWarning_Type(Integer32):
    """Custom type ddmTempHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmTempHiWarning_Type.__name__ = "Integer32"
_DdmTempHiWarning_Object = MibTableColumn
ddmTempHiWarning = _DdmTempHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 4),
    _DdmTempHiWarning_Type()
)
ddmTempHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTempHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmTempHiWarning.setUnits("thousandth of a degree celcius")


class _DdmTempHiAlarm_Type(Integer32):
    """Custom type ddmTempHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-150000, 150000),
    )


_DdmTempHiAlarm_Type.__name__ = "Integer32"
_DdmTempHiAlarm_Object = MibTableColumn
ddmTempHiAlarm = _DdmTempHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 5),
    _DdmTempHiAlarm_Type()
)
ddmTempHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTempHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmTempHiAlarm.setUnits("thousandth of a degree celcius")


class _DdmSupplyVoltage_Type(Integer32):
    """Custom type ddmSupplyVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmSupplyVoltage_Type.__name__ = "Integer32"
_DdmSupplyVoltage_Object = MibTableColumn
ddmSupplyVoltage = _DdmSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 6),
    _DdmSupplyVoltage_Type()
)
ddmSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmSupplyVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ddmSupplyVoltage.setUnits("thousandth of a volt")


class _DdmSupplyVoltageLowWarning_Type(Integer32):
    """Custom type ddmSupplyVoltageLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmSupplyVoltageLowWarning_Type.__name__ = "Integer32"
_DdmSupplyVoltageLowWarning_Object = MibTableColumn
ddmSupplyVoltageLowWarning = _DdmSupplyVoltageLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 7),
    _DdmSupplyVoltageLowWarning_Type()
)
ddmSupplyVoltageLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmSupplyVoltageLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmSupplyVoltageLowWarning.setUnits("thousandth of a volt")


class _DdmSupplyVoltageLowAlarm_Type(Integer32):
    """Custom type ddmSupplyVoltageLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmSupplyVoltageLowAlarm_Type.__name__ = "Integer32"
_DdmSupplyVoltageLowAlarm_Object = MibTableColumn
ddmSupplyVoltageLowAlarm = _DdmSupplyVoltageLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 8),
    _DdmSupplyVoltageLowAlarm_Type()
)
ddmSupplyVoltageLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmSupplyVoltageLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmSupplyVoltageLowAlarm.setUnits("thousandth of a volt")


class _DdmSupplyVoltageHiWarning_Type(Integer32):
    """Custom type ddmSupplyVoltageHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmSupplyVoltageHiWarning_Type.__name__ = "Integer32"
_DdmSupplyVoltageHiWarning_Object = MibTableColumn
ddmSupplyVoltageHiWarning = _DdmSupplyVoltageHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 9),
    _DdmSupplyVoltageHiWarning_Type()
)
ddmSupplyVoltageHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmSupplyVoltageHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmSupplyVoltageHiWarning.setUnits("thousandth of a volt")


class _DdmSupplyVoltageHiAlarm_Type(Integer32):
    """Custom type ddmSupplyVoltageHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmSupplyVoltageHiAlarm_Type.__name__ = "Integer32"
_DdmSupplyVoltageHiAlarm_Object = MibTableColumn
ddmSupplyVoltageHiAlarm = _DdmSupplyVoltageHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 10),
    _DdmSupplyVoltageHiAlarm_Type()
)
ddmSupplyVoltageHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmSupplyVoltageHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmSupplyVoltageHiAlarm.setUnits("thousandth of a volt")


class _DdmTxBiasCurrent_Type(Integer32):
    """Custom type ddmTxBiasCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmTxBiasCurrent_Type.__name__ = "Integer32"
_DdmTxBiasCurrent_Object = MibTableColumn
ddmTxBiasCurrent = _DdmTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 11),
    _DdmTxBiasCurrent_Type()
)
ddmTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxBiasCurrent.setUnits("thousandth of a milli-Ampere")


class _DdmTxBiasCurrentLowWarning_Type(Integer32):
    """Custom type ddmTxBiasCurrentLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmTxBiasCurrentLowWarning_Type.__name__ = "Integer32"
_DdmTxBiasCurrentLowWarning_Object = MibTableColumn
ddmTxBiasCurrentLowWarning = _DdmTxBiasCurrentLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 12),
    _DdmTxBiasCurrentLowWarning_Type()
)
ddmTxBiasCurrentLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentLowWarning.setUnits("thousandth of a milli-Ampere")


class _DdmTxBiasCurrentLowAlarm_Type(Integer32):
    """Custom type ddmTxBiasCurrentLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmTxBiasCurrentLowAlarm_Type.__name__ = "Integer32"
_DdmTxBiasCurrentLowAlarm_Object = MibTableColumn
ddmTxBiasCurrentLowAlarm = _DdmTxBiasCurrentLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 13),
    _DdmTxBiasCurrentLowAlarm_Type()
)
ddmTxBiasCurrentLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentLowAlarm.setUnits("thousandth of a milli-Ampere")


class _DdmTxBiasCurrentHiWarning_Type(Integer32):
    """Custom type ddmTxBiasCurrentHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmTxBiasCurrentHiWarning_Type.__name__ = "Integer32"
_DdmTxBiasCurrentHiWarning_Object = MibTableColumn
ddmTxBiasCurrentHiWarning = _DdmTxBiasCurrentHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 14),
    _DdmTxBiasCurrentHiWarning_Type()
)
ddmTxBiasCurrentHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentHiWarning.setUnits("thousandth of a milli-Ampere")


class _DdmTxBiasCurrentHiAlarm_Type(Integer32):
    """Custom type ddmTxBiasCurrentHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(0, 10000),
    )


_DdmTxBiasCurrentHiAlarm_Type.__name__ = "Integer32"
_DdmTxBiasCurrentHiAlarm_Object = MibTableColumn
ddmTxBiasCurrentHiAlarm = _DdmTxBiasCurrentHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 15),
    _DdmTxBiasCurrentHiAlarm_Type()
)
ddmTxBiasCurrentHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxBiasCurrentHiAlarm.setUnits("thousandth of a milli-Ampere")


class _DdmTxOutputPower_Type(Integer32):
    """Custom type ddmTxOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmTxOutputPower_Type.__name__ = "Integer32"
_DdmTxOutputPower_Object = MibTableColumn
ddmTxOutputPower = _DdmTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 16),
    _DdmTxOutputPower_Type()
)
ddmTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxOutputPower.setUnits("thousandth of a dBm")


class _DdmTxOutputPowerLowWarning_Type(Integer32):
    """Custom type ddmTxOutputPowerLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmTxOutputPowerLowWarning_Type.__name__ = "Integer32"
_DdmTxOutputPowerLowWarning_Object = MibTableColumn
ddmTxOutputPowerLowWarning = _DdmTxOutputPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 17),
    _DdmTxOutputPowerLowWarning_Type()
)
ddmTxOutputPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxOutputPowerLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxOutputPowerLowWarning.setUnits("thousandth of a dBm")


class _DdmTxOutputPowerLowAlarm_Type(Integer32):
    """Custom type ddmTxOutputPowerLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmTxOutputPowerLowAlarm_Type.__name__ = "Integer32"
_DdmTxOutputPowerLowAlarm_Object = MibTableColumn
ddmTxOutputPowerLowAlarm = _DdmTxOutputPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 18),
    _DdmTxOutputPowerLowAlarm_Type()
)
ddmTxOutputPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxOutputPowerLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxOutputPowerLowAlarm.setUnits("thousandth of a dBm")


class _DdmTxOutputPowerHiWarning_Type(Integer32):
    """Custom type ddmTxOutputPowerHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmTxOutputPowerHiWarning_Type.__name__ = "Integer32"
_DdmTxOutputPowerHiWarning_Object = MibTableColumn
ddmTxOutputPowerHiWarning = _DdmTxOutputPowerHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 19),
    _DdmTxOutputPowerHiWarning_Type()
)
ddmTxOutputPowerHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxOutputPowerHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxOutputPowerHiWarning.setUnits("thousandth of a dBm")


class _DdmTxOutputPowerHiAlarm_Type(Integer32):
    """Custom type ddmTxOutputPowerHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmTxOutputPowerHiAlarm_Type.__name__ = "Integer32"
_DdmTxOutputPowerHiAlarm_Object = MibTableColumn
ddmTxOutputPowerHiAlarm = _DdmTxOutputPowerHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 20),
    _DdmTxOutputPowerHiAlarm_Type()
)
ddmTxOutputPowerHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmTxOutputPowerHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmTxOutputPowerHiAlarm.setUnits("thousandth of a dBm")


class _DdmRxOpticalPower_Type(Integer32):
    """Custom type ddmRxOpticalPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmRxOpticalPower_Type.__name__ = "Integer32"
_DdmRxOpticalPower_Object = MibTableColumn
ddmRxOpticalPower = _DdmRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 21),
    _DdmRxOpticalPower_Type()
)
ddmRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmRxOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    ddmRxOpticalPower.setUnits("thousandth of a dBm")


class _DdmRxOpticalPowerLowWarning_Type(Integer32):
    """Custom type ddmRxOpticalPowerLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmRxOpticalPowerLowWarning_Type.__name__ = "Integer32"
_DdmRxOpticalPowerLowWarning_Object = MibTableColumn
ddmRxOpticalPowerLowWarning = _DdmRxOpticalPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 22),
    _DdmRxOpticalPowerLowWarning_Type()
)
ddmRxOpticalPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerLowWarning.setUnits("thousandth of a dBm")


class _DdmRxOpticalPowerLowAlarm_Type(Integer32):
    """Custom type ddmRxOpticalPowerLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmRxOpticalPowerLowAlarm_Type.__name__ = "Integer32"
_DdmRxOpticalPowerLowAlarm_Object = MibTableColumn
ddmRxOpticalPowerLowAlarm = _DdmRxOpticalPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 23),
    _DdmRxOpticalPowerLowAlarm_Type()
)
ddmRxOpticalPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerLowAlarm.setUnits("thousandth of a dBm")


class _DdmRxOpticalPowerHiWarning_Type(Integer32):
    """Custom type ddmRxOpticalPowerHiWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmRxOpticalPowerHiWarning_Type.__name__ = "Integer32"
_DdmRxOpticalPowerHiWarning_Object = MibTableColumn
ddmRxOpticalPowerHiWarning = _DdmRxOpticalPowerHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 24),
    _DdmRxOpticalPowerHiWarning_Type()
)
ddmRxOpticalPowerHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerHiWarning.setStatus("current")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerHiWarning.setUnits("thousandth of a dBm")


class _DdmRxOpticalPowerHiAlarm_Type(Integer32):
    """Custom type ddmRxOpticalPowerHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200000, -200000),
        ValueRangeConstraint(-40000, 10000),
    )


_DdmRxOpticalPowerHiAlarm_Type.__name__ = "Integer32"
_DdmRxOpticalPowerHiAlarm_Object = MibTableColumn
ddmRxOpticalPowerHiAlarm = _DdmRxOpticalPowerHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 5, 1, 25),
    _DdmRxOpticalPowerHiAlarm_Type()
)
ddmRxOpticalPowerHiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerHiAlarm.setStatus("current")
if mibBuilder.loadTexts:
    ddmRxOpticalPowerHiAlarm.setUnits("thousandth of a dBm")
_EsmPortModeTable_Object = MibTable
esmPortModeTable = _EsmPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    esmPortModeTable.setStatus("current")
_EsmPortModeEntry_Object = MibTableRow
esmPortModeEntry = _EsmPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 6, 1)
)
esmPortModeEntry.setIndexNames(
    (0, "ALCATEL-IND1-PORT-MIB", "esmPortModeIndex"),
)
if mibBuilder.loadTexts:
    esmPortModeEntry.setStatus("current")


class _EsmPortModeIndex_Type(Integer32):
    """Custom type esmPortModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 8128),
    )


_EsmPortModeIndex_Type.__name__ = "Integer32"
_EsmPortModeIndex_Object = MibTableColumn
esmPortModeIndex = _EsmPortModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 6, 1, 1),
    _EsmPortModeIndex_Type()
)
esmPortModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esmPortModeIndex.setStatus("current")


class _EsmPortRunningMode_Type(Integer32):
    """Custom type esmPortRunningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uplink", 1),
          ("stackable", 2))
    )


_EsmPortRunningMode_Type.__name__ = "Integer32"
_EsmPortRunningMode_Object = MibTableColumn
esmPortRunningMode = _EsmPortRunningMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 6, 1, 2),
    _EsmPortRunningMode_Type()
)
esmPortRunningMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esmPortRunningMode.setStatus("current")


class _EsmPortSavedMode_Type(Integer32):
    """Custom type esmPortSavedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uplink", 1),
          ("stackable", 2))
    )


_EsmPortSavedMode_Type.__name__ = "Integer32"
_EsmPortSavedMode_Object = MibTableColumn
esmPortSavedMode = _EsmPortSavedMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 2, 6, 1, 3),
    _EsmPortSavedMode_Type()
)
esmPortSavedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmPortSavedMode.setStatus("current")


class _EsmE2EFlowVlan_Type(Integer32):
    """Custom type esmE2EFlowVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_EsmE2EFlowVlan_Type.__name__ = "Integer32"
_EsmE2EFlowVlan_Object = MibScalar
esmE2EFlowVlan = _EsmE2EFlowVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 3),
    _EsmE2EFlowVlan_Type()
)
esmE2EFlowVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmE2EFlowVlan.setStatus("current")
_DdmConfiguration_ObjectIdentity = ObjectIdentity
ddmConfiguration = _DdmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 4)
)


class _DdmConfig_Type(Integer32):
    """Custom type ddmConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DdmConfig_Type.__name__ = "Integer32"
_DdmConfig_Object = MibScalar
ddmConfig = _DdmConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 4, 1),
    _DdmConfig_Type()
)
ddmConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmConfig.setStatus("current")


class _DdmTrapConfig_Type(Integer32):
    """Custom type ddmTrapConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DdmTrapConfig_Type.__name__ = "Integer32"
_DdmTrapConfig_Object = MibScalar
ddmTrapConfig = _DdmTrapConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 4, 2),
    _DdmTrapConfig_Type()
)
ddmTrapConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddmTrapConfig.setStatus("current")


class _DdmNotificationType_Type(Integer32):
    """Custom type ddmNotificationType based on Integer32"""
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
        *(("clearViolation", 1),
          ("highAlarm", 2),
          ("highWarning", 3),
          ("lowWarning", 4),
          ("lowAlarm", 5))
    )


_DdmNotificationType_Type.__name__ = "Integer32"
_DdmNotificationType_Object = MibScalar
ddmNotificationType = _DdmNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 4, 3),
    _DdmNotificationType_Type()
)
ddmNotificationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ddmNotificationType.setStatus("current")
_EsmViolationRecovery_ObjectIdentity = ObjectIdentity
esmViolationRecovery = _EsmViolationRecovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 5)
)


class _EsmViolationRecoveryTrap_Type(Integer32):
    """Custom type esmViolationRecoveryTrap based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EsmViolationRecoveryTrap_Type.__name__ = "Integer32"
_EsmViolationRecoveryTrap_Object = MibScalar
esmViolationRecoveryTrap = _EsmViolationRecoveryTrap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 5, 1),
    _EsmViolationRecoveryTrap_Type()
)
esmViolationRecoveryTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmViolationRecoveryTrap.setStatus("current")


class _EsmViolationRecoveryTime_Type(Integer32):
    """Custom type esmViolationRecoveryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_EsmViolationRecoveryTime_Type.__name__ = "Integer32"
_EsmViolationRecoveryTime_Object = MibScalar
esmViolationRecoveryTime = _EsmViolationRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 5, 2),
    _EsmViolationRecoveryTime_Type()
)
esmViolationRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esmViolationRecoveryTime.setStatus("current")


class _EsmViolationRecoveryNotificationType_Type(Integer32):
    """Custom type esmViolationRecoveryNotificationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearViolation", 1)
    )


_EsmViolationRecoveryNotificationType_Type.__name__ = "Integer32"
_EsmViolationRecoveryNotificationType_Object = MibScalar
esmViolationRecoveryNotificationType = _EsmViolationRecoveryNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 1, 5, 3),
    _EsmViolationRecoveryNotificationType_Type()
)
esmViolationRecoveryNotificationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    esmViolationRecoveryNotificationType.setStatus("current")
_AlcatelIND1PortMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1PortMIBConformance = _AlcatelIND1PortMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2)
)
_AlcatelIND1PortMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1PortMIBCompliances = _AlcatelIND1PortMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2, 1)
)
_AlcatelIND1PortMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1PortMIBGroups = _AlcatelIND1PortMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2, 2)
)

# Managed Objects groups

esmConfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2, 2, 1)
)
esmConfMIBGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "esmPortCfgSpeed"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortCfgDuplexMode"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortCfgIFG"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortPauseSlotTime"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortMaxFloodRate"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortFloodMcastEnable"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortCfgMaxFrameSize"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortCfgAutoNegotiation"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortCfgCrossover"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortCfgFlow"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortFloodUnknownUcastEnable"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortMaxUnknownUcastFloodRate"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortMaxMcastFloodRate"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortFloodBcastEnable"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortMaxFloodRateLimit"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortMaxUnknownUcastFloodRateLimit"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortMaxMcastFloodRateLimit"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortCfgSFPType"))
)
if mibBuilder.loadTexts:
    esmConfMIBGroup.setStatus("current")

esmDetectedConfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2, 2, 2)
)
esmDetectedConfMIBGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "esmPortAutoSpeed"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortAutoDuplexMode"))
)
if mibBuilder.loadTexts:
    esmDetectedConfMIBGroup.setStatus("current")

alcEtherStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2, 2, 3)
)
alcEtherStatsMIBGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "alcetherClearStats"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherLastClearStats"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsCRCAlignErrors"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxUndersizePkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxUndersizePkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxOversizePkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxJabbers"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxCollisions"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxCollisions"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts64Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts65to127Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts128to255Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts256to511Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts512to1023Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts1024to1518Octets"),
        ("ALCATEL-IND1-PORT-MIB", "gigaEtherStatsPkts1519to4095Octets"),
        ("ALCATEL-IND1-PORT-MIB", "gigaEtherStatsPkts4096to9215Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts1519to2047Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts2048to4095Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsPkts4096Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxGiantPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxDribbleNibblePkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxLongEventPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxVlanTagPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxControlPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxLenChkErrPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxCodeErrPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxDvEventPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsRxPrevPktDropped"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx64Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx65to127Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx128to255Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx256to511Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx512to1023Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx1024to1518Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx1519to2047Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx2048to4095Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTx4096Octets"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxRetryCount"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxVlanTagPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxControlPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxLatePkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxTotalBytesOnWire"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxLenChkErrPkts"),
        ("ALCATEL-IND1-PORT-MIB", "alcetherStatsTxExcDeferPkts"))
)
if mibBuilder.loadTexts:
    alcEtherStatsMIBGroup.setStatus("current")

esmPortModeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2, 2, 5)
)
esmPortModeMIBGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "esmPortRunningMode"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortSavedMode"))
)
if mibBuilder.loadTexts:
    esmPortModeMIBGroup.setStatus("current")

ddmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2, 2, 6)
)
ddmInfoGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "ddmTemperature"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTempLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTempLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTempHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTempHiAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmSupplyVoltage"),
        ("ALCATEL-IND1-PORT-MIB", "ddmSupplyVoltageLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmSupplyVoltageLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmSupplyVoltageHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmSupplyVoltageHiAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxBiasCurrent"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxBiasCurrentLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxBiasCurrentLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxBiasCurrentHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxBiasCurrentHiAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxOutputPower"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxOutputPowerLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxOutputPowerLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxOutputPowerHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxOutputPowerHiAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmRxOpticalPower"),
        ("ALCATEL-IND1-PORT-MIB", "ddmRxOpticalPowerLowWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmRxOpticalPowerLowAlarm"),
        ("ALCATEL-IND1-PORT-MIB", "ddmRxOpticalPowerHiWarning"),
        ("ALCATEL-IND1-PORT-MIB", "ddmRxOpticalPowerHiAlarm"))
)
if mibBuilder.loadTexts:
    ddmInfoGroup.setStatus("current")

ddmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2, 2, 7)
)
ddmConfigGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "ddmConfig"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTrapConfig"))
)
if mibBuilder.loadTexts:
    ddmConfigGroup.setStatus("current")

violationRecoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2, 2, 9)
)
violationRecoveryGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "esmViolationRecoveryTrap"),
        ("ALCATEL-IND1-PORT-MIB", "esmViolationRecoveryTime"))
)
if mibBuilder.loadTexts:
    violationRecoveryGroup.setStatus("current")


# Notification objects

ddmTemperatureThresholdViolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 0, 1, 0, 1)
)
ddmTemperatureThresholdViolated.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ALCATEL-IND1-PORT-MIB", "ddmNotificationType"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTemperature"))
)
if mibBuilder.loadTexts:
    ddmTemperatureThresholdViolated.setStatus(
        "current"
    )

ddmVoltageThresholdViolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 0, 1, 0, 2)
)
ddmVoltageThresholdViolated.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ALCATEL-IND1-PORT-MIB", "ddmNotificationType"),
        ("ALCATEL-IND1-PORT-MIB", "ddmSupplyVoltage"))
)
if mibBuilder.loadTexts:
    ddmVoltageThresholdViolated.setStatus(
        "current"
    )

ddmCurrentThresholdViolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 0, 1, 0, 3)
)
ddmCurrentThresholdViolated.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ALCATEL-IND1-PORT-MIB", "ddmNotificationType"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxBiasCurrent"))
)
if mibBuilder.loadTexts:
    ddmCurrentThresholdViolated.setStatus(
        "current"
    )

ddmTxPowerThresholdViolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 0, 1, 0, 4)
)
ddmTxPowerThresholdViolated.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ALCATEL-IND1-PORT-MIB", "ddmNotificationType"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxOutputPower"))
)
if mibBuilder.loadTexts:
    ddmTxPowerThresholdViolated.setStatus(
        "current"
    )

ddmRxPowerThresholdViolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 0, 1, 0, 5)
)
ddmRxPowerThresholdViolated.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ALCATEL-IND1-PORT-MIB", "ddmNotificationType"),
        ("ALCATEL-IND1-PORT-MIB", "ddmRxOpticalPower"))
)
if mibBuilder.loadTexts:
    ddmRxPowerThresholdViolated.setStatus(
        "current"
    )

esmViolationRecoveryTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 0, 2, 0, 1)
)
esmViolationRecoveryTimeout.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ALCATEL-IND1-PORT-MIB", "esmViolationRecoveryNotificationType"))
)
if mibBuilder.loadTexts:
    esmViolationRecoveryTimeout.setStatus(
        "current"
    )

esmDrvTrapDropsLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 6, 0, 1)
)
esmDrvTrapDropsLink.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "esmPortSlot"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortIF"),
        ("IF-MIB", "ifInErrors"),
        ("IF-MIB", "ifOutErrors"),
        ("ALCATEL-IND1-PORT-MIB", "esmDrvTrapDrops"))
)
if mibBuilder.loadTexts:
    esmDrvTrapDropsLink.setStatus(
        "current"
    )

e2eStackTopoChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 6, 0, 2)
)
e2eStackTopoChangeTrap.setObjects(
    ("ALCATEL-IND1-PORT-MIB", "esmE2EFlowVlan")
)
if mibBuilder.loadTexts:
    e2eStackTopoChangeTrap.setStatus(
        "current"
    )


# Notifications groups

alcPortNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2, 2, 4)
)
alcPortNotificationGroup.setObjects(
    ("ALCATEL-IND1-PORT-MIB", "esmDrvTrapDropsLink")
)
if mibBuilder.loadTexts:
    alcPortNotificationGroup.setStatus(
        "current"
    )

ddmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2, 2, 8)
)
ddmNotificationsGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "ddmTemperatureThresholdViolated"),
        ("ALCATEL-IND1-PORT-MIB", "ddmVoltageThresholdViolated"),
        ("ALCATEL-IND1-PORT-MIB", "ddmCurrentThresholdViolated"),
        ("ALCATEL-IND1-PORT-MIB", "ddmTxPowerThresholdViolated"),
        ("ALCATEL-IND1-PORT-MIB", "ddmRxPowerThresholdViolated"))
)
if mibBuilder.loadTexts:
    ddmNotificationsGroup.setStatus(
        "current"
    )

violationNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2, 2, 10)
)
violationNotificationsGroup.setObjects(
    ("ALCATEL-IND1-PORT-MIB", "esmViolationRecoveryTimeout")
)
if mibBuilder.loadTexts:
    violationNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

esmConfPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2, 1, 1)
)
esmConfPortCompliance.setObjects(
      *(("ALCATEL-IND1-PORT-MIB", "esmConfMIBGroup"),
        ("ALCATEL-IND1-PORT-MIB", "esmDetectedConfMIBGroup"),
        ("ALCATEL-IND1-PORT-MIB", "esmPortModeMIBGroup"),
        ("ALCATEL-IND1-PORT-MIB", "ddmInfoGroup"),
        ("ALCATEL-IND1-PORT-MIB", "ddmConfigGroup"),
        ("ALCATEL-IND1-PORT-MIB", "ddmNotificationsGroup"),
        ("ALCATEL-IND1-PORT-MIB", "violationRecoveryGroup"),
        ("ALCATEL-IND1-PORT-MIB", "violationNotificationsGroup"))
)
if mibBuilder.loadTexts:
    esmConfPortCompliance.setStatus(
        "current"
    )

alcEtherStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 5, 1, 2, 1, 2)
)
alcEtherStatsCompliance.setObjects(
    ("ALCATEL-IND1-PORT-MIB", "alcEtherStatsMIBGroup")
)
if mibBuilder.loadTexts:
    alcEtherStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-PORT-MIB",
    **{"alcatelIND1PortMIB": alcatelIND1PortMIB,
       "alcatelIND1PortNotifications": alcatelIND1PortNotifications,
       "ddmNotifications": ddmNotifications,
       "ddmTemperatureThresholdViolated": ddmTemperatureThresholdViolated,
       "ddmVoltageThresholdViolated": ddmVoltageThresholdViolated,
       "ddmCurrentThresholdViolated": ddmCurrentThresholdViolated,
       "ddmTxPowerThresholdViolated": ddmTxPowerThresholdViolated,
       "ddmRxPowerThresholdViolated": ddmRxPowerThresholdViolated,
       "esmViolationNotifications": esmViolationNotifications,
       "esmViolationRecoveryTimeout": esmViolationRecoveryTimeout,
       "alcatelIND1PortMIBObjects": alcatelIND1PortMIBObjects,
       "esmConfTrap": esmConfTrap,
       "esmDrvTrapDrops": esmDrvTrapDrops,
       "physicalPort": physicalPort,
       "esmConfTable": esmConfTable,
       "esmConfEntry": esmConfEntry,
       "esmPortSlot": esmPortSlot,
       "esmPortIF": esmPortIF,
       "esmPortAutoSpeed": esmPortAutoSpeed,
       "esmPortAutoDuplexMode": esmPortAutoDuplexMode,
       "esmPortCfgSpeed": esmPortCfgSpeed,
       "esmPortCfgDuplexMode": esmPortCfgDuplexMode,
       "esmPortCfgIFG": esmPortCfgIFG,
       "esmPortPauseSlotTime": esmPortPauseSlotTime,
       "esmPortMaxFloodRate": esmPortMaxFloodRate,
       "esmPortFloodMcastEnable": esmPortFloodMcastEnable,
       "esmPortCfgMaxFrameSize": esmPortCfgMaxFrameSize,
       "esmPortCfgLongEnable": esmPortCfgLongEnable,
       "esmPortCfgRuntEnable": esmPortCfgRuntEnable,
       "esmPortCfgRuntSize": esmPortCfgRuntSize,
       "esmPortCfgAutoNegotiation": esmPortCfgAutoNegotiation,
       "esmPortCfgCrossover": esmPortCfgCrossover,
       "esmPortCfgFlow": esmPortCfgFlow,
       "esmPortCfgHybridActiveType": esmPortCfgHybridActiveType,
       "esmPortCfgHybridMode": esmPortCfgHybridMode,
       "esmPortOperationalHybridType": esmPortOperationalHybridType,
       "esmPortCfgMMULowWaterMarkCellSetLimit": esmPortCfgMMULowWaterMarkCellSetLimit,
       "esmPortCfgMMUDynamicCellSetLimit": esmPortCfgMMUDynamicCellSetLimit,
       "esmPortViolationBitMap": esmPortViolationBitMap,
       "esmPortViolationClearAll": esmPortViolationClearAll,
       "esmPortFloodBcastEnable": esmPortFloodBcastEnable,
       "esmPortFloodUnknownUcastEnable": esmPortFloodUnknownUcastEnable,
       "esmPortMaxUnknownUcastFloodRate": esmPortMaxUnknownUcastFloodRate,
       "esmPortMaxMcastFloodRate": esmPortMaxMcastFloodRate,
       "esmPortMaxFloodRateLimit": esmPortMaxFloodRateLimit,
       "esmPortMaxUnknownUcastFloodRateLimit": esmPortMaxUnknownUcastFloodRateLimit,
       "esmPortMaxMcastFloodRateLimit": esmPortMaxMcastFloodRateLimit,
       "esmPortCfgSFPType": esmPortCfgSFPType,
       "alcetherStatsTable": alcetherStatsTable,
       "alcetherStatsEntry": alcetherStatsEntry,
       "alcetherClearStats": alcetherClearStats,
       "alcetherLastClearStats": alcetherLastClearStats,
       "alcetherStatsCRCAlignErrors": alcetherStatsCRCAlignErrors,
       "alcetherStatsRxUndersizePkts": alcetherStatsRxUndersizePkts,
       "alcetherStatsTxUndersizePkts": alcetherStatsTxUndersizePkts,
       "alcetherStatsTxOversizePkts": alcetherStatsTxOversizePkts,
       "alcetherStatsRxJabbers": alcetherStatsRxJabbers,
       "alcetherStatsRxCollisions": alcetherStatsRxCollisions,
       "alcetherStatsTxCollisions": alcetherStatsTxCollisions,
       "alcetherStatsPkts64Octets": alcetherStatsPkts64Octets,
       "alcetherStatsPkts65to127Octets": alcetherStatsPkts65to127Octets,
       "alcetherStatsPkts128to255Octets": alcetherStatsPkts128to255Octets,
       "alcetherStatsPkts256to511Octets": alcetherStatsPkts256to511Octets,
       "alcetherStatsPkts512to1023Octets": alcetherStatsPkts512to1023Octets,
       "alcetherStatsPkts1024to1518Octets": alcetherStatsPkts1024to1518Octets,
       "gigaEtherStatsPkts1519to4095Octets": gigaEtherStatsPkts1519to4095Octets,
       "gigaEtherStatsPkts4096to9215Octets": gigaEtherStatsPkts4096to9215Octets,
       "alcetherStatsPkts1519to2047Octets": alcetherStatsPkts1519to2047Octets,
       "alcetherStatsPkts2048to4095Octets": alcetherStatsPkts2048to4095Octets,
       "alcetherStatsPkts4096Octets": alcetherStatsPkts4096Octets,
       "alcetherStatsRxGiantPkts": alcetherStatsRxGiantPkts,
       "alcetherStatsRxDribbleNibblePkts": alcetherStatsRxDribbleNibblePkts,
       "alcetherStatsRxLongEventPkts": alcetherStatsRxLongEventPkts,
       "alcetherStatsRxVlanTagPkts": alcetherStatsRxVlanTagPkts,
       "alcetherStatsRxControlPkts": alcetherStatsRxControlPkts,
       "alcetherStatsRxLenChkErrPkts": alcetherStatsRxLenChkErrPkts,
       "alcetherStatsRxCodeErrPkts": alcetherStatsRxCodeErrPkts,
       "alcetherStatsRxDvEventPkts": alcetherStatsRxDvEventPkts,
       "alcetherStatsRxPrevPktDropped": alcetherStatsRxPrevPktDropped,
       "alcetherStatsTx64Octets": alcetherStatsTx64Octets,
       "alcetherStatsTx65to127Octets": alcetherStatsTx65to127Octets,
       "alcetherStatsTx128to255Octets": alcetherStatsTx128to255Octets,
       "alcetherStatsTx256to511Octets": alcetherStatsTx256to511Octets,
       "alcetherStatsTx512to1023Octets": alcetherStatsTx512to1023Octets,
       "alcetherStatsTx1024to1518Octets": alcetherStatsTx1024to1518Octets,
       "alcetherStatsTx1519to2047Octets": alcetherStatsTx1519to2047Octets,
       "alcetherStatsTx2048to4095Octets": alcetherStatsTx2048to4095Octets,
       "alcetherStatsTx4096Octets": alcetherStatsTx4096Octets,
       "alcetherStatsTxRetryCount": alcetherStatsTxRetryCount,
       "alcetherStatsTxVlanTagPkts": alcetherStatsTxVlanTagPkts,
       "alcetherStatsTxControlPkts": alcetherStatsTxControlPkts,
       "alcetherStatsTxLatePkts": alcetherStatsTxLatePkts,
       "alcetherStatsTxTotalBytesOnWire": alcetherStatsTxTotalBytesOnWire,
       "alcetherStatsTxLenChkErrPkts": alcetherStatsTxLenChkErrPkts,
       "alcetherStatsTxExcDeferPkts": alcetherStatsTxExcDeferPkts,
       "esmHybridConfTable": esmHybridConfTable,
       "esmHybridConfEntry": esmHybridConfEntry,
       "esmHybridPortCfgSpeed": esmHybridPortCfgSpeed,
       "esmHybridPortCfgDuplexMode": esmHybridPortCfgDuplexMode,
       "esmHybridPortCfgAutoNegotiation": esmHybridPortCfgAutoNegotiation,
       "esmHybridPortCfgCrossover": esmHybridPortCfgCrossover,
       "esmHybridPortCfgFlow": esmHybridPortCfgFlow,
       "esmHybridPortCfgInactiveType": esmHybridPortCfgInactiveType,
       "esmHybridPortCfgSFPType": esmHybridPortCfgSFPType,
       "alcether10GigTable": alcether10GigTable,
       "alcether10GigEntry": alcether10GigEntry,
       "alcether10GigPrimary": alcether10GigPrimary,
       "ddmInfoTable": ddmInfoTable,
       "ddmInfoEntry": ddmInfoEntry,
       "ddmTemperature": ddmTemperature,
       "ddmTempLowWarning": ddmTempLowWarning,
       "ddmTempLowAlarm": ddmTempLowAlarm,
       "ddmTempHiWarning": ddmTempHiWarning,
       "ddmTempHiAlarm": ddmTempHiAlarm,
       "ddmSupplyVoltage": ddmSupplyVoltage,
       "ddmSupplyVoltageLowWarning": ddmSupplyVoltageLowWarning,
       "ddmSupplyVoltageLowAlarm": ddmSupplyVoltageLowAlarm,
       "ddmSupplyVoltageHiWarning": ddmSupplyVoltageHiWarning,
       "ddmSupplyVoltageHiAlarm": ddmSupplyVoltageHiAlarm,
       "ddmTxBiasCurrent": ddmTxBiasCurrent,
       "ddmTxBiasCurrentLowWarning": ddmTxBiasCurrentLowWarning,
       "ddmTxBiasCurrentLowAlarm": ddmTxBiasCurrentLowAlarm,
       "ddmTxBiasCurrentHiWarning": ddmTxBiasCurrentHiWarning,
       "ddmTxBiasCurrentHiAlarm": ddmTxBiasCurrentHiAlarm,
       "ddmTxOutputPower": ddmTxOutputPower,
       "ddmTxOutputPowerLowWarning": ddmTxOutputPowerLowWarning,
       "ddmTxOutputPowerLowAlarm": ddmTxOutputPowerLowAlarm,
       "ddmTxOutputPowerHiWarning": ddmTxOutputPowerHiWarning,
       "ddmTxOutputPowerHiAlarm": ddmTxOutputPowerHiAlarm,
       "ddmRxOpticalPower": ddmRxOpticalPower,
       "ddmRxOpticalPowerLowWarning": ddmRxOpticalPowerLowWarning,
       "ddmRxOpticalPowerLowAlarm": ddmRxOpticalPowerLowAlarm,
       "ddmRxOpticalPowerHiWarning": ddmRxOpticalPowerHiWarning,
       "ddmRxOpticalPowerHiAlarm": ddmRxOpticalPowerHiAlarm,
       "esmPortModeTable": esmPortModeTable,
       "esmPortModeEntry": esmPortModeEntry,
       "esmPortModeIndex": esmPortModeIndex,
       "esmPortRunningMode": esmPortRunningMode,
       "esmPortSavedMode": esmPortSavedMode,
       "esmE2EFlowVlan": esmE2EFlowVlan,
       "ddmConfiguration": ddmConfiguration,
       "ddmConfig": ddmConfig,
       "ddmTrapConfig": ddmTrapConfig,
       "ddmNotificationType": ddmNotificationType,
       "esmViolationRecovery": esmViolationRecovery,
       "esmViolationRecoveryTrap": esmViolationRecoveryTrap,
       "esmViolationRecoveryTime": esmViolationRecoveryTime,
       "esmViolationRecoveryNotificationType": esmViolationRecoveryNotificationType,
       "alcatelIND1PortMIBConformance": alcatelIND1PortMIBConformance,
       "alcatelIND1PortMIBCompliances": alcatelIND1PortMIBCompliances,
       "esmConfPortCompliance": esmConfPortCompliance,
       "alcEtherStatsCompliance": alcEtherStatsCompliance,
       "alcatelIND1PortMIBGroups": alcatelIND1PortMIBGroups,
       "esmConfMIBGroup": esmConfMIBGroup,
       "esmDetectedConfMIBGroup": esmDetectedConfMIBGroup,
       "alcEtherStatsMIBGroup": alcEtherStatsMIBGroup,
       "alcPortNotificationGroup": alcPortNotificationGroup,
       "esmPortModeMIBGroup": esmPortModeMIBGroup,
       "ddmInfoGroup": ddmInfoGroup,
       "ddmConfigGroup": ddmConfigGroup,
       "ddmNotificationsGroup": ddmNotificationsGroup,
       "violationRecoveryGroup": violationRecoveryGroup,
       "violationNotificationsGroup": violationNotificationsGroup,
       "esmDrvTrapDropsLink": esmDrvTrapDropsLink,
       "e2eStackTopoChangeTrap": e2eStackTopoChangeTrap}
)
