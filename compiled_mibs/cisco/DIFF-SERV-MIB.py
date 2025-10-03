# SNMP MIB module (DIFF-SERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\DIFF-SERV-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:17 2025
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

(rlExperience,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "rlExperience")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

diffServMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1)
)
if mibBuilder.loadTexts:
    diffServMib.setRevisions(
        ("1999-07-19 01:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Dscp(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class MFClassifierL4Port(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_DiffServObjects_ObjectIdentity = ObjectIdentity
diffServObjects = _DiffServObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 1)
)
_DiffServMFClassifierUnique_Type = TestAndIncr
_DiffServMFClassifierUnique_Object = MibScalar
diffServMFClassifierUnique = _DiffServMFClassifierUnique_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 1, 1),
    _DiffServMFClassifierUnique_Type()
)
diffServMFClassifierUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServMFClassifierUnique.setStatus("current")
_DiffServClassifierUnique_Type = TestAndIncr
_DiffServClassifierUnique_Object = MibScalar
diffServClassifierUnique = _DiffServClassifierUnique_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 1, 2),
    _DiffServClassifierUnique_Type()
)
diffServClassifierUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassifierUnique.setStatus("current")
_DiffServTBMeterUnique_Type = TestAndIncr
_DiffServTBMeterUnique_Object = MibScalar
diffServTBMeterUnique = _DiffServTBMeterUnique_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 1, 3),
    _DiffServTBMeterUnique_Type()
)
diffServTBMeterUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServTBMeterUnique.setStatus("current")
_DiffServActionUnique_Type = TestAndIncr
_DiffServActionUnique_Object = MibScalar
diffServActionUnique = _DiffServActionUnique_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 1, 4),
    _DiffServActionUnique_Type()
)
diffServActionUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServActionUnique.setStatus("current")
_DiffServQueueUnique_Type = TestAndIncr
_DiffServQueueUnique_Object = MibScalar
diffServQueueUnique = _DiffServQueueUnique_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 1, 5),
    _DiffServQueueUnique_Type()
)
diffServQueueUnique.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServQueueUnique.setStatus("current")
_DiffServTables_ObjectIdentity = ObjectIdentity
diffServTables = _DiffServTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2)
)
_DiffServAggregateTable_Object = MibTable
diffServAggregateTable = _DiffServAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 1)
)
if mibBuilder.loadTexts:
    diffServAggregateTable.setStatus("current")
_DiffServAggregateEntry_Object = MibTableRow
diffServAggregateEntry = _DiffServAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 1, 1)
)
diffServAggregateEntry.setIndexNames(
    (0, "DIFF-SERV-MIB", "diffServAggregateDSCP"),
)
if mibBuilder.loadTexts:
    diffServAggregateEntry.setStatus("current")
_DiffServAggregateDSCP_Type = Dscp
_DiffServAggregateDSCP_Object = MibTableColumn
diffServAggregateDSCP = _DiffServAggregateDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 1, 1, 1),
    _DiffServAggregateDSCP_Type()
)
diffServAggregateDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAggregateDSCP.setStatus("current")
_DiffServMFClassifierTable_Object = MibTable
diffServMFClassifierTable = _DiffServMFClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2)
)
if mibBuilder.loadTexts:
    diffServMFClassifierTable.setStatus("current")
_DiffServMFClassifierEntry_Object = MibTableRow
diffServMFClassifierEntry = _DiffServMFClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2, 1)
)
diffServMFClassifierEntry.setIndexNames(
    (0, "DIFF-SERV-MIB", "diffServMFClassifierIndex"),
)
if mibBuilder.loadTexts:
    diffServMFClassifierEntry.setStatus("current")


class _DiffServMFClassifierIndex_Type(Integer32):
    """Custom type diffServMFClassifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DiffServMFClassifierIndex_Type.__name__ = "Integer32"
_DiffServMFClassifierIndex_Object = MibTableColumn
diffServMFClassifierIndex = _DiffServMFClassifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2, 1, 1),
    _DiffServMFClassifierIndex_Type()
)
diffServMFClassifierIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServMFClassifierIndex.setStatus("current")
_DiffServMFClassifierAddrType_Type = InetAddressType
_DiffServMFClassifierAddrType_Object = MibTableColumn
diffServMFClassifierAddrType = _DiffServMFClassifierAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2, 1, 2),
    _DiffServMFClassifierAddrType_Type()
)
diffServMFClassifierAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMFClassifierAddrType.setStatus("current")
_DiffServMFClassifierDstAddr_Type = InetAddress
_DiffServMFClassifierDstAddr_Object = MibTableColumn
diffServMFClassifierDstAddr = _DiffServMFClassifierDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2, 1, 3),
    _DiffServMFClassifierDstAddr_Type()
)
diffServMFClassifierDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMFClassifierDstAddr.setStatus("current")
_DiffServMFClassifierDstAddrMask_Type = InetAddress
_DiffServMFClassifierDstAddrMask_Object = MibTableColumn
diffServMFClassifierDstAddrMask = _DiffServMFClassifierDstAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2, 1, 4),
    _DiffServMFClassifierDstAddrMask_Type()
)
diffServMFClassifierDstAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMFClassifierDstAddrMask.setStatus("current")
_DiffServMFClassifierSrcAddr_Type = InetAddress
_DiffServMFClassifierSrcAddr_Object = MibTableColumn
diffServMFClassifierSrcAddr = _DiffServMFClassifierSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2, 1, 5),
    _DiffServMFClassifierSrcAddr_Type()
)
diffServMFClassifierSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMFClassifierSrcAddr.setStatus("current")
_DiffServMFClassifierSrcAddrMask_Type = InetAddress
_DiffServMFClassifierSrcAddrMask_Object = MibTableColumn
diffServMFClassifierSrcAddrMask = _DiffServMFClassifierSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2, 1, 6),
    _DiffServMFClassifierSrcAddrMask_Type()
)
diffServMFClassifierSrcAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMFClassifierSrcAddrMask.setStatus("current")


class _DiffServMFClassifierDscp_Type(Integer32):
    """Custom type diffServMFClassifierDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_DiffServMFClassifierDscp_Type.__name__ = "Integer32"
_DiffServMFClassifierDscp_Object = MibTableColumn
diffServMFClassifierDscp = _DiffServMFClassifierDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2, 1, 7),
    _DiffServMFClassifierDscp_Type()
)
diffServMFClassifierDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMFClassifierDscp.setStatus("current")


class _DiffServMFClassifierProtocol_Type(Integer32):
    """Custom type diffServMFClassifierProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DiffServMFClassifierProtocol_Type.__name__ = "Integer32"
_DiffServMFClassifierProtocol_Object = MibTableColumn
diffServMFClassifierProtocol = _DiffServMFClassifierProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2, 1, 8),
    _DiffServMFClassifierProtocol_Type()
)
diffServMFClassifierProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMFClassifierProtocol.setStatus("current")
_DiffServMFClassifierDstL4PortMin_Type = MFClassifierL4Port
_DiffServMFClassifierDstL4PortMin_Object = MibTableColumn
diffServMFClassifierDstL4PortMin = _DiffServMFClassifierDstL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2, 1, 9),
    _DiffServMFClassifierDstL4PortMin_Type()
)
diffServMFClassifierDstL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMFClassifierDstL4PortMin.setStatus("current")
_DiffServMFClassifierDstL4PortMax_Type = MFClassifierL4Port
_DiffServMFClassifierDstL4PortMax_Object = MibTableColumn
diffServMFClassifierDstL4PortMax = _DiffServMFClassifierDstL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2, 1, 10),
    _DiffServMFClassifierDstL4PortMax_Type()
)
diffServMFClassifierDstL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMFClassifierDstL4PortMax.setStatus("current")
_DiffServMFClassifierSrcL4PortMin_Type = MFClassifierL4Port
_DiffServMFClassifierSrcL4PortMin_Object = MibTableColumn
diffServMFClassifierSrcL4PortMin = _DiffServMFClassifierSrcL4PortMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2, 1, 11),
    _DiffServMFClassifierSrcL4PortMin_Type()
)
diffServMFClassifierSrcL4PortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMFClassifierSrcL4PortMin.setStatus("current")
_DiffServMFClassifierSrcL4PortMax_Type = MFClassifierL4Port
_DiffServMFClassifierSrcL4PortMax_Object = MibTableColumn
diffServMFClassifierSrcL4PortMax = _DiffServMFClassifierSrcL4PortMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2, 1, 12),
    _DiffServMFClassifierSrcL4PortMax_Type()
)
diffServMFClassifierSrcL4PortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMFClassifierSrcL4PortMax.setStatus("current")
_DiffServMFClassifierStatus_Type = RowStatus
_DiffServMFClassifierStatus_Object = MibTableColumn
diffServMFClassifierStatus = _DiffServMFClassifierStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 2, 1, 13),
    _DiffServMFClassifierStatus_Type()
)
diffServMFClassifierStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMFClassifierStatus.setStatus("current")
_DiffServClassifierTable_Object = MibTable
diffServClassifierTable = _DiffServClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 3)
)
if mibBuilder.loadTexts:
    diffServClassifierTable.setStatus("current")
_DiffServClassifierEntry_Object = MibTableRow
diffServClassifierEntry = _DiffServClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 3, 1)
)
diffServClassifierEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DIFF-SERV-MIB", "diffServInterfaceDirection"),
    (0, "DIFF-SERV-MIB", "diffServClassifierNumber"),
)
if mibBuilder.loadTexts:
    diffServClassifierEntry.setStatus("current")


class _DiffServInterfaceDirection_Type(Integer32):
    """Custom type diffServInterfaceDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_DiffServInterfaceDirection_Type.__name__ = "Integer32"
_DiffServInterfaceDirection_Object = MibTableColumn
diffServInterfaceDirection = _DiffServInterfaceDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 3, 1, 1),
    _DiffServInterfaceDirection_Type()
)
diffServInterfaceDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServInterfaceDirection.setStatus("current")


class _DiffServClassifierNumber_Type(Integer32):
    """Custom type diffServClassifierNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DiffServClassifierNumber_Type.__name__ = "Integer32"
_DiffServClassifierNumber_Object = MibTableColumn
diffServClassifierNumber = _DiffServClassifierNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 3, 1, 2),
    _DiffServClassifierNumber_Type()
)
diffServClassifierNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassifierNumber.setStatus("current")


class _DiffServClassifierMatchObject_Type(RowPointer):
    """Custom type diffServClassifierMatchObject based on RowPointer"""
    defaultValue = (0, 0)


_DiffServClassifierMatchObject_Type.__name__ = "RowPointer"
_DiffServClassifierMatchObject_Object = MibTableColumn
diffServClassifierMatchObject = _DiffServClassifierMatchObject_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 3, 1, 3),
    _DiffServClassifierMatchObject_Type()
)
diffServClassifierMatchObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassifierMatchObject.setStatus("current")
_DiffServClassifierNext_Type = RowPointer
_DiffServClassifierNext_Object = MibTableColumn
diffServClassifierNext = _DiffServClassifierNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 3, 1, 4),
    _DiffServClassifierNext_Type()
)
diffServClassifierNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassifierNext.setStatus("current")


class _DiffServClassifierSequence_Type(Unsigned32):
    """Custom type diffServClassifierSequence based on Unsigned32"""
    defaultValue = 0


_DiffServClassifierSequence_Type.__name__ = "Unsigned32"
_DiffServClassifierSequence_Object = MibTableColumn
diffServClassifierSequence = _DiffServClassifierSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 3, 1, 5),
    _DiffServClassifierSequence_Type()
)
diffServClassifierSequence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassifierSequence.setStatus("current")


class _DiffServClassifierConfigType_Type(Integer32):
    """Custom type diffServClassifierConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("mib", 1),
          ("pib", 2),
          ("bgp", 3))
    )


_DiffServClassifierConfigType_Type.__name__ = "Integer32"
_DiffServClassifierConfigType_Object = MibTableColumn
diffServClassifierConfigType = _DiffServClassifierConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 3, 1, 6),
    _DiffServClassifierConfigType_Type()
)
diffServClassifierConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassifierConfigType.setStatus("current")
_DiffServClassifierConfigTypeInfo_Type = OctetString
_DiffServClassifierConfigTypeInfo_Object = MibTableColumn
diffServClassifierConfigTypeInfo = _DiffServClassifierConfigTypeInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 3, 1, 7),
    _DiffServClassifierConfigTypeInfo_Type()
)
diffServClassifierConfigTypeInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassifierConfigTypeInfo.setStatus("current")
_DiffServClassifierStatus_Type = RowStatus
_DiffServClassifierStatus_Object = MibTableColumn
diffServClassifierStatus = _DiffServClassifierStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 3, 1, 8),
    _DiffServClassifierStatus_Type()
)
diffServClassifierStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassifierStatus.setStatus("current")
_DiffServTBMeterTable_Object = MibTable
diffServTBMeterTable = _DiffServTBMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 4)
)
if mibBuilder.loadTexts:
    diffServTBMeterTable.setStatus("current")
_DiffServTBMeterEntry_Object = MibTableRow
diffServTBMeterEntry = _DiffServTBMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 4, 1)
)
diffServTBMeterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DIFF-SERV-MIB", "diffServInterfaceDirection"),
    (0, "DIFF-SERV-MIB", "diffServTBMeterNumber"),
)
if mibBuilder.loadTexts:
    diffServTBMeterEntry.setStatus("current")


class _DiffServTBMeterNumber_Type(Integer32):
    """Custom type diffServTBMeterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DiffServTBMeterNumber_Type.__name__ = "Integer32"
_DiffServTBMeterNumber_Object = MibTableColumn
diffServTBMeterNumber = _DiffServTBMeterNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 4, 1, 1),
    _DiffServTBMeterNumber_Type()
)
diffServTBMeterNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServTBMeterNumber.setStatus("current")
_DiffServTBMeterInterval_Type = Unsigned32
_DiffServTBMeterInterval_Object = MibTableColumn
diffServTBMeterInterval = _DiffServTBMeterInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 4, 1, 2),
    _DiffServTBMeterInterval_Type()
)
diffServTBMeterInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServTBMeterInterval.setStatus("current")
if mibBuilder.loadTexts:
    diffServTBMeterInterval.setUnits("microseconds")
_DiffServTBMeterBurstSize_Type = Unsigned32
_DiffServTBMeterBurstSize_Object = MibTableColumn
diffServTBMeterBurstSize = _DiffServTBMeterBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 4, 1, 3),
    _DiffServTBMeterBurstSize_Type()
)
diffServTBMeterBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServTBMeterBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    diffServTBMeterBurstSize.setUnits("bytes")
_DiffServTBMeterFailNext_Type = RowPointer
_DiffServTBMeterFailNext_Object = MibTableColumn
diffServTBMeterFailNext = _DiffServTBMeterFailNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 4, 1, 4),
    _DiffServTBMeterFailNext_Type()
)
diffServTBMeterFailNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServTBMeterFailNext.setStatus("current")


class _DiffServTBMeterSucceedNext_Type(RowPointer):
    """Custom type diffServTBMeterSucceedNext based on RowPointer"""
    defaultValue = (0, 0)


_DiffServTBMeterSucceedNext_Type.__name__ = "RowPointer"
_DiffServTBMeterSucceedNext_Object = MibTableColumn
diffServTBMeterSucceedNext = _DiffServTBMeterSucceedNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 4, 1, 5),
    _DiffServTBMeterSucceedNext_Type()
)
diffServTBMeterSucceedNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServTBMeterSucceedNext.setStatus("current")
_DiffServTBMeterStatus_Type = RowStatus
_DiffServTBMeterStatus_Object = MibTableColumn
diffServTBMeterStatus = _DiffServTBMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 4, 1, 6),
    _DiffServTBMeterStatus_Type()
)
diffServTBMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServTBMeterStatus.setStatus("current")
_DiffServActionTable_Object = MibTable
diffServActionTable = _DiffServActionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5)
)
if mibBuilder.loadTexts:
    diffServActionTable.setStatus("current")
_DiffServActionEntry_Object = MibTableRow
diffServActionEntry = _DiffServActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1)
)
diffServActionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DIFF-SERV-MIB", "diffServInterfaceDirection"),
    (0, "DIFF-SERV-MIB", "diffServActionNumber"),
)
if mibBuilder.loadTexts:
    diffServActionEntry.setStatus("current")


class _DiffServActionNumber_Type(Integer32):
    """Custom type diffServActionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DiffServActionNumber_Type.__name__ = "Integer32"
_DiffServActionNumber_Object = MibTableColumn
diffServActionNumber = _DiffServActionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 1),
    _DiffServActionNumber_Type()
)
diffServActionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServActionNumber.setStatus("current")


class _DiffServActionNext_Type(RowPointer):
    """Custom type diffServActionNext based on RowPointer"""
    defaultValue = (0, 0)


_DiffServActionNext_Type.__name__ = "RowPointer"
_DiffServActionNext_Object = MibTableColumn
diffServActionNext = _DiffServActionNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 2),
    _DiffServActionNext_Type()
)
diffServActionNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionNext.setStatus("current")
_DiffServActionDSCP_Type = Dscp
_DiffServActionDSCP_Object = MibTableColumn
diffServActionDSCP = _DiffServActionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 3),
    _DiffServActionDSCP_Type()
)
diffServActionDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionDSCP.setStatus("current")
_DiffServActionMinThreshold_Type = Unsigned32
_DiffServActionMinThreshold_Object = MibTableColumn
diffServActionMinThreshold = _DiffServActionMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 4),
    _DiffServActionMinThreshold_Type()
)
diffServActionMinThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionMinThreshold.setStatus("current")
if mibBuilder.loadTexts:
    diffServActionMinThreshold.setUnits("packets")
_DiffServActionMaxThreshold_Type = Unsigned32
_DiffServActionMaxThreshold_Object = MibTableColumn
diffServActionMaxThreshold = _DiffServActionMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 5),
    _DiffServActionMaxThreshold_Type()
)
diffServActionMaxThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    diffServActionMaxThreshold.setUnits("packets")


class _DiffServActionDropPolicy_Type(Integer32):
    """Custom type diffServActionDropPolicy based on Integer32"""
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
        *(("other", 1),
          ("alwaysDrop", 2),
          ("tailDrop", 3),
          ("randomDrop", 4))
    )


_DiffServActionDropPolicy_Type.__name__ = "Integer32"
_DiffServActionDropPolicy_Object = MibTableColumn
diffServActionDropPolicy = _DiffServActionDropPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 6),
    _DiffServActionDropPolicy_Type()
)
diffServActionDropPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionDropPolicy.setStatus("current")
_DiffServActionHCConformingPackets_Type = Counter64
_DiffServActionHCConformingPackets_Object = MibTableColumn
diffServActionHCConformingPackets = _DiffServActionHCConformingPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 7),
    _DiffServActionHCConformingPackets_Type()
)
diffServActionHCConformingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServActionHCConformingPackets.setStatus("current")
if mibBuilder.loadTexts:
    diffServActionHCConformingPackets.setUnits("bytes")
_DiffServActionConformingPackets_Type = Counter32
_DiffServActionConformingPackets_Object = MibTableColumn
diffServActionConformingPackets = _DiffServActionConformingPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 8),
    _DiffServActionConformingPackets_Type()
)
diffServActionConformingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServActionConformingPackets.setStatus("current")
if mibBuilder.loadTexts:
    diffServActionConformingPackets.setUnits("bytes")
_DiffServActionHCConformingOctets_Type = Counter64
_DiffServActionHCConformingOctets_Object = MibTableColumn
diffServActionHCConformingOctets = _DiffServActionHCConformingOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 9),
    _DiffServActionHCConformingOctets_Type()
)
diffServActionHCConformingOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServActionHCConformingOctets.setStatus("current")
if mibBuilder.loadTexts:
    diffServActionHCConformingOctets.setUnits("bytes")
_DiffServActionConformingOctets_Type = Counter32
_DiffServActionConformingOctets_Object = MibTableColumn
diffServActionConformingOctets = _DiffServActionConformingOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 10),
    _DiffServActionConformingOctets_Type()
)
diffServActionConformingOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServActionConformingOctets.setStatus("current")
if mibBuilder.loadTexts:
    diffServActionConformingOctets.setUnits("bytes")
_DiffServActionTailDrops_Type = Counter32
_DiffServActionTailDrops_Object = MibTableColumn
diffServActionTailDrops = _DiffServActionTailDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 11),
    _DiffServActionTailDrops_Type()
)
diffServActionTailDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServActionTailDrops.setStatus("current")
_DiffServActionHCTailDrops_Type = Counter64
_DiffServActionHCTailDrops_Object = MibTableColumn
diffServActionHCTailDrops = _DiffServActionHCTailDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 12),
    _DiffServActionHCTailDrops_Type()
)
diffServActionHCTailDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServActionHCTailDrops.setStatus("current")
_DiffServActionRandomDrops_Type = Counter32
_DiffServActionRandomDrops_Object = MibTableColumn
diffServActionRandomDrops = _DiffServActionRandomDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 13),
    _DiffServActionRandomDrops_Type()
)
diffServActionRandomDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServActionRandomDrops.setStatus("current")
_DiffServActionHCRandomDrops_Type = Counter64
_DiffServActionHCRandomDrops_Object = MibTableColumn
diffServActionHCRandomDrops = _DiffServActionHCRandomDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 14),
    _DiffServActionHCRandomDrops_Type()
)
diffServActionHCRandomDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServActionHCRandomDrops.setStatus("current")
_DiffServActionStatus_Type = RowStatus
_DiffServActionStatus_Object = MibTableColumn
diffServActionStatus = _DiffServActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 5, 1, 15),
    _DiffServActionStatus_Type()
)
diffServActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionStatus.setStatus("current")
_DiffServQueueTable_Object = MibTable
diffServQueueTable = _DiffServQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 6)
)
if mibBuilder.loadTexts:
    diffServQueueTable.setStatus("current")
_DiffServQueueEntry_Object = MibTableRow
diffServQueueEntry = _DiffServQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 6, 1)
)
diffServQueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DIFF-SERV-MIB", "diffServInterfaceDirection"),
    (0, "DIFF-SERV-MIB", "diffServQueueNumber"),
)
if mibBuilder.loadTexts:
    diffServQueueEntry.setStatus("current")


class _DiffServQueueNumber_Type(Integer32):
    """Custom type diffServQueueNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DiffServQueueNumber_Type.__name__ = "Integer32"
_DiffServQueueNumber_Object = MibTableColumn
diffServQueueNumber = _DiffServQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 6, 1, 1),
    _DiffServQueueNumber_Type()
)
diffServQueueNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServQueueNumber.setStatus("current")
_DiffServQueueMinimumRate_Type = Unsigned32
_DiffServQueueMinimumRate_Object = MibTableColumn
diffServQueueMinimumRate = _DiffServQueueMinimumRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 6, 1, 2),
    _DiffServQueueMinimumRate_Type()
)
diffServQueueMinimumRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQueueMinimumRate.setStatus("current")
if mibBuilder.loadTexts:
    diffServQueueMinimumRate.setUnits("KBPS")
_DiffServQueueMaximumRate_Type = Unsigned32
_DiffServQueueMaximumRate_Object = MibTableColumn
diffServQueueMaximumRate = _DiffServQueueMaximumRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 6, 1, 3),
    _DiffServQueueMaximumRate_Type()
)
diffServQueueMaximumRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQueueMaximumRate.setStatus("current")
if mibBuilder.loadTexts:
    diffServQueueMaximumRate.setUnits("KBPS")
_DiffServQueuePriority_Type = Unsigned32
_DiffServQueuePriority_Object = MibTableColumn
diffServQueuePriority = _DiffServQueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 6, 1, 4),
    _DiffServQueuePriority_Type()
)
diffServQueuePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQueuePriority.setStatus("current")


class _DiffServQueueNextTCB_Type(RowPointer):
    """Custom type diffServQueueNextTCB based on RowPointer"""
    defaultValue = (0, 0)


_DiffServQueueNextTCB_Type.__name__ = "RowPointer"
_DiffServQueueNextTCB_Object = MibTableColumn
diffServQueueNextTCB = _DiffServQueueNextTCB_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 6, 1, 5),
    _DiffServQueueNextTCB_Type()
)
diffServQueueNextTCB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQueueNextTCB.setStatus("current")
_DiffServQueueOccupancyWeight_Type = Unsigned32
_DiffServQueueOccupancyWeight_Object = MibTableColumn
diffServQueueOccupancyWeight = _DiffServQueueOccupancyWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 6, 1, 6),
    _DiffServQueueOccupancyWeight_Type()
)
diffServQueueOccupancyWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQueueOccupancyWeight.setStatus("current")
_DiffServQueueStatus_Type = RowStatus
_DiffServQueueStatus_Object = MibTableColumn
diffServQueueStatus = _DiffServQueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 2, 6, 1, 7),
    _DiffServQueueStatus_Type()
)
diffServQueueStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServQueueStatus.setStatus("current")
_DiffServMIBConformance_ObjectIdentity = ObjectIdentity
diffServMIBConformance = _DiffServMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIFF-SERV-MIB",
    **{"Dscp": Dscp,
       "MFClassifierL4Port": MFClassifierL4Port,
       "diffServMib": diffServMib,
       "diffServObjects": diffServObjects,
       "diffServMFClassifierUnique": diffServMFClassifierUnique,
       "diffServClassifierUnique": diffServClassifierUnique,
       "diffServTBMeterUnique": diffServTBMeterUnique,
       "diffServActionUnique": diffServActionUnique,
       "diffServQueueUnique": diffServQueueUnique,
       "diffServTables": diffServTables,
       "diffServAggregateTable": diffServAggregateTable,
       "diffServAggregateEntry": diffServAggregateEntry,
       "diffServAggregateDSCP": diffServAggregateDSCP,
       "diffServMFClassifierTable": diffServMFClassifierTable,
       "diffServMFClassifierEntry": diffServMFClassifierEntry,
       "diffServMFClassifierIndex": diffServMFClassifierIndex,
       "diffServMFClassifierAddrType": diffServMFClassifierAddrType,
       "diffServMFClassifierDstAddr": diffServMFClassifierDstAddr,
       "diffServMFClassifierDstAddrMask": diffServMFClassifierDstAddrMask,
       "diffServMFClassifierSrcAddr": diffServMFClassifierSrcAddr,
       "diffServMFClassifierSrcAddrMask": diffServMFClassifierSrcAddrMask,
       "diffServMFClassifierDscp": diffServMFClassifierDscp,
       "diffServMFClassifierProtocol": diffServMFClassifierProtocol,
       "diffServMFClassifierDstL4PortMin": diffServMFClassifierDstL4PortMin,
       "diffServMFClassifierDstL4PortMax": diffServMFClassifierDstL4PortMax,
       "diffServMFClassifierSrcL4PortMin": diffServMFClassifierSrcL4PortMin,
       "diffServMFClassifierSrcL4PortMax": diffServMFClassifierSrcL4PortMax,
       "diffServMFClassifierStatus": diffServMFClassifierStatus,
       "diffServClassifierTable": diffServClassifierTable,
       "diffServClassifierEntry": diffServClassifierEntry,
       "diffServInterfaceDirection": diffServInterfaceDirection,
       "diffServClassifierNumber": diffServClassifierNumber,
       "diffServClassifierMatchObject": diffServClassifierMatchObject,
       "diffServClassifierNext": diffServClassifierNext,
       "diffServClassifierSequence": diffServClassifierSequence,
       "diffServClassifierConfigType": diffServClassifierConfigType,
       "diffServClassifierConfigTypeInfo": diffServClassifierConfigTypeInfo,
       "diffServClassifierStatus": diffServClassifierStatus,
       "diffServTBMeterTable": diffServTBMeterTable,
       "diffServTBMeterEntry": diffServTBMeterEntry,
       "diffServTBMeterNumber": diffServTBMeterNumber,
       "diffServTBMeterInterval": diffServTBMeterInterval,
       "diffServTBMeterBurstSize": diffServTBMeterBurstSize,
       "diffServTBMeterFailNext": diffServTBMeterFailNext,
       "diffServTBMeterSucceedNext": diffServTBMeterSucceedNext,
       "diffServTBMeterStatus": diffServTBMeterStatus,
       "diffServActionTable": diffServActionTable,
       "diffServActionEntry": diffServActionEntry,
       "diffServActionNumber": diffServActionNumber,
       "diffServActionNext": diffServActionNext,
       "diffServActionDSCP": diffServActionDSCP,
       "diffServActionMinThreshold": diffServActionMinThreshold,
       "diffServActionMaxThreshold": diffServActionMaxThreshold,
       "diffServActionDropPolicy": diffServActionDropPolicy,
       "diffServActionHCConformingPackets": diffServActionHCConformingPackets,
       "diffServActionConformingPackets": diffServActionConformingPackets,
       "diffServActionHCConformingOctets": diffServActionHCConformingOctets,
       "diffServActionConformingOctets": diffServActionConformingOctets,
       "diffServActionTailDrops": diffServActionTailDrops,
       "diffServActionHCTailDrops": diffServActionHCTailDrops,
       "diffServActionRandomDrops": diffServActionRandomDrops,
       "diffServActionHCRandomDrops": diffServActionHCRandomDrops,
       "diffServActionStatus": diffServActionStatus,
       "diffServQueueTable": diffServQueueTable,
       "diffServQueueEntry": diffServQueueEntry,
       "diffServQueueNumber": diffServQueueNumber,
       "diffServQueueMinimumRate": diffServQueueMinimumRate,
       "diffServQueueMaximumRate": diffServQueueMaximumRate,
       "diffServQueuePriority": diffServQueuePriority,
       "diffServQueueNextTCB": diffServQueueNextTCB,
       "diffServQueueOccupancyWeight": diffServQueueOccupancyWeight,
       "diffServQueueStatus": diffServQueueStatus,
       "diffServMIBConformance": diffServMIBConformance}
)
