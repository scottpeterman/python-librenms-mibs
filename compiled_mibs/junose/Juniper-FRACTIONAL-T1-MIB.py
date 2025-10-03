# SNMP MIB module (Juniper-FRACTIONAL-T1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-FRACTIONAL-T1-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:06:32 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniNextIfIndex,
 JuniTimeSlotMap) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniNextIfIndex",
    "JuniTimeSlotMap")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

juniFt1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6)
)
if mibBuilder.loadTexts:
    juniFt1MIB.setRevisions(
        ("2002-09-16 21:44",
         "2000-09-26 17:30",
         "1999-07-14 00:00",
         "1998-11-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniFt1Objects_ObjectIdentity = ObjectIdentity
juniFt1Objects = _JuniFt1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1)
)
_JuniFt1NextIfIndex_Type = JuniNextIfIndex
_JuniFt1NextIfIndex_Object = MibScalar
juniFt1NextIfIndex = _JuniFt1NextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 1),
    _JuniFt1NextIfIndex_Type()
)
juniFt1NextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFt1NextIfIndex.setStatus("current")
_JuniFt1IfTable_Object = MibTable
juniFt1IfTable = _JuniFt1IfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2)
)
if mibBuilder.loadTexts:
    juniFt1IfTable.setStatus("current")
_JuniFt1IfEntry_Object = MibTableRow
juniFt1IfEntry = _JuniFt1IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1)
)
juniFt1IfEntry.setIndexNames(
    (0, "Juniper-FRACTIONAL-T1-MIB", "juniFt1IfIndex"),
)
if mibBuilder.loadTexts:
    juniFt1IfEntry.setStatus("current")
_JuniFt1IfIndex_Type = InterfaceIndex
_JuniFt1IfIndex_Object = MibTableColumn
juniFt1IfIndex = _JuniFt1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 1),
    _JuniFt1IfIndex_Type()
)
juniFt1IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniFt1IfIndex.setStatus("current")
_JuniFt1IfRowStatus_Type = RowStatus
_JuniFt1IfRowStatus_Object = MibTableColumn
juniFt1IfRowStatus = _JuniFt1IfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 2),
    _JuniFt1IfRowStatus_Type()
)
juniFt1IfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFt1IfRowStatus.setStatus("current")
_JuniFt1IfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniFt1IfLowerIfIndex_Object = MibTableColumn
juniFt1IfLowerIfIndex = _JuniFt1IfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 3),
    _JuniFt1IfLowerIfIndex_Type()
)
juniFt1IfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFt1IfLowerIfIndex.setStatus("current")
_JuniFt1IfTimeSlotMap_Type = JuniTimeSlotMap
_JuniFt1IfTimeSlotMap_Object = MibTableColumn
juniFt1IfTimeSlotMap = _JuniFt1IfTimeSlotMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 4),
    _JuniFt1IfTimeSlotMap_Type()
)
juniFt1IfTimeSlotMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFt1IfTimeSlotMap.setStatus("current")


class _JuniFt1IfTimeSlotRate_Type(Integer32):
    """Custom type juniFt1IfTimeSlotRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nx56kbps", 0),
          ("nx64kbps", 1))
    )


_JuniFt1IfTimeSlotRate_Type.__name__ = "Integer32"
_JuniFt1IfTimeSlotRate_Object = MibTableColumn
juniFt1IfTimeSlotRate = _JuniFt1IfTimeSlotRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 5),
    _JuniFt1IfTimeSlotRate_Type()
)
juniFt1IfTimeSlotRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFt1IfTimeSlotRate.setStatus("current")


class _JuniFt1IfDataPolarity_Type(Integer32):
    """Custom type juniFt1IfDataPolarity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("inverted", 1))
    )


_JuniFt1IfDataPolarity_Type.__name__ = "Integer32"
_JuniFt1IfDataPolarity_Object = MibTableColumn
juniFt1IfDataPolarity = _JuniFt1IfDataPolarity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 6),
    _JuniFt1IfDataPolarity_Type()
)
juniFt1IfDataPolarity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFt1IfDataPolarity.setStatus("obsolete")


class _JuniFt1IfLoopbackConfig_Type(Integer32):
    """Custom type juniFt1IfLoopbackConfig based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noLoop", 0),
          ("loop", 1))
    )


_JuniFt1IfLoopbackConfig_Type.__name__ = "Integer32"
_JuniFt1IfLoopbackConfig_Object = MibTableColumn
juniFt1IfLoopbackConfig = _JuniFt1IfLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 7),
    _JuniFt1IfLoopbackConfig_Type()
)
juniFt1IfLoopbackConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFt1IfLoopbackConfig.setStatus("current")
_JuniFt1Conformance_ObjectIdentity = ObjectIdentity
juniFt1Conformance = _JuniFt1Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4)
)
_JuniFt1Compliances_ObjectIdentity = ObjectIdentity
juniFt1Compliances = _JuniFt1Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1)
)
_JuniFt1Groups_ObjectIdentity = ObjectIdentity
juniFt1Groups = _JuniFt1Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2)
)

# Managed Objects groups

juniFt1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2, 1)
)
juniFt1Group.setObjects(
      *(("Juniper-FRACTIONAL-T1-MIB", "juniFt1NextIfIndex"),
        ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfRowStatus"),
        ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfLowerIfIndex"),
        ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfTimeSlotMap"),
        ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfTimeSlotRate"),
        ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfDataPolarity"),
        ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfLoopbackConfig"))
)
if mibBuilder.loadTexts:
    juniFt1Group.setStatus("obsolete")

juniFt1Group2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2, 2)
)
juniFt1Group2.setObjects(
      *(("Juniper-FRACTIONAL-T1-MIB", "juniFt1NextIfIndex"),
        ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfRowStatus"),
        ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfLowerIfIndex"),
        ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfTimeSlotMap"),
        ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfTimeSlotRate"),
        ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfLoopbackConfig"))
)
if mibBuilder.loadTexts:
    juniFt1Group2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniFt1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1, 1)
)
juniFt1Compliance.setObjects(
    ("Juniper-FRACTIONAL-T1-MIB", "juniFt1Group")
)
if mibBuilder.loadTexts:
    juniFt1Compliance.setStatus(
        "obsolete"
    )

juniFt1Compliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1, 2)
)
juniFt1Compliance2.setObjects(
    ("Juniper-FRACTIONAL-T1-MIB", "juniFt1Group2")
)
if mibBuilder.loadTexts:
    juniFt1Compliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-FRACTIONAL-T1-MIB",
    **{"juniFt1MIB": juniFt1MIB,
       "juniFt1Objects": juniFt1Objects,
       "juniFt1NextIfIndex": juniFt1NextIfIndex,
       "juniFt1IfTable": juniFt1IfTable,
       "juniFt1IfEntry": juniFt1IfEntry,
       "juniFt1IfIndex": juniFt1IfIndex,
       "juniFt1IfRowStatus": juniFt1IfRowStatus,
       "juniFt1IfLowerIfIndex": juniFt1IfLowerIfIndex,
       "juniFt1IfTimeSlotMap": juniFt1IfTimeSlotMap,
       "juniFt1IfTimeSlotRate": juniFt1IfTimeSlotRate,
       "juniFt1IfDataPolarity": juniFt1IfDataPolarity,
       "juniFt1IfLoopbackConfig": juniFt1IfLoopbackConfig,
       "juniFt1Conformance": juniFt1Conformance,
       "juniFt1Compliances": juniFt1Compliances,
       "juniFt1Compliance": juniFt1Compliance,
       "juniFt1Compliance2": juniFt1Compliance2,
       "juniFt1Groups": juniFt1Groups,
       "juniFt1Group": juniFt1Group,
       "juniFt1Group2": juniFt1Group2}
)
