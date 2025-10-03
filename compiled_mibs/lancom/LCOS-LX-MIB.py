# SNMP MIB module (LCOS-LX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\lancom\LCOS-LX-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:08:10 2025
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
 enterprises,
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
    "enterprises",
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

lcosLX = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13)
)
if mibBuilder.loadTexts:
    lcosLX.setRevisions(
        ("2021-05-06 22:34",
         "2021-03-23 21:51")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LcosLXTrapsGrp_ObjectIdentity = ObjectIdentity
lcosLXTrapsGrp = _LcosLXTrapsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 0)
)
_LcosLXWifiTraps_ObjectIdentity = ObjectIdentity
lcosLXWifiTraps = _LcosLXWifiTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 0, 0)
)
_LcosLXStatus_ObjectIdentity = ObjectIdentity
lcosLXStatus = _LcosLXStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1)
)


class _LcosLXStatusOperatingTime_Type(Unsigned32):
    """Custom type lcosLXStatusOperatingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusOperatingTime_Type.__name__ = "Unsigned32"
_LcosLXStatusOperatingTime_Object = MibScalar
lcosLXStatusOperatingTime = _LcosLXStatusOperatingTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 2),
    _LcosLXStatusOperatingTime_Type()
)
lcosLXStatusOperatingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusOperatingTime.setStatus("current")
_LcosLXStatusWLAN_ObjectIdentity = ObjectIdentity
lcosLXStatusWLAN = _LcosLXStatusWLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3)
)


class _LcosLXStatusWLANEnvironmentScanStatus_Type(OctetString):
    """Custom type lcosLXStatusWLANEnvironmentScanStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_LcosLXStatusWLANEnvironmentScanStatus_Type.__name__ = "OctetString"
_LcosLXStatusWLANEnvironmentScanStatus_Object = MibScalar
lcosLXStatusWLANEnvironmentScanStatus = _LcosLXStatusWLANEnvironmentScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 1),
    _LcosLXStatusWLANEnvironmentScanStatus_Type()
)
lcosLXStatusWLANEnvironmentScanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANEnvironmentScanStatus.setStatus("current")


class _LcosLXStatusWLANEnvironmentScanStatusShort_Type(Integer32):
    """Custom type lcosLXStatusWLANEnvironmentScanStatusShort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNever", 0),
          ("eScanning", 1),
          ("eScanned", 2))
    )


_LcosLXStatusWLANEnvironmentScanStatusShort_Type.__name__ = "Integer32"
_LcosLXStatusWLANEnvironmentScanStatusShort_Object = MibScalar
lcosLXStatusWLANEnvironmentScanStatusShort = _LcosLXStatusWLANEnvironmentScanStatusShort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 3),
    _LcosLXStatusWLANEnvironmentScanStatusShort_Type()
)
lcosLXStatusWLANEnvironmentScanStatusShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANEnvironmentScanStatusShort.setStatus("current")
_LcosLXStatusWLANClientManagement_ObjectIdentity = ObjectIdentity
lcosLXStatusWLANClientManagement = _LcosLXStatusWLANClientManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4)
)
_LcosLXStatusWLANClientManagementStationTable_Object = MibTable
lcosLXStatusWLANClientManagementStationTable = _LcosLXStatusWLANClientManagementStationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementStationTable.setStatus("current")
_LcosLXStatusWLANClientManagementStationEntry_Object = MibTableRow
lcosLXStatusWLANClientManagementStationEntry = _LcosLXStatusWLANClientManagementStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 1, 1)
)
lcosLXStatusWLANClientManagementStationEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANClientManagementStationEntryMACAddress"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementStationEntry.setStatus("current")
_LcosLXStatusWLANClientManagementStationEntryMACAddress_Type = MacAddress
_LcosLXStatusWLANClientManagementStationEntryMACAddress_Object = MibTableColumn
lcosLXStatusWLANClientManagementStationEntryMACAddress = _LcosLXStatusWLANClientManagementStationEntryMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 1, 1, 1),
    _LcosLXStatusWLANClientManagementStationEntryMACAddress_Type()
)
lcosLXStatusWLANClientManagementStationEntryMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementStationEntryMACAddress.setStatus("current")


class _LcosLXStatusWLANClientManagementStationEntryChannel_Type(Unsigned32):
    """Custom type lcosLXStatusWLANClientManagementStationEntryChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANClientManagementStationEntryChannel_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANClientManagementStationEntryChannel_Object = MibTableColumn
lcosLXStatusWLANClientManagementStationEntryChannel = _LcosLXStatusWLANClientManagementStationEntryChannel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 1, 1, 2),
    _LcosLXStatusWLANClientManagementStationEntryChannel_Type()
)
lcosLXStatusWLANClientManagementStationEntryChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementStationEntryChannel.setStatus("current")


class _LcosLXStatusWLANClientManagementStationEntryActive_Type(Integer32):
    """Custom type lcosLXStatusWLANClientManagementStationEntryActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANClientManagementStationEntryActive_Type.__name__ = "Integer32"
_LcosLXStatusWLANClientManagementStationEntryActive_Object = MibTableColumn
lcosLXStatusWLANClientManagementStationEntryActive = _LcosLXStatusWLANClientManagementStationEntryActive_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 1, 1, 3),
    _LcosLXStatusWLANClientManagementStationEntryActive_Type()
)
lcosLXStatusWLANClientManagementStationEntryActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementStationEntryActive.setStatus("current")


class _LcosLXStatusWLANClientManagementStationEntryDualBand_Type(Integer32):
    """Custom type lcosLXStatusWLANClientManagementStationEntryDualBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANClientManagementStationEntryDualBand_Type.__name__ = "Integer32"
_LcosLXStatusWLANClientManagementStationEntryDualBand_Object = MibTableColumn
lcosLXStatusWLANClientManagementStationEntryDualBand = _LcosLXStatusWLANClientManagementStationEntryDualBand_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 1, 1, 4),
    _LcosLXStatusWLANClientManagementStationEntryDualBand_Type()
)
lcosLXStatusWLANClientManagementStationEntryDualBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementStationEntryDualBand.setStatus("current")


class _LcosLXStatusWLANClientManagementStationEntryBTMSupport_Type(Integer32):
    """Custom type lcosLXStatusWLANClientManagementStationEntryBTMSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANClientManagementStationEntryBTMSupport_Type.__name__ = "Integer32"
_LcosLXStatusWLANClientManagementStationEntryBTMSupport_Object = MibTableColumn
lcosLXStatusWLANClientManagementStationEntryBTMSupport = _LcosLXStatusWLANClientManagementStationEntryBTMSupport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 1, 1, 5),
    _LcosLXStatusWLANClientManagementStationEntryBTMSupport_Type()
)
lcosLXStatusWLANClientManagementStationEntryBTMSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementStationEntryBTMSupport.setStatus("current")


class _LcosLXStatusWLANClientManagementStationEntryRRMSupport_Type(Integer32):
    """Custom type lcosLXStatusWLANClientManagementStationEntryRRMSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANClientManagementStationEntryRRMSupport_Type.__name__ = "Integer32"
_LcosLXStatusWLANClientManagementStationEntryRRMSupport_Object = MibTableColumn
lcosLXStatusWLANClientManagementStationEntryRRMSupport = _LcosLXStatusWLANClientManagementStationEntryRRMSupport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 1, 1, 6),
    _LcosLXStatusWLANClientManagementStationEntryRRMSupport_Type()
)
lcosLXStatusWLANClientManagementStationEntryRRMSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementStationEntryRRMSupport.setStatus("current")


class _LcosLXStatusWLANClientManagementStationEntryBTMUnfriendly_Type(Integer32):
    """Custom type lcosLXStatusWLANClientManagementStationEntryBTMUnfriendly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANClientManagementStationEntryBTMUnfriendly_Type.__name__ = "Integer32"
_LcosLXStatusWLANClientManagementStationEntryBTMUnfriendly_Object = MibTableColumn
lcosLXStatusWLANClientManagementStationEntryBTMUnfriendly = _LcosLXStatusWLANClientManagementStationEntryBTMUnfriendly_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 1, 1, 7),
    _LcosLXStatusWLANClientManagementStationEntryBTMUnfriendly_Type()
)
lcosLXStatusWLANClientManagementStationEntryBTMUnfriendly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementStationEntryBTMUnfriendly.setStatus("current")


class _LcosLXStatusWLANClientManagementStationEntryBTMCompliance_Type(Integer32):
    """Custom type lcosLXStatusWLANClientManagementStationEntryBTMCompliance based on Integer32"""
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
        *(("eUnknown", 0),
          ("eIdle", 1),
          ("eActiveUnfriendly", 2),
          ("eActive", 3))
    )


_LcosLXStatusWLANClientManagementStationEntryBTMCompliance_Type.__name__ = "Integer32"
_LcosLXStatusWLANClientManagementStationEntryBTMCompliance_Object = MibTableColumn
lcosLXStatusWLANClientManagementStationEntryBTMCompliance = _LcosLXStatusWLANClientManagementStationEntryBTMCompliance_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 1, 1, 8),
    _LcosLXStatusWLANClientManagementStationEntryBTMCompliance_Type()
)
lcosLXStatusWLANClientManagementStationEntryBTMCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementStationEntryBTMCompliance.setStatus("current")


class _LcosLXStatusWLANClientManagementStationEntrySteeringUnfriendly_Type(Integer32):
    """Custom type lcosLXStatusWLANClientManagementStationEntrySteeringUnfriendly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANClientManagementStationEntrySteeringUnfriendly_Type.__name__ = "Integer32"
_LcosLXStatusWLANClientManagementStationEntrySteeringUnfriendly_Object = MibTableColumn
lcosLXStatusWLANClientManagementStationEntrySteeringUnfriendly = _LcosLXStatusWLANClientManagementStationEntrySteeringUnfriendly_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 1, 1, 9),
    _LcosLXStatusWLANClientManagementStationEntrySteeringUnfriendly_Type()
)
lcosLXStatusWLANClientManagementStationEntrySteeringUnfriendly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementStationEntrySteeringUnfriendly.setStatus("current")


class _LcosLXStatusWLANClientManagementStationEntrySteeringProhibited_Type(Integer32):
    """Custom type lcosLXStatusWLANClientManagementStationEntrySteeringProhibited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANClientManagementStationEntrySteeringProhibited_Type.__name__ = "Integer32"
_LcosLXStatusWLANClientManagementStationEntrySteeringProhibited_Object = MibTableColumn
lcosLXStatusWLANClientManagementStationEntrySteeringProhibited = _LcosLXStatusWLANClientManagementStationEntrySteeringProhibited_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 1, 1, 10),
    _LcosLXStatusWLANClientManagementStationEntrySteeringProhibited_Type()
)
lcosLXStatusWLANClientManagementStationEntrySteeringProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementStationEntrySteeringProhibited.setStatus("current")
_LcosLXStatusWLANClientManagementChannelTable_Object = MibTable
lcosLXStatusWLANClientManagementChannelTable = _LcosLXStatusWLANClientManagementChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementChannelTable.setStatus("current")
_LcosLXStatusWLANClientManagementChannelEntry_Object = MibTableRow
lcosLXStatusWLANClientManagementChannelEntry = _LcosLXStatusWLANClientManagementChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 2, 1)
)
lcosLXStatusWLANClientManagementChannelEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANClientManagementChannelEntryChannel"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementChannelEntry.setStatus("current")


class _LcosLXStatusWLANClientManagementChannelEntryChannel_Type(Unsigned32):
    """Custom type lcosLXStatusWLANClientManagementChannelEntryChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANClientManagementChannelEntryChannel_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANClientManagementChannelEntryChannel_Object = MibTableColumn
lcosLXStatusWLANClientManagementChannelEntryChannel = _LcosLXStatusWLANClientManagementChannelEntryChannel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 2, 1, 1),
    _LcosLXStatusWLANClientManagementChannelEntryChannel_Type()
)
lcosLXStatusWLANClientManagementChannelEntryChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementChannelEntryChannel.setStatus("current")


class _LcosLXStatusWLANClientManagementChannelEntryUtilization_Type(Unsigned32):
    """Custom type lcosLXStatusWLANClientManagementChannelEntryUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANClientManagementChannelEntryUtilization_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANClientManagementChannelEntryUtilization_Object = MibTableColumn
lcosLXStatusWLANClientManagementChannelEntryUtilization = _LcosLXStatusWLANClientManagementChannelEntryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 2, 1, 2),
    _LcosLXStatusWLANClientManagementChannelEntryUtilization_Type()
)
lcosLXStatusWLANClientManagementChannelEntryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementChannelEntryUtilization.setStatus("current")


class _LcosLXStatusWLANClientManagementChannelEntryOverload_Type(Integer32):
    """Custom type lcosLXStatusWLANClientManagementChannelEntryOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANClientManagementChannelEntryOverload_Type.__name__ = "Integer32"
_LcosLXStatusWLANClientManagementChannelEntryOverload_Object = MibTableColumn
lcosLXStatusWLANClientManagementChannelEntryOverload = _LcosLXStatusWLANClientManagementChannelEntryOverload_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 2, 1, 3),
    _LcosLXStatusWLANClientManagementChannelEntryOverload_Type()
)
lcosLXStatusWLANClientManagementChannelEntryOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementChannelEntryOverload.setStatus("current")
_LcosLXStatusWLANClientManagementSteeringLog_Object = MibTable
lcosLXStatusWLANClientManagementSteeringLog = _LcosLXStatusWLANClientManagementSteeringLog_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementSteeringLog.setStatus("current")
_LcosLXStatusWLANClientManagementSteeringLogEntry_Object = MibTableRow
lcosLXStatusWLANClientManagementSteeringLogEntry = _LcosLXStatusWLANClientManagementSteeringLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 3, 1)
)
lcosLXStatusWLANClientManagementSteeringLogEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANClientManagementSteeringLogEntryID"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementSteeringLogEntry.setStatus("current")


class _LcosLXStatusWLANClientManagementSteeringLogEntryID_Type(Unsigned32):
    """Custom type lcosLXStatusWLANClientManagementSteeringLogEntryID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANClientManagementSteeringLogEntryID_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANClientManagementSteeringLogEntryID_Object = MibTableColumn
lcosLXStatusWLANClientManagementSteeringLogEntryID = _LcosLXStatusWLANClientManagementSteeringLogEntryID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 3, 1, 1),
    _LcosLXStatusWLANClientManagementSteeringLogEntryID_Type()
)
lcosLXStatusWLANClientManagementSteeringLogEntryID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementSteeringLogEntryID.setStatus("current")


class _LcosLXStatusWLANClientManagementSteeringLogEntryTimestampEpoch_Type(Unsigned32):
    """Custom type lcosLXStatusWLANClientManagementSteeringLogEntryTimestampEpoch based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANClientManagementSteeringLogEntryTimestampEpoch_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANClientManagementSteeringLogEntryTimestampEpoch_Object = MibTableColumn
lcosLXStatusWLANClientManagementSteeringLogEntryTimestampEpoch = _LcosLXStatusWLANClientManagementSteeringLogEntryTimestampEpoch_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 3, 1, 2),
    _LcosLXStatusWLANClientManagementSteeringLogEntryTimestampEpoch_Type()
)
lcosLXStatusWLANClientManagementSteeringLogEntryTimestampEpoch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementSteeringLogEntryTimestampEpoch.setStatus("current")


class _LcosLXStatusWLANClientManagementSteeringLogEntryTimestamp_Type(OctetString):
    """Custom type lcosLXStatusWLANClientManagementSteeringLogEntryTimestamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LcosLXStatusWLANClientManagementSteeringLogEntryTimestamp_Type.__name__ = "OctetString"
_LcosLXStatusWLANClientManagementSteeringLogEntryTimestamp_Object = MibTableColumn
lcosLXStatusWLANClientManagementSteeringLogEntryTimestamp = _LcosLXStatusWLANClientManagementSteeringLogEntryTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 3, 1, 3),
    _LcosLXStatusWLANClientManagementSteeringLogEntryTimestamp_Type()
)
lcosLXStatusWLANClientManagementSteeringLogEntryTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementSteeringLogEntryTimestamp.setStatus("current")
_LcosLXStatusWLANClientManagementSteeringLogEntryMACAddress_Type = MacAddress
_LcosLXStatusWLANClientManagementSteeringLogEntryMACAddress_Object = MibTableColumn
lcosLXStatusWLANClientManagementSteeringLogEntryMACAddress = _LcosLXStatusWLANClientManagementSteeringLogEntryMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 3, 1, 4),
    _LcosLXStatusWLANClientManagementSteeringLogEntryMACAddress_Type()
)
lcosLXStatusWLANClientManagementSteeringLogEntryMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementSteeringLogEntryMACAddress.setStatus("current")


class _LcosLXStatusWLANClientManagementSteeringLogEntryReason_Type(Integer32):
    """Custom type lcosLXStatusWLANClientManagementSteeringLogEntryReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eUnknown", 0),
          ("eActiveUpgrade", 1),
          ("eActiveDowngradeRate", 2),
          ("eActiveDowngradeRSSI", 3),
          ("eIdleUpgrade", 4),
          ("eIdleDowngrade", 5),
          ("eActiveOffload", 6),
          ("eIdleOffload", 7),
          ("eInterferenceAvoidance", 8))
    )


_LcosLXStatusWLANClientManagementSteeringLogEntryReason_Type.__name__ = "Integer32"
_LcosLXStatusWLANClientManagementSteeringLogEntryReason_Object = MibTableColumn
lcosLXStatusWLANClientManagementSteeringLogEntryReason = _LcosLXStatusWLANClientManagementSteeringLogEntryReason_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 3, 1, 5),
    _LcosLXStatusWLANClientManagementSteeringLogEntryReason_Type()
)
lcosLXStatusWLANClientManagementSteeringLogEntryReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementSteeringLogEntryReason.setStatus("current")


class _LcosLXStatusWLANClientManagementSteeringLogEntryChannel_Type(Unsigned32):
    """Custom type lcosLXStatusWLANClientManagementSteeringLogEntryChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANClientManagementSteeringLogEntryChannel_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANClientManagementSteeringLogEntryChannel_Object = MibTableColumn
lcosLXStatusWLANClientManagementSteeringLogEntryChannel = _LcosLXStatusWLANClientManagementSteeringLogEntryChannel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 3, 1, 6),
    _LcosLXStatusWLANClientManagementSteeringLogEntryChannel_Type()
)
lcosLXStatusWLANClientManagementSteeringLogEntryChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementSteeringLogEntryChannel.setStatus("current")


class _LcosLXStatusWLANClientManagementSteeringLogEntryCandidates_Type(OctetString):
    """Custom type lcosLXStatusWLANClientManagementSteeringLogEntryCandidates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANClientManagementSteeringLogEntryCandidates_Type.__name__ = "OctetString"
_LcosLXStatusWLANClientManagementSteeringLogEntryCandidates_Object = MibTableColumn
lcosLXStatusWLANClientManagementSteeringLogEntryCandidates = _LcosLXStatusWLANClientManagementSteeringLogEntryCandidates_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 3, 1, 7),
    _LcosLXStatusWLANClientManagementSteeringLogEntryCandidates_Type()
)
lcosLXStatusWLANClientManagementSteeringLogEntryCandidates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementSteeringLogEntryCandidates.setStatus("current")


class _LcosLXStatusWLANClientManagementSteeringLogEntryType_Type(Integer32):
    """Custom type lcosLXStatusWLANClientManagementSteeringLogEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("eUnknown", 0),
          ("eNone", 1),
          ("eLegacy", 2),
          ("eBTMAndBlacklist", 3),
          ("eBTM", 4),
          ("eBTMAndBlacklistActive", 5),
          ("eBTMActive", 6),
          ("ePreassociation", 7),
          ("eBTMBE", 8),
          ("eBTMBEActive", 9),
          ("eBTMBlacklistBE", 10),
          ("eBTMBlacklistBEActive", 11),
          ("eLegacyBE", 12),
          ("eBTMBEActiveForce", 13))
    )


_LcosLXStatusWLANClientManagementSteeringLogEntryType_Type.__name__ = "Integer32"
_LcosLXStatusWLANClientManagementSteeringLogEntryType_Object = MibTableColumn
lcosLXStatusWLANClientManagementSteeringLogEntryType = _LcosLXStatusWLANClientManagementSteeringLogEntryType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 3, 1, 8),
    _LcosLXStatusWLANClientManagementSteeringLogEntryType_Type()
)
lcosLXStatusWLANClientManagementSteeringLogEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementSteeringLogEntryType.setStatus("current")


class _LcosLXStatusWLANClientManagementSteeringLogEntryState_Type(Integer32):
    """Custom type lcosLXStatusWLANClientManagementSteeringLogEntryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("eUnknown", 0),
          ("eRunning", 1),
          ("eSuccess", 2),
          ("eAbortAuthReject", 3),
          ("eAbortLowRSSI", 4),
          ("eAbortChangeTarget", 5),
          ("eBTMReject", 6),
          ("eBTMResponseTimeout", 7),
          ("eAssocTimeout", 8),
          ("eChannelChange", 9),
          ("ePrepareFail", 10),
          ("eUnexpectedBSS", 11))
    )


_LcosLXStatusWLANClientManagementSteeringLogEntryState_Type.__name__ = "Integer32"
_LcosLXStatusWLANClientManagementSteeringLogEntryState_Object = MibTableColumn
lcosLXStatusWLANClientManagementSteeringLogEntryState = _LcosLXStatusWLANClientManagementSteeringLogEntryState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 4, 3, 1, 9),
    _LcosLXStatusWLANClientManagementSteeringLogEntryState_Type()
)
lcosLXStatusWLANClientManagementSteeringLogEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANClientManagementSteeringLogEntryState.setStatus("current")


class _LcosLXStatusWLANAutomaticEnvironmentScanTime_Type(OctetString):
    """Custom type lcosLXStatusWLANAutomaticEnvironmentScanTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_LcosLXStatusWLANAutomaticEnvironmentScanTime_Type.__name__ = "OctetString"
_LcosLXStatusWLANAutomaticEnvironmentScanTime_Object = MibScalar
lcosLXStatusWLANAutomaticEnvironmentScanTime = _LcosLXStatusWLANAutomaticEnvironmentScanTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 6),
    _LcosLXStatusWLANAutomaticEnvironmentScanTime_Type()
)
lcosLXStatusWLANAutomaticEnvironmentScanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANAutomaticEnvironmentScanTime.setStatus("current")
_LcosLXStatusWLANHotspots_ObjectIdentity = ObjectIdentity
lcosLXStatusWLANHotspots = _LcosLXStatusWLANHotspots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 12)
)
_LcosLXStatusWLANHotspotsHotspots_Object = MibTable
lcosLXStatusWLANHotspotsHotspots = _LcosLXStatusWLANHotspotsHotspots_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 12, 1)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANHotspotsHotspots.setStatus("current")
_LcosLXStatusWLANHotspotsHotspotsEntry_Object = MibTableRow
lcosLXStatusWLANHotspotsHotspotsEntry = _LcosLXStatusWLANHotspotsHotspotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 12, 1, 1)
)
lcosLXStatusWLANHotspotsHotspotsEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANHotspotsHotspotsEntryHotspot"),
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANHotspotsHotspotsEntryMACAddress"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANHotspotsHotspotsEntry.setStatus("current")


class _LcosLXStatusWLANHotspotsHotspotsEntryHotspot_Type(OctetString):
    """Custom type lcosLXStatusWLANHotspotsHotspotsEntryHotspot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANHotspotsHotspotsEntryHotspot_Type.__name__ = "OctetString"
_LcosLXStatusWLANHotspotsHotspotsEntryHotspot_Object = MibTableColumn
lcosLXStatusWLANHotspotsHotspotsEntryHotspot = _LcosLXStatusWLANHotspotsHotspotsEntryHotspot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 12, 1, 1, 1),
    _LcosLXStatusWLANHotspotsHotspotsEntryHotspot_Type()
)
lcosLXStatusWLANHotspotsHotspotsEntryHotspot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANHotspotsHotspotsEntryHotspot.setStatus("current")
_LcosLXStatusWLANHotspotsHotspotsEntryMACAddress_Type = MacAddress
_LcosLXStatusWLANHotspotsHotspotsEntryMACAddress_Object = MibTableColumn
lcosLXStatusWLANHotspotsHotspotsEntryMACAddress = _LcosLXStatusWLANHotspotsHotspotsEntryMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 12, 1, 1, 2),
    _LcosLXStatusWLANHotspotsHotspotsEntryMACAddress_Type()
)
lcosLXStatusWLANHotspotsHotspotsEntryMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANHotspotsHotspotsEntryMACAddress.setStatus("current")


class _LcosLXStatusWLANHotspotsHotspotsEntryLastLoggedIn_Type(Unsigned32):
    """Custom type lcosLXStatusWLANHotspotsHotspotsEntryLastLoggedIn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANHotspotsHotspotsEntryLastLoggedIn_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANHotspotsHotspotsEntryLastLoggedIn_Object = MibTableColumn
lcosLXStatusWLANHotspotsHotspotsEntryLastLoggedIn = _LcosLXStatusWLANHotspotsHotspotsEntryLastLoggedIn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 12, 1, 1, 3),
    _LcosLXStatusWLANHotspotsHotspotsEntryLastLoggedIn_Type()
)
lcosLXStatusWLANHotspotsHotspotsEntryLastLoggedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANHotspotsHotspotsEntryLastLoggedIn.setStatus("current")


class _LcosLXStatusWLANHotspotsHotspotsEntryValidUntil_Type(Unsigned32):
    """Custom type lcosLXStatusWLANHotspotsHotspotsEntryValidUntil based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANHotspotsHotspotsEntryValidUntil_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANHotspotsHotspotsEntryValidUntil_Object = MibTableColumn
lcosLXStatusWLANHotspotsHotspotsEntryValidUntil = _LcosLXStatusWLANHotspotsHotspotsEntryValidUntil_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 12, 1, 1, 4),
    _LcosLXStatusWLANHotspotsHotspotsEntryValidUntil_Type()
)
lcosLXStatusWLANHotspotsHotspotsEntryValidUntil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANHotspotsHotspotsEntryValidUntil.setStatus("current")
_LcosLXStatusWLANStationTable_Object = MibTable
lcosLXStatusWLANStationTable = _LcosLXStatusWLANStationTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationTable.setStatus("current")
_LcosLXStatusWLANStationEntry_Object = MibTableRow
lcosLXStatusWLANStationEntry = _LcosLXStatusWLANStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1)
)
lcosLXStatusWLANStationEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANStationEntryMACAddress"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntry.setStatus("current")


class _LcosLXStatusWLANStationEntryRadioBand_Type(Integer32):
    """Custom type lcosLXStatusWLANStationEntryRadioBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e24GHz", 1),
          ("e5GHz", 2))
    )


_LcosLXStatusWLANStationEntryRadioBand_Type.__name__ = "Integer32"
_LcosLXStatusWLANStationEntryRadioBand_Object = MibTableColumn
lcosLXStatusWLANStationEntryRadioBand = _LcosLXStatusWLANStationEntryRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 2),
    _LcosLXStatusWLANStationEntryRadioBand_Type()
)
lcosLXStatusWLANStationEntryRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryRadioBand.setStatus("current")


class _LcosLXStatusWLANStationEntryIfc_Type(OctetString):
    """Custom type lcosLXStatusWLANStationEntryIfc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LcosLXStatusWLANStationEntryIfc_Type.__name__ = "OctetString"
_LcosLXStatusWLANStationEntryIfc_Object = MibTableColumn
lcosLXStatusWLANStationEntryIfc = _LcosLXStatusWLANStationEntryIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 3),
    _LcosLXStatusWLANStationEntryIfc_Type()
)
lcosLXStatusWLANStationEntryIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryIfc.setStatus("current")
_LcosLXStatusWLANStationEntryMACAddress_Type = MacAddress
_LcosLXStatusWLANStationEntryMACAddress_Object = MibTableColumn
lcosLXStatusWLANStationEntryMACAddress = _LcosLXStatusWLANStationEntryMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 4),
    _LcosLXStatusWLANStationEntryMACAddress_Type()
)
lcosLXStatusWLANStationEntryMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryMACAddress.setStatus("current")
_LcosLXStatusWLANStationEntryTxBytes_Type = Counter64
_LcosLXStatusWLANStationEntryTxBytes_Object = MibTableColumn
lcosLXStatusWLANStationEntryTxBytes = _LcosLXStatusWLANStationEntryTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 6),
    _LcosLXStatusWLANStationEntryTxBytes_Type()
)
lcosLXStatusWLANStationEntryTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryTxBytes.setStatus("current")
_LcosLXStatusWLANStationEntryRxBytes_Type = Counter64
_LcosLXStatusWLANStationEntryRxBytes_Object = MibTableColumn
lcosLXStatusWLANStationEntryRxBytes = _LcosLXStatusWLANStationEntryRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 7),
    _LcosLXStatusWLANStationEntryRxBytes_Type()
)
lcosLXStatusWLANStationEntryRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryRxBytes.setStatus("current")


class _LcosLXStatusWLANStationEntryIdentification_Type(OctetString):
    """Custom type lcosLXStatusWLANStationEntryIdentification based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_LcosLXStatusWLANStationEntryIdentification_Type.__name__ = "OctetString"
_LcosLXStatusWLANStationEntryIdentification_Object = MibTableColumn
lcosLXStatusWLANStationEntryIdentification = _LcosLXStatusWLANStationEntryIdentification_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 9),
    _LcosLXStatusWLANStationEntryIdentification_Type()
)
lcosLXStatusWLANStationEntryIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryIdentification.setStatus("current")


class _LcosLXStatusWLANStationEntryState_Type(Integer32):
    """Custom type lcosLXStatusWLANStationEntryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("eNone", 0),
          ("eAuthenticated", 2),
          ("eConnected", 3),
          ("eKeyHandshake", 8),
          ("eAssociated", 9),
          ("e1xNegotiation", 10))
    )


_LcosLXStatusWLANStationEntryState_Type.__name__ = "Integer32"
_LcosLXStatusWLANStationEntryState_Object = MibTableColumn
lcosLXStatusWLANStationEntryState = _LcosLXStatusWLANStationEntryState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 10),
    _LcosLXStatusWLANStationEntryState_Type()
)
lcosLXStatusWLANStationEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryState.setStatus("current")


class _LcosLXStatusWLANStationEntryInterface_Type(OctetString):
    """Custom type lcosLXStatusWLANStationEntryInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANStationEntryInterface_Type.__name__ = "OctetString"
_LcosLXStatusWLANStationEntryInterface_Object = MibTableColumn
lcosLXStatusWLANStationEntryInterface = _LcosLXStatusWLANStationEntryInterface_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 15),
    _LcosLXStatusWLANStationEntryInterface_Type()
)
lcosLXStatusWLANStationEntryInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryInterface.setStatus("current")


class _LcosLXStatusWLANStationEntryConnectTime_Type(Unsigned32):
    """Custom type lcosLXStatusWLANStationEntryConnectTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANStationEntryConnectTime_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANStationEntryConnectTime_Object = MibTableColumn
lcosLXStatusWLANStationEntryConnectTime = _LcosLXStatusWLANStationEntryConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 18),
    _LcosLXStatusWLANStationEntryConnectTime_Type()
)
lcosLXStatusWLANStationEntryConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryConnectTime.setStatus("current")


class _LcosLXStatusWLANStationEntryThroughput_Type(Unsigned32):
    """Custom type lcosLXStatusWLANStationEntryThroughput based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANStationEntryThroughput_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANStationEntryThroughput_Object = MibTableColumn
lcosLXStatusWLANStationEntryThroughput = _LcosLXStatusWLANStationEntryThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 20),
    _LcosLXStatusWLANStationEntryThroughput_Type()
)
lcosLXStatusWLANStationEntryThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryThroughput.setStatus("current")


class _LcosLXStatusWLANStationEntryPhySignal_Type(Unsigned32):
    """Custom type lcosLXStatusWLANStationEntryPhySignal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANStationEntryPhySignal_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANStationEntryPhySignal_Object = MibTableColumn
lcosLXStatusWLANStationEntryPhySignal = _LcosLXStatusWLANStationEntryPhySignal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 26),
    _LcosLXStatusWLANStationEntryPhySignal_Type()
)
lcosLXStatusWLANStationEntryPhySignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryPhySignal.setStatus("current")
_LcosLXStatusWLANStationEntryIPv4Address_Type = IpAddress
_LcosLXStatusWLANStationEntryIPv4Address_Object = MibTableColumn
lcosLXStatusWLANStationEntryIPv4Address = _LcosLXStatusWLANStationEntryIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 27),
    _LcosLXStatusWLANStationEntryIPv4Address_Type()
)
lcosLXStatusWLANStationEntryIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryIPv4Address.setStatus("current")


class _LcosLXStatusWLANStationEntryWPAVersion_Type(Integer32):
    """Custom type lcosLXStatusWLANStationEntryWPAVersion based on Integer32"""
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
        *(("eNone", 0),
          ("eWPA1", 1),
          ("eWPA2", 2),
          ("eWPA3", 3))
    )


_LcosLXStatusWLANStationEntryWPAVersion_Type.__name__ = "Integer32"
_LcosLXStatusWLANStationEntryWPAVersion_Object = MibTableColumn
lcosLXStatusWLANStationEntryWPAVersion = _LcosLXStatusWLANStationEntryWPAVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 33),
    _LcosLXStatusWLANStationEntryWPAVersion_Type()
)
lcosLXStatusWLANStationEntryWPAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryWPAVersion.setStatus("current")


class _LcosLXStatusWLANStationEntryVLANId_Type(Unsigned32):
    """Custom type lcosLXStatusWLANStationEntryVLANId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANStationEntryVLANId_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANStationEntryVLANId_Object = MibTableColumn
lcosLXStatusWLANStationEntryVLANId = _LcosLXStatusWLANStationEntryVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 38),
    _LcosLXStatusWLANStationEntryVLANId_Type()
)
lcosLXStatusWLANStationEntryVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryVLANId.setStatus("current")


class _LcosLXStatusWLANStationEntryUserName_Type(OctetString):
    """Custom type lcosLXStatusWLANStationEntryUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANStationEntryUserName_Type.__name__ = "OctetString"
_LcosLXStatusWLANStationEntryUserName_Object = MibTableColumn
lcosLXStatusWLANStationEntryUserName = _LcosLXStatusWLANStationEntryUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 39),
    _LcosLXStatusWLANStationEntryUserName_Type()
)
lcosLXStatusWLANStationEntryUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryUserName.setStatus("current")


class _LcosLXStatusWLANStationEntryIdleTimeout_Type(Unsigned32):
    """Custom type lcosLXStatusWLANStationEntryIdleTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANStationEntryIdleTimeout_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANStationEntryIdleTimeout_Object = MibTableColumn
lcosLXStatusWLANStationEntryIdleTimeout = _LcosLXStatusWLANStationEntryIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 43),
    _LcosLXStatusWLANStationEntryIdleTimeout_Type()
)
lcosLXStatusWLANStationEntryIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryIdleTimeout.setStatus("current")


class _LcosLXStatusWLANStationEntryEffTxRate_Type(Unsigned32):
    """Custom type lcosLXStatusWLANStationEntryEffTxRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANStationEntryEffTxRate_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANStationEntryEffTxRate_Object = MibTableColumn
lcosLXStatusWLANStationEntryEffTxRate = _LcosLXStatusWLANStationEntryEffTxRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 50),
    _LcosLXStatusWLANStationEntryEffTxRate_Type()
)
lcosLXStatusWLANStationEntryEffTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryEffTxRate.setStatus("current")


class _LcosLXStatusWLANStationEntryEffRxRate_Type(Unsigned32):
    """Custom type lcosLXStatusWLANStationEntryEffRxRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANStationEntryEffRxRate_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANStationEntryEffRxRate_Object = MibTableColumn
lcosLXStatusWLANStationEntryEffRxRate = _LcosLXStatusWLANStationEntryEffRxRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 51),
    _LcosLXStatusWLANStationEntryEffRxRate_Type()
)
lcosLXStatusWLANStationEntryEffRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryEffRxRate.setStatus("current")


class _LcosLXStatusWLANStationEntryFastRoaming_Type(Integer32):
    """Custom type lcosLXStatusWLANStationEntryFastRoaming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANStationEntryFastRoaming_Type.__name__ = "Integer32"
_LcosLXStatusWLANStationEntryFastRoaming_Object = MibTableColumn
lcosLXStatusWLANStationEntryFastRoaming = _LcosLXStatusWLANStationEntryFastRoaming_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 63),
    _LcosLXStatusWLANStationEntryFastRoaming_Type()
)
lcosLXStatusWLANStationEntryFastRoaming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryFastRoaming.setStatus("current")


class _LcosLXStatusWLANStationEntryWPA2KeyManagement_Type(Integer32):
    """Custom type lcosLXStatusWLANStationEntryWPA2KeyManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("eNone", 0),
          ("eStandard", 1),
          ("eFastRoaming", 2),
          ("eSHA256", 3),
          ("eSHA384", 4),
          ("eFastRoamingSHA384", 5),
          ("eSHA512", 6))
    )


_LcosLXStatusWLANStationEntryWPA2KeyManagement_Type.__name__ = "Integer32"
_LcosLXStatusWLANStationEntryWPA2KeyManagement_Object = MibTableColumn
lcosLXStatusWLANStationEntryWPA2KeyManagement = _LcosLXStatusWLANStationEntryWPA2KeyManagement_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 64),
    _LcosLXStatusWLANStationEntryWPA2KeyManagement_Type()
)
lcosLXStatusWLANStationEntryWPA2KeyManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryWPA2KeyManagement.setStatus("current")


class _LcosLXStatusWLANStationEntryChannelBandwidths_Type(OctetString):
    """Custom type lcosLXStatusWLANStationEntryChannelBandwidths based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_LcosLXStatusWLANStationEntryChannelBandwidths_Type.__name__ = "OctetString"
_LcosLXStatusWLANStationEntryChannelBandwidths_Object = MibTableColumn
lcosLXStatusWLANStationEntryChannelBandwidths = _LcosLXStatusWLANStationEntryChannelBandwidths_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 66),
    _LcosLXStatusWLANStationEntryChannelBandwidths_Type()
)
lcosLXStatusWLANStationEntryChannelBandwidths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryChannelBandwidths.setStatus("current")


class _LcosLXStatusWLANStationEntryOperationMode_Type(Integer32):
    """Custom type lcosLXStatusWLANStationEntryOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("eunknown", 0),
          ("e11b", 1),
          ("e11g", 2),
          ("e11a", 3),
          ("e11n", 4),
          ("e11ac", 5),
          ("e11ax", 6))
    )


_LcosLXStatusWLANStationEntryOperationMode_Type.__name__ = "Integer32"
_LcosLXStatusWLANStationEntryOperationMode_Object = MibTableColumn
lcosLXStatusWLANStationEntryOperationMode = _LcosLXStatusWLANStationEntryOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 71),
    _LcosLXStatusWLANStationEntryOperationMode_Type()
)
lcosLXStatusWLANStationEntryOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryOperationMode.setStatus("current")


class _LcosLXStatusWLANStationEntryDHCPHostname_Type(OctetString):
    """Custom type lcosLXStatusWLANStationEntryDHCPHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANStationEntryDHCPHostname_Type.__name__ = "OctetString"
_LcosLXStatusWLANStationEntryDHCPHostname_Object = MibTableColumn
lcosLXStatusWLANStationEntryDHCPHostname = _LcosLXStatusWLANStationEntryDHCPHostname_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 80),
    _LcosLXStatusWLANStationEntryDHCPHostname_Type()
)
lcosLXStatusWLANStationEntryDHCPHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryDHCPHostname.setStatus("current")


class _LcosLXStatusWLANStationEntryMaxSpatialStreams_Type(Unsigned32):
    """Custom type lcosLXStatusWLANStationEntryMaxSpatialStreams based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANStationEntryMaxSpatialStreams_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANStationEntryMaxSpatialStreams_Object = MibTableColumn
lcosLXStatusWLANStationEntryMaxSpatialStreams = _LcosLXStatusWLANStationEntryMaxSpatialStreams_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 83),
    _LcosLXStatusWLANStationEntryMaxSpatialStreams_Type()
)
lcosLXStatusWLANStationEntryMaxSpatialStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryMaxSpatialStreams.setStatus("current")


class _LcosLXStatusWLANStationEntryPhySignaldBm_Type(Integer32):
    """Custom type lcosLXStatusWLANStationEntryPhySignaldBm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_LcosLXStatusWLANStationEntryPhySignaldBm_Type.__name__ = "Integer32"
_LcosLXStatusWLANStationEntryPhySignaldBm_Object = MibTableColumn
lcosLXStatusWLANStationEntryPhySignaldBm = _LcosLXStatusWLANStationEntryPhySignaldBm_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 97),
    _LcosLXStatusWLANStationEntryPhySignaldBm_Type()
)
lcosLXStatusWLANStationEntryPhySignaldBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryPhySignaldBm.setStatus("current")


class _LcosLXStatusWLANStationEntryNetworkName_Type(OctetString):
    """Custom type lcosLXStatusWLANStationEntryNetworkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANStationEntryNetworkName_Type.__name__ = "OctetString"
_LcosLXStatusWLANStationEntryNetworkName_Object = MibTableColumn
lcosLXStatusWLANStationEntryNetworkName = _LcosLXStatusWLANStationEntryNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 98),
    _LcosLXStatusWLANStationEntryNetworkName_Type()
)
lcosLXStatusWLANStationEntryNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntryNetworkName.setStatus("current")


class _LcosLXStatusWLANStationEntrySSID_Type(OctetString):
    """Custom type lcosLXStatusWLANStationEntrySSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANStationEntrySSID_Type.__name__ = "OctetString"
_LcosLXStatusWLANStationEntrySSID_Object = MibTableColumn
lcosLXStatusWLANStationEntrySSID = _LcosLXStatusWLANStationEntrySSID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 32, 1, 99),
    _LcosLXStatusWLANStationEntrySSID_Type()
)
lcosLXStatusWLANStationEntrySSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANStationEntrySSID.setStatus("current")
_LcosLXStatusWLANIAPPTable_Object = MibTable
lcosLXStatusWLANIAPPTable = _LcosLXStatusWLANIAPPTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 38)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANIAPPTable.setStatus("current")
_LcosLXStatusWLANIAPPEntry_Object = MibTableRow
lcosLXStatusWLANIAPPEntry = _LcosLXStatusWLANIAPPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 38, 1)
)
lcosLXStatusWLANIAPPEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANIAPPEntryIPAddress"),
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANIAPPEntryBSSID"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANIAPPEntry.setStatus("current")
_LcosLXStatusWLANIAPPEntryIPAddress_Type = IpAddress
_LcosLXStatusWLANIAPPEntryIPAddress_Object = MibTableColumn
lcosLXStatusWLANIAPPEntryIPAddress = _LcosLXStatusWLANIAPPEntryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 38, 1, 1),
    _LcosLXStatusWLANIAPPEntryIPAddress_Type()
)
lcosLXStatusWLANIAPPEntryIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANIAPPEntryIPAddress.setStatus("current")


class _LcosLXStatusWLANIAPPEntryBSSID_Type(OctetString):
    """Custom type lcosLXStatusWLANIAPPEntryBSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_LcosLXStatusWLANIAPPEntryBSSID_Type.__name__ = "OctetString"
_LcosLXStatusWLANIAPPEntryBSSID_Object = MibTableColumn
lcosLXStatusWLANIAPPEntryBSSID = _LcosLXStatusWLANIAPPEntryBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 38, 1, 2),
    _LcosLXStatusWLANIAPPEntryBSSID_Type()
)
lcosLXStatusWLANIAPPEntryBSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANIAPPEntryBSSID.setStatus("current")


class _LcosLXStatusWLANIAPPEntrySSID_Type(OctetString):
    """Custom type lcosLXStatusWLANIAPPEntrySSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANIAPPEntrySSID_Type.__name__ = "OctetString"
_LcosLXStatusWLANIAPPEntrySSID_Object = MibTableColumn
lcosLXStatusWLANIAPPEntrySSID = _LcosLXStatusWLANIAPPEntrySSID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 38, 1, 7),
    _LcosLXStatusWLANIAPPEntrySSID_Type()
)
lcosLXStatusWLANIAPPEntrySSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANIAPPEntrySSID.setStatus("current")


class _LcosLXStatusWLANIAPPEntryRadioChannel_Type(Unsigned32):
    """Custom type lcosLXStatusWLANIAPPEntryRadioChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANIAPPEntryRadioChannel_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANIAPPEntryRadioChannel_Object = MibTableColumn
lcosLXStatusWLANIAPPEntryRadioChannel = _LcosLXStatusWLANIAPPEntryRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 38, 1, 8),
    _LcosLXStatusWLANIAPPEntryRadioChannel_Type()
)
lcosLXStatusWLANIAPPEntryRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANIAPPEntryRadioChannel.setStatus("current")


class _LcosLXStatusWLANIAPPEntryDomainID_Type(OctetString):
    """Custom type lcosLXStatusWLANIAPPEntryDomainID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANIAPPEntryDomainID_Type.__name__ = "OctetString"
_LcosLXStatusWLANIAPPEntryDomainID_Object = MibTableColumn
lcosLXStatusWLANIAPPEntryDomainID = _LcosLXStatusWLANIAPPEntryDomainID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 38, 1, 9),
    _LcosLXStatusWLANIAPPEntryDomainID_Type()
)
lcosLXStatusWLANIAPPEntryDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANIAPPEntryDomainID.setStatus("current")


class _LcosLXStatusWLANIAPPEntryLoad_Type(OctetString):
    """Custom type lcosLXStatusWLANIAPPEntryLoad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_LcosLXStatusWLANIAPPEntryLoad_Type.__name__ = "OctetString"
_LcosLXStatusWLANIAPPEntryLoad_Object = MibTableColumn
lcosLXStatusWLANIAPPEntryLoad = _LcosLXStatusWLANIAPPEntryLoad_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 38, 1, 10),
    _LcosLXStatusWLANIAPPEntryLoad_Type()
)
lcosLXStatusWLANIAPPEntryLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANIAPPEntryLoad.setStatus("current")
_LcosLXStatusWLANChannelScanResults_Object = MibTable
lcosLXStatusWLANChannelScanResults = _LcosLXStatusWLANChannelScanResults_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 42)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelScanResults.setStatus("current")
_LcosLXStatusWLANChannelScanResultsEntry_Object = MibTableRow
lcosLXStatusWLANChannelScanResultsEntry = _LcosLXStatusWLANChannelScanResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 42, 1)
)
lcosLXStatusWLANChannelScanResultsEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANChannelScanResultsEntryRadioChannel"),
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANChannelScanResultsEntryInterface"),
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANChannelScanResultsEntryRadioBand"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelScanResultsEntry.setStatus("current")


class _LcosLXStatusWLANChannelScanResultsEntryRadioChannel_Type(Unsigned32):
    """Custom type lcosLXStatusWLANChannelScanResultsEntryRadioChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANChannelScanResultsEntryRadioChannel_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANChannelScanResultsEntryRadioChannel_Object = MibTableColumn
lcosLXStatusWLANChannelScanResultsEntryRadioChannel = _LcosLXStatusWLANChannelScanResultsEntryRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 42, 1, 1),
    _LcosLXStatusWLANChannelScanResultsEntryRadioChannel_Type()
)
lcosLXStatusWLANChannelScanResultsEntryRadioChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelScanResultsEntryRadioChannel.setStatus("current")


class _LcosLXStatusWLANChannelScanResultsEntryInterface_Type(OctetString):
    """Custom type lcosLXStatusWLANChannelScanResultsEntryInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LcosLXStatusWLANChannelScanResultsEntryInterface_Type.__name__ = "OctetString"
_LcosLXStatusWLANChannelScanResultsEntryInterface_Object = MibTableColumn
lcosLXStatusWLANChannelScanResultsEntryInterface = _LcosLXStatusWLANChannelScanResultsEntryInterface_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 42, 1, 2),
    _LcosLXStatusWLANChannelScanResultsEntryInterface_Type()
)
lcosLXStatusWLANChannelScanResultsEntryInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelScanResultsEntryInterface.setStatus("current")


class _LcosLXStatusWLANChannelScanResultsEntryRadioBand_Type(Integer32):
    """Custom type lcosLXStatusWLANChannelScanResultsEntryRadioBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e24GHz", 1),
          ("e5GHz", 2))
    )


_LcosLXStatusWLANChannelScanResultsEntryRadioBand_Type.__name__ = "Integer32"
_LcosLXStatusWLANChannelScanResultsEntryRadioBand_Object = MibTableColumn
lcosLXStatusWLANChannelScanResultsEntryRadioBand = _LcosLXStatusWLANChannelScanResultsEntryRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 42, 1, 9),
    _LcosLXStatusWLANChannelScanResultsEntryRadioBand_Type()
)
lcosLXStatusWLANChannelScanResultsEntryRadioBand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelScanResultsEntryRadioBand.setStatus("current")


class _LcosLXStatusWLANChannelScanResultsEntryDFSState_Type(Integer32):
    """Custom type lcosLXStatusWLANChannelScanResultsEntryDFSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eunknown", 0),
          ("eclear", 1),
          ("eblocked", 2))
    )


_LcosLXStatusWLANChannelScanResultsEntryDFSState_Type.__name__ = "Integer32"
_LcosLXStatusWLANChannelScanResultsEntryDFSState_Object = MibTableColumn
lcosLXStatusWLANChannelScanResultsEntryDFSState = _LcosLXStatusWLANChannelScanResultsEntryDFSState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 42, 1, 12),
    _LcosLXStatusWLANChannelScanResultsEntryDFSState_Type()
)
lcosLXStatusWLANChannelScanResultsEntryDFSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelScanResultsEntryDFSState.setStatus("current")


class _LcosLXStatusWLANChannelScanResultsEntryDFSScanAge_Type(Unsigned32):
    """Custom type lcosLXStatusWLANChannelScanResultsEntryDFSScanAge based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANChannelScanResultsEntryDFSScanAge_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANChannelScanResultsEntryDFSScanAge_Object = MibTableColumn
lcosLXStatusWLANChannelScanResultsEntryDFSScanAge = _LcosLXStatusWLANChannelScanResultsEntryDFSScanAge_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 42, 1, 13),
    _LcosLXStatusWLANChannelScanResultsEntryDFSScanAge_Type()
)
lcosLXStatusWLANChannelScanResultsEntryDFSScanAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelScanResultsEntryDFSScanAge.setStatus("current")


class _LcosLXStatusWLANChannelScanResultsEntryChannelBandwidth_Type(Integer32):
    """Custom type lcosLXStatusWLANChannelScanResultsEntryChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e20MHz", 0),
          ("e40MHz", 1),
          ("e80MHz", 2),
          ("e160MHz", 3),
          ("eAuto", 255))
    )


_LcosLXStatusWLANChannelScanResultsEntryChannelBandwidth_Type.__name__ = "Integer32"
_LcosLXStatusWLANChannelScanResultsEntryChannelBandwidth_Object = MibTableColumn
lcosLXStatusWLANChannelScanResultsEntryChannelBandwidth = _LcosLXStatusWLANChannelScanResultsEntryChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 42, 1, 23),
    _LcosLXStatusWLANChannelScanResultsEntryChannelBandwidth_Type()
)
lcosLXStatusWLANChannelScanResultsEntryChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelScanResultsEntryChannelBandwidth.setStatus("current")
_LcosLXStatusWLANInterfaces_Object = MibTable
lcosLXStatusWLANInterfaces = _LcosLXStatusWLANInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 51)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANInterfaces.setStatus("current")
_LcosLXStatusWLANInterfacesEntry_Object = MibTableRow
lcosLXStatusWLANInterfacesEntry = _LcosLXStatusWLANInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 51, 1)
)
lcosLXStatusWLANInterfacesEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANInterfacesEntryNetworkName"),
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANInterfacesEntryRadioBand"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANInterfacesEntry.setStatus("current")


class _LcosLXStatusWLANInterfacesEntryNetworkName_Type(OctetString):
    """Custom type lcosLXStatusWLANInterfacesEntryNetworkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANInterfacesEntryNetworkName_Type.__name__ = "OctetString"
_LcosLXStatusWLANInterfacesEntryNetworkName_Object = MibTableColumn
lcosLXStatusWLANInterfacesEntryNetworkName = _LcosLXStatusWLANInterfacesEntryNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 51, 1, 1),
    _LcosLXStatusWLANInterfacesEntryNetworkName_Type()
)
lcosLXStatusWLANInterfacesEntryNetworkName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANInterfacesEntryNetworkName.setStatus("current")


class _LcosLXStatusWLANInterfacesEntrySSID_Type(OctetString):
    """Custom type lcosLXStatusWLANInterfacesEntrySSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANInterfacesEntrySSID_Type.__name__ = "OctetString"
_LcosLXStatusWLANInterfacesEntrySSID_Object = MibTableColumn
lcosLXStatusWLANInterfacesEntrySSID = _LcosLXStatusWLANInterfacesEntrySSID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 51, 1, 2),
    _LcosLXStatusWLANInterfacesEntrySSID_Type()
)
lcosLXStatusWLANInterfacesEntrySSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANInterfacesEntrySSID.setStatus("current")


class _LcosLXStatusWLANInterfacesEntryRadioBand_Type(Integer32):
    """Custom type lcosLXStatusWLANInterfacesEntryRadioBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e24GHz", 1),
          ("e5GHz", 2))
    )


_LcosLXStatusWLANInterfacesEntryRadioBand_Type.__name__ = "Integer32"
_LcosLXStatusWLANInterfacesEntryRadioBand_Object = MibTableColumn
lcosLXStatusWLANInterfacesEntryRadioBand = _LcosLXStatusWLANInterfacesEntryRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 51, 1, 3),
    _LcosLXStatusWLANInterfacesEntryRadioBand_Type()
)
lcosLXStatusWLANInterfacesEntryRadioBand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANInterfacesEntryRadioBand.setStatus("current")


class _LcosLXStatusWLANInterfacesEntryWPAPSKNumSuccess_Type(Unsigned32):
    """Custom type lcosLXStatusWLANInterfacesEntryWPAPSKNumSuccess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANInterfacesEntryWPAPSKNumSuccess_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANInterfacesEntryWPAPSKNumSuccess_Object = MibTableColumn
lcosLXStatusWLANInterfacesEntryWPAPSKNumSuccess = _LcosLXStatusWLANInterfacesEntryWPAPSKNumSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 51, 1, 4),
    _LcosLXStatusWLANInterfacesEntryWPAPSKNumSuccess_Type()
)
lcosLXStatusWLANInterfacesEntryWPAPSKNumSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANInterfacesEntryWPAPSKNumSuccess.setStatus("current")


class _LcosLXStatusWLANInterfacesEntryWPAPSKNumFailures_Type(Unsigned32):
    """Custom type lcosLXStatusWLANInterfacesEntryWPAPSKNumFailures based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANInterfacesEntryWPAPSKNumFailures_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANInterfacesEntryWPAPSKNumFailures_Object = MibTableColumn
lcosLXStatusWLANInterfacesEntryWPAPSKNumFailures = _LcosLXStatusWLANInterfacesEntryWPAPSKNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 51, 1, 5),
    _LcosLXStatusWLANInterfacesEntryWPAPSKNumFailures_Type()
)
lcosLXStatusWLANInterfacesEntryWPAPSKNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANInterfacesEntryWPAPSKNumFailures.setStatus("current")


class _LcosLXStatusWLANInterfacesEntryWPAPSKNumWrongPassphrase_Type(Unsigned32):
    """Custom type lcosLXStatusWLANInterfacesEntryWPAPSKNumWrongPassphrase based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANInterfacesEntryWPAPSKNumWrongPassphrase_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANInterfacesEntryWPAPSKNumWrongPassphrase_Object = MibTableColumn
lcosLXStatusWLANInterfacesEntryWPAPSKNumWrongPassphrase = _LcosLXStatusWLANInterfacesEntryWPAPSKNumWrongPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 51, 1, 6),
    _LcosLXStatusWLANInterfacesEntryWPAPSKNumWrongPassphrase_Type()
)
lcosLXStatusWLANInterfacesEntryWPAPSKNumWrongPassphrase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANInterfacesEntryWPAPSKNumWrongPassphrase.setStatus("current")


class _LcosLXStatusWLANInterfacesEntryIfc_Type(OctetString):
    """Custom type lcosLXStatusWLANInterfacesEntryIfc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LcosLXStatusWLANInterfacesEntryIfc_Type.__name__ = "OctetString"
_LcosLXStatusWLANInterfacesEntryIfc_Object = MibTableColumn
lcosLXStatusWLANInterfacesEntryIfc = _LcosLXStatusWLANInterfacesEntryIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 51, 1, 7),
    _LcosLXStatusWLANInterfacesEntryIfc_Type()
)
lcosLXStatusWLANInterfacesEntryIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANInterfacesEntryIfc.setStatus("current")
_LcosLXStatusWLANRadios_Object = MibTable
lcosLXStatusWLANRadios = _LcosLXStatusWLANRadios_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadios.setStatus("current")
_LcosLXStatusWLANRadiosEntry_Object = MibTableRow
lcosLXStatusWLANRadiosEntry = _LcosLXStatusWLANRadiosEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1)
)
lcosLXStatusWLANRadiosEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANRadiosEntryIfc"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntry.setStatus("current")


class _LcosLXStatusWLANRadiosEntryIfc_Type(OctetString):
    """Custom type lcosLXStatusWLANRadiosEntryIfc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LcosLXStatusWLANRadiosEntryIfc_Type.__name__ = "OctetString"
_LcosLXStatusWLANRadiosEntryIfc_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryIfc = _LcosLXStatusWLANRadiosEntryIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 1),
    _LcosLXStatusWLANRadiosEntryIfc_Type()
)
lcosLXStatusWLANRadiosEntryIfc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryIfc.setStatus("current")


class _LcosLXStatusWLANRadiosEntryRadioBand_Type(Integer32):
    """Custom type lcosLXStatusWLANRadiosEntryRadioBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e24GHz", 1),
          ("e5GHz", 2))
    )


_LcosLXStatusWLANRadiosEntryRadioBand_Type.__name__ = "Integer32"
_LcosLXStatusWLANRadiosEntryRadioBand_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryRadioBand = _LcosLXStatusWLANRadiosEntryRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 2),
    _LcosLXStatusWLANRadiosEntryRadioBand_Type()
)
lcosLXStatusWLANRadiosEntryRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryRadioBand.setStatus("current")


class _LcosLXStatusWLANRadiosEntryRadioChannel_Type(Unsigned32):
    """Custom type lcosLXStatusWLANRadiosEntryRadioChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANRadiosEntryRadioChannel_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANRadiosEntryRadioChannel_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryRadioChannel = _LcosLXStatusWLANRadiosEntryRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 3),
    _LcosLXStatusWLANRadiosEntryRadioChannel_Type()
)
lcosLXStatusWLANRadiosEntryRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryRadioChannel.setStatus("current")


class _LcosLXStatusWLANRadiosEntryNoiseFloor_Type(Integer32):
    """Custom type lcosLXStatusWLANRadiosEntryNoiseFloor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_LcosLXStatusWLANRadiosEntryNoiseFloor_Type.__name__ = "Integer32"
_LcosLXStatusWLANRadiosEntryNoiseFloor_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryNoiseFloor = _LcosLXStatusWLANRadiosEntryNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 4),
    _LcosLXStatusWLANRadiosEntryNoiseFloor_Type()
)
lcosLXStatusWLANRadiosEntryNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryNoiseFloor.setStatus("current")


class _LcosLXStatusWLANRadiosEntryNoiseLevel_Type(Integer32):
    """Custom type lcosLXStatusWLANRadiosEntryNoiseLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_LcosLXStatusWLANRadiosEntryNoiseLevel_Type.__name__ = "Integer32"
_LcosLXStatusWLANRadiosEntryNoiseLevel_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryNoiseLevel = _LcosLXStatusWLANRadiosEntryNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 5),
    _LcosLXStatusWLANRadiosEntryNoiseLevel_Type()
)
lcosLXStatusWLANRadiosEntryNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryNoiseLevel.setStatus("current")


class _LcosLXStatusWLANRadiosEntryModemLoad_Type(Unsigned32):
    """Custom type lcosLXStatusWLANRadiosEntryModemLoad based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANRadiosEntryModemLoad_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANRadiosEntryModemLoad_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryModemLoad = _LcosLXStatusWLANRadiosEntryModemLoad_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 6),
    _LcosLXStatusWLANRadiosEntryModemLoad_Type()
)
lcosLXStatusWLANRadiosEntryModemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryModemLoad.setStatus("current")


class _LcosLXStatusWLANRadiosEntryTransmitPower_Type(Integer32):
    """Custom type lcosLXStatusWLANRadiosEntryTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_LcosLXStatusWLANRadiosEntryTransmitPower_Type.__name__ = "Integer32"
_LcosLXStatusWLANRadiosEntryTransmitPower_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryTransmitPower = _LcosLXStatusWLANRadiosEntryTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 7),
    _LcosLXStatusWLANRadiosEntryTransmitPower_Type()
)
lcosLXStatusWLANRadiosEntryTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryTransmitPower.setStatus("current")


class _LcosLXStatusWLANRadiosEntryEIRP_Type(Integer32):
    """Custom type lcosLXStatusWLANRadiosEntryEIRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_LcosLXStatusWLANRadiosEntryEIRP_Type.__name__ = "Integer32"
_LcosLXStatusWLANRadiosEntryEIRP_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryEIRP = _LcosLXStatusWLANRadiosEntryEIRP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 8),
    _LcosLXStatusWLANRadiosEntryEIRP_Type()
)
lcosLXStatusWLANRadiosEntryEIRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryEIRP.setStatus("current")


class _LcosLXStatusWLANRadiosEntryMode_Type(Integer32):
    """Custom type lcosLXStatusWLANRadiosEntryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              7,
              8,
              9,
              10,
              256,
              259,
              263,
              264,
              265,
              266)
        )
    )
    namedValues = NamedValues(
        *(("e11bgmixed", 0),
          ("e11gonly", 1),
          ("e11bonly", 2),
          ("e11bgnmixed", 5),
          ("e11gnmixed", 7),
          ("e11nonly", 8),
          ("e11bgnaxmixed", 9),
          ("e11gnaxmixed", 10),
          ("e11aonly", 256),
          ("e11anmixed", 259),
          ("e11anacmixed", 263),
          ("e11nacmixed", 264),
          ("e11aconly", 265),
          ("e11anacaxmixed", 266))
    )


_LcosLXStatusWLANRadiosEntryMode_Type.__name__ = "Integer32"
_LcosLXStatusWLANRadiosEntryMode_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryMode = _LcosLXStatusWLANRadiosEntryMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 14),
    _LcosLXStatusWLANRadiosEntryMode_Type()
)
lcosLXStatusWLANRadiosEntryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryMode.setStatus("current")


class _LcosLXStatusWLANRadiosEntryChannelBandwidth_Type(Integer32):
    """Custom type lcosLXStatusWLANRadiosEntryChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e20MHz", 0),
          ("e40MHz", 1),
          ("e80MHz", 2),
          ("e160MHz", 3),
          ("eAuto", 255))
    )


_LcosLXStatusWLANRadiosEntryChannelBandwidth_Type.__name__ = "Integer32"
_LcosLXStatusWLANRadiosEntryChannelBandwidth_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryChannelBandwidth = _LcosLXStatusWLANRadiosEntryChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 19),
    _LcosLXStatusWLANRadiosEntryChannelBandwidth_Type()
)
lcosLXStatusWLANRadiosEntryChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryChannelBandwidth.setStatus("current")


class _LcosLXStatusWLANRadiosEntryRxErrorRatio_Type(Unsigned32):
    """Custom type lcosLXStatusWLANRadiosEntryRxErrorRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANRadiosEntryRxErrorRatio_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANRadiosEntryRxErrorRatio_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryRxErrorRatio = _LcosLXStatusWLANRadiosEntryRxErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 20),
    _LcosLXStatusWLANRadiosEntryRxErrorRatio_Type()
)
lcosLXStatusWLANRadiosEntryRxErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryRxErrorRatio.setStatus("current")


class _LcosLXStatusWLANRadiosEntryTxErrorRatio_Type(Unsigned32):
    """Custom type lcosLXStatusWLANRadiosEntryTxErrorRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANRadiosEntryTxErrorRatio_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANRadiosEntryTxErrorRatio_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryTxErrorRatio = _LcosLXStatusWLANRadiosEntryTxErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 21),
    _LcosLXStatusWLANRadiosEntryTxErrorRatio_Type()
)
lcosLXStatusWLANRadiosEntryTxErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryTxErrorRatio.setStatus("current")
_LcosLXStatusWLANRadiosEntryRxBytes_Type = Counter64
_LcosLXStatusWLANRadiosEntryRxBytes_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryRxBytes = _LcosLXStatusWLANRadiosEntryRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 22),
    _LcosLXStatusWLANRadiosEntryRxBytes_Type()
)
lcosLXStatusWLANRadiosEntryRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryRxBytes.setStatus("current")
_LcosLXStatusWLANRadiosEntryTxBytes_Type = Counter64
_LcosLXStatusWLANRadiosEntryTxBytes_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryTxBytes = _LcosLXStatusWLANRadiosEntryTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 23),
    _LcosLXStatusWLANRadiosEntryTxBytes_Type()
)
lcosLXStatusWLANRadiosEntryTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryTxBytes.setStatus("current")


class _LcosLXStatusWLANRadiosEntryModemLoadMin_Type(Unsigned32):
    """Custom type lcosLXStatusWLANRadiosEntryModemLoadMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANRadiosEntryModemLoadMin_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANRadiosEntryModemLoadMin_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryModemLoadMin = _LcosLXStatusWLANRadiosEntryModemLoadMin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 40),
    _LcosLXStatusWLANRadiosEntryModemLoadMin_Type()
)
lcosLXStatusWLANRadiosEntryModemLoadMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryModemLoadMin.setStatus("current")


class _LcosLXStatusWLANRadiosEntryModemLoadMax_Type(Unsigned32):
    """Custom type lcosLXStatusWLANRadiosEntryModemLoadMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANRadiosEntryModemLoadMax_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANRadiosEntryModemLoadMax_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryModemLoadMax = _LcosLXStatusWLANRadiosEntryModemLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 41),
    _LcosLXStatusWLANRadiosEntryModemLoadMax_Type()
)
lcosLXStatusWLANRadiosEntryModemLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryModemLoadMax.setStatus("current")


class _LcosLXStatusWLANRadiosEntryModemLoadAverage_Type(Unsigned32):
    """Custom type lcosLXStatusWLANRadiosEntryModemLoadAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANRadiosEntryModemLoadAverage_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANRadiosEntryModemLoadAverage_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryModemLoadAverage = _LcosLXStatusWLANRadiosEntryModemLoadAverage_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 42),
    _LcosLXStatusWLANRadiosEntryModemLoadAverage_Type()
)
lcosLXStatusWLANRadiosEntryModemLoadAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryModemLoadAverage.setStatus("current")


class _LcosLXStatusWLANRadiosEntryTemperatureDegrees_Type(Unsigned32):
    """Custom type lcosLXStatusWLANRadiosEntryTemperatureDegrees based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANRadiosEntryTemperatureDegrees_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANRadiosEntryTemperatureDegrees_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryTemperatureDegrees = _LcosLXStatusWLANRadiosEntryTemperatureDegrees_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 50),
    _LcosLXStatusWLANRadiosEntryTemperatureDegrees_Type()
)
lcosLXStatusWLANRadiosEntryTemperatureDegrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryTemperatureDegrees.setStatus("current")


class _LcosLXStatusWLANRadiosEntryAllChannelsBlocked_Type(Integer32):
    """Custom type lcosLXStatusWLANRadiosEntryAllChannelsBlocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANRadiosEntryAllChannelsBlocked_Type.__name__ = "Integer32"
_LcosLXStatusWLANRadiosEntryAllChannelsBlocked_Object = MibTableColumn
lcosLXStatusWLANRadiosEntryAllChannelsBlocked = _LcosLXStatusWLANRadiosEntryAllChannelsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 57, 1, 51),
    _LcosLXStatusWLANRadiosEntryAllChannelsBlocked_Type()
)
lcosLXStatusWLANRadiosEntryAllChannelsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANRadiosEntryAllChannelsBlocked.setStatus("current")
_LcosLXStatusWLANEnvironmentScanResults_Object = MibTable
lcosLXStatusWLANEnvironmentScanResults = _LcosLXStatusWLANEnvironmentScanResults_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 69)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANEnvironmentScanResults.setStatus("current")
_LcosLXStatusWLANEnvironmentScanResultsEntry_Object = MibTableRow
lcosLXStatusWLANEnvironmentScanResultsEntry = _LcosLXStatusWLANEnvironmentScanResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 69, 1)
)
lcosLXStatusWLANEnvironmentScanResultsEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANEnvironmentScanResultsEntryBSSID"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANEnvironmentScanResultsEntry.setStatus("current")


class _LcosLXStatusWLANEnvironmentScanResultsEntryBSSID_Type(OctetString):
    """Custom type lcosLXStatusWLANEnvironmentScanResultsEntryBSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_LcosLXStatusWLANEnvironmentScanResultsEntryBSSID_Type.__name__ = "OctetString"
_LcosLXStatusWLANEnvironmentScanResultsEntryBSSID_Object = MibTableColumn
lcosLXStatusWLANEnvironmentScanResultsEntryBSSID = _LcosLXStatusWLANEnvironmentScanResultsEntryBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 69, 1, 1),
    _LcosLXStatusWLANEnvironmentScanResultsEntryBSSID_Type()
)
lcosLXStatusWLANEnvironmentScanResultsEntryBSSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANEnvironmentScanResultsEntryBSSID.setStatus("current")


class _LcosLXStatusWLANEnvironmentScanResultsEntrySSID_Type(OctetString):
    """Custom type lcosLXStatusWLANEnvironmentScanResultsEntrySSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANEnvironmentScanResultsEntrySSID_Type.__name__ = "OctetString"
_LcosLXStatusWLANEnvironmentScanResultsEntrySSID_Object = MibTableColumn
lcosLXStatusWLANEnvironmentScanResultsEntrySSID = _LcosLXStatusWLANEnvironmentScanResultsEntrySSID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 69, 1, 2),
    _LcosLXStatusWLANEnvironmentScanResultsEntrySSID_Type()
)
lcosLXStatusWLANEnvironmentScanResultsEntrySSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANEnvironmentScanResultsEntrySSID.setStatus("current")


class _LcosLXStatusWLANEnvironmentScanResultsEntryIfc_Type(OctetString):
    """Custom type lcosLXStatusWLANEnvironmentScanResultsEntryIfc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LcosLXStatusWLANEnvironmentScanResultsEntryIfc_Type.__name__ = "OctetString"
_LcosLXStatusWLANEnvironmentScanResultsEntryIfc_Object = MibTableColumn
lcosLXStatusWLANEnvironmentScanResultsEntryIfc = _LcosLXStatusWLANEnvironmentScanResultsEntryIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 69, 1, 3),
    _LcosLXStatusWLANEnvironmentScanResultsEntryIfc_Type()
)
lcosLXStatusWLANEnvironmentScanResultsEntryIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANEnvironmentScanResultsEntryIfc.setStatus("current")


class _LcosLXStatusWLANEnvironmentScanResultsEntryRadioChannel_Type(Unsigned32):
    """Custom type lcosLXStatusWLANEnvironmentScanResultsEntryRadioChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANEnvironmentScanResultsEntryRadioChannel_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANEnvironmentScanResultsEntryRadioChannel_Object = MibTableColumn
lcosLXStatusWLANEnvironmentScanResultsEntryRadioChannel = _LcosLXStatusWLANEnvironmentScanResultsEntryRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 69, 1, 8),
    _LcosLXStatusWLANEnvironmentScanResultsEntryRadioChannel_Type()
)
lcosLXStatusWLANEnvironmentScanResultsEntryRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANEnvironmentScanResultsEntryRadioChannel.setStatus("current")


class _LcosLXStatusWLANEnvironmentScanResultsEntryRadioBand_Type(Integer32):
    """Custom type lcosLXStatusWLANEnvironmentScanResultsEntryRadioBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e24GHz", 1),
          ("e5GHz", 2))
    )


_LcosLXStatusWLANEnvironmentScanResultsEntryRadioBand_Type.__name__ = "Integer32"
_LcosLXStatusWLANEnvironmentScanResultsEntryRadioBand_Object = MibTableColumn
lcosLXStatusWLANEnvironmentScanResultsEntryRadioBand = _LcosLXStatusWLANEnvironmentScanResultsEntryRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 69, 1, 16),
    _LcosLXStatusWLANEnvironmentScanResultsEntryRadioBand_Type()
)
lcosLXStatusWLANEnvironmentScanResultsEntryRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANEnvironmentScanResultsEntryRadioBand.setStatus("current")


class _LcosLXStatusWLANEnvironmentScanResultsEntrySignalLevel_Type(Integer32):
    """Custom type lcosLXStatusWLANEnvironmentScanResultsEntrySignalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_LcosLXStatusWLANEnvironmentScanResultsEntrySignalLevel_Type.__name__ = "Integer32"
_LcosLXStatusWLANEnvironmentScanResultsEntrySignalLevel_Object = MibTableColumn
lcosLXStatusWLANEnvironmentScanResultsEntrySignalLevel = _LcosLXStatusWLANEnvironmentScanResultsEntrySignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 69, 1, 26),
    _LcosLXStatusWLANEnvironmentScanResultsEntrySignalLevel_Type()
)
lcosLXStatusWLANEnvironmentScanResultsEntrySignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANEnvironmentScanResultsEntrySignalLevel.setStatus("current")


class _LcosLXStatusWLANEnvironmentScanResultsEntrySignalLevelPercent_Type(Unsigned32):
    """Custom type lcosLXStatusWLANEnvironmentScanResultsEntrySignalLevelPercent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANEnvironmentScanResultsEntrySignalLevelPercent_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANEnvironmentScanResultsEntrySignalLevelPercent_Object = MibTableColumn
lcosLXStatusWLANEnvironmentScanResultsEntrySignalLevelPercent = _LcosLXStatusWLANEnvironmentScanResultsEntrySignalLevelPercent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 69, 1, 27),
    _LcosLXStatusWLANEnvironmentScanResultsEntrySignalLevelPercent_Type()
)
lcosLXStatusWLANEnvironmentScanResultsEntrySignalLevelPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANEnvironmentScanResultsEntrySignalLevelPercent.setStatus("current")


class _LcosLXStatusWLANEnvironmentScanResultsEntryChannelBandwidth_Type(Unsigned32):
    """Custom type lcosLXStatusWLANEnvironmentScanResultsEntryChannelBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANEnvironmentScanResultsEntryChannelBandwidth_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANEnvironmentScanResultsEntryChannelBandwidth_Object = MibTableColumn
lcosLXStatusWLANEnvironmentScanResultsEntryChannelBandwidth = _LcosLXStatusWLANEnvironmentScanResultsEntryChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 69, 1, 45),
    _LcosLXStatusWLANEnvironmentScanResultsEntryChannelBandwidth_Type()
)
lcosLXStatusWLANEnvironmentScanResultsEntryChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANEnvironmentScanResultsEntryChannelBandwidth.setStatus("current")
_LcosLXStatusWLANChannelsAllowedByRegulatory_Object = MibTable
lcosLXStatusWLANChannelsAllowedByRegulatory = _LcosLXStatusWLANChannelsAllowedByRegulatory_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 99)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelsAllowedByRegulatory.setStatus("current")
_LcosLXStatusWLANChannelsAllowedByRegulatoryEntry_Object = MibTableRow
lcosLXStatusWLANChannelsAllowedByRegulatoryEntry = _LcosLXStatusWLANChannelsAllowedByRegulatoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 99, 1)
)
lcosLXStatusWLANChannelsAllowedByRegulatoryEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANChannelsAllowedByRegulatoryEntryChannel"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelsAllowedByRegulatoryEntry.setStatus("current")


class _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryChannel_Type(Unsigned32):
    """Custom type lcosLXStatusWLANChannelsAllowedByRegulatoryEntryChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANChannelsAllowedByRegulatoryEntryChannel_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANChannelsAllowedByRegulatoryEntryChannel_Object = MibTableColumn
lcosLXStatusWLANChannelsAllowedByRegulatoryEntryChannel = _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryChannel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 99, 1, 1),
    _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryChannel_Type()
)
lcosLXStatusWLANChannelsAllowedByRegulatoryEntryChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelsAllowedByRegulatoryEntryChannel.setStatus("current")


class _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryOutdoor_Type(Integer32):
    """Custom type lcosLXStatusWLANChannelsAllowedByRegulatoryEntryOutdoor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANChannelsAllowedByRegulatoryEntryOutdoor_Type.__name__ = "Integer32"
_LcosLXStatusWLANChannelsAllowedByRegulatoryEntryOutdoor_Object = MibTableColumn
lcosLXStatusWLANChannelsAllowedByRegulatoryEntryOutdoor = _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryOutdoor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 99, 1, 2),
    _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryOutdoor_Type()
)
lcosLXStatusWLANChannelsAllowedByRegulatoryEntryOutdoor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelsAllowedByRegulatoryEntryOutdoor.setStatus("current")


class _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryDFS_Type(Integer32):
    """Custom type lcosLXStatusWLANChannelsAllowedByRegulatoryEntryDFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANChannelsAllowedByRegulatoryEntryDFS_Type.__name__ = "Integer32"
_LcosLXStatusWLANChannelsAllowedByRegulatoryEntryDFS_Object = MibTableColumn
lcosLXStatusWLANChannelsAllowedByRegulatoryEntryDFS = _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryDFS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 99, 1, 3),
    _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryDFS_Type()
)
lcosLXStatusWLANChannelsAllowedByRegulatoryEntryDFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelsAllowedByRegulatoryEntryDFS.setStatus("current")


class _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryWeatherRadarChan_Type(Integer32):
    """Custom type lcosLXStatusWLANChannelsAllowedByRegulatoryEntryWeatherRadarChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANChannelsAllowedByRegulatoryEntryWeatherRadarChan_Type.__name__ = "Integer32"
_LcosLXStatusWLANChannelsAllowedByRegulatoryEntryWeatherRadarChan_Object = MibTableColumn
lcosLXStatusWLANChannelsAllowedByRegulatoryEntryWeatherRadarChan = _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryWeatherRadarChan_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 99, 1, 4),
    _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryWeatherRadarChan_Type()
)
lcosLXStatusWLANChannelsAllowedByRegulatoryEntryWeatherRadarChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelsAllowedByRegulatoryEntryWeatherRadarChan.setStatus("current")


class _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryRadioBand_Type(Integer32):
    """Custom type lcosLXStatusWLANChannelsAllowedByRegulatoryEntryRadioBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e24GHz", 1),
          ("e5GHz", 2))
    )


_LcosLXStatusWLANChannelsAllowedByRegulatoryEntryRadioBand_Type.__name__ = "Integer32"
_LcosLXStatusWLANChannelsAllowedByRegulatoryEntryRadioBand_Object = MibTableColumn
lcosLXStatusWLANChannelsAllowedByRegulatoryEntryRadioBand = _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 3, 99, 1, 5),
    _LcosLXStatusWLANChannelsAllowedByRegulatoryEntryRadioBand_Type()
)
lcosLXStatusWLANChannelsAllowedByRegulatoryEntryRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANChannelsAllowedByRegulatoryEntryRadioBand.setStatus("current")
_LcosLXStatusLAN_ObjectIdentity = ObjectIdentity
lcosLXStatusLAN = _LcosLXStatusLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 5)
)
_LcosLXStatusLANByteTransport_Object = MibTable
lcosLXStatusLANByteTransport = _LcosLXStatusLANByteTransport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 5, 52)
)
if mibBuilder.loadTexts:
    lcosLXStatusLANByteTransport.setStatus("current")
_LcosLXStatusLANByteTransportEntry_Object = MibTableRow
lcosLXStatusLANByteTransportEntry = _LcosLXStatusLANByteTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 5, 52, 1)
)
lcosLXStatusLANByteTransportEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusLANByteTransportEntryPort"),
)
if mibBuilder.loadTexts:
    lcosLXStatusLANByteTransportEntry.setStatus("current")


class _LcosLXStatusLANByteTransportEntryPort_Type(OctetString):
    """Custom type lcosLXStatusLANByteTransportEntryPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_LcosLXStatusLANByteTransportEntryPort_Type.__name__ = "OctetString"
_LcosLXStatusLANByteTransportEntryPort_Object = MibTableColumn
lcosLXStatusLANByteTransportEntryPort = _LcosLXStatusLANByteTransportEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 5, 52, 1, 1),
    _LcosLXStatusLANByteTransportEntryPort_Type()
)
lcosLXStatusLANByteTransportEntryPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusLANByteTransportEntryPort.setStatus("current")
_LcosLXStatusLANByteTransportEntryTxBytes_Type = Counter64
_LcosLXStatusLANByteTransportEntryTxBytes_Object = MibTableColumn
lcosLXStatusLANByteTransportEntryTxBytes = _LcosLXStatusLANByteTransportEntryTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 5, 52, 1, 2),
    _LcosLXStatusLANByteTransportEntryTxBytes_Type()
)
lcosLXStatusLANByteTransportEntryTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLANByteTransportEntryTxBytes.setStatus("current")
_LcosLXStatusLANByteTransportEntryRxBytes_Type = Counter64
_LcosLXStatusLANByteTransportEntryRxBytes_Object = MibTableColumn
lcosLXStatusLANByteTransportEntryRxBytes = _LcosLXStatusLANByteTransportEntryRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 5, 52, 1, 3),
    _LcosLXStatusLANByteTransportEntryRxBytes_Type()
)
lcosLXStatusLANByteTransportEntryRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLANByteTransportEntryRxBytes.setStatus("current")
_LcosLXStatusLANByteTransportEntryRxCRCErrors_Type = Counter64
_LcosLXStatusLANByteTransportEntryRxCRCErrors_Object = MibTableColumn
lcosLXStatusLANByteTransportEntryRxCRCErrors = _LcosLXStatusLANByteTransportEntryRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 5, 52, 1, 4),
    _LcosLXStatusLANByteTransportEntryRxCRCErrors_Type()
)
lcosLXStatusLANByteTransportEntryRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLANByteTransportEntryRxCRCErrors.setStatus("current")
_LcosLXStatusLANPorts_Object = MibTable
lcosLXStatusLANPorts = _LcosLXStatusLANPorts_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 5, 99)
)
if mibBuilder.loadTexts:
    lcosLXStatusLANPorts.setStatus("current")
_LcosLXStatusLANPortsEntry_Object = MibTableRow
lcosLXStatusLANPortsEntry = _LcosLXStatusLANPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 5, 99, 1)
)
lcosLXStatusLANPortsEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusLANPortsEntryPort"),
)
if mibBuilder.loadTexts:
    lcosLXStatusLANPortsEntry.setStatus("current")


class _LcosLXStatusLANPortsEntryPort_Type(OctetString):
    """Custom type lcosLXStatusLANPortsEntryPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_LcosLXStatusLANPortsEntryPort_Type.__name__ = "OctetString"
_LcosLXStatusLANPortsEntryPort_Object = MibTableColumn
lcosLXStatusLANPortsEntryPort = _LcosLXStatusLANPortsEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 5, 99, 1, 1),
    _LcosLXStatusLANPortsEntryPort_Type()
)
lcosLXStatusLANPortsEntryPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusLANPortsEntryPort.setStatus("current")


class _LcosLXStatusLANPortsEntryLinkActive_Type(Integer32):
    """Custom type lcosLXStatusLANPortsEntryLinkActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusLANPortsEntryLinkActive_Type.__name__ = "Integer32"
_LcosLXStatusLANPortsEntryLinkActive_Object = MibTableColumn
lcosLXStatusLANPortsEntryLinkActive = _LcosLXStatusLANPortsEntryLinkActive_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 5, 99, 1, 2),
    _LcosLXStatusLANPortsEntryLinkActive_Type()
)
lcosLXStatusLANPortsEntryLinkActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLANPortsEntryLinkActive.setStatus("current")


class _LcosLXStatusLANPortsEntryConnector_Type(Integer32):
    """Custom type lcosLXStatusLANPortsEntryConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              9,
              10,
              11,
              255)
        )
    )
    namedValues = NamedValues(
        *(("eNone", 0),
          ("e10BT", 1),
          ("eFD10BTX", 2),
          ("e100BTX", 3),
          ("eFD100BTX", 4),
          ("eFD1000BTX", 6),
          ("eFD2500BTX", 9),
          ("eFD5000BTX", 10),
          ("eFD10GBTX", 11),
          ("ePowerDown", 255))
    )


_LcosLXStatusLANPortsEntryConnector_Type.__name__ = "Integer32"
_LcosLXStatusLANPortsEntryConnector_Object = MibTableColumn
lcosLXStatusLANPortsEntryConnector = _LcosLXStatusLANPortsEntryConnector_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 5, 99, 1, 3),
    _LcosLXStatusLANPortsEntryConnector_Type()
)
lcosLXStatusLANPortsEntryConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLANPortsEntryConnector.setStatus("current")
_LcosLXStatusLANPortsEntryMACAddress_Type = MacAddress
_LcosLXStatusLANPortsEntryMACAddress_Object = MibTableColumn
lcosLXStatusLANPortsEntryMACAddress = _LcosLXStatusLANPortsEntryMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 5, 99, 1, 4),
    _LcosLXStatusLANPortsEntryMACAddress_Type()
)
lcosLXStatusLANPortsEntryMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLANPortsEntryMACAddress.setStatus("current")
_LcosLXStatusConfig_ObjectIdentity = ObjectIdentity
lcosLXStatusConfig = _LcosLXStatusConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 11)
)
_LcosLXStatusConfigServices_Object = MibTable
lcosLXStatusConfigServices = _LcosLXStatusConfigServices_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 11, 71)
)
if mibBuilder.loadTexts:
    lcosLXStatusConfigServices.setStatus("current")
_LcosLXStatusConfigServicesEntry_Object = MibTableRow
lcosLXStatusConfigServicesEntry = _LcosLXStatusConfigServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 11, 71, 1)
)
lcosLXStatusConfigServicesEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusConfigServicesEntryService"),
)
if mibBuilder.loadTexts:
    lcosLXStatusConfigServicesEntry.setStatus("current")


class _LcosLXStatusConfigServicesEntryService_Type(OctetString):
    """Custom type lcosLXStatusConfigServicesEntryService based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LcosLXStatusConfigServicesEntryService_Type.__name__ = "OctetString"
_LcosLXStatusConfigServicesEntryService_Object = MibTableColumn
lcosLXStatusConfigServicesEntryService = _LcosLXStatusConfigServicesEntryService_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 11, 71, 1, 1),
    _LcosLXStatusConfigServicesEntryService_Type()
)
lcosLXStatusConfigServicesEntryService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusConfigServicesEntryService.setStatus("current")


class _LcosLXStatusConfigServicesEntryPort_Type(Unsigned32):
    """Custom type lcosLXStatusConfigServicesEntryPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusConfigServicesEntryPort_Type.__name__ = "Unsigned32"
_LcosLXStatusConfigServicesEntryPort_Object = MibTableColumn
lcosLXStatusConfigServicesEntryPort = _LcosLXStatusConfigServicesEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 11, 71, 1, 2),
    _LcosLXStatusConfigServicesEntryPort_Type()
)
lcosLXStatusConfigServicesEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusConfigServicesEntryPort.setStatus("current")


class _LcosLXStatusConfigServicesEntryProtocol_Type(OctetString):
    """Custom type lcosLXStatusConfigServicesEntryProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_LcosLXStatusConfigServicesEntryProtocol_Type.__name__ = "OctetString"
_LcosLXStatusConfigServicesEntryProtocol_Object = MibTableColumn
lcosLXStatusConfigServicesEntryProtocol = _LcosLXStatusConfigServicesEntryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 11, 71, 1, 3),
    _LcosLXStatusConfigServicesEntryProtocol_Type()
)
lcosLXStatusConfigServicesEntryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusConfigServicesEntryProtocol.setStatus("current")


class _LcosLXStatusConfigServicesEntryActive_Type(Integer32):
    """Custom type lcosLXStatusConfigServicesEntryActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusConfigServicesEntryActive_Type.__name__ = "Integer32"
_LcosLXStatusConfigServicesEntryActive_Object = MibTableColumn
lcosLXStatusConfigServicesEntryActive = _LcosLXStatusConfigServicesEntryActive_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 11, 71, 1, 4),
    _LcosLXStatusConfigServicesEntryActive_Type()
)
lcosLXStatusConfigServicesEntryActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusConfigServicesEntryActive.setStatus("current")


class _LcosLXStatusConfigServicesEntryLAN_Type(Integer32):
    """Custom type lcosLXStatusConfigServicesEntryLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusConfigServicesEntryLAN_Type.__name__ = "Integer32"
_LcosLXStatusConfigServicesEntryLAN_Object = MibTableColumn
lcosLXStatusConfigServicesEntryLAN = _LcosLXStatusConfigServicesEntryLAN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 11, 71, 1, 5),
    _LcosLXStatusConfigServicesEntryLAN_Type()
)
lcosLXStatusConfigServicesEntryLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusConfigServicesEntryLAN.setStatus("current")


class _LcosLXStatusConfigServicesEntryWLAN_Type(Integer32):
    """Custom type lcosLXStatusConfigServicesEntryWLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusConfigServicesEntryWLAN_Type.__name__ = "Integer32"
_LcosLXStatusConfigServicesEntryWLAN_Object = MibTableColumn
lcosLXStatusConfigServicesEntryWLAN = _LcosLXStatusConfigServicesEntryWLAN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 11, 71, 1, 8),
    _LcosLXStatusConfigServicesEntryWLAN_Type()
)
lcosLXStatusConfigServicesEntryWLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusConfigServicesEntryWLAN.setStatus("current")


class _LcosLXStatusCurrentTime_Type(OctetString):
    """Custom type lcosLXStatusCurrentTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LcosLXStatusCurrentTime_Type.__name__ = "OctetString"
_LcosLXStatusCurrentTime_Object = MibScalar
lcosLXStatusCurrentTime = _LcosLXStatusCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 18),
    _LcosLXStatusCurrentTime_Type()
)
lcosLXStatusCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusCurrentTime.setStatus("current")


class _LcosLXStatusCurrentTimeEpoch_Type(Unsigned32):
    """Custom type lcosLXStatusCurrentTimeEpoch based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusCurrentTimeEpoch_Type.__name__ = "Unsigned32"
_LcosLXStatusCurrentTimeEpoch_Object = MibScalar
lcosLXStatusCurrentTimeEpoch = _LcosLXStatusCurrentTimeEpoch_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 19),
    _LcosLXStatusCurrentTimeEpoch_Type()
)
lcosLXStatusCurrentTimeEpoch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusCurrentTimeEpoch.setStatus("current")
_LcosLXStatusDHCPClient_ObjectIdentity = ObjectIdentity
lcosLXStatusDHCPClient = _LcosLXStatusDHCPClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 32)
)


class _LcosLXStatusDHCPClientLMCDomain_Type(OctetString):
    """Custom type lcosLXStatusDHCPClientLMCDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcosLXStatusDHCPClientLMCDomain_Type.__name__ = "OctetString"
_LcosLXStatusDHCPClientLMCDomain_Object = MibScalar
lcosLXStatusDHCPClientLMCDomain = _LcosLXStatusDHCPClientLMCDomain_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 32, 5),
    _LcosLXStatusDHCPClientLMCDomain_Type()
)
lcosLXStatusDHCPClientLMCDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusDHCPClientLMCDomain.setStatus("current")


class _LcosLXStatusDHCPClientRolloutProjectID_Type(OctetString):
    """Custom type lcosLXStatusDHCPClientRolloutProjectID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_LcosLXStatusDHCPClientRolloutProjectID_Type.__name__ = "OctetString"
_LcosLXStatusDHCPClientRolloutProjectID_Object = MibScalar
lcosLXStatusDHCPClientRolloutProjectID = _LcosLXStatusDHCPClientRolloutProjectID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 32, 6),
    _LcosLXStatusDHCPClientRolloutProjectID_Type()
)
lcosLXStatusDHCPClientRolloutProjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusDHCPClientRolloutProjectID.setStatus("current")


class _LcosLXStatusDHCPClientRolloutLocationID_Type(OctetString):
    """Custom type lcosLXStatusDHCPClientRolloutLocationID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_LcosLXStatusDHCPClientRolloutLocationID_Type.__name__ = "OctetString"
_LcosLXStatusDHCPClientRolloutLocationID_Object = MibScalar
lcosLXStatusDHCPClientRolloutLocationID = _LcosLXStatusDHCPClientRolloutLocationID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 32, 7),
    _LcosLXStatusDHCPClientRolloutLocationID_Type()
)
lcosLXStatusDHCPClientRolloutLocationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusDHCPClientRolloutLocationID.setStatus("current")
_LcosLXStatusSNMP_ObjectIdentity = ObjectIdentity
lcosLXStatusSNMP = _LcosLXStatusSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 35)
)
_LcosLXStatusSNMPEvent_Object = MibTable
lcosLXStatusSNMPEvent = _LcosLXStatusSNMPEvent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 35, 1)
)
if mibBuilder.loadTexts:
    lcosLXStatusSNMPEvent.setStatus("current")
_LcosLXStatusSNMPEventEntry_Object = MibTableRow
lcosLXStatusSNMPEventEntry = _LcosLXStatusSNMPEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 35, 1, 1)
)
lcosLXStatusSNMPEventEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusSNMPEventEntryTrapID"),
)
if mibBuilder.loadTexts:
    lcosLXStatusSNMPEventEntry.setStatus("current")
_LcosLXStatusSNMPEventEntryTrapID_Type = ObjectIdentifier
_LcosLXStatusSNMPEventEntryTrapID_Object = MibTableColumn
lcosLXStatusSNMPEventEntryTrapID = _LcosLXStatusSNMPEventEntryTrapID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 35, 1, 1, 1),
    _LcosLXStatusSNMPEventEntryTrapID_Type()
)
lcosLXStatusSNMPEventEntryTrapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusSNMPEventEntryTrapID.setStatus("current")


class _LcosLXStatusSNMPEventEntryGroup_Type(OctetString):
    """Custom type lcosLXStatusSNMPEventEntryGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusSNMPEventEntryGroup_Type.__name__ = "OctetString"
_LcosLXStatusSNMPEventEntryGroup_Object = MibTableColumn
lcosLXStatusSNMPEventEntryGroup = _LcosLXStatusSNMPEventEntryGroup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 35, 1, 1, 2),
    _LcosLXStatusSNMPEventEntryGroup_Type()
)
lcosLXStatusSNMPEventEntryGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusSNMPEventEntryGroup.setStatus("current")


class _LcosLXStatusSNMPEventEntryName_Type(OctetString):
    """Custom type lcosLXStatusSNMPEventEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusSNMPEventEntryName_Type.__name__ = "OctetString"
_LcosLXStatusSNMPEventEntryName_Object = MibTableColumn
lcosLXStatusSNMPEventEntryName = _LcosLXStatusSNMPEventEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 35, 1, 1, 3),
    _LcosLXStatusSNMPEventEntryName_Type()
)
lcosLXStatusSNMPEventEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusSNMPEventEntryName.setStatus("current")


class _LcosLXStatusSNMPEventEntryCount_Type(Unsigned32):
    """Custom type lcosLXStatusSNMPEventEntryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusSNMPEventEntryCount_Type.__name__ = "Unsigned32"
_LcosLXStatusSNMPEventEntryCount_Object = MibTableColumn
lcosLXStatusSNMPEventEntryCount = _LcosLXStatusSNMPEventEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 35, 1, 1, 4),
    _LcosLXStatusSNMPEventEntryCount_Type()
)
lcosLXStatusSNMPEventEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusSNMPEventEntryCount.setStatus("current")
_LcosLXStatusHardwareInfo_ObjectIdentity = ObjectIdentity
lcosLXStatusHardwareInfo = _LcosLXStatusHardwareInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 47)
)


class _LcosLXStatusHardwareInfoTotalMemoryKbytes_Type(Unsigned32):
    """Custom type lcosLXStatusHardwareInfoTotalMemoryKbytes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusHardwareInfoTotalMemoryKbytes_Type.__name__ = "Unsigned32"
_LcosLXStatusHardwareInfoTotalMemoryKbytes_Object = MibScalar
lcosLXStatusHardwareInfoTotalMemoryKbytes = _LcosLXStatusHardwareInfoTotalMemoryKbytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 47, 4),
    _LcosLXStatusHardwareInfoTotalMemoryKbytes_Type()
)
lcosLXStatusHardwareInfoTotalMemoryKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusHardwareInfoTotalMemoryKbytes.setStatus("current")


class _LcosLXStatusHardwareInfoFreeMemoryKbytes_Type(Unsigned32):
    """Custom type lcosLXStatusHardwareInfoFreeMemoryKbytes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusHardwareInfoFreeMemoryKbytes_Type.__name__ = "Unsigned32"
_LcosLXStatusHardwareInfoFreeMemoryKbytes_Object = MibScalar
lcosLXStatusHardwareInfoFreeMemoryKbytes = _LcosLXStatusHardwareInfoFreeMemoryKbytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 47, 5),
    _LcosLXStatusHardwareInfoFreeMemoryKbytes_Type()
)
lcosLXStatusHardwareInfoFreeMemoryKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusHardwareInfoFreeMemoryKbytes.setStatus("current")


class _LcosLXStatusHardwareInfoSerialNumber_Type(OctetString):
    """Custom type lcosLXStatusHardwareInfoSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LcosLXStatusHardwareInfoSerialNumber_Type.__name__ = "OctetString"
_LcosLXStatusHardwareInfoSerialNumber_Object = MibScalar
lcosLXStatusHardwareInfoSerialNumber = _LcosLXStatusHardwareInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 47, 7),
    _LcosLXStatusHardwareInfoSerialNumber_Type()
)
lcosLXStatusHardwareInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusHardwareInfoSerialNumber.setStatus("current")


class _LcosLXStatusHardwareInfoBoardRevision_Type(OctetString):
    """Custom type lcosLXStatusHardwareInfoBoardRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LcosLXStatusHardwareInfoBoardRevision_Type.__name__ = "OctetString"
_LcosLXStatusHardwareInfoBoardRevision_Object = MibScalar
lcosLXStatusHardwareInfoBoardRevision = _LcosLXStatusHardwareInfoBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 47, 8),
    _LcosLXStatusHardwareInfoBoardRevision_Type()
)
lcosLXStatusHardwareInfoBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusHardwareInfoBoardRevision.setStatus("current")


class _LcosLXStatusHardwareInfoSWVersion_Type(OctetString):
    """Custom type lcosLXStatusHardwareInfoSWVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusHardwareInfoSWVersion_Type.__name__ = "OctetString"
_LcosLXStatusHardwareInfoSWVersion_Object = MibScalar
lcosLXStatusHardwareInfoSWVersion = _LcosLXStatusHardwareInfoSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 47, 9),
    _LcosLXStatusHardwareInfoSWVersion_Type()
)
lcosLXStatusHardwareInfoSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusHardwareInfoSWVersion.setStatus("current")


class _LcosLXStatusHardwareInfoCPULoad60sPercent_Type(Unsigned32):
    """Custom type lcosLXStatusHardwareInfoCPULoad60sPercent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusHardwareInfoCPULoad60sPercent_Type.__name__ = "Unsigned32"
_LcosLXStatusHardwareInfoCPULoad60sPercent_Object = MibScalar
lcosLXStatusHardwareInfoCPULoad60sPercent = _LcosLXStatusHardwareInfoCPULoad60sPercent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 47, 14),
    _LcosLXStatusHardwareInfoCPULoad60sPercent_Type()
)
lcosLXStatusHardwareInfoCPULoad60sPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusHardwareInfoCPULoad60sPercent.setStatus("current")


class _LcosLXStatusHardwareInfoProductiondate_Type(OctetString):
    """Custom type lcosLXStatusHardwareInfoProductiondate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LcosLXStatusHardwareInfoProductiondate_Type.__name__ = "OctetString"
_LcosLXStatusHardwareInfoProductiondate_Object = MibScalar
lcosLXStatusHardwareInfoProductiondate = _LcosLXStatusHardwareInfoProductiondate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 47, 41),
    _LcosLXStatusHardwareInfoProductiondate_Type()
)
lcosLXStatusHardwareInfoProductiondate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusHardwareInfoProductiondate.setStatus("current")
_LcosLXStatusWLANManagement_ObjectIdentity = ObjectIdentity
lcosLXStatusWLANManagement = _LcosLXStatusWLANManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59)
)
_LcosLXStatusWLANManagementAPConnections_Object = MibTable
lcosLXStatusWLANManagementAPConnections = _LcosLXStatusWLANManagementAPConnections_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 1)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementAPConnections.setStatus("current")
_LcosLXStatusWLANManagementAPConnectionsEntry_Object = MibTableRow
lcosLXStatusWLANManagementAPConnectionsEntry = _LcosLXStatusWLANManagementAPConnectionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 1, 1)
)
lcosLXStatusWLANManagementAPConnectionsEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANManagementAPConnectionsEntryIPAddress"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementAPConnectionsEntry.setStatus("current")


class _LcosLXStatusWLANManagementAPConnectionsEntryIPAddress_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementAPConnectionsEntryIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_LcosLXStatusWLANManagementAPConnectionsEntryIPAddress_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementAPConnectionsEntryIPAddress_Object = MibTableColumn
lcosLXStatusWLANManagementAPConnectionsEntryIPAddress = _LcosLXStatusWLANManagementAPConnectionsEntryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 1, 1, 2),
    _LcosLXStatusWLANManagementAPConnectionsEntryIPAddress_Type()
)
lcosLXStatusWLANManagementAPConnectionsEntryIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementAPConnectionsEntryIPAddress.setStatus("current")


class _LcosLXStatusWLANManagementAPConnectionsEntryPort_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementAPConnectionsEntryPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANManagementAPConnectionsEntryPort_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementAPConnectionsEntryPort_Object = MibTableColumn
lcosLXStatusWLANManagementAPConnectionsEntryPort = _LcosLXStatusWLANManagementAPConnectionsEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 1, 1, 3),
    _LcosLXStatusWLANManagementAPConnectionsEntryPort_Type()
)
lcosLXStatusWLANManagementAPConnectionsEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementAPConnectionsEntryPort.setStatus("current")


class _LcosLXStatusWLANManagementAPConnectionsEntryRespTime_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementAPConnectionsEntryRespTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANManagementAPConnectionsEntryRespTime_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementAPConnectionsEntryRespTime_Object = MibTableColumn
lcosLXStatusWLANManagementAPConnectionsEntryRespTime = _LcosLXStatusWLANManagementAPConnectionsEntryRespTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 1, 1, 4),
    _LcosLXStatusWLANManagementAPConnectionsEntryRespTime_Type()
)
lcosLXStatusWLANManagementAPConnectionsEntryRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementAPConnectionsEntryRespTime.setStatus("current")


class _LcosLXStatusWLANManagementAPConnectionsEntryName_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementAPConnectionsEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANManagementAPConnectionsEntryName_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementAPConnectionsEntryName_Object = MibTableColumn
lcosLXStatusWLANManagementAPConnectionsEntryName = _LcosLXStatusWLANManagementAPConnectionsEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 1, 1, 5),
    _LcosLXStatusWLANManagementAPConnectionsEntryName_Type()
)
lcosLXStatusWLANManagementAPConnectionsEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementAPConnectionsEntryName.setStatus("current")


class _LcosLXStatusWLANManagementAPConnectionsEntryState_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementAPConnectionsEntryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              100)
        )
    )
    namedValues = NamedValues(
        *(("eUnknown", 0),
          ("eIdle", 5),
          ("eDiscovery", 10),
          ("eDTLSSetup", 15),
          ("eJoin", 20),
          ("eConfigure", 25),
          ("eImageData", 30),
          ("eReset", 35),
          ("eDTLSTeardown", 40),
          ("eSulking", 45),
          ("eRun", 100))
    )


_LcosLXStatusWLANManagementAPConnectionsEntryState_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementAPConnectionsEntryState_Object = MibTableColumn
lcosLXStatusWLANManagementAPConnectionsEntryState = _LcosLXStatusWLANManagementAPConnectionsEntryState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 1, 1, 6),
    _LcosLXStatusWLANManagementAPConnectionsEntryState_Type()
)
lcosLXStatusWLANManagementAPConnectionsEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementAPConnectionsEntryState.setStatus("current")


class _LcosLXStatusWLANManagementAPConnectionsEntryResult_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementAPConnectionsEntryResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              300,
              301,
              302,
              303)
        )
    )
    namedValues = NamedValues(
        *(("eSuccess", 0),
          ("eFailure", 1),
          ("eSuccessNAT", 2),
          ("eJoinFailunspecified", 3),
          ("eJoinFailResourceDepletion", 4),
          ("eJoinFailUnknwnSrc", 5),
          ("eJoinFailIncorrectData", 6),
          ("eJoinFailSessionIDinuse", 7),
          ("eJoinFailWTPnotsupported", 8),
          ("eJoinFailBindingnotsupp", 9),
          ("eResetFailUnabletoReset", 10),
          ("eResetFailFirmwWriteErr", 11),
          ("eFailMissingMandMsgElem", 12),
          ("eFailUnrecognizedMsgElem", 13),
          ("eUnsupportedLoaderVersion", 14),
          ("eUnsupportedFirmwareVersion", 15),
          ("e", 16),
          ("eConfigurationErrorServprovanyhow", 17),
          ("eConfigurationErrorServnotprov", 18),
          ("eImageDataErrorChecksum", 19),
          ("eImageDataErrorLength", 20),
          ("eImageDataErrorOther", 21),
          ("eImageDataErrorAlrpresent", 300),
          ("eMessageUnexpectedinvalid", 301),
          ("eMessageUnexpectedunrecognized", 302),
          ("eJoinFailAlreadyConnected", 303))
    )


_LcosLXStatusWLANManagementAPConnectionsEntryResult_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementAPConnectionsEntryResult_Object = MibTableColumn
lcosLXStatusWLANManagementAPConnectionsEntryResult = _LcosLXStatusWLANManagementAPConnectionsEntryResult_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 1, 1, 7),
    _LcosLXStatusWLANManagementAPConnectionsEntryResult_Type()
)
lcosLXStatusWLANManagementAPConnectionsEntryResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementAPConnectionsEntryResult.setStatus("current")


class _LcosLXStatusWLANManagementAPConnectionsEntryUtilisation_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementAPConnectionsEntryUtilisation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANManagementAPConnectionsEntryUtilisation_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementAPConnectionsEntryUtilisation_Object = MibTableColumn
lcosLXStatusWLANManagementAPConnectionsEntryUtilisation = _LcosLXStatusWLANManagementAPConnectionsEntryUtilisation_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 1, 1, 9),
    _LcosLXStatusWLANManagementAPConnectionsEntryUtilisation_Type()
)
lcosLXStatusWLANManagementAPConnectionsEntryUtilisation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementAPConnectionsEntryUtilisation.setStatus("current")


class _LcosLXStatusWLANManagementAPConnectionsEntryFirmwareVersion_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementAPConnectionsEntryFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANManagementAPConnectionsEntryFirmwareVersion_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementAPConnectionsEntryFirmwareVersion_Object = MibTableColumn
lcosLXStatusWLANManagementAPConnectionsEntryFirmwareVersion = _LcosLXStatusWLANManagementAPConnectionsEntryFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 1, 1, 10),
    _LcosLXStatusWLANManagementAPConnectionsEntryFirmwareVersion_Type()
)
lcosLXStatusWLANManagementAPConnectionsEntryFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementAPConnectionsEntryFirmwareVersion.setStatus("current")


class _LcosLXStatusWLANManagementAPConnectionsEntryPMTU_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementAPConnectionsEntryPMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANManagementAPConnectionsEntryPMTU_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementAPConnectionsEntryPMTU_Object = MibTableColumn
lcosLXStatusWLANManagementAPConnectionsEntryPMTU = _LcosLXStatusWLANManagementAPConnectionsEntryPMTU_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 1, 1, 11),
    _LcosLXStatusWLANManagementAPConnectionsEntryPMTU_Type()
)
lcosLXStatusWLANManagementAPConnectionsEntryPMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementAPConnectionsEntryPMTU.setStatus("current")


class _LcosLXStatusWLANManagementAPConnectionsEntryPreference_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementAPConnectionsEntryPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANManagementAPConnectionsEntryPreference_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementAPConnectionsEntryPreference_Object = MibTableColumn
lcosLXStatusWLANManagementAPConnectionsEntryPreference = _LcosLXStatusWLANManagementAPConnectionsEntryPreference_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 1, 1, 14),
    _LcosLXStatusWLANManagementAPConnectionsEntryPreference_Type()
)
lcosLXStatusWLANManagementAPConnectionsEntryPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementAPConnectionsEntryPreference.setStatus("current")


class _LcosLXStatusWLANManagementAPConnectionsEntryCPULoad300sPercent_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementAPConnectionsEntryCPULoad300sPercent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANManagementAPConnectionsEntryCPULoad300sPercent_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementAPConnectionsEntryCPULoad300sPercent_Object = MibTableColumn
lcosLXStatusWLANManagementAPConnectionsEntryCPULoad300sPercent = _LcosLXStatusWLANManagementAPConnectionsEntryCPULoad300sPercent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 1, 1, 15),
    _LcosLXStatusWLANManagementAPConnectionsEntryCPULoad300sPercent_Type()
)
lcosLXStatusWLANManagementAPConnectionsEntryCPULoad300sPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementAPConnectionsEntryCPULoad300sPercent.setStatus("current")


class _LcosLXStatusWLANManagementAPConnectionsEntryRetransmissions_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementAPConnectionsEntryRetransmissions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANManagementAPConnectionsEntryRetransmissions_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementAPConnectionsEntryRetransmissions_Object = MibTableColumn
lcosLXStatusWLANManagementAPConnectionsEntryRetransmissions = _LcosLXStatusWLANManagementAPConnectionsEntryRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 1, 1, 16),
    _LcosLXStatusWLANManagementAPConnectionsEntryRetransmissions_Type()
)
lcosLXStatusWLANManagementAPConnectionsEntryRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementAPConnectionsEntryRetransmissions.setStatus("current")


class _LcosLXStatusWLANManagementState_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              10,
              15,
              20,
              25,
              30,
              35,
              40,
              45,
              100)
        )
    )
    namedValues = NamedValues(
        *(("eUnknown", 0),
          ("eIdle", 5),
          ("eDiscovery", 10),
          ("eDTLSSetup", 15),
          ("eJoin", 20),
          ("eConfigure", 25),
          ("eImageData", 30),
          ("eReset", 35),
          ("eDTLSTeardown", 40),
          ("eSulking", 45),
          ("eRun", 100))
    )


_LcosLXStatusWLANManagementState_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementState_Object = MibScalar
lcosLXStatusWLANManagementState = _LcosLXStatusWLANManagementState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 2),
    _LcosLXStatusWLANManagementState_Type()
)
lcosLXStatusWLANManagementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementState.setStatus("current")


class _LcosLXStatusWLANManagementStarted_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementStarted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LcosLXStatusWLANManagementStarted_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementStarted_Object = MibScalar
lcosLXStatusWLANManagementStarted = _LcosLXStatusWLANManagementStarted_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 3),
    _LcosLXStatusWLANManagementStarted_Type()
)
lcosLXStatusWLANManagementStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementStarted.setStatus("current")


class _LcosLXStatusWLANManagementDNSSuffix_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementDNSSuffix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANManagementDNSSuffix_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementDNSSuffix_Object = MibScalar
lcosLXStatusWLANManagementDNSSuffix = _LcosLXStatusWLANManagementDNSSuffix_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 4),
    _LcosLXStatusWLANManagementDNSSuffix_Type()
)
lcosLXStatusWLANManagementDNSSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementDNSSuffix.setStatus("current")
_LcosLXStatusWLANManagementRadioprofiles_Object = MibTable
lcosLXStatusWLANManagementRadioprofiles = _LcosLXStatusWLANManagementRadioprofiles_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofiles.setStatus("current")
_LcosLXStatusWLANManagementRadioprofilesEntry_Object = MibTableRow
lcosLXStatusWLANManagementRadioprofilesEntry = _LcosLXStatusWLANManagementRadioprofilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101, 1)
)
lcosLXStatusWLANManagementRadioprofilesEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANManagementRadioprofilesEntryName"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofilesEntry.setStatus("current")


class _LcosLXStatusWLANManagementRadioprofilesEntryName_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementRadioprofilesEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANManagementRadioprofilesEntryName_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementRadioprofilesEntryName_Object = MibTableColumn
lcosLXStatusWLANManagementRadioprofilesEntryName = _LcosLXStatusWLANManagementRadioprofilesEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101, 1, 1),
    _LcosLXStatusWLANManagementRadioprofilesEntryName_Type()
)
lcosLXStatusWLANManagementRadioprofilesEntryName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofilesEntryName.setStatus("current")


class _LcosLXStatusWLANManagementRadioprofilesEntryCountry_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementRadioprofilesEntryCountry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(36,
              40,
              56,
              100,
              191,
              196,
              203,
              208,
              233,
              246,
              250,
              276,
              300,
              348,
              372,
              380,
              428,
              440,
              442,
              470,
              528,
              554,
              616,
              620,
              642,
              703,
              705,
              724,
              752,
              756,
              826,
              840,
              998)
        )
    )
    namedValues = NamedValues(
        *(("eAustralia", 36),
          ("eAustria", 40),
          ("eBelgium", 56),
          ("eBulgaria", 100),
          ("eCroatia", 191),
          ("eCyprus", 196),
          ("eCzechRepublic", 203),
          ("eDenmark", 208),
          ("eEstonia", 233),
          ("eFinland", 246),
          ("eFrance", 250),
          ("eGermany", 276),
          ("eGreece", 300),
          ("eHungary", 348),
          ("eIreland", 372),
          ("eItaly", 380),
          ("eLatvia", 428),
          ("eLithuania", 440),
          ("eLuxembourg", 442),
          ("eMalta", 470),
          ("eNetherlands", 528),
          ("eNewZealand", 554),
          ("ePoland", 616),
          ("ePortugal", 620),
          ("eRomania", 642),
          ("eSlovakia", 703),
          ("eSlovenia", 705),
          ("eSpain", 724),
          ("eSweden", 752),
          ("eSwitzerland", 756),
          ("eUnitedKingdom", 826),
          ("eUnitedStates", 840),
          ("eEurope", 998))
    )


_LcosLXStatusWLANManagementRadioprofilesEntryCountry_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementRadioprofilesEntryCountry_Object = MibTableColumn
lcosLXStatusWLANManagementRadioprofilesEntryCountry = _LcosLXStatusWLANManagementRadioprofilesEntryCountry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101, 1, 4),
    _LcosLXStatusWLANManagementRadioprofilesEntryCountry_Type()
)
lcosLXStatusWLANManagementRadioprofilesEntryCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofilesEntryCountry.setStatus("current")


class _LcosLXStatusWLANManagementRadioprofilesEntry24GHzMode_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementRadioprofilesEntry24GHzMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e11bgmixed", 0),
          ("e11gonly", 1),
          ("e11bonly", 2),
          ("e108Mbps", 3),
          ("e11bgnmixed", 4),
          ("e11gnmixed", 5),
          ("eGreenfield", 6),
          ("eAuto", 255))
    )


_LcosLXStatusWLANManagementRadioprofilesEntry24GHzMode_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementRadioprofilesEntry24GHzMode_Object = MibTableColumn
lcosLXStatusWLANManagementRadioprofilesEntry24GHzMode = _LcosLXStatusWLANManagementRadioprofilesEntry24GHzMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101, 1, 6),
    _LcosLXStatusWLANManagementRadioprofilesEntry24GHzMode_Type()
)
lcosLXStatusWLANManagementRadioprofilesEntry24GHzMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofilesEntry24GHzMode.setStatus("current")


class _LcosLXStatusWLANManagementRadioprofilesEntry5GHzMode_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementRadioprofilesEntry5GHzMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              7,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("eNormal", 0),
          ("e108Mbps", 3),
          ("e11anmixed", 4),
          ("eGreenfield", 5),
          ("e11anacmixed", 6),
          ("e11nacmixed", 7),
          ("e11aconly", 8),
          ("eAuto", 255))
    )


_LcosLXStatusWLANManagementRadioprofilesEntry5GHzMode_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementRadioprofilesEntry5GHzMode_Object = MibTableColumn
lcosLXStatusWLANManagementRadioprofilesEntry5GHzMode = _LcosLXStatusWLANManagementRadioprofilesEntry5GHzMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101, 1, 7),
    _LcosLXStatusWLANManagementRadioprofilesEntry5GHzMode_Type()
)
lcosLXStatusWLANManagementRadioprofilesEntry5GHzMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofilesEntry5GHzMode.setStatus("current")


class _LcosLXStatusWLANManagementRadioprofilesEntrySubbands_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementRadioprofilesEntrySubbands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("eBand123", 0),
          ("eBand1", 1),
          ("eBand2", 2),
          ("eBand3", 3),
          ("eBand12", 4),
          ("eBand13", 5),
          ("eBand23", 6))
    )


_LcosLXStatusWLANManagementRadioprofilesEntrySubbands_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementRadioprofilesEntrySubbands_Object = MibTableColumn
lcosLXStatusWLANManagementRadioprofilesEntrySubbands = _LcosLXStatusWLANManagementRadioprofilesEntrySubbands_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101, 1, 8),
    _LcosLXStatusWLANManagementRadioprofilesEntrySubbands_Type()
)
lcosLXStatusWLANManagementRadioprofilesEntrySubbands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofilesEntrySubbands.setStatus("current")


class _LcosLXStatusWLANManagementRadioprofilesEntryQoS_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementRadioprofilesEntryQoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANManagementRadioprofilesEntryQoS_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementRadioprofilesEntryQoS_Object = MibTableColumn
lcosLXStatusWLANManagementRadioprofilesEntryQoS = _LcosLXStatusWLANManagementRadioprofilesEntryQoS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101, 1, 9),
    _LcosLXStatusWLANManagementRadioprofilesEntryQoS_Type()
)
lcosLXStatusWLANManagementRadioprofilesEntryQoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofilesEntryQoS.setStatus("current")


class _LcosLXStatusWLANManagementRadioprofilesEntryDTIMPeriod_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementRadioprofilesEntryDTIMPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANManagementRadioprofilesEntryDTIMPeriod_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementRadioprofilesEntryDTIMPeriod_Object = MibTableColumn
lcosLXStatusWLANManagementRadioprofilesEntryDTIMPeriod = _LcosLXStatusWLANManagementRadioprofilesEntryDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101, 1, 10),
    _LcosLXStatusWLANManagementRadioprofilesEntryDTIMPeriod_Type()
)
lcosLXStatusWLANManagementRadioprofilesEntryDTIMPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofilesEntryDTIMPeriod.setStatus("current")


class _LcosLXStatusWLANManagementRadioprofilesEntryBackgroundScan_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementRadioprofilesEntryBackgroundScan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANManagementRadioprofilesEntryBackgroundScan_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementRadioprofilesEntryBackgroundScan_Object = MibTableColumn
lcosLXStatusWLANManagementRadioprofilesEntryBackgroundScan = _LcosLXStatusWLANManagementRadioprofilesEntryBackgroundScan_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101, 1, 11),
    _LcosLXStatusWLANManagementRadioprofilesEntryBackgroundScan_Type()
)
lcosLXStatusWLANManagementRadioprofilesEntryBackgroundScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofilesEntryBackgroundScan.setStatus("current")


class _LcosLXStatusWLANManagementRadioprofilesEntryAntennaGain_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementRadioprofilesEntryAntennaGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_LcosLXStatusWLANManagementRadioprofilesEntryAntennaGain_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementRadioprofilesEntryAntennaGain_Object = MibTableColumn
lcosLXStatusWLANManagementRadioprofilesEntryAntennaGain = _LcosLXStatusWLANManagementRadioprofilesEntryAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101, 1, 12),
    _LcosLXStatusWLANManagementRadioprofilesEntryAntennaGain_Type()
)
lcosLXStatusWLANManagementRadioprofilesEntryAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofilesEntryAntennaGain.setStatus("current")


class _LcosLXStatusWLANManagementRadioprofilesEntryTxPowerReduction_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementRadioprofilesEntryTxPowerReduction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANManagementRadioprofilesEntryTxPowerReduction_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementRadioprofilesEntryTxPowerReduction_Object = MibTableColumn
lcosLXStatusWLANManagementRadioprofilesEntryTxPowerReduction = _LcosLXStatusWLANManagementRadioprofilesEntryTxPowerReduction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101, 1, 13),
    _LcosLXStatusWLANManagementRadioprofilesEntryTxPowerReduction_Type()
)
lcosLXStatusWLANManagementRadioprofilesEntryTxPowerReduction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofilesEntryTxPowerReduction.setStatus("current")


class _LcosLXStatusWLANManagementRadioprofilesEntryIndoorOnlyOperation_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementRadioprofilesEntryIndoorOnlyOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANManagementRadioprofilesEntryIndoorOnlyOperation_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementRadioprofilesEntryIndoorOnlyOperation_Object = MibTableColumn
lcosLXStatusWLANManagementRadioprofilesEntryIndoorOnlyOperation = _LcosLXStatusWLANManagementRadioprofilesEntryIndoorOnlyOperation_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101, 1, 16),
    _LcosLXStatusWLANManagementRadioprofilesEntryIndoorOnlyOperation_Type()
)
lcosLXStatusWLANManagementRadioprofilesEntryIndoorOnlyOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofilesEntryIndoorOnlyOperation.setStatus("current")


class _LcosLXStatusWLANManagementRadioprofilesEntryReportSeenClients_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementRadioprofilesEntryReportSeenClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANManagementRadioprofilesEntryReportSeenClients_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementRadioprofilesEntryReportSeenClients_Object = MibTableColumn
lcosLXStatusWLANManagementRadioprofilesEntryReportSeenClients = _LcosLXStatusWLANManagementRadioprofilesEntryReportSeenClients_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101, 1, 20),
    _LcosLXStatusWLANManagementRadioprofilesEntryReportSeenClients_Type()
)
lcosLXStatusWLANManagementRadioprofilesEntryReportSeenClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofilesEntryReportSeenClients.setStatus("current")


class _LcosLXStatusWLANManagementRadioprofilesEntryRxSensReduction_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementRadioprofilesEntryRxSensReduction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXStatusWLANManagementRadioprofilesEntryRxSensReduction_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementRadioprofilesEntryRxSensReduction_Object = MibTableColumn
lcosLXStatusWLANManagementRadioprofilesEntryRxSensReduction = _LcosLXStatusWLANManagementRadioprofilesEntryRxSensReduction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 101, 1, 25),
    _LcosLXStatusWLANManagementRadioprofilesEntryRxSensReduction_Type()
)
lcosLXStatusWLANManagementRadioprofilesEntryRxSensReduction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRadioprofilesEntryRxSensReduction.setStatus("current")
_LcosLXStatusWLANManagementNetworkprofiles_Object = MibTable
lcosLXStatusWLANManagementNetworkprofiles = _LcosLXStatusWLANManagementNetworkprofiles_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofiles.setStatus("current")
_LcosLXStatusWLANManagementNetworkprofilesEntry_Object = MibTableRow
lcosLXStatusWLANManagementNetworkprofilesEntry = _LcosLXStatusWLANManagementNetworkprofilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1)
)
lcosLXStatusWLANManagementNetworkprofilesEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANManagementNetworkprofilesEntryName"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntry.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryName_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryName_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementNetworkprofilesEntryName_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryName = _LcosLXStatusWLANManagementNetworkprofilesEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 1),
    _LcosLXStatusWLANManagementNetworkprofilesEntryName_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryName.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryOperating_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryOperating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryOperating_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryOperating_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryOperating = _LcosLXStatusWLANManagementNetworkprofilesEntryOperating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 4),
    _LcosLXStatusWLANManagementNetworkprofilesEntryOperating_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryOperating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryOperating.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryEncryption_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("e80211iWPAPSK", 0),
          ("e80211iWPA8021x", 1),
          ("eWEP104Bits", 2),
          ("eWEP40Bits", 3),
          ("eWEP104Bits8021x", 4),
          ("eWEP40Bits8021x", 5),
          ("eNone", 6),
          ("eEnhancedOpen", 7),
          ("eEnhancedOpenTransitional", 8))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryEncryption_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryEncryption_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryEncryption = _LcosLXStatusWLANManagementNetworkprofilesEntryEncryption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 6),
    _LcosLXStatusWLANManagementNetworkprofilesEntryEncryption_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryEncryption.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryWPA1SessKeytypes_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryWPA1SessKeytypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eTKIP", 1),
          ("eAES", 2),
          ("eTKIPAES", 3))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryWPA1SessKeytypes_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryWPA1SessKeytypes_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryWPA1SessKeytypes = _LcosLXStatusWLANManagementNetworkprofilesEntryWPA1SessKeytypes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 7),
    _LcosLXStatusWLANManagementNetworkprofilesEntryWPA1SessKeytypes_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryWPA1SessKeytypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryWPA1SessKeytypes.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryWPAVersion_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryWPAVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eWPA12", 0),
          ("eWPA1", 1),
          ("eWPA2", 2),
          ("eWPA3", 3),
          ("eWPA23", 4),
          ("eWPA123", 5))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryWPAVersion_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryWPAVersion_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryWPAVersion = _LcosLXStatusWLANManagementNetworkprofilesEntryWPAVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 8),
    _LcosLXStatusWLANManagementNetworkprofilesEntryWPAVersion_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryWPAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryWPAVersion.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryKey_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryKey_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementNetworkprofilesEntryKey_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryKey = _LcosLXStatusWLANManagementNetworkprofilesEntryKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 9),
    _LcosLXStatusWLANManagementNetworkprofilesEntryKey_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryKey.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryRadioBand_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryRadioBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e24GHz5GHz", 0),
          ("e24GHz", 1),
          ("e5GHz", 2))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryRadioBand_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryRadioBand_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryRadioBand = _LcosLXStatusWLANManagementNetworkprofilesEntryRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 10),
    _LcosLXStatusWLANManagementNetworkprofilesEntryRadioBand_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryRadioBand.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryContinuationTime_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryContinuationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryContinuationTime_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementNetworkprofilesEntryContinuationTime_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryContinuationTime = _LcosLXStatusWLANManagementNetworkprofilesEntryContinuationTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 11),
    _LcosLXStatusWLANManagementNetworkprofilesEntryContinuationTime_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryContinuationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryContinuationTime.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryMinTxRate_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryMinTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("eAuto", 0),
          ("e1M", 1),
          ("e2M", 2),
          ("e55M", 3),
          ("e11M", 4),
          ("e6M", 5),
          ("e9M", 6),
          ("e12M", 7),
          ("e18M", 8),
          ("e24M", 9),
          ("e36M", 10),
          ("e48M", 11),
          ("e54M", 12),
          ("eT72M", 13),
          ("eT96M", 14),
          ("eT108M", 15))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryMinTxRate_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryMinTxRate_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryMinTxRate = _LcosLXStatusWLANManagementNetworkprofilesEntryMinTxRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 12),
    _LcosLXStatusWLANManagementNetworkprofilesEntryMinTxRate_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryMinTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryMinTxRate.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryMaxTxRate_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryMaxTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("eAuto", 0),
          ("e1M", 1),
          ("e2M", 2),
          ("e55M", 3),
          ("e11M", 4),
          ("e6M", 5),
          ("e9M", 6),
          ("e12M", 7),
          ("e18M", 8),
          ("e24M", 9),
          ("e36M", 10),
          ("e48M", 11),
          ("e54M", 12),
          ("eT72M", 13),
          ("eT96M", 14),
          ("eT108M", 15))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryMaxTxRate_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryMaxTxRate_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryMaxTxRate = _LcosLXStatusWLANManagementNetworkprofilesEntryMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 13),
    _LcosLXStatusWLANManagementNetworkprofilesEntryMaxTxRate_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryMaxTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryMaxTxRate.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryBasicRate_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryBasicRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("e2M", 0),
          ("e1M", 1),
          ("eAuto", 2),
          ("e55M", 3),
          ("e11M", 4),
          ("e6M", 5),
          ("e9M", 6),
          ("e12M", 7),
          ("e18M", 8),
          ("e24M", 9),
          ("e36M", 10),
          ("e48M", 11),
          ("e54M", 12),
          ("eT72M", 13),
          ("eT96M", 14),
          ("eT108M", 15))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryBasicRate_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryBasicRate_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryBasicRate = _LcosLXStatusWLANManagementNetworkprofilesEntryBasicRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 14),
    _LcosLXStatusWLANManagementNetworkprofilesEntryBasicRate_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryBasicRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryBasicRate.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryPreamble_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryPreamble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eAuto", 0),
          ("eLang", 1))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryPreamble_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryPreamble_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryPreamble = _LcosLXStatusWLANManagementNetworkprofilesEntryPreamble_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 15),
    _LcosLXStatusWLANManagementNetworkprofilesEntryPreamble_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryPreamble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryPreamble.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryMACFilter_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryMACFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryMACFilter_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryMACFilter_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryMACFilter = _LcosLXStatusWLANManagementNetworkprofilesEntryMACFilter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 16),
    _LcosLXStatusWLANManagementNetworkprofilesEntryMACFilter_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryMACFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryMACFilter.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryClBrgSupport_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryClBrgSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1),
          ("eExclusive", 2))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryClBrgSupport_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryClBrgSupport_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryClBrgSupport = _LcosLXStatusWLANManagementNetworkprofilesEntryClBrgSupport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 17),
    _LcosLXStatusWLANManagementNetworkprofilesEntryClBrgSupport_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryClBrgSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryClBrgSupport.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryMaxStations_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryMaxStations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryMaxStations_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementNetworkprofilesEntryMaxStations_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryMaxStations = _LcosLXStatusWLANManagementNetworkprofilesEntryMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 18),
    _LcosLXStatusWLANManagementNetworkprofilesEntryMaxStations_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryMaxStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryMaxStations.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryClosedNetwork_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryClosedNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1),
          ("eTightened", 2))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryClosedNetwork_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryClosedNetwork_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryClosedNetwork = _LcosLXStatusWLANManagementNetworkprofilesEntryClosedNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 19),
    _LcosLXStatusWLANManagementNetworkprofilesEntryClosedNetwork_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryClosedNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryClosedNetwork.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntrySSID_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntrySSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANManagementNetworkprofilesEntrySSID_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementNetworkprofilesEntrySSID_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntrySSID = _LcosLXStatusWLANManagementNetworkprofilesEntrySSID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 21),
    _LcosLXStatusWLANManagementNetworkprofilesEntrySSID_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntrySSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntrySSID.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryMinHTMCS_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryMinHTMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eAuto", 0),
          ("eMCS08", 1),
          ("eMCS19", 2),
          ("eMCS210", 3),
          ("eMCS311", 4),
          ("eMCS412", 5),
          ("eMCS513", 6),
          ("eMCS614", 7),
          ("eMCS715", 8))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryMinHTMCS_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryMinHTMCS_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryMinHTMCS = _LcosLXStatusWLANManagementNetworkprofilesEntryMinHTMCS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 22),
    _LcosLXStatusWLANManagementNetworkprofilesEntryMinHTMCS_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryMinHTMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryMinHTMCS.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryMaxHTMCS_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryMaxHTMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eAuto", 0),
          ("eMCS08", 1),
          ("eMCS19", 2),
          ("eMCS210", 3),
          ("eMCS311", 4),
          ("eMCS412", 5),
          ("eMCS513", 6),
          ("eMCS614", 7),
          ("eMCS715", 8))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryMaxHTMCS_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryMaxHTMCS_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryMaxHTMCS = _LcosLXStatusWLANManagementNetworkprofilesEntryMaxHTMCS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 23),
    _LcosLXStatusWLANManagementNetworkprofilesEntryMaxHTMCS_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryMaxHTMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryMaxHTMCS.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryShortGuardInterval_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryShortGuardInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eAuto", 0),
          ("eNo", 1))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryShortGuardInterval_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryShortGuardInterval_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryShortGuardInterval = _LcosLXStatusWLANManagementNetworkprofilesEntryShortGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 24),
    _LcosLXStatusWLANManagementNetworkprofilesEntryShortGuardInterval_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryShortGuardInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryShortGuardInterval.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryMaxSpatialStreams_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryMaxSpatialStreams based on Integer32"""
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
        *(("eAuto", 0),
          ("eOne", 1),
          ("eTwo", 2),
          ("eThree", 3),
          ("eFour", 4))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryMaxSpatialStreams_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryMaxSpatialStreams_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryMaxSpatialStreams = _LcosLXStatusWLANManagementNetworkprofilesEntryMaxSpatialStreams_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 25),
    _LcosLXStatusWLANManagementNetworkprofilesEntryMaxSpatialStreams_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryMaxSpatialStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryMaxSpatialStreams.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntrySendAggregates_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntrySendAggregates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntrySendAggregates_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntrySendAggregates_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntrySendAggregates = _LcosLXStatusWLANManagementNetworkprofilesEntrySendAggregates_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 26),
    _LcosLXStatusWLANManagementNetworkprofilesEntrySendAggregates_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntrySendAggregates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntrySendAggregates.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryRADIUSAccounting_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryRADIUSAccounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryRADIUSAccounting_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryRADIUSAccounting_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryRADIUSAccounting = _LcosLXStatusWLANManagementNetworkprofilesEntryRADIUSAccounting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 28),
    _LcosLXStatusWLANManagementNetworkprofilesEntryRADIUSAccounting_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryRADIUSAccounting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryRADIUSAccounting.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryVLANMode_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryVLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eUntagged", 0),
          ("eTagged", 1))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryVLANMode_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryVLANMode_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryVLANMode = _LcosLXStatusWLANManagementNetworkprofilesEntryVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 30),
    _LcosLXStatusWLANManagementNetworkprofilesEntryVLANMode_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryVLANMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryVLANMode.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryVLANId_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryVLANId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryVLANId_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementNetworkprofilesEntryVLANId_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryVLANId = _LcosLXStatusWLANManagementNetworkprofilesEntryVLANId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 34),
    _LcosLXStatusWLANManagementNetworkprofilesEntryVLANId_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryVLANId.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryRADIUSProfile_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryRADIUSProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryRADIUSProfile_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementNetworkprofilesEntryRADIUSProfile_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryRADIUSProfile = _LcosLXStatusWLANManagementNetworkprofilesEntryRADIUSProfile_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 35),
    _LcosLXStatusWLANManagementNetworkprofilesEntryRADIUSProfile_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryRADIUSProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryRADIUSProfile.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryMinClientStrength_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryMinClientStrength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryMinClientStrength_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementNetworkprofilesEntryMinClientStrength_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryMinClientStrength = _LcosLXStatusWLANManagementNetworkprofilesEntryMinClientStrength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 38),
    _LcosLXStatusWLANManagementNetworkprofilesEntryMinClientStrength_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryMinClientStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryMinClientStrength.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryIEEE80211uNetProf_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryIEEE80211uNetProf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryIEEE80211uNetProf_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementNetworkprofilesEntryIEEE80211uNetProf_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryIEEE80211uNetProf = _LcosLXStatusWLANManagementNetworkprofilesEntryIEEE80211uNetProf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 39),
    _LcosLXStatusWLANManagementNetworkprofilesEntryIEEE80211uNetProf_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryIEEE80211uNetProf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryIEEE80211uNetProf.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryOKC_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryOKC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryOKC_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryOKC_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryOKC = _LcosLXStatusWLANManagementNetworkprofilesEntryOKC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 40),
    _LcosLXStatusWLANManagementNetworkprofilesEntryOKC_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryOKC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryOKC.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryWPA2KeyManagement_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryWPA2KeyManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eStandard", 0),
          ("eFastRoaming", 1),
          ("eStandardFastRoaming", 2))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryWPA2KeyManagement_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryWPA2KeyManagement_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryWPA2KeyManagement = _LcosLXStatusWLANManagementNetworkprofilesEntryWPA2KeyManagement_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 41),
    _LcosLXStatusWLANManagementNetworkprofilesEntryWPA2KeyManagement_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryWPA2KeyManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryWPA2KeyManagement.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryAPSD_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryAPSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryAPSD_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryAPSD_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryAPSD = _LcosLXStatusWLANManagementNetworkprofilesEntryAPSD_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 42),
    _LcosLXStatusWLANManagementNetworkprofilesEntryAPSD_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryAPSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryAPSD.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryProtMgmtFrames_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryProtMgmtFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eoptional", 1),
          ("emandatory", 2))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryProtMgmtFrames_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryProtMgmtFrames_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryProtMgmtFrames = _LcosLXStatusWLANManagementNetworkprofilesEntryProtMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 43),
    _LcosLXStatusWLANManagementNetworkprofilesEntryProtMgmtFrames_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryProtMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryProtMgmtFrames.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryTxLimit_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryTxLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryTxLimit_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementNetworkprofilesEntryTxLimit_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryTxLimit = _LcosLXStatusWLANManagementNetworkprofilesEntryTxLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 44),
    _LcosLXStatusWLANManagementNetworkprofilesEntryTxLimit_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryTxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryTxLimit.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryRxLimit_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryRxLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryRxLimit_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementNetworkprofilesEntryRxLimit_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryRxLimit = _LcosLXStatusWLANManagementNetworkprofilesEntryRxLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 45),
    _LcosLXStatusWLANManagementNetworkprofilesEntryRxLimit_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryRxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryRxLimit.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryLBSTracking_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryLBSTracking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryLBSTracking_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryLBSTracking_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryLBSTracking = _LcosLXStatusWLANManagementNetworkprofilesEntryLBSTracking_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 46),
    _LcosLXStatusWLANManagementNetworkprofilesEntryLBSTracking_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryLBSTracking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryLBSTracking.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryLBSTrackingList_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryLBSTrackingList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryLBSTrackingList_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementNetworkprofilesEntryLBSTrackingList_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryLBSTrackingList = _LcosLXStatusWLANManagementNetworkprofilesEntryLBSTrackingList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 47),
    _LcosLXStatusWLANManagementNetworkprofilesEntryLBSTrackingList_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryLBSTrackingList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryLBSTrackingList.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryConverttoUnicast_Type(Bits):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryConverttoUnicast based on Bits"""
    namedValues = NamedValues(
        *(("eDHCP", 0),
          ("eMulticast", 1),
          ("enone", 32))
    )

_LcosLXStatusWLANManagementNetworkprofilesEntryConverttoUnicast_Type.__name__ = "Bits"
_LcosLXStatusWLANManagementNetworkprofilesEntryConverttoUnicast_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryConverttoUnicast = _LcosLXStatusWLANManagementNetworkprofilesEntryConverttoUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 50),
    _LcosLXStatusWLANManagementNetworkprofilesEntryConverttoUnicast_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryConverttoUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryConverttoUnicast.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryTransonlyUnicast_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryTransonlyUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryTransonlyUnicast_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryTransonlyUnicast_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryTransonlyUnicast = _LcosLXStatusWLANManagementNetworkprofilesEntryTransonlyUnicast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 51),
    _LcosLXStatusWLANManagementNetworkprofilesEntryTransonlyUnicast_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryTransonlyUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryTransonlyUnicast.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryWPA23SessKeytypes_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryWPA23SessKeytypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eTKIP", 1),
          ("eAES", 2),
          ("eTKIPAES", 3))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryWPA23SessKeytypes_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryWPA23SessKeytypes_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryWPA23SessKeytypes = _LcosLXStatusWLANManagementNetworkprofilesEntryWPA23SessKeytypes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 53),
    _LcosLXStatusWLANManagementNetworkprofilesEntryWPA23SessKeytypes_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryWPA23SessKeytypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryWPA23SessKeytypes.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryWPA8021XSecLev_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryWPA8021XSecLev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eStandard", 0),
          ("eSuiteB128Bits", 1),
          ("eSuiteB192Bits", 2))
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryWPA8021XSecLev_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementNetworkprofilesEntryWPA8021XSecLev_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryWPA8021XSecLev = _LcosLXStatusWLANManagementNetworkprofilesEntryWPA8021XSecLev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 54),
    _LcosLXStatusWLANManagementNetworkprofilesEntryWPA8021XSecLev_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryWPA8021XSecLev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryWPA8021XSecLev.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryPerClientTxLimit_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryPerClientTxLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryPerClientTxLimit_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementNetworkprofilesEntryPerClientTxLimit_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryPerClientTxLimit = _LcosLXStatusWLANManagementNetworkprofilesEntryPerClientTxLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 55),
    _LcosLXStatusWLANManagementNetworkprofilesEntryPerClientTxLimit_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryPerClientTxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryPerClientTxLimit.setStatus("current")


class _LcosLXStatusWLANManagementNetworkprofilesEntryPerClientRxLimit_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementNetworkprofilesEntryPerClientRxLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusWLANManagementNetworkprofilesEntryPerClientRxLimit_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementNetworkprofilesEntryPerClientRxLimit_Object = MibTableColumn
lcosLXStatusWLANManagementNetworkprofilesEntryPerClientRxLimit = _LcosLXStatusWLANManagementNetworkprofilesEntryPerClientRxLimit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 103, 1, 56),
    _LcosLXStatusWLANManagementNetworkprofilesEntryPerClientRxLimit_Type()
)
lcosLXStatusWLANManagementNetworkprofilesEntryPerClientRxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementNetworkprofilesEntryPerClientRxLimit.setStatus("current")
_LcosLXStatusWLANManagementRADIUSProfiles_Object = MibTable
lcosLXStatusWLANManagementRADIUSProfiles = _LcosLXStatusWLANManagementRADIUSProfiles_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 105)
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRADIUSProfiles.setStatus("current")
_LcosLXStatusWLANManagementRADIUSProfilesEntry_Object = MibTableRow
lcosLXStatusWLANManagementRADIUSProfilesEntry = _LcosLXStatusWLANManagementRADIUSProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 105, 1)
)
lcosLXStatusWLANManagementRADIUSProfilesEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusWLANManagementRADIUSProfilesEntryName"),
)
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRADIUSProfilesEntry.setStatus("current")


class _LcosLXStatusWLANManagementRADIUSProfilesEntryName_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementRADIUSProfilesEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANManagementRADIUSProfilesEntryName_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementRADIUSProfilesEntryName_Object = MibTableColumn
lcosLXStatusWLANManagementRADIUSProfilesEntryName = _LcosLXStatusWLANManagementRADIUSProfilesEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 105, 1, 1),
    _LcosLXStatusWLANManagementRADIUSProfilesEntryName_Type()
)
lcosLXStatusWLANManagementRADIUSProfilesEntryName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRADIUSProfilesEntryName.setStatus("current")


class _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountIP_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementRADIUSProfilesEntryAccountIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_LcosLXStatusWLANManagementRADIUSProfilesEntryAccountIP_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementRADIUSProfilesEntryAccountIP_Object = MibTableColumn
lcosLXStatusWLANManagementRADIUSProfilesEntryAccountIP = _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 105, 1, 2),
    _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountIP_Type()
)
lcosLXStatusWLANManagementRADIUSProfilesEntryAccountIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRADIUSProfilesEntryAccountIP.setStatus("current")


class _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountPort_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementRADIUSProfilesEntryAccountPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANManagementRADIUSProfilesEntryAccountPort_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementRADIUSProfilesEntryAccountPort_Object = MibTableColumn
lcosLXStatusWLANManagementRADIUSProfilesEntryAccountPort = _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 105, 1, 3),
    _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountPort_Type()
)
lcosLXStatusWLANManagementRADIUSProfilesEntryAccountPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRADIUSProfilesEntryAccountPort.setStatus("current")


class _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountSecret_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementRADIUSProfilesEntryAccountSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANManagementRADIUSProfilesEntryAccountSecret_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementRADIUSProfilesEntryAccountSecret_Object = MibTableColumn
lcosLXStatusWLANManagementRADIUSProfilesEntryAccountSecret = _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 105, 1, 4),
    _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountSecret_Type()
)
lcosLXStatusWLANManagementRADIUSProfilesEntryAccountSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRADIUSProfilesEntryAccountSecret.setStatus("current")


class _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountLoopback_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementRADIUSProfilesEntryAccountLoopback based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANManagementRADIUSProfilesEntryAccountLoopback_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementRADIUSProfilesEntryAccountLoopback_Object = MibTableColumn
lcosLXStatusWLANManagementRADIUSProfilesEntryAccountLoopback = _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 105, 1, 5),
    _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountLoopback_Type()
)
lcosLXStatusWLANManagementRADIUSProfilesEntryAccountLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRADIUSProfilesEntryAccountLoopback.setStatus("current")


class _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountProtocol_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementRADIUSProfilesEntryAccountProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eRADIUS", 0),
          ("eRADSEC", 1))
    )


_LcosLXStatusWLANManagementRADIUSProfilesEntryAccountProtocol_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementRADIUSProfilesEntryAccountProtocol_Object = MibTableColumn
lcosLXStatusWLANManagementRADIUSProfilesEntryAccountProtocol = _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 105, 1, 6),
    _LcosLXStatusWLANManagementRADIUSProfilesEntryAccountProtocol_Type()
)
lcosLXStatusWLANManagementRADIUSProfilesEntryAccountProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRADIUSProfilesEntryAccountProtocol.setStatus("current")


class _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessIP_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementRADIUSProfilesEntryAccessIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_LcosLXStatusWLANManagementRADIUSProfilesEntryAccessIP_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementRADIUSProfilesEntryAccessIP_Object = MibTableColumn
lcosLXStatusWLANManagementRADIUSProfilesEntryAccessIP = _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessIP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 105, 1, 7),
    _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessIP_Type()
)
lcosLXStatusWLANManagementRADIUSProfilesEntryAccessIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRADIUSProfilesEntryAccessIP.setStatus("current")


class _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessPort_Type(Unsigned32):
    """Custom type lcosLXStatusWLANManagementRADIUSProfilesEntryAccessPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXStatusWLANManagementRADIUSProfilesEntryAccessPort_Type.__name__ = "Unsigned32"
_LcosLXStatusWLANManagementRADIUSProfilesEntryAccessPort_Object = MibTableColumn
lcosLXStatusWLANManagementRADIUSProfilesEntryAccessPort = _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 105, 1, 8),
    _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessPort_Type()
)
lcosLXStatusWLANManagementRADIUSProfilesEntryAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRADIUSProfilesEntryAccessPort.setStatus("current")


class _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessSecret_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementRADIUSProfilesEntryAccessSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANManagementRADIUSProfilesEntryAccessSecret_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementRADIUSProfilesEntryAccessSecret_Object = MibTableColumn
lcosLXStatusWLANManagementRADIUSProfilesEntryAccessSecret = _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 105, 1, 9),
    _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessSecret_Type()
)
lcosLXStatusWLANManagementRADIUSProfilesEntryAccessSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRADIUSProfilesEntryAccessSecret.setStatus("current")


class _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessLoopback_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementRADIUSProfilesEntryAccessLoopback based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusWLANManagementRADIUSProfilesEntryAccessLoopback_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementRADIUSProfilesEntryAccessLoopback_Object = MibTableColumn
lcosLXStatusWLANManagementRADIUSProfilesEntryAccessLoopback = _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 105, 1, 10),
    _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessLoopback_Type()
)
lcosLXStatusWLANManagementRADIUSProfilesEntryAccessLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRADIUSProfilesEntryAccessLoopback.setStatus("current")


class _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessProtocol_Type(Integer32):
    """Custom type lcosLXStatusWLANManagementRADIUSProfilesEntryAccessProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eRADIUS", 0),
          ("eRADSEC", 1))
    )


_LcosLXStatusWLANManagementRADIUSProfilesEntryAccessProtocol_Type.__name__ = "Integer32"
_LcosLXStatusWLANManagementRADIUSProfilesEntryAccessProtocol_Object = MibTableColumn
lcosLXStatusWLANManagementRADIUSProfilesEntryAccessProtocol = _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 105, 1, 11),
    _LcosLXStatusWLANManagementRADIUSProfilesEntryAccessProtocol_Type()
)
lcosLXStatusWLANManagementRADIUSProfilesEntryAccessProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRADIUSProfilesEntryAccessProtocol.setStatus("current")


class _LcosLXStatusWLANManagementRADIUSProfilesEntryBackup_Type(OctetString):
    """Custom type lcosLXStatusWLANManagementRADIUSProfilesEntryBackup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusWLANManagementRADIUSProfilesEntryBackup_Type.__name__ = "OctetString"
_LcosLXStatusWLANManagementRADIUSProfilesEntryBackup_Object = MibTableColumn
lcosLXStatusWLANManagementRADIUSProfilesEntryBackup = _LcosLXStatusWLANManagementRADIUSProfilesEntryBackup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 59, 105, 1, 12),
    _LcosLXStatusWLANManagementRADIUSProfilesEntryBackup_Type()
)
lcosLXStatusWLANManagementRADIUSProfilesEntryBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusWLANManagementRADIUSProfilesEntryBackup.setStatus("current")
_LcosLXStatusIPConfiguration_ObjectIdentity = ObjectIdentity
lcosLXStatusIPConfiguration = _LcosLXStatusIPConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 70)
)
_LcosLXStatusIPConfigurationAddresses_Object = MibTable
lcosLXStatusIPConfigurationAddresses = _LcosLXStatusIPConfigurationAddresses_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 70, 1)
)
if mibBuilder.loadTexts:
    lcosLXStatusIPConfigurationAddresses.setStatus("current")
_LcosLXStatusIPConfigurationAddressesEntry_Object = MibTableRow
lcosLXStatusIPConfigurationAddressesEntry = _LcosLXStatusIPConfigurationAddressesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 70, 1, 1)
)
lcosLXStatusIPConfigurationAddressesEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusIPConfigurationAddressesEntryInterfaceName"),
    (0, "LCOS-LX-MIB", "lcosLXStatusIPConfigurationAddressesEntryIPVersion"),
    (0, "LCOS-LX-MIB", "lcosLXStatusIPConfigurationAddressesEntryAddressSource"),
    (0, "LCOS-LX-MIB", "lcosLXStatusIPConfigurationAddressesEntryAddress"),
)
if mibBuilder.loadTexts:
    lcosLXStatusIPConfigurationAddressesEntry.setStatus("current")


class _LcosLXStatusIPConfigurationAddressesEntryInterfaceName_Type(OctetString):
    """Custom type lcosLXStatusIPConfigurationAddressesEntryInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusIPConfigurationAddressesEntryInterfaceName_Type.__name__ = "OctetString"
_LcosLXStatusIPConfigurationAddressesEntryInterfaceName_Object = MibTableColumn
lcosLXStatusIPConfigurationAddressesEntryInterfaceName = _LcosLXStatusIPConfigurationAddressesEntryInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 70, 1, 1, 1),
    _LcosLXStatusIPConfigurationAddressesEntryInterfaceName_Type()
)
lcosLXStatusIPConfigurationAddressesEntryInterfaceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusIPConfigurationAddressesEntryInterfaceName.setStatus("current")


class _LcosLXStatusIPConfigurationAddressesEntryIPVersion_Type(Integer32):
    """Custom type lcosLXStatusIPConfigurationAddressesEntryIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eIPv4", 1),
          ("eIPv6", 2))
    )


_LcosLXStatusIPConfigurationAddressesEntryIPVersion_Type.__name__ = "Integer32"
_LcosLXStatusIPConfigurationAddressesEntryIPVersion_Object = MibTableColumn
lcosLXStatusIPConfigurationAddressesEntryIPVersion = _LcosLXStatusIPConfigurationAddressesEntryIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 70, 1, 1, 2),
    _LcosLXStatusIPConfigurationAddressesEntryIPVersion_Type()
)
lcosLXStatusIPConfigurationAddressesEntryIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusIPConfigurationAddressesEntryIPVersion.setStatus("current")


class _LcosLXStatusIPConfigurationAddressesEntryAddressSource_Type(Integer32):
    """Custom type lcosLXStatusIPConfigurationAddressesEntryAddressSource based on Integer32"""
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
        *(("eRouterAdvertisement", 1),
          ("eLinkLocal", 2),
          ("eDHCPv6", 3),
          ("eDHCP", 4),
          ("estatic", 5))
    )


_LcosLXStatusIPConfigurationAddressesEntryAddressSource_Type.__name__ = "Integer32"
_LcosLXStatusIPConfigurationAddressesEntryAddressSource_Object = MibTableColumn
lcosLXStatusIPConfigurationAddressesEntryAddressSource = _LcosLXStatusIPConfigurationAddressesEntryAddressSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 70, 1, 1, 3),
    _LcosLXStatusIPConfigurationAddressesEntryAddressSource_Type()
)
lcosLXStatusIPConfigurationAddressesEntryAddressSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusIPConfigurationAddressesEntryAddressSource.setStatus("current")


class _LcosLXStatusIPConfigurationAddressesEntryAddress_Type(OctetString):
    """Custom type lcosLXStatusIPConfigurationAddressesEntryAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_LcosLXStatusIPConfigurationAddressesEntryAddress_Type.__name__ = "OctetString"
_LcosLXStatusIPConfigurationAddressesEntryAddress_Object = MibTableColumn
lcosLXStatusIPConfigurationAddressesEntryAddress = _LcosLXStatusIPConfigurationAddressesEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 70, 1, 1, 4),
    _LcosLXStatusIPConfigurationAddressesEntryAddress_Type()
)
lcosLXStatusIPConfigurationAddressesEntryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusIPConfigurationAddressesEntryAddress.setStatus("current")


class _LcosLXStatusIPConfigurationAddressesEntryGateway_Type(OctetString):
    """Custom type lcosLXStatusIPConfigurationAddressesEntryGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_LcosLXStatusIPConfigurationAddressesEntryGateway_Type.__name__ = "OctetString"
_LcosLXStatusIPConfigurationAddressesEntryGateway_Object = MibTableColumn
lcosLXStatusIPConfigurationAddressesEntryGateway = _LcosLXStatusIPConfigurationAddressesEntryGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 70, 1, 1, 5),
    _LcosLXStatusIPConfigurationAddressesEntryGateway_Type()
)
lcosLXStatusIPConfigurationAddressesEntryGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusIPConfigurationAddressesEntryGateway.setStatus("current")
_LcosLXStatusLMC_ObjectIdentity = ObjectIdentity
lcosLXStatusLMC = _LcosLXStatusLMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98)
)
_LcosLXStatusLMCTransportStatus_Object = MibTable
lcosLXStatusLMCTransportStatus = _LcosLXStatusLMCTransportStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 1)
)
if mibBuilder.loadTexts:
    lcosLXStatusLMCTransportStatus.setStatus("current")
_LcosLXStatusLMCTransportStatusEntry_Object = MibTableRow
lcosLXStatusLMCTransportStatusEntry = _LcosLXStatusLMCTransportStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 1, 1)
)
lcosLXStatusLMCTransportStatusEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusLMCTransportStatusEntryServiceName"),
)
if mibBuilder.loadTexts:
    lcosLXStatusLMCTransportStatusEntry.setStatus("current")


class _LcosLXStatusLMCTransportStatusEntryServiceName_Type(OctetString):
    """Custom type lcosLXStatusLMCTransportStatusEntryServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LcosLXStatusLMCTransportStatusEntryServiceName_Type.__name__ = "OctetString"
_LcosLXStatusLMCTransportStatusEntryServiceName_Object = MibTableColumn
lcosLXStatusLMCTransportStatusEntryServiceName = _LcosLXStatusLMCTransportStatusEntryServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 1, 1, 1),
    _LcosLXStatusLMCTransportStatusEntryServiceName_Type()
)
lcosLXStatusLMCTransportStatusEntryServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusLMCTransportStatusEntryServiceName.setStatus("current")
_LcosLXStatusLMCTransportStatusEntryHTTPRequests_Type = Counter64
_LcosLXStatusLMCTransportStatusEntryHTTPRequests_Object = MibTableColumn
lcosLXStatusLMCTransportStatusEntryHTTPRequests = _LcosLXStatusLMCTransportStatusEntryHTTPRequests_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 1, 1, 2),
    _LcosLXStatusLMCTransportStatusEntryHTTPRequests_Type()
)
lcosLXStatusLMCTransportStatusEntryHTTPRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLMCTransportStatusEntryHTTPRequests.setStatus("current")
_LcosLXStatusLMCTransportStatusEntryHTTPRequestErrors_Type = Counter64
_LcosLXStatusLMCTransportStatusEntryHTTPRequestErrors_Object = MibTableColumn
lcosLXStatusLMCTransportStatusEntryHTTPRequestErrors = _LcosLXStatusLMCTransportStatusEntryHTTPRequestErrors_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 1, 1, 3),
    _LcosLXStatusLMCTransportStatusEntryHTTPRequestErrors_Type()
)
lcosLXStatusLMCTransportStatusEntryHTTPRequestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLMCTransportStatusEntryHTTPRequestErrors.setStatus("current")
_LcosLXStatusLMCTransportStatusEntryTxBytes_Type = Counter64
_LcosLXStatusLMCTransportStatusEntryTxBytes_Object = MibTableColumn
lcosLXStatusLMCTransportStatusEntryTxBytes = _LcosLXStatusLMCTransportStatusEntryTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 1, 1, 4),
    _LcosLXStatusLMCTransportStatusEntryTxBytes_Type()
)
lcosLXStatusLMCTransportStatusEntryTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLMCTransportStatusEntryTxBytes.setStatus("current")
_LcosLXStatusLMCTransportStatusEntryRxBytes_Type = Counter64
_LcosLXStatusLMCTransportStatusEntryRxBytes_Object = MibTableColumn
lcosLXStatusLMCTransportStatusEntryRxBytes = _LcosLXStatusLMCTransportStatusEntryRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 1, 1, 6),
    _LcosLXStatusLMCTransportStatusEntryRxBytes_Type()
)
lcosLXStatusLMCTransportStatusEntryRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLMCTransportStatusEntryRxBytes.setStatus("current")


class _LcosLXStatusLMCCustomerDeviceID_Type(OctetString):
    """Custom type lcosLXStatusLMCCustomerDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_LcosLXStatusLMCCustomerDeviceID_Type.__name__ = "OctetString"
_LcosLXStatusLMCCustomerDeviceID_Object = MibScalar
lcosLXStatusLMCCustomerDeviceID = _LcosLXStatusLMCCustomerDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 5),
    _LcosLXStatusLMCCustomerDeviceID_Type()
)
lcosLXStatusLMCCustomerDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLMCCustomerDeviceID.setStatus("current")


class _LcosLXStatusLMCRoundTripTime_Type(Unsigned32):
    """Custom type lcosLXStatusLMCRoundTripTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusLMCRoundTripTime_Type.__name__ = "Unsigned32"
_LcosLXStatusLMCRoundTripTime_Object = MibScalar
lcosLXStatusLMCRoundTripTime = _LcosLXStatusLMCRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 6),
    _LcosLXStatusLMCRoundTripTime_Type()
)
lcosLXStatusLMCRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLMCRoundTripTime.setStatus("current")


class _LcosLXStatusLMCManagementStatus_Type(Integer32):
    """Custom type lcosLXStatusLMCManagementStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("eNotAuthenticatedwithLMCnoCloudManagement", 0),
          ("eAuthenticatedwithLMCCloudManagementinactive", 1),
          ("eDisabled", 2),
          ("eDisabledByWLC", 3),
          ("eOperating", 4),
          ("eHTTPProtocolError", 5),
          ("eHTTPConnectionError", 6),
          ("eDNSError", 7),
          ("eMemoryError", 8),
          ("eWaitingNotYet", 9),
          ("eRedirect", 10),
          ("eAuthenticationError", 11),
          ("eGenericError", 12),
          ("eCertificateStorageFailed", 13),
          ("eAuthenticatedwithLMCCloudManagementactive", 14),
          ("eCertificateGenerationAborted", 15),
          ("eNoActivationCode", 16))
    )


_LcosLXStatusLMCManagementStatus_Type.__name__ = "Integer32"
_LcosLXStatusLMCManagementStatus_Object = MibScalar
lcosLXStatusLMCManagementStatus = _LcosLXStatusLMCManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 7),
    _LcosLXStatusLMCManagementStatus_Type()
)
lcosLXStatusLMCManagementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLMCManagementStatus.setStatus("current")


class _LcosLXStatusLMCControlStatus_Type(Integer32):
    """Custom type lcosLXStatusLMCControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("eNotAuthenticatedwithLMCnoCloudManagement", 0),
          ("eAuthenticatedwithLMCCloudManagementinactive", 1),
          ("eDisabled", 2),
          ("eDisabledByWLC", 3),
          ("eOperating", 4),
          ("eHTTPProtocolError", 5),
          ("eHTTPConnectionError", 6),
          ("eDNSError", 7),
          ("eMemoryError", 8),
          ("eWaitingNotYet", 9),
          ("eRedirect", 10),
          ("eAuthenticationError", 11),
          ("eGenericError", 12),
          ("eCertificateStorageFailed", 13),
          ("eAuthenticatedwithLMCCloudManagementactive", 14),
          ("eCertificateGenerationAborted", 15),
          ("eNoActivationCode", 16))
    )


_LcosLXStatusLMCControlStatus_Type.__name__ = "Integer32"
_LcosLXStatusLMCControlStatus_Object = MibScalar
lcosLXStatusLMCControlStatus = _LcosLXStatusLMCControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 9),
    _LcosLXStatusLMCControlStatus_Type()
)
lcosLXStatusLMCControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLMCControlStatus.setStatus("current")


class _LcosLXStatusLMCMonitorStatus_Type(Integer32):
    """Custom type lcosLXStatusLMCMonitorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("eNotAuthenticatedwithLMCnoCloudManagement", 0),
          ("eAuthenticatedwithLMCCloudManagementinactive", 1),
          ("eDisabled", 2),
          ("eDisabledByWLC", 3),
          ("eOperating", 4),
          ("eHTTPProtocolError", 5),
          ("eHTTPConnectionError", 6),
          ("eDNSError", 7),
          ("eMemoryError", 8),
          ("eWaitingNotYet", 9),
          ("eRedirect", 10),
          ("eAuthenticationError", 11),
          ("eGenericError", 12),
          ("eCertificateStorageFailed", 13),
          ("eAuthenticatedwithLMCCloudManagementactive", 14),
          ("eCertificateGenerationAborted", 15),
          ("eNoActivationCode", 16))
    )


_LcosLXStatusLMCMonitorStatus_Type.__name__ = "Integer32"
_LcosLXStatusLMCMonitorStatus_Object = MibScalar
lcosLXStatusLMCMonitorStatus = _LcosLXStatusLMCMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 10),
    _LcosLXStatusLMCMonitorStatus_Type()
)
lcosLXStatusLMCMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLMCMonitorStatus.setStatus("current")


class _LcosLXStatusLMCZeroTouchSupport_Type(Integer32):
    """Custom type lcosLXStatusLMCZeroTouchSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusLMCZeroTouchSupport_Type.__name__ = "Integer32"
_LcosLXStatusLMCZeroTouchSupport_Object = MibScalar
lcosLXStatusLMCZeroTouchSupport = _LcosLXStatusLMCZeroTouchSupport_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 12),
    _LcosLXStatusLMCZeroTouchSupport_Type()
)
lcosLXStatusLMCZeroTouchSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLMCZeroTouchSupport.setStatus("current")


class _LcosLXStatusLMCPairingTokenPresent_Type(Integer32):
    """Custom type lcosLXStatusLMCPairingTokenPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusLMCPairingTokenPresent_Type.__name__ = "Integer32"
_LcosLXStatusLMCPairingTokenPresent_Object = MibScalar
lcosLXStatusLMCPairingTokenPresent = _LcosLXStatusLMCPairingTokenPresent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 13),
    _LcosLXStatusLMCPairingTokenPresent_Type()
)
lcosLXStatusLMCPairingTokenPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLMCPairingTokenPresent.setStatus("current")


class _LcosLXStatusLMCConfigModified_Type(Integer32):
    """Custom type lcosLXStatusLMCConfigModified based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXStatusLMCConfigModified_Type.__name__ = "Integer32"
_LcosLXStatusLMCConfigModified_Object = MibScalar
lcosLXStatusLMCConfigModified = _LcosLXStatusLMCConfigModified_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 98, 15),
    _LcosLXStatusLMCConfigModified_Type()
)
lcosLXStatusLMCConfigModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLMCConfigModified.setStatus("current")
_LcosLXStatusLBS_ObjectIdentity = ObjectIdentity
lcosLXStatusLBS = _LcosLXStatusLBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 99)
)
_LcosLXStatusLBSBLEScanResults_Object = MibTable
lcosLXStatusLBSBLEScanResults = _LcosLXStatusLBSBLEScanResults_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 99, 4)
)
if mibBuilder.loadTexts:
    lcosLXStatusLBSBLEScanResults.setStatus("current")
_LcosLXStatusLBSBLEScanResultsEntry_Object = MibTableRow
lcosLXStatusLBSBLEScanResultsEntry = _LcosLXStatusLBSBLEScanResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 99, 4, 1)
)
lcosLXStatusLBSBLEScanResultsEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXStatusLBSBLEScanResultsEntryDeviceAddress"),
)
if mibBuilder.loadTexts:
    lcosLXStatusLBSBLEScanResultsEntry.setStatus("current")


class _LcosLXStatusLBSBLEScanResultsEntryDeviceAddress_Type(OctetString):
    """Custom type lcosLXStatusLBSBLEScanResultsEntryDeviceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LcosLXStatusLBSBLEScanResultsEntryDeviceAddress_Type.__name__ = "OctetString"
_LcosLXStatusLBSBLEScanResultsEntryDeviceAddress_Object = MibTableColumn
lcosLXStatusLBSBLEScanResultsEntryDeviceAddress = _LcosLXStatusLBSBLEScanResultsEntryDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 99, 4, 1, 1),
    _LcosLXStatusLBSBLEScanResultsEntryDeviceAddress_Type()
)
lcosLXStatusLBSBLEScanResultsEntryDeviceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXStatusLBSBLEScanResultsEntryDeviceAddress.setStatus("current")


class _LcosLXStatusLBSBLEScanResultsEntryAddressType_Type(OctetString):
    """Custom type lcosLXStatusLBSBLEScanResultsEntryAddressType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LcosLXStatusLBSBLEScanResultsEntryAddressType_Type.__name__ = "OctetString"
_LcosLXStatusLBSBLEScanResultsEntryAddressType_Object = MibTableColumn
lcosLXStatusLBSBLEScanResultsEntryAddressType = _LcosLXStatusLBSBLEScanResultsEntryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 99, 4, 1, 2),
    _LcosLXStatusLBSBLEScanResultsEntryAddressType_Type()
)
lcosLXStatusLBSBLEScanResultsEntryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLBSBLEScanResultsEntryAddressType.setStatus("current")


class _LcosLXStatusLBSBLEScanResultsEntryRSSI_Type(Integer32):
    """Custom type lcosLXStatusLBSBLEScanResultsEntryRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_LcosLXStatusLBSBLEScanResultsEntryRSSI_Type.__name__ = "Integer32"
_LcosLXStatusLBSBLEScanResultsEntryRSSI_Object = MibTableColumn
lcosLXStatusLBSBLEScanResultsEntryRSSI = _LcosLXStatusLBSBLEScanResultsEntryRSSI_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 99, 4, 1, 3),
    _LcosLXStatusLBSBLEScanResultsEntryRSSI_Type()
)
lcosLXStatusLBSBLEScanResultsEntryRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLBSBLEScanResultsEntryRSSI.setStatus("current")


class _LcosLXStatusLBSBLEScanResultsEntryLastSeen_Type(OctetString):
    """Custom type lcosLXStatusLBSBLEScanResultsEntryLastSeen based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXStatusLBSBLEScanResultsEntryLastSeen_Type.__name__ = "OctetString"
_LcosLXStatusLBSBLEScanResultsEntryLastSeen_Object = MibTableColumn
lcosLXStatusLBSBLEScanResultsEntryLastSeen = _LcosLXStatusLBSBLEScanResultsEntryLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 99, 4, 1, 4),
    _LcosLXStatusLBSBLEScanResultsEntryLastSeen_Type()
)
lcosLXStatusLBSBLEScanResultsEntryLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLBSBLEScanResultsEntryLastSeen.setStatus("current")


class _LcosLXStatusLBSBLEScanResultsEntryAdvertisingData_Type(OctetString):
    """Custom type lcosLXStatusLBSBLEScanResultsEntryAdvertisingData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusLBSBLEScanResultsEntryAdvertisingData_Type.__name__ = "OctetString"
_LcosLXStatusLBSBLEScanResultsEntryAdvertisingData_Object = MibTableColumn
lcosLXStatusLBSBLEScanResultsEntryAdvertisingData = _LcosLXStatusLBSBLEScanResultsEntryAdvertisingData_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 99, 4, 1, 5),
    _LcosLXStatusLBSBLEScanResultsEntryAdvertisingData_Type()
)
lcosLXStatusLBSBLEScanResultsEntryAdvertisingData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLBSBLEScanResultsEntryAdvertisingData.setStatus("current")


class _LcosLXStatusLBSBLEScanResultsEntryScanResponseData_Type(OctetString):
    """Custom type lcosLXStatusLBSBLEScanResultsEntryScanResponseData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusLBSBLEScanResultsEntryScanResponseData_Type.__name__ = "OctetString"
_LcosLXStatusLBSBLEScanResultsEntryScanResponseData_Object = MibTableColumn
lcosLXStatusLBSBLEScanResultsEntryScanResponseData = _LcosLXStatusLBSBLEScanResultsEntryScanResponseData_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 99, 4, 1, 6),
    _LcosLXStatusLBSBLEScanResultsEntryScanResponseData_Type()
)
lcosLXStatusLBSBLEScanResultsEntryScanResponseData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLBSBLEScanResultsEntryScanResponseData.setStatus("current")


class _LcosLXStatusLBSBLEScanResultsEntryManufacturer_Type(OctetString):
    """Custom type lcosLXStatusLBSBLEScanResultsEntryManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LcosLXStatusLBSBLEScanResultsEntryManufacturer_Type.__name__ = "OctetString"
_LcosLXStatusLBSBLEScanResultsEntryManufacturer_Object = MibTableColumn
lcosLXStatusLBSBLEScanResultsEntryManufacturer = _LcosLXStatusLBSBLEScanResultsEntryManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 99, 4, 1, 7),
    _LcosLXStatusLBSBLEScanResultsEntryManufacturer_Type()
)
lcosLXStatusLBSBLEScanResultsEntryManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLBSBLEScanResultsEntryManufacturer.setStatus("current")


class _LcosLXStatusLBSBLEScanResultsEntryLocalNameType_Type(Integer32):
    """Custom type lcosLXStatusLBSBLEScanResultsEntryLocalNameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNone", 0),
          ("eShortened", 1),
          ("eComplete", 2))
    )


_LcosLXStatusLBSBLEScanResultsEntryLocalNameType_Type.__name__ = "Integer32"
_LcosLXStatusLBSBLEScanResultsEntryLocalNameType_Object = MibTableColumn
lcosLXStatusLBSBLEScanResultsEntryLocalNameType = _LcosLXStatusLBSBLEScanResultsEntryLocalNameType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 99, 4, 1, 8),
    _LcosLXStatusLBSBLEScanResultsEntryLocalNameType_Type()
)
lcosLXStatusLBSBLEScanResultsEntryLocalNameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLBSBLEScanResultsEntryLocalNameType.setStatus("current")


class _LcosLXStatusLBSBLEScanResultsEntryASCIILocalName_Type(OctetString):
    """Custom type lcosLXStatusLBSBLEScanResultsEntryASCIILocalName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LcosLXStatusLBSBLEScanResultsEntryASCIILocalName_Type.__name__ = "OctetString"
_LcosLXStatusLBSBLEScanResultsEntryASCIILocalName_Object = MibTableColumn
lcosLXStatusLBSBLEScanResultsEntryASCIILocalName = _LcosLXStatusLBSBLEScanResultsEntryASCIILocalName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 99, 4, 1, 9),
    _LcosLXStatusLBSBLEScanResultsEntryASCIILocalName_Type()
)
lcosLXStatusLBSBLEScanResultsEntryASCIILocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLBSBLEScanResultsEntryASCIILocalName.setStatus("current")


class _LcosLXStatusLBSCACertinfo_Type(OctetString):
    """Custom type lcosLXStatusLBSCACertinfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_LcosLXStatusLBSCACertinfo_Type.__name__ = "OctetString"
_LcosLXStatusLBSCACertinfo_Object = MibScalar
lcosLXStatusLBSCACertinfo = _LcosLXStatusLBSCACertinfo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 99, 5),
    _LcosLXStatusLBSCACertinfo_Type()
)
lcosLXStatusLBSCACertinfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusLBSCACertinfo.setStatus("current")
_LcosLXStatusAutomaticFirmwareUpdate_ObjectIdentity = ObjectIdentity
lcosLXStatusAutomaticFirmwareUpdate = _LcosLXStatusAutomaticFirmwareUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 107)
)


class _LcosLXStatusAutomaticFirmwareUpdateMode_Type(Integer32):
    """Custom type lcosLXStatusAutomaticFirmwareUpdateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emanual", 0),
          ("echeck", 1),
          ("echeckandupdate", 2))
    )


_LcosLXStatusAutomaticFirmwareUpdateMode_Type.__name__ = "Integer32"
_LcosLXStatusAutomaticFirmwareUpdateMode_Object = MibScalar
lcosLXStatusAutomaticFirmwareUpdateMode = _LcosLXStatusAutomaticFirmwareUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 107, 1),
    _LcosLXStatusAutomaticFirmwareUpdateMode_Type()
)
lcosLXStatusAutomaticFirmwareUpdateMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusAutomaticFirmwareUpdateMode.setStatus("current")


class _LcosLXStatusAutomaticFirmwareUpdateLastCheck_Type(OctetString):
    """Custom type lcosLXStatusAutomaticFirmwareUpdateLastCheck based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_LcosLXStatusAutomaticFirmwareUpdateLastCheck_Type.__name__ = "OctetString"
_LcosLXStatusAutomaticFirmwareUpdateLastCheck_Object = MibScalar
lcosLXStatusAutomaticFirmwareUpdateLastCheck = _LcosLXStatusAutomaticFirmwareUpdateLastCheck_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 107, 2),
    _LcosLXStatusAutomaticFirmwareUpdateLastCheck_Type()
)
lcosLXStatusAutomaticFirmwareUpdateLastCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusAutomaticFirmwareUpdateLastCheck.setStatus("current")


class _LcosLXStatusAutomaticFirmwareUpdateNextCheck_Type(OctetString):
    """Custom type lcosLXStatusAutomaticFirmwareUpdateNextCheck based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_LcosLXStatusAutomaticFirmwareUpdateNextCheck_Type.__name__ = "OctetString"
_LcosLXStatusAutomaticFirmwareUpdateNextCheck_Object = MibScalar
lcosLXStatusAutomaticFirmwareUpdateNextCheck = _LcosLXStatusAutomaticFirmwareUpdateNextCheck_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 107, 3),
    _LcosLXStatusAutomaticFirmwareUpdateNextCheck_Type()
)
lcosLXStatusAutomaticFirmwareUpdateNextCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusAutomaticFirmwareUpdateNextCheck.setStatus("current")


class _LcosLXStatusAutomaticFirmwareUpdateUpdateCandidate_Type(OctetString):
    """Custom type lcosLXStatusAutomaticFirmwareUpdateUpdateCandidate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_LcosLXStatusAutomaticFirmwareUpdateUpdateCandidate_Type.__name__ = "OctetString"
_LcosLXStatusAutomaticFirmwareUpdateUpdateCandidate_Object = MibScalar
lcosLXStatusAutomaticFirmwareUpdateUpdateCandidate = _LcosLXStatusAutomaticFirmwareUpdateUpdateCandidate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 107, 4),
    _LcosLXStatusAutomaticFirmwareUpdateUpdateCandidate_Type()
)
lcosLXStatusAutomaticFirmwareUpdateUpdateCandidate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusAutomaticFirmwareUpdateUpdateCandidate.setStatus("current")


class _LcosLXStatusAutomaticFirmwareUpdateState_Type(Integer32):
    """Custom type lcosLXStatusAutomaticFirmwareUpdateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("eclosed", 0),
          ("eclosing", 1),
          ("ecancel", 2),
          ("eidle", 3),
          ("einitializing", 4),
          ("eworking", 5),
          ("etesting", 6),
          ("erequesting", 7),
          ("econtactingupdateserver", 8),
          ("eprocessingresponse", 9),
          ("edownloading", 10),
          ("everifyingdownload", 11),
          ("einstalling", 12),
          ("ereboot", 13),
          ("econtinueinstallation", 14),
          ("eprepareverifyinginstallation", 15),
          ("everifyinginstallation", 16),
          ("eresetting", 17),
          ("ewaiting", 18),
          ("ewaitingforinstallation", 19))
    )


_LcosLXStatusAutomaticFirmwareUpdateState_Type.__name__ = "Integer32"
_LcosLXStatusAutomaticFirmwareUpdateState_Object = MibScalar
lcosLXStatusAutomaticFirmwareUpdateState = _LcosLXStatusAutomaticFirmwareUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 107, 5),
    _LcosLXStatusAutomaticFirmwareUpdateState_Type()
)
lcosLXStatusAutomaticFirmwareUpdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusAutomaticFirmwareUpdateState.setStatus("current")


class _LcosLXStatusAutomaticFirmwareUpdateCurrentAction_Type(Integer32):
    """Custom type lcosLXStatusAutomaticFirmwareUpdateCurrentAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("enone", 0),
          ("estartup", 1),
          ("eautomaticupdatecheck", 2),
          ("emanualupdatecheck", 3),
          ("eautomaticupdate", 4),
          ("emanualupdate", 5),
          ("ereset", 6))
    )


_LcosLXStatusAutomaticFirmwareUpdateCurrentAction_Type.__name__ = "Integer32"
_LcosLXStatusAutomaticFirmwareUpdateCurrentAction_Object = MibScalar
lcosLXStatusAutomaticFirmwareUpdateCurrentAction = _LcosLXStatusAutomaticFirmwareUpdateCurrentAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 107, 6),
    _LcosLXStatusAutomaticFirmwareUpdateCurrentAction_Type()
)
lcosLXStatusAutomaticFirmwareUpdateCurrentAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusAutomaticFirmwareUpdateCurrentAction.setStatus("current")


class _LcosLXStatusAutomaticFirmwareUpdateLastResult_Type(Integer32):
    """Custom type lcosLXStatusAutomaticFirmwareUpdateLastResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              501,
              502,
              503,
              504)
        )
    )
    namedValues = NamedValues(
        *(("eOK", 0),
          ("eunknownerroroccured", 30),
          ("eactioncancelledbyuser", 31),
          ("efailedtoloadupdateserverresponse", 32),
          ("einvalidupdateserverresponse", 33),
          ("eupdateservererror", 34),
          ("einternallogicerror", 35),
          ("einternalmissingdataerror", 36),
          ("einternalprocessingerror", 37),
          ("eupdatefilechecksuminvalid", 38),
          ("eupdateinstallationfailed", 39),
          ("esystemrebootedunexpectedly", 40),
          ("ewrongactionhasbeendetectedwithingivencontext", 41),
          ("ewrongstatehasbeendetectedwithingivencontext", 42),
          ("eupdateserverofferedblacklistedfirmware", 43),
          ("efirmwareverificationfailedretrying", 44),
          ("efirmwareverificationfailed", 45),
          ("efirmwareinstallationfailed", 46),
          ("erepeatedupdatesearchhasfailed", 47),
          ("eupdateserverunavailable", 48),
          ("eupdateserverbusyrepeating", 49),
          ("eupdateserverrepeatedlybusy", 50),
          ("eupdateserverbusyretrylater", 51),
          ("eactioncancelledoutoftimerange", 52),
          ("eactioncancelledbyupdateinstallation", 53),
          ("eactioncancelledbyrequest", 54),
          ("efailedtoqueueaction", 55),
          ("efirmwarefallback", 56),
          ("eactioncancelledbyconfigchange", 57),
          ("eactioncancelledbyshutdown", 58),
          ("eunknowndownloaderroroccured", 300),
          ("eserverurlinvalid", 301),
          ("edownloadfailedinvalidtarget", 302),
          ("efailedtocreatedownloadtask", 303),
          ("efailedtorequestdownload", 304),
          ("efailedtowritedownloadtofile", 305),
          ("efailedtoopendownloadfile", 306),
          ("edownloadcancelled", 307),
          ("edownloadtimeout", 308),
          ("efailedtoconnecttotheserver", 309),
          ("edownloadprotocolerror", 310),
          ("ednserror", 311),
          ("eoutofmemory", 312),
          ("etoomanyconnections", 313),
          ("etruststorenotavailable", 314),
          ("esecureconnectionfailed", 315),
          ("efailedtoattachdownloadeventhandles", 316),
          ("efailedtoreaddownloadstream", 317),
          ("eupdateserveremptyerror", 401),
          ("eserverresponsemismatchesinitialrequest", 402),
          ("eserverresponseidmismatch", 403),
          ("eserverresponseheaderincomplete", 404),
          ("eserverresponsehasinvalidstructure", 405),
          ("eserverresponseinvalid", 406),
          ("eserverresponsebodyincomplete", 407),
          ("einternalparametererror", 408),
          ("eunsupportedfirmwaretypeprovided", 409),
          ("ewritingmainconfigurationhasfailed", 501),
          ("einvalidmainconfiguration", 502),
          ("emodifyingmainconfigurationfailed", 503),
          ("emodifyingblacklistfailed", 504))
    )


_LcosLXStatusAutomaticFirmwareUpdateLastResult_Type.__name__ = "Integer32"
_LcosLXStatusAutomaticFirmwareUpdateLastResult_Object = MibScalar
lcosLXStatusAutomaticFirmwareUpdateLastResult = _LcosLXStatusAutomaticFirmwareUpdateLastResult_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 107, 7),
    _LcosLXStatusAutomaticFirmwareUpdateLastResult_Type()
)
lcosLXStatusAutomaticFirmwareUpdateLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusAutomaticFirmwareUpdateLastResult.setStatus("current")


class _LcosLXStatusAutomaticFirmwareUpdatePlannedInstallation_Type(OctetString):
    """Custom type lcosLXStatusAutomaticFirmwareUpdatePlannedInstallation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_LcosLXStatusAutomaticFirmwareUpdatePlannedInstallation_Type.__name__ = "OctetString"
_LcosLXStatusAutomaticFirmwareUpdatePlannedInstallation_Object = MibScalar
lcosLXStatusAutomaticFirmwareUpdatePlannedInstallation = _LcosLXStatusAutomaticFirmwareUpdatePlannedInstallation_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 107, 8),
    _LcosLXStatusAutomaticFirmwareUpdatePlannedInstallation_Type()
)
lcosLXStatusAutomaticFirmwareUpdatePlannedInstallation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusAutomaticFirmwareUpdatePlannedInstallation.setStatus("current")


class _LcosLXStatusAutomaticFirmwareUpdateCurrentVersion_Type(OctetString):
    """Custom type lcosLXStatusAutomaticFirmwareUpdateCurrentVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_LcosLXStatusAutomaticFirmwareUpdateCurrentVersion_Type.__name__ = "OctetString"
_LcosLXStatusAutomaticFirmwareUpdateCurrentVersion_Object = MibScalar
lcosLXStatusAutomaticFirmwareUpdateCurrentVersion = _LcosLXStatusAutomaticFirmwareUpdateCurrentVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 107, 12),
    _LcosLXStatusAutomaticFirmwareUpdateCurrentVersion_Type()
)
lcosLXStatusAutomaticFirmwareUpdateCurrentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusAutomaticFirmwareUpdateCurrentVersion.setStatus("current")


class _LcosLXStatusAutomaticFirmwareUpdateLastCheckEpoch_Type(Unsigned32):
    """Custom type lcosLXStatusAutomaticFirmwareUpdateLastCheckEpoch based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusAutomaticFirmwareUpdateLastCheckEpoch_Type.__name__ = "Unsigned32"
_LcosLXStatusAutomaticFirmwareUpdateLastCheckEpoch_Object = MibScalar
lcosLXStatusAutomaticFirmwareUpdateLastCheckEpoch = _LcosLXStatusAutomaticFirmwareUpdateLastCheckEpoch_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 107, 102),
    _LcosLXStatusAutomaticFirmwareUpdateLastCheckEpoch_Type()
)
lcosLXStatusAutomaticFirmwareUpdateLastCheckEpoch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusAutomaticFirmwareUpdateLastCheckEpoch.setStatus("current")


class _LcosLXStatusAutomaticFirmwareUpdateNextCheckEpoch_Type(Unsigned32):
    """Custom type lcosLXStatusAutomaticFirmwareUpdateNextCheckEpoch based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusAutomaticFirmwareUpdateNextCheckEpoch_Type.__name__ = "Unsigned32"
_LcosLXStatusAutomaticFirmwareUpdateNextCheckEpoch_Object = MibScalar
lcosLXStatusAutomaticFirmwareUpdateNextCheckEpoch = _LcosLXStatusAutomaticFirmwareUpdateNextCheckEpoch_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 107, 103),
    _LcosLXStatusAutomaticFirmwareUpdateNextCheckEpoch_Type()
)
lcosLXStatusAutomaticFirmwareUpdateNextCheckEpoch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusAutomaticFirmwareUpdateNextCheckEpoch.setStatus("current")


class _LcosLXStatusAutomaticFirmwareUpdatePlannedInstallationEpoch_Type(Unsigned32):
    """Custom type lcosLXStatusAutomaticFirmwareUpdatePlannedInstallationEpoch based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusAutomaticFirmwareUpdatePlannedInstallationEpoch_Type.__name__ = "Unsigned32"
_LcosLXStatusAutomaticFirmwareUpdatePlannedInstallationEpoch_Object = MibScalar
lcosLXStatusAutomaticFirmwareUpdatePlannedInstallationEpoch = _LcosLXStatusAutomaticFirmwareUpdatePlannedInstallationEpoch_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 107, 108),
    _LcosLXStatusAutomaticFirmwareUpdatePlannedInstallationEpoch_Type()
)
lcosLXStatusAutomaticFirmwareUpdatePlannedInstallationEpoch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusAutomaticFirmwareUpdatePlannedInstallationEpoch.setStatus("current")
_LcosLXStatusIoT_ObjectIdentity = ObjectIdentity
lcosLXStatusIoT = _LcosLXStatusIoT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 111)
)
_LcosLXStatusIoTWirelessePaper_ObjectIdentity = ObjectIdentity
lcosLXStatusIoTWirelessePaper = _LcosLXStatusIoTWirelessePaper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 111, 88)
)


class _LcosLXStatusIoTWirelessePaperServerCAInfo_Type(OctetString):
    """Custom type lcosLXStatusIoTWirelessePaperServerCAInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_LcosLXStatusIoTWirelessePaperServerCAInfo_Type.__name__ = "OctetString"
_LcosLXStatusIoTWirelessePaperServerCAInfo_Object = MibScalar
lcosLXStatusIoTWirelessePaperServerCAInfo = _LcosLXStatusIoTWirelessePaperServerCAInfo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 111, 88, 1),
    _LcosLXStatusIoTWirelessePaperServerCAInfo_Type()
)
lcosLXStatusIoTWirelessePaperServerCAInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusIoTWirelessePaperServerCAInfo.setStatus("current")


class _LcosLXStatusIoTWirelessePaperAccessPointID_Type(Unsigned32):
    """Custom type lcosLXStatusIoTWirelessePaperAccessPointID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXStatusIoTWirelessePaperAccessPointID_Type.__name__ = "Unsigned32"
_LcosLXStatusIoTWirelessePaperAccessPointID_Object = MibScalar
lcosLXStatusIoTWirelessePaperAccessPointID = _LcosLXStatusIoTWirelessePaperAccessPointID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 111, 88, 2),
    _LcosLXStatusIoTWirelessePaperAccessPointID_Type()
)
lcosLXStatusIoTWirelessePaperAccessPointID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusIoTWirelessePaperAccessPointID.setStatus("current")


class _LcosLXStatusIoTWirelessePaperConnectedServer_Type(OctetString):
    """Custom type lcosLXStatusIoTWirelessePaperConnectedServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusIoTWirelessePaperConnectedServer_Type.__name__ = "OctetString"
_LcosLXStatusIoTWirelessePaperConnectedServer_Object = MibScalar
lcosLXStatusIoTWirelessePaperConnectedServer = _LcosLXStatusIoTWirelessePaperConnectedServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 111, 88, 3),
    _LcosLXStatusIoTWirelessePaperConnectedServer_Type()
)
lcosLXStatusIoTWirelessePaperConnectedServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusIoTWirelessePaperConnectedServer.setStatus("current")


class _LcosLXStatusIoTWirelessePaperCurrentChannel_Type(Integer32):
    """Custom type lcosLXStatusIoTWirelessePaperCurrentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e2404MHz", 0),
          ("e2410MHz", 1),
          ("e2422MHz", 2),
          ("e2425MHz", 3),
          ("e2442MHz", 4),
          ("e2450MHz", 5),
          ("e2462MHz", 6),
          ("e2470MHz", 7),
          ("e2474MHz", 8),
          ("e2477MHz", 9),
          ("e2480MHz", 10),
          ("eNone", 255))
    )


_LcosLXStatusIoTWirelessePaperCurrentChannel_Type.__name__ = "Integer32"
_LcosLXStatusIoTWirelessePaperCurrentChannel_Object = MibScalar
lcosLXStatusIoTWirelessePaperCurrentChannel = _LcosLXStatusIoTWirelessePaperCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 111, 88, 4),
    _LcosLXStatusIoTWirelessePaperCurrentChannel_Type()
)
lcosLXStatusIoTWirelessePaperCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusIoTWirelessePaperCurrentChannel.setStatus("current")


class _LcosLXStatusIoTWirelessePaperFirmwareVersion_Type(OctetString):
    """Custom type lcosLXStatusIoTWirelessePaperFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXStatusIoTWirelessePaperFirmwareVersion_Type.__name__ = "OctetString"
_LcosLXStatusIoTWirelessePaperFirmwareVersion_Object = MibScalar
lcosLXStatusIoTWirelessePaperFirmwareVersion = _LcosLXStatusIoTWirelessePaperFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 111, 88, 5),
    _LcosLXStatusIoTWirelessePaperFirmwareVersion_Type()
)
lcosLXStatusIoTWirelessePaperFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusIoTWirelessePaperFirmwareVersion.setStatus("current")


class _LcosLXStatusIoTWirelessePaperClaimID_Type(OctetString):
    """Custom type lcosLXStatusIoTWirelessePaperClaimID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LcosLXStatusIoTWirelessePaperClaimID_Type.__name__ = "OctetString"
_LcosLXStatusIoTWirelessePaperClaimID_Object = MibScalar
lcosLXStatusIoTWirelessePaperClaimID = _LcosLXStatusIoTWirelessePaperClaimID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 1, 111, 88, 6),
    _LcosLXStatusIoTWirelessePaperClaimID_Type()
)
lcosLXStatusIoTWirelessePaperClaimID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXStatusIoTWirelessePaperClaimID.setStatus("current")
_LcosLXSetup_ObjectIdentity = ObjectIdentity
lcosLXSetup = _LcosLXSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2)
)


class _LcosLXSetupName_Type(OctetString):
    """Custom type lcosLXSetupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupName_Type.__name__ = "OctetString"
_LcosLXSetupName_Object = MibScalar
lcosLXSetupName = _LcosLXSetupName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 1),
    _LcosLXSetupName_Type()
)
lcosLXSetupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupName.setStatus("current")
_LcosLXSetupConfig_ObjectIdentity = ObjectIdentity
lcosLXSetupConfig = _LcosLXSetupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11)
)


class _LcosLXSetupConfigComment1_Type(OctetString):
    """Custom type lcosLXSetupConfigComment1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcosLXSetupConfigComment1_Type.__name__ = "OctetString"
_LcosLXSetupConfigComment1_Object = MibScalar
lcosLXSetupConfigComment1 = _LcosLXSetupConfigComment1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 1),
    _LcosLXSetupConfigComment1_Type()
)
lcosLXSetupConfigComment1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigComment1.setStatus("current")


class _LcosLXSetupConfigComment2_Type(OctetString):
    """Custom type lcosLXSetupConfigComment2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcosLXSetupConfigComment2_Type.__name__ = "OctetString"
_LcosLXSetupConfigComment2_Object = MibScalar
lcosLXSetupConfigComment2 = _LcosLXSetupConfigComment2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 2),
    _LcosLXSetupConfigComment2_Type()
)
lcosLXSetupConfigComment2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigComment2.setStatus("current")


class _LcosLXSetupConfigComment3_Type(OctetString):
    """Custom type lcosLXSetupConfigComment3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcosLXSetupConfigComment3_Type.__name__ = "OctetString"
_LcosLXSetupConfigComment3_Object = MibScalar
lcosLXSetupConfigComment3 = _LcosLXSetupConfigComment3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 3),
    _LcosLXSetupConfigComment3_Type()
)
lcosLXSetupConfigComment3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigComment3.setStatus("current")


class _LcosLXSetupConfigComment4_Type(OctetString):
    """Custom type lcosLXSetupConfigComment4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcosLXSetupConfigComment4_Type.__name__ = "OctetString"
_LcosLXSetupConfigComment4_Object = MibScalar
lcosLXSetupConfigComment4 = _LcosLXSetupConfigComment4_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 4),
    _LcosLXSetupConfigComment4_Type()
)
lcosLXSetupConfigComment4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigComment4.setStatus("current")


class _LcosLXSetupConfigComment5_Type(OctetString):
    """Custom type lcosLXSetupConfigComment5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcosLXSetupConfigComment5_Type.__name__ = "OctetString"
_LcosLXSetupConfigComment5_Object = MibScalar
lcosLXSetupConfigComment5 = _LcosLXSetupConfigComment5_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 5),
    _LcosLXSetupConfigComment5_Type()
)
lcosLXSetupConfigComment5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigComment5.setStatus("current")


class _LcosLXSetupConfigComment6_Type(OctetString):
    """Custom type lcosLXSetupConfigComment6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcosLXSetupConfigComment6_Type.__name__ = "OctetString"
_LcosLXSetupConfigComment6_Object = MibScalar
lcosLXSetupConfigComment6 = _LcosLXSetupConfigComment6_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 6),
    _LcosLXSetupConfigComment6_Type()
)
lcosLXSetupConfigComment6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigComment6.setStatus("current")


class _LcosLXSetupConfigComment7_Type(OctetString):
    """Custom type lcosLXSetupConfigComment7 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcosLXSetupConfigComment7_Type.__name__ = "OctetString"
_LcosLXSetupConfigComment7_Object = MibScalar
lcosLXSetupConfigComment7 = _LcosLXSetupConfigComment7_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 7),
    _LcosLXSetupConfigComment7_Type()
)
lcosLXSetupConfigComment7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigComment7.setStatus("current")


class _LcosLXSetupConfigComment8_Type(OctetString):
    """Custom type lcosLXSetupConfigComment8 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcosLXSetupConfigComment8_Type.__name__ = "OctetString"
_LcosLXSetupConfigComment8_Object = MibScalar
lcosLXSetupConfigComment8 = _LcosLXSetupConfigComment8_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 8),
    _LcosLXSetupConfigComment8_Type()
)
lcosLXSetupConfigComment8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigComment8.setStatus("current")


class _LcosLXSetupConfigLocation_Type(OctetString):
    """Custom type lcosLXSetupConfigLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcosLXSetupConfigLocation_Type.__name__ = "OctetString"
_LcosLXSetupConfigLocation_Object = MibScalar
lcosLXSetupConfigLocation = _LcosLXSetupConfigLocation_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 9),
    _LcosLXSetupConfigLocation_Type()
)
lcosLXSetupConfigLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigLocation.setStatus("current")


class _LcosLXSetupConfigAdministrator_Type(OctetString):
    """Custom type lcosLXSetupConfigAdministrator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcosLXSetupConfigAdministrator_Type.__name__ = "OctetString"
_LcosLXSetupConfigAdministrator_Object = MibScalar
lcosLXSetupConfigAdministrator = _LcosLXSetupConfigAdministrator_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 10),
    _LcosLXSetupConfigAdministrator_Type()
)
lcosLXSetupConfigAdministrator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigAdministrator.setStatus("current")


class _LcosLXSetupConfigConfigAgingMinutes_Type(Unsigned32):
    """Custom type lcosLXSetupConfigConfigAgingMinutes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupConfigConfigAgingMinutes_Type.__name__ = "Unsigned32"
_LcosLXSetupConfigConfigAgingMinutes_Object = MibScalar
lcosLXSetupConfigConfigAgingMinutes = _LcosLXSetupConfigConfigAgingMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 11),
    _LcosLXSetupConfigConfigAgingMinutes_Type()
)
lcosLXSetupConfigConfigAgingMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigConfigAgingMinutes.setStatus("current")


class _LcosLXSetupConfigLEDMode_Type(Integer32):
    """Custom type lcosLXSetupConfigLEDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOn", 0),
          ("eOff", 1),
          ("eTimedOff", 2))
    )


_LcosLXSetupConfigLEDMode_Type.__name__ = "Integer32"
_LcosLXSetupConfigLEDMode_Object = MibScalar
lcosLXSetupConfigLEDMode = _LcosLXSetupConfigLEDMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 18),
    _LcosLXSetupConfigLEDMode_Type()
)
lcosLXSetupConfigLEDMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigLEDMode.setStatus("current")
_LcosLXSetupConfigAdmins_Object = MibTable
lcosLXSetupConfigAdmins = _LcosLXSetupConfigAdmins_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 21)
)
if mibBuilder.loadTexts:
    lcosLXSetupConfigAdmins.setStatus("current")
_LcosLXSetupConfigAdminsEntry_Object = MibTableRow
lcosLXSetupConfigAdminsEntry = _LcosLXSetupConfigAdminsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 21, 1)
)
lcosLXSetupConfigAdminsEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupConfigAdminsEntryAdministrator"),
)
if mibBuilder.loadTexts:
    lcosLXSetupConfigAdminsEntry.setStatus("current")


class _LcosLXSetupConfigAdminsEntryAdministrator_Type(OctetString):
    """Custom type lcosLXSetupConfigAdminsEntryAdministrator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LcosLXSetupConfigAdminsEntryAdministrator_Type.__name__ = "OctetString"
_LcosLXSetupConfigAdminsEntryAdministrator_Object = MibTableColumn
lcosLXSetupConfigAdminsEntryAdministrator = _LcosLXSetupConfigAdminsEntryAdministrator_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 21, 1, 1),
    _LcosLXSetupConfigAdminsEntryAdministrator_Type()
)
lcosLXSetupConfigAdminsEntryAdministrator.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupConfigAdminsEntryAdministrator.setStatus("current")


class _LcosLXSetupConfigAdminsEntryFunctionRights_Type(Bits):
    """Custom type lcosLXSetupConfigAdminsEntryFunctionRights based on Bits"""
    namedValues = NamedValues(
        *(("eBasic", 0),
          ("eAdminManagement", 31))
    )

_LcosLXSetupConfigAdminsEntryFunctionRights_Type.__name__ = "Bits"
_LcosLXSetupConfigAdminsEntryFunctionRights_Object = MibTableColumn
lcosLXSetupConfigAdminsEntryFunctionRights = _LcosLXSetupConfigAdminsEntryFunctionRights_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 21, 1, 3),
    _LcosLXSetupConfigAdminsEntryFunctionRights_Type()
)
lcosLXSetupConfigAdminsEntryFunctionRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigAdminsEntryFunctionRights.setStatus("current")


class _LcosLXSetupConfigAdminsEntryRights_Type(Integer32):
    """Custom type lcosLXSetupConfigAdminsEntryRights based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eNone", 0),
          ("eAdminROLimit", 1),
          ("eAdminRWLimit", 2),
          ("eAdminRO", 3),
          ("eAdminRW", 4),
          ("eSupervisor", 5))
    )


_LcosLXSetupConfigAdminsEntryRights_Type.__name__ = "Integer32"
_LcosLXSetupConfigAdminsEntryRights_Object = MibTableColumn
lcosLXSetupConfigAdminsEntryRights = _LcosLXSetupConfigAdminsEntryRights_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 21, 1, 5),
    _LcosLXSetupConfigAdminsEntryRights_Type()
)
lcosLXSetupConfigAdminsEntryRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigAdminsEntryRights.setStatus("current")


class _LcosLXSetupConfigAdminsEntryHashedPassword_Type(OctetString):
    """Custom type lcosLXSetupConfigAdminsEntryHashedPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcosLXSetupConfigAdminsEntryHashedPassword_Type.__name__ = "OctetString"
_LcosLXSetupConfigAdminsEntryHashedPassword_Object = MibTableColumn
lcosLXSetupConfigAdminsEntryHashedPassword = _LcosLXSetupConfigAdminsEntryHashedPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 21, 1, 6),
    _LcosLXSetupConfigAdminsEntryHashedPassword_Type()
)
lcosLXSetupConfigAdminsEntryHashedPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigAdminsEntryHashedPassword.setStatus("current")


class _LcosLXSetupConfigLEDOffSeconds_Type(Unsigned32):
    """Custom type lcosLXSetupConfigLEDOffSeconds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupConfigLEDOffSeconds_Type.__name__ = "Unsigned32"
_LcosLXSetupConfigLEDOffSeconds_Object = MibScalar
lcosLXSetupConfigLEDOffSeconds = _LcosLXSetupConfigLEDOffSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 90),
    _LcosLXSetupConfigLEDOffSeconds_Type()
)
lcosLXSetupConfigLEDOffSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigLEDOffSeconds.setStatus("current")


class _LcosLXSetupConfigLEDTest_Type(Integer32):
    """Custom type lcosLXSetupConfigLEDTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 0),
          ("eRed", 1),
          ("eGreen", 2),
          ("eBlue", 3),
          ("eAll", 4),
          ("eNoTest", 255))
    )


_LcosLXSetupConfigLEDTest_Type.__name__ = "Integer32"
_LcosLXSetupConfigLEDTest_Object = MibScalar
lcosLXSetupConfigLEDTest = _LcosLXSetupConfigLEDTest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 91),
    _LcosLXSetupConfigLEDTest_Type()
)
lcosLXSetupConfigLEDTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigLEDTest.setStatus("current")


class _LcosLXSetupConfigAllowSupportAccess_Type(Integer32):
    """Custom type lcosLXSetupConfigAllowSupportAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupConfigAllowSupportAccess_Type.__name__ = "Integer32"
_LcosLXSetupConfigAllowSupportAccess_Object = MibScalar
lcosLXSetupConfigAllowSupportAccess = _LcosLXSetupConfigAllowSupportAccess_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 11, 129),
    _LcosLXSetupConfigAllowSupportAccess_Type()
)
lcosLXSetupConfigAllowSupportAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupConfigAllowSupportAccess.setStatus("current")
_LcosLXSetupTime_ObjectIdentity = ObjectIdentity
lcosLXSetupTime = _LcosLXSetupTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 14)
)


class _LcosLXSetupTimeTimezone_Type(Integer32):
    """Custom type lcosLXSetupTimeTimezone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("eUTC", 0),
          ("eEuropeBerlin", 1),
          ("eEuropeVienna", 2),
          ("eEuropeZurich", 3),
          ("eEuropeLondon", 4),
          ("eEuropePrague", 5),
          ("eEuropeWarsaw", 6),
          ("eEuropeZagreb", 7),
          ("eEuropeCopenhagen", 8),
          ("eEuropeParis", 9),
          ("eEuropeHelsinki", 10),
          ("eEuropeTallinn", 11),
          ("eEuropeAthens", 12),
          ("eEuropeBudapest", 13),
          ("eEuropeDublin", 14),
          ("eEuropeRome", 15),
          ("eEuropeRiga", 16),
          ("eEuropeVilnius", 17),
          ("eEuropeLuxembourg", 18),
          ("eEuropeMalta", 19),
          ("eEuropeAmsterdam", 20),
          ("eEuropeNicosia", 21),
          ("eEuropeLisbon", 22),
          ("eEuropeBucharest", 23),
          ("eEuropeBratislava", 24),
          ("eEuropeLjubljana", 25),
          ("eEuropeMadrid", 26),
          ("eEuropeStockholm", 27),
          ("eEuropeBrussels", 28),
          ("eEuropeSofia", 29),
          ("eUSAlaska", 30),
          ("eUSPacific", 31),
          ("eUSMountain", 32),
          ("eUSCentral", 33),
          ("eUSEastern", 34),
          ("ePacificAuckland", 35),
          ("ePacificHonolulu", 36),
          ("eAustraliaBrisbane", 37),
          ("eAustraliaSydney", 38),
          ("eAustraliaPerth", 39),
          ("eAustraliaDarwin", 40),
          ("eAustraliaAdelaide", 41))
    )


_LcosLXSetupTimeTimezone_Type.__name__ = "Integer32"
_LcosLXSetupTimeTimezone_Object = MibScalar
lcosLXSetupTimeTimezone = _LcosLXSetupTimeTimezone_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 14, 20),
    _LcosLXSetupTimeTimezone_Type()
)
lcosLXSetupTimeTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupTimeTimezone.setStatus("current")
_LcosLXSetupTimeNTP_ObjectIdentity = ObjectIdentity
lcosLXSetupTimeNTP = _LcosLXSetupTimeNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 14, 21)
)


class _LcosLXSetupTimeNTPOperating_Type(Integer32):
    """Custom type lcosLXSetupTimeNTPOperating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupTimeNTPOperating_Type.__name__ = "Integer32"
_LcosLXSetupTimeNTPOperating_Object = MibScalar
lcosLXSetupTimeNTPOperating = _LcosLXSetupTimeNTPOperating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 14, 21, 1),
    _LcosLXSetupTimeNTPOperating_Type()
)
lcosLXSetupTimeNTPOperating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupTimeNTPOperating.setStatus("current")


class _LcosLXSetupTimeNTPServer_Type(OctetString):
    """Custom type lcosLXSetupTimeNTPServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupTimeNTPServer_Type.__name__ = "OctetString"
_LcosLXSetupTimeNTPServer_Object = MibScalar
lcosLXSetupTimeNTPServer = _LcosLXSetupTimeNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 14, 21, 2),
    _LcosLXSetupTimeNTPServer_Type()
)
lcosLXSetupTimeNTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupTimeNTPServer.setStatus("current")
_LcosLXSetupTimeNTPServers_Object = MibTable
lcosLXSetupTimeNTPServers = _LcosLXSetupTimeNTPServers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 14, 21, 3)
)
if mibBuilder.loadTexts:
    lcosLXSetupTimeNTPServers.setStatus("current")
_LcosLXSetupTimeNTPServersEntry_Object = MibTableRow
lcosLXSetupTimeNTPServersEntry = _LcosLXSetupTimeNTPServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 14, 21, 3, 1)
)
lcosLXSetupTimeNTPServersEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupTimeNTPServersEntryName"),
)
if mibBuilder.loadTexts:
    lcosLXSetupTimeNTPServersEntry.setStatus("current")


class _LcosLXSetupTimeNTPServersEntryName_Type(OctetString):
    """Custom type lcosLXSetupTimeNTPServersEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupTimeNTPServersEntryName_Type.__name__ = "OctetString"
_LcosLXSetupTimeNTPServersEntryName_Object = MibTableColumn
lcosLXSetupTimeNTPServersEntryName = _LcosLXSetupTimeNTPServersEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 14, 21, 3, 1, 1),
    _LcosLXSetupTimeNTPServersEntryName_Type()
)
lcosLXSetupTimeNTPServersEntryName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupTimeNTPServersEntryName.setStatus("current")


class _LcosLXSetupTimeNTPServersEntryActive_Type(Integer32):
    """Custom type lcosLXSetupTimeNTPServersEntryActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupTimeNTPServersEntryActive_Type.__name__ = "Integer32"
_LcosLXSetupTimeNTPServersEntryActive_Object = MibTableColumn
lcosLXSetupTimeNTPServersEntryActive = _LcosLXSetupTimeNTPServersEntryActive_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 14, 21, 3, 1, 2),
    _LcosLXSetupTimeNTPServersEntryActive_Type()
)
lcosLXSetupTimeNTPServersEntryActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupTimeNTPServersEntryActive.setStatus("current")
_LcosLXSetupWLAN_ObjectIdentity = ObjectIdentity
lcosLXSetupWLAN = _LcosLXSetupWLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20)
)
_LcosLXSetupWLANNetwork_Object = MibTable
lcosLXSetupWLANNetwork = _LcosLXSetupWLANNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1)
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetwork.setStatus("current")
_LcosLXSetupWLANNetworkEntry_Object = MibTableRow
lcosLXSetupWLANNetworkEntry = _LcosLXSetupWLANNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1)
)
lcosLXSetupWLANNetworkEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupWLANNetworkEntryNetworkName"),
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntry.setStatus("current")


class _LcosLXSetupWLANNetworkEntryNetworkName_Type(OctetString):
    """Custom type lcosLXSetupWLANNetworkEntryNetworkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupWLANNetworkEntryNetworkName_Type.__name__ = "OctetString"
_LcosLXSetupWLANNetworkEntryNetworkName_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryNetworkName = _LcosLXSetupWLANNetworkEntryNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 1),
    _LcosLXSetupWLANNetworkEntryNetworkName_Type()
)
lcosLXSetupWLANNetworkEntryNetworkName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryNetworkName.setStatus("current")


class _LcosLXSetupWLANNetworkEntrySSIDName_Type(OctetString):
    """Custom type lcosLXSetupWLANNetworkEntrySSIDName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXSetupWLANNetworkEntrySSIDName_Type.__name__ = "OctetString"
_LcosLXSetupWLANNetworkEntrySSIDName_Object = MibTableColumn
lcosLXSetupWLANNetworkEntrySSIDName = _LcosLXSetupWLANNetworkEntrySSIDName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 2),
    _LcosLXSetupWLANNetworkEntrySSIDName_Type()
)
lcosLXSetupWLANNetworkEntrySSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntrySSIDName.setStatus("current")


class _LcosLXSetupWLANNetworkEntryClosedNetwork_Type(Integer32):
    """Custom type lcosLXSetupWLANNetworkEntryClosedNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupWLANNetworkEntryClosedNetwork_Type.__name__ = "Integer32"
_LcosLXSetupWLANNetworkEntryClosedNetwork_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryClosedNetwork = _LcosLXSetupWLANNetworkEntryClosedNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 4),
    _LcosLXSetupWLANNetworkEntryClosedNetwork_Type()
)
lcosLXSetupWLANNetworkEntryClosedNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryClosedNetwork.setStatus("current")


class _LcosLXSetupWLANNetworkEntryMaxStations_Type(Unsigned32):
    """Custom type lcosLXSetupWLANNetworkEntryMaxStations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupWLANNetworkEntryMaxStations_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANNetworkEntryMaxStations_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryMaxStations = _LcosLXSetupWLANNetworkEntryMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 10),
    _LcosLXSetupWLANNetworkEntryMaxStations_Type()
)
lcosLXSetupWLANNetworkEntryMaxStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryMaxStations.setStatus("current")


class _LcosLXSetupWLANNetworkEntryInterStationTraffic_Type(Integer32):
    """Custom type lcosLXSetupWLANNetworkEntryInterStationTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupWLANNetworkEntryInterStationTraffic_Type.__name__ = "Integer32"
_LcosLXSetupWLANNetworkEntryInterStationTraffic_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryInterStationTraffic = _LcosLXSetupWLANNetworkEntryInterStationTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 13),
    _LcosLXSetupWLANNetworkEntryInterStationTraffic_Type()
)
lcosLXSetupWLANNetworkEntryInterStationTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryInterStationTraffic.setStatus("current")


class _LcosLXSetupWLANNetworkEntryMinClientStrength_Type(Unsigned32):
    """Custom type lcosLXSetupWLANNetworkEntryMinClientStrength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXSetupWLANNetworkEntryMinClientStrength_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANNetworkEntryMinClientStrength_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryMinClientStrength = _LcosLXSetupWLANNetworkEntryMinClientStrength_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 16),
    _LcosLXSetupWLANNetworkEntryMinClientStrength_Type()
)
lcosLXSetupWLANNetworkEntryMinClientStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryMinClientStrength.setStatus("current")


class _LcosLXSetupWLANNetworkEntryExcludeFromClientManagement_Type(Integer32):
    """Custom type lcosLXSetupWLANNetworkEntryExcludeFromClientManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupWLANNetworkEntryExcludeFromClientManagement_Type.__name__ = "Integer32"
_LcosLXSetupWLANNetworkEntryExcludeFromClientManagement_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryExcludeFromClientManagement = _LcosLXSetupWLANNetworkEntryExcludeFromClientManagement_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 17),
    _LcosLXSetupWLANNetworkEntryExcludeFromClientManagement_Type()
)
lcosLXSetupWLANNetworkEntryExcludeFromClientManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryExcludeFromClientManagement.setStatus("current")


class _LcosLXSetupWLANNetworkEntryTimeframe_Type(OctetString):
    """Custom type lcosLXSetupWLANNetworkEntryTimeframe based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LcosLXSetupWLANNetworkEntryTimeframe_Type.__name__ = "OctetString"
_LcosLXSetupWLANNetworkEntryTimeframe_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryTimeframe = _LcosLXSetupWLANNetworkEntryTimeframe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 18),
    _LcosLXSetupWLANNetworkEntryTimeframe_Type()
)
lcosLXSetupWLANNetworkEntryTimeframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryTimeframe.setStatus("current")


class _LcosLXSetupWLANNetworkEntryHotspot_Type(OctetString):
    """Custom type lcosLXSetupWLANNetworkEntryHotspot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXSetupWLANNetworkEntryHotspot_Type.__name__ = "OctetString"
_LcosLXSetupWLANNetworkEntryHotspot_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryHotspot = _LcosLXSetupWLANNetworkEntryHotspot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 19),
    _LcosLXSetupWLANNetworkEntryHotspot_Type()
)
lcosLXSetupWLANNetworkEntryHotspot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryHotspot.setStatus("current")


class _LcosLXSetupWLANNetworkEntrySummaricTxLimitKbits_Type(Unsigned32):
    """Custom type lcosLXSetupWLANNetworkEntrySummaricTxLimitKbits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANNetworkEntrySummaricTxLimitKbits_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANNetworkEntrySummaricTxLimitKbits_Object = MibTableColumn
lcosLXSetupWLANNetworkEntrySummaricTxLimitKbits = _LcosLXSetupWLANNetworkEntrySummaricTxLimitKbits_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 20),
    _LcosLXSetupWLANNetworkEntrySummaricTxLimitKbits_Type()
)
lcosLXSetupWLANNetworkEntrySummaricTxLimitKbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntrySummaricTxLimitKbits.setStatus("current")


class _LcosLXSetupWLANNetworkEntrySummaricRxLimitKbits_Type(Unsigned32):
    """Custom type lcosLXSetupWLANNetworkEntrySummaricRxLimitKbits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANNetworkEntrySummaricRxLimitKbits_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANNetworkEntrySummaricRxLimitKbits_Object = MibTableColumn
lcosLXSetupWLANNetworkEntrySummaricRxLimitKbits = _LcosLXSetupWLANNetworkEntrySummaricRxLimitKbits_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 21),
    _LcosLXSetupWLANNetworkEntrySummaricRxLimitKbits_Type()
)
lcosLXSetupWLANNetworkEntrySummaricRxLimitKbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntrySummaricRxLimitKbits.setStatus("current")


class _LcosLXSetupWLANNetworkEntryBlockMulticast_Type(Integer32):
    """Custom type lcosLXSetupWLANNetworkEntryBlockMulticast based on Integer32"""
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
        *(("eNo", 0),
          ("eIPv4only", 1),
          ("eIPv6only", 2),
          ("eBoth", 3))
    )


_LcosLXSetupWLANNetworkEntryBlockMulticast_Type.__name__ = "Integer32"
_LcosLXSetupWLANNetworkEntryBlockMulticast_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryBlockMulticast = _LcosLXSetupWLANNetworkEntryBlockMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 25),
    _LcosLXSetupWLANNetworkEntryBlockMulticast_Type()
)
lcosLXSetupWLANNetworkEntryBlockMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryBlockMulticast.setStatus("current")


class _LcosLXSetupWLANNetworkEntryClientTxLimitKbits_Type(Unsigned32):
    """Custom type lcosLXSetupWLANNetworkEntryClientTxLimitKbits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANNetworkEntryClientTxLimitKbits_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANNetworkEntryClientTxLimitKbits_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryClientTxLimitKbits = _LcosLXSetupWLANNetworkEntryClientTxLimitKbits_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 26),
    _LcosLXSetupWLANNetworkEntryClientTxLimitKbits_Type()
)
lcosLXSetupWLANNetworkEntryClientTxLimitKbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryClientTxLimitKbits.setStatus("current")


class _LcosLXSetupWLANNetworkEntryClientRxLimitKbits_Type(Unsigned32):
    """Custom type lcosLXSetupWLANNetworkEntryClientRxLimitKbits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANNetworkEntryClientRxLimitKbits_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANNetworkEntryClientRxLimitKbits_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryClientRxLimitKbits = _LcosLXSetupWLANNetworkEntryClientRxLimitKbits_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 27),
    _LcosLXSetupWLANNetworkEntryClientRxLimitKbits_Type()
)
lcosLXSetupWLANNetworkEntryClientRxLimitKbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryClientRxLimitKbits.setStatus("current")


class _LcosLXSetupWLANNetworkEntryKey_Type(OctetString):
    """Custom type lcosLXSetupWLANNetworkEntryKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LcosLXSetupWLANNetworkEntryKey_Type.__name__ = "OctetString"
_LcosLXSetupWLANNetworkEntryKey_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryKey = _LcosLXSetupWLANNetworkEntryKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 100),
    _LcosLXSetupWLANNetworkEntryKey_Type()
)
lcosLXSetupWLANNetworkEntryKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryKey.setStatus("current")


class _LcosLXSetupWLANNetworkEntryRadios_Type(Integer32):
    """Custom type lcosLXSetupWLANNetworkEntryRadios based on Integer32"""
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
        *(("e24GHz5GHz", 1),
          ("e24GHz", 2),
          ("e5GHz", 3),
          ("enone", 4))
    )


_LcosLXSetupWLANNetworkEntryRadios_Type.__name__ = "Integer32"
_LcosLXSetupWLANNetworkEntryRadios_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryRadios = _LcosLXSetupWLANNetworkEntryRadios_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 101),
    _LcosLXSetupWLANNetworkEntryRadios_Type()
)
lcosLXSetupWLANNetworkEntryRadios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryRadios.setStatus("current")


class _LcosLXSetupWLANNetworkEntryEncryptionProfile_Type(OctetString):
    """Custom type lcosLXSetupWLANNetworkEntryEncryptionProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LcosLXSetupWLANNetworkEntryEncryptionProfile_Type.__name__ = "OctetString"
_LcosLXSetupWLANNetworkEntryEncryptionProfile_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryEncryptionProfile = _LcosLXSetupWLANNetworkEntryEncryptionProfile_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 102),
    _LcosLXSetupWLANNetworkEntryEncryptionProfile_Type()
)
lcosLXSetupWLANNetworkEntryEncryptionProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryEncryptionProfile.setStatus("current")


class _LcosLXSetupWLANNetworkEntryIdleTimeout_Type(Unsigned32):
    """Custom type lcosLXSetupWLANNetworkEntryIdleTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupWLANNetworkEntryIdleTimeout_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANNetworkEntryIdleTimeout_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryIdleTimeout = _LcosLXSetupWLANNetworkEntryIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 103),
    _LcosLXSetupWLANNetworkEntryIdleTimeout_Type()
)
lcosLXSetupWLANNetworkEntryIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryIdleTimeout.setStatus("current")


class _LcosLXSetupWLANNetworkEntryVLANID_Type(Unsigned32):
    """Custom type lcosLXSetupWLANNetworkEntryVLANID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupWLANNetworkEntryVLANID_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANNetworkEntryVLANID_Object = MibTableColumn
lcosLXSetupWLANNetworkEntryVLANID = _LcosLXSetupWLANNetworkEntryVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1, 1, 200),
    _LcosLXSetupWLANNetworkEntryVLANID_Type()
)
lcosLXSetupWLANNetworkEntryVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANNetworkEntryVLANID.setStatus("current")


class _LcosLXSetupWLANCountry_Type(Integer32):
    """Custom type lcosLXSetupWLANCountry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(36,
              40,
              56,
              100,
              191,
              196,
              203,
              208,
              233,
              246,
              250,
              276,
              300,
              348,
              372,
              380,
              428,
              440,
              442,
              470,
              528,
              554,
              616,
              620,
              642,
              703,
              705,
              724,
              752,
              756,
              826,
              840,
              998)
        )
    )
    namedValues = NamedValues(
        *(("eAustralia", 36),
          ("eAustria", 40),
          ("eBelgium", 56),
          ("eBulgaria", 100),
          ("eCroatia", 191),
          ("eCyprus", 196),
          ("eCzechRepublic", 203),
          ("eDenmark", 208),
          ("eEstonia", 233),
          ("eFinland", 246),
          ("eFrance", 250),
          ("eGermany", 276),
          ("eGreece", 300),
          ("eHungary", 348),
          ("eIreland", 372),
          ("eItaly", 380),
          ("eLatvia", 428),
          ("eLithuania", 440),
          ("eLuxembourg", 442),
          ("eMalta", 470),
          ("eNetherlands", 528),
          ("eNewZealand", 554),
          ("ePoland", 616),
          ("ePortugal", 620),
          ("eRomania", 642),
          ("eSlovakia", 703),
          ("eSlovenia", 705),
          ("eSpain", 724),
          ("eSweden", 752),
          ("eSwitzerland", 756),
          ("eUnitedKingdom", 826),
          ("eUnitedStates", 840),
          ("eEurope", 998))
    )


_LcosLXSetupWLANCountry_Type.__name__ = "Integer32"
_LcosLXSetupWLANCountry_Object = MibScalar
lcosLXSetupWLANCountry = _LcosLXSetupWLANCountry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 2),
    _LcosLXSetupWLANCountry_Type()
)
lcosLXSetupWLANCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANCountry.setStatus("current")
_LcosLXSetupWLANEncryption_Object = MibTable
lcosLXSetupWLANEncryption = _LcosLXSetupWLANEncryption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3)
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryption.setStatus("current")
_LcosLXSetupWLANEncryptionEntry_Object = MibTableRow
lcosLXSetupWLANEncryptionEntry = _LcosLXSetupWLANEncryptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1)
)
lcosLXSetupWLANEncryptionEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupWLANEncryptionEntryProfileName"),
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntry.setStatus("current")


class _LcosLXSetupWLANEncryptionEntryProfileName_Type(OctetString):
    """Custom type lcosLXSetupWLANEncryptionEntryProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LcosLXSetupWLANEncryptionEntryProfileName_Type.__name__ = "OctetString"
_LcosLXSetupWLANEncryptionEntryProfileName_Object = MibTableColumn
lcosLXSetupWLANEncryptionEntryProfileName = _LcosLXSetupWLANEncryptionEntryProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1, 1),
    _LcosLXSetupWLANEncryptionEntryProfileName_Type()
)
lcosLXSetupWLANEncryptionEntryProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntryProfileName.setStatus("current")


class _LcosLXSetupWLANEncryptionEntryEncryption_Type(Integer32):
    """Custom type lcosLXSetupWLANEncryptionEntryEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupWLANEncryptionEntryEncryption_Type.__name__ = "Integer32"
_LcosLXSetupWLANEncryptionEntryEncryption_Object = MibTableColumn
lcosLXSetupWLANEncryptionEntryEncryption = _LcosLXSetupWLANEncryptionEntryEncryption_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1, 2),
    _LcosLXSetupWLANEncryptionEntryEncryption_Type()
)
lcosLXSetupWLANEncryptionEntryEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntryEncryption.setStatus("current")


class _LcosLXSetupWLANEncryptionEntryMethod_Type(Integer32):
    """Custom type lcosLXSetupWLANEncryptionEntryMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              13,
              16,
              32,
              33,
              34,
              35,
              36,
              37,
              38)
        )
    )
    namedValues = NamedValues(
        *(("eWEP40Bits", 5),
          ("eWEP104Bits", 13),
          ("eWEP128Bits", 16),
          ("e80211iWPAPSK", 32),
          ("e80211iWPA8021X", 33),
          ("eWEP40Bits8021X", 34),
          ("eWEP104Bits8021X", 35),
          ("eWEP128Bits8021X", 36),
          ("eEnhancedOpen", 37),
          ("e80211iWPA8021X192Bits", 38))
    )


_LcosLXSetupWLANEncryptionEntryMethod_Type.__name__ = "Integer32"
_LcosLXSetupWLANEncryptionEntryMethod_Object = MibTableColumn
lcosLXSetupWLANEncryptionEntryMethod = _LcosLXSetupWLANEncryptionEntryMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1, 4),
    _LcosLXSetupWLANEncryptionEntryMethod_Type()
)
lcosLXSetupWLANEncryptionEntryMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntryMethod.setStatus("current")


class _LcosLXSetupWLANEncryptionEntryWPAVersion_Type(Integer32):
    """Custom type lcosLXSetupWLANEncryptionEntryWPAVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              8,
              12)
        )
    )
    namedValues = NamedValues(
        *(("eWPA1", 2),
          ("eWPA2", 4),
          ("eWPA12", 6),
          ("eWPA3", 8),
          ("eWPA23", 12))
    )


_LcosLXSetupWLANEncryptionEntryWPAVersion_Type.__name__ = "Integer32"
_LcosLXSetupWLANEncryptionEntryWPAVersion_Object = MibTableColumn
lcosLXSetupWLANEncryptionEntryWPAVersion = _LcosLXSetupWLANEncryptionEntryWPAVersion_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1, 9),
    _LcosLXSetupWLANEncryptionEntryWPAVersion_Type()
)
lcosLXSetupWLANEncryptionEntryWPAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntryWPAVersion.setStatus("current")


class _LcosLXSetupWLANEncryptionEntryWPARekeyingCycle_Type(Unsigned32):
    """Custom type lcosLXSetupWLANEncryptionEntryWPARekeyingCycle based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANEncryptionEntryWPARekeyingCycle_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANEncryptionEntryWPARekeyingCycle_Object = MibTableColumn
lcosLXSetupWLANEncryptionEntryWPARekeyingCycle = _LcosLXSetupWLANEncryptionEntryWPARekeyingCycle_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1, 11),
    _LcosLXSetupWLANEncryptionEntryWPARekeyingCycle_Type()
)
lcosLXSetupWLANEncryptionEntryWPARekeyingCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntryWPARekeyingCycle.setStatus("current")


class _LcosLXSetupWLANEncryptionEntryWPA1SessionKeytypes_Type(Integer32):
    """Custom type lcosLXSetupWLANEncryptionEntryWPA1SessionKeytypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eTKIP", 1),
          ("eAES", 2),
          ("eTKIPAES", 3))
    )


_LcosLXSetupWLANEncryptionEntryWPA1SessionKeytypes_Type.__name__ = "Integer32"
_LcosLXSetupWLANEncryptionEntryWPA1SessionKeytypes_Object = MibTableColumn
lcosLXSetupWLANEncryptionEntryWPA1SessionKeytypes = _LcosLXSetupWLANEncryptionEntryWPA1SessionKeytypes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1, 12),
    _LcosLXSetupWLANEncryptionEntryWPA1SessionKeytypes_Type()
)
lcosLXSetupWLANEncryptionEntryWPA1SessionKeytypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntryWPA1SessionKeytypes.setStatus("current")


class _LcosLXSetupWLANEncryptionEntryWPA23SessionKeytypes_Type(Integer32):
    """Custom type lcosLXSetupWLANEncryptionEntryWPA23SessionKeytypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eTKIP", 1),
          ("eAES", 2),
          ("eTKIPAES", 3))
    )


_LcosLXSetupWLANEncryptionEntryWPA23SessionKeytypes_Type.__name__ = "Integer32"
_LcosLXSetupWLANEncryptionEntryWPA23SessionKeytypes_Object = MibTableColumn
lcosLXSetupWLANEncryptionEntryWPA23SessionKeytypes = _LcosLXSetupWLANEncryptionEntryWPA23SessionKeytypes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1, 13),
    _LcosLXSetupWLANEncryptionEntryWPA23SessionKeytypes_Type()
)
lcosLXSetupWLANEncryptionEntryWPA23SessionKeytypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntryWPA23SessionKeytypes.setStatus("current")


class _LcosLXSetupWLANEncryptionEntryProtMgmtFrames_Type(Integer32):
    """Custom type lcosLXSetupWLANEncryptionEntryProtMgmtFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eoptional", 1),
          ("emandatory", 2))
    )


_LcosLXSetupWLANEncryptionEntryProtMgmtFrames_Type.__name__ = "Integer32"
_LcosLXSetupWLANEncryptionEntryProtMgmtFrames_Object = MibTableColumn
lcosLXSetupWLANEncryptionEntryProtMgmtFrames = _LcosLXSetupWLANEncryptionEntryProtMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1, 14),
    _LcosLXSetupWLANEncryptionEntryProtMgmtFrames_Type()
)
lcosLXSetupWLANEncryptionEntryProtMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntryProtMgmtFrames.setStatus("current")


class _LcosLXSetupWLANEncryptionEntryPreAuthentication_Type(Integer32):
    """Custom type lcosLXSetupWLANEncryptionEntryPreAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupWLANEncryptionEntryPreAuthentication_Type.__name__ = "Integer32"
_LcosLXSetupWLANEncryptionEntryPreAuthentication_Object = MibTableColumn
lcosLXSetupWLANEncryptionEntryPreAuthentication = _LcosLXSetupWLANEncryptionEntryPreAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1, 16),
    _LcosLXSetupWLANEncryptionEntryPreAuthentication_Type()
)
lcosLXSetupWLANEncryptionEntryPreAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntryPreAuthentication.setStatus("current")


class _LcosLXSetupWLANEncryptionEntryOKC_Type(Integer32):
    """Custom type lcosLXSetupWLANEncryptionEntryOKC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupWLANEncryptionEntryOKC_Type.__name__ = "Integer32"
_LcosLXSetupWLANEncryptionEntryOKC_Object = MibTableColumn
lcosLXSetupWLANEncryptionEntryOKC = _LcosLXSetupWLANEncryptionEntryOKC_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1, 17),
    _LcosLXSetupWLANEncryptionEntryOKC_Type()
)
lcosLXSetupWLANEncryptionEntryOKC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntryOKC.setStatus("current")


class _LcosLXSetupWLANEncryptionEntryWPA2KeyManagement_Type(Integer32):
    """Custom type lcosLXSetupWLANEncryptionEntryWPA2KeyManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eStandard", 0),
          ("eFastRoaming", 1),
          ("eStandardFastRoaming", 2))
    )


_LcosLXSetupWLANEncryptionEntryWPA2KeyManagement_Type.__name__ = "Integer32"
_LcosLXSetupWLANEncryptionEntryWPA2KeyManagement_Object = MibTableColumn
lcosLXSetupWLANEncryptionEntryWPA2KeyManagement = _LcosLXSetupWLANEncryptionEntryWPA2KeyManagement_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1, 19),
    _LcosLXSetupWLANEncryptionEntryWPA2KeyManagement_Type()
)
lcosLXSetupWLANEncryptionEntryWPA2KeyManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntryWPA2KeyManagement.setStatus("current")


class _LcosLXSetupWLANEncryptionEntryPMKIAPPSecret_Type(OctetString):
    """Custom type lcosLXSetupWLANEncryptionEntryPMKIAPPSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupWLANEncryptionEntryPMKIAPPSecret_Type.__name__ = "OctetString"
_LcosLXSetupWLANEncryptionEntryPMKIAPPSecret_Object = MibTableColumn
lcosLXSetupWLANEncryptionEntryPMKIAPPSecret = _LcosLXSetupWLANEncryptionEntryPMKIAPPSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1, 20),
    _LcosLXSetupWLANEncryptionEntryPMKIAPPSecret_Type()
)
lcosLXSetupWLANEncryptionEntryPMKIAPPSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntryPMKIAPPSecret.setStatus("current")


class _LcosLXSetupWLANEncryptionEntryRADIUSServerProfile_Type(OctetString):
    """Custom type lcosLXSetupWLANEncryptionEntryRADIUSServerProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupWLANEncryptionEntryRADIUSServerProfile_Type.__name__ = "OctetString"
_LcosLXSetupWLANEncryptionEntryRADIUSServerProfile_Object = MibTableColumn
lcosLXSetupWLANEncryptionEntryRADIUSServerProfile = _LcosLXSetupWLANEncryptionEntryRADIUSServerProfile_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1, 21),
    _LcosLXSetupWLANEncryptionEntryRADIUSServerProfile_Type()
)
lcosLXSetupWLANEncryptionEntryRADIUSServerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntryRADIUSServerProfile.setStatus("current")


class _LcosLXSetupWLANEncryptionEntrySAEOWEGroups_Type(Bits):
    """Custom type lcosLXSetupWLANEncryptionEntrySAEOWEGroups based on Bits"""
    namedValues = NamedValues(
        *(("eDH19", 19),
          ("eDH20", 20),
          ("eDH21", 21))
    )

_LcosLXSetupWLANEncryptionEntrySAEOWEGroups_Type.__name__ = "Bits"
_LcosLXSetupWLANEncryptionEntrySAEOWEGroups_Object = MibTableColumn
lcosLXSetupWLANEncryptionEntrySAEOWEGroups = _LcosLXSetupWLANEncryptionEntrySAEOWEGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 3, 1, 26),
    _LcosLXSetupWLANEncryptionEntrySAEOWEGroups_Type()
)
lcosLXSetupWLANEncryptionEntrySAEOWEGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANEncryptionEntrySAEOWEGroups.setStatus("current")
_LcosLXSetupWLANMgmt_ObjectIdentity = ObjectIdentity
lcosLXSetupWLANMgmt = _LcosLXSetupWLANMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4)
)


class _LcosLXSetupWLANMgmtActiveProfile_Type(OctetString):
    """Custom type lcosLXSetupWLANMgmtActiveProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LcosLXSetupWLANMgmtActiveProfile_Type.__name__ = "OctetString"
_LcosLXSetupWLANMgmtActiveProfile_Object = MibScalar
lcosLXSetupWLANMgmtActiveProfile = _LcosLXSetupWLANMgmtActiveProfile_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 1),
    _LcosLXSetupWLANMgmtActiveProfile_Type()
)
lcosLXSetupWLANMgmtActiveProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmtActiveProfile.setStatus("current")
_LcosLXSetupWLANMgmtProfiles_Object = MibTable
lcosLXSetupWLANMgmtProfiles = _LcosLXSetupWLANMgmtProfiles_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 2)
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmtProfiles.setStatus("current")
_LcosLXSetupWLANMgmtProfilesEntry_Object = MibTableRow
lcosLXSetupWLANMgmtProfilesEntry = _LcosLXSetupWLANMgmtProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 2, 1)
)
lcosLXSetupWLANMgmtProfilesEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupWLANMgmtProfilesEntryProfileName"),
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmtProfilesEntry.setStatus("current")


class _LcosLXSetupWLANMgmtProfilesEntryProfileName_Type(OctetString):
    """Custom type lcosLXSetupWLANMgmtProfilesEntryProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LcosLXSetupWLANMgmtProfilesEntryProfileName_Type.__name__ = "OctetString"
_LcosLXSetupWLANMgmtProfilesEntryProfileName_Object = MibTableColumn
lcosLXSetupWLANMgmtProfilesEntryProfileName = _LcosLXSetupWLANMgmtProfilesEntryProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 2, 1, 1),
    _LcosLXSetupWLANMgmtProfilesEntryProfileName_Type()
)
lcosLXSetupWLANMgmtProfilesEntryProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmtProfilesEntryProfileName.setStatus("current")


class _LcosLXSetupWLANMgmtProfilesEntryOperating_Type(Integer32):
    """Custom type lcosLXSetupWLANMgmtProfilesEntryOperating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupWLANMgmtProfilesEntryOperating_Type.__name__ = "Integer32"
_LcosLXSetupWLANMgmtProfilesEntryOperating_Object = MibTableColumn
lcosLXSetupWLANMgmtProfilesEntryOperating = _LcosLXSetupWLANMgmtProfilesEntryOperating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 2, 1, 2),
    _LcosLXSetupWLANMgmtProfilesEntryOperating_Type()
)
lcosLXSetupWLANMgmtProfilesEntryOperating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmtProfilesEntryOperating.setStatus("current")


class _LcosLXSetupWLANMgmtProfilesEntrySteeringMinPHYSignal_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmtProfilesEntrySteeringMinPHYSignal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmtProfilesEntrySteeringMinPHYSignal_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmtProfilesEntrySteeringMinPHYSignal_Object = MibTableColumn
lcosLXSetupWLANMgmtProfilesEntrySteeringMinPHYSignal = _LcosLXSetupWLANMgmtProfilesEntrySteeringMinPHYSignal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 2, 1, 3),
    _LcosLXSetupWLANMgmtProfilesEntrySteeringMinPHYSignal_Type()
)
lcosLXSetupWLANMgmtProfilesEntrySteeringMinPHYSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmtProfilesEntrySteeringMinPHYSignal.setStatus("current")


class _LcosLXSetupWLANMgmtProfilesEntryUpgradeTXRateThreshold_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmtProfilesEntryUpgradeTXRateThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmtProfilesEntryUpgradeTXRateThreshold_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmtProfilesEntryUpgradeTXRateThreshold_Object = MibTableColumn
lcosLXSetupWLANMgmtProfilesEntryUpgradeTXRateThreshold = _LcosLXSetupWLANMgmtProfilesEntryUpgradeTXRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 2, 1, 4),
    _LcosLXSetupWLANMgmtProfilesEntryUpgradeTXRateThreshold_Type()
)
lcosLXSetupWLANMgmtProfilesEntryUpgradeTXRateThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmtProfilesEntryUpgradeTXRateThreshold.setStatus("current")


class _LcosLXSetupWLANMgmtProfilesEntryUpgradePHYSignalThreshold_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmtProfilesEntryUpgradePHYSignalThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmtProfilesEntryUpgradePHYSignalThreshold_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmtProfilesEntryUpgradePHYSignalThreshold_Object = MibTableColumn
lcosLXSetupWLANMgmtProfilesEntryUpgradePHYSignalThreshold = _LcosLXSetupWLANMgmtProfilesEntryUpgradePHYSignalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 2, 1, 5),
    _LcosLXSetupWLANMgmtProfilesEntryUpgradePHYSignalThreshold_Type()
)
lcosLXSetupWLANMgmtProfilesEntryUpgradePHYSignalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmtProfilesEntryUpgradePHYSignalThreshold.setStatus("current")


class _LcosLXSetupWLANMgmtProfilesEntryDowngradeTXRateThreshold_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmtProfilesEntryDowngradeTXRateThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmtProfilesEntryDowngradeTXRateThreshold_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmtProfilesEntryDowngradeTXRateThreshold_Object = MibTableColumn
lcosLXSetupWLANMgmtProfilesEntryDowngradeTXRateThreshold = _LcosLXSetupWLANMgmtProfilesEntryDowngradeTXRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 2, 1, 6),
    _LcosLXSetupWLANMgmtProfilesEntryDowngradeTXRateThreshold_Type()
)
lcosLXSetupWLANMgmtProfilesEntryDowngradeTXRateThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmtProfilesEntryDowngradeTXRateThreshold.setStatus("current")


class _LcosLXSetupWLANMgmtProfilesEntryDowngradePHYSignalThreshold_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmtProfilesEntryDowngradePHYSignalThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmtProfilesEntryDowngradePHYSignalThreshold_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmtProfilesEntryDowngradePHYSignalThreshold_Object = MibTableColumn
lcosLXSetupWLANMgmtProfilesEntryDowngradePHYSignalThreshold = _LcosLXSetupWLANMgmtProfilesEntryDowngradePHYSignalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 2, 1, 7),
    _LcosLXSetupWLANMgmtProfilesEntryDowngradePHYSignalThreshold_Type()
)
lcosLXSetupWLANMgmtProfilesEntryDowngradePHYSignalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmtProfilesEntryDowngradePHYSignalThreshold.setStatus("current")


class _LcosLXSetupWLANMgmtProfilesEntry24GHzSubProfile_Type(OctetString):
    """Custom type lcosLXSetupWLANMgmtProfilesEntry24GHzSubProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LcosLXSetupWLANMgmtProfilesEntry24GHzSubProfile_Type.__name__ = "OctetString"
_LcosLXSetupWLANMgmtProfilesEntry24GHzSubProfile_Object = MibTableColumn
lcosLXSetupWLANMgmtProfilesEntry24GHzSubProfile = _LcosLXSetupWLANMgmtProfilesEntry24GHzSubProfile_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 2, 1, 8),
    _LcosLXSetupWLANMgmtProfilesEntry24GHzSubProfile_Type()
)
lcosLXSetupWLANMgmtProfilesEntry24GHzSubProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmtProfilesEntry24GHzSubProfile.setStatus("current")


class _LcosLXSetupWLANMgmtProfilesEntry5GHzSubProfile_Type(OctetString):
    """Custom type lcosLXSetupWLANMgmtProfilesEntry5GHzSubProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LcosLXSetupWLANMgmtProfilesEntry5GHzSubProfile_Type.__name__ = "OctetString"
_LcosLXSetupWLANMgmtProfilesEntry5GHzSubProfile_Object = MibTableColumn
lcosLXSetupWLANMgmtProfilesEntry5GHzSubProfile = _LcosLXSetupWLANMgmtProfilesEntry5GHzSubProfile_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 2, 1, 9),
    _LcosLXSetupWLANMgmtProfilesEntry5GHzSubProfile_Type()
)
lcosLXSetupWLANMgmtProfilesEntry5GHzSubProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmtProfilesEntry5GHzSubProfile.setStatus("current")
_LcosLXSetupWLANMgmt24GHz_Object = MibTable
lcosLXSetupWLANMgmt24GHz = _LcosLXSetupWLANMgmt24GHz_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 3)
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt24GHz.setStatus("current")
_LcosLXSetupWLANMgmt24GHzEntry_Object = MibTableRow
lcosLXSetupWLANMgmt24GHzEntry = _LcosLXSetupWLANMgmt24GHzEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 3, 1)
)
lcosLXSetupWLANMgmt24GHzEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupWLANMgmt24GHzEntryProfileName"),
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt24GHzEntry.setStatus("current")


class _LcosLXSetupWLANMgmt24GHzEntryProfileName_Type(OctetString):
    """Custom type lcosLXSetupWLANMgmt24GHzEntryProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LcosLXSetupWLANMgmt24GHzEntryProfileName_Type.__name__ = "OctetString"
_LcosLXSetupWLANMgmt24GHzEntryProfileName_Object = MibTableColumn
lcosLXSetupWLANMgmt24GHzEntryProfileName = _LcosLXSetupWLANMgmt24GHzEntryProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 3, 1, 1),
    _LcosLXSetupWLANMgmt24GHzEntryProfileName_Type()
)
lcosLXSetupWLANMgmt24GHzEntryProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt24GHzEntryProfileName.setStatus("current")


class _LcosLXSetupWLANMgmt24GHzEntryUtilizationCheckInterval_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmt24GHzEntryUtilizationCheckInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmt24GHzEntryUtilizationCheckInterval_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmt24GHzEntryUtilizationCheckInterval_Object = MibTableColumn
lcosLXSetupWLANMgmt24GHzEntryUtilizationCheckInterval = _LcosLXSetupWLANMgmt24GHzEntryUtilizationCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 3, 1, 2),
    _LcosLXSetupWLANMgmt24GHzEntryUtilizationCheckInterval_Type()
)
lcosLXSetupWLANMgmt24GHzEntryUtilizationCheckInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt24GHzEntryUtilizationCheckInterval.setStatus("current")


class _LcosLXSetupWLANMgmt24GHzEntryUtilizationAveragePeriod_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmt24GHzEntryUtilizationAveragePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmt24GHzEntryUtilizationAveragePeriod_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmt24GHzEntryUtilizationAveragePeriod_Object = MibTableColumn
lcosLXSetupWLANMgmt24GHzEntryUtilizationAveragePeriod = _LcosLXSetupWLANMgmt24GHzEntryUtilizationAveragePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 3, 1, 3),
    _LcosLXSetupWLANMgmt24GHzEntryUtilizationAveragePeriod_Type()
)
lcosLXSetupWLANMgmt24GHzEntryUtilizationAveragePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt24GHzEntryUtilizationAveragePeriod.setStatus("current")


class _LcosLXSetupWLANMgmt24GHzEntryUtilizationOverloadThreshold_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmt24GHzEntryUtilizationOverloadThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmt24GHzEntryUtilizationOverloadThreshold_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmt24GHzEntryUtilizationOverloadThreshold_Object = MibTableColumn
lcosLXSetupWLANMgmt24GHzEntryUtilizationOverloadThreshold = _LcosLXSetupWLANMgmt24GHzEntryUtilizationOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 3, 1, 4),
    _LcosLXSetupWLANMgmt24GHzEntryUtilizationOverloadThreshold_Type()
)
lcosLXSetupWLANMgmt24GHzEntryUtilizationOverloadThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt24GHzEntryUtilizationOverloadThreshold.setStatus("current")


class _LcosLXSetupWLANMgmt24GHzEntryUtilizationDeviationThreshold_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmt24GHzEntryUtilizationDeviationThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmt24GHzEntryUtilizationDeviationThreshold_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmt24GHzEntryUtilizationDeviationThreshold_Object = MibTableColumn
lcosLXSetupWLANMgmt24GHzEntryUtilizationDeviationThreshold = _LcosLXSetupWLANMgmt24GHzEntryUtilizationDeviationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 3, 1, 5),
    _LcosLXSetupWLANMgmt24GHzEntryUtilizationDeviationThreshold_Type()
)
lcosLXSetupWLANMgmt24GHzEntryUtilizationDeviationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt24GHzEntryUtilizationDeviationThreshold.setStatus("current")


class _LcosLXSetupWLANMgmt24GHzEntryInterferenceDetection_Type(Integer32):
    """Custom type lcosLXSetupWLANMgmt24GHzEntryInterferenceDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupWLANMgmt24GHzEntryInterferenceDetection_Type.__name__ = "Integer32"
_LcosLXSetupWLANMgmt24GHzEntryInterferenceDetection_Object = MibTableColumn
lcosLXSetupWLANMgmt24GHzEntryInterferenceDetection = _LcosLXSetupWLANMgmt24GHzEntryInterferenceDetection_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 3, 1, 6),
    _LcosLXSetupWLANMgmt24GHzEntryInterferenceDetection_Type()
)
lcosLXSetupWLANMgmt24GHzEntryInterferenceDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt24GHzEntryInterferenceDetection.setStatus("current")


class _LcosLXSetupWLANMgmt24GHzEntryDelayProbePHYSignalThreshold_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmt24GHzEntryDelayProbePHYSignalThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmt24GHzEntryDelayProbePHYSignalThreshold_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmt24GHzEntryDelayProbePHYSignalThreshold_Object = MibTableColumn
lcosLXSetupWLANMgmt24GHzEntryDelayProbePHYSignalThreshold = _LcosLXSetupWLANMgmt24GHzEntryDelayProbePHYSignalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 3, 1, 7),
    _LcosLXSetupWLANMgmt24GHzEntryDelayProbePHYSignalThreshold_Type()
)
lcosLXSetupWLANMgmt24GHzEntryDelayProbePHYSignalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt24GHzEntryDelayProbePHYSignalThreshold.setStatus("current")


class _LcosLXSetupWLANMgmt24GHzEntryDelayProbeTimeWindow_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmt24GHzEntryDelayProbeTimeWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmt24GHzEntryDelayProbeTimeWindow_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmt24GHzEntryDelayProbeTimeWindow_Object = MibTableColumn
lcosLXSetupWLANMgmt24GHzEntryDelayProbeTimeWindow = _LcosLXSetupWLANMgmt24GHzEntryDelayProbeTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 3, 1, 8),
    _LcosLXSetupWLANMgmt24GHzEntryDelayProbeTimeWindow_Type()
)
lcosLXSetupWLANMgmt24GHzEntryDelayProbeTimeWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt24GHzEntryDelayProbeTimeWindow.setStatus("current")


class _LcosLXSetupWLANMgmt24GHzEntryDelayProbeMinRequestCount_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmt24GHzEntryDelayProbeMinRequestCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmt24GHzEntryDelayProbeMinRequestCount_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmt24GHzEntryDelayProbeMinRequestCount_Object = MibTableColumn
lcosLXSetupWLANMgmt24GHzEntryDelayProbeMinRequestCount = _LcosLXSetupWLANMgmt24GHzEntryDelayProbeMinRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 3, 1, 9),
    _LcosLXSetupWLANMgmt24GHzEntryDelayProbeMinRequestCount_Type()
)
lcosLXSetupWLANMgmt24GHzEntryDelayProbeMinRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt24GHzEntryDelayProbeMinRequestCount.setStatus("current")
_LcosLXSetupWLANMgmt5GHz_Object = MibTable
lcosLXSetupWLANMgmt5GHz = _LcosLXSetupWLANMgmt5GHz_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 4)
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt5GHz.setStatus("current")
_LcosLXSetupWLANMgmt5GHzEntry_Object = MibTableRow
lcosLXSetupWLANMgmt5GHzEntry = _LcosLXSetupWLANMgmt5GHzEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 4, 1)
)
lcosLXSetupWLANMgmt5GHzEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupWLANMgmt5GHzEntryProfileName"),
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt5GHzEntry.setStatus("current")


class _LcosLXSetupWLANMgmt5GHzEntryProfileName_Type(OctetString):
    """Custom type lcosLXSetupWLANMgmt5GHzEntryProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LcosLXSetupWLANMgmt5GHzEntryProfileName_Type.__name__ = "OctetString"
_LcosLXSetupWLANMgmt5GHzEntryProfileName_Object = MibTableColumn
lcosLXSetupWLANMgmt5GHzEntryProfileName = _LcosLXSetupWLANMgmt5GHzEntryProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 4, 1, 1),
    _LcosLXSetupWLANMgmt5GHzEntryProfileName_Type()
)
lcosLXSetupWLANMgmt5GHzEntryProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt5GHzEntryProfileName.setStatus("current")


class _LcosLXSetupWLANMgmt5GHzEntryUtilizationCheckInterval_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmt5GHzEntryUtilizationCheckInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmt5GHzEntryUtilizationCheckInterval_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmt5GHzEntryUtilizationCheckInterval_Object = MibTableColumn
lcosLXSetupWLANMgmt5GHzEntryUtilizationCheckInterval = _LcosLXSetupWLANMgmt5GHzEntryUtilizationCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 4, 1, 2),
    _LcosLXSetupWLANMgmt5GHzEntryUtilizationCheckInterval_Type()
)
lcosLXSetupWLANMgmt5GHzEntryUtilizationCheckInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt5GHzEntryUtilizationCheckInterval.setStatus("current")


class _LcosLXSetupWLANMgmt5GHzEntryUtilizationAveragePeriod_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmt5GHzEntryUtilizationAveragePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmt5GHzEntryUtilizationAveragePeriod_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmt5GHzEntryUtilizationAveragePeriod_Object = MibTableColumn
lcosLXSetupWLANMgmt5GHzEntryUtilizationAveragePeriod = _LcosLXSetupWLANMgmt5GHzEntryUtilizationAveragePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 4, 1, 3),
    _LcosLXSetupWLANMgmt5GHzEntryUtilizationAveragePeriod_Type()
)
lcosLXSetupWLANMgmt5GHzEntryUtilizationAveragePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt5GHzEntryUtilizationAveragePeriod.setStatus("current")


class _LcosLXSetupWLANMgmt5GHzEntryUtilizationOverloadThreshold_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmt5GHzEntryUtilizationOverloadThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmt5GHzEntryUtilizationOverloadThreshold_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmt5GHzEntryUtilizationOverloadThreshold_Object = MibTableColumn
lcosLXSetupWLANMgmt5GHzEntryUtilizationOverloadThreshold = _LcosLXSetupWLANMgmt5GHzEntryUtilizationOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 4, 1, 4),
    _LcosLXSetupWLANMgmt5GHzEntryUtilizationOverloadThreshold_Type()
)
lcosLXSetupWLANMgmt5GHzEntryUtilizationOverloadThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt5GHzEntryUtilizationOverloadThreshold.setStatus("current")


class _LcosLXSetupWLANMgmt5GHzEntryUtilizationDeviationThreshold_Type(Unsigned32):
    """Custom type lcosLXSetupWLANMgmt5GHzEntryUtilizationDeviationThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LcosLXSetupWLANMgmt5GHzEntryUtilizationDeviationThreshold_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANMgmt5GHzEntryUtilizationDeviationThreshold_Object = MibTableColumn
lcosLXSetupWLANMgmt5GHzEntryUtilizationDeviationThreshold = _LcosLXSetupWLANMgmt5GHzEntryUtilizationDeviationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 4, 1, 5),
    _LcosLXSetupWLANMgmt5GHzEntryUtilizationDeviationThreshold_Type()
)
lcosLXSetupWLANMgmt5GHzEntryUtilizationDeviationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt5GHzEntryUtilizationDeviationThreshold.setStatus("current")


class _LcosLXSetupWLANMgmt5GHzEntryInterferenceDetection_Type(Integer32):
    """Custom type lcosLXSetupWLANMgmt5GHzEntryInterferenceDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupWLANMgmt5GHzEntryInterferenceDetection_Type.__name__ = "Integer32"
_LcosLXSetupWLANMgmt5GHzEntryInterferenceDetection_Object = MibTableColumn
lcosLXSetupWLANMgmt5GHzEntryInterferenceDetection = _LcosLXSetupWLANMgmt5GHzEntryInterferenceDetection_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 4, 4, 1, 6),
    _LcosLXSetupWLANMgmt5GHzEntryInterferenceDetection_Type()
)
lcosLXSetupWLANMgmt5GHzEntryInterferenceDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANMgmt5GHzEntryInterferenceDetection.setStatus("current")
_LcosLXSetupWLANRadioSettings_Object = MibTable
lcosLXSetupWLANRadioSettings = _LcosLXSetupWLANRadioSettings_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 8)
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANRadioSettings.setStatus("current")
_LcosLXSetupWLANRadioSettingsEntry_Object = MibTableRow
lcosLXSetupWLANRadioSettingsEntry = _LcosLXSetupWLANRadioSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 8, 1)
)
lcosLXSetupWLANRadioSettingsEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupWLANRadioSettingsEntryIfc"),
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANRadioSettingsEntry.setStatus("current")


class _LcosLXSetupWLANRadioSettingsEntryIfc_Type(OctetString):
    """Custom type lcosLXSetupWLANRadioSettingsEntryIfc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_LcosLXSetupWLANRadioSettingsEntryIfc_Type.__name__ = "OctetString"
_LcosLXSetupWLANRadioSettingsEntryIfc_Object = MibTableColumn
lcosLXSetupWLANRadioSettingsEntryIfc = _LcosLXSetupWLANRadioSettingsEntryIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 8, 1, 1),
    _LcosLXSetupWLANRadioSettingsEntryIfc_Type()
)
lcosLXSetupWLANRadioSettingsEntryIfc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRadioSettingsEntryIfc.setStatus("current")


class _LcosLXSetupWLANRadioSettingsEntry5GHzMode_Type(Integer32):
    """Custom type lcosLXSetupWLANRadioSettingsEntry5GHzMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              7,
              8,
              9,
              10,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e11anmixed", 3),
          ("e11anacmixed", 7),
          ("e11nacmixed", 8),
          ("e11aconly", 9),
          ("e11anacaxmixed", 10),
          ("eAuto", 255))
    )


_LcosLXSetupWLANRadioSettingsEntry5GHzMode_Type.__name__ = "Integer32"
_LcosLXSetupWLANRadioSettingsEntry5GHzMode_Object = MibTableColumn
lcosLXSetupWLANRadioSettingsEntry5GHzMode = _LcosLXSetupWLANRadioSettingsEntry5GHzMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 8, 1, 3),
    _LcosLXSetupWLANRadioSettingsEntry5GHzMode_Type()
)
lcosLXSetupWLANRadioSettingsEntry5GHzMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRadioSettingsEntry5GHzMode.setStatus("current")


class _LcosLXSetupWLANRadioSettingsEntryRadioBand_Type(Integer32):
    """Custom type lcosLXSetupWLANRadioSettingsEntryRadioBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e24GHz", 1),
          ("e5GHz", 2))
    )


_LcosLXSetupWLANRadioSettingsEntryRadioBand_Type.__name__ = "Integer32"
_LcosLXSetupWLANRadioSettingsEntryRadioBand_Object = MibTableColumn
lcosLXSetupWLANRadioSettingsEntryRadioBand = _LcosLXSetupWLANRadioSettingsEntryRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 8, 1, 6),
    _LcosLXSetupWLANRadioSettingsEntryRadioBand_Type()
)
lcosLXSetupWLANRadioSettingsEntryRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRadioSettingsEntryRadioBand.setStatus("current")


class _LcosLXSetupWLANRadioSettingsEntrySubBand_Type(Integer32):
    """Custom type lcosLXSetupWLANRadioSettingsEntrySubBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eBand12", 0),
          ("eBand1", 1),
          ("eBand2", 2))
    )


_LcosLXSetupWLANRadioSettingsEntrySubBand_Type.__name__ = "Integer32"
_LcosLXSetupWLANRadioSettingsEntrySubBand_Object = MibTableColumn
lcosLXSetupWLANRadioSettingsEntrySubBand = _LcosLXSetupWLANRadioSettingsEntrySubBand_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 8, 1, 7),
    _LcosLXSetupWLANRadioSettingsEntrySubBand_Type()
)
lcosLXSetupWLANRadioSettingsEntrySubBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRadioSettingsEntrySubBand.setStatus("current")


class _LcosLXSetupWLANRadioSettingsEntryChannel_Type(Unsigned32):
    """Custom type lcosLXSetupWLANRadioSettingsEntryChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXSetupWLANRadioSettingsEntryChannel_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANRadioSettingsEntryChannel_Object = MibTableColumn
lcosLXSetupWLANRadioSettingsEntryChannel = _LcosLXSetupWLANRadioSettingsEntryChannel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 8, 1, 8),
    _LcosLXSetupWLANRadioSettingsEntryChannel_Type()
)
lcosLXSetupWLANRadioSettingsEntryChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRadioSettingsEntryChannel.setStatus("current")


class _LcosLXSetupWLANRadioSettingsEntry24GHzMode_Type(Integer32):
    """Custom type lcosLXSetupWLANRadioSettingsEntry24GHzMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              5,
              7,
              8,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e11bgmixed", 0),
          ("e11gonly", 1),
          ("e11bgnmixed", 5),
          ("e11gnmixed", 7),
          ("e11bgnaxmixed", 8),
          ("e11gnaxmixed", 9),
          ("eAuto", 255))
    )


_LcosLXSetupWLANRadioSettingsEntry24GHzMode_Type.__name__ = "Integer32"
_LcosLXSetupWLANRadioSettingsEntry24GHzMode_Object = MibTableColumn
lcosLXSetupWLANRadioSettingsEntry24GHzMode = _LcosLXSetupWLANRadioSettingsEntry24GHzMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 8, 1, 9),
    _LcosLXSetupWLANRadioSettingsEntry24GHzMode_Type()
)
lcosLXSetupWLANRadioSettingsEntry24GHzMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRadioSettingsEntry24GHzMode.setStatus("current")


class _LcosLXSetupWLANRadioSettingsEntryAntennaGain_Type(Unsigned32):
    """Custom type lcosLXSetupWLANRadioSettingsEntryAntennaGain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXSetupWLANRadioSettingsEntryAntennaGain_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANRadioSettingsEntryAntennaGain_Object = MibTableColumn
lcosLXSetupWLANRadioSettingsEntryAntennaGain = _LcosLXSetupWLANRadioSettingsEntryAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 8, 1, 12),
    _LcosLXSetupWLANRadioSettingsEntryAntennaGain_Type()
)
lcosLXSetupWLANRadioSettingsEntryAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRadioSettingsEntryAntennaGain.setStatus("current")


class _LcosLXSetupWLANRadioSettingsEntryChannelList_Type(OctetString):
    """Custom type lcosLXSetupWLANRadioSettingsEntryChannelList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_LcosLXSetupWLANRadioSettingsEntryChannelList_Type.__name__ = "OctetString"
_LcosLXSetupWLANRadioSettingsEntryChannelList_Object = MibTableColumn
lcosLXSetupWLANRadioSettingsEntryChannelList = _LcosLXSetupWLANRadioSettingsEntryChannelList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 8, 1, 13),
    _LcosLXSetupWLANRadioSettingsEntryChannelList_Type()
)
lcosLXSetupWLANRadioSettingsEntryChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRadioSettingsEntryChannelList.setStatus("current")


class _LcosLXSetupWLANRadioSettingsEntryMaxChannelBandwidth_Type(Integer32):
    """Custom type lcosLXSetupWLANRadioSettingsEntryMaxChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e20MHz", 0),
          ("e40MHz", 1),
          ("e80MHz", 2),
          ("e160MHz", 3),
          ("eAuto", 255))
    )


_LcosLXSetupWLANRadioSettingsEntryMaxChannelBandwidth_Type.__name__ = "Integer32"
_LcosLXSetupWLANRadioSettingsEntryMaxChannelBandwidth_Object = MibTableColumn
lcosLXSetupWLANRadioSettingsEntryMaxChannelBandwidth = _LcosLXSetupWLANRadioSettingsEntryMaxChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 8, 1, 24),
    _LcosLXSetupWLANRadioSettingsEntryMaxChannelBandwidth_Type()
)
lcosLXSetupWLANRadioSettingsEntryMaxChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRadioSettingsEntryMaxChannelBandwidth.setStatus("current")


class _LcosLXSetupWLANRadioSettingsEntryExcludeDFSChannels_Type(Integer32):
    """Custom type lcosLXSetupWLANRadioSettingsEntryExcludeDFSChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupWLANRadioSettingsEntryExcludeDFSChannels_Type.__name__ = "Integer32"
_LcosLXSetupWLANRadioSettingsEntryExcludeDFSChannels_Object = MibTableColumn
lcosLXSetupWLANRadioSettingsEntryExcludeDFSChannels = _LcosLXSetupWLANRadioSettingsEntryExcludeDFSChannels_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 8, 1, 29),
    _LcosLXSetupWLANRadioSettingsEntryExcludeDFSChannels_Type()
)
lcosLXSetupWLANRadioSettingsEntryExcludeDFSChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRadioSettingsEntryExcludeDFSChannels.setStatus("current")


class _LcosLXSetupWLANRadioSettingsEntryPowerSetting_Type(Integer32):
    """Custom type lcosLXSetupWLANRadioSettingsEntryPowerSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eAutomatic", 0),
          ("eManual", 1))
    )


_LcosLXSetupWLANRadioSettingsEntryPowerSetting_Type.__name__ = "Integer32"
_LcosLXSetupWLANRadioSettingsEntryPowerSetting_Object = MibTableColumn
lcosLXSetupWLANRadioSettingsEntryPowerSetting = _LcosLXSetupWLANRadioSettingsEntryPowerSetting_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 8, 1, 33),
    _LcosLXSetupWLANRadioSettingsEntryPowerSetting_Type()
)
lcosLXSetupWLANRadioSettingsEntryPowerSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRadioSettingsEntryPowerSetting.setStatus("current")


class _LcosLXSetupWLANRadioSettingsEntryEIRP_Type(Unsigned32):
    """Custom type lcosLXSetupWLANRadioSettingsEntryEIRP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXSetupWLANRadioSettingsEntryEIRP_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANRadioSettingsEntryEIRP_Object = MibTableColumn
lcosLXSetupWLANRadioSettingsEntryEIRP = _LcosLXSetupWLANRadioSettingsEntryEIRP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 8, 1, 34),
    _LcosLXSetupWLANRadioSettingsEntryEIRP_Type()
)
lcosLXSetupWLANRadioSettingsEntryEIRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRadioSettingsEntryEIRP.setStatus("current")


class _LcosLXSetupWLANAutomaticEnvironmentScanEnabled_Type(Integer32):
    """Custom type lcosLXSetupWLANAutomaticEnvironmentScanEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupWLANAutomaticEnvironmentScanEnabled_Type.__name__ = "Integer32"
_LcosLXSetupWLANAutomaticEnvironmentScanEnabled_Object = MibScalar
lcosLXSetupWLANAutomaticEnvironmentScanEnabled = _LcosLXSetupWLANAutomaticEnvironmentScanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 9),
    _LcosLXSetupWLANAutomaticEnvironmentScanEnabled_Type()
)
lcosLXSetupWLANAutomaticEnvironmentScanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANAutomaticEnvironmentScanEnabled.setStatus("current")


class _LcosLXSetupWLANAutomaticEnvironmentScanTimeBegin_Type(OctetString):
    """Custom type lcosLXSetupWLANAutomaticEnvironmentScanTimeBegin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_LcosLXSetupWLANAutomaticEnvironmentScanTimeBegin_Type.__name__ = "OctetString"
_LcosLXSetupWLANAutomaticEnvironmentScanTimeBegin_Object = MibScalar
lcosLXSetupWLANAutomaticEnvironmentScanTimeBegin = _LcosLXSetupWLANAutomaticEnvironmentScanTimeBegin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 10),
    _LcosLXSetupWLANAutomaticEnvironmentScanTimeBegin_Type()
)
lcosLXSetupWLANAutomaticEnvironmentScanTimeBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANAutomaticEnvironmentScanTimeBegin.setStatus("current")


class _LcosLXSetupWLANAutomaticEnvironmentScanTimeEnd_Type(OctetString):
    """Custom type lcosLXSetupWLANAutomaticEnvironmentScanTimeEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_LcosLXSetupWLANAutomaticEnvironmentScanTimeEnd_Type.__name__ = "OctetString"
_LcosLXSetupWLANAutomaticEnvironmentScanTimeEnd_Object = MibScalar
lcosLXSetupWLANAutomaticEnvironmentScanTimeEnd = _LcosLXSetupWLANAutomaticEnvironmentScanTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 11),
    _LcosLXSetupWLANAutomaticEnvironmentScanTimeEnd_Type()
)
lcosLXSetupWLANAutomaticEnvironmentScanTimeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANAutomaticEnvironmentScanTimeEnd.setStatus("current")
_LcosLXSetupWLANHotspot_ObjectIdentity = ObjectIdentity
lcosLXSetupWLANHotspot = _LcosLXSetupWLANHotspot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 12)
)
_LcosLXSetupWLANHotspotHotspots_Object = MibTable
lcosLXSetupWLANHotspotHotspots = _LcosLXSetupWLANHotspotHotspots_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 12, 1)
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANHotspotHotspots.setStatus("current")
_LcosLXSetupWLANHotspotHotspotsEntry_Object = MibTableRow
lcosLXSetupWLANHotspotHotspotsEntry = _LcosLXSetupWLANHotspotHotspotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 12, 1, 1)
)
lcosLXSetupWLANHotspotHotspotsEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupWLANHotspotHotspotsEntryName"),
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANHotspotHotspotsEntry.setStatus("current")


class _LcosLXSetupWLANHotspotHotspotsEntryName_Type(OctetString):
    """Custom type lcosLXSetupWLANHotspotHotspotsEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXSetupWLANHotspotHotspotsEntryName_Type.__name__ = "OctetString"
_LcosLXSetupWLANHotspotHotspotsEntryName_Object = MibTableColumn
lcosLXSetupWLANHotspotHotspotsEntryName = _LcosLXSetupWLANHotspotHotspotsEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 12, 1, 1, 1),
    _LcosLXSetupWLANHotspotHotspotsEntryName_Type()
)
lcosLXSetupWLANHotspotHotspotsEntryName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupWLANHotspotHotspotsEntryName.setStatus("current")


class _LcosLXSetupWLANHotspotHotspotsEntryURL_Type(OctetString):
    """Custom type lcosLXSetupWLANHotspotHotspotsEntryURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LcosLXSetupWLANHotspotHotspotsEntryURL_Type.__name__ = "OctetString"
_LcosLXSetupWLANHotspotHotspotsEntryURL_Object = MibTableColumn
lcosLXSetupWLANHotspotHotspotsEntryURL = _LcosLXSetupWLANHotspotHotspotsEntryURL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 12, 1, 1, 2),
    _LcosLXSetupWLANHotspotHotspotsEntryURL_Type()
)
lcosLXSetupWLANHotspotHotspotsEntryURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANHotspotHotspotsEntryURL.setStatus("current")


class _LcosLXSetupWLANHotspotHotspotsEntryRevisionID_Type(OctetString):
    """Custom type lcosLXSetupWLANHotspotHotspotsEntryRevisionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_LcosLXSetupWLANHotspotHotspotsEntryRevisionID_Type.__name__ = "OctetString"
_LcosLXSetupWLANHotspotHotspotsEntryRevisionID_Object = MibTableColumn
lcosLXSetupWLANHotspotHotspotsEntryRevisionID = _LcosLXSetupWLANHotspotHotspotsEntryRevisionID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 12, 1, 1, 3),
    _LcosLXSetupWLANHotspotHotspotsEntryRevisionID_Type()
)
lcosLXSetupWLANHotspotHotspotsEntryRevisionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANHotspotHotspotsEntryRevisionID.setStatus("current")


class _LcosLXSetupWLANHotspotHotspotsEntryPrivateNetwork_Type(Integer32):
    """Custom type lcosLXSetupWLANHotspotHotspotsEntryPrivateNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupWLANHotspotHotspotsEntryPrivateNetwork_Type.__name__ = "Integer32"
_LcosLXSetupWLANHotspotHotspotsEntryPrivateNetwork_Object = MibTableColumn
lcosLXSetupWLANHotspotHotspotsEntryPrivateNetwork = _LcosLXSetupWLANHotspotHotspotsEntryPrivateNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 12, 1, 1, 4),
    _LcosLXSetupWLANHotspotHotspotsEntryPrivateNetwork_Type()
)
lcosLXSetupWLANHotspotHotspotsEntryPrivateNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANHotspotHotspotsEntryPrivateNetwork.setStatus("current")


class _LcosLXSetupWLANHotspotHotspotsEntryDHCPRangeStart_Type(OctetString):
    """Custom type lcosLXSetupWLANHotspotHotspotsEntryDHCPRangeStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXSetupWLANHotspotHotspotsEntryDHCPRangeStart_Type.__name__ = "OctetString"
_LcosLXSetupWLANHotspotHotspotsEntryDHCPRangeStart_Object = MibTableColumn
lcosLXSetupWLANHotspotHotspotsEntryDHCPRangeStart = _LcosLXSetupWLANHotspotHotspotsEntryDHCPRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 12, 1, 1, 5),
    _LcosLXSetupWLANHotspotHotspotsEntryDHCPRangeStart_Type()
)
lcosLXSetupWLANHotspotHotspotsEntryDHCPRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANHotspotHotspotsEntryDHCPRangeStart.setStatus("current")


class _LcosLXSetupWLANHotspotHotspotsEntryDHCPRangeEnd_Type(OctetString):
    """Custom type lcosLXSetupWLANHotspotHotspotsEntryDHCPRangeEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXSetupWLANHotspotHotspotsEntryDHCPRangeEnd_Type.__name__ = "OctetString"
_LcosLXSetupWLANHotspotHotspotsEntryDHCPRangeEnd_Object = MibTableColumn
lcosLXSetupWLANHotspotHotspotsEntryDHCPRangeEnd = _LcosLXSetupWLANHotspotHotspotsEntryDHCPRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 12, 1, 1, 6),
    _LcosLXSetupWLANHotspotHotspotsEntryDHCPRangeEnd_Type()
)
lcosLXSetupWLANHotspotHotspotsEntryDHCPRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANHotspotHotspotsEntryDHCPRangeEnd.setStatus("current")
_LcosLXSetupWLANLEPS_ObjectIdentity = ObjectIdentity
lcosLXSetupWLANLEPS = _LcosLXSetupWLANLEPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133)
)


class _LcosLXSetupWLANLEPSOperating_Type(Integer32):
    """Custom type lcosLXSetupWLANLEPSOperating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupWLANLEPSOperating_Type.__name__ = "Integer32"
_LcosLXSetupWLANLEPSOperating_Object = MibScalar
lcosLXSetupWLANLEPSOperating = _LcosLXSetupWLANLEPSOperating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133, 1),
    _LcosLXSetupWLANLEPSOperating_Type()
)
lcosLXSetupWLANLEPSOperating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANLEPSOperating.setStatus("current")
_LcosLXSetupWLANLEPSProfiles_Object = MibTable
lcosLXSetupWLANLEPSProfiles = _LcosLXSetupWLANLEPSProfiles_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133, 2)
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANLEPSProfiles.setStatus("current")
_LcosLXSetupWLANLEPSProfilesEntry_Object = MibTableRow
lcosLXSetupWLANLEPSProfilesEntry = _LcosLXSetupWLANLEPSProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133, 2, 1)
)
lcosLXSetupWLANLEPSProfilesEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupWLANLEPSProfilesEntryName"),
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANLEPSProfilesEntry.setStatus("current")


class _LcosLXSetupWLANLEPSProfilesEntryName_Type(OctetString):
    """Custom type lcosLXSetupWLANLEPSProfilesEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXSetupWLANLEPSProfilesEntryName_Type.__name__ = "OctetString"
_LcosLXSetupWLANLEPSProfilesEntryName_Object = MibTableColumn
lcosLXSetupWLANLEPSProfilesEntryName = _LcosLXSetupWLANLEPSProfilesEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133, 2, 1, 1),
    _LcosLXSetupWLANLEPSProfilesEntryName_Type()
)
lcosLXSetupWLANLEPSProfilesEntryName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupWLANLEPSProfilesEntryName.setStatus("current")


class _LcosLXSetupWLANLEPSProfilesEntryNetworkName_Type(OctetString):
    """Custom type lcosLXSetupWLANLEPSProfilesEntryNetworkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXSetupWLANLEPSProfilesEntryNetworkName_Type.__name__ = "OctetString"
_LcosLXSetupWLANLEPSProfilesEntryNetworkName_Object = MibTableColumn
lcosLXSetupWLANLEPSProfilesEntryNetworkName = _LcosLXSetupWLANLEPSProfilesEntryNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133, 2, 1, 2),
    _LcosLXSetupWLANLEPSProfilesEntryNetworkName_Type()
)
lcosLXSetupWLANLEPSProfilesEntryNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANLEPSProfilesEntryNetworkName.setStatus("current")


class _LcosLXSetupWLANLEPSProfilesEntryMACList_Type(Integer32):
    """Custom type lcosLXSetupWLANLEPSProfilesEntryMACList based on Integer32"""
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
        *(("eDisabled", 0),
          ("eWhitelist", 1),
          ("eBlacklist", 2),
          ("eRADIUS", 3))
    )


_LcosLXSetupWLANLEPSProfilesEntryMACList_Type.__name__ = "Integer32"
_LcosLXSetupWLANLEPSProfilesEntryMACList_Object = MibTableColumn
lcosLXSetupWLANLEPSProfilesEntryMACList = _LcosLXSetupWLANLEPSProfilesEntryMACList_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133, 2, 1, 3),
    _LcosLXSetupWLANLEPSProfilesEntryMACList_Type()
)
lcosLXSetupWLANLEPSProfilesEntryMACList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANLEPSProfilesEntryMACList.setStatus("current")


class _LcosLXSetupWLANLEPSProfilesEntryVLAN_Type(Unsigned32):
    """Custom type lcosLXSetupWLANLEPSProfilesEntryVLAN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupWLANLEPSProfilesEntryVLAN_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANLEPSProfilesEntryVLAN_Object = MibTableColumn
lcosLXSetupWLANLEPSProfilesEntryVLAN = _LcosLXSetupWLANLEPSProfilesEntryVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133, 2, 1, 4),
    _LcosLXSetupWLANLEPSProfilesEntryVLAN_Type()
)
lcosLXSetupWLANLEPSProfilesEntryVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANLEPSProfilesEntryVLAN.setStatus("current")
_LcosLXSetupWLANLEPSUsers_Object = MibTable
lcosLXSetupWLANLEPSUsers = _LcosLXSetupWLANLEPSUsers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133, 3)
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANLEPSUsers.setStatus("current")
_LcosLXSetupWLANLEPSUsersEntry_Object = MibTableRow
lcosLXSetupWLANLEPSUsersEntry = _LcosLXSetupWLANLEPSUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133, 3, 1)
)
lcosLXSetupWLANLEPSUsersEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupWLANLEPSUsersEntryName"),
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANLEPSUsersEntry.setStatus("current")


class _LcosLXSetupWLANLEPSUsersEntryName_Type(OctetString):
    """Custom type lcosLXSetupWLANLEPSUsersEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXSetupWLANLEPSUsersEntryName_Type.__name__ = "OctetString"
_LcosLXSetupWLANLEPSUsersEntryName_Object = MibTableColumn
lcosLXSetupWLANLEPSUsersEntryName = _LcosLXSetupWLANLEPSUsersEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133, 3, 1, 1),
    _LcosLXSetupWLANLEPSUsersEntryName_Type()
)
lcosLXSetupWLANLEPSUsersEntryName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupWLANLEPSUsersEntryName.setStatus("current")


class _LcosLXSetupWLANLEPSUsersEntryProfile_Type(OctetString):
    """Custom type lcosLXSetupWLANLEPSUsersEntryProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXSetupWLANLEPSUsersEntryProfile_Type.__name__ = "OctetString"
_LcosLXSetupWLANLEPSUsersEntryProfile_Object = MibTableColumn
lcosLXSetupWLANLEPSUsersEntryProfile = _LcosLXSetupWLANLEPSUsersEntryProfile_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133, 3, 1, 2),
    _LcosLXSetupWLANLEPSUsersEntryProfile_Type()
)
lcosLXSetupWLANLEPSUsersEntryProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANLEPSUsersEntryProfile.setStatus("current")


class _LcosLXSetupWLANLEPSUsersEntryWPAPassphrase_Type(OctetString):
    """Custom type lcosLXSetupWLANLEPSUsersEntryWPAPassphrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LcosLXSetupWLANLEPSUsersEntryWPAPassphrase_Type.__name__ = "OctetString"
_LcosLXSetupWLANLEPSUsersEntryWPAPassphrase_Object = MibTableColumn
lcosLXSetupWLANLEPSUsersEntryWPAPassphrase = _LcosLXSetupWLANLEPSUsersEntryWPAPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133, 3, 1, 3),
    _LcosLXSetupWLANLEPSUsersEntryWPAPassphrase_Type()
)
lcosLXSetupWLANLEPSUsersEntryWPAPassphrase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANLEPSUsersEntryWPAPassphrase.setStatus("current")


class _LcosLXSetupWLANLEPSUsersEntryVLAN_Type(Unsigned32):
    """Custom type lcosLXSetupWLANLEPSUsersEntryVLAN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupWLANLEPSUsersEntryVLAN_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANLEPSUsersEntryVLAN_Object = MibTableColumn
lcosLXSetupWLANLEPSUsersEntryVLAN = _LcosLXSetupWLANLEPSUsersEntryVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133, 3, 1, 4),
    _LcosLXSetupWLANLEPSUsersEntryVLAN_Type()
)
lcosLXSetupWLANLEPSUsersEntryVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANLEPSUsersEntryVLAN.setStatus("current")
_LcosLXSetupWLANLEPSUsersEntryMACAddress_Type = MacAddress
_LcosLXSetupWLANLEPSUsersEntryMACAddress_Object = MibTableColumn
lcosLXSetupWLANLEPSUsersEntryMACAddress = _LcosLXSetupWLANLEPSUsersEntryMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 133, 3, 1, 7),
    _LcosLXSetupWLANLEPSUsersEntryMACAddress_Type()
)
lcosLXSetupWLANLEPSUsersEntryMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANLEPSUsersEntryMACAddress.setStatus("current")
_LcosLXSetupWLANRateSelection_Object = MibTable
lcosLXSetupWLANRateSelection = _LcosLXSetupWLANRateSelection_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1111)
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANRateSelection.setStatus("current")
_LcosLXSetupWLANRateSelectionEntry_Object = MibTableRow
lcosLXSetupWLANRateSelectionEntry = _LcosLXSetupWLANRateSelectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1111, 1)
)
lcosLXSetupWLANRateSelectionEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupWLANRateSelectionEntryNetworkName"),
    (0, "LCOS-LX-MIB", "lcosLXSetupWLANRateSelectionEntryRadioband"),
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANRateSelectionEntry.setStatus("current")


class _LcosLXSetupWLANRateSelectionEntryNetworkName_Type(OctetString):
    """Custom type lcosLXSetupWLANRateSelectionEntryNetworkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupWLANRateSelectionEntryNetworkName_Type.__name__ = "OctetString"
_LcosLXSetupWLANRateSelectionEntryNetworkName_Object = MibTableColumn
lcosLXSetupWLANRateSelectionEntryNetworkName = _LcosLXSetupWLANRateSelectionEntryNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1111, 1, 1),
    _LcosLXSetupWLANRateSelectionEntryNetworkName_Type()
)
lcosLXSetupWLANRateSelectionEntryNetworkName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRateSelectionEntryNetworkName.setStatus("current")


class _LcosLXSetupWLANRateSelectionEntryBroadcastRate_Type(Integer32):
    """Custom type lcosLXSetupWLANRateSelectionEntryBroadcastRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1000,
              2000,
              5500,
              6000,
              9000,
              11000,
              12000,
              18000,
              24000,
              36000,
              48000,
              54000)
        )
    )
    namedValues = NamedValues(
        *(("edefault", 0),
          ("e1MBit", 1000),
          ("e2MBit", 2000),
          ("e55MBit", 5500),
          ("e6MBit", 6000),
          ("e9MBit", 9000),
          ("e11MBit", 11000),
          ("e12MBit", 12000),
          ("e18MBit", 18000),
          ("e24MBit", 24000),
          ("e36MBit", 36000),
          ("e48MBit", 48000),
          ("e54MBit", 54000))
    )


_LcosLXSetupWLANRateSelectionEntryBroadcastRate_Type.__name__ = "Integer32"
_LcosLXSetupWLANRateSelectionEntryBroadcastRate_Object = MibTableColumn
lcosLXSetupWLANRateSelectionEntryBroadcastRate = _LcosLXSetupWLANRateSelectionEntryBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1111, 1, 23),
    _LcosLXSetupWLANRateSelectionEntryBroadcastRate_Type()
)
lcosLXSetupWLANRateSelectionEntryBroadcastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRateSelectionEntryBroadcastRate.setStatus("current")


class _LcosLXSetupWLANRateSelectionEntryMulticastRate_Type(Integer32):
    """Custom type lcosLXSetupWLANRateSelectionEntryMulticastRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1000,
              2000,
              5500,
              6000,
              9000,
              11000,
              12000,
              18000,
              24000,
              36000,
              48000,
              54000)
        )
    )
    namedValues = NamedValues(
        *(("edefault", 0),
          ("e1MBit", 1000),
          ("e2MBit", 2000),
          ("e55MBit", 5500),
          ("e6MBit", 6000),
          ("e9MBit", 9000),
          ("e11MBit", 11000),
          ("e12MBit", 12000),
          ("e18MBit", 18000),
          ("e24MBit", 24000),
          ("e36MBit", 36000),
          ("e48MBit", 48000),
          ("e54MBit", 54000))
    )


_LcosLXSetupWLANRateSelectionEntryMulticastRate_Type.__name__ = "Integer32"
_LcosLXSetupWLANRateSelectionEntryMulticastRate_Object = MibTableColumn
lcosLXSetupWLANRateSelectionEntryMulticastRate = _LcosLXSetupWLANRateSelectionEntryMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1111, 1, 24),
    _LcosLXSetupWLANRateSelectionEntryMulticastRate_Type()
)
lcosLXSetupWLANRateSelectionEntryMulticastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRateSelectionEntryMulticastRate.setStatus("current")


class _LcosLXSetupWLANRateSelectionEntryRadioband_Type(Integer32):
    """Custom type lcosLXSetupWLANRateSelectionEntryRadioband based on Integer32"""
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
        *(("e24GHz5GHz", 1),
          ("e24GHz", 2),
          ("e5GHz", 3),
          ("enone", 4))
    )


_LcosLXSetupWLANRateSelectionEntryRadioband_Type.__name__ = "Integer32"
_LcosLXSetupWLANRateSelectionEntryRadioband_Object = MibTableColumn
lcosLXSetupWLANRateSelectionEntryRadioband = _LcosLXSetupWLANRateSelectionEntryRadioband_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 20, 1111, 1, 101),
    _LcosLXSetupWLANRateSelectionEntryRadioband_Type()
)
lcosLXSetupWLANRateSelectionEntryRadioband.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupWLANRateSelectionEntryRadioband.setStatus("current")
_LcosLXSetupSyslog_ObjectIdentity = ObjectIdentity
lcosLXSetupSyslog = _LcosLXSetupSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 22)
)
_LcosLXSetupSyslogServer_Object = MibTable
lcosLXSetupSyslogServer = _LcosLXSetupSyslogServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 22, 2)
)
if mibBuilder.loadTexts:
    lcosLXSetupSyslogServer.setStatus("current")
_LcosLXSetupSyslogServerEntry_Object = MibTableRow
lcosLXSetupSyslogServerEntry = _LcosLXSetupSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 22, 2, 1)
)
lcosLXSetupSyslogServerEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupSyslogServerEntryName"),
)
if mibBuilder.loadTexts:
    lcosLXSetupSyslogServerEntry.setStatus("current")


class _LcosLXSetupSyslogServerEntryName_Type(OctetString):
    """Custom type lcosLXSetupSyslogServerEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXSetupSyslogServerEntryName_Type.__name__ = "OctetString"
_LcosLXSetupSyslogServerEntryName_Object = MibTableColumn
lcosLXSetupSyslogServerEntryName = _LcosLXSetupSyslogServerEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 22, 2, 1, 1),
    _LcosLXSetupSyslogServerEntryName_Type()
)
lcosLXSetupSyslogServerEntryName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupSyslogServerEntryName.setStatus("current")


class _LcosLXSetupSyslogServerEntryIPAddress_Type(OctetString):
    """Custom type lcosLXSetupSyslogServerEntryIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXSetupSyslogServerEntryIPAddress_Type.__name__ = "OctetString"
_LcosLXSetupSyslogServerEntryIPAddress_Object = MibTableColumn
lcosLXSetupSyslogServerEntryIPAddress = _LcosLXSetupSyslogServerEntryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 22, 2, 1, 7),
    _LcosLXSetupSyslogServerEntryIPAddress_Type()
)
lcosLXSetupSyslogServerEntryIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupSyslogServerEntryIPAddress.setStatus("current")


class _LcosLXSetupSyslogServerEntryPort_Type(Unsigned32):
    """Custom type lcosLXSetupSyslogServerEntryPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupSyslogServerEntryPort_Type.__name__ = "Unsigned32"
_LcosLXSetupSyslogServerEntryPort_Object = MibTableColumn
lcosLXSetupSyslogServerEntryPort = _LcosLXSetupSyslogServerEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 22, 2, 1, 8),
    _LcosLXSetupSyslogServerEntryPort_Type()
)
lcosLXSetupSyslogServerEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupSyslogServerEntryPort.setStatus("current")


class _LcosLXSetupSyslogServerEntryProtocol_Type(Integer32):
    """Custom type lcosLXSetupSyslogServerEntryProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eTCP", 1),
          ("eUDP", 2))
    )


_LcosLXSetupSyslogServerEntryProtocol_Type.__name__ = "Integer32"
_LcosLXSetupSyslogServerEntryProtocol_Object = MibTableColumn
lcosLXSetupSyslogServerEntryProtocol = _LcosLXSetupSyslogServerEntryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 22, 2, 1, 9),
    _LcosLXSetupSyslogServerEntryProtocol_Type()
)
lcosLXSetupSyslogServerEntryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupSyslogServerEntryProtocol.setStatus("current")
_LcosLXSetupRADIUS_ObjectIdentity = ObjectIdentity
lcosLXSetupRADIUS = _LcosLXSetupRADIUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30)
)
_LcosLXSetupRADIUSRADIUSServer_Object = MibTable
lcosLXSetupRADIUSRADIUSServer = _LcosLXSetupRADIUSRADIUSServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 3)
)
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSRADIUSServer.setStatus("current")
_LcosLXSetupRADIUSRADIUSServerEntry_Object = MibTableRow
lcosLXSetupRADIUSRADIUSServerEntry = _LcosLXSetupRADIUSRADIUSServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 3, 1)
)
lcosLXSetupRADIUSRADIUSServerEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupRADIUSRADIUSServerEntryName"),
)
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSRADIUSServerEntry.setStatus("current")


class _LcosLXSetupRADIUSRADIUSServerEntryName_Type(OctetString):
    """Custom type lcosLXSetupRADIUSRADIUSServerEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupRADIUSRADIUSServerEntryName_Type.__name__ = "OctetString"
_LcosLXSetupRADIUSRADIUSServerEntryName_Object = MibTableColumn
lcosLXSetupRADIUSRADIUSServerEntryName = _LcosLXSetupRADIUSRADIUSServerEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 3, 1, 1),
    _LcosLXSetupRADIUSRADIUSServerEntryName_Type()
)
lcosLXSetupRADIUSRADIUSServerEntryName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSRADIUSServerEntryName.setStatus("current")


class _LcosLXSetupRADIUSRADIUSServerEntryPort_Type(Unsigned32):
    """Custom type lcosLXSetupRADIUSRADIUSServerEntryPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupRADIUSRADIUSServerEntryPort_Type.__name__ = "Unsigned32"
_LcosLXSetupRADIUSRADIUSServerEntryPort_Object = MibTableColumn
lcosLXSetupRADIUSRADIUSServerEntryPort = _LcosLXSetupRADIUSRADIUSServerEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 3, 1, 3),
    _LcosLXSetupRADIUSRADIUSServerEntryPort_Type()
)
lcosLXSetupRADIUSRADIUSServerEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSRADIUSServerEntryPort.setStatus("current")


class _LcosLXSetupRADIUSRADIUSServerEntrySecret_Type(OctetString):
    """Custom type lcosLXSetupRADIUSRADIUSServerEntrySecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupRADIUSRADIUSServerEntrySecret_Type.__name__ = "OctetString"
_LcosLXSetupRADIUSRADIUSServerEntrySecret_Object = MibTableColumn
lcosLXSetupRADIUSRADIUSServerEntrySecret = _LcosLXSetupRADIUSRADIUSServerEntrySecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 3, 1, 4),
    _LcosLXSetupRADIUSRADIUSServerEntrySecret_Type()
)
lcosLXSetupRADIUSRADIUSServerEntrySecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSRADIUSServerEntrySecret.setStatus("current")


class _LcosLXSetupRADIUSRADIUSServerEntryBackup_Type(OctetString):
    """Custom type lcosLXSetupRADIUSRADIUSServerEntryBackup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupRADIUSRADIUSServerEntryBackup_Type.__name__ = "OctetString"
_LcosLXSetupRADIUSRADIUSServerEntryBackup_Object = MibTableColumn
lcosLXSetupRADIUSRADIUSServerEntryBackup = _LcosLXSetupRADIUSRADIUSServerEntryBackup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 3, 1, 5),
    _LcosLXSetupRADIUSRADIUSServerEntryBackup_Type()
)
lcosLXSetupRADIUSRADIUSServerEntryBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSRADIUSServerEntryBackup.setStatus("current")


class _LcosLXSetupRADIUSRADIUSServerEntryServerIPAddress_Type(OctetString):
    """Custom type lcosLXSetupRADIUSRADIUSServerEntryServerIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupRADIUSRADIUSServerEntryServerIPAddress_Type.__name__ = "OctetString"
_LcosLXSetupRADIUSRADIUSServerEntryServerIPAddress_Object = MibTableColumn
lcosLXSetupRADIUSRADIUSServerEntryServerIPAddress = _LcosLXSetupRADIUSRADIUSServerEntryServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 3, 1, 8),
    _LcosLXSetupRADIUSRADIUSServerEntryServerIPAddress_Type()
)
lcosLXSetupRADIUSRADIUSServerEntryServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSRADIUSServerEntryServerIPAddress.setStatus("current")


class _LcosLXSetupRADIUSRADIUSServerEntryAccountingPort_Type(Unsigned32):
    """Custom type lcosLXSetupRADIUSRADIUSServerEntryAccountingPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupRADIUSRADIUSServerEntryAccountingPort_Type.__name__ = "Unsigned32"
_LcosLXSetupRADIUSRADIUSServerEntryAccountingPort_Object = MibTableColumn
lcosLXSetupRADIUSRADIUSServerEntryAccountingPort = _LcosLXSetupRADIUSRADIUSServerEntryAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 3, 1, 9),
    _LcosLXSetupRADIUSRADIUSServerEntryAccountingPort_Type()
)
lcosLXSetupRADIUSRADIUSServerEntryAccountingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSRADIUSServerEntryAccountingPort.setStatus("current")


class _LcosLXSetupRADIUSRADIUSServerEntryAccountingIPAddress_Type(OctetString):
    """Custom type lcosLXSetupRADIUSRADIUSServerEntryAccountingIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupRADIUSRADIUSServerEntryAccountingIPAddress_Type.__name__ = "OctetString"
_LcosLXSetupRADIUSRADIUSServerEntryAccountingIPAddress_Object = MibTableColumn
lcosLXSetupRADIUSRADIUSServerEntryAccountingIPAddress = _LcosLXSetupRADIUSRADIUSServerEntryAccountingIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 3, 1, 14),
    _LcosLXSetupRADIUSRADIUSServerEntryAccountingIPAddress_Type()
)
lcosLXSetupRADIUSRADIUSServerEntryAccountingIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSRADIUSServerEntryAccountingIPAddress.setStatus("current")


class _LcosLXSetupRADIUSRADIUSServerEntryMACCheck_Type(Integer32):
    """Custom type lcosLXSetupRADIUSRADIUSServerEntryMACCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupRADIUSRADIUSServerEntryMACCheck_Type.__name__ = "Integer32"
_LcosLXSetupRADIUSRADIUSServerEntryMACCheck_Object = MibTableColumn
lcosLXSetupRADIUSRADIUSServerEntryMACCheck = _LcosLXSetupRADIUSRADIUSServerEntryMACCheck_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 3, 1, 15),
    _LcosLXSetupRADIUSRADIUSServerEntryMACCheck_Type()
)
lcosLXSetupRADIUSRADIUSServerEntryMACCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSRADIUSServerEntryMACCheck.setStatus("current")


class _LcosLXSetupRADIUSRADIUSServerEntryFallbackDynamicVLANID_Type(Unsigned32):
    """Custom type lcosLXSetupRADIUSRADIUSServerEntryFallbackDynamicVLANID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupRADIUSRADIUSServerEntryFallbackDynamicVLANID_Type.__name__ = "Unsigned32"
_LcosLXSetupRADIUSRADIUSServerEntryFallbackDynamicVLANID_Object = MibTableColumn
lcosLXSetupRADIUSRADIUSServerEntryFallbackDynamicVLANID = _LcosLXSetupRADIUSRADIUSServerEntryFallbackDynamicVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 3, 1, 16),
    _LcosLXSetupRADIUSRADIUSServerEntryFallbackDynamicVLANID_Type()
)
lcosLXSetupRADIUSRADIUSServerEntryFallbackDynamicVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSRADIUSServerEntryFallbackDynamicVLANID.setStatus("current")
_LcosLXSetupRADIUSSupplicantIfcSetup_Object = MibTable
lcosLXSetupRADIUSSupplicantIfcSetup = _LcosLXSetupRADIUSSupplicantIfcSetup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 11)
)
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSSupplicantIfcSetup.setStatus("current")
_LcosLXSetupRADIUSSupplicantIfcSetupEntry_Object = MibTableRow
lcosLXSetupRADIUSSupplicantIfcSetupEntry = _LcosLXSetupRADIUSSupplicantIfcSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 11, 1)
)
lcosLXSetupRADIUSSupplicantIfcSetupEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupRADIUSSupplicantIfcSetupEntryInterfaceName"),
)
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSSupplicantIfcSetupEntry.setStatus("current")


class _LcosLXSetupRADIUSSupplicantIfcSetupEntryInterfaceName_Type(OctetString):
    """Custom type lcosLXSetupRADIUSSupplicantIfcSetupEntryInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupRADIUSSupplicantIfcSetupEntryInterfaceName_Type.__name__ = "OctetString"
_LcosLXSetupRADIUSSupplicantIfcSetupEntryInterfaceName_Object = MibTableColumn
lcosLXSetupRADIUSSupplicantIfcSetupEntryInterfaceName = _LcosLXSetupRADIUSSupplicantIfcSetupEntryInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 11, 1, 1),
    _LcosLXSetupRADIUSSupplicantIfcSetupEntryInterfaceName_Type()
)
lcosLXSetupRADIUSSupplicantIfcSetupEntryInterfaceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSSupplicantIfcSetupEntryInterfaceName.setStatus("current")


class _LcosLXSetupRADIUSSupplicantIfcSetupEntryMethod_Type(Integer32):
    """Custom type lcosLXSetupRADIUSSupplicantIfcSetupEntryMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1024,
              3328,
              4352,
              5380,
              5383,
              5384,
              5402,
              5567,
              6406,
              6426)
        )
    )
    namedValues = NamedValues(
        *(("enone", 0),
          ("eMD5", 1024),
          ("eTLS", 3328),
          ("eLEAP", 4352),
          ("eTTLSMD5", 5380),
          ("eTTLSPAP", 5383),
          ("eTTLSCHAP", 5384),
          ("eTTLSMSCHAPv2", 5402),
          ("eTTLSMSCHAP", 5567),
          ("ePEAPGTC", 6406),
          ("ePEAPMSCHAPv2", 6426))
    )


_LcosLXSetupRADIUSSupplicantIfcSetupEntryMethod_Type.__name__ = "Integer32"
_LcosLXSetupRADIUSSupplicantIfcSetupEntryMethod_Object = MibTableColumn
lcosLXSetupRADIUSSupplicantIfcSetupEntryMethod = _LcosLXSetupRADIUSSupplicantIfcSetupEntryMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 11, 1, 2),
    _LcosLXSetupRADIUSSupplicantIfcSetupEntryMethod_Type()
)
lcosLXSetupRADIUSSupplicantIfcSetupEntryMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSSupplicantIfcSetupEntryMethod.setStatus("current")


class _LcosLXSetupRADIUSSupplicantIfcSetupEntryUsername_Type(OctetString):
    """Custom type lcosLXSetupRADIUSSupplicantIfcSetupEntryUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupRADIUSSupplicantIfcSetupEntryUsername_Type.__name__ = "OctetString"
_LcosLXSetupRADIUSSupplicantIfcSetupEntryUsername_Object = MibTableColumn
lcosLXSetupRADIUSSupplicantIfcSetupEntryUsername = _LcosLXSetupRADIUSSupplicantIfcSetupEntryUsername_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 11, 1, 3),
    _LcosLXSetupRADIUSSupplicantIfcSetupEntryUsername_Type()
)
lcosLXSetupRADIUSSupplicantIfcSetupEntryUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSSupplicantIfcSetupEntryUsername.setStatus("current")


class _LcosLXSetupRADIUSSupplicantIfcSetupEntryPassword_Type(OctetString):
    """Custom type lcosLXSetupRADIUSSupplicantIfcSetupEntryPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupRADIUSSupplicantIfcSetupEntryPassword_Type.__name__ = "OctetString"
_LcosLXSetupRADIUSSupplicantIfcSetupEntryPassword_Object = MibTableColumn
lcosLXSetupRADIUSSupplicantIfcSetupEntryPassword = _LcosLXSetupRADIUSSupplicantIfcSetupEntryPassword_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 30, 11, 1, 4),
    _LcosLXSetupRADIUSSupplicantIfcSetupEntryPassword_Type()
)
lcosLXSetupRADIUSSupplicantIfcSetupEntryPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupRADIUSSupplicantIfcSetupEntryPassword.setStatus("current")
_LcosLXSetupWLANManagement_ObjectIdentity = ObjectIdentity
lcosLXSetupWLANManagement = _LcosLXSetupWLANManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 59)
)
_LcosLXSetupWLANManagementStaticWLCConfiguration_Object = MibTable
lcosLXSetupWLANManagementStaticWLCConfiguration = _LcosLXSetupWLANManagementStaticWLCConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 59, 1)
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANManagementStaticWLCConfiguration.setStatus("current")
_LcosLXSetupWLANManagementStaticWLCConfigurationEntry_Object = MibTableRow
lcosLXSetupWLANManagementStaticWLCConfigurationEntry = _LcosLXSetupWLANManagementStaticWLCConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 59, 1, 1)
)
lcosLXSetupWLANManagementStaticWLCConfigurationEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupWLANManagementStaticWLCConfigurationEntryIPAddress"),
)
if mibBuilder.loadTexts:
    lcosLXSetupWLANManagementStaticWLCConfigurationEntry.setStatus("current")


class _LcosLXSetupWLANManagementStaticWLCConfigurationEntryIPAddress_Type(OctetString):
    """Custom type lcosLXSetupWLANManagementStaticWLCConfigurationEntryIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_LcosLXSetupWLANManagementStaticWLCConfigurationEntryIPAddress_Type.__name__ = "OctetString"
_LcosLXSetupWLANManagementStaticWLCConfigurationEntryIPAddress_Object = MibTableColumn
lcosLXSetupWLANManagementStaticWLCConfigurationEntryIPAddress = _LcosLXSetupWLANManagementStaticWLCConfigurationEntryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 59, 1, 1, 1),
    _LcosLXSetupWLANManagementStaticWLCConfigurationEntryIPAddress_Type()
)
lcosLXSetupWLANManagementStaticWLCConfigurationEntryIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupWLANManagementStaticWLCConfigurationEntryIPAddress.setStatus("current")


class _LcosLXSetupWLANManagementStaticWLCConfigurationEntryPort_Type(Unsigned32):
    """Custom type lcosLXSetupWLANManagementStaticWLCConfigurationEntryPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupWLANManagementStaticWLCConfigurationEntryPort_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANManagementStaticWLCConfigurationEntryPort_Object = MibTableColumn
lcosLXSetupWLANManagementStaticWLCConfigurationEntryPort = _LcosLXSetupWLANManagementStaticWLCConfigurationEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 59, 1, 1, 2),
    _LcosLXSetupWLANManagementStaticWLCConfigurationEntryPort_Type()
)
lcosLXSetupWLANManagementStaticWLCConfigurationEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANManagementStaticWLCConfigurationEntryPort.setStatus("current")


class _LcosLXSetupWLANManagementOperating_Type(Integer32):
    """Custom type lcosLXSetupWLANManagementOperating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupWLANManagementOperating_Type.__name__ = "Integer32"
_LcosLXSetupWLANManagementOperating_Object = MibScalar
lcosLXSetupWLANManagementOperating = _LcosLXSetupWLANManagementOperating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 59, 2),
    _LcosLXSetupWLANManagementOperating_Type()
)
lcosLXSetupWLANManagementOperating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANManagementOperating.setStatus("current")


class _LcosLXSetupWLANManagementUpdateCertBefore_Type(Unsigned32):
    """Custom type lcosLXSetupWLANManagementUpdateCertBefore based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupWLANManagementUpdateCertBefore_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANManagementUpdateCertBefore_Object = MibScalar
lcosLXSetupWLANManagementUpdateCertBefore = _LcosLXSetupWLANManagementUpdateCertBefore_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 59, 3),
    _LcosLXSetupWLANManagementUpdateCertBefore_Type()
)
lcosLXSetupWLANManagementUpdateCertBefore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANManagementUpdateCertBefore.setStatus("current")


class _LcosLXSetupWLANManagementCapwapPort_Type(Unsigned32):
    """Custom type lcosLXSetupWLANManagementCapwapPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupWLANManagementCapwapPort_Type.__name__ = "Unsigned32"
_LcosLXSetupWLANManagementCapwapPort_Object = MibScalar
lcosLXSetupWLANManagementCapwapPort = _LcosLXSetupWLANManagementCapwapPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 59, 4),
    _LcosLXSetupWLANManagementCapwapPort_Type()
)
lcosLXSetupWLANManagementCapwapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupWLANManagementCapwapPort.setStatus("current")
_LcosLXSetupIPConfiguration_ObjectIdentity = ObjectIdentity
lcosLXSetupIPConfiguration = _LcosLXSetupIPConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70)
)
_LcosLXSetupIPConfigurationStaticParameters_Object = MibTable
lcosLXSetupIPConfigurationStaticParameters = _LcosLXSetupIPConfigurationStaticParameters_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 4)
)
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationStaticParameters.setStatus("current")
_LcosLXSetupIPConfigurationStaticParametersEntry_Object = MibTableRow
lcosLXSetupIPConfigurationStaticParametersEntry = _LcosLXSetupIPConfigurationStaticParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 4, 1)
)
lcosLXSetupIPConfigurationStaticParametersEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupIPConfigurationStaticParametersEntryInterfaceName"),
)
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationStaticParametersEntry.setStatus("current")


class _LcosLXSetupIPConfigurationStaticParametersEntryInterfaceName_Type(OctetString):
    """Custom type lcosLXSetupIPConfigurationStaticParametersEntryInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupIPConfigurationStaticParametersEntryInterfaceName_Type.__name__ = "OctetString"
_LcosLXSetupIPConfigurationStaticParametersEntryInterfaceName_Object = MibTableColumn
lcosLXSetupIPConfigurationStaticParametersEntryInterfaceName = _LcosLXSetupIPConfigurationStaticParametersEntryInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 4, 1, 1),
    _LcosLXSetupIPConfigurationStaticParametersEntryInterfaceName_Type()
)
lcosLXSetupIPConfigurationStaticParametersEntryInterfaceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationStaticParametersEntryInterfaceName.setStatus("current")
_LcosLXSetupIPConfigurationStaticParametersEntryIPv4Gateway_Type = IpAddress
_LcosLXSetupIPConfigurationStaticParametersEntryIPv4Gateway_Object = MibTableColumn
lcosLXSetupIPConfigurationStaticParametersEntryIPv4Gateway = _LcosLXSetupIPConfigurationStaticParametersEntryIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 4, 1, 2),
    _LcosLXSetupIPConfigurationStaticParametersEntryIPv4Gateway_Type()
)
lcosLXSetupIPConfigurationStaticParametersEntryIPv4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationStaticParametersEntryIPv4Gateway.setStatus("current")


class _LcosLXSetupIPConfigurationStaticParametersEntryIPv6Gateway_Type(OctetString):
    """Custom type lcosLXSetupIPConfigurationStaticParametersEntryIPv6Gateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_LcosLXSetupIPConfigurationStaticParametersEntryIPv6Gateway_Type.__name__ = "OctetString"
_LcosLXSetupIPConfigurationStaticParametersEntryIPv6Gateway_Object = MibTableColumn
lcosLXSetupIPConfigurationStaticParametersEntryIPv6Gateway = _LcosLXSetupIPConfigurationStaticParametersEntryIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 4, 1, 3),
    _LcosLXSetupIPConfigurationStaticParametersEntryIPv6Gateway_Type()
)
lcosLXSetupIPConfigurationStaticParametersEntryIPv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationStaticParametersEntryIPv6Gateway.setStatus("current")
_LcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv4DNS_Type = IpAddress
_LcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv4DNS_Object = MibTableColumn
lcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv4DNS = _LcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv4DNS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 4, 1, 4),
    _LcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv4DNS_Type()
)
lcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv4DNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv4DNS.setStatus("current")
_LcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv4DNS_Type = IpAddress
_LcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv4DNS_Object = MibTableColumn
lcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv4DNS = _LcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv4DNS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 4, 1, 5),
    _LcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv4DNS_Type()
)
lcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv4DNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv4DNS.setStatus("current")


class _LcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv6DNS_Type(OctetString):
    """Custom type lcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv6DNS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_LcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv6DNS_Type.__name__ = "OctetString"
_LcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv6DNS_Object = MibTableColumn
lcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv6DNS = _LcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv6DNS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 4, 1, 6),
    _LcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv6DNS_Type()
)
lcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv6DNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv6DNS.setStatus("current")


class _LcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv6DNS_Type(OctetString):
    """Custom type lcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv6DNS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_LcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv6DNS_Type.__name__ = "OctetString"
_LcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv6DNS_Object = MibTableColumn
lcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv6DNS = _LcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv6DNS_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 4, 1, 7),
    _LcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv6DNS_Type()
)
lcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv6DNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv6DNS.setStatus("current")
_LcosLXSetupIPConfigurationLANInterfaces_Object = MibTable
lcosLXSetupIPConfigurationLANInterfaces = _LcosLXSetupIPConfigurationLANInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 6)
)
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationLANInterfaces.setStatus("current")
_LcosLXSetupIPConfigurationLANInterfacesEntry_Object = MibTableRow
lcosLXSetupIPConfigurationLANInterfacesEntry = _LcosLXSetupIPConfigurationLANInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 6, 1)
)
lcosLXSetupIPConfigurationLANInterfacesEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupIPConfigurationLANInterfacesEntryInterfaceName"),
)
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationLANInterfacesEntry.setStatus("current")


class _LcosLXSetupIPConfigurationLANInterfacesEntryInterfaceName_Type(OctetString):
    """Custom type lcosLXSetupIPConfigurationLANInterfacesEntryInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupIPConfigurationLANInterfacesEntryInterfaceName_Type.__name__ = "OctetString"
_LcosLXSetupIPConfigurationLANInterfacesEntryInterfaceName_Object = MibTableColumn
lcosLXSetupIPConfigurationLANInterfacesEntryInterfaceName = _LcosLXSetupIPConfigurationLANInterfacesEntryInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 6, 1, 1),
    _LcosLXSetupIPConfigurationLANInterfacesEntryInterfaceName_Type()
)
lcosLXSetupIPConfigurationLANInterfacesEntryInterfaceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationLANInterfacesEntryInterfaceName.setStatus("current")


class _LcosLXSetupIPConfigurationLANInterfacesEntryInterfaceID_Type(OctetString):
    """Custom type lcosLXSetupIPConfigurationLANInterfacesEntryInterfaceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LcosLXSetupIPConfigurationLANInterfacesEntryInterfaceID_Type.__name__ = "OctetString"
_LcosLXSetupIPConfigurationLANInterfacesEntryInterfaceID_Object = MibTableColumn
lcosLXSetupIPConfigurationLANInterfacesEntryInterfaceID = _LcosLXSetupIPConfigurationLANInterfacesEntryInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 6, 1, 2),
    _LcosLXSetupIPConfigurationLANInterfacesEntryInterfaceID_Type()
)
lcosLXSetupIPConfigurationLANInterfacesEntryInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationLANInterfacesEntryInterfaceID.setStatus("current")


class _LcosLXSetupIPConfigurationLANInterfacesEntryVLANID_Type(Unsigned32):
    """Custom type lcosLXSetupIPConfigurationLANInterfacesEntryVLANID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupIPConfigurationLANInterfacesEntryVLANID_Type.__name__ = "Unsigned32"
_LcosLXSetupIPConfigurationLANInterfacesEntryVLANID_Object = MibTableColumn
lcosLXSetupIPConfigurationLANInterfacesEntryVLANID = _LcosLXSetupIPConfigurationLANInterfacesEntryVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 6, 1, 3),
    _LcosLXSetupIPConfigurationLANInterfacesEntryVLANID_Type()
)
lcosLXSetupIPConfigurationLANInterfacesEntryVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationLANInterfacesEntryVLANID.setStatus("current")


class _LcosLXSetupIPConfigurationLANInterfacesEntryIPv4AddressSource_Type(Integer32):
    """Custom type lcosLXSetupIPConfigurationLANInterfacesEntryIPv4AddressSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDHCP", 1),
          ("estatic", 2))
    )


_LcosLXSetupIPConfigurationLANInterfacesEntryIPv4AddressSource_Type.__name__ = "Integer32"
_LcosLXSetupIPConfigurationLANInterfacesEntryIPv4AddressSource_Object = MibTableColumn
lcosLXSetupIPConfigurationLANInterfacesEntryIPv4AddressSource = _LcosLXSetupIPConfigurationLANInterfacesEntryIPv4AddressSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 6, 1, 4),
    _LcosLXSetupIPConfigurationLANInterfacesEntryIPv4AddressSource_Type()
)
lcosLXSetupIPConfigurationLANInterfacesEntryIPv4AddressSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationLANInterfacesEntryIPv4AddressSource.setStatus("current")


class _LcosLXSetupIPConfigurationLANInterfacesEntryIPv6AddressSource_Type(Integer32):
    """Custom type lcosLXSetupIPConfigurationLANInterfacesEntryIPv6AddressSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eRouterAdvertisement", 1),
          ("eDHCPv6", 2),
          ("estatic", 3))
    )


_LcosLXSetupIPConfigurationLANInterfacesEntryIPv6AddressSource_Type.__name__ = "Integer32"
_LcosLXSetupIPConfigurationLANInterfacesEntryIPv6AddressSource_Object = MibTableColumn
lcosLXSetupIPConfigurationLANInterfacesEntryIPv6AddressSource = _LcosLXSetupIPConfigurationLANInterfacesEntryIPv6AddressSource_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 6, 1, 5),
    _LcosLXSetupIPConfigurationLANInterfacesEntryIPv6AddressSource_Type()
)
lcosLXSetupIPConfigurationLANInterfacesEntryIPv6AddressSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationLANInterfacesEntryIPv6AddressSource.setStatus("current")


class _LcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv4Address_Type(OctetString):
    """Custom type lcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv4Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_LcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv4Address_Type.__name__ = "OctetString"
_LcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv4Address_Object = MibTableColumn
lcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv4Address = _LcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 6, 1, 6),
    _LcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv4Address_Type()
)
lcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv4Address.setStatus("current")


class _LcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv6Address_Type(OctetString):
    """Custom type lcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_LcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv6Address_Type.__name__ = "OctetString"
_LcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv6Address_Object = MibTableColumn
lcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv6Address = _LcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 6, 1, 7),
    _LcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv6Address_Type()
)
lcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv6Address.setStatus("current")


class _LcosLXSetupIPConfigurationLANInterfacesEntryComment_Type(OctetString):
    """Custom type lcosLXSetupIPConfigurationLANInterfacesEntryComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LcosLXSetupIPConfigurationLANInterfacesEntryComment_Type.__name__ = "OctetString"
_LcosLXSetupIPConfigurationLANInterfacesEntryComment_Object = MibTableColumn
lcosLXSetupIPConfigurationLANInterfacesEntryComment = _LcosLXSetupIPConfigurationLANInterfacesEntryComment_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 70, 6, 1, 9),
    _LcosLXSetupIPConfigurationLANInterfacesEntryComment_Type()
)
lcosLXSetupIPConfigurationLANInterfacesEntryComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupIPConfigurationLANInterfacesEntryComment.setStatus("current")
_LcosLXSetupLBS_ObjectIdentity = ObjectIdentity
lcosLXSetupLBS = _LcosLXSetupLBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 99)
)
_LcosLXSetupLBSHTTPServer_Object = MibTable
lcosLXSetupLBSHTTPServer = _LcosLXSetupLBSHTTPServer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 99, 1)
)
if mibBuilder.loadTexts:
    lcosLXSetupLBSHTTPServer.setStatus("current")
_LcosLXSetupLBSHTTPServerEntry_Object = MibTableRow
lcosLXSetupLBSHTTPServerEntry = _LcosLXSetupLBSHTTPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 99, 1, 1)
)
lcosLXSetupLBSHTTPServerEntry.setIndexNames(
    (0, "LCOS-LX-MIB", "lcosLXSetupLBSHTTPServerEntryURL"),
)
if mibBuilder.loadTexts:
    lcosLXSetupLBSHTTPServerEntry.setStatus("current")


class _LcosLXSetupLBSHTTPServerEntryURL_Type(OctetString):
    """Custom type lcosLXSetupLBSHTTPServerEntryURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 251),
    )


_LcosLXSetupLBSHTTPServerEntryURL_Type.__name__ = "OctetString"
_LcosLXSetupLBSHTTPServerEntryURL_Object = MibTableColumn
lcosLXSetupLBSHTTPServerEntryURL = _LcosLXSetupLBSHTTPServerEntryURL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 99, 1, 1, 1),
    _LcosLXSetupLBSHTTPServerEntryURL_Type()
)
lcosLXSetupLBSHTTPServerEntryURL.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcosLXSetupLBSHTTPServerEntryURL.setStatus("current")


class _LcosLXSetupLBSHTTPServerEntrySecret_Type(OctetString):
    """Custom type lcosLXSetupLBSHTTPServerEntrySecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LcosLXSetupLBSHTTPServerEntrySecret_Type.__name__ = "OctetString"
_LcosLXSetupLBSHTTPServerEntrySecret_Object = MibTableColumn
lcosLXSetupLBSHTTPServerEntrySecret = _LcosLXSetupLBSHTTPServerEntrySecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 99, 1, 1, 3),
    _LcosLXSetupLBSHTTPServerEntrySecret_Type()
)
lcosLXSetupLBSHTTPServerEntrySecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLBSHTTPServerEntrySecret.setStatus("current")


class _LcosLXSetupLBSHTTPServerEntryDataSources_Type(Bits):
    """Custom type lcosLXSetupLBSHTTPServerEntryDataSources based on Bits"""
    namedValues = NamedValues(
        ("eBLE", 1)
    )

_LcosLXSetupLBSHTTPServerEntryDataSources_Type.__name__ = "Bits"
_LcosLXSetupLBSHTTPServerEntryDataSources_Object = MibTableColumn
lcosLXSetupLBSHTTPServerEntryDataSources = _LcosLXSetupLBSHTTPServerEntryDataSources_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 99, 1, 1, 4),
    _LcosLXSetupLBSHTTPServerEntryDataSources_Type()
)
lcosLXSetupLBSHTTPServerEntryDataSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLBSHTTPServerEntryDataSources.setStatus("current")


class _LcosLXSetupLBSHTTPServerEntryBLEMeasurementsFields_Type(Bits):
    """Custom type lcosLXSetupLBSHTTPServerEntryBLEMeasurementsFields based on Bits"""
    namedValues = NamedValues(
        *(("eBLEAddressTypeTransmit", 0),
          ("eBLEAdvertisingDataTransmit", 1),
          ("eBLENameTransmit", 2),
          ("eBLERSSITransmit", 3),
          ("eBLEScanResponseDataTransmit", 4),
          ("eNone", 32))
    )

_LcosLXSetupLBSHTTPServerEntryBLEMeasurementsFields_Type.__name__ = "Bits"
_LcosLXSetupLBSHTTPServerEntryBLEMeasurementsFields_Object = MibTableColumn
lcosLXSetupLBSHTTPServerEntryBLEMeasurementsFields = _LcosLXSetupLBSHTTPServerEntryBLEMeasurementsFields_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 99, 1, 1, 5),
    _LcosLXSetupLBSHTTPServerEntryBLEMeasurementsFields_Type()
)
lcosLXSetupLBSHTTPServerEntryBLEMeasurementsFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLBSHTTPServerEntryBLEMeasurementsFields.setStatus("current")


class _LcosLXSetupLBSHTTPServerEntryBufferingTimeout_Type(Unsigned32):
    """Custom type lcosLXSetupLBSHTTPServerEntryBufferingTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupLBSHTTPServerEntryBufferingTimeout_Type.__name__ = "Unsigned32"
_LcosLXSetupLBSHTTPServerEntryBufferingTimeout_Object = MibTableColumn
lcosLXSetupLBSHTTPServerEntryBufferingTimeout = _LcosLXSetupLBSHTTPServerEntryBufferingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 99, 1, 1, 6),
    _LcosLXSetupLBSHTTPServerEntryBufferingTimeout_Type()
)
lcosLXSetupLBSHTTPServerEntryBufferingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLBSHTTPServerEntryBufferingTimeout.setStatus("current")


class _LcosLXSetupLBSHTTPServerEntryBufferSize_Type(Unsigned32):
    """Custom type lcosLXSetupLBSHTTPServerEntryBufferSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcosLXSetupLBSHTTPServerEntryBufferSize_Type.__name__ = "Unsigned32"
_LcosLXSetupLBSHTTPServerEntryBufferSize_Object = MibTableColumn
lcosLXSetupLBSHTTPServerEntryBufferSize = _LcosLXSetupLBSHTTPServerEntryBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 99, 1, 1, 7),
    _LcosLXSetupLBSHTTPServerEntryBufferSize_Type()
)
lcosLXSetupLBSHTTPServerEntryBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLBSHTTPServerEntryBufferSize.setStatus("current")


class _LcosLXSetupLBSOperating_Type(Integer32):
    """Custom type lcosLXSetupLBSOperating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupLBSOperating_Type.__name__ = "Integer32"
_LcosLXSetupLBSOperating_Object = MibScalar
lcosLXSetupLBSOperating = _LcosLXSetupLBSOperating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 99, 2),
    _LcosLXSetupLBSOperating_Type()
)
lcosLXSetupLBSOperating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLBSOperating.setStatus("current")


class _LcosLXSetupLBSLBSServerType_Type(Integer32):
    """Custom type lcosLXSetupLBSLBSServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eHTTPJSON", 1)
    )


_LcosLXSetupLBSLBSServerType_Type.__name__ = "Integer32"
_LcosLXSetupLBSLBSServerType_Object = MibScalar
lcosLXSetupLBSLBSServerType = _LcosLXSetupLBSLBSServerType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 99, 3),
    _LcosLXSetupLBSLBSServerType_Type()
)
lcosLXSetupLBSLBSServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLBSLBSServerType.setStatus("current")


class _LcosLXSetupLBSBLEScanType_Type(Integer32):
    """Custom type lcosLXSetupLBSBLEScanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ePassive", 1),
          ("eActive", 2))
    )


_LcosLXSetupLBSBLEScanType_Type.__name__ = "Integer32"
_LcosLXSetupLBSBLEScanType_Object = MibScalar
lcosLXSetupLBSBLEScanType = _LcosLXSetupLBSBLEScanType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 99, 4),
    _LcosLXSetupLBSBLEScanType_Type()
)
lcosLXSetupLBSBLEScanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLBSBLEScanType.setStatus("current")
_LcosLXSetupLMC_ObjectIdentity = ObjectIdentity
lcosLXSetupLMC = _LcosLXSetupLMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 102)
)


class _LcosLXSetupLMCOperating_Type(Integer32):
    """Custom type lcosLXSetupLMCOperating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1),
          ("eOnlyWithoutWLC", 2))
    )


_LcosLXSetupLMCOperating_Type.__name__ = "Integer32"
_LcosLXSetupLMCOperating_Object = MibScalar
lcosLXSetupLMCOperating = _LcosLXSetupLMCOperating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 102, 1),
    _LcosLXSetupLMCOperating_Type()
)
lcosLXSetupLMCOperating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLMCOperating.setStatus("current")


class _LcosLXSetupLMCDHCPClientAutoRenew_Type(Integer32):
    """Custom type lcosLXSetupLMCDHCPClientAutoRenew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupLMCDHCPClientAutoRenew_Type.__name__ = "Integer32"
_LcosLXSetupLMCDHCPClientAutoRenew_Object = MibScalar
lcosLXSetupLMCDHCPClientAutoRenew = _LcosLXSetupLMCDHCPClientAutoRenew_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 102, 8),
    _LcosLXSetupLMCDHCPClientAutoRenew_Type()
)
lcosLXSetupLMCDHCPClientAutoRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLMCDHCPClientAutoRenew.setStatus("current")


class _LcosLXSetupLMCConfigurationViaDHCP_Type(Integer32):
    """Custom type lcosLXSetupLMCConfigurationViaDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eNo", 0),
          ("eYes", 1))
    )


_LcosLXSetupLMCConfigurationViaDHCP_Type.__name__ = "Integer32"
_LcosLXSetupLMCConfigurationViaDHCP_Object = MibScalar
lcosLXSetupLMCConfigurationViaDHCP = _LcosLXSetupLMCConfigurationViaDHCP_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 102, 13),
    _LcosLXSetupLMCConfigurationViaDHCP_Type()
)
lcosLXSetupLMCConfigurationViaDHCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLMCConfigurationViaDHCP.setStatus("current")


class _LcosLXSetupLMCLMCDomain_Type(OctetString):
    """Custom type lcosLXSetupLMCLMCDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LcosLXSetupLMCLMCDomain_Type.__name__ = "OctetString"
_LcosLXSetupLMCLMCDomain_Object = MibScalar
lcosLXSetupLMCLMCDomain = _LcosLXSetupLMCLMCDomain_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 102, 15),
    _LcosLXSetupLMCLMCDomain_Type()
)
lcosLXSetupLMCLMCDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLMCLMCDomain.setStatus("current")


class _LcosLXSetupLMCRolloutProjectID_Type(OctetString):
    """Custom type lcosLXSetupLMCRolloutProjectID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_LcosLXSetupLMCRolloutProjectID_Type.__name__ = "OctetString"
_LcosLXSetupLMCRolloutProjectID_Object = MibScalar
lcosLXSetupLMCRolloutProjectID = _LcosLXSetupLMCRolloutProjectID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 102, 16),
    _LcosLXSetupLMCRolloutProjectID_Type()
)
lcosLXSetupLMCRolloutProjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLMCRolloutProjectID.setStatus("current")


class _LcosLXSetupLMCRolloutLocationID_Type(OctetString):
    """Custom type lcosLXSetupLMCRolloutLocationID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_LcosLXSetupLMCRolloutLocationID_Type.__name__ = "OctetString"
_LcosLXSetupLMCRolloutLocationID_Object = MibScalar
lcosLXSetupLMCRolloutLocationID = _LcosLXSetupLMCRolloutLocationID_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 102, 17),
    _LcosLXSetupLMCRolloutLocationID_Type()
)
lcosLXSetupLMCRolloutLocationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLMCRolloutLocationID.setStatus("current")


class _LcosLXSetupLMCRolloutDeviceRole_Type(OctetString):
    """Custom type lcosLXSetupLMCRolloutDeviceRole based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_LcosLXSetupLMCRolloutDeviceRole_Type.__name__ = "OctetString"
_LcosLXSetupLMCRolloutDeviceRole_Object = MibScalar
lcosLXSetupLMCRolloutDeviceRole = _LcosLXSetupLMCRolloutDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 102, 18),
    _LcosLXSetupLMCRolloutDeviceRole_Type()
)
lcosLXSetupLMCRolloutDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLMCRolloutDeviceRole.setStatus("current")


class _LcosLXSetupLMCPairingToken_Type(OctetString):
    """Custom type lcosLXSetupLMCPairingToken based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_LcosLXSetupLMCPairingToken_Type.__name__ = "OctetString"
_LcosLXSetupLMCPairingToken_Object = MibScalar
lcosLXSetupLMCPairingToken = _LcosLXSetupLMCPairingToken_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 102, 200),
    _LcosLXSetupLMCPairingToken_Type()
)
lcosLXSetupLMCPairingToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupLMCPairingToken.setStatus("current")
_LcosLXSetupAutomaticFirmwareUpdate_ObjectIdentity = ObjectIdentity
lcosLXSetupAutomaticFirmwareUpdate = _LcosLXSetupAutomaticFirmwareUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 107)
)


class _LcosLXSetupAutomaticFirmwareUpdateMode_Type(Integer32):
    """Custom type lcosLXSetupAutomaticFirmwareUpdateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emanual", 0),
          ("echeck", 1),
          ("echeckandupdate", 2))
    )


_LcosLXSetupAutomaticFirmwareUpdateMode_Type.__name__ = "Integer32"
_LcosLXSetupAutomaticFirmwareUpdateMode_Object = MibScalar
lcosLXSetupAutomaticFirmwareUpdateMode = _LcosLXSetupAutomaticFirmwareUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 107, 1),
    _LcosLXSetupAutomaticFirmwareUpdateMode_Type()
)
lcosLXSetupAutomaticFirmwareUpdateMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupAutomaticFirmwareUpdateMode.setStatus("current")


class _LcosLXSetupAutomaticFirmwareUpdateBaseURL_Type(OctetString):
    """Custom type lcosLXSetupAutomaticFirmwareUpdateBaseURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_LcosLXSetupAutomaticFirmwareUpdateBaseURL_Type.__name__ = "OctetString"
_LcosLXSetupAutomaticFirmwareUpdateBaseURL_Object = MibScalar
lcosLXSetupAutomaticFirmwareUpdateBaseURL = _LcosLXSetupAutomaticFirmwareUpdateBaseURL_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 107, 6),
    _LcosLXSetupAutomaticFirmwareUpdateBaseURL_Type()
)
lcosLXSetupAutomaticFirmwareUpdateBaseURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupAutomaticFirmwareUpdateBaseURL.setStatus("current")


class _LcosLXSetupAutomaticFirmwareUpdateCheckInterval_Type(Integer32):
    """Custom type lcosLXSetupAutomaticFirmwareUpdateCheckInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("edaily", 0),
          ("eweekly", 1))
    )


_LcosLXSetupAutomaticFirmwareUpdateCheckInterval_Type.__name__ = "Integer32"
_LcosLXSetupAutomaticFirmwareUpdateCheckInterval_Object = MibScalar
lcosLXSetupAutomaticFirmwareUpdateCheckInterval = _LcosLXSetupAutomaticFirmwareUpdateCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 107, 7),
    _LcosLXSetupAutomaticFirmwareUpdateCheckInterval_Type()
)
lcosLXSetupAutomaticFirmwareUpdateCheckInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupAutomaticFirmwareUpdateCheckInterval.setStatus("current")


class _LcosLXSetupAutomaticFirmwareUpdateVersionPolicy_Type(Integer32):
    """Custom type lcosLXSetupAutomaticFirmwareUpdateVersionPolicy based on Integer32"""
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
        *(("elatest", 0),
          ("ecurrent", 1),
          ("esecurityupdatesonly", 2),
          ("elatestwithoutREL", 3))
    )


_LcosLXSetupAutomaticFirmwareUpdateVersionPolicy_Type.__name__ = "Integer32"
_LcosLXSetupAutomaticFirmwareUpdateVersionPolicy_Object = MibScalar
lcosLXSetupAutomaticFirmwareUpdateVersionPolicy = _LcosLXSetupAutomaticFirmwareUpdateVersionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 107, 8),
    _LcosLXSetupAutomaticFirmwareUpdateVersionPolicy_Type()
)
lcosLXSetupAutomaticFirmwareUpdateVersionPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupAutomaticFirmwareUpdateVersionPolicy.setStatus("current")


class _LcosLXSetupAutomaticFirmwareUpdateCheckTimeBegin_Type(Unsigned32):
    """Custom type lcosLXSetupAutomaticFirmwareUpdateCheckTimeBegin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXSetupAutomaticFirmwareUpdateCheckTimeBegin_Type.__name__ = "Unsigned32"
_LcosLXSetupAutomaticFirmwareUpdateCheckTimeBegin_Object = MibScalar
lcosLXSetupAutomaticFirmwareUpdateCheckTimeBegin = _LcosLXSetupAutomaticFirmwareUpdateCheckTimeBegin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 107, 10),
    _LcosLXSetupAutomaticFirmwareUpdateCheckTimeBegin_Type()
)
lcosLXSetupAutomaticFirmwareUpdateCheckTimeBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupAutomaticFirmwareUpdateCheckTimeBegin.setStatus("current")


class _LcosLXSetupAutomaticFirmwareUpdateCheckTimeEnd_Type(Unsigned32):
    """Custom type lcosLXSetupAutomaticFirmwareUpdateCheckTimeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXSetupAutomaticFirmwareUpdateCheckTimeEnd_Type.__name__ = "Unsigned32"
_LcosLXSetupAutomaticFirmwareUpdateCheckTimeEnd_Object = MibScalar
lcosLXSetupAutomaticFirmwareUpdateCheckTimeEnd = _LcosLXSetupAutomaticFirmwareUpdateCheckTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 107, 11),
    _LcosLXSetupAutomaticFirmwareUpdateCheckTimeEnd_Type()
)
lcosLXSetupAutomaticFirmwareUpdateCheckTimeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupAutomaticFirmwareUpdateCheckTimeEnd.setStatus("current")


class _LcosLXSetupAutomaticFirmwareUpdateInstallTimeBegin_Type(Unsigned32):
    """Custom type lcosLXSetupAutomaticFirmwareUpdateInstallTimeBegin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXSetupAutomaticFirmwareUpdateInstallTimeBegin_Type.__name__ = "Unsigned32"
_LcosLXSetupAutomaticFirmwareUpdateInstallTimeBegin_Object = MibScalar
lcosLXSetupAutomaticFirmwareUpdateInstallTimeBegin = _LcosLXSetupAutomaticFirmwareUpdateInstallTimeBegin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 107, 12),
    _LcosLXSetupAutomaticFirmwareUpdateInstallTimeBegin_Type()
)
lcosLXSetupAutomaticFirmwareUpdateInstallTimeBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupAutomaticFirmwareUpdateInstallTimeBegin.setStatus("current")


class _LcosLXSetupAutomaticFirmwareUpdateInstallTimeEnd_Type(Unsigned32):
    """Custom type lcosLXSetupAutomaticFirmwareUpdateInstallTimeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXSetupAutomaticFirmwareUpdateInstallTimeEnd_Type.__name__ = "Unsigned32"
_LcosLXSetupAutomaticFirmwareUpdateInstallTimeEnd_Object = MibScalar
lcosLXSetupAutomaticFirmwareUpdateInstallTimeEnd = _LcosLXSetupAutomaticFirmwareUpdateInstallTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 107, 13),
    _LcosLXSetupAutomaticFirmwareUpdateInstallTimeEnd_Type()
)
lcosLXSetupAutomaticFirmwareUpdateInstallTimeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXSetupAutomaticFirmwareUpdateInstallTimeEnd.setStatus("current")
_LcosLXSetupIoT_ObjectIdentity = ObjectIdentity
lcosLXSetupIoT = _LcosLXSetupIoT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 111)
)
_LcosLXSetupIoTWirelessePaper_ObjectIdentity = ObjectIdentity
lcosLXSetupIoTWirelessePaper = _LcosLXSetupIoTWirelessePaper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 2, 111, 88)
)
_LcosLXFirmware_ObjectIdentity = ObjectIdentity
lcosLXFirmware = _LcosLXFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 3)
)


class _LcosLXFirmwareBootcount_Type(Unsigned32):
    """Custom type lcosLXFirmwareBootcount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcosLXFirmwareBootcount_Type.__name__ = "Unsigned32"
_LcosLXFirmwareBootcount_Object = MibScalar
lcosLXFirmwareBootcount = _LcosLXFirmwareBootcount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 13, 3, 10),
    _LcosLXFirmwareBootcount_Type()
)
lcosLXFirmwareBootcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcosLXFirmwareBootcount.setStatus("current")
_LcosLXOther_ObjectIdentity = ObjectIdentity
lcosLXOther = _LcosLXOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 4)
)
_LcosLXProducts_ObjectIdentity = ObjectIdentity
lcosLXProducts = _LcosLXProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 8)
)
_LcosLXProductsAccessPoints_ObjectIdentity = ObjectIdentity
lcosLXProductsAccessPoints = _LcosLXProductsAccessPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 8, 0)
)
_LcosLXProductsAccessPointsLW500_ObjectIdentity = ObjectIdentity
lcosLXProductsAccessPointsLW500 = _LcosLXProductsAccessPointsLW500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 8, 0, 1)
)
_LcosLXProductsAccessPointsLX6400_ObjectIdentity = ObjectIdentity
lcosLXProductsAccessPointsLX6400 = _LcosLXProductsAccessPointsLX6400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 8, 0, 2)
)
_LcosLXProductsAccessPointsLX6402_ObjectIdentity = ObjectIdentity
lcosLXProductsAccessPointsLX6402 = _LcosLXProductsAccessPointsLX6402_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 8, 0, 3)
)
_LcosLXProductsAccessPointsLW600_ObjectIdentity = ObjectIdentity
lcosLXProductsAccessPointsLW600 = _LcosLXProductsAccessPointsLW600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 8, 0, 4)
)
_LcosLXProductsAccessPointsOW602_ObjectIdentity = ObjectIdentity
lcosLXProductsAccessPointsOW602 = _LcosLXProductsAccessPointsOW602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 8, 0, 5)
)
_LcosLXProductsAccessPointsLX6200E_ObjectIdentity = ObjectIdentity
lcosLXProductsAccessPointsLX6200E = _LcosLXProductsAccessPointsLX6200E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 13, 8, 0, 6)
)

# Managed Objects groups


# Notification objects

lcosLXWifiTrapAuthStation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 13, 0, 0, 1)
)
lcosLXWifiTrapAuthStation.setObjects(
      *(("LCOS-LX-MIB", "lcosLXStatusSNMPEventEntryCount"),
        ("LCOS-LX-MIB", "lcosLXStatusWLANStationEntryIdentification"))
)
if mibBuilder.loadTexts:
    lcosLXWifiTrapAuthStation.setStatus(
        "current"
    )

lcosLXWifiTrapDeAuthStation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 13, 0, 0, 2)
)
lcosLXWifiTrapDeAuthStation.setObjects(
      *(("LCOS-LX-MIB", "lcosLXStatusSNMPEventEntryCount"),
        ("LCOS-LX-MIB", "lcosLXStatusWLANStationEntryIdentification"))
)
if mibBuilder.loadTexts:
    lcosLXWifiTrapDeAuthStation.setStatus(
        "current"
    )

lcosLXWifiTrapAssStation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 13, 0, 0, 3)
)
lcosLXWifiTrapAssStation.setObjects(
      *(("LCOS-LX-MIB", "lcosLXStatusSNMPEventEntryCount"),
        ("LCOS-LX-MIB", "lcosLXStatusWLANStationEntryIdentification"))
)
if mibBuilder.loadTexts:
    lcosLXWifiTrapAssStation.setStatus(
        "current"
    )

lcosLXWifiTrapReAssStation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 13, 0, 0, 4)
)
lcosLXWifiTrapReAssStation.setObjects(
      *(("LCOS-LX-MIB", "lcosLXStatusSNMPEventEntryCount"),
        ("LCOS-LX-MIB", "lcosLXStatusWLANStationEntryIdentification"))
)
if mibBuilder.loadTexts:
    lcosLXWifiTrapReAssStation.setStatus(
        "current"
    )

lcosLXWifiTrapDisAssStation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 13, 0, 0, 5)
)
lcosLXWifiTrapDisAssStation.setObjects(
      *(("LCOS-LX-MIB", "lcosLXStatusSNMPEventEntryCount"),
        ("LCOS-LX-MIB", "lcosLXStatusWLANStationEntryIdentification"))
)
if mibBuilder.loadTexts:
    lcosLXWifiTrapDisAssStation.setStatus(
        "current"
    )

lcosLXWifiTrapAssRej = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 13, 0, 0, 6)
)
lcosLXWifiTrapAssRej.setObjects(
      *(("LCOS-LX-MIB", "lcosLXStatusSNMPEventEntryCount"),
        ("LCOS-LX-MIB", "lcosLXStatusWLANStationEntryIdentification"))
)
if mibBuilder.loadTexts:
    lcosLXWifiTrapAssRej.setStatus(
        "current"
    )

lcosLXWifiTrapConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 13, 0, 0, 7)
)
lcosLXWifiTrapConnected.setObjects(
      *(("LCOS-LX-MIB", "lcosLXStatusSNMPEventEntryCount"),
        ("LCOS-LX-MIB", "lcosLXStatusWLANStationEntryIdentification"))
)
if mibBuilder.loadTexts:
    lcosLXWifiTrapConnected.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LCOS-LX-MIB",
    **{"lcosLX": lcosLX,
       "lcosLXTrapsGrp": lcosLXTrapsGrp,
       "lcosLXWifiTraps": lcosLXWifiTraps,
       "lcosLXWifiTrapAuthStation": lcosLXWifiTrapAuthStation,
       "lcosLXWifiTrapDeAuthStation": lcosLXWifiTrapDeAuthStation,
       "lcosLXWifiTrapAssStation": lcosLXWifiTrapAssStation,
       "lcosLXWifiTrapReAssStation": lcosLXWifiTrapReAssStation,
       "lcosLXWifiTrapDisAssStation": lcosLXWifiTrapDisAssStation,
       "lcosLXWifiTrapAssRej": lcosLXWifiTrapAssRej,
       "lcosLXWifiTrapConnected": lcosLXWifiTrapConnected,
       "lcosLXStatus": lcosLXStatus,
       "lcosLXStatusOperatingTime": lcosLXStatusOperatingTime,
       "lcosLXStatusWLAN": lcosLXStatusWLAN,
       "lcosLXStatusWLANEnvironmentScanStatus": lcosLXStatusWLANEnvironmentScanStatus,
       "lcosLXStatusWLANEnvironmentScanStatusShort": lcosLXStatusWLANEnvironmentScanStatusShort,
       "lcosLXStatusWLANClientManagement": lcosLXStatusWLANClientManagement,
       "lcosLXStatusWLANClientManagementStationTable": lcosLXStatusWLANClientManagementStationTable,
       "lcosLXStatusWLANClientManagementStationEntry": lcosLXStatusWLANClientManagementStationEntry,
       "lcosLXStatusWLANClientManagementStationEntryMACAddress": lcosLXStatusWLANClientManagementStationEntryMACAddress,
       "lcosLXStatusWLANClientManagementStationEntryChannel": lcosLXStatusWLANClientManagementStationEntryChannel,
       "lcosLXStatusWLANClientManagementStationEntryActive": lcosLXStatusWLANClientManagementStationEntryActive,
       "lcosLXStatusWLANClientManagementStationEntryDualBand": lcosLXStatusWLANClientManagementStationEntryDualBand,
       "lcosLXStatusWLANClientManagementStationEntryBTMSupport": lcosLXStatusWLANClientManagementStationEntryBTMSupport,
       "lcosLXStatusWLANClientManagementStationEntryRRMSupport": lcosLXStatusWLANClientManagementStationEntryRRMSupport,
       "lcosLXStatusWLANClientManagementStationEntryBTMUnfriendly": lcosLXStatusWLANClientManagementStationEntryBTMUnfriendly,
       "lcosLXStatusWLANClientManagementStationEntryBTMCompliance": lcosLXStatusWLANClientManagementStationEntryBTMCompliance,
       "lcosLXStatusWLANClientManagementStationEntrySteeringUnfriendly": lcosLXStatusWLANClientManagementStationEntrySteeringUnfriendly,
       "lcosLXStatusWLANClientManagementStationEntrySteeringProhibited": lcosLXStatusWLANClientManagementStationEntrySteeringProhibited,
       "lcosLXStatusWLANClientManagementChannelTable": lcosLXStatusWLANClientManagementChannelTable,
       "lcosLXStatusWLANClientManagementChannelEntry": lcosLXStatusWLANClientManagementChannelEntry,
       "lcosLXStatusWLANClientManagementChannelEntryChannel": lcosLXStatusWLANClientManagementChannelEntryChannel,
       "lcosLXStatusWLANClientManagementChannelEntryUtilization": lcosLXStatusWLANClientManagementChannelEntryUtilization,
       "lcosLXStatusWLANClientManagementChannelEntryOverload": lcosLXStatusWLANClientManagementChannelEntryOverload,
       "lcosLXStatusWLANClientManagementSteeringLog": lcosLXStatusWLANClientManagementSteeringLog,
       "lcosLXStatusWLANClientManagementSteeringLogEntry": lcosLXStatusWLANClientManagementSteeringLogEntry,
       "lcosLXStatusWLANClientManagementSteeringLogEntryID": lcosLXStatusWLANClientManagementSteeringLogEntryID,
       "lcosLXStatusWLANClientManagementSteeringLogEntryTimestampEpoch": lcosLXStatusWLANClientManagementSteeringLogEntryTimestampEpoch,
       "lcosLXStatusWLANClientManagementSteeringLogEntryTimestamp": lcosLXStatusWLANClientManagementSteeringLogEntryTimestamp,
       "lcosLXStatusWLANClientManagementSteeringLogEntryMACAddress": lcosLXStatusWLANClientManagementSteeringLogEntryMACAddress,
       "lcosLXStatusWLANClientManagementSteeringLogEntryReason": lcosLXStatusWLANClientManagementSteeringLogEntryReason,
       "lcosLXStatusWLANClientManagementSteeringLogEntryChannel": lcosLXStatusWLANClientManagementSteeringLogEntryChannel,
       "lcosLXStatusWLANClientManagementSteeringLogEntryCandidates": lcosLXStatusWLANClientManagementSteeringLogEntryCandidates,
       "lcosLXStatusWLANClientManagementSteeringLogEntryType": lcosLXStatusWLANClientManagementSteeringLogEntryType,
       "lcosLXStatusWLANClientManagementSteeringLogEntryState": lcosLXStatusWLANClientManagementSteeringLogEntryState,
       "lcosLXStatusWLANAutomaticEnvironmentScanTime": lcosLXStatusWLANAutomaticEnvironmentScanTime,
       "lcosLXStatusWLANHotspots": lcosLXStatusWLANHotspots,
       "lcosLXStatusWLANHotspotsHotspots": lcosLXStatusWLANHotspotsHotspots,
       "lcosLXStatusWLANHotspotsHotspotsEntry": lcosLXStatusWLANHotspotsHotspotsEntry,
       "lcosLXStatusWLANHotspotsHotspotsEntryHotspot": lcosLXStatusWLANHotspotsHotspotsEntryHotspot,
       "lcosLXStatusWLANHotspotsHotspotsEntryMACAddress": lcosLXStatusWLANHotspotsHotspotsEntryMACAddress,
       "lcosLXStatusWLANHotspotsHotspotsEntryLastLoggedIn": lcosLXStatusWLANHotspotsHotspotsEntryLastLoggedIn,
       "lcosLXStatusWLANHotspotsHotspotsEntryValidUntil": lcosLXStatusWLANHotspotsHotspotsEntryValidUntil,
       "lcosLXStatusWLANStationTable": lcosLXStatusWLANStationTable,
       "lcosLXStatusWLANStationEntry": lcosLXStatusWLANStationEntry,
       "lcosLXStatusWLANStationEntryRadioBand": lcosLXStatusWLANStationEntryRadioBand,
       "lcosLXStatusWLANStationEntryIfc": lcosLXStatusWLANStationEntryIfc,
       "lcosLXStatusWLANStationEntryMACAddress": lcosLXStatusWLANStationEntryMACAddress,
       "lcosLXStatusWLANStationEntryTxBytes": lcosLXStatusWLANStationEntryTxBytes,
       "lcosLXStatusWLANStationEntryRxBytes": lcosLXStatusWLANStationEntryRxBytes,
       "lcosLXStatusWLANStationEntryIdentification": lcosLXStatusWLANStationEntryIdentification,
       "lcosLXStatusWLANStationEntryState": lcosLXStatusWLANStationEntryState,
       "lcosLXStatusWLANStationEntryInterface": lcosLXStatusWLANStationEntryInterface,
       "lcosLXStatusWLANStationEntryConnectTime": lcosLXStatusWLANStationEntryConnectTime,
       "lcosLXStatusWLANStationEntryThroughput": lcosLXStatusWLANStationEntryThroughput,
       "lcosLXStatusWLANStationEntryPhySignal": lcosLXStatusWLANStationEntryPhySignal,
       "lcosLXStatusWLANStationEntryIPv4Address": lcosLXStatusWLANStationEntryIPv4Address,
       "lcosLXStatusWLANStationEntryWPAVersion": lcosLXStatusWLANStationEntryWPAVersion,
       "lcosLXStatusWLANStationEntryVLANId": lcosLXStatusWLANStationEntryVLANId,
       "lcosLXStatusWLANStationEntryUserName": lcosLXStatusWLANStationEntryUserName,
       "lcosLXStatusWLANStationEntryIdleTimeout": lcosLXStatusWLANStationEntryIdleTimeout,
       "lcosLXStatusWLANStationEntryEffTxRate": lcosLXStatusWLANStationEntryEffTxRate,
       "lcosLXStatusWLANStationEntryEffRxRate": lcosLXStatusWLANStationEntryEffRxRate,
       "lcosLXStatusWLANStationEntryFastRoaming": lcosLXStatusWLANStationEntryFastRoaming,
       "lcosLXStatusWLANStationEntryWPA2KeyManagement": lcosLXStatusWLANStationEntryWPA2KeyManagement,
       "lcosLXStatusWLANStationEntryChannelBandwidths": lcosLXStatusWLANStationEntryChannelBandwidths,
       "lcosLXStatusWLANStationEntryOperationMode": lcosLXStatusWLANStationEntryOperationMode,
       "lcosLXStatusWLANStationEntryDHCPHostname": lcosLXStatusWLANStationEntryDHCPHostname,
       "lcosLXStatusWLANStationEntryMaxSpatialStreams": lcosLXStatusWLANStationEntryMaxSpatialStreams,
       "lcosLXStatusWLANStationEntryPhySignaldBm": lcosLXStatusWLANStationEntryPhySignaldBm,
       "lcosLXStatusWLANStationEntryNetworkName": lcosLXStatusWLANStationEntryNetworkName,
       "lcosLXStatusWLANStationEntrySSID": lcosLXStatusWLANStationEntrySSID,
       "lcosLXStatusWLANIAPPTable": lcosLXStatusWLANIAPPTable,
       "lcosLXStatusWLANIAPPEntry": lcosLXStatusWLANIAPPEntry,
       "lcosLXStatusWLANIAPPEntryIPAddress": lcosLXStatusWLANIAPPEntryIPAddress,
       "lcosLXStatusWLANIAPPEntryBSSID": lcosLXStatusWLANIAPPEntryBSSID,
       "lcosLXStatusWLANIAPPEntrySSID": lcosLXStatusWLANIAPPEntrySSID,
       "lcosLXStatusWLANIAPPEntryRadioChannel": lcosLXStatusWLANIAPPEntryRadioChannel,
       "lcosLXStatusWLANIAPPEntryDomainID": lcosLXStatusWLANIAPPEntryDomainID,
       "lcosLXStatusWLANIAPPEntryLoad": lcosLXStatusWLANIAPPEntryLoad,
       "lcosLXStatusWLANChannelScanResults": lcosLXStatusWLANChannelScanResults,
       "lcosLXStatusWLANChannelScanResultsEntry": lcosLXStatusWLANChannelScanResultsEntry,
       "lcosLXStatusWLANChannelScanResultsEntryRadioChannel": lcosLXStatusWLANChannelScanResultsEntryRadioChannel,
       "lcosLXStatusWLANChannelScanResultsEntryInterface": lcosLXStatusWLANChannelScanResultsEntryInterface,
       "lcosLXStatusWLANChannelScanResultsEntryRadioBand": lcosLXStatusWLANChannelScanResultsEntryRadioBand,
       "lcosLXStatusWLANChannelScanResultsEntryDFSState": lcosLXStatusWLANChannelScanResultsEntryDFSState,
       "lcosLXStatusWLANChannelScanResultsEntryDFSScanAge": lcosLXStatusWLANChannelScanResultsEntryDFSScanAge,
       "lcosLXStatusWLANChannelScanResultsEntryChannelBandwidth": lcosLXStatusWLANChannelScanResultsEntryChannelBandwidth,
       "lcosLXStatusWLANInterfaces": lcosLXStatusWLANInterfaces,
       "lcosLXStatusWLANInterfacesEntry": lcosLXStatusWLANInterfacesEntry,
       "lcosLXStatusWLANInterfacesEntryNetworkName": lcosLXStatusWLANInterfacesEntryNetworkName,
       "lcosLXStatusWLANInterfacesEntrySSID": lcosLXStatusWLANInterfacesEntrySSID,
       "lcosLXStatusWLANInterfacesEntryRadioBand": lcosLXStatusWLANInterfacesEntryRadioBand,
       "lcosLXStatusWLANInterfacesEntryWPAPSKNumSuccess": lcosLXStatusWLANInterfacesEntryWPAPSKNumSuccess,
       "lcosLXStatusWLANInterfacesEntryWPAPSKNumFailures": lcosLXStatusWLANInterfacesEntryWPAPSKNumFailures,
       "lcosLXStatusWLANInterfacesEntryWPAPSKNumWrongPassphrase": lcosLXStatusWLANInterfacesEntryWPAPSKNumWrongPassphrase,
       "lcosLXStatusWLANInterfacesEntryIfc": lcosLXStatusWLANInterfacesEntryIfc,
       "lcosLXStatusWLANRadios": lcosLXStatusWLANRadios,
       "lcosLXStatusWLANRadiosEntry": lcosLXStatusWLANRadiosEntry,
       "lcosLXStatusWLANRadiosEntryIfc": lcosLXStatusWLANRadiosEntryIfc,
       "lcosLXStatusWLANRadiosEntryRadioBand": lcosLXStatusWLANRadiosEntryRadioBand,
       "lcosLXStatusWLANRadiosEntryRadioChannel": lcosLXStatusWLANRadiosEntryRadioChannel,
       "lcosLXStatusWLANRadiosEntryNoiseFloor": lcosLXStatusWLANRadiosEntryNoiseFloor,
       "lcosLXStatusWLANRadiosEntryNoiseLevel": lcosLXStatusWLANRadiosEntryNoiseLevel,
       "lcosLXStatusWLANRadiosEntryModemLoad": lcosLXStatusWLANRadiosEntryModemLoad,
       "lcosLXStatusWLANRadiosEntryTransmitPower": lcosLXStatusWLANRadiosEntryTransmitPower,
       "lcosLXStatusWLANRadiosEntryEIRP": lcosLXStatusWLANRadiosEntryEIRP,
       "lcosLXStatusWLANRadiosEntryMode": lcosLXStatusWLANRadiosEntryMode,
       "lcosLXStatusWLANRadiosEntryChannelBandwidth": lcosLXStatusWLANRadiosEntryChannelBandwidth,
       "lcosLXStatusWLANRadiosEntryRxErrorRatio": lcosLXStatusWLANRadiosEntryRxErrorRatio,
       "lcosLXStatusWLANRadiosEntryTxErrorRatio": lcosLXStatusWLANRadiosEntryTxErrorRatio,
       "lcosLXStatusWLANRadiosEntryRxBytes": lcosLXStatusWLANRadiosEntryRxBytes,
       "lcosLXStatusWLANRadiosEntryTxBytes": lcosLXStatusWLANRadiosEntryTxBytes,
       "lcosLXStatusWLANRadiosEntryModemLoadMin": lcosLXStatusWLANRadiosEntryModemLoadMin,
       "lcosLXStatusWLANRadiosEntryModemLoadMax": lcosLXStatusWLANRadiosEntryModemLoadMax,
       "lcosLXStatusWLANRadiosEntryModemLoadAverage": lcosLXStatusWLANRadiosEntryModemLoadAverage,
       "lcosLXStatusWLANRadiosEntryTemperatureDegrees": lcosLXStatusWLANRadiosEntryTemperatureDegrees,
       "lcosLXStatusWLANRadiosEntryAllChannelsBlocked": lcosLXStatusWLANRadiosEntryAllChannelsBlocked,
       "lcosLXStatusWLANEnvironmentScanResults": lcosLXStatusWLANEnvironmentScanResults,
       "lcosLXStatusWLANEnvironmentScanResultsEntry": lcosLXStatusWLANEnvironmentScanResultsEntry,
       "lcosLXStatusWLANEnvironmentScanResultsEntryBSSID": lcosLXStatusWLANEnvironmentScanResultsEntryBSSID,
       "lcosLXStatusWLANEnvironmentScanResultsEntrySSID": lcosLXStatusWLANEnvironmentScanResultsEntrySSID,
       "lcosLXStatusWLANEnvironmentScanResultsEntryIfc": lcosLXStatusWLANEnvironmentScanResultsEntryIfc,
       "lcosLXStatusWLANEnvironmentScanResultsEntryRadioChannel": lcosLXStatusWLANEnvironmentScanResultsEntryRadioChannel,
       "lcosLXStatusWLANEnvironmentScanResultsEntryRadioBand": lcosLXStatusWLANEnvironmentScanResultsEntryRadioBand,
       "lcosLXStatusWLANEnvironmentScanResultsEntrySignalLevel": lcosLXStatusWLANEnvironmentScanResultsEntrySignalLevel,
       "lcosLXStatusWLANEnvironmentScanResultsEntrySignalLevelPercent": lcosLXStatusWLANEnvironmentScanResultsEntrySignalLevelPercent,
       "lcosLXStatusWLANEnvironmentScanResultsEntryChannelBandwidth": lcosLXStatusWLANEnvironmentScanResultsEntryChannelBandwidth,
       "lcosLXStatusWLANChannelsAllowedByRegulatory": lcosLXStatusWLANChannelsAllowedByRegulatory,
       "lcosLXStatusWLANChannelsAllowedByRegulatoryEntry": lcosLXStatusWLANChannelsAllowedByRegulatoryEntry,
       "lcosLXStatusWLANChannelsAllowedByRegulatoryEntryChannel": lcosLXStatusWLANChannelsAllowedByRegulatoryEntryChannel,
       "lcosLXStatusWLANChannelsAllowedByRegulatoryEntryOutdoor": lcosLXStatusWLANChannelsAllowedByRegulatoryEntryOutdoor,
       "lcosLXStatusWLANChannelsAllowedByRegulatoryEntryDFS": lcosLXStatusWLANChannelsAllowedByRegulatoryEntryDFS,
       "lcosLXStatusWLANChannelsAllowedByRegulatoryEntryWeatherRadarChan": lcosLXStatusWLANChannelsAllowedByRegulatoryEntryWeatherRadarChan,
       "lcosLXStatusWLANChannelsAllowedByRegulatoryEntryRadioBand": lcosLXStatusWLANChannelsAllowedByRegulatoryEntryRadioBand,
       "lcosLXStatusLAN": lcosLXStatusLAN,
       "lcosLXStatusLANByteTransport": lcosLXStatusLANByteTransport,
       "lcosLXStatusLANByteTransportEntry": lcosLXStatusLANByteTransportEntry,
       "lcosLXStatusLANByteTransportEntryPort": lcosLXStatusLANByteTransportEntryPort,
       "lcosLXStatusLANByteTransportEntryTxBytes": lcosLXStatusLANByteTransportEntryTxBytes,
       "lcosLXStatusLANByteTransportEntryRxBytes": lcosLXStatusLANByteTransportEntryRxBytes,
       "lcosLXStatusLANByteTransportEntryRxCRCErrors": lcosLXStatusLANByteTransportEntryRxCRCErrors,
       "lcosLXStatusLANPorts": lcosLXStatusLANPorts,
       "lcosLXStatusLANPortsEntry": lcosLXStatusLANPortsEntry,
       "lcosLXStatusLANPortsEntryPort": lcosLXStatusLANPortsEntryPort,
       "lcosLXStatusLANPortsEntryLinkActive": lcosLXStatusLANPortsEntryLinkActive,
       "lcosLXStatusLANPortsEntryConnector": lcosLXStatusLANPortsEntryConnector,
       "lcosLXStatusLANPortsEntryMACAddress": lcosLXStatusLANPortsEntryMACAddress,
       "lcosLXStatusConfig": lcosLXStatusConfig,
       "lcosLXStatusConfigServices": lcosLXStatusConfigServices,
       "lcosLXStatusConfigServicesEntry": lcosLXStatusConfigServicesEntry,
       "lcosLXStatusConfigServicesEntryService": lcosLXStatusConfigServicesEntryService,
       "lcosLXStatusConfigServicesEntryPort": lcosLXStatusConfigServicesEntryPort,
       "lcosLXStatusConfigServicesEntryProtocol": lcosLXStatusConfigServicesEntryProtocol,
       "lcosLXStatusConfigServicesEntryActive": lcosLXStatusConfigServicesEntryActive,
       "lcosLXStatusConfigServicesEntryLAN": lcosLXStatusConfigServicesEntryLAN,
       "lcosLXStatusConfigServicesEntryWLAN": lcosLXStatusConfigServicesEntryWLAN,
       "lcosLXStatusCurrentTime": lcosLXStatusCurrentTime,
       "lcosLXStatusCurrentTimeEpoch": lcosLXStatusCurrentTimeEpoch,
       "lcosLXStatusDHCPClient": lcosLXStatusDHCPClient,
       "lcosLXStatusDHCPClientLMCDomain": lcosLXStatusDHCPClientLMCDomain,
       "lcosLXStatusDHCPClientRolloutProjectID": lcosLXStatusDHCPClientRolloutProjectID,
       "lcosLXStatusDHCPClientRolloutLocationID": lcosLXStatusDHCPClientRolloutLocationID,
       "lcosLXStatusSNMP": lcosLXStatusSNMP,
       "lcosLXStatusSNMPEvent": lcosLXStatusSNMPEvent,
       "lcosLXStatusSNMPEventEntry": lcosLXStatusSNMPEventEntry,
       "lcosLXStatusSNMPEventEntryTrapID": lcosLXStatusSNMPEventEntryTrapID,
       "lcosLXStatusSNMPEventEntryGroup": lcosLXStatusSNMPEventEntryGroup,
       "lcosLXStatusSNMPEventEntryName": lcosLXStatusSNMPEventEntryName,
       "lcosLXStatusSNMPEventEntryCount": lcosLXStatusSNMPEventEntryCount,
       "lcosLXStatusHardwareInfo": lcosLXStatusHardwareInfo,
       "lcosLXStatusHardwareInfoTotalMemoryKbytes": lcosLXStatusHardwareInfoTotalMemoryKbytes,
       "lcosLXStatusHardwareInfoFreeMemoryKbytes": lcosLXStatusHardwareInfoFreeMemoryKbytes,
       "lcosLXStatusHardwareInfoSerialNumber": lcosLXStatusHardwareInfoSerialNumber,
       "lcosLXStatusHardwareInfoBoardRevision": lcosLXStatusHardwareInfoBoardRevision,
       "lcosLXStatusHardwareInfoSWVersion": lcosLXStatusHardwareInfoSWVersion,
       "lcosLXStatusHardwareInfoCPULoad60sPercent": lcosLXStatusHardwareInfoCPULoad60sPercent,
       "lcosLXStatusHardwareInfoProductiondate": lcosLXStatusHardwareInfoProductiondate,
       "lcosLXStatusWLANManagement": lcosLXStatusWLANManagement,
       "lcosLXStatusWLANManagementAPConnections": lcosLXStatusWLANManagementAPConnections,
       "lcosLXStatusWLANManagementAPConnectionsEntry": lcosLXStatusWLANManagementAPConnectionsEntry,
       "lcosLXStatusWLANManagementAPConnectionsEntryIPAddress": lcosLXStatusWLANManagementAPConnectionsEntryIPAddress,
       "lcosLXStatusWLANManagementAPConnectionsEntryPort": lcosLXStatusWLANManagementAPConnectionsEntryPort,
       "lcosLXStatusWLANManagementAPConnectionsEntryRespTime": lcosLXStatusWLANManagementAPConnectionsEntryRespTime,
       "lcosLXStatusWLANManagementAPConnectionsEntryName": lcosLXStatusWLANManagementAPConnectionsEntryName,
       "lcosLXStatusWLANManagementAPConnectionsEntryState": lcosLXStatusWLANManagementAPConnectionsEntryState,
       "lcosLXStatusWLANManagementAPConnectionsEntryResult": lcosLXStatusWLANManagementAPConnectionsEntryResult,
       "lcosLXStatusWLANManagementAPConnectionsEntryUtilisation": lcosLXStatusWLANManagementAPConnectionsEntryUtilisation,
       "lcosLXStatusWLANManagementAPConnectionsEntryFirmwareVersion": lcosLXStatusWLANManagementAPConnectionsEntryFirmwareVersion,
       "lcosLXStatusWLANManagementAPConnectionsEntryPMTU": lcosLXStatusWLANManagementAPConnectionsEntryPMTU,
       "lcosLXStatusWLANManagementAPConnectionsEntryPreference": lcosLXStatusWLANManagementAPConnectionsEntryPreference,
       "lcosLXStatusWLANManagementAPConnectionsEntryCPULoad300sPercent": lcosLXStatusWLANManagementAPConnectionsEntryCPULoad300sPercent,
       "lcosLXStatusWLANManagementAPConnectionsEntryRetransmissions": lcosLXStatusWLANManagementAPConnectionsEntryRetransmissions,
       "lcosLXStatusWLANManagementState": lcosLXStatusWLANManagementState,
       "lcosLXStatusWLANManagementStarted": lcosLXStatusWLANManagementStarted,
       "lcosLXStatusWLANManagementDNSSuffix": lcosLXStatusWLANManagementDNSSuffix,
       "lcosLXStatusWLANManagementRadioprofiles": lcosLXStatusWLANManagementRadioprofiles,
       "lcosLXStatusWLANManagementRadioprofilesEntry": lcosLXStatusWLANManagementRadioprofilesEntry,
       "lcosLXStatusWLANManagementRadioprofilesEntryName": lcosLXStatusWLANManagementRadioprofilesEntryName,
       "lcosLXStatusWLANManagementRadioprofilesEntryCountry": lcosLXStatusWLANManagementRadioprofilesEntryCountry,
       "lcosLXStatusWLANManagementRadioprofilesEntry24GHzMode": lcosLXStatusWLANManagementRadioprofilesEntry24GHzMode,
       "lcosLXStatusWLANManagementRadioprofilesEntry5GHzMode": lcosLXStatusWLANManagementRadioprofilesEntry5GHzMode,
       "lcosLXStatusWLANManagementRadioprofilesEntrySubbands": lcosLXStatusWLANManagementRadioprofilesEntrySubbands,
       "lcosLXStatusWLANManagementRadioprofilesEntryQoS": lcosLXStatusWLANManagementRadioprofilesEntryQoS,
       "lcosLXStatusWLANManagementRadioprofilesEntryDTIMPeriod": lcosLXStatusWLANManagementRadioprofilesEntryDTIMPeriod,
       "lcosLXStatusWLANManagementRadioprofilesEntryBackgroundScan": lcosLXStatusWLANManagementRadioprofilesEntryBackgroundScan,
       "lcosLXStatusWLANManagementRadioprofilesEntryAntennaGain": lcosLXStatusWLANManagementRadioprofilesEntryAntennaGain,
       "lcosLXStatusWLANManagementRadioprofilesEntryTxPowerReduction": lcosLXStatusWLANManagementRadioprofilesEntryTxPowerReduction,
       "lcosLXStatusWLANManagementRadioprofilesEntryIndoorOnlyOperation": lcosLXStatusWLANManagementRadioprofilesEntryIndoorOnlyOperation,
       "lcosLXStatusWLANManagementRadioprofilesEntryReportSeenClients": lcosLXStatusWLANManagementRadioprofilesEntryReportSeenClients,
       "lcosLXStatusWLANManagementRadioprofilesEntryRxSensReduction": lcosLXStatusWLANManagementRadioprofilesEntryRxSensReduction,
       "lcosLXStatusWLANManagementNetworkprofiles": lcosLXStatusWLANManagementNetworkprofiles,
       "lcosLXStatusWLANManagementNetworkprofilesEntry": lcosLXStatusWLANManagementNetworkprofilesEntry,
       "lcosLXStatusWLANManagementNetworkprofilesEntryName": lcosLXStatusWLANManagementNetworkprofilesEntryName,
       "lcosLXStatusWLANManagementNetworkprofilesEntryOperating": lcosLXStatusWLANManagementNetworkprofilesEntryOperating,
       "lcosLXStatusWLANManagementNetworkprofilesEntryEncryption": lcosLXStatusWLANManagementNetworkprofilesEntryEncryption,
       "lcosLXStatusWLANManagementNetworkprofilesEntryWPA1SessKeytypes": lcosLXStatusWLANManagementNetworkprofilesEntryWPA1SessKeytypes,
       "lcosLXStatusWLANManagementNetworkprofilesEntryWPAVersion": lcosLXStatusWLANManagementNetworkprofilesEntryWPAVersion,
       "lcosLXStatusWLANManagementNetworkprofilesEntryKey": lcosLXStatusWLANManagementNetworkprofilesEntryKey,
       "lcosLXStatusWLANManagementNetworkprofilesEntryRadioBand": lcosLXStatusWLANManagementNetworkprofilesEntryRadioBand,
       "lcosLXStatusWLANManagementNetworkprofilesEntryContinuationTime": lcosLXStatusWLANManagementNetworkprofilesEntryContinuationTime,
       "lcosLXStatusWLANManagementNetworkprofilesEntryMinTxRate": lcosLXStatusWLANManagementNetworkprofilesEntryMinTxRate,
       "lcosLXStatusWLANManagementNetworkprofilesEntryMaxTxRate": lcosLXStatusWLANManagementNetworkprofilesEntryMaxTxRate,
       "lcosLXStatusWLANManagementNetworkprofilesEntryBasicRate": lcosLXStatusWLANManagementNetworkprofilesEntryBasicRate,
       "lcosLXStatusWLANManagementNetworkprofilesEntryPreamble": lcosLXStatusWLANManagementNetworkprofilesEntryPreamble,
       "lcosLXStatusWLANManagementNetworkprofilesEntryMACFilter": lcosLXStatusWLANManagementNetworkprofilesEntryMACFilter,
       "lcosLXStatusWLANManagementNetworkprofilesEntryClBrgSupport": lcosLXStatusWLANManagementNetworkprofilesEntryClBrgSupport,
       "lcosLXStatusWLANManagementNetworkprofilesEntryMaxStations": lcosLXStatusWLANManagementNetworkprofilesEntryMaxStations,
       "lcosLXStatusWLANManagementNetworkprofilesEntryClosedNetwork": lcosLXStatusWLANManagementNetworkprofilesEntryClosedNetwork,
       "lcosLXStatusWLANManagementNetworkprofilesEntrySSID": lcosLXStatusWLANManagementNetworkprofilesEntrySSID,
       "lcosLXStatusWLANManagementNetworkprofilesEntryMinHTMCS": lcosLXStatusWLANManagementNetworkprofilesEntryMinHTMCS,
       "lcosLXStatusWLANManagementNetworkprofilesEntryMaxHTMCS": lcosLXStatusWLANManagementNetworkprofilesEntryMaxHTMCS,
       "lcosLXStatusWLANManagementNetworkprofilesEntryShortGuardInterval": lcosLXStatusWLANManagementNetworkprofilesEntryShortGuardInterval,
       "lcosLXStatusWLANManagementNetworkprofilesEntryMaxSpatialStreams": lcosLXStatusWLANManagementNetworkprofilesEntryMaxSpatialStreams,
       "lcosLXStatusWLANManagementNetworkprofilesEntrySendAggregates": lcosLXStatusWLANManagementNetworkprofilesEntrySendAggregates,
       "lcosLXStatusWLANManagementNetworkprofilesEntryRADIUSAccounting": lcosLXStatusWLANManagementNetworkprofilesEntryRADIUSAccounting,
       "lcosLXStatusWLANManagementNetworkprofilesEntryVLANMode": lcosLXStatusWLANManagementNetworkprofilesEntryVLANMode,
       "lcosLXStatusWLANManagementNetworkprofilesEntryVLANId": lcosLXStatusWLANManagementNetworkprofilesEntryVLANId,
       "lcosLXStatusWLANManagementNetworkprofilesEntryRADIUSProfile": lcosLXStatusWLANManagementNetworkprofilesEntryRADIUSProfile,
       "lcosLXStatusWLANManagementNetworkprofilesEntryMinClientStrength": lcosLXStatusWLANManagementNetworkprofilesEntryMinClientStrength,
       "lcosLXStatusWLANManagementNetworkprofilesEntryIEEE80211uNetProf": lcosLXStatusWLANManagementNetworkprofilesEntryIEEE80211uNetProf,
       "lcosLXStatusWLANManagementNetworkprofilesEntryOKC": lcosLXStatusWLANManagementNetworkprofilesEntryOKC,
       "lcosLXStatusWLANManagementNetworkprofilesEntryWPA2KeyManagement": lcosLXStatusWLANManagementNetworkprofilesEntryWPA2KeyManagement,
       "lcosLXStatusWLANManagementNetworkprofilesEntryAPSD": lcosLXStatusWLANManagementNetworkprofilesEntryAPSD,
       "lcosLXStatusWLANManagementNetworkprofilesEntryProtMgmtFrames": lcosLXStatusWLANManagementNetworkprofilesEntryProtMgmtFrames,
       "lcosLXStatusWLANManagementNetworkprofilesEntryTxLimit": lcosLXStatusWLANManagementNetworkprofilesEntryTxLimit,
       "lcosLXStatusWLANManagementNetworkprofilesEntryRxLimit": lcosLXStatusWLANManagementNetworkprofilesEntryRxLimit,
       "lcosLXStatusWLANManagementNetworkprofilesEntryLBSTracking": lcosLXStatusWLANManagementNetworkprofilesEntryLBSTracking,
       "lcosLXStatusWLANManagementNetworkprofilesEntryLBSTrackingList": lcosLXStatusWLANManagementNetworkprofilesEntryLBSTrackingList,
       "lcosLXStatusWLANManagementNetworkprofilesEntryConverttoUnicast": lcosLXStatusWLANManagementNetworkprofilesEntryConverttoUnicast,
       "lcosLXStatusWLANManagementNetworkprofilesEntryTransonlyUnicast": lcosLXStatusWLANManagementNetworkprofilesEntryTransonlyUnicast,
       "lcosLXStatusWLANManagementNetworkprofilesEntryWPA23SessKeytypes": lcosLXStatusWLANManagementNetworkprofilesEntryWPA23SessKeytypes,
       "lcosLXStatusWLANManagementNetworkprofilesEntryWPA8021XSecLev": lcosLXStatusWLANManagementNetworkprofilesEntryWPA8021XSecLev,
       "lcosLXStatusWLANManagementNetworkprofilesEntryPerClientTxLimit": lcosLXStatusWLANManagementNetworkprofilesEntryPerClientTxLimit,
       "lcosLXStatusWLANManagementNetworkprofilesEntryPerClientRxLimit": lcosLXStatusWLANManagementNetworkprofilesEntryPerClientRxLimit,
       "lcosLXStatusWLANManagementRADIUSProfiles": lcosLXStatusWLANManagementRADIUSProfiles,
       "lcosLXStatusWLANManagementRADIUSProfilesEntry": lcosLXStatusWLANManagementRADIUSProfilesEntry,
       "lcosLXStatusWLANManagementRADIUSProfilesEntryName": lcosLXStatusWLANManagementRADIUSProfilesEntryName,
       "lcosLXStatusWLANManagementRADIUSProfilesEntryAccountIP": lcosLXStatusWLANManagementRADIUSProfilesEntryAccountIP,
       "lcosLXStatusWLANManagementRADIUSProfilesEntryAccountPort": lcosLXStatusWLANManagementRADIUSProfilesEntryAccountPort,
       "lcosLXStatusWLANManagementRADIUSProfilesEntryAccountSecret": lcosLXStatusWLANManagementRADIUSProfilesEntryAccountSecret,
       "lcosLXStatusWLANManagementRADIUSProfilesEntryAccountLoopback": lcosLXStatusWLANManagementRADIUSProfilesEntryAccountLoopback,
       "lcosLXStatusWLANManagementRADIUSProfilesEntryAccountProtocol": lcosLXStatusWLANManagementRADIUSProfilesEntryAccountProtocol,
       "lcosLXStatusWLANManagementRADIUSProfilesEntryAccessIP": lcosLXStatusWLANManagementRADIUSProfilesEntryAccessIP,
       "lcosLXStatusWLANManagementRADIUSProfilesEntryAccessPort": lcosLXStatusWLANManagementRADIUSProfilesEntryAccessPort,
       "lcosLXStatusWLANManagementRADIUSProfilesEntryAccessSecret": lcosLXStatusWLANManagementRADIUSProfilesEntryAccessSecret,
       "lcosLXStatusWLANManagementRADIUSProfilesEntryAccessLoopback": lcosLXStatusWLANManagementRADIUSProfilesEntryAccessLoopback,
       "lcosLXStatusWLANManagementRADIUSProfilesEntryAccessProtocol": lcosLXStatusWLANManagementRADIUSProfilesEntryAccessProtocol,
       "lcosLXStatusWLANManagementRADIUSProfilesEntryBackup": lcosLXStatusWLANManagementRADIUSProfilesEntryBackup,
       "lcosLXStatusIPConfiguration": lcosLXStatusIPConfiguration,
       "lcosLXStatusIPConfigurationAddresses": lcosLXStatusIPConfigurationAddresses,
       "lcosLXStatusIPConfigurationAddressesEntry": lcosLXStatusIPConfigurationAddressesEntry,
       "lcosLXStatusIPConfigurationAddressesEntryInterfaceName": lcosLXStatusIPConfigurationAddressesEntryInterfaceName,
       "lcosLXStatusIPConfigurationAddressesEntryIPVersion": lcosLXStatusIPConfigurationAddressesEntryIPVersion,
       "lcosLXStatusIPConfigurationAddressesEntryAddressSource": lcosLXStatusIPConfigurationAddressesEntryAddressSource,
       "lcosLXStatusIPConfigurationAddressesEntryAddress": lcosLXStatusIPConfigurationAddressesEntryAddress,
       "lcosLXStatusIPConfigurationAddressesEntryGateway": lcosLXStatusIPConfigurationAddressesEntryGateway,
       "lcosLXStatusLMC": lcosLXStatusLMC,
       "lcosLXStatusLMCTransportStatus": lcosLXStatusLMCTransportStatus,
       "lcosLXStatusLMCTransportStatusEntry": lcosLXStatusLMCTransportStatusEntry,
       "lcosLXStatusLMCTransportStatusEntryServiceName": lcosLXStatusLMCTransportStatusEntryServiceName,
       "lcosLXStatusLMCTransportStatusEntryHTTPRequests": lcosLXStatusLMCTransportStatusEntryHTTPRequests,
       "lcosLXStatusLMCTransportStatusEntryHTTPRequestErrors": lcosLXStatusLMCTransportStatusEntryHTTPRequestErrors,
       "lcosLXStatusLMCTransportStatusEntryTxBytes": lcosLXStatusLMCTransportStatusEntryTxBytes,
       "lcosLXStatusLMCTransportStatusEntryRxBytes": lcosLXStatusLMCTransportStatusEntryRxBytes,
       "lcosLXStatusLMCCustomerDeviceID": lcosLXStatusLMCCustomerDeviceID,
       "lcosLXStatusLMCRoundTripTime": lcosLXStatusLMCRoundTripTime,
       "lcosLXStatusLMCManagementStatus": lcosLXStatusLMCManagementStatus,
       "lcosLXStatusLMCControlStatus": lcosLXStatusLMCControlStatus,
       "lcosLXStatusLMCMonitorStatus": lcosLXStatusLMCMonitorStatus,
       "lcosLXStatusLMCZeroTouchSupport": lcosLXStatusLMCZeroTouchSupport,
       "lcosLXStatusLMCPairingTokenPresent": lcosLXStatusLMCPairingTokenPresent,
       "lcosLXStatusLMCConfigModified": lcosLXStatusLMCConfigModified,
       "lcosLXStatusLBS": lcosLXStatusLBS,
       "lcosLXStatusLBSBLEScanResults": lcosLXStatusLBSBLEScanResults,
       "lcosLXStatusLBSBLEScanResultsEntry": lcosLXStatusLBSBLEScanResultsEntry,
       "lcosLXStatusLBSBLEScanResultsEntryDeviceAddress": lcosLXStatusLBSBLEScanResultsEntryDeviceAddress,
       "lcosLXStatusLBSBLEScanResultsEntryAddressType": lcosLXStatusLBSBLEScanResultsEntryAddressType,
       "lcosLXStatusLBSBLEScanResultsEntryRSSI": lcosLXStatusLBSBLEScanResultsEntryRSSI,
       "lcosLXStatusLBSBLEScanResultsEntryLastSeen": lcosLXStatusLBSBLEScanResultsEntryLastSeen,
       "lcosLXStatusLBSBLEScanResultsEntryAdvertisingData": lcosLXStatusLBSBLEScanResultsEntryAdvertisingData,
       "lcosLXStatusLBSBLEScanResultsEntryScanResponseData": lcosLXStatusLBSBLEScanResultsEntryScanResponseData,
       "lcosLXStatusLBSBLEScanResultsEntryManufacturer": lcosLXStatusLBSBLEScanResultsEntryManufacturer,
       "lcosLXStatusLBSBLEScanResultsEntryLocalNameType": lcosLXStatusLBSBLEScanResultsEntryLocalNameType,
       "lcosLXStatusLBSBLEScanResultsEntryASCIILocalName": lcosLXStatusLBSBLEScanResultsEntryASCIILocalName,
       "lcosLXStatusLBSCACertinfo": lcosLXStatusLBSCACertinfo,
       "lcosLXStatusAutomaticFirmwareUpdate": lcosLXStatusAutomaticFirmwareUpdate,
       "lcosLXStatusAutomaticFirmwareUpdateMode": lcosLXStatusAutomaticFirmwareUpdateMode,
       "lcosLXStatusAutomaticFirmwareUpdateLastCheck": lcosLXStatusAutomaticFirmwareUpdateLastCheck,
       "lcosLXStatusAutomaticFirmwareUpdateNextCheck": lcosLXStatusAutomaticFirmwareUpdateNextCheck,
       "lcosLXStatusAutomaticFirmwareUpdateUpdateCandidate": lcosLXStatusAutomaticFirmwareUpdateUpdateCandidate,
       "lcosLXStatusAutomaticFirmwareUpdateState": lcosLXStatusAutomaticFirmwareUpdateState,
       "lcosLXStatusAutomaticFirmwareUpdateCurrentAction": lcosLXStatusAutomaticFirmwareUpdateCurrentAction,
       "lcosLXStatusAutomaticFirmwareUpdateLastResult": lcosLXStatusAutomaticFirmwareUpdateLastResult,
       "lcosLXStatusAutomaticFirmwareUpdatePlannedInstallation": lcosLXStatusAutomaticFirmwareUpdatePlannedInstallation,
       "lcosLXStatusAutomaticFirmwareUpdateCurrentVersion": lcosLXStatusAutomaticFirmwareUpdateCurrentVersion,
       "lcosLXStatusAutomaticFirmwareUpdateLastCheckEpoch": lcosLXStatusAutomaticFirmwareUpdateLastCheckEpoch,
       "lcosLXStatusAutomaticFirmwareUpdateNextCheckEpoch": lcosLXStatusAutomaticFirmwareUpdateNextCheckEpoch,
       "lcosLXStatusAutomaticFirmwareUpdatePlannedInstallationEpoch": lcosLXStatusAutomaticFirmwareUpdatePlannedInstallationEpoch,
       "lcosLXStatusIoT": lcosLXStatusIoT,
       "lcosLXStatusIoTWirelessePaper": lcosLXStatusIoTWirelessePaper,
       "lcosLXStatusIoTWirelessePaperServerCAInfo": lcosLXStatusIoTWirelessePaperServerCAInfo,
       "lcosLXStatusIoTWirelessePaperAccessPointID": lcosLXStatusIoTWirelessePaperAccessPointID,
       "lcosLXStatusIoTWirelessePaperConnectedServer": lcosLXStatusIoTWirelessePaperConnectedServer,
       "lcosLXStatusIoTWirelessePaperCurrentChannel": lcosLXStatusIoTWirelessePaperCurrentChannel,
       "lcosLXStatusIoTWirelessePaperFirmwareVersion": lcosLXStatusIoTWirelessePaperFirmwareVersion,
       "lcosLXStatusIoTWirelessePaperClaimID": lcosLXStatusIoTWirelessePaperClaimID,
       "lcosLXSetup": lcosLXSetup,
       "lcosLXSetupName": lcosLXSetupName,
       "lcosLXSetupConfig": lcosLXSetupConfig,
       "lcosLXSetupConfigComment1": lcosLXSetupConfigComment1,
       "lcosLXSetupConfigComment2": lcosLXSetupConfigComment2,
       "lcosLXSetupConfigComment3": lcosLXSetupConfigComment3,
       "lcosLXSetupConfigComment4": lcosLXSetupConfigComment4,
       "lcosLXSetupConfigComment5": lcosLXSetupConfigComment5,
       "lcosLXSetupConfigComment6": lcosLXSetupConfigComment6,
       "lcosLXSetupConfigComment7": lcosLXSetupConfigComment7,
       "lcosLXSetupConfigComment8": lcosLXSetupConfigComment8,
       "lcosLXSetupConfigLocation": lcosLXSetupConfigLocation,
       "lcosLXSetupConfigAdministrator": lcosLXSetupConfigAdministrator,
       "lcosLXSetupConfigConfigAgingMinutes": lcosLXSetupConfigConfigAgingMinutes,
       "lcosLXSetupConfigLEDMode": lcosLXSetupConfigLEDMode,
       "lcosLXSetupConfigAdmins": lcosLXSetupConfigAdmins,
       "lcosLXSetupConfigAdminsEntry": lcosLXSetupConfigAdminsEntry,
       "lcosLXSetupConfigAdminsEntryAdministrator": lcosLXSetupConfigAdminsEntryAdministrator,
       "lcosLXSetupConfigAdminsEntryFunctionRights": lcosLXSetupConfigAdminsEntryFunctionRights,
       "lcosLXSetupConfigAdminsEntryRights": lcosLXSetupConfigAdminsEntryRights,
       "lcosLXSetupConfigAdminsEntryHashedPassword": lcosLXSetupConfigAdminsEntryHashedPassword,
       "lcosLXSetupConfigLEDOffSeconds": lcosLXSetupConfigLEDOffSeconds,
       "lcosLXSetupConfigLEDTest": lcosLXSetupConfigLEDTest,
       "lcosLXSetupConfigAllowSupportAccess": lcosLXSetupConfigAllowSupportAccess,
       "lcosLXSetupTime": lcosLXSetupTime,
       "lcosLXSetupTimeTimezone": lcosLXSetupTimeTimezone,
       "lcosLXSetupTimeNTP": lcosLXSetupTimeNTP,
       "lcosLXSetupTimeNTPOperating": lcosLXSetupTimeNTPOperating,
       "lcosLXSetupTimeNTPServer": lcosLXSetupTimeNTPServer,
       "lcosLXSetupTimeNTPServers": lcosLXSetupTimeNTPServers,
       "lcosLXSetupTimeNTPServersEntry": lcosLXSetupTimeNTPServersEntry,
       "lcosLXSetupTimeNTPServersEntryName": lcosLXSetupTimeNTPServersEntryName,
       "lcosLXSetupTimeNTPServersEntryActive": lcosLXSetupTimeNTPServersEntryActive,
       "lcosLXSetupWLAN": lcosLXSetupWLAN,
       "lcosLXSetupWLANNetwork": lcosLXSetupWLANNetwork,
       "lcosLXSetupWLANNetworkEntry": lcosLXSetupWLANNetworkEntry,
       "lcosLXSetupWLANNetworkEntryNetworkName": lcosLXSetupWLANNetworkEntryNetworkName,
       "lcosLXSetupWLANNetworkEntrySSIDName": lcosLXSetupWLANNetworkEntrySSIDName,
       "lcosLXSetupWLANNetworkEntryClosedNetwork": lcosLXSetupWLANNetworkEntryClosedNetwork,
       "lcosLXSetupWLANNetworkEntryMaxStations": lcosLXSetupWLANNetworkEntryMaxStations,
       "lcosLXSetupWLANNetworkEntryInterStationTraffic": lcosLXSetupWLANNetworkEntryInterStationTraffic,
       "lcosLXSetupWLANNetworkEntryMinClientStrength": lcosLXSetupWLANNetworkEntryMinClientStrength,
       "lcosLXSetupWLANNetworkEntryExcludeFromClientManagement": lcosLXSetupWLANNetworkEntryExcludeFromClientManagement,
       "lcosLXSetupWLANNetworkEntryTimeframe": lcosLXSetupWLANNetworkEntryTimeframe,
       "lcosLXSetupWLANNetworkEntryHotspot": lcosLXSetupWLANNetworkEntryHotspot,
       "lcosLXSetupWLANNetworkEntrySummaricTxLimitKbits": lcosLXSetupWLANNetworkEntrySummaricTxLimitKbits,
       "lcosLXSetupWLANNetworkEntrySummaricRxLimitKbits": lcosLXSetupWLANNetworkEntrySummaricRxLimitKbits,
       "lcosLXSetupWLANNetworkEntryBlockMulticast": lcosLXSetupWLANNetworkEntryBlockMulticast,
       "lcosLXSetupWLANNetworkEntryClientTxLimitKbits": lcosLXSetupWLANNetworkEntryClientTxLimitKbits,
       "lcosLXSetupWLANNetworkEntryClientRxLimitKbits": lcosLXSetupWLANNetworkEntryClientRxLimitKbits,
       "lcosLXSetupWLANNetworkEntryKey": lcosLXSetupWLANNetworkEntryKey,
       "lcosLXSetupWLANNetworkEntryRadios": lcosLXSetupWLANNetworkEntryRadios,
       "lcosLXSetupWLANNetworkEntryEncryptionProfile": lcosLXSetupWLANNetworkEntryEncryptionProfile,
       "lcosLXSetupWLANNetworkEntryIdleTimeout": lcosLXSetupWLANNetworkEntryIdleTimeout,
       "lcosLXSetupWLANNetworkEntryVLANID": lcosLXSetupWLANNetworkEntryVLANID,
       "lcosLXSetupWLANCountry": lcosLXSetupWLANCountry,
       "lcosLXSetupWLANEncryption": lcosLXSetupWLANEncryption,
       "lcosLXSetupWLANEncryptionEntry": lcosLXSetupWLANEncryptionEntry,
       "lcosLXSetupWLANEncryptionEntryProfileName": lcosLXSetupWLANEncryptionEntryProfileName,
       "lcosLXSetupWLANEncryptionEntryEncryption": lcosLXSetupWLANEncryptionEntryEncryption,
       "lcosLXSetupWLANEncryptionEntryMethod": lcosLXSetupWLANEncryptionEntryMethod,
       "lcosLXSetupWLANEncryptionEntryWPAVersion": lcosLXSetupWLANEncryptionEntryWPAVersion,
       "lcosLXSetupWLANEncryptionEntryWPARekeyingCycle": lcosLXSetupWLANEncryptionEntryWPARekeyingCycle,
       "lcosLXSetupWLANEncryptionEntryWPA1SessionKeytypes": lcosLXSetupWLANEncryptionEntryWPA1SessionKeytypes,
       "lcosLXSetupWLANEncryptionEntryWPA23SessionKeytypes": lcosLXSetupWLANEncryptionEntryWPA23SessionKeytypes,
       "lcosLXSetupWLANEncryptionEntryProtMgmtFrames": lcosLXSetupWLANEncryptionEntryProtMgmtFrames,
       "lcosLXSetupWLANEncryptionEntryPreAuthentication": lcosLXSetupWLANEncryptionEntryPreAuthentication,
       "lcosLXSetupWLANEncryptionEntryOKC": lcosLXSetupWLANEncryptionEntryOKC,
       "lcosLXSetupWLANEncryptionEntryWPA2KeyManagement": lcosLXSetupWLANEncryptionEntryWPA2KeyManagement,
       "lcosLXSetupWLANEncryptionEntryPMKIAPPSecret": lcosLXSetupWLANEncryptionEntryPMKIAPPSecret,
       "lcosLXSetupWLANEncryptionEntryRADIUSServerProfile": lcosLXSetupWLANEncryptionEntryRADIUSServerProfile,
       "lcosLXSetupWLANEncryptionEntrySAEOWEGroups": lcosLXSetupWLANEncryptionEntrySAEOWEGroups,
       "lcosLXSetupWLANMgmt": lcosLXSetupWLANMgmt,
       "lcosLXSetupWLANMgmtActiveProfile": lcosLXSetupWLANMgmtActiveProfile,
       "lcosLXSetupWLANMgmtProfiles": lcosLXSetupWLANMgmtProfiles,
       "lcosLXSetupWLANMgmtProfilesEntry": lcosLXSetupWLANMgmtProfilesEntry,
       "lcosLXSetupWLANMgmtProfilesEntryProfileName": lcosLXSetupWLANMgmtProfilesEntryProfileName,
       "lcosLXSetupWLANMgmtProfilesEntryOperating": lcosLXSetupWLANMgmtProfilesEntryOperating,
       "lcosLXSetupWLANMgmtProfilesEntrySteeringMinPHYSignal": lcosLXSetupWLANMgmtProfilesEntrySteeringMinPHYSignal,
       "lcosLXSetupWLANMgmtProfilesEntryUpgradeTXRateThreshold": lcosLXSetupWLANMgmtProfilesEntryUpgradeTXRateThreshold,
       "lcosLXSetupWLANMgmtProfilesEntryUpgradePHYSignalThreshold": lcosLXSetupWLANMgmtProfilesEntryUpgradePHYSignalThreshold,
       "lcosLXSetupWLANMgmtProfilesEntryDowngradeTXRateThreshold": lcosLXSetupWLANMgmtProfilesEntryDowngradeTXRateThreshold,
       "lcosLXSetupWLANMgmtProfilesEntryDowngradePHYSignalThreshold": lcosLXSetupWLANMgmtProfilesEntryDowngradePHYSignalThreshold,
       "lcosLXSetupWLANMgmtProfilesEntry24GHzSubProfile": lcosLXSetupWLANMgmtProfilesEntry24GHzSubProfile,
       "lcosLXSetupWLANMgmtProfilesEntry5GHzSubProfile": lcosLXSetupWLANMgmtProfilesEntry5GHzSubProfile,
       "lcosLXSetupWLANMgmt24GHz": lcosLXSetupWLANMgmt24GHz,
       "lcosLXSetupWLANMgmt24GHzEntry": lcosLXSetupWLANMgmt24GHzEntry,
       "lcosLXSetupWLANMgmt24GHzEntryProfileName": lcosLXSetupWLANMgmt24GHzEntryProfileName,
       "lcosLXSetupWLANMgmt24GHzEntryUtilizationCheckInterval": lcosLXSetupWLANMgmt24GHzEntryUtilizationCheckInterval,
       "lcosLXSetupWLANMgmt24GHzEntryUtilizationAveragePeriod": lcosLXSetupWLANMgmt24GHzEntryUtilizationAveragePeriod,
       "lcosLXSetupWLANMgmt24GHzEntryUtilizationOverloadThreshold": lcosLXSetupWLANMgmt24GHzEntryUtilizationOverloadThreshold,
       "lcosLXSetupWLANMgmt24GHzEntryUtilizationDeviationThreshold": lcosLXSetupWLANMgmt24GHzEntryUtilizationDeviationThreshold,
       "lcosLXSetupWLANMgmt24GHzEntryInterferenceDetection": lcosLXSetupWLANMgmt24GHzEntryInterferenceDetection,
       "lcosLXSetupWLANMgmt24GHzEntryDelayProbePHYSignalThreshold": lcosLXSetupWLANMgmt24GHzEntryDelayProbePHYSignalThreshold,
       "lcosLXSetupWLANMgmt24GHzEntryDelayProbeTimeWindow": lcosLXSetupWLANMgmt24GHzEntryDelayProbeTimeWindow,
       "lcosLXSetupWLANMgmt24GHzEntryDelayProbeMinRequestCount": lcosLXSetupWLANMgmt24GHzEntryDelayProbeMinRequestCount,
       "lcosLXSetupWLANMgmt5GHz": lcosLXSetupWLANMgmt5GHz,
       "lcosLXSetupWLANMgmt5GHzEntry": lcosLXSetupWLANMgmt5GHzEntry,
       "lcosLXSetupWLANMgmt5GHzEntryProfileName": lcosLXSetupWLANMgmt5GHzEntryProfileName,
       "lcosLXSetupWLANMgmt5GHzEntryUtilizationCheckInterval": lcosLXSetupWLANMgmt5GHzEntryUtilizationCheckInterval,
       "lcosLXSetupWLANMgmt5GHzEntryUtilizationAveragePeriod": lcosLXSetupWLANMgmt5GHzEntryUtilizationAveragePeriod,
       "lcosLXSetupWLANMgmt5GHzEntryUtilizationOverloadThreshold": lcosLXSetupWLANMgmt5GHzEntryUtilizationOverloadThreshold,
       "lcosLXSetupWLANMgmt5GHzEntryUtilizationDeviationThreshold": lcosLXSetupWLANMgmt5GHzEntryUtilizationDeviationThreshold,
       "lcosLXSetupWLANMgmt5GHzEntryInterferenceDetection": lcosLXSetupWLANMgmt5GHzEntryInterferenceDetection,
       "lcosLXSetupWLANRadioSettings": lcosLXSetupWLANRadioSettings,
       "lcosLXSetupWLANRadioSettingsEntry": lcosLXSetupWLANRadioSettingsEntry,
       "lcosLXSetupWLANRadioSettingsEntryIfc": lcosLXSetupWLANRadioSettingsEntryIfc,
       "lcosLXSetupWLANRadioSettingsEntry5GHzMode": lcosLXSetupWLANRadioSettingsEntry5GHzMode,
       "lcosLXSetupWLANRadioSettingsEntryRadioBand": lcosLXSetupWLANRadioSettingsEntryRadioBand,
       "lcosLXSetupWLANRadioSettingsEntrySubBand": lcosLXSetupWLANRadioSettingsEntrySubBand,
       "lcosLXSetupWLANRadioSettingsEntryChannel": lcosLXSetupWLANRadioSettingsEntryChannel,
       "lcosLXSetupWLANRadioSettingsEntry24GHzMode": lcosLXSetupWLANRadioSettingsEntry24GHzMode,
       "lcosLXSetupWLANRadioSettingsEntryAntennaGain": lcosLXSetupWLANRadioSettingsEntryAntennaGain,
       "lcosLXSetupWLANRadioSettingsEntryChannelList": lcosLXSetupWLANRadioSettingsEntryChannelList,
       "lcosLXSetupWLANRadioSettingsEntryMaxChannelBandwidth": lcosLXSetupWLANRadioSettingsEntryMaxChannelBandwidth,
       "lcosLXSetupWLANRadioSettingsEntryExcludeDFSChannels": lcosLXSetupWLANRadioSettingsEntryExcludeDFSChannels,
       "lcosLXSetupWLANRadioSettingsEntryPowerSetting": lcosLXSetupWLANRadioSettingsEntryPowerSetting,
       "lcosLXSetupWLANRadioSettingsEntryEIRP": lcosLXSetupWLANRadioSettingsEntryEIRP,
       "lcosLXSetupWLANAutomaticEnvironmentScanEnabled": lcosLXSetupWLANAutomaticEnvironmentScanEnabled,
       "lcosLXSetupWLANAutomaticEnvironmentScanTimeBegin": lcosLXSetupWLANAutomaticEnvironmentScanTimeBegin,
       "lcosLXSetupWLANAutomaticEnvironmentScanTimeEnd": lcosLXSetupWLANAutomaticEnvironmentScanTimeEnd,
       "lcosLXSetupWLANHotspot": lcosLXSetupWLANHotspot,
       "lcosLXSetupWLANHotspotHotspots": lcosLXSetupWLANHotspotHotspots,
       "lcosLXSetupWLANHotspotHotspotsEntry": lcosLXSetupWLANHotspotHotspotsEntry,
       "lcosLXSetupWLANHotspotHotspotsEntryName": lcosLXSetupWLANHotspotHotspotsEntryName,
       "lcosLXSetupWLANHotspotHotspotsEntryURL": lcosLXSetupWLANHotspotHotspotsEntryURL,
       "lcosLXSetupWLANHotspotHotspotsEntryRevisionID": lcosLXSetupWLANHotspotHotspotsEntryRevisionID,
       "lcosLXSetupWLANHotspotHotspotsEntryPrivateNetwork": lcosLXSetupWLANHotspotHotspotsEntryPrivateNetwork,
       "lcosLXSetupWLANHotspotHotspotsEntryDHCPRangeStart": lcosLXSetupWLANHotspotHotspotsEntryDHCPRangeStart,
       "lcosLXSetupWLANHotspotHotspotsEntryDHCPRangeEnd": lcosLXSetupWLANHotspotHotspotsEntryDHCPRangeEnd,
       "lcosLXSetupWLANLEPS": lcosLXSetupWLANLEPS,
       "lcosLXSetupWLANLEPSOperating": lcosLXSetupWLANLEPSOperating,
       "lcosLXSetupWLANLEPSProfiles": lcosLXSetupWLANLEPSProfiles,
       "lcosLXSetupWLANLEPSProfilesEntry": lcosLXSetupWLANLEPSProfilesEntry,
       "lcosLXSetupWLANLEPSProfilesEntryName": lcosLXSetupWLANLEPSProfilesEntryName,
       "lcosLXSetupWLANLEPSProfilesEntryNetworkName": lcosLXSetupWLANLEPSProfilesEntryNetworkName,
       "lcosLXSetupWLANLEPSProfilesEntryMACList": lcosLXSetupWLANLEPSProfilesEntryMACList,
       "lcosLXSetupWLANLEPSProfilesEntryVLAN": lcosLXSetupWLANLEPSProfilesEntryVLAN,
       "lcosLXSetupWLANLEPSUsers": lcosLXSetupWLANLEPSUsers,
       "lcosLXSetupWLANLEPSUsersEntry": lcosLXSetupWLANLEPSUsersEntry,
       "lcosLXSetupWLANLEPSUsersEntryName": lcosLXSetupWLANLEPSUsersEntryName,
       "lcosLXSetupWLANLEPSUsersEntryProfile": lcosLXSetupWLANLEPSUsersEntryProfile,
       "lcosLXSetupWLANLEPSUsersEntryWPAPassphrase": lcosLXSetupWLANLEPSUsersEntryWPAPassphrase,
       "lcosLXSetupWLANLEPSUsersEntryVLAN": lcosLXSetupWLANLEPSUsersEntryVLAN,
       "lcosLXSetupWLANLEPSUsersEntryMACAddress": lcosLXSetupWLANLEPSUsersEntryMACAddress,
       "lcosLXSetupWLANRateSelection": lcosLXSetupWLANRateSelection,
       "lcosLXSetupWLANRateSelectionEntry": lcosLXSetupWLANRateSelectionEntry,
       "lcosLXSetupWLANRateSelectionEntryNetworkName": lcosLXSetupWLANRateSelectionEntryNetworkName,
       "lcosLXSetupWLANRateSelectionEntryBroadcastRate": lcosLXSetupWLANRateSelectionEntryBroadcastRate,
       "lcosLXSetupWLANRateSelectionEntryMulticastRate": lcosLXSetupWLANRateSelectionEntryMulticastRate,
       "lcosLXSetupWLANRateSelectionEntryRadioband": lcosLXSetupWLANRateSelectionEntryRadioband,
       "lcosLXSetupSyslog": lcosLXSetupSyslog,
       "lcosLXSetupSyslogServer": lcosLXSetupSyslogServer,
       "lcosLXSetupSyslogServerEntry": lcosLXSetupSyslogServerEntry,
       "lcosLXSetupSyslogServerEntryName": lcosLXSetupSyslogServerEntryName,
       "lcosLXSetupSyslogServerEntryIPAddress": lcosLXSetupSyslogServerEntryIPAddress,
       "lcosLXSetupSyslogServerEntryPort": lcosLXSetupSyslogServerEntryPort,
       "lcosLXSetupSyslogServerEntryProtocol": lcosLXSetupSyslogServerEntryProtocol,
       "lcosLXSetupRADIUS": lcosLXSetupRADIUS,
       "lcosLXSetupRADIUSRADIUSServer": lcosLXSetupRADIUSRADIUSServer,
       "lcosLXSetupRADIUSRADIUSServerEntry": lcosLXSetupRADIUSRADIUSServerEntry,
       "lcosLXSetupRADIUSRADIUSServerEntryName": lcosLXSetupRADIUSRADIUSServerEntryName,
       "lcosLXSetupRADIUSRADIUSServerEntryPort": lcosLXSetupRADIUSRADIUSServerEntryPort,
       "lcosLXSetupRADIUSRADIUSServerEntrySecret": lcosLXSetupRADIUSRADIUSServerEntrySecret,
       "lcosLXSetupRADIUSRADIUSServerEntryBackup": lcosLXSetupRADIUSRADIUSServerEntryBackup,
       "lcosLXSetupRADIUSRADIUSServerEntryServerIPAddress": lcosLXSetupRADIUSRADIUSServerEntryServerIPAddress,
       "lcosLXSetupRADIUSRADIUSServerEntryAccountingPort": lcosLXSetupRADIUSRADIUSServerEntryAccountingPort,
       "lcosLXSetupRADIUSRADIUSServerEntryAccountingIPAddress": lcosLXSetupRADIUSRADIUSServerEntryAccountingIPAddress,
       "lcosLXSetupRADIUSRADIUSServerEntryMACCheck": lcosLXSetupRADIUSRADIUSServerEntryMACCheck,
       "lcosLXSetupRADIUSRADIUSServerEntryFallbackDynamicVLANID": lcosLXSetupRADIUSRADIUSServerEntryFallbackDynamicVLANID,
       "lcosLXSetupRADIUSSupplicantIfcSetup": lcosLXSetupRADIUSSupplicantIfcSetup,
       "lcosLXSetupRADIUSSupplicantIfcSetupEntry": lcosLXSetupRADIUSSupplicantIfcSetupEntry,
       "lcosLXSetupRADIUSSupplicantIfcSetupEntryInterfaceName": lcosLXSetupRADIUSSupplicantIfcSetupEntryInterfaceName,
       "lcosLXSetupRADIUSSupplicantIfcSetupEntryMethod": lcosLXSetupRADIUSSupplicantIfcSetupEntryMethod,
       "lcosLXSetupRADIUSSupplicantIfcSetupEntryUsername": lcosLXSetupRADIUSSupplicantIfcSetupEntryUsername,
       "lcosLXSetupRADIUSSupplicantIfcSetupEntryPassword": lcosLXSetupRADIUSSupplicantIfcSetupEntryPassword,
       "lcosLXSetupWLANManagement": lcosLXSetupWLANManagement,
       "lcosLXSetupWLANManagementStaticWLCConfiguration": lcosLXSetupWLANManagementStaticWLCConfiguration,
       "lcosLXSetupWLANManagementStaticWLCConfigurationEntry": lcosLXSetupWLANManagementStaticWLCConfigurationEntry,
       "lcosLXSetupWLANManagementStaticWLCConfigurationEntryIPAddress": lcosLXSetupWLANManagementStaticWLCConfigurationEntryIPAddress,
       "lcosLXSetupWLANManagementStaticWLCConfigurationEntryPort": lcosLXSetupWLANManagementStaticWLCConfigurationEntryPort,
       "lcosLXSetupWLANManagementOperating": lcosLXSetupWLANManagementOperating,
       "lcosLXSetupWLANManagementUpdateCertBefore": lcosLXSetupWLANManagementUpdateCertBefore,
       "lcosLXSetupWLANManagementCapwapPort": lcosLXSetupWLANManagementCapwapPort,
       "lcosLXSetupIPConfiguration": lcosLXSetupIPConfiguration,
       "lcosLXSetupIPConfigurationStaticParameters": lcosLXSetupIPConfigurationStaticParameters,
       "lcosLXSetupIPConfigurationStaticParametersEntry": lcosLXSetupIPConfigurationStaticParametersEntry,
       "lcosLXSetupIPConfigurationStaticParametersEntryInterfaceName": lcosLXSetupIPConfigurationStaticParametersEntryInterfaceName,
       "lcosLXSetupIPConfigurationStaticParametersEntryIPv4Gateway": lcosLXSetupIPConfigurationStaticParametersEntryIPv4Gateway,
       "lcosLXSetupIPConfigurationStaticParametersEntryIPv6Gateway": lcosLXSetupIPConfigurationStaticParametersEntryIPv6Gateway,
       "lcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv4DNS": lcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv4DNS,
       "lcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv4DNS": lcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv4DNS,
       "lcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv6DNS": lcosLXSetupIPConfigurationStaticParametersEntryPrimaryIPv6DNS,
       "lcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv6DNS": lcosLXSetupIPConfigurationStaticParametersEntrySecondaryIPv6DNS,
       "lcosLXSetupIPConfigurationLANInterfaces": lcosLXSetupIPConfigurationLANInterfaces,
       "lcosLXSetupIPConfigurationLANInterfacesEntry": lcosLXSetupIPConfigurationLANInterfacesEntry,
       "lcosLXSetupIPConfigurationLANInterfacesEntryInterfaceName": lcosLXSetupIPConfigurationLANInterfacesEntryInterfaceName,
       "lcosLXSetupIPConfigurationLANInterfacesEntryInterfaceID": lcosLXSetupIPConfigurationLANInterfacesEntryInterfaceID,
       "lcosLXSetupIPConfigurationLANInterfacesEntryVLANID": lcosLXSetupIPConfigurationLANInterfacesEntryVLANID,
       "lcosLXSetupIPConfigurationLANInterfacesEntryIPv4AddressSource": lcosLXSetupIPConfigurationLANInterfacesEntryIPv4AddressSource,
       "lcosLXSetupIPConfigurationLANInterfacesEntryIPv6AddressSource": lcosLXSetupIPConfigurationLANInterfacesEntryIPv6AddressSource,
       "lcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv4Address": lcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv4Address,
       "lcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv6Address": lcosLXSetupIPConfigurationLANInterfacesEntryStaticIPv6Address,
       "lcosLXSetupIPConfigurationLANInterfacesEntryComment": lcosLXSetupIPConfigurationLANInterfacesEntryComment,
       "lcosLXSetupLBS": lcosLXSetupLBS,
       "lcosLXSetupLBSHTTPServer": lcosLXSetupLBSHTTPServer,
       "lcosLXSetupLBSHTTPServerEntry": lcosLXSetupLBSHTTPServerEntry,
       "lcosLXSetupLBSHTTPServerEntryURL": lcosLXSetupLBSHTTPServerEntryURL,
       "lcosLXSetupLBSHTTPServerEntrySecret": lcosLXSetupLBSHTTPServerEntrySecret,
       "lcosLXSetupLBSHTTPServerEntryDataSources": lcosLXSetupLBSHTTPServerEntryDataSources,
       "lcosLXSetupLBSHTTPServerEntryBLEMeasurementsFields": lcosLXSetupLBSHTTPServerEntryBLEMeasurementsFields,
       "lcosLXSetupLBSHTTPServerEntryBufferingTimeout": lcosLXSetupLBSHTTPServerEntryBufferingTimeout,
       "lcosLXSetupLBSHTTPServerEntryBufferSize": lcosLXSetupLBSHTTPServerEntryBufferSize,
       "lcosLXSetupLBSOperating": lcosLXSetupLBSOperating,
       "lcosLXSetupLBSLBSServerType": lcosLXSetupLBSLBSServerType,
       "lcosLXSetupLBSBLEScanType": lcosLXSetupLBSBLEScanType,
       "lcosLXSetupLMC": lcosLXSetupLMC,
       "lcosLXSetupLMCOperating": lcosLXSetupLMCOperating,
       "lcosLXSetupLMCDHCPClientAutoRenew": lcosLXSetupLMCDHCPClientAutoRenew,
       "lcosLXSetupLMCConfigurationViaDHCP": lcosLXSetupLMCConfigurationViaDHCP,
       "lcosLXSetupLMCLMCDomain": lcosLXSetupLMCLMCDomain,
       "lcosLXSetupLMCRolloutProjectID": lcosLXSetupLMCRolloutProjectID,
       "lcosLXSetupLMCRolloutLocationID": lcosLXSetupLMCRolloutLocationID,
       "lcosLXSetupLMCRolloutDeviceRole": lcosLXSetupLMCRolloutDeviceRole,
       "lcosLXSetupLMCPairingToken": lcosLXSetupLMCPairingToken,
       "lcosLXSetupAutomaticFirmwareUpdate": lcosLXSetupAutomaticFirmwareUpdate,
       "lcosLXSetupAutomaticFirmwareUpdateMode": lcosLXSetupAutomaticFirmwareUpdateMode,
       "lcosLXSetupAutomaticFirmwareUpdateBaseURL": lcosLXSetupAutomaticFirmwareUpdateBaseURL,
       "lcosLXSetupAutomaticFirmwareUpdateCheckInterval": lcosLXSetupAutomaticFirmwareUpdateCheckInterval,
       "lcosLXSetupAutomaticFirmwareUpdateVersionPolicy": lcosLXSetupAutomaticFirmwareUpdateVersionPolicy,
       "lcosLXSetupAutomaticFirmwareUpdateCheckTimeBegin": lcosLXSetupAutomaticFirmwareUpdateCheckTimeBegin,
       "lcosLXSetupAutomaticFirmwareUpdateCheckTimeEnd": lcosLXSetupAutomaticFirmwareUpdateCheckTimeEnd,
       "lcosLXSetupAutomaticFirmwareUpdateInstallTimeBegin": lcosLXSetupAutomaticFirmwareUpdateInstallTimeBegin,
       "lcosLXSetupAutomaticFirmwareUpdateInstallTimeEnd": lcosLXSetupAutomaticFirmwareUpdateInstallTimeEnd,
       "lcosLXSetupIoT": lcosLXSetupIoT,
       "lcosLXSetupIoTWirelessePaper": lcosLXSetupIoTWirelessePaper,
       "lcosLXFirmware": lcosLXFirmware,
       "lcosLXFirmwareBootcount": lcosLXFirmwareBootcount,
       "lcosLXOther": lcosLXOther,
       "lcosLXProducts": lcosLXProducts,
       "lcosLXProductsAccessPoints": lcosLXProductsAccessPoints,
       "lcosLXProductsAccessPointsLW500": lcosLXProductsAccessPointsLW500,
       "lcosLXProductsAccessPointsLX6400": lcosLXProductsAccessPointsLX6400,
       "lcosLXProductsAccessPointsLX6402": lcosLXProductsAccessPointsLX6402,
       "lcosLXProductsAccessPointsLW600": lcosLXProductsAccessPointsLW600,
       "lcosLXProductsAccessPointsOW602": lcosLXProductsAccessPointsOW602,
       "lcosLXProductsAccessPointsLX6200E": lcosLXProductsAccessPointsLX6200E}
)
