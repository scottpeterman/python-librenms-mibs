# SNMP MIB module (ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ATM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:02:25 2025
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

(AtmAddr,
 AtmConnCastType,
 AtmConnKind,
 AtmServiceCategory,
 AtmTrafficDescrParamIndex,
 AtmVcIdentifier,
 AtmVorXAdminStatus,
 AtmVorXLastChange,
 AtmVorXOperStatus,
 AtmVpIdentifier,
 atmNoClpNoScr) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr",
    "AtmConnCastType",
    "AtmConnKind",
    "AtmServiceCategory",
    "AtmTrafficDescrParamIndex",
    "AtmVcIdentifier",
    "AtmVorXAdminStatus",
    "AtmVorXLastChange",
    "AtmVorXOperStatus",
    "AtmVpIdentifier",
    "atmNoClpNoScr")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

atmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 37)
)
if mibBuilder.loadTexts:
    atmMIB.setRevisions(
        ("1998-10-19 12:00",
         "1994-06-07 22:45")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmMIBObjects_ObjectIdentity = ObjectIdentity
atmMIBObjects = _AtmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1)
)
_AtmInterfaceConfTable_Object = MibTable
atmInterfaceConfTable = _AtmInterfaceConfTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2)
)
if mibBuilder.loadTexts:
    atmInterfaceConfTable.setStatus("current")
_AtmInterfaceConfEntry_Object = MibTableRow
atmInterfaceConfEntry = _AtmInterfaceConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1)
)
atmInterfaceConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmInterfaceConfEntry.setStatus("current")


class _AtmInterfaceMaxVpcs_Type(Integer32):
    """Custom type atmInterfaceMaxVpcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AtmInterfaceMaxVpcs_Type.__name__ = "Integer32"
_AtmInterfaceMaxVpcs_Object = MibTableColumn
atmInterfaceMaxVpcs = _AtmInterfaceMaxVpcs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 1),
    _AtmInterfaceMaxVpcs_Type()
)
atmInterfaceMaxVpcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceMaxVpcs.setStatus("current")


class _AtmInterfaceMaxVccs_Type(Integer32):
    """Custom type atmInterfaceMaxVccs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AtmInterfaceMaxVccs_Type.__name__ = "Integer32"
_AtmInterfaceMaxVccs_Object = MibTableColumn
atmInterfaceMaxVccs = _AtmInterfaceMaxVccs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 2),
    _AtmInterfaceMaxVccs_Type()
)
atmInterfaceMaxVccs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceMaxVccs.setStatus("current")


class _AtmInterfaceConfVpcs_Type(Integer32):
    """Custom type atmInterfaceConfVpcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AtmInterfaceConfVpcs_Type.__name__ = "Integer32"
_AtmInterfaceConfVpcs_Object = MibTableColumn
atmInterfaceConfVpcs = _AtmInterfaceConfVpcs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 3),
    _AtmInterfaceConfVpcs_Type()
)
atmInterfaceConfVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceConfVpcs.setStatus("current")


class _AtmInterfaceConfVccs_Type(Integer32):
    """Custom type atmInterfaceConfVccs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AtmInterfaceConfVccs_Type.__name__ = "Integer32"
_AtmInterfaceConfVccs_Object = MibTableColumn
atmInterfaceConfVccs = _AtmInterfaceConfVccs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 4),
    _AtmInterfaceConfVccs_Type()
)
atmInterfaceConfVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceConfVccs.setStatus("current")


class _AtmInterfaceMaxActiveVpiBits_Type(Integer32):
    """Custom type atmInterfaceMaxActiveVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AtmInterfaceMaxActiveVpiBits_Type.__name__ = "Integer32"
_AtmInterfaceMaxActiveVpiBits_Object = MibTableColumn
atmInterfaceMaxActiveVpiBits = _AtmInterfaceMaxActiveVpiBits_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 5),
    _AtmInterfaceMaxActiveVpiBits_Type()
)
atmInterfaceMaxActiveVpiBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceMaxActiveVpiBits.setStatus("current")


class _AtmInterfaceMaxActiveVciBits_Type(Integer32):
    """Custom type atmInterfaceMaxActiveVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AtmInterfaceMaxActiveVciBits_Type.__name__ = "Integer32"
_AtmInterfaceMaxActiveVciBits_Object = MibTableColumn
atmInterfaceMaxActiveVciBits = _AtmInterfaceMaxActiveVciBits_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 6),
    _AtmInterfaceMaxActiveVciBits_Type()
)
atmInterfaceMaxActiveVciBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceMaxActiveVciBits.setStatus("current")


class _AtmInterfaceIlmiVpi_Type(AtmVpIdentifier):
    """Custom type atmInterfaceIlmiVpi based on AtmVpIdentifier"""
    defaultValue = 0


_AtmInterfaceIlmiVpi_Type.__name__ = "AtmVpIdentifier"
_AtmInterfaceIlmiVpi_Object = MibTableColumn
atmInterfaceIlmiVpi = _AtmInterfaceIlmiVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 7),
    _AtmInterfaceIlmiVpi_Type()
)
atmInterfaceIlmiVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceIlmiVpi.setStatus("current")


class _AtmInterfaceIlmiVci_Type(AtmVcIdentifier):
    """Custom type atmInterfaceIlmiVci based on AtmVcIdentifier"""
    defaultValue = 16


_AtmInterfaceIlmiVci_Type.__name__ = "AtmVcIdentifier"
_AtmInterfaceIlmiVci_Object = MibTableColumn
atmInterfaceIlmiVci = _AtmInterfaceIlmiVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 8),
    _AtmInterfaceIlmiVci_Type()
)
atmInterfaceIlmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceIlmiVci.setStatus("current")


class _AtmInterfaceAddressType_Type(Integer32):
    """Custom type atmInterfaceAddressType based on Integer32"""
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
        *(("private", 1),
          ("nsapE164", 2),
          ("nativeE164", 3),
          ("other", 4))
    )


_AtmInterfaceAddressType_Type.__name__ = "Integer32"
_AtmInterfaceAddressType_Object = MibTableColumn
atmInterfaceAddressType = _AtmInterfaceAddressType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 9),
    _AtmInterfaceAddressType_Type()
)
atmInterfaceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceAddressType.setStatus("deprecated")
_AtmInterfaceAdminAddress_Type = AtmAddr
_AtmInterfaceAdminAddress_Object = MibTableColumn
atmInterfaceAdminAddress = _AtmInterfaceAdminAddress_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 10),
    _AtmInterfaceAdminAddress_Type()
)
atmInterfaceAdminAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceAdminAddress.setStatus("deprecated")
_AtmInterfaceMyNeighborIpAddress_Type = IpAddress
_AtmInterfaceMyNeighborIpAddress_Object = MibTableColumn
atmInterfaceMyNeighborIpAddress = _AtmInterfaceMyNeighborIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 11),
    _AtmInterfaceMyNeighborIpAddress_Type()
)
atmInterfaceMyNeighborIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceMyNeighborIpAddress.setStatus("current")
_AtmInterfaceMyNeighborIfName_Type = DisplayString
_AtmInterfaceMyNeighborIfName_Object = MibTableColumn
atmInterfaceMyNeighborIfName = _AtmInterfaceMyNeighborIfName_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 12),
    _AtmInterfaceMyNeighborIfName_Type()
)
atmInterfaceMyNeighborIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceMyNeighborIfName.setStatus("current")


class _AtmInterfaceCurrentMaxVpiBits_Type(Integer32):
    """Custom type atmInterfaceCurrentMaxVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AtmInterfaceCurrentMaxVpiBits_Type.__name__ = "Integer32"
_AtmInterfaceCurrentMaxVpiBits_Object = MibTableColumn
atmInterfaceCurrentMaxVpiBits = _AtmInterfaceCurrentMaxVpiBits_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 13),
    _AtmInterfaceCurrentMaxVpiBits_Type()
)
atmInterfaceCurrentMaxVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceCurrentMaxVpiBits.setStatus("current")


class _AtmInterfaceCurrentMaxVciBits_Type(Integer32):
    """Custom type atmInterfaceCurrentMaxVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AtmInterfaceCurrentMaxVciBits_Type.__name__ = "Integer32"
_AtmInterfaceCurrentMaxVciBits_Object = MibTableColumn
atmInterfaceCurrentMaxVciBits = _AtmInterfaceCurrentMaxVciBits_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 14),
    _AtmInterfaceCurrentMaxVciBits_Type()
)
atmInterfaceCurrentMaxVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceCurrentMaxVciBits.setStatus("current")
_AtmInterfaceSubscrAddress_Type = AtmAddr
_AtmInterfaceSubscrAddress_Object = MibTableColumn
atmInterfaceSubscrAddress = _AtmInterfaceSubscrAddress_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 2, 1, 15),
    _AtmInterfaceSubscrAddress_Type()
)
atmInterfaceSubscrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceSubscrAddress.setStatus("current")
_AtmInterfaceDs3PlcpTable_Object = MibTable
atmInterfaceDs3PlcpTable = _AtmInterfaceDs3PlcpTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 3)
)
if mibBuilder.loadTexts:
    atmInterfaceDs3PlcpTable.setStatus("current")
_AtmInterfaceDs3PlcpEntry_Object = MibTableRow
atmInterfaceDs3PlcpEntry = _AtmInterfaceDs3PlcpEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 3, 1)
)
atmInterfaceDs3PlcpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmInterfaceDs3PlcpEntry.setStatus("current")
_AtmInterfaceDs3PlcpSEFSs_Type = Counter32
_AtmInterfaceDs3PlcpSEFSs_Object = MibTableColumn
atmInterfaceDs3PlcpSEFSs = _AtmInterfaceDs3PlcpSEFSs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 3, 1, 1),
    _AtmInterfaceDs3PlcpSEFSs_Type()
)
atmInterfaceDs3PlcpSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceDs3PlcpSEFSs.setStatus("current")


class _AtmInterfaceDs3PlcpAlarmState_Type(Integer32):
    """Custom type atmInterfaceDs3PlcpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("receivedFarEndAlarm", 2),
          ("incomingLOF", 3))
    )


_AtmInterfaceDs3PlcpAlarmState_Type.__name__ = "Integer32"
_AtmInterfaceDs3PlcpAlarmState_Object = MibTableColumn
atmInterfaceDs3PlcpAlarmState = _AtmInterfaceDs3PlcpAlarmState_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 3, 1, 2),
    _AtmInterfaceDs3PlcpAlarmState_Type()
)
atmInterfaceDs3PlcpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceDs3PlcpAlarmState.setStatus("current")
_AtmInterfaceDs3PlcpUASs_Type = Counter32
_AtmInterfaceDs3PlcpUASs_Object = MibTableColumn
atmInterfaceDs3PlcpUASs = _AtmInterfaceDs3PlcpUASs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 3, 1, 3),
    _AtmInterfaceDs3PlcpUASs_Type()
)
atmInterfaceDs3PlcpUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceDs3PlcpUASs.setStatus("current")
_AtmInterfaceTCTable_Object = MibTable
atmInterfaceTCTable = _AtmInterfaceTCTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 4)
)
if mibBuilder.loadTexts:
    atmInterfaceTCTable.setStatus("current")
_AtmInterfaceTCEntry_Object = MibTableRow
atmInterfaceTCEntry = _AtmInterfaceTCEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 4, 1)
)
atmInterfaceTCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmInterfaceTCEntry.setStatus("current")
_AtmInterfaceOCDEvents_Type = Counter32
_AtmInterfaceOCDEvents_Object = MibTableColumn
atmInterfaceOCDEvents = _AtmInterfaceOCDEvents_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 4, 1, 1),
    _AtmInterfaceOCDEvents_Type()
)
atmInterfaceOCDEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceOCDEvents.setStatus("current")


class _AtmInterfaceTCAlarmState_Type(Integer32):
    """Custom type atmInterfaceTCAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 1),
          ("lcdFailure", 2))
    )


_AtmInterfaceTCAlarmState_Type.__name__ = "Integer32"
_AtmInterfaceTCAlarmState_Object = MibTableColumn
atmInterfaceTCAlarmState = _AtmInterfaceTCAlarmState_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 4, 1, 2),
    _AtmInterfaceTCAlarmState_Type()
)
atmInterfaceTCAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceTCAlarmState.setStatus("current")
_AtmTrafficDescrParamTable_Object = MibTable
atmTrafficDescrParamTable = _AtmTrafficDescrParamTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5)
)
if mibBuilder.loadTexts:
    atmTrafficDescrParamTable.setStatus("current")
_AtmTrafficDescrParamEntry_Object = MibTableRow
atmTrafficDescrParamEntry = _AtmTrafficDescrParamEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1)
)
atmTrafficDescrParamEntry.setIndexNames(
    (0, "ATM-MIB", "atmTrafficDescrParamIndex"),
)
if mibBuilder.loadTexts:
    atmTrafficDescrParamEntry.setStatus("current")


class _AtmTrafficDescrParamIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type atmTrafficDescrParamIndex based on AtmTrafficDescrParamIndex"""
    subtypeSpec = AtmTrafficDescrParamIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmTrafficDescrParamIndex_Type.__name__ = "AtmTrafficDescrParamIndex"
_AtmTrafficDescrParamIndex_Object = MibTableColumn
atmTrafficDescrParamIndex = _AtmTrafficDescrParamIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 1),
    _AtmTrafficDescrParamIndex_Type()
)
atmTrafficDescrParamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmTrafficDescrParamIndex.setStatus("current")


class _AtmTrafficDescrType_Type(ObjectIdentifier):
    """Custom type atmTrafficDescrType based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 2, 1, 37, 1, 1, 2)


_AtmTrafficDescrType_Type.__name__ = "ObjectIdentifier"
_AtmTrafficDescrType_Object = MibTableColumn
atmTrafficDescrType = _AtmTrafficDescrType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 2),
    _AtmTrafficDescrType_Type()
)
atmTrafficDescrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescrType.setStatus("current")


class _AtmTrafficDescrParam1_Type(Integer32):
    """Custom type atmTrafficDescrParam1 based on Integer32"""
    defaultValue = 0


_AtmTrafficDescrParam1_Type.__name__ = "Integer32"
_AtmTrafficDescrParam1_Object = MibTableColumn
atmTrafficDescrParam1 = _AtmTrafficDescrParam1_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 3),
    _AtmTrafficDescrParam1_Type()
)
atmTrafficDescrParam1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescrParam1.setStatus("current")


class _AtmTrafficDescrParam2_Type(Integer32):
    """Custom type atmTrafficDescrParam2 based on Integer32"""
    defaultValue = 0


_AtmTrafficDescrParam2_Type.__name__ = "Integer32"
_AtmTrafficDescrParam2_Object = MibTableColumn
atmTrafficDescrParam2 = _AtmTrafficDescrParam2_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 4),
    _AtmTrafficDescrParam2_Type()
)
atmTrafficDescrParam2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescrParam2.setStatus("current")


class _AtmTrafficDescrParam3_Type(Integer32):
    """Custom type atmTrafficDescrParam3 based on Integer32"""
    defaultValue = 0


_AtmTrafficDescrParam3_Type.__name__ = "Integer32"
_AtmTrafficDescrParam3_Object = MibTableColumn
atmTrafficDescrParam3 = _AtmTrafficDescrParam3_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 5),
    _AtmTrafficDescrParam3_Type()
)
atmTrafficDescrParam3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescrParam3.setStatus("current")


class _AtmTrafficDescrParam4_Type(Integer32):
    """Custom type atmTrafficDescrParam4 based on Integer32"""
    defaultValue = 0


_AtmTrafficDescrParam4_Type.__name__ = "Integer32"
_AtmTrafficDescrParam4_Object = MibTableColumn
atmTrafficDescrParam4 = _AtmTrafficDescrParam4_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 6),
    _AtmTrafficDescrParam4_Type()
)
atmTrafficDescrParam4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescrParam4.setStatus("current")


class _AtmTrafficDescrParam5_Type(Integer32):
    """Custom type atmTrafficDescrParam5 based on Integer32"""
    defaultValue = 0


_AtmTrafficDescrParam5_Type.__name__ = "Integer32"
_AtmTrafficDescrParam5_Object = MibTableColumn
atmTrafficDescrParam5 = _AtmTrafficDescrParam5_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 7),
    _AtmTrafficDescrParam5_Type()
)
atmTrafficDescrParam5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescrParam5.setStatus("current")


class _AtmTrafficQoSClass_Type(Integer32):
    """Custom type atmTrafficQoSClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmTrafficQoSClass_Type.__name__ = "Integer32"
_AtmTrafficQoSClass_Object = MibTableColumn
atmTrafficQoSClass = _AtmTrafficQoSClass_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 8),
    _AtmTrafficQoSClass_Type()
)
atmTrafficQoSClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficQoSClass.setStatus("deprecated")


class _AtmTrafficDescrRowStatus_Type(RowStatus):
    """Custom type atmTrafficDescrRowStatus based on RowStatus"""
    defaultValue = 1


_AtmTrafficDescrRowStatus_Type.__name__ = "RowStatus"
_AtmTrafficDescrRowStatus_Object = MibTableColumn
atmTrafficDescrRowStatus = _AtmTrafficDescrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 9),
    _AtmTrafficDescrRowStatus_Type()
)
atmTrafficDescrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficDescrRowStatus.setStatus("current")


class _AtmServiceCategory_Type(AtmServiceCategory):
    """Custom type atmServiceCategory based on AtmServiceCategory"""
    defaultValue = 6


_AtmServiceCategory_Type.__name__ = "AtmServiceCategory"
_AtmServiceCategory_Object = MibTableColumn
atmServiceCategory = _AtmServiceCategory_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 10),
    _AtmServiceCategory_Type()
)
atmServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmServiceCategory.setStatus("current")


class _AtmTrafficFrameDiscard_Type(TruthValue):
    """Custom type atmTrafficFrameDiscard based on TruthValue"""
    defaultValue = 1


_AtmTrafficFrameDiscard_Type.__name__ = "TruthValue"
_AtmTrafficFrameDiscard_Object = MibTableColumn
atmTrafficFrameDiscard = _AtmTrafficFrameDiscard_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 5, 1, 11),
    _AtmTrafficFrameDiscard_Type()
)
atmTrafficFrameDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmTrafficFrameDiscard.setStatus("current")
_AtmVplTable_Object = MibTable
atmVplTable = _AtmVplTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6)
)
if mibBuilder.loadTexts:
    atmVplTable.setStatus("current")
_AtmVplEntry_Object = MibTableRow
atmVplEntry = _AtmVplEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1)
)
atmVplEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    atmVplEntry.setStatus("current")
_AtmVplVpi_Type = AtmVpIdentifier
_AtmVplVpi_Object = MibTableColumn
atmVplVpi = _AtmVplVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 1),
    _AtmVplVpi_Type()
)
atmVplVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVplVpi.setStatus("current")


class _AtmVplAdminStatus_Type(AtmVorXAdminStatus):
    """Custom type atmVplAdminStatus based on AtmVorXAdminStatus"""
    defaultValue = 2


_AtmVplAdminStatus_Type.__name__ = "AtmVorXAdminStatus"
_AtmVplAdminStatus_Object = MibTableColumn
atmVplAdminStatus = _AtmVplAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 2),
    _AtmVplAdminStatus_Type()
)
atmVplAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVplAdminStatus.setStatus("current")
_AtmVplOperStatus_Type = AtmVorXOperStatus
_AtmVplOperStatus_Object = MibTableColumn
atmVplOperStatus = _AtmVplOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 3),
    _AtmVplOperStatus_Type()
)
atmVplOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplOperStatus.setStatus("current")
_AtmVplLastChange_Type = AtmVorXLastChange
_AtmVplLastChange_Object = MibTableColumn
atmVplLastChange = _AtmVplLastChange_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 4),
    _AtmVplLastChange_Type()
)
atmVplLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplLastChange.setStatus("current")


class _AtmVplReceiveTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type atmVplReceiveTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 0


_AtmVplReceiveTrafficDescrIndex_Type.__name__ = "AtmTrafficDescrParamIndex"
_AtmVplReceiveTrafficDescrIndex_Object = MibTableColumn
atmVplReceiveTrafficDescrIndex = _AtmVplReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 5),
    _AtmVplReceiveTrafficDescrIndex_Type()
)
atmVplReceiveTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVplReceiveTrafficDescrIndex.setStatus("current")


class _AtmVplTransmitTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type atmVplTransmitTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 0


_AtmVplTransmitTrafficDescrIndex_Type.__name__ = "AtmTrafficDescrParamIndex"
_AtmVplTransmitTrafficDescrIndex_Object = MibTableColumn
atmVplTransmitTrafficDescrIndex = _AtmVplTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 6),
    _AtmVplTransmitTrafficDescrIndex_Type()
)
atmVplTransmitTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVplTransmitTrafficDescrIndex.setStatus("current")


class _AtmVplCrossConnectIdentifier_Type(Integer32):
    """Custom type atmVplCrossConnectIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmVplCrossConnectIdentifier_Type.__name__ = "Integer32"
_AtmVplCrossConnectIdentifier_Object = MibTableColumn
atmVplCrossConnectIdentifier = _AtmVplCrossConnectIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 7),
    _AtmVplCrossConnectIdentifier_Type()
)
atmVplCrossConnectIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplCrossConnectIdentifier.setStatus("current")


class _AtmVplRowStatus_Type(RowStatus):
    """Custom type atmVplRowStatus based on RowStatus"""
    defaultValue = 5


_AtmVplRowStatus_Type.__name__ = "RowStatus"
_AtmVplRowStatus_Object = MibTableColumn
atmVplRowStatus = _AtmVplRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 8),
    _AtmVplRowStatus_Type()
)
atmVplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVplRowStatus.setStatus("current")


class _AtmVplCastType_Type(AtmConnCastType):
    """Custom type atmVplCastType based on AtmConnCastType"""
    defaultValue = 1


_AtmVplCastType_Type.__name__ = "AtmConnCastType"
_AtmVplCastType_Object = MibTableColumn
atmVplCastType = _AtmVplCastType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 9),
    _AtmVplCastType_Type()
)
atmVplCastType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVplCastType.setStatus("current")


class _AtmVplConnKind_Type(AtmConnKind):
    """Custom type atmVplConnKind based on AtmConnKind"""
    defaultValue = 1


_AtmVplConnKind_Type.__name__ = "AtmConnKind"
_AtmVplConnKind_Object = MibTableColumn
atmVplConnKind = _AtmVplConnKind_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 6, 1, 10),
    _AtmVplConnKind_Type()
)
atmVplConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVplConnKind.setStatus("current")
_AtmVclTable_Object = MibTable
atmVclTable = _AtmVclTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7)
)
if mibBuilder.loadTexts:
    atmVclTable.setStatus("current")
_AtmVclEntry_Object = MibTableRow
atmVclEntry = _AtmVclEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1)
)
atmVclEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    atmVclEntry.setStatus("current")
_AtmVclVpi_Type = AtmVpIdentifier
_AtmVclVpi_Object = MibTableColumn
atmVclVpi = _AtmVclVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 1),
    _AtmVclVpi_Type()
)
atmVclVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVclVpi.setStatus("current")
_AtmVclVci_Type = AtmVcIdentifier
_AtmVclVci_Object = MibTableColumn
atmVclVci = _AtmVclVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 2),
    _AtmVclVci_Type()
)
atmVclVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVclVci.setStatus("current")


class _AtmVclAdminStatus_Type(AtmVorXAdminStatus):
    """Custom type atmVclAdminStatus based on AtmVorXAdminStatus"""
    defaultValue = 2


_AtmVclAdminStatus_Type.__name__ = "AtmVorXAdminStatus"
_AtmVclAdminStatus_Object = MibTableColumn
atmVclAdminStatus = _AtmVclAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 3),
    _AtmVclAdminStatus_Type()
)
atmVclAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclAdminStatus.setStatus("current")
_AtmVclOperStatus_Type = AtmVorXOperStatus
_AtmVclOperStatus_Object = MibTableColumn
atmVclOperStatus = _AtmVclOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 4),
    _AtmVclOperStatus_Type()
)
atmVclOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclOperStatus.setStatus("current")
_AtmVclLastChange_Type = AtmVorXLastChange
_AtmVclLastChange_Object = MibTableColumn
atmVclLastChange = _AtmVclLastChange_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 5),
    _AtmVclLastChange_Type()
)
atmVclLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclLastChange.setStatus("current")


class _AtmVclReceiveTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type atmVclReceiveTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 0


_AtmVclReceiveTrafficDescrIndex_Type.__name__ = "AtmTrafficDescrParamIndex"
_AtmVclReceiveTrafficDescrIndex_Object = MibTableColumn
atmVclReceiveTrafficDescrIndex = _AtmVclReceiveTrafficDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 6),
    _AtmVclReceiveTrafficDescrIndex_Type()
)
atmVclReceiveTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclReceiveTrafficDescrIndex.setStatus("current")


class _AtmVclTransmitTrafficDescrIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type atmVclTransmitTrafficDescrIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 0


_AtmVclTransmitTrafficDescrIndex_Type.__name__ = "AtmTrafficDescrParamIndex"
_AtmVclTransmitTrafficDescrIndex_Object = MibTableColumn
atmVclTransmitTrafficDescrIndex = _AtmVclTransmitTrafficDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 7),
    _AtmVclTransmitTrafficDescrIndex_Type()
)
atmVclTransmitTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclTransmitTrafficDescrIndex.setStatus("current")


class _AtmVccAalType_Type(Integer32):
    """Custom type atmVccAalType based on Integer32"""
    defaultValue = 3

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
        *(("aal1", 1),
          ("aal34", 2),
          ("aal5", 3),
          ("other", 4),
          ("unknown", 5),
          ("aal2", 6))
    )


_AtmVccAalType_Type.__name__ = "Integer32"
_AtmVccAalType_Object = MibTableColumn
atmVccAalType = _AtmVccAalType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 8),
    _AtmVccAalType_Type()
)
atmVccAalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVccAalType.setStatus("current")


class _AtmVccAal5CpcsTransmitSduSize_Type(Integer32):
    """Custom type atmVccAal5CpcsTransmitSduSize based on Integer32"""
    defaultValue = 9188

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmVccAal5CpcsTransmitSduSize_Type.__name__ = "Integer32"
_AtmVccAal5CpcsTransmitSduSize_Object = MibTableColumn
atmVccAal5CpcsTransmitSduSize = _AtmVccAal5CpcsTransmitSduSize_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 9),
    _AtmVccAal5CpcsTransmitSduSize_Type()
)
atmVccAal5CpcsTransmitSduSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVccAal5CpcsTransmitSduSize.setStatus("current")


class _AtmVccAal5CpcsReceiveSduSize_Type(Integer32):
    """Custom type atmVccAal5CpcsReceiveSduSize based on Integer32"""
    defaultValue = 9188

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmVccAal5CpcsReceiveSduSize_Type.__name__ = "Integer32"
_AtmVccAal5CpcsReceiveSduSize_Object = MibTableColumn
atmVccAal5CpcsReceiveSduSize = _AtmVccAal5CpcsReceiveSduSize_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 10),
    _AtmVccAal5CpcsReceiveSduSize_Type()
)
atmVccAal5CpcsReceiveSduSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVccAal5CpcsReceiveSduSize.setStatus("current")


class _AtmVccAal5EncapsType_Type(Integer32):
    """Custom type atmVccAal5EncapsType based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("vcMultiplexRoutedProtocol", 1),
          ("vcMultiplexBridgedProtocol8023", 2),
          ("vcMultiplexBridgedProtocol8025", 3),
          ("vcMultiplexBridgedProtocol8026", 4),
          ("vcMultiplexLANemulation8023", 5),
          ("vcMultiplexLANemulation8025", 6),
          ("llcEncapsulation", 7),
          ("multiprotocolFrameRelaySscs", 8),
          ("other", 9),
          ("unknown", 10))
    )


_AtmVccAal5EncapsType_Type.__name__ = "Integer32"
_AtmVccAal5EncapsType_Object = MibTableColumn
atmVccAal5EncapsType = _AtmVccAal5EncapsType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 11),
    _AtmVccAal5EncapsType_Type()
)
atmVccAal5EncapsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVccAal5EncapsType.setStatus("current")


class _AtmVclCrossConnectIdentifier_Type(Integer32):
    """Custom type atmVclCrossConnectIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmVclCrossConnectIdentifier_Type.__name__ = "Integer32"
_AtmVclCrossConnectIdentifier_Object = MibTableColumn
atmVclCrossConnectIdentifier = _AtmVclCrossConnectIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 12),
    _AtmVclCrossConnectIdentifier_Type()
)
atmVclCrossConnectIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclCrossConnectIdentifier.setStatus("current")


class _AtmVclRowStatus_Type(RowStatus):
    """Custom type atmVclRowStatus based on RowStatus"""
    defaultValue = 5


_AtmVclRowStatus_Type.__name__ = "RowStatus"
_AtmVclRowStatus_Object = MibTableColumn
atmVclRowStatus = _AtmVclRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 13),
    _AtmVclRowStatus_Type()
)
atmVclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclRowStatus.setStatus("current")


class _AtmVclCastType_Type(AtmConnCastType):
    """Custom type atmVclCastType based on AtmConnCastType"""
    defaultValue = 1


_AtmVclCastType_Type.__name__ = "AtmConnCastType"
_AtmVclCastType_Object = MibTableColumn
atmVclCastType = _AtmVclCastType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 14),
    _AtmVclCastType_Type()
)
atmVclCastType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclCastType.setStatus("current")


class _AtmVclConnKind_Type(AtmConnKind):
    """Custom type atmVclConnKind based on AtmConnKind"""
    defaultValue = 1


_AtmVclConnKind_Type.__name__ = "AtmConnKind"
_AtmVclConnKind_Object = MibTableColumn
atmVclConnKind = _AtmVclConnKind_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 7, 1, 15),
    _AtmVclConnKind_Type()
)
atmVclConnKind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclConnKind.setStatus("current")


class _AtmVpCrossConnectIndexNext_Type(Integer32):
    """Custom type atmVpCrossConnectIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmVpCrossConnectIndexNext_Type.__name__ = "Integer32"
_AtmVpCrossConnectIndexNext_Object = MibScalar
atmVpCrossConnectIndexNext = _AtmVpCrossConnectIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 8),
    _AtmVpCrossConnectIndexNext_Type()
)
atmVpCrossConnectIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCrossConnectIndexNext.setStatus("current")
_AtmVpCrossConnectTable_Object = MibTable
atmVpCrossConnectTable = _AtmVpCrossConnectTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9)
)
if mibBuilder.loadTexts:
    atmVpCrossConnectTable.setStatus("current")
_AtmVpCrossConnectEntry_Object = MibTableRow
atmVpCrossConnectEntry = _AtmVpCrossConnectEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1)
)
atmVpCrossConnectEntry.setIndexNames(
    (0, "ATM-MIB", "atmVpCrossConnectIndex"),
    (0, "ATM-MIB", "atmVpCrossConnectLowIfIndex"),
    (0, "ATM-MIB", "atmVpCrossConnectLowVpi"),
    (0, "ATM-MIB", "atmVpCrossConnectHighIfIndex"),
    (0, "ATM-MIB", "atmVpCrossConnectHighVpi"),
)
if mibBuilder.loadTexts:
    atmVpCrossConnectEntry.setStatus("current")


class _AtmVpCrossConnectIndex_Type(Integer32):
    """Custom type atmVpCrossConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmVpCrossConnectIndex_Type.__name__ = "Integer32"
_AtmVpCrossConnectIndex_Object = MibTableColumn
atmVpCrossConnectIndex = _AtmVpCrossConnectIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 1),
    _AtmVpCrossConnectIndex_Type()
)
atmVpCrossConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVpCrossConnectIndex.setStatus("current")
_AtmVpCrossConnectLowIfIndex_Type = InterfaceIndex
_AtmVpCrossConnectLowIfIndex_Object = MibTableColumn
atmVpCrossConnectLowIfIndex = _AtmVpCrossConnectLowIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 2),
    _AtmVpCrossConnectLowIfIndex_Type()
)
atmVpCrossConnectLowIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVpCrossConnectLowIfIndex.setStatus("current")
_AtmVpCrossConnectLowVpi_Type = AtmVpIdentifier
_AtmVpCrossConnectLowVpi_Object = MibTableColumn
atmVpCrossConnectLowVpi = _AtmVpCrossConnectLowVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 3),
    _AtmVpCrossConnectLowVpi_Type()
)
atmVpCrossConnectLowVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVpCrossConnectLowVpi.setStatus("current")
_AtmVpCrossConnectHighIfIndex_Type = InterfaceIndex
_AtmVpCrossConnectHighIfIndex_Object = MibTableColumn
atmVpCrossConnectHighIfIndex = _AtmVpCrossConnectHighIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 4),
    _AtmVpCrossConnectHighIfIndex_Type()
)
atmVpCrossConnectHighIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVpCrossConnectHighIfIndex.setStatus("current")
_AtmVpCrossConnectHighVpi_Type = AtmVpIdentifier
_AtmVpCrossConnectHighVpi_Object = MibTableColumn
atmVpCrossConnectHighVpi = _AtmVpCrossConnectHighVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 5),
    _AtmVpCrossConnectHighVpi_Type()
)
atmVpCrossConnectHighVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVpCrossConnectHighVpi.setStatus("current")


class _AtmVpCrossConnectAdminStatus_Type(AtmVorXAdminStatus):
    """Custom type atmVpCrossConnectAdminStatus based on AtmVorXAdminStatus"""
    defaultValue = 2


_AtmVpCrossConnectAdminStatus_Type.__name__ = "AtmVorXAdminStatus"
_AtmVpCrossConnectAdminStatus_Object = MibTableColumn
atmVpCrossConnectAdminStatus = _AtmVpCrossConnectAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 6),
    _AtmVpCrossConnectAdminStatus_Type()
)
atmVpCrossConnectAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVpCrossConnectAdminStatus.setStatus("current")
_AtmVpCrossConnectL2HOperStatus_Type = AtmVorXOperStatus
_AtmVpCrossConnectL2HOperStatus_Object = MibTableColumn
atmVpCrossConnectL2HOperStatus = _AtmVpCrossConnectL2HOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 7),
    _AtmVpCrossConnectL2HOperStatus_Type()
)
atmVpCrossConnectL2HOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCrossConnectL2HOperStatus.setStatus("current")
_AtmVpCrossConnectH2LOperStatus_Type = AtmVorXOperStatus
_AtmVpCrossConnectH2LOperStatus_Object = MibTableColumn
atmVpCrossConnectH2LOperStatus = _AtmVpCrossConnectH2LOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 8),
    _AtmVpCrossConnectH2LOperStatus_Type()
)
atmVpCrossConnectH2LOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCrossConnectH2LOperStatus.setStatus("current")
_AtmVpCrossConnectL2HLastChange_Type = AtmVorXLastChange
_AtmVpCrossConnectL2HLastChange_Object = MibTableColumn
atmVpCrossConnectL2HLastChange = _AtmVpCrossConnectL2HLastChange_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 9),
    _AtmVpCrossConnectL2HLastChange_Type()
)
atmVpCrossConnectL2HLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCrossConnectL2HLastChange.setStatus("current")
_AtmVpCrossConnectH2LLastChange_Type = AtmVorXLastChange
_AtmVpCrossConnectH2LLastChange_Object = MibTableColumn
atmVpCrossConnectH2LLastChange = _AtmVpCrossConnectH2LLastChange_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 10),
    _AtmVpCrossConnectH2LLastChange_Type()
)
atmVpCrossConnectH2LLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCrossConnectH2LLastChange.setStatus("current")


class _AtmVpCrossConnectRowStatus_Type(RowStatus):
    """Custom type atmVpCrossConnectRowStatus based on RowStatus"""
    defaultValue = 5


_AtmVpCrossConnectRowStatus_Type.__name__ = "RowStatus"
_AtmVpCrossConnectRowStatus_Object = MibTableColumn
atmVpCrossConnectRowStatus = _AtmVpCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 9, 1, 11),
    _AtmVpCrossConnectRowStatus_Type()
)
atmVpCrossConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVpCrossConnectRowStatus.setStatus("current")


class _AtmVcCrossConnectIndexNext_Type(Integer32):
    """Custom type atmVcCrossConnectIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmVcCrossConnectIndexNext_Type.__name__ = "Integer32"
_AtmVcCrossConnectIndexNext_Object = MibScalar
atmVcCrossConnectIndexNext = _AtmVcCrossConnectIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 10),
    _AtmVcCrossConnectIndexNext_Type()
)
atmVcCrossConnectIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCrossConnectIndexNext.setStatus("current")
_AtmVcCrossConnectTable_Object = MibTable
atmVcCrossConnectTable = _AtmVcCrossConnectTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11)
)
if mibBuilder.loadTexts:
    atmVcCrossConnectTable.setStatus("current")
_AtmVcCrossConnectEntry_Object = MibTableRow
atmVcCrossConnectEntry = _AtmVcCrossConnectEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1)
)
atmVcCrossConnectEntry.setIndexNames(
    (0, "ATM-MIB", "atmVcCrossConnectIndex"),
    (0, "ATM-MIB", "atmVcCrossConnectLowIfIndex"),
    (0, "ATM-MIB", "atmVcCrossConnectLowVpi"),
    (0, "ATM-MIB", "atmVcCrossConnectLowVci"),
    (0, "ATM-MIB", "atmVcCrossConnectHighIfIndex"),
    (0, "ATM-MIB", "atmVcCrossConnectHighVpi"),
    (0, "ATM-MIB", "atmVcCrossConnectHighVci"),
)
if mibBuilder.loadTexts:
    atmVcCrossConnectEntry.setStatus("current")


class _AtmVcCrossConnectIndex_Type(Integer32):
    """Custom type atmVcCrossConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmVcCrossConnectIndex_Type.__name__ = "Integer32"
_AtmVcCrossConnectIndex_Object = MibTableColumn
atmVcCrossConnectIndex = _AtmVcCrossConnectIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 1),
    _AtmVcCrossConnectIndex_Type()
)
atmVcCrossConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcCrossConnectIndex.setStatus("current")
_AtmVcCrossConnectLowIfIndex_Type = InterfaceIndex
_AtmVcCrossConnectLowIfIndex_Object = MibTableColumn
atmVcCrossConnectLowIfIndex = _AtmVcCrossConnectLowIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 2),
    _AtmVcCrossConnectLowIfIndex_Type()
)
atmVcCrossConnectLowIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcCrossConnectLowIfIndex.setStatus("current")
_AtmVcCrossConnectLowVpi_Type = AtmVpIdentifier
_AtmVcCrossConnectLowVpi_Object = MibTableColumn
atmVcCrossConnectLowVpi = _AtmVcCrossConnectLowVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 3),
    _AtmVcCrossConnectLowVpi_Type()
)
atmVcCrossConnectLowVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcCrossConnectLowVpi.setStatus("current")
_AtmVcCrossConnectLowVci_Type = AtmVcIdentifier
_AtmVcCrossConnectLowVci_Object = MibTableColumn
atmVcCrossConnectLowVci = _AtmVcCrossConnectLowVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 4),
    _AtmVcCrossConnectLowVci_Type()
)
atmVcCrossConnectLowVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcCrossConnectLowVci.setStatus("current")
_AtmVcCrossConnectHighIfIndex_Type = InterfaceIndex
_AtmVcCrossConnectHighIfIndex_Object = MibTableColumn
atmVcCrossConnectHighIfIndex = _AtmVcCrossConnectHighIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 5),
    _AtmVcCrossConnectHighIfIndex_Type()
)
atmVcCrossConnectHighIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcCrossConnectHighIfIndex.setStatus("current")
_AtmVcCrossConnectHighVpi_Type = AtmVpIdentifier
_AtmVcCrossConnectHighVpi_Object = MibTableColumn
atmVcCrossConnectHighVpi = _AtmVcCrossConnectHighVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 6),
    _AtmVcCrossConnectHighVpi_Type()
)
atmVcCrossConnectHighVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcCrossConnectHighVpi.setStatus("current")
_AtmVcCrossConnectHighVci_Type = AtmVcIdentifier
_AtmVcCrossConnectHighVci_Object = MibTableColumn
atmVcCrossConnectHighVci = _AtmVcCrossConnectHighVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 7),
    _AtmVcCrossConnectHighVci_Type()
)
atmVcCrossConnectHighVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcCrossConnectHighVci.setStatus("current")


class _AtmVcCrossConnectAdminStatus_Type(AtmVorXAdminStatus):
    """Custom type atmVcCrossConnectAdminStatus based on AtmVorXAdminStatus"""
    defaultValue = 2


_AtmVcCrossConnectAdminStatus_Type.__name__ = "AtmVorXAdminStatus"
_AtmVcCrossConnectAdminStatus_Object = MibTableColumn
atmVcCrossConnectAdminStatus = _AtmVcCrossConnectAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 8),
    _AtmVcCrossConnectAdminStatus_Type()
)
atmVcCrossConnectAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVcCrossConnectAdminStatus.setStatus("current")
_AtmVcCrossConnectL2HOperStatus_Type = AtmVorXOperStatus
_AtmVcCrossConnectL2HOperStatus_Object = MibTableColumn
atmVcCrossConnectL2HOperStatus = _AtmVcCrossConnectL2HOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 9),
    _AtmVcCrossConnectL2HOperStatus_Type()
)
atmVcCrossConnectL2HOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCrossConnectL2HOperStatus.setStatus("current")
_AtmVcCrossConnectH2LOperStatus_Type = AtmVorXOperStatus
_AtmVcCrossConnectH2LOperStatus_Object = MibTableColumn
atmVcCrossConnectH2LOperStatus = _AtmVcCrossConnectH2LOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 10),
    _AtmVcCrossConnectH2LOperStatus_Type()
)
atmVcCrossConnectH2LOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCrossConnectH2LOperStatus.setStatus("current")
_AtmVcCrossConnectL2HLastChange_Type = AtmVorXLastChange
_AtmVcCrossConnectL2HLastChange_Object = MibTableColumn
atmVcCrossConnectL2HLastChange = _AtmVcCrossConnectL2HLastChange_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 11),
    _AtmVcCrossConnectL2HLastChange_Type()
)
atmVcCrossConnectL2HLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCrossConnectL2HLastChange.setStatus("current")
_AtmVcCrossConnectH2LLastChange_Type = AtmVorXLastChange
_AtmVcCrossConnectH2LLastChange_Object = MibTableColumn
atmVcCrossConnectH2LLastChange = _AtmVcCrossConnectH2LLastChange_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 12),
    _AtmVcCrossConnectH2LLastChange_Type()
)
atmVcCrossConnectH2LLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCrossConnectH2LLastChange.setStatus("current")


class _AtmVcCrossConnectRowStatus_Type(RowStatus):
    """Custom type atmVcCrossConnectRowStatus based on RowStatus"""
    defaultValue = 5


_AtmVcCrossConnectRowStatus_Type.__name__ = "RowStatus"
_AtmVcCrossConnectRowStatus_Object = MibTableColumn
atmVcCrossConnectRowStatus = _AtmVcCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 11, 1, 13),
    _AtmVcCrossConnectRowStatus_Type()
)
atmVcCrossConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVcCrossConnectRowStatus.setStatus("current")
_Aal5VccTable_Object = MibTable
aal5VccTable = _Aal5VccTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 12)
)
if mibBuilder.loadTexts:
    aal5VccTable.setStatus("current")
_Aal5VccEntry_Object = MibTableRow
aal5VccEntry = _Aal5VccEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 12, 1)
)
aal5VccEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "aal5VccVpi"),
    (0, "ATM-MIB", "aal5VccVci"),
)
if mibBuilder.loadTexts:
    aal5VccEntry.setStatus("current")
_Aal5VccVpi_Type = AtmVpIdentifier
_Aal5VccVpi_Object = MibTableColumn
aal5VccVpi = _Aal5VccVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 1),
    _Aal5VccVpi_Type()
)
aal5VccVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aal5VccVpi.setStatus("current")
_Aal5VccVci_Type = AtmVcIdentifier
_Aal5VccVci_Object = MibTableColumn
aal5VccVci = _Aal5VccVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 2),
    _Aal5VccVci_Type()
)
aal5VccVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aal5VccVci.setStatus("current")
_Aal5VccCrcErrors_Type = Counter32
_Aal5VccCrcErrors_Object = MibTableColumn
aal5VccCrcErrors = _Aal5VccCrcErrors_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 3),
    _Aal5VccCrcErrors_Type()
)
aal5VccCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccCrcErrors.setStatus("current")
_Aal5VccSarTimeOuts_Type = Counter32
_Aal5VccSarTimeOuts_Object = MibTableColumn
aal5VccSarTimeOuts = _Aal5VccSarTimeOuts_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 4),
    _Aal5VccSarTimeOuts_Type()
)
aal5VccSarTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccSarTimeOuts.setStatus("current")
_Aal5VccOverSizedSDUs_Type = Counter32
_Aal5VccOverSizedSDUs_Object = MibTableColumn
aal5VccOverSizedSDUs = _Aal5VccOverSizedSDUs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 12, 1, 5),
    _Aal5VccOverSizedSDUs_Type()
)
aal5VccOverSizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccOverSizedSDUs.setStatus("current")


class _AtmTrafficDescrParamIndexNext_Type(Integer32):
    """Custom type atmTrafficDescrParamIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmTrafficDescrParamIndexNext_Type.__name__ = "Integer32"
_AtmTrafficDescrParamIndexNext_Object = MibScalar
atmTrafficDescrParamIndexNext = _AtmTrafficDescrParamIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 13),
    _AtmTrafficDescrParamIndexNext_Type()
)
atmTrafficDescrParamIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTrafficDescrParamIndexNext.setStatus("current")
_AtmMIBConformance_ObjectIdentity = ObjectIdentity
atmMIBConformance = _AtmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 2)
)
_AtmMIBGroups_ObjectIdentity = ObjectIdentity
atmMIBGroups = _AtmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 2, 1)
)
_AtmMIBCompliances_ObjectIdentity = ObjectIdentity
atmMIBCompliances = _AtmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 2, 2)
)

# Managed Objects groups

atmInterfaceConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 1)
)
atmInterfaceConfGroup.setObjects(
      *(("ATM-MIB", "atmInterfaceMaxVpcs"),
        ("ATM-MIB", "atmInterfaceMaxVccs"),
        ("ATM-MIB", "atmInterfaceConfVpcs"),
        ("ATM-MIB", "atmInterfaceConfVccs"),
        ("ATM-MIB", "atmInterfaceMaxActiveVpiBits"),
        ("ATM-MIB", "atmInterfaceMaxActiveVciBits"),
        ("ATM-MIB", "atmInterfaceIlmiVpi"),
        ("ATM-MIB", "atmInterfaceIlmiVci"),
        ("ATM-MIB", "atmInterfaceAddressType"),
        ("ATM-MIB", "atmInterfaceAdminAddress"),
        ("ATM-MIB", "atmInterfaceMyNeighborIpAddress"),
        ("ATM-MIB", "atmInterfaceMyNeighborIfName"))
)
if mibBuilder.loadTexts:
    atmInterfaceConfGroup.setStatus("deprecated")

atmTrafficDescrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 2)
)
atmTrafficDescrGroup.setObjects(
      *(("ATM-MIB", "atmTrafficDescrType"),
        ("ATM-MIB", "atmTrafficDescrParam1"),
        ("ATM-MIB", "atmTrafficDescrParam2"),
        ("ATM-MIB", "atmTrafficDescrParam3"),
        ("ATM-MIB", "atmTrafficDescrParam4"),
        ("ATM-MIB", "atmTrafficDescrParam5"),
        ("ATM-MIB", "atmTrafficQoSClass"),
        ("ATM-MIB", "atmTrafficDescrRowStatus"))
)
if mibBuilder.loadTexts:
    atmTrafficDescrGroup.setStatus("deprecated")

atmInterfaceDs3PlcpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 3)
)
atmInterfaceDs3PlcpGroup.setObjects(
      *(("ATM-MIB", "atmInterfaceDs3PlcpSEFSs"),
        ("ATM-MIB", "atmInterfaceDs3PlcpAlarmState"),
        ("ATM-MIB", "atmInterfaceDs3PlcpUASs"))
)
if mibBuilder.loadTexts:
    atmInterfaceDs3PlcpGroup.setStatus("current")

atmInterfaceTCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 4)
)
atmInterfaceTCGroup.setObjects(
      *(("ATM-MIB", "atmInterfaceOCDEvents"),
        ("ATM-MIB", "atmInterfaceTCAlarmState"))
)
if mibBuilder.loadTexts:
    atmInterfaceTCGroup.setStatus("current")

atmVpcTerminationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 5)
)
atmVpcTerminationGroup.setObjects(
      *(("ATM-MIB", "atmVplOperStatus"),
        ("ATM-MIB", "atmVplAdminStatus"),
        ("ATM-MIB", "atmVplLastChange"),
        ("ATM-MIB", "atmVplReceiveTrafficDescrIndex"),
        ("ATM-MIB", "atmVplTransmitTrafficDescrIndex"),
        ("ATM-MIB", "atmVplRowStatus"))
)
if mibBuilder.loadTexts:
    atmVpcTerminationGroup.setStatus("deprecated")

atmVccTerminationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 6)
)
atmVccTerminationGroup.setObjects(
      *(("ATM-MIB", "atmVclOperStatus"),
        ("ATM-MIB", "atmVclAdminStatus"),
        ("ATM-MIB", "atmVclLastChange"),
        ("ATM-MIB", "atmVclReceiveTrafficDescrIndex"),
        ("ATM-MIB", "atmVclTransmitTrafficDescrIndex"),
        ("ATM-MIB", "atmVccAalType"),
        ("ATM-MIB", "atmVclRowStatus"))
)
if mibBuilder.loadTexts:
    atmVccTerminationGroup.setStatus("deprecated")

atmVpCrossConnectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 7)
)
atmVpCrossConnectGroup.setObjects(
      *(("ATM-MIB", "atmVplReceiveTrafficDescrIndex"),
        ("ATM-MIB", "atmVplTransmitTrafficDescrIndex"),
        ("ATM-MIB", "atmVplOperStatus"),
        ("ATM-MIB", "atmVplRowStatus"),
        ("ATM-MIB", "atmVpCrossConnectAdminStatus"),
        ("ATM-MIB", "atmVpCrossConnectL2HOperStatus"),
        ("ATM-MIB", "atmVpCrossConnectH2LOperStatus"),
        ("ATM-MIB", "atmVpCrossConnectL2HLastChange"),
        ("ATM-MIB", "atmVpCrossConnectH2LLastChange"),
        ("ATM-MIB", "atmVpCrossConnectRowStatus"),
        ("ATM-MIB", "atmVplCrossConnectIdentifier"),
        ("ATM-MIB", "atmVpCrossConnectIndexNext"))
)
if mibBuilder.loadTexts:
    atmVpCrossConnectGroup.setStatus("deprecated")

atmVcCrossConnectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 8)
)
atmVcCrossConnectGroup.setObjects(
      *(("ATM-MIB", "atmVclReceiveTrafficDescrIndex"),
        ("ATM-MIB", "atmVclTransmitTrafficDescrIndex"),
        ("ATM-MIB", "atmVclOperStatus"),
        ("ATM-MIB", "atmVclRowStatus"),
        ("ATM-MIB", "atmVcCrossConnectAdminStatus"),
        ("ATM-MIB", "atmVcCrossConnectL2HOperStatus"),
        ("ATM-MIB", "atmVcCrossConnectH2LOperStatus"),
        ("ATM-MIB", "atmVcCrossConnectL2HLastChange"),
        ("ATM-MIB", "atmVcCrossConnectH2LLastChange"),
        ("ATM-MIB", "atmVcCrossConnectRowStatus"),
        ("ATM-MIB", "atmVclCrossConnectIdentifier"),
        ("ATM-MIB", "atmVcCrossConnectIndexNext"))
)
if mibBuilder.loadTexts:
    atmVcCrossConnectGroup.setStatus("deprecated")

aal5VccGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 9)
)
aal5VccGroup.setObjects(
      *(("ATM-MIB", "atmVccAal5CpcsTransmitSduSize"),
        ("ATM-MIB", "atmVccAal5CpcsReceiveSduSize"),
        ("ATM-MIB", "atmVccAal5EncapsType"),
        ("ATM-MIB", "aal5VccCrcErrors"),
        ("ATM-MIB", "aal5VccSarTimeOuts"),
        ("ATM-MIB", "aal5VccOverSizedSDUs"))
)
if mibBuilder.loadTexts:
    aal5VccGroup.setStatus("current")

atmInterfaceConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 10)
)
atmInterfaceConfGroup2.setObjects(
      *(("ATM-MIB", "atmInterfaceMaxVpcs"),
        ("ATM-MIB", "atmInterfaceMaxVccs"),
        ("ATM-MIB", "atmInterfaceConfVpcs"),
        ("ATM-MIB", "atmInterfaceConfVccs"),
        ("ATM-MIB", "atmInterfaceMaxActiveVpiBits"),
        ("ATM-MIB", "atmInterfaceMaxActiveVciBits"),
        ("ATM-MIB", "atmInterfaceIlmiVpi"),
        ("ATM-MIB", "atmInterfaceIlmiVci"),
        ("ATM-MIB", "atmInterfaceMyNeighborIpAddress"),
        ("ATM-MIB", "atmInterfaceMyNeighborIfName"),
        ("ATM-MIB", "atmInterfaceCurrentMaxVpiBits"),
        ("ATM-MIB", "atmInterfaceCurrentMaxVciBits"),
        ("ATM-MIB", "atmInterfaceSubscrAddress"))
)
if mibBuilder.loadTexts:
    atmInterfaceConfGroup2.setStatus("current")

atmTrafficDescrGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 11)
)
atmTrafficDescrGroup2.setObjects(
      *(("ATM-MIB", "atmTrafficDescrType"),
        ("ATM-MIB", "atmTrafficDescrParam1"),
        ("ATM-MIB", "atmTrafficDescrParam2"),
        ("ATM-MIB", "atmTrafficDescrParam3"),
        ("ATM-MIB", "atmTrafficDescrParam4"),
        ("ATM-MIB", "atmTrafficDescrParam5"),
        ("ATM-MIB", "atmTrafficDescrRowStatus"),
        ("ATM-MIB", "atmServiceCategory"),
        ("ATM-MIB", "atmTrafficFrameDiscard"),
        ("ATM-MIB", "atmTrafficDescrParamIndexNext"))
)
if mibBuilder.loadTexts:
    atmTrafficDescrGroup2.setStatus("current")

atmVpcTerminationGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 12)
)
atmVpcTerminationGroup2.setObjects(
      *(("ATM-MIB", "atmVplOperStatus"),
        ("ATM-MIB", "atmVplAdminStatus"),
        ("ATM-MIB", "atmVplLastChange"),
        ("ATM-MIB", "atmVplReceiveTrafficDescrIndex"),
        ("ATM-MIB", "atmVplTransmitTrafficDescrIndex"),
        ("ATM-MIB", "atmVplRowStatus"),
        ("ATM-MIB", "atmVplCastType"),
        ("ATM-MIB", "atmVplConnKind"))
)
if mibBuilder.loadTexts:
    atmVpcTerminationGroup2.setStatus("current")

atmVccTerminationGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 13)
)
atmVccTerminationGroup2.setObjects(
      *(("ATM-MIB", "atmVclOperStatus"),
        ("ATM-MIB", "atmVclAdminStatus"),
        ("ATM-MIB", "atmVclLastChange"),
        ("ATM-MIB", "atmVclReceiveTrafficDescrIndex"),
        ("ATM-MIB", "atmVclTransmitTrafficDescrIndex"),
        ("ATM-MIB", "atmVccAalType"),
        ("ATM-MIB", "atmVclRowStatus"),
        ("ATM-MIB", "atmVclCastType"),
        ("ATM-MIB", "atmVclConnKind"))
)
if mibBuilder.loadTexts:
    atmVccTerminationGroup2.setStatus("current")

atmVplCrossConnectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 14)
)
atmVplCrossConnectGroup.setObjects(
      *(("ATM-MIB", "atmVplReceiveTrafficDescrIndex"),
        ("ATM-MIB", "atmVplTransmitTrafficDescrIndex"),
        ("ATM-MIB", "atmVplOperStatus"),
        ("ATM-MIB", "atmVplLastChange"),
        ("ATM-MIB", "atmVplRowStatus"),
        ("ATM-MIB", "atmVplCastType"),
        ("ATM-MIB", "atmVplConnKind"))
)
if mibBuilder.loadTexts:
    atmVplCrossConnectGroup.setStatus("current")

atmVpPvcCrossConnectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 15)
)
atmVpPvcCrossConnectGroup.setObjects(
      *(("ATM-MIB", "atmVpCrossConnectAdminStatus"),
        ("ATM-MIB", "atmVpCrossConnectL2HOperStatus"),
        ("ATM-MIB", "atmVpCrossConnectH2LOperStatus"),
        ("ATM-MIB", "atmVpCrossConnectL2HLastChange"),
        ("ATM-MIB", "atmVpCrossConnectH2LLastChange"),
        ("ATM-MIB", "atmVpCrossConnectRowStatus"),
        ("ATM-MIB", "atmVplCrossConnectIdentifier"),
        ("ATM-MIB", "atmVpCrossConnectIndexNext"))
)
if mibBuilder.loadTexts:
    atmVpPvcCrossConnectGroup.setStatus("current")

atmVclCrossConnectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 16)
)
atmVclCrossConnectGroup.setObjects(
      *(("ATM-MIB", "atmVclReceiveTrafficDescrIndex"),
        ("ATM-MIB", "atmVclTransmitTrafficDescrIndex"),
        ("ATM-MIB", "atmVclOperStatus"),
        ("ATM-MIB", "atmVclLastChange"),
        ("ATM-MIB", "atmVclRowStatus"),
        ("ATM-MIB", "atmVclCastType"),
        ("ATM-MIB", "atmVclConnKind"))
)
if mibBuilder.loadTexts:
    atmVclCrossConnectGroup.setStatus("current")

atmVcPvcCrossConnectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 2, 1, 17)
)
atmVcPvcCrossConnectGroup.setObjects(
      *(("ATM-MIB", "atmVcCrossConnectAdminStatus"),
        ("ATM-MIB", "atmVcCrossConnectL2HOperStatus"),
        ("ATM-MIB", "atmVcCrossConnectH2LOperStatus"),
        ("ATM-MIB", "atmVcCrossConnectL2HLastChange"),
        ("ATM-MIB", "atmVcCrossConnectH2LLastChange"),
        ("ATM-MIB", "atmVcCrossConnectRowStatus"),
        ("ATM-MIB", "atmVclCrossConnectIdentifier"),
        ("ATM-MIB", "atmVcCrossConnectIndexNext"))
)
if mibBuilder.loadTexts:
    atmVcPvcCrossConnectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

atmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 37, 2, 2, 1)
)
atmMIBCompliance.setObjects(
      *(("ATM-MIB", "atmInterfaceConfGroup"),
        ("ATM-MIB", "atmTrafficDescrGroup"))
)
if mibBuilder.loadTexts:
    atmMIBCompliance.setStatus(
        "deprecated"
    )

atmMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 37, 2, 2, 2)
)
atmMIBCompliance2.setObjects(
      *(("ATM-MIB", "atmInterfaceConfGroup2"),
        ("ATM-MIB", "atmTrafficDescrGroup2"))
)
if mibBuilder.loadTexts:
    atmMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-MIB",
    **{"atmMIB": atmMIB,
       "atmMIBObjects": atmMIBObjects,
       "atmInterfaceConfTable": atmInterfaceConfTable,
       "atmInterfaceConfEntry": atmInterfaceConfEntry,
       "atmInterfaceMaxVpcs": atmInterfaceMaxVpcs,
       "atmInterfaceMaxVccs": atmInterfaceMaxVccs,
       "atmInterfaceConfVpcs": atmInterfaceConfVpcs,
       "atmInterfaceConfVccs": atmInterfaceConfVccs,
       "atmInterfaceMaxActiveVpiBits": atmInterfaceMaxActiveVpiBits,
       "atmInterfaceMaxActiveVciBits": atmInterfaceMaxActiveVciBits,
       "atmInterfaceIlmiVpi": atmInterfaceIlmiVpi,
       "atmInterfaceIlmiVci": atmInterfaceIlmiVci,
       "atmInterfaceAddressType": atmInterfaceAddressType,
       "atmInterfaceAdminAddress": atmInterfaceAdminAddress,
       "atmInterfaceMyNeighborIpAddress": atmInterfaceMyNeighborIpAddress,
       "atmInterfaceMyNeighborIfName": atmInterfaceMyNeighborIfName,
       "atmInterfaceCurrentMaxVpiBits": atmInterfaceCurrentMaxVpiBits,
       "atmInterfaceCurrentMaxVciBits": atmInterfaceCurrentMaxVciBits,
       "atmInterfaceSubscrAddress": atmInterfaceSubscrAddress,
       "atmInterfaceDs3PlcpTable": atmInterfaceDs3PlcpTable,
       "atmInterfaceDs3PlcpEntry": atmInterfaceDs3PlcpEntry,
       "atmInterfaceDs3PlcpSEFSs": atmInterfaceDs3PlcpSEFSs,
       "atmInterfaceDs3PlcpAlarmState": atmInterfaceDs3PlcpAlarmState,
       "atmInterfaceDs3PlcpUASs": atmInterfaceDs3PlcpUASs,
       "atmInterfaceTCTable": atmInterfaceTCTable,
       "atmInterfaceTCEntry": atmInterfaceTCEntry,
       "atmInterfaceOCDEvents": atmInterfaceOCDEvents,
       "atmInterfaceTCAlarmState": atmInterfaceTCAlarmState,
       "atmTrafficDescrParamTable": atmTrafficDescrParamTable,
       "atmTrafficDescrParamEntry": atmTrafficDescrParamEntry,
       "atmTrafficDescrParamIndex": atmTrafficDescrParamIndex,
       "atmTrafficDescrType": atmTrafficDescrType,
       "atmTrafficDescrParam1": atmTrafficDescrParam1,
       "atmTrafficDescrParam2": atmTrafficDescrParam2,
       "atmTrafficDescrParam3": atmTrafficDescrParam3,
       "atmTrafficDescrParam4": atmTrafficDescrParam4,
       "atmTrafficDescrParam5": atmTrafficDescrParam5,
       "atmTrafficQoSClass": atmTrafficQoSClass,
       "atmTrafficDescrRowStatus": atmTrafficDescrRowStatus,
       "atmServiceCategory": atmServiceCategory,
       "atmTrafficFrameDiscard": atmTrafficFrameDiscard,
       "atmVplTable": atmVplTable,
       "atmVplEntry": atmVplEntry,
       "atmVplVpi": atmVplVpi,
       "atmVplAdminStatus": atmVplAdminStatus,
       "atmVplOperStatus": atmVplOperStatus,
       "atmVplLastChange": atmVplLastChange,
       "atmVplReceiveTrafficDescrIndex": atmVplReceiveTrafficDescrIndex,
       "atmVplTransmitTrafficDescrIndex": atmVplTransmitTrafficDescrIndex,
       "atmVplCrossConnectIdentifier": atmVplCrossConnectIdentifier,
       "atmVplRowStatus": atmVplRowStatus,
       "atmVplCastType": atmVplCastType,
       "atmVplConnKind": atmVplConnKind,
       "atmVclTable": atmVclTable,
       "atmVclEntry": atmVclEntry,
       "atmVclVpi": atmVclVpi,
       "atmVclVci": atmVclVci,
       "atmVclAdminStatus": atmVclAdminStatus,
       "atmVclOperStatus": atmVclOperStatus,
       "atmVclLastChange": atmVclLastChange,
       "atmVclReceiveTrafficDescrIndex": atmVclReceiveTrafficDescrIndex,
       "atmVclTransmitTrafficDescrIndex": atmVclTransmitTrafficDescrIndex,
       "atmVccAalType": atmVccAalType,
       "atmVccAal5CpcsTransmitSduSize": atmVccAal5CpcsTransmitSduSize,
       "atmVccAal5CpcsReceiveSduSize": atmVccAal5CpcsReceiveSduSize,
       "atmVccAal5EncapsType": atmVccAal5EncapsType,
       "atmVclCrossConnectIdentifier": atmVclCrossConnectIdentifier,
       "atmVclRowStatus": atmVclRowStatus,
       "atmVclCastType": atmVclCastType,
       "atmVclConnKind": atmVclConnKind,
       "atmVpCrossConnectIndexNext": atmVpCrossConnectIndexNext,
       "atmVpCrossConnectTable": atmVpCrossConnectTable,
       "atmVpCrossConnectEntry": atmVpCrossConnectEntry,
       "atmVpCrossConnectIndex": atmVpCrossConnectIndex,
       "atmVpCrossConnectLowIfIndex": atmVpCrossConnectLowIfIndex,
       "atmVpCrossConnectLowVpi": atmVpCrossConnectLowVpi,
       "atmVpCrossConnectHighIfIndex": atmVpCrossConnectHighIfIndex,
       "atmVpCrossConnectHighVpi": atmVpCrossConnectHighVpi,
       "atmVpCrossConnectAdminStatus": atmVpCrossConnectAdminStatus,
       "atmVpCrossConnectL2HOperStatus": atmVpCrossConnectL2HOperStatus,
       "atmVpCrossConnectH2LOperStatus": atmVpCrossConnectH2LOperStatus,
       "atmVpCrossConnectL2HLastChange": atmVpCrossConnectL2HLastChange,
       "atmVpCrossConnectH2LLastChange": atmVpCrossConnectH2LLastChange,
       "atmVpCrossConnectRowStatus": atmVpCrossConnectRowStatus,
       "atmVcCrossConnectIndexNext": atmVcCrossConnectIndexNext,
       "atmVcCrossConnectTable": atmVcCrossConnectTable,
       "atmVcCrossConnectEntry": atmVcCrossConnectEntry,
       "atmVcCrossConnectIndex": atmVcCrossConnectIndex,
       "atmVcCrossConnectLowIfIndex": atmVcCrossConnectLowIfIndex,
       "atmVcCrossConnectLowVpi": atmVcCrossConnectLowVpi,
       "atmVcCrossConnectLowVci": atmVcCrossConnectLowVci,
       "atmVcCrossConnectHighIfIndex": atmVcCrossConnectHighIfIndex,
       "atmVcCrossConnectHighVpi": atmVcCrossConnectHighVpi,
       "atmVcCrossConnectHighVci": atmVcCrossConnectHighVci,
       "atmVcCrossConnectAdminStatus": atmVcCrossConnectAdminStatus,
       "atmVcCrossConnectL2HOperStatus": atmVcCrossConnectL2HOperStatus,
       "atmVcCrossConnectH2LOperStatus": atmVcCrossConnectH2LOperStatus,
       "atmVcCrossConnectL2HLastChange": atmVcCrossConnectL2HLastChange,
       "atmVcCrossConnectH2LLastChange": atmVcCrossConnectH2LLastChange,
       "atmVcCrossConnectRowStatus": atmVcCrossConnectRowStatus,
       "aal5VccTable": aal5VccTable,
       "aal5VccEntry": aal5VccEntry,
       "aal5VccVpi": aal5VccVpi,
       "aal5VccVci": aal5VccVci,
       "aal5VccCrcErrors": aal5VccCrcErrors,
       "aal5VccSarTimeOuts": aal5VccSarTimeOuts,
       "aal5VccOverSizedSDUs": aal5VccOverSizedSDUs,
       "atmTrafficDescrParamIndexNext": atmTrafficDescrParamIndexNext,
       "atmMIBConformance": atmMIBConformance,
       "atmMIBGroups": atmMIBGroups,
       "atmInterfaceConfGroup": atmInterfaceConfGroup,
       "atmTrafficDescrGroup": atmTrafficDescrGroup,
       "atmInterfaceDs3PlcpGroup": atmInterfaceDs3PlcpGroup,
       "atmInterfaceTCGroup": atmInterfaceTCGroup,
       "atmVpcTerminationGroup": atmVpcTerminationGroup,
       "atmVccTerminationGroup": atmVccTerminationGroup,
       "atmVpCrossConnectGroup": atmVpCrossConnectGroup,
       "atmVcCrossConnectGroup": atmVcCrossConnectGroup,
       "aal5VccGroup": aal5VccGroup,
       "atmInterfaceConfGroup2": atmInterfaceConfGroup2,
       "atmTrafficDescrGroup2": atmTrafficDescrGroup2,
       "atmVpcTerminationGroup2": atmVpcTerminationGroup2,
       "atmVccTerminationGroup2": atmVccTerminationGroup2,
       "atmVplCrossConnectGroup": atmVplCrossConnectGroup,
       "atmVpPvcCrossConnectGroup": atmVpPvcCrossConnectGroup,
       "atmVclCrossConnectGroup": atmVclCrossConnectGroup,
       "atmVcPvcCrossConnectGroup": atmVcPvcCrossConnectGroup,
       "atmMIBCompliances": atmMIBCompliances,
       "atmMIBCompliance": atmMIBCompliance,
       "atmMIBCompliance2": atmMIBCompliance2}
)
