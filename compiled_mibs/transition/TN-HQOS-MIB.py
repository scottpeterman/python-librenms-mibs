# SNMP MIB module (TN-HQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-HQOS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:35 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(TNInterfaceIndex,
 TNRowEditorState,
 TNUnsigned8) = mibBuilder.importSymbols(
    "TN-TC",
    "TNInterfaceIndex",
    "TNRowEditorState",
    "TNUnsigned8")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnHqosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145)
)
if mibBuilder.loadTexts:
    tnHqosMib.setRevisions(
        ("2015-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TNhqosSchMode(TextualConvention, Integer32):
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
        *(("normal", 0),
          ("basic", 1),
          ("hierarchical", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TnHqosMibObjects_ObjectIdentity = ObjectIdentity
tnHqosMibObjects = _TnHqosMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1)
)
_TnHqosConfig_ObjectIdentity = ObjectIdentity
tnHqosConfig = _TnHqosConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2)
)
_TnHqosConfigInterface_ObjectIdentity = ObjectIdentity
tnHqosConfigInterface = _TnHqosConfigInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2)
)
_TnHqosConfigInterfaceTable_Object = MibTable
tnHqosConfigInterfaceTable = _TnHqosConfigInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceTable.setStatus("current")
_TnHqosConfigInterfaceEntry_Object = MibTableRow
tnHqosConfigInterfaceEntry = _TnHqosConfigInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 1, 1)
)
tnHqosConfigInterfaceEntry.setIndexNames(
    (0, "TN-HQOS-MIB", "tnHqosConfigInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceEntry.setStatus("current")
_TnHqosConfigInterfaceIfIndex_Type = TNInterfaceIndex
_TnHqosConfigInterfaceIfIndex_Object = MibTableColumn
tnHqosConfigInterfaceIfIndex = _TnHqosConfigInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 1, 1, 1),
    _TnHqosConfigInterfaceIfIndex_Type()
)
tnHqosConfigInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceIfIndex.setStatus("current")
_TnHqosConfigInterfaceSchMode_Type = TNhqosSchMode
_TnHqosConfigInterfaceSchMode_Object = MibTableColumn
tnHqosConfigInterfaceSchMode = _TnHqosConfigInterfaceSchMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 1, 1, 2),
    _TnHqosConfigInterfaceSchMode_Type()
)
tnHqosConfigInterfaceSchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceSchMode.setStatus("current")
_TnHqosConfigInterfaceHqosTable_Object = MibTable
tnHqosConfigInterfaceHqosTable = _TnHqosConfigInterfaceHqosTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosTable.setStatus("current")
_TnHqosConfigInterfaceHqosEntry_Object = MibTableRow
tnHqosConfigInterfaceHqosEntry = _TnHqosConfigInterfaceHqosEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 2, 1)
)
tnHqosConfigInterfaceHqosEntry.setIndexNames(
    (0, "TN-HQOS-MIB", "tnHqosConfigInterfaceHqosIfIndex"),
    (0, "TN-HQOS-MIB", "tnHqosConfigInterfaceHqosHqosId"),
)
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosEntry.setStatus("current")
_TnHqosConfigInterfaceHqosIfIndex_Type = TNInterfaceIndex
_TnHqosConfigInterfaceHqosIfIndex_Object = MibTableColumn
tnHqosConfigInterfaceHqosIfIndex = _TnHqosConfigInterfaceHqosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 2, 1, 1),
    _TnHqosConfigInterfaceHqosIfIndex_Type()
)
tnHqosConfigInterfaceHqosIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosIfIndex.setStatus("current")


class _TnHqosConfigInterfaceHqosHqosId_Type(Integer32):
    """Custom type tnHqosConfigInterfaceHqosHqosId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnHqosConfigInterfaceHqosHqosId_Type.__name__ = "Integer32"
_TnHqosConfigInterfaceHqosHqosId_Object = MibTableColumn
tnHqosConfigInterfaceHqosHqosId = _TnHqosConfigInterfaceHqosHqosId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 2, 1, 2),
    _TnHqosConfigInterfaceHqosHqosId_Type()
)
tnHqosConfigInterfaceHqosHqosId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosHqosId.setStatus("current")
_TnHqosConfigInterfaceHqosDwrrCount_Type = TNUnsigned8
_TnHqosConfigInterfaceHqosDwrrCount_Object = MibTableColumn
tnHqosConfigInterfaceHqosDwrrCount = _TnHqosConfigInterfaceHqosDwrrCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 2, 1, 3),
    _TnHqosConfigInterfaceHqosDwrrCount_Type()
)
tnHqosConfigInterfaceHqosDwrrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosDwrrCount.setStatus("current")
_TnHqosConfigInterfaceHqosShaperEnable_Type = TruthValue
_TnHqosConfigInterfaceHqosShaperEnable_Object = MibTableColumn
tnHqosConfigInterfaceHqosShaperEnable = _TnHqosConfigInterfaceHqosShaperEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 2, 1, 4),
    _TnHqosConfigInterfaceHqosShaperEnable_Type()
)
tnHqosConfigInterfaceHqosShaperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosShaperEnable.setStatus("current")
_TnHqosConfigInterfaceHqosShaperRate_Type = Unsigned32
_TnHqosConfigInterfaceHqosShaperRate_Object = MibTableColumn
tnHqosConfigInterfaceHqosShaperRate = _TnHqosConfigInterfaceHqosShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 2, 1, 5),
    _TnHqosConfigInterfaceHqosShaperRate_Type()
)
tnHqosConfigInterfaceHqosShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosShaperRate.setStatus("current")
_TnHqosConfigInterfaceHqosMinRate_Type = Unsigned32
_TnHqosConfigInterfaceHqosMinRate_Object = MibTableColumn
tnHqosConfigInterfaceHqosMinRate = _TnHqosConfigInterfaceHqosMinRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 2, 1, 6),
    _TnHqosConfigInterfaceHqosMinRate_Type()
)
tnHqosConfigInterfaceHqosMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosMinRate.setStatus("current")
_TnHqosConfigInterfaceHqosAction_Type = TNRowEditorState
_TnHqosConfigInterfaceHqosAction_Object = MibTableColumn
tnHqosConfigInterfaceHqosAction = _TnHqosConfigInterfaceHqosAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 2, 1, 10000),
    _TnHqosConfigInterfaceHqosAction_Type()
)
tnHqosConfigInterfaceHqosAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosAction.setStatus("current")
_TnHqosConfigInterfaceHqosTableRowEditor_ObjectIdentity = ObjectIdentity
tnHqosConfigInterfaceHqosTableRowEditor = _TnHqosConfigInterfaceHqosTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 3)
)
_TnHqosConfigInterfaceHqosTableRowEditorIfIndex_Type = TNInterfaceIndex
_TnHqosConfigInterfaceHqosTableRowEditorIfIndex_Object = MibScalar
tnHqosConfigInterfaceHqosTableRowEditorIfIndex = _TnHqosConfigInterfaceHqosTableRowEditorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 3, 1),
    _TnHqosConfigInterfaceHqosTableRowEditorIfIndex_Type()
)
tnHqosConfigInterfaceHqosTableRowEditorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosTableRowEditorIfIndex.setStatus("current")


class _TnHqosConfigInterfaceHqosTableRowEditorHqosId_Type(Integer32):
    """Custom type tnHqosConfigInterfaceHqosTableRowEditorHqosId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnHqosConfigInterfaceHqosTableRowEditorHqosId_Type.__name__ = "Integer32"
_TnHqosConfigInterfaceHqosTableRowEditorHqosId_Object = MibScalar
tnHqosConfigInterfaceHqosTableRowEditorHqosId = _TnHqosConfigInterfaceHqosTableRowEditorHqosId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 3, 2),
    _TnHqosConfigInterfaceHqosTableRowEditorHqosId_Type()
)
tnHqosConfigInterfaceHqosTableRowEditorHqosId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosTableRowEditorHqosId.setStatus("current")
_TnHqosConfigInterfaceHqosTableRowEditorDwrrCount_Type = TNUnsigned8
_TnHqosConfigInterfaceHqosTableRowEditorDwrrCount_Object = MibScalar
tnHqosConfigInterfaceHqosTableRowEditorDwrrCount = _TnHqosConfigInterfaceHqosTableRowEditorDwrrCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 3, 3),
    _TnHqosConfigInterfaceHqosTableRowEditorDwrrCount_Type()
)
tnHqosConfigInterfaceHqosTableRowEditorDwrrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosTableRowEditorDwrrCount.setStatus("current")
_TnHqosConfigInterfaceHqosTableRowEditorShaperEnable_Type = TruthValue
_TnHqosConfigInterfaceHqosTableRowEditorShaperEnable_Object = MibScalar
tnHqosConfigInterfaceHqosTableRowEditorShaperEnable = _TnHqosConfigInterfaceHqosTableRowEditorShaperEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 3, 4),
    _TnHqosConfigInterfaceHqosTableRowEditorShaperEnable_Type()
)
tnHqosConfigInterfaceHqosTableRowEditorShaperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosTableRowEditorShaperEnable.setStatus("current")
_TnHqosConfigInterfaceHqosTableRowEditorShaperRate_Type = Unsigned32
_TnHqosConfigInterfaceHqosTableRowEditorShaperRate_Object = MibScalar
tnHqosConfigInterfaceHqosTableRowEditorShaperRate = _TnHqosConfigInterfaceHqosTableRowEditorShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 3, 5),
    _TnHqosConfigInterfaceHqosTableRowEditorShaperRate_Type()
)
tnHqosConfigInterfaceHqosTableRowEditorShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosTableRowEditorShaperRate.setStatus("current")
_TnHqosConfigInterfaceHqosTableRowEditorMinRate_Type = Unsigned32
_TnHqosConfigInterfaceHqosTableRowEditorMinRate_Object = MibScalar
tnHqosConfigInterfaceHqosTableRowEditorMinRate = _TnHqosConfigInterfaceHqosTableRowEditorMinRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 3, 6),
    _TnHqosConfigInterfaceHqosTableRowEditorMinRate_Type()
)
tnHqosConfigInterfaceHqosTableRowEditorMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosTableRowEditorMinRate.setStatus("current")
_TnHqosConfigInterfaceHqosTableRowEditorAction_Type = TNRowEditorState
_TnHqosConfigInterfaceHqosTableRowEditorAction_Object = MibScalar
tnHqosConfigInterfaceHqosTableRowEditorAction = _TnHqosConfigInterfaceHqosTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 3, 10000),
    _TnHqosConfigInterfaceHqosTableRowEditorAction_Type()
)
tnHqosConfigInterfaceHqosTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosTableRowEditorAction.setStatus("current")
_TnHqosConfigInterfaceHqosQueueTable_Object = MibTable
tnHqosConfigInterfaceHqosQueueTable = _TnHqosConfigInterfaceHqosQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosQueueTable.setStatus("current")
_TnHqosConfigInterfaceHqosQueueEntry_Object = MibTableRow
tnHqosConfigInterfaceHqosQueueEntry = _TnHqosConfigInterfaceHqosQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 4, 1)
)
tnHqosConfigInterfaceHqosQueueEntry.setIndexNames(
    (0, "TN-HQOS-MIB", "tnHqosConfigInterfaceHqosQueueIfIndex"),
    (0, "TN-HQOS-MIB", "tnHqosConfigInterfaceHqosQueueHqosId"),
    (0, "TN-HQOS-MIB", "tnHqosConfigInterfaceHqosQueueQueue"),
)
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosQueueEntry.setStatus("current")
_TnHqosConfigInterfaceHqosQueueIfIndex_Type = TNInterfaceIndex
_TnHqosConfigInterfaceHqosQueueIfIndex_Object = MibTableColumn
tnHqosConfigInterfaceHqosQueueIfIndex = _TnHqosConfigInterfaceHqosQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 4, 1, 1),
    _TnHqosConfigInterfaceHqosQueueIfIndex_Type()
)
tnHqosConfigInterfaceHqosQueueIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosQueueIfIndex.setStatus("current")


class _TnHqosConfigInterfaceHqosQueueHqosId_Type(Integer32):
    """Custom type tnHqosConfigInterfaceHqosQueueHqosId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnHqosConfigInterfaceHqosQueueHqosId_Type.__name__ = "Integer32"
_TnHqosConfigInterfaceHqosQueueHqosId_Object = MibTableColumn
tnHqosConfigInterfaceHqosQueueHqosId = _TnHqosConfigInterfaceHqosQueueHqosId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 4, 1, 2),
    _TnHqosConfigInterfaceHqosQueueHqosId_Type()
)
tnHqosConfigInterfaceHqosQueueHqosId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosQueueHqosId.setStatus("current")


class _TnHqosConfigInterfaceHqosQueueQueue_Type(Integer32):
    """Custom type tnHqosConfigInterfaceHqosQueueQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnHqosConfigInterfaceHqosQueueQueue_Type.__name__ = "Integer32"
_TnHqosConfigInterfaceHqosQueueQueue_Object = MibTableColumn
tnHqosConfigInterfaceHqosQueueQueue = _TnHqosConfigInterfaceHqosQueueQueue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 4, 1, 3),
    _TnHqosConfigInterfaceHqosQueueQueue_Type()
)
tnHqosConfigInterfaceHqosQueueQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosQueueQueue.setStatus("current")
_TnHqosConfigInterfaceHqosQueueShaperEnable_Type = TruthValue
_TnHqosConfigInterfaceHqosQueueShaperEnable_Object = MibTableColumn
tnHqosConfigInterfaceHqosQueueShaperEnable = _TnHqosConfigInterfaceHqosQueueShaperEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 4, 1, 4),
    _TnHqosConfigInterfaceHqosQueueShaperEnable_Type()
)
tnHqosConfigInterfaceHqosQueueShaperEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosQueueShaperEnable.setStatus("current")
_TnHqosConfigInterfaceHqosQueueShaperRate_Type = Unsigned32
_TnHqosConfigInterfaceHqosQueueShaperRate_Object = MibTableColumn
tnHqosConfigInterfaceHqosQueueShaperRate = _TnHqosConfigInterfaceHqosQueueShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 4, 1, 5),
    _TnHqosConfigInterfaceHqosQueueShaperRate_Type()
)
tnHqosConfigInterfaceHqosQueueShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosQueueShaperRate.setStatus("current")
_TnHqosConfigInterfaceHqosQueueSchedulerWeight_Type = TNUnsigned8
_TnHqosConfigInterfaceHqosQueueSchedulerWeight_Object = MibTableColumn
tnHqosConfigInterfaceHqosQueueSchedulerWeight = _TnHqosConfigInterfaceHqosQueueSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 2, 4, 1, 6),
    _TnHqosConfigInterfaceHqosQueueSchedulerWeight_Type()
)
tnHqosConfigInterfaceHqosQueueSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosQueueSchedulerWeight.setStatus("current")
_TnHqosConfigHqos_ObjectIdentity = ObjectIdentity
tnHqosConfigHqos = _TnHqosConfigHqos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 1, 2, 4)
)
_TnHqosMibConformance_ObjectIdentity = ObjectIdentity
tnHqosMibConformance = _TnHqosMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 2)
)
_TnHqosMibCompliances_ObjectIdentity = ObjectIdentity
tnHqosMibCompliances = _TnHqosMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 2, 1)
)
_TnHqosMibGroups_ObjectIdentity = ObjectIdentity
tnHqosMibGroups = _TnHqosMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 2, 2)
)

# Managed Objects groups

tnHqosConfigInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 2, 2, 1)
)
tnHqosConfigInterfaceTableInfoGroup.setObjects(
    ("TN-HQOS-MIB", "tnHqosConfigInterfaceSchMode")
)
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceTableInfoGroup.setStatus("current")

tnHqosConfigInterfaceHqosTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 2, 2, 2)
)
tnHqosConfigInterfaceHqosTableInfoGroup.setObjects(
      *(("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosDwrrCount"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosShaperEnable"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosShaperRate"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosMinRate"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosAction"))
)
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosTableInfoGroup.setStatus("current")

tnHqosConfigInterfaceHqosTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 2, 2, 3)
)
tnHqosConfigInterfaceHqosTableRowEditorInfoGroup.setObjects(
      *(("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosTableRowEditorIfIndex"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosTableRowEditorHqosId"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosTableRowEditorDwrrCount"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosTableRowEditorShaperEnable"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosTableRowEditorShaperRate"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosTableRowEditorMinRate"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosTableRowEditorInfoGroup.setStatus("current")

tnHqosConfigInterfaceHqosQueueTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 2, 2, 4)
)
tnHqosConfigInterfaceHqosQueueTableInfoGroup.setObjects(
      *(("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosQueueShaperEnable"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosQueueShaperRate"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosQueueSchedulerWeight"))
)
if mibBuilder.loadTexts:
    tnHqosConfigInterfaceHqosQueueTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnHqosMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 145, 2, 1, 1)
)
tnHqosMibCompliance.setObjects(
      *(("TN-HQOS-MIB", "tnHqosConfigInterfaceTableInfoGroup"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosTableInfoGroup"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosTableRowEditorInfoGroup"),
        ("TN-HQOS-MIB", "tnHqosConfigInterfaceHqosQueueTableInfoGroup"))
)
if mibBuilder.loadTexts:
    tnHqosMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-HQOS-MIB",
    **{"TNhqosSchMode": TNhqosSchMode,
       "tnHqosMib": tnHqosMib,
       "tnHqosMibObjects": tnHqosMibObjects,
       "tnHqosConfig": tnHqosConfig,
       "tnHqosConfigInterface": tnHqosConfigInterface,
       "tnHqosConfigInterfaceTable": tnHqosConfigInterfaceTable,
       "tnHqosConfigInterfaceEntry": tnHqosConfigInterfaceEntry,
       "tnHqosConfigInterfaceIfIndex": tnHqosConfigInterfaceIfIndex,
       "tnHqosConfigInterfaceSchMode": tnHqosConfigInterfaceSchMode,
       "tnHqosConfigInterfaceHqosTable": tnHqosConfigInterfaceHqosTable,
       "tnHqosConfigInterfaceHqosEntry": tnHqosConfigInterfaceHqosEntry,
       "tnHqosConfigInterfaceHqosIfIndex": tnHqosConfigInterfaceHqosIfIndex,
       "tnHqosConfigInterfaceHqosHqosId": tnHqosConfigInterfaceHqosHqosId,
       "tnHqosConfigInterfaceHqosDwrrCount": tnHqosConfigInterfaceHqosDwrrCount,
       "tnHqosConfigInterfaceHqosShaperEnable": tnHqosConfigInterfaceHqosShaperEnable,
       "tnHqosConfigInterfaceHqosShaperRate": tnHqosConfigInterfaceHqosShaperRate,
       "tnHqosConfigInterfaceHqosMinRate": tnHqosConfigInterfaceHqosMinRate,
       "tnHqosConfigInterfaceHqosAction": tnHqosConfigInterfaceHqosAction,
       "tnHqosConfigInterfaceHqosTableRowEditor": tnHqosConfigInterfaceHqosTableRowEditor,
       "tnHqosConfigInterfaceHqosTableRowEditorIfIndex": tnHqosConfigInterfaceHqosTableRowEditorIfIndex,
       "tnHqosConfigInterfaceHqosTableRowEditorHqosId": tnHqosConfigInterfaceHqosTableRowEditorHqosId,
       "tnHqosConfigInterfaceHqosTableRowEditorDwrrCount": tnHqosConfigInterfaceHqosTableRowEditorDwrrCount,
       "tnHqosConfigInterfaceHqosTableRowEditorShaperEnable": tnHqosConfigInterfaceHqosTableRowEditorShaperEnable,
       "tnHqosConfigInterfaceHqosTableRowEditorShaperRate": tnHqosConfigInterfaceHqosTableRowEditorShaperRate,
       "tnHqosConfigInterfaceHqosTableRowEditorMinRate": tnHqosConfigInterfaceHqosTableRowEditorMinRate,
       "tnHqosConfigInterfaceHqosTableRowEditorAction": tnHqosConfigInterfaceHqosTableRowEditorAction,
       "tnHqosConfigInterfaceHqosQueueTable": tnHqosConfigInterfaceHqosQueueTable,
       "tnHqosConfigInterfaceHqosQueueEntry": tnHqosConfigInterfaceHqosQueueEntry,
       "tnHqosConfigInterfaceHqosQueueIfIndex": tnHqosConfigInterfaceHqosQueueIfIndex,
       "tnHqosConfigInterfaceHqosQueueHqosId": tnHqosConfigInterfaceHqosQueueHqosId,
       "tnHqosConfigInterfaceHqosQueueQueue": tnHqosConfigInterfaceHqosQueueQueue,
       "tnHqosConfigInterfaceHqosQueueShaperEnable": tnHqosConfigInterfaceHqosQueueShaperEnable,
       "tnHqosConfigInterfaceHqosQueueShaperRate": tnHqosConfigInterfaceHqosQueueShaperRate,
       "tnHqosConfigInterfaceHqosQueueSchedulerWeight": tnHqosConfigInterfaceHqosQueueSchedulerWeight,
       "tnHqosConfigHqos": tnHqosConfigHqos,
       "tnHqosMibConformance": tnHqosMibConformance,
       "tnHqosMibCompliances": tnHqosMibCompliances,
       "tnHqosMibCompliance": tnHqosMibCompliance,
       "tnHqosMibGroups": tnHqosMibGroups,
       "tnHqosConfigInterfaceTableInfoGroup": tnHqosConfigInterfaceTableInfoGroup,
       "tnHqosConfigInterfaceHqosTableInfoGroup": tnHqosConfigInterfaceHqosTableInfoGroup,
       "tnHqosConfigInterfaceHqosTableRowEditorInfoGroup": tnHqosConfigInterfaceHqosTableRowEditorInfoGroup,
       "tnHqosConfigInterfaceHqosQueueTableInfoGroup": tnHqosConfigInterfaceHqosQueueTableInfoGroup}
)
