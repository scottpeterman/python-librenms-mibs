# SNMP MIB module (ARUBAWIRED-DIST-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-DIST-SERVICES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:06 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

arubaWiredDistServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25)
)
if mibBuilder.loadTexts:
    arubaWiredDistServicesMIB.setRevisions(
        ("2022-01-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredDSMStatus_ObjectIdentity = ObjectIdentity
arubaWiredDSMStatus = _ArubaWiredDSMStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 1)
)
_ArubaWiredDSMStatusTable_Object = MibTable
arubaWiredDSMStatusTable = _ArubaWiredDSMStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredDSMStatusTable.setStatus("current")
_ArubaWiredDSMStatusEntry_Object = MibTableRow
arubaWiredDSMStatusEntry = _ArubaWiredDSMStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 1, 1, 1)
)
arubaWiredDSMStatusEntry.setIndexNames(
    (0, "ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSMIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredDSMStatusEntry.setStatus("current")
_ArubaWiredDSMIndex_Type = Unsigned32
_ArubaWiredDSMIndex_Object = MibTableColumn
arubaWiredDSMIndex = _ArubaWiredDSMIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 1, 1, 1, 1),
    _ArubaWiredDSMIndex_Type()
)
arubaWiredDSMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredDSMIndex.setStatus("current")


class _ArubaWiredDSMName_Type(DisplayString):
    """Custom type arubaWiredDSMName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredDSMName_Type.__name__ = "DisplayString"
_ArubaWiredDSMName_Object = MibTableColumn
arubaWiredDSMName = _ArubaWiredDSMName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 1, 1, 1, 2),
    _ArubaWiredDSMName_Type()
)
arubaWiredDSMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSMName.setStatus("current")


class _ArubaWiredDSMDescr_Type(DisplayString):
    """Custom type arubaWiredDSMDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ArubaWiredDSMDescr_Type.__name__ = "DisplayString"
_ArubaWiredDSMDescr_Object = MibTableColumn
arubaWiredDSMDescr = _ArubaWiredDSMDescr_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 1, 1, 1, 3),
    _ArubaWiredDSMDescr_Type()
)
arubaWiredDSMDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSMDescr.setStatus("current")


class _ArubaWiredDSMSerialNum_Type(DisplayString):
    """Custom type arubaWiredDSMSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredDSMSerialNum_Type.__name__ = "DisplayString"
_ArubaWiredDSMSerialNum_Object = MibTableColumn
arubaWiredDSMSerialNum = _ArubaWiredDSMSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 1, 1, 1, 4),
    _ArubaWiredDSMSerialNum_Type()
)
arubaWiredDSMSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSMSerialNum.setStatus("current")


class _ArubaWiredDSMProductNum_Type(DisplayString):
    """Custom type arubaWiredDSMProductNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ArubaWiredDSMProductNum_Type.__name__ = "DisplayString"
_ArubaWiredDSMProductNum_Object = MibTableColumn
arubaWiredDSMProductNum = _ArubaWiredDSMProductNum_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 1, 1, 1, 5),
    _ArubaWiredDSMProductNum_Type()
)
arubaWiredDSMProductNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSMProductNum.setStatus("current")
_ArubaWiredDSMPhysAddress_Type = MacAddress
_ArubaWiredDSMPhysAddress_Object = MibTableColumn
arubaWiredDSMPhysAddress = _ArubaWiredDSMPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 1, 1, 1, 6),
    _ArubaWiredDSMPhysAddress_Type()
)
arubaWiredDSMPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSMPhysAddress.setStatus("current")


class _ArubaWiredDSMOperStatus_Type(Integer32):
    """Custom type arubaWiredDSMOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initializing", 1),
          ("ready", 2),
          ("failed", 3))
    )


_ArubaWiredDSMOperStatus_Type.__name__ = "Integer32"
_ArubaWiredDSMOperStatus_Object = MibTableColumn
arubaWiredDSMOperStatus = _ArubaWiredDSMOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 1, 1, 1, 7),
    _ArubaWiredDSMOperStatus_Type()
)
arubaWiredDSMOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSMOperStatus.setStatus("current")
_ArubaWiredDSSInterfaces_ObjectIdentity = ObjectIdentity
arubaWiredDSSInterfaces = _ArubaWiredDSSInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2)
)
_ArubaWiredDSSIfTable_Object = MibTable
arubaWiredDSSIfTable = _ArubaWiredDSSIfTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1)
)
if mibBuilder.loadTexts:
    arubaWiredDSSIfTable.setStatus("current")
_ArubaWiredDSSIfEntry_Object = MibTableRow
arubaWiredDSSIfEntry = _ArubaWiredDSSIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1)
)
arubaWiredDSSIfEntry.setIndexNames(
    (0, "ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSModuleIndex"),
    (0, "ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredDSSIfEntry.setStatus("current")


class _ArubaWiredDSSModuleIndex_Type(Integer32):
    """Custom type arubaWiredDSSModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredDSSModuleIndex_Type.__name__ = "Integer32"
_ArubaWiredDSSModuleIndex_Object = MibTableColumn
arubaWiredDSSModuleIndex = _ArubaWiredDSSModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 1),
    _ArubaWiredDSSModuleIndex_Type()
)
arubaWiredDSSModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredDSSModuleIndex.setStatus("current")


class _ArubaWiredDSSIfIndex_Type(Integer32):
    """Custom type arubaWiredDSSIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArubaWiredDSSIfIndex_Type.__name__ = "Integer32"
_ArubaWiredDSSIfIndex_Object = MibTableColumn
arubaWiredDSSIfIndex = _ArubaWiredDSSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 2),
    _ArubaWiredDSSIfIndex_Type()
)
arubaWiredDSSIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredDSSIfIndex.setStatus("current")


class _ArubaWiredDSSIfDescr_Type(DisplayString):
    """Custom type arubaWiredDSSIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ArubaWiredDSSIfDescr_Type.__name__ = "DisplayString"
_ArubaWiredDSSIfDescr_Object = MibTableColumn
arubaWiredDSSIfDescr = _ArubaWiredDSSIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 3),
    _ArubaWiredDSSIfDescr_Type()
)
arubaWiredDSSIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSSIfDescr.setStatus("current")
_ArubaWiredDSSIfInOctets_Type = Counter64
_ArubaWiredDSSIfInOctets_Object = MibTableColumn
arubaWiredDSSIfInOctets = _ArubaWiredDSSIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 4),
    _ArubaWiredDSSIfInOctets_Type()
)
arubaWiredDSSIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSSIfInOctets.setStatus("current")
_ArubaWiredDSSIfInUcastPkts_Type = Counter64
_ArubaWiredDSSIfInUcastPkts_Object = MibTableColumn
arubaWiredDSSIfInUcastPkts = _ArubaWiredDSSIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 5),
    _ArubaWiredDSSIfInUcastPkts_Type()
)
arubaWiredDSSIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSSIfInUcastPkts.setStatus("current")
_ArubaWiredDSSIfInDiscards_Type = Counter64
_ArubaWiredDSSIfInDiscards_Object = MibTableColumn
arubaWiredDSSIfInDiscards = _ArubaWiredDSSIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 6),
    _ArubaWiredDSSIfInDiscards_Type()
)
arubaWiredDSSIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSSIfInDiscards.setStatus("current")
_ArubaWiredDSSIfInErrors_Type = Counter64
_ArubaWiredDSSIfInErrors_Object = MibTableColumn
arubaWiredDSSIfInErrors = _ArubaWiredDSSIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 7),
    _ArubaWiredDSSIfInErrors_Type()
)
arubaWiredDSSIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSSIfInErrors.setStatus("current")
_ArubaWiredDSSIfInUnknownProtos_Type = Counter64
_ArubaWiredDSSIfInUnknownProtos_Object = MibTableColumn
arubaWiredDSSIfInUnknownProtos = _ArubaWiredDSSIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 8),
    _ArubaWiredDSSIfInUnknownProtos_Type()
)
arubaWiredDSSIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSSIfInUnknownProtos.setStatus("current")
_ArubaWiredDSSIfInMulticastPkts_Type = Counter64
_ArubaWiredDSSIfInMulticastPkts_Object = MibTableColumn
arubaWiredDSSIfInMulticastPkts = _ArubaWiredDSSIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 9),
    _ArubaWiredDSSIfInMulticastPkts_Type()
)
arubaWiredDSSIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSSIfInMulticastPkts.setStatus("current")
_ArubaWiredDSSIfInBroadcastPkts_Type = Counter64
_ArubaWiredDSSIfInBroadcastPkts_Object = MibTableColumn
arubaWiredDSSIfInBroadcastPkts = _ArubaWiredDSSIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 10),
    _ArubaWiredDSSIfInBroadcastPkts_Type()
)
arubaWiredDSSIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSSIfInBroadcastPkts.setStatus("current")
_ArubaWiredDSSIfOutOctets_Type = Counter64
_ArubaWiredDSSIfOutOctets_Object = MibTableColumn
arubaWiredDSSIfOutOctets = _ArubaWiredDSSIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 11),
    _ArubaWiredDSSIfOutOctets_Type()
)
arubaWiredDSSIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSSIfOutOctets.setStatus("current")
_ArubaWiredDSSIfOutUcastPkts_Type = Counter64
_ArubaWiredDSSIfOutUcastPkts_Object = MibTableColumn
arubaWiredDSSIfOutUcastPkts = _ArubaWiredDSSIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 12),
    _ArubaWiredDSSIfOutUcastPkts_Type()
)
arubaWiredDSSIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSSIfOutUcastPkts.setStatus("current")
_ArubaWiredDSSIfOutDiscards_Type = Counter64
_ArubaWiredDSSIfOutDiscards_Object = MibTableColumn
arubaWiredDSSIfOutDiscards = _ArubaWiredDSSIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 13),
    _ArubaWiredDSSIfOutDiscards_Type()
)
arubaWiredDSSIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSSIfOutDiscards.setStatus("current")
_ArubaWiredDSSIfOutErrors_Type = Counter64
_ArubaWiredDSSIfOutErrors_Object = MibTableColumn
arubaWiredDSSIfOutErrors = _ArubaWiredDSSIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 14),
    _ArubaWiredDSSIfOutErrors_Type()
)
arubaWiredDSSIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSSIfOutErrors.setStatus("current")
_ArubaWiredDSSIfOutMulticastPkts_Type = Counter64
_ArubaWiredDSSIfOutMulticastPkts_Object = MibTableColumn
arubaWiredDSSIfOutMulticastPkts = _ArubaWiredDSSIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 15),
    _ArubaWiredDSSIfOutMulticastPkts_Type()
)
arubaWiredDSSIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSSIfOutMulticastPkts.setStatus("current")
_ArubaWiredDSSIfOutBroadcastPkts_Type = Counter64
_ArubaWiredDSSIfOutBroadcastPkts_Object = MibTableColumn
arubaWiredDSSIfOutBroadcastPkts = _ArubaWiredDSSIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 2, 1, 1, 16),
    _ArubaWiredDSSIfOutBroadcastPkts_Type()
)
arubaWiredDSSIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredDSSIfOutBroadcastPkts.setStatus("current")
_ArubaWiredDSSConformance_ObjectIdentity = ObjectIdentity
arubaWiredDSSConformance = _ArubaWiredDSSConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 3)
)
_ArubaWiredDSSCompliances_ObjectIdentity = ObjectIdentity
arubaWiredDSSCompliances = _ArubaWiredDSSCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 3, 1)
)
_ArubaWiredDSSGroups_ObjectIdentity = ObjectIdentity
arubaWiredDSSGroups = _ArubaWiredDSSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 3, 2)
)

# Managed Objects groups

arubaWiredDSMStatusTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 3, 2, 1)
)
arubaWiredDSMStatusTableGroup.setObjects(
      *(("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSMName"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSMDescr"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSMSerialNum"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSMProductNum"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSMPhysAddress"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSMOperStatus"))
)
if mibBuilder.loadTexts:
    arubaWiredDSMStatusTableGroup.setStatus("current")

arubaWiredDSSIfTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 3, 2, 2)
)
arubaWiredDSSIfTableGroup.setObjects(
      *(("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfDescr"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfInOctets"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfInUcastPkts"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfInDiscards"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfInErrors"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfInUnknownProtos"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfInMulticastPkts"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfInBroadcastPkts"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfOutOctets"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfOutUcastPkts"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfOutDiscards"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfOutErrors"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfOutMulticastPkts"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfOutBroadcastPkts"))
)
if mibBuilder.loadTexts:
    arubaWiredDSSIfTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredDSSMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25, 3, 1, 1)
)
arubaWiredDSSMibCompliance.setObjects(
      *(("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSMStatusTableGroup"),
        ("ARUBAWIRED-DIST-SERVICES-MIB", "arubaWiredDSSIfTableGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredDSSMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-DIST-SERVICES-MIB",
    **{"arubaWiredDistServicesMIB": arubaWiredDistServicesMIB,
       "arubaWiredDSMStatus": arubaWiredDSMStatus,
       "arubaWiredDSMStatusTable": arubaWiredDSMStatusTable,
       "arubaWiredDSMStatusEntry": arubaWiredDSMStatusEntry,
       "arubaWiredDSMIndex": arubaWiredDSMIndex,
       "arubaWiredDSMName": arubaWiredDSMName,
       "arubaWiredDSMDescr": arubaWiredDSMDescr,
       "arubaWiredDSMSerialNum": arubaWiredDSMSerialNum,
       "arubaWiredDSMProductNum": arubaWiredDSMProductNum,
       "arubaWiredDSMPhysAddress": arubaWiredDSMPhysAddress,
       "arubaWiredDSMOperStatus": arubaWiredDSMOperStatus,
       "arubaWiredDSSInterfaces": arubaWiredDSSInterfaces,
       "arubaWiredDSSIfTable": arubaWiredDSSIfTable,
       "arubaWiredDSSIfEntry": arubaWiredDSSIfEntry,
       "arubaWiredDSSModuleIndex": arubaWiredDSSModuleIndex,
       "arubaWiredDSSIfIndex": arubaWiredDSSIfIndex,
       "arubaWiredDSSIfDescr": arubaWiredDSSIfDescr,
       "arubaWiredDSSIfInOctets": arubaWiredDSSIfInOctets,
       "arubaWiredDSSIfInUcastPkts": arubaWiredDSSIfInUcastPkts,
       "arubaWiredDSSIfInDiscards": arubaWiredDSSIfInDiscards,
       "arubaWiredDSSIfInErrors": arubaWiredDSSIfInErrors,
       "arubaWiredDSSIfInUnknownProtos": arubaWiredDSSIfInUnknownProtos,
       "arubaWiredDSSIfInMulticastPkts": arubaWiredDSSIfInMulticastPkts,
       "arubaWiredDSSIfInBroadcastPkts": arubaWiredDSSIfInBroadcastPkts,
       "arubaWiredDSSIfOutOctets": arubaWiredDSSIfOutOctets,
       "arubaWiredDSSIfOutUcastPkts": arubaWiredDSSIfOutUcastPkts,
       "arubaWiredDSSIfOutDiscards": arubaWiredDSSIfOutDiscards,
       "arubaWiredDSSIfOutErrors": arubaWiredDSSIfOutErrors,
       "arubaWiredDSSIfOutMulticastPkts": arubaWiredDSSIfOutMulticastPkts,
       "arubaWiredDSSIfOutBroadcastPkts": arubaWiredDSSIfOutBroadcastPkts,
       "arubaWiredDSSConformance": arubaWiredDSSConformance,
       "arubaWiredDSSCompliances": arubaWiredDSSCompliances,
       "arubaWiredDSSMibCompliance": arubaWiredDSSMibCompliance,
       "arubaWiredDSSGroups": arubaWiredDSSGroups,
       "arubaWiredDSMStatusTableGroup": arubaWiredDSMStatusTableGroup,
       "arubaWiredDSSIfTableGroup": arubaWiredDSSIfTableGroup}
)
